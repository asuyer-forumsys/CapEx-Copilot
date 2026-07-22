#!/usr/bin/env python3
"""Ingest a document into the Pinecone corpus"""

import argparse
import os
import sys
import uuid
from dataclasses import asdict, dataclass
from pathlib import Path

# Try to import required modules. Abort if not installed
required_modules = ["numpy", "openai", "pinecone", "chonkie"]
try:
    import numpy as np
    from chonkie import OverlapRefinery, RecursiveChunker
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


class Chunker:
    def __init__(self, chunk_size_tokens: int = 2048):
        # Create markdown chunker
        self.chunker = RecursiveChunker.from_recipe(
            "markdown",
            lang="en",
            chunk_size=chunk_size_tokens,
        )

        # Create refiner
        self.refinery = OverlapRefinery(
            tokenizer="character",
            context_size=0.25,
            method="justified",
            merge=True,
        )

    def chunk(self, contents: str) -> list[str]:
        """
        Breaks `contents` into chunks
        """
        # Divide contents into chunks
        chunks = self.chunker.chunk(contents)

        # Add overlap between chunks
        refined = self.refinery.refine(chunks)

        return [c.text for c in refined]


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


class Ingester:
    def __init__(self, chunker: Chunker, embedder: Embedder, database: PineconeDB):
        self.chunker = chunker
        self.embedder = embedder
        self.database = database

    def ingest_document(self, path: Path, metadata: ChunkMetadata):
        """
        Chunks, embeds, and upserts a markdown document into the database.

        Args:
            path (Path): path to the markdown document
            metadata (ChunkMetadata): chunk metadata
        """
        # Read document contents
        with open(path, "r") as f:
            contents = f.read()

        # Compute remaining metadata
        word_count = len(contents.split())
        section_count = contents.count("## ")
        metadata.words = word_count
        metadata.sections = section_count

        # Break document down into chunks
        chunks = self.chunker.chunk(contents)

        # Create embedding for each chunk and insert into the database
        for idx, chunk in enumerate(chunks):
            embedding = self.embedder.create_embedding(chunk)
            self.database.upsert(embedding, chunk, idx, metadata)


def ingest(
    document: str,
    doc_id: str,
    doc_type: str,
    title: str,
    note: str,
):
    chunker = Chunker()
    embedder = Embedder()
    database = PineconeDB()
    ingester = Ingester(chunker, embedder, database)

    document_path = Path(document)
    if document_path.is_file() and document_path.suffix == ".md":
        metadata = ChunkMetadata(
            filename=document_path.name,
            doc_id=doc_id,
            doc_type=doc_type,
            title=title,
            words=0,  # computed later
            sections=0,  # computed later
            synthetic=False,
            note=note,
        )
        ingester.ingest_document(document_path, metadata)
    else:
        print(f"Cannot ingest {str(document_path)}. Document must be a '.md' file")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=(
            "Ingests documents by splitting them into chunks, creating vector embeddings for "
            "them, and upserting them into a Pinecone vector database"
        )
    )
    parser.add_argument("document", help="Path to document to ingest")
    parser.add_argument(
        "doc_id", help="An ID for the document, usually filename without extension"
    )
    parser.add_argument(
        "doc_type", help="The category of document (e.g., business_case)"
    )
    parser.add_argument(
        "title", help="Human readable document title, usually H1 in document"
    )
    parser.add_argument(
        "note", help="Note containing the key information about the document"
    )
    args = parser.parse_args()

    ingest(args.document, args.doc_id, args.doc_type, args.title, args.note)
    print("Document ingested")
