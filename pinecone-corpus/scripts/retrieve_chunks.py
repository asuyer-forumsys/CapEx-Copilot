#!/usr/bin/env python3
"""Retreive chunks from the Pinecone corpus using semantic similarity search"""

import sys
import argparse
import json
import os
import uuid
from dataclasses import asdict, dataclass

# Try to import required modules. Abort if not installed
required_modules = ["numpy", "openai", "pinecone"]
try:
    import numpy as np
    from openai import OpenAI
    from pinecone import DeletionProtection, Pinecone, ServerlessSpec
except ModuleNotFoundError:
    print(f"missing one or more of the required modules: {' '.join(required_modules)}")
    print("Install them using `pip install ...` or `python3 -m pip install ...`")
    sys.exit(1)

# List of required environment variables
required_envs = [
    "PINECONE_API_KEY",
    "PINECONE_EMBEDDING_MODEL",
    "PINECONE_NAMESPACE",
    "PINECONE_INDEX",
    "PINECONE_OPENAI_API_BASE",
    "PINECONE_OPENAI_API_KEY"
]

# Check for unset environment variables
for var in required_envs:
    if not os.getenv(var):
        print(f"Error: {var} is not set. Please set it and run again.")
        sys.exit(1)

# Load environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY") or ""
PINECONE_EMBEDDING_MODEL = os.getenv("PINECONE_EMBEDDING_MODEL") or ""
PINECONE_NAMESPACE = os.getenv("PINECONE_NAMESPACE") or ""
PINECONE_INDEX = os.getenv("PINECONE_INDEX") or ""
PINECONE_OPENAI_API_BASE = os.getenv("PINECONE_OPENAI_API_BASE") or ""
PINECONE_OPENAI_API_KEY = os.getenv("PINECONE_OPENAI_API_KEY") or ""


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
    def __init__(self):
        """
        Initializes a pinecone database index and namespace, creating them if they do
        not yet exist
        """
        pc = Pinecone(api_key=PINECONE_API_KEY)
        if not pc.has_index(PINECONE_INDEX):
            pc.indexes.create(
                name=PINECONE_INDEX,
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

        self.index = pc.index(PINECONE_INDEX)
        self.namespace_name = PINECONE_NAMESPACE

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


class Embedder:
    def __init__(self):
        """
        Constructs an OpenAI embedding client that uses the specified `model` for vector embeddings.
        """
        self.embedding_client = OpenAI(
            api_key=PINECONE_OPENAI_API_KEY,
            base_url=PINECONE_OPENAI_API_BASE,
        )
        self.model = PINECONE_EMBEDDING_MODEL

    def create_embedding(self, input: str) -> list[float]:
        """
        Creates a vector embedding of `input`
        """

        # Create embedding of input using the chosen model
        response = self.embedding_client.embeddings.create(
            input=input,
            model=self.model,
            encoding_format="float",
        )

        # Extract the raw embedding
        embedding = response.data[0].embedding

        # Convert to NumPy array for normalization
        emb_array = np.array(embedding, dtype=float)

        # Normalize: avoid operating directly on Pydantic object
        normed = emb_array / np.linalg.norm(emb_array)

        return normed.tolist()


class Retriever:
    def __init__(self, embedder: Embedder, database: PineconeDB):
        self.embedder = embedder
        self.database = database

    def retrieve_chunks(self, query: str, top_k: int = 3) -> list[MatchedChunk]:
        """
        Retrieves the `top_k` most relevant chunks for the `query`.
        """
        embedding = self.embedder.create_embedding(query)
        return self.database.query(embedding, top_k)


def retrieve(
    query: str,
    top_k: int,
) -> list[dict]:
    embedder = Embedder()
    database = PineconeDB()

    # print("Retrieving chunks...")
    retriever = Retriever(embedder, database)
    chunks = retriever.retrieve_chunks(query, top_k)
    # print()

    results = [
        {"text": c.text, "source": c.filename, "score": c.similarity_score}
        for c in chunks
    ]
    return results



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Document ingester")
    parser.add_argument("query")
    parser.add_argument("top_k", type=int, help="Number of chunks to return")
    args = parser.parse_args()

    results = retrieve(args.query, args.top_k)
    print(json.dumps({"results": results}))
