#
# Copyright (C) 2026
# Created by asuyer-forum, asuyer@forumsys.com
#

from ..embedder import Embedder
from ..pineconedb import MatchedChunk, PineconeDB


class Retriever:
    def __init__(self, embedder: Embedder, database: PineconeDB):
        self.embedder = embedder
        self.database = database

    def retrieve_chunks(self, query: str, top_k: int = 3) -> list[MatchedChunk]:
        """
        Retrieves the `top_k` most relevant chunks for the `query`
        """
        embedding = self.embedder.create_embedding(query)
        return self.database.query(embedding, top_k)
