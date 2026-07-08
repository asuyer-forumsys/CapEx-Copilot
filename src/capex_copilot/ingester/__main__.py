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
    database = PineconeDB("corpus", "all-files")

    ingester = Ingester(chunker, embedder, database)

    metadata_path = Path("corpus/_manifest.json")
    corpus_dir = Path("corpus")
    for file_path in corpus_dir.iterdir():
        if file_path.is_file() and file_path.suffix == ".md":
            print(f"Ingesting {file_path.name}")
            ingester.ingest_document(file_path, metadata_path)


if __name__ == "__main__":
    main()
