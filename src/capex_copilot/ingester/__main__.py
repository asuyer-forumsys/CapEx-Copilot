#
# Copyright (C) 2026
# Created by asuyer-forum, asuyer@forumsys.com
#

from pathlib import Path
import argparse
from . import Ingester, Chunker, Embedder, PineconeDB


def main():
    print("Beginning ingestion process")

    chunker = Chunker()
    embedder = Embedder("Qwen/Qwen3-Embedding-8B")
    database = PineconeDB("corpus", "all-files")

    ingester = Ingester(chunker, embedder, database)

    metadata_path = Path("corpus/_manifest.json")
    corpus_dir = Path("corpus")
    for file_path in corpus_dir.iterdir():
        if file_path.is_file() and file_path.suffix == ".md":
            print(f"Ingesting {file_path.name}")
            ingester.ingest_document(file_path, metadata_path)


def ingest(
    index: str,
    namespace: str,
    document: str,
    metadata: str,
    model: str = "Qwen/Qwen3-Embedding-8B",
):
    chunker = Chunker()
    embedder = Embedder(model)
    database = PineconeDB(index, namespace)

    ingester = Ingester(chunker, embedder, database)

    metadata_path = Path(metadata)
    document_path = Path(document)
    if document_path.is_dir():
        for file_path in document_path.iterdir():
            if file_path.is_file() and file_path.suffix == ".md":
                print(f"Ingesting {file_path.name}")
                ingester.ingest_document(file_path, metadata_path)
    else:
        print(f"Ingesting {document_path.name}")
        ingester.ingest_document(document_path, metadata_path)

    print("Done")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Document ingester")

    parser.add_argument("index", help="Pinecone index")
    parser.add_argument("namespace", help="Pinecone namespace within index")
    parser.add_argument(
        "document",
        help="Path to document to injest or to directory containing all documents to injest",
    )
    parser.add_argument("metadata", help="Path to metadata document")

    parser.add_argument(
        "-m",
        "--model",
        type=str,
        default="Qwen/Qwen3-Embedding-8B",
        help="Path to metadata document",
    )

    args = parser.parse_args()

    ingest(args.index, args.namespace, args.document, args.metadata, args.model)


