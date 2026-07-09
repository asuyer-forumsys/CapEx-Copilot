#
# Copyright (C) 2026
# Created by asuyer-forum, asuyer@forumsys.com
#

from chonkie import RecursiveChunker, OverlapRefinery


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
