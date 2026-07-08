#
# Copyright (C) 2026
# Created by asuyer-forum, asuyer@forumsys.com
#

from dataclasses import dataclass, asdict
import os
from pinecone import Pinecone, ServerlessSpec, DeletionProtection
import uuid

# Load environment variables
import dotenv

dotenv.load_dotenv(dotenv.find_dotenv(".env"))


@dataclass
class ChunkMetadata:
    filename: str
    doc_id: str
    doc_type: str
    title: str
    # initiative: str
    # as_of_date: str
    # fiscal_period: str
    words: int
    sections: int
    synthetic: bool
    note: str


@dataclass
class MatchedChunk:
    text: str
    filename: str
    similarity_score: float


class PineconeDB:
    def __init__(self, index_name: str, namespace_name: str):
        """
        Initializes a pinecone database index and namespace, creating them if they do
        not yet exist
        """
        pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        if not pc.has_index(index_name):
            pc.indexes.create(
                name=index_name,
                vector_type="dense",
                dimension=4096,
                metric="dotproduct",
                spec=ServerlessSpec(
                    cloud="aws",
                    region="us-east-1",
                ),
                deletion_protection=DeletionProtection.DISABLED,
                tags={
                    "environment": "development",
                },
            )

        self.index = pc.index(index_name)
        self.namespace_name = namespace_name

    def upsert(
        self, vector: list[float], text: str, chunk_index: int, metadata: ChunkMetadata
    ):
        """
        Inserts a vector embedding `vector` into the chosen index namespace with
        associated `metadata`
        """
        self.index.upsert(
            namespace=self.namespace_name,
            vectors=[
                {
                    "id": f"vec-{uuid.uuid4()}",
                    "values": vector,
                    "metadata": {
                        "text": text,
                        "chunk_index": chunk_index,
                        **asdict(metadata),
                    },
                }
            ],
        )

    def query(self, vector: list[float], top_k: int) -> list[MatchedChunk]:
        """
        Query the database for chunks most similar to the vector encoded chunk `vector`
        """
        response = self.index.query(
            namespace=self.namespace_name,
            vector=vector,
            top_k=top_k,
            include_values=False,
            include_metadata=True,
        )

        # Extract chunk content, filename, and similarity score
        matched_chunks = []
        for match in response.matches:
            matched_chunks.append(
                MatchedChunk(
                    text=match.metadata.get("text"),
                    filename=match.metadata.get("filename"),
                    similarity_score=match.score,
                )
            )

        return matched_chunks
