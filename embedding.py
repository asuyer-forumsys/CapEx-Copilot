
import dspy, json
from typing import Literal, Tuple, List
from openai import OpenAI
from httpx import Client, Limits
import numpy as np

embedding_client = OpenAI(
    api_key="EMPTY",  # OpenAI-compatible dummy key
    base_url="http://lambda3.quantumgears.com:18005/v1"
)


def get_query_embedding_llm(query: str) -> list:
    """
    Generate embedding for a single query using Qwen3 hosted on vLLM.

    Args:
        query (str): Input query string.

    Returns:
        List[float]: Embedding vector.
    """
    try:
        response = embedding_client.embeddings.create(
            input=query,
            model="Qwen/Qwen3-Embedding-8B",
            encoding_format="float"
        )
        # Extract the raw embedding
        embedding = response.data[0].embedding  # Correct attribute access

        # Convert to NumPy array for normalization
        emb_array = np.array(embedding, dtype=float)

        # Normalize: avoid operating directly on Pydantic object
        normed = emb_array / np.linalg.norm(emb_array)

        return normed.tolist()

    except Exception as e:
        print(f"❌ Failed to get embedding: {e}")
        return []


