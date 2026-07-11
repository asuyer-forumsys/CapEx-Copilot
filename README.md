# CapEx Copilot

CapEx Copilot is a planned RAG project for reviewing enterprise technology investment business
cases. The corpus follows a fictional mid-size retailer, **Copperline Retail Group, Inc.**, through
its Tech Investment Steering Committee's portfolio of 7 technology initiatives — proposal, vendor
selection, approval, go-live, and post-implementation review — including a business case that gets
revised after scope creep (ERP) and two that get deferred/rejected (WMS, AI chatbot).

**Status:** data-only. This is the synthetic source corpus, built ahead of the lab guide PDF,
`src/`, and reference tests — none of that exists yet.

## What's in `data/corpus/`

19 long, fully synthetic Markdown documents (~2,140 words average — noticeably longer than
Research Desk's ~200-word and Analyst Copilot's ~380-word documents) across ten categories:

- **`policy__*.md`** — the internal business case review policy and template guide.
- **`case__*.md`** — seven full business cases, one per technology initiative (cloud migration,
  omnichannel POS, customer data platform, cybersecurity, ERP replacement, WMS + robotics, AI
  chatbot).
- **`vendor__*.md`** — two vendor evaluation scorecards (ERP finalists, WMS/robotics finalists).
- **`minutes__*.md`** — two steering committee meeting minutes (Q1 and Q3 2026).
- **`memo__*.md`** — the CFO's FY2027 portfolio prioritization memo.
- **`review__*.md`** — two post-implementation reviews (Cloud Migration at 12 months, POS at 6
  months), reporting real actual-vs-projected variance against their original business cases.
- **`audit__*.md`** — an internal audit risk memo across the portfolio.
- **`addendum__*.md`** — a change request that deliberately revises the ERP case's cost, timeline,
  NPV, and IRR after a scope-creep discovery.
- **`glossary__*.md`** — the company's NPV/IRR/payback/TCO methodology reference.
- **`tracker__*.md`** — a portfolio-wide benefits realization tracker.

`_manifest.json` in the same folder provides metadata (doc type, initiative, as-of date, word
count, and `supersedes`/`superseded_by` links) for every document, including explicit notes on the
intentional cross-document contradictions and variances built into the corpus on purpose — e.g. the
ERP case and its addendum carry deliberately different numbers, and the two post-implementation
reviews carry deliberately different numbers than their tracker/minutes follow-ups — to give a RAG
system real version-reconciliation and compare-across-documents exercises.

All content is entirely fictional. No real company, person, or vendor is represented.

Do not modify these files.

## Modules

- `ingester`: document ingestion
    - Breaks documents down into chunks
    - Generates vector embeddings for each chunk
    - Inserts vector embeddings into Pinecone vector database

- `retriever`: chunk retriever
    - Retrieves chunks that are semantically similar to a query

- `agent`: (do not use)

## Installing Hermes plugin

First, install the `capex_copilot` package in the Hermes agent environment. From within 
the root of this project, run:

```sh
~/.hermes/hermes-agent/venv/bin/pip install .
```

Next, copy the `src/capex_copilot/rag-retrieve` directory to `.hermes/plugins`.

Now, enable the plugin by running `hermes plugins enable rag-retrieve`

Now, start the Hermes agent with the following command to test it with only the RAG tool
available:

```sh
hermes chat --toolset "rag-retrieve"
```


## Installing OpenClaw plugin

Enter into the `openclaw-rag-retrieve` directory and run the following commands:

```sh
npm run plugin:build
npm run plugin:validate
```

Then, `cd` back into this project root directory and make OpenClaw install the plugin:

```sh
cd ..       # into CapEx-Copilot/
openclaw plugins install ./openclaw-rag-retrieve --force
```

Verify the install by running the following command:

```sh
openclaw plugins inspect openclaw-rag-retrieve --runtime
```

It should show `Status: loaded` and list `rag_retrieve` under `Tools`.

**Important**: In order for the `rag_retrieve` tool to be accessible to the agent, you
must be using the `full` tool profile. Be sure you have the following in
`~/.openclaw/opencclaw.json`:

```json
"tools": {
    "profile": "full"
}
```

In an OpenClaw chat, you can verify that the tool is accessible by running `/tools compact` 
and check if `rag_retrive` appears under "Connected tools."

