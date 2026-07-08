#
# Copyright (C) 2026
# Created by asuyer-forum, asuyer@forumsys.com
#

from pathlib import Path
from . import Ingester, Chunker, Embedder, PineconeDB


def main():
    print("Beginning ingestion process")

    chunker = Chunker()
    embedder = Embedder("Qwen/Qwen3-Embedding-8B")
    database = PineconeDB("corpus", "test-4")

    ingester = Ingester(chunker, embedder, database)

    document_path = Path("corpus/case__ai_customer_service_chatbot.md")
    metadata_path = Path("corpus/_manifest.json")

    print("Ingesting")
    ingester.ingest_document(document_path, metadata_path)
    print("Done")


if __name__ == "__main__":
    main()
