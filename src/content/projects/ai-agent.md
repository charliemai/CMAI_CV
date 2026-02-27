---
title: "RAG Troubleshooting GPT Assistant"
description: "A self-built AI assistant that indexes my technical docs/runbooks/logs for semantic troubleshooting and faster incident resolution."
updatedDate: "Feb 27 2026"
heroImage: "/project_cmai_troubleshooting_system.png"
badge: "AI"
url: "https://troubleshooting-system.onrender.com/"
demo: "/lab#rag-troubleshooting"
tech:
  - Python
  - FastAPI
  - OpenAI API
  - Vector DB (Pinecone)
  - AWS Lambda (ingestion / embedding jobs)
  - Document pipelines
highlights:
  - "RAG over personal/internal knowledge: ingest docs → chunk → embed → retrieve → answer with citations/context."
  - "Designed a memory loop to continuously improve answers from feedback and new documents."
  - "Built as a practical troubleshooting copilot for real production workflows (cloud + DevOps)."
metrics:
  - "Reduced time-to-context-switch during investigations by making domain knowledge searchable and explainable."
  - "Reusable architecture for other domains (e.g., video transcription, argument analysis)."
tags:
  - RAG
  - LLM
  - DevOps
---

## Why I built it

In cloud support and DevOps work, the hardest part is rarely the command you run—it's **finding the right context**:
runbooks, postmortems, internal docs, logs, diagrams, and past cases.

This project turns that scattered knowledge into a searchable, conversational assistant.

## How it works (simplified)

1. **Ingestion**: documents/logs/design specs are collected and normalized
2. **Chunking + Embeddings**: text is split and embedded into a vector database
3. **Retrieval**: relevant chunks are retrieved based on semantic similarity
4. **Answering (RAG)**: LLM generates an answer grounded in retrieved context
5. **Memory loop**: feedback and new knowledge improve future responses

## Demo

- External demo: the hosted app (link above)
- Portfolio demo: a lightweight "prototype UI" in the **Lab** page

## Related writing

I documented the motivation and design decisions in my blog posts on this site.
