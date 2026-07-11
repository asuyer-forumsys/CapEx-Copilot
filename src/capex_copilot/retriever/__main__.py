#
# Copyright (C) 2026
# Created by asuyer-forum, asuyer@forumsys.com
#

# import textwrap
import json
import argparse
from . import Retriever, Embedder, PineconeDB
from colorama import Fore, init

init(autoreset=True)  # Reset print style after each print


def retrieve(
    query: str,
    top_k: int,
    index: str = "corpus",
    namespace: str = "all-files-with-overlap",
    model: str = "Qwen/Qwen3-Embedding-8B",
):
    embedder = Embedder(model)
    database = PineconeDB(index, namespace)

    # print("Retrieving chunks...")
    retriever = Retriever(embedder, database)
    chunks = retriever.retrieve_chunks(query, top_k)
    # print()

    results = [
        {"text": c.text, "source": c.filename, "score": c.similarity_score}
        for c in chunks
    ]
    print(json.dumps({"results": results}))

    # Print each of the retrieved chunks
    # for i, chunk in enumerate(chunks):
    #     print(f"Chunk #{i} from ", end="")
    #     print(str(Fore.RED) + f"{chunk.filename}")
    #     print(f"Similarity score: {chunk.similarity_score}")
    #     print("-" * 80)
    #     formatted_text = "\n".join(
    #         [textwrap.fill(line, width=80) for line in chunk.text.splitlines()]
    #     )
    #     print(formatted_text)
    #     print()
    #
    # print("Done")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Document ingester")

    # parser.add_argument("index", help="Pinecone index")
    # parser.add_argument("namespace", help="Pinecone namespace within index")
    parser.add_argument("query")
    parser.add_argument("top_k", type=int, help="Number of chunks to return")

    # parser.add_argument(
    #     "-m",
    #     "--model",
    #     type=str,
    #     default="Qwen/Qwen3-Embedding-8B",
    #     help="Path to metadata document",
    # )
    #
    args = parser.parse_args()

    retrieve(args.query, args.top_k)
