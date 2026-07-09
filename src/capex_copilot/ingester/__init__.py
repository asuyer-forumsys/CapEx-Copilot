#
# Copyright (C) 2026
# Created by asuyer-forum, asuyer@forumsys.com
#

"""
The ingester module handles ingestion of documents into the database. It spits the
documents into chunks, creates vector embeddings for them, and upserts them into a
Pinecone vector database. The chunk content is stored in the metadata of the vector in the
database.
"""

from .document_ingester import Ingester
from ..chunker import Chunker
from ..embedder import Embedder
from ..pineconedb import PineconeDB, ChunkMetadata

__all__ = [
    Ingester,
    Chunker,
    Embedder,
    PineconeDB,
    ChunkMetadata,
]

