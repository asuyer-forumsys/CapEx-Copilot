#
# Copyright (C) 2026
# Created by asuyer-forum, asuyer@forumsys.com
#

from chonkie import RecursiveChunker


class Chunker:
    def __init__(self, chunk_size_tokens: int = 2048):
        self.chunker = RecursiveChunker.from_recipe(
            "markdown", lang="en", chunk_size=chunk_size_tokens, 
        )

    def chunk(self, contents: str) -> list[str]:
        """
        Breaks `contents` into chunks
        """
        chunks = self.chunker.chunk(contents)
        return [c.text for c in chunks]
