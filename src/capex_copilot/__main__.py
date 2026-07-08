#
# Copyright (C) 2026
# Created by asuyer-forum, asuyer@forumsys.com
#

from .ingester import Ingester
from .ingester import Chunker
from .ingester import Embedder
from .ingester import PineconeDB


def main():
    print("Hello from CapEx-Copilot")

    chunker = Chunker()
    embedder = Embedder("Qwen/Qwen3-Embedding-8B")
    database = PineconeDB("corpus", "test-1")

    # injester = Ingester(
    #     chunker=Chunker(),
    #     embedder=Embedder(),
    #     database=PineconeDB(),
    # )
    #
    # injester.injest_document(path_to_document)


def chunker_only():
    filepath = "corpus/case__ai_customer_service_chatbot.md"
    with open(filepath, "r") as f:
        contents = f.read()

    chunker = Chunker()
    chunks = chunker.chunk(contents)

    for i, chunk in enumerate(chunks):
        print(f"-- Chunk {i} --")
        print(chunk)
        print()


def embed_first_chunk():
    filepath = "corpus/case__ai_customer_service_chatbot.md"
    with open(filepath, "r") as f:
        contents = f.read()

    chunker = Chunker()
    chunks = chunker.chunk(contents)
    first_chunk = chunks[0]

    embedder = Embedder("Qwen/Qwen3-Embedding-8B")
    embedding = embedder.create_embedding(first_chunk)

    print("-- Chunk 1 --")
    print(first_chunk)
    print()
    print("Embedding dimension:", len(embedding))
    print("Embedding:")
    print(embedding)


def injest_first_chunk():
    filepath = "corpus/case__ai_customer_service_chatbot.md"
    with open(filepath, "r") as f:
        contents = f.read()

    chunker = Chunker()
    chunks = chunker.chunk(contents)
    first_chunk = chunks[1]

    embedder = Embedder("Qwen/Qwen3-Embedding-8B")
    embedding = embedder.create_embedding(first_chunk)

    meta = {
        "title": "case__ai_customer_service_chatbot.md",
    }

    print("Creating database index and namespace")
    database = PineconeDB("corpus", "test-1")
    print("Inserting embedding")
    database.upsert(embedding, meta)
    print("Embedding inserted")


if __name__ == "__main__":
    chunker_only()
