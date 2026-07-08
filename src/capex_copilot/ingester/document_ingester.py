#
# Copyright (C) 2026
# Created by asuyer-forum, asuyer@forumsys.com
#

import json
from typing import Any
from pathlib import Path

from .chunker import Chunker
from .embedder import Embedder
from .pineconedb import PineconeDB, ChunkMetadata


class Ingester:
    def __init__(self, chunker: Chunker, embedder: Embedder, database: PineconeDB):
        self.chunker = chunker
        self.embedder = embedder
        self.database = database

    def ingest_document(self, path: Path, metadata_path: Path):
        """
        Chunks, embeds, and ingests a markdown document into the database.

        Args:
            path (Path): path to the markdown document
            metadata_path (Path): path to json document containing document metadata
        """
        # Read document contents
        with open(path, "r") as f:
            contents = f.read()

        # Read document metadata
        with open(metadata_path, "r") as f:
            all_metadata = json.load(f)

        # Get the metadata for this document
        for meta in all_metadata:
            if meta.get("file") == path.name:
                metadata = ChunkMetadata(
                    filename=meta.get("file", ""),
                    doc_id=meta.get("doc_id", ""),
                    doc_type=meta.get("doc_type", ""),
                    title=meta.get("title", ""),
                    # initiative=meta.get("initiative", ""),
                    # as_of_date=meta.get("as_of_date", ""),
                    # fiscal_period=meta.get("fiscal_period", ""),
                    words=meta.get("words", 0),
                    sections=meta.get("sections", 0),
                    synthetic=meta.get("synthetic", False),
                    note=meta.get("note", ""),
                )

        # Break document down into chunks
        chunks = self.chunker.chunk(contents)

        # Create embedding for each chunk and insert into the database
        for idx, chunk in enumerate(chunks):
            embedding = self.embedder.create_embedding(chunk)
            self.database.upsert(embedding, chunk, idx, metadata)
