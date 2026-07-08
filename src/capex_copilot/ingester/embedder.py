#
# Copyright (C) 2026
# Created by asuyer-forum, asuyer@forumsys.com
#

from openai import OpenAI
import numpy as np


class Embedder:
    def __init__(self, model: str):
        """
        Constructs an OpenAI embedding client that uses the specified `model` for vector embeddings.
        """
        self.embedding_client = OpenAI(
            api_key="EMPTY",  # OpenAI-compatible dummy key
            base_url="http://lambda3.quantumgears.com:18005/v1",
        )
        self.model = model

    def create_embedding(self, input: str) -> list[float]:
        """
        Creates a vector embedding of `input`
        """

        # Create embedding of input using the chosen model
        response = self.embedding_client.embeddings.create(
            input=input,
            model=self.model,
            encoding_format="float",
        )

        # Extract the raw embedding
        embedding = response.data[0].embedding

        # Convert to NumPy array for normalization
        emb_array = np.array(embedding, dtype=float)

        # Normalize: avoid operating directly on Pydantic object
        normed = emb_array / np.linalg.norm(emb_array)

        return normed.tolist()
