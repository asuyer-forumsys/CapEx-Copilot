#
# Copyright (C) 2026
# Created by asuyer-forum, asuyer@forumsys.com
#

"""
The retriever module handles retrieval of document chunks that are relevant to a query. It
takes a query, creates a vector embedding from it, and uses that to query the Pinecone
vector database. The top matching chunks are returned.
"""


from .retriever import Retriever
from ..embedder import Embedder
from ..pineconedb import PineconeDB, ChunkMetadata

__all__ = [
    Retriever,
    Embedder,
    PineconeDB,
    ChunkMetadata,
]

