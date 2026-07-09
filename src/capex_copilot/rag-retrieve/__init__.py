#
# Copyright (C) 2026
# Created by asuyer-forum, asuyer@forumsys.com
#


import json
from capex_copilot.retriever import Retriever, Embedder, PineconeDB

_EMBEDDDER_MODEL = "Qwen/Qwen3-Embedding-8B"
_PINECONE_INDEX = "corpus"
_PINECONE_NAMESPACE = "all-files-with-overlap"

RAG_RETRIEVE_SCHEMA = {
    "name": "rag_retrieve",
    "description": "Search the knowledge base for chunks relevant to a query. Use this before answering questions that depend on indexed documents.",
    "parameters": {
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "The search query"},
            "top_k": {
                "type": "integer",
                "description": "Number of chunks to return",
                "default": 3,
            },
        },
        "required": ["query"],
    },
}


def rag_retrieve_handler(args, **kwargs):
    del kwargs
    try:
        embedder = Embedder(_EMBEDDDER_MODEL)
        database = PineconeDB(_PINECONE_INDEX, _PINECONE_NAMESPACE)
        retriever = Retriever(embedder, database)
        chunks = retriever.retrieve_chunks(
            args.get("query", ""), top_k=args.get("top_k", 3)
        )
        results = [
            {"text": c.text, "source": c.filename, "score": c.similarity_score}
            for c in chunks
        ]
        return json.dumps({"results": results})
    except Exception as e:
        return json.dumps({"error": str(e)})


def register(ctx):
    ctx.register_tool(
        name="rag_retrieve",
        toolset="rag_retrieve",
        schema=RAG_RETRIEVE_SCHEMA,
        handler=rag_retrieve_handler,
    )
