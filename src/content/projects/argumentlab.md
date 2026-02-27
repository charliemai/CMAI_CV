---
title: "ArgumentLab"
description: "A YouTube-to-VectorDB pipeline for exploring political ideas: summarize videos, extract claims, embed into a vector DB, and chat to compare viewpoints + map my own reasoning over time."
updatedDate: "Feb 27 2026"
heroImage: "/project_argumentlab.png"
badge: "AI Lab"
demo: "/lab#argumentlab"
tech:
  - YouTube transcript ingestion
  - Embeddings + Vector DB
  - RAG / LLM reasoning
  - Frontend chat UI
highlights:
  - "Turns scattered political videos into a structured, searchable knowledge base."
  - "Interactive chat experience for comparing arguments and generating counterpoints."
  - "Personal stance mapping: builds a trace of how my thinking evolves across topics."
metrics:
  - "Designed for reflective thinking and constructive dialogue (not just 'hot takes')."
tags:
  - RAG
  - KnowledgeGraph
  - UX
---

## What it is

**ArgumentLab** is my experiment in *knowledge + reasoning UX*.

Instead of bookmarking countless YouTube videos, I wanted a system that:

- Extracts the core arguments
- Stores them as searchable knowledge
- Helps me explore **both sides**
- Produces a **personal reasoning trace** (how my opinions form and change)

## High-level pipeline

1. Collect a YouTube URL
2. Pull transcript / metadata
3. Summarize + extract claims / evidence / assumptions
4. Embed into a vector DB
5. Frontend: chat + argument comparison + stance timeline

## Demo

See the interactive prototype on the **Lab** page.
