---
name: pinecone-corpus
description: >-
  Ingest and retrieve documents from the Pinecone vector database corpus
---

# Pinecone Corpus

The Pinecone corpus contains documents that can be retrieved using semantic similarity search. This skill provides scripts for querying the database for relevant chunks and ingesting new documents into the database.

## Prerequisites

The following environment variables *MUST* be set by the user:
- PINECONE_API_KEY
- PINECONE_EMBEDDING_MODEL
- PINECONE_NAMESPACE
- PINECONE_INDEX
- PINECONE_OPENAI_API_BASE
- PINECONE_OPENAI_API_KEY

The scripts will fail if one or more of these variables is not set. Make sure the user sets these variables before running the scripts.

Additionally, you require python version >3.9 and the following external python modules:
- `numpy`
- `openai`
- `pinecone`
- `chonkie`

## Document chunk retrieval

Use the `retrieve_chunks.py` script to retrieve relevant chunks from the Pinecone corpus whenever the user mentions needing information from:
- Pinecone
- Corpus
- Vector database
- CapEx-Copilot

Invoke the script as follows:

```sh
scripts/retrieve_chunks.py <query> <top_k>
```

Args:
- `<query>`: query to use for semantic similarity search.
- `<top_k>`: number of chunks to retrieve.

Prints a JSON string with key `results` that contains a list of chunk results, each containing:
- `text`: text from the chunk
- `source`: name of the source file
- `score`: semantic similarity score

Example:

```sh
scripts/retrieve_chunks.py "What are the required sections in a business case review" 3
```

## Document ingestion

Use the `ingest_document.py` script to ingest a document into the Pinecone corpus upon the user's request.

Invoke the script as follows:

```sh
scripts/ingest_document.py <document> <doc_id> <doc_type> <title> <note>
```

Args:
- `<document>`: path to the markdown document to ingest.
- `<doc_id>`: An ID for the document, usually filename without extension.
- `<doc_type>`: The category of document (e.g., business_case).
- `<title>`: Human readable document title, usually H1 in document.
- `<note>`: Note containing the key information about the document.

On success, the script prints "Document ingested".

Example:

```sh
scripts/ingest_document.py corpus/policy__business_case_review_and_template_guide.md "policy__business_case_review_and_template_guide" "policy" "Business Case Review and Template Guide" "Standing governance policy defining the 7-section business case template, approval thresholds, and disposition vocabulary used consistently across every other document in this corpus."
```

