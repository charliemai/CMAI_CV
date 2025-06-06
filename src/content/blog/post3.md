---
title: "Why I'm Building My Own GPT-based Troubleshooting Agent"
description: "How I designed a GPT-powered assistant to semantically search my own documentation and streamline technical investigations."
pubDate: "Jun 6 2025"
heroImage: "/Troubleshooting_Agent.png"
tags: ["RAG", "GPT", "DevOps", "Pinecone"]
---

Troubleshooting complex systems has always been a major part of my job—whether during my years at **Amazon Web Service(AWS)** helping global enterprises resolve urgent technical issues, or now at **National Broadband Ireland**, supporting national infrastructure in a mission-critical DevOps role.

But the tools we rely on—manual document searches, outdated Confluence pages, scattered logs—just don’t scale with the complexity of modern distributed systems.

That’s why I built my own **GPT-based troubleshooting agent**: a fully personalized AI system capable of understanding, remembering, and evolving with the way I work.

The system—**CMAI GPT**—ingests my documents, high-level designs, logs, and even pipeline specs, transforming them into searchable vector embeddings with **Pinecone**. It then uses **OpenAI's GPT-4 Turbo** for **retrieval-augmented generation (RAG)**, delivering precise, context-aware answers to my queries in real-time.

But I didn’t stop there.

I added:
- **Lambda-based embedding pipelines**
- **FastAPI-powered endpoints**
- **Semantic memory that learns from feedback**
- **Dynamic document ingestion and auto-indexing**
- **Vector drift awareness and self-reinforcement loops**

This isn’t just a knowledge base—it’s a **self-evolving AI partner** that grows smarter as I work. It can explain edge-case bugs, trace architectural dependencies, and answer questions faster than any team wiki ever could.

The deeper I built, the clearer my goal became: I want to develop **AI agents that enhance human cognition**. Tools that help engineers like me **think more clearly**, **solve faster**, and **retain institutional knowledge** over time.

This project is also what inspired me to pursue formal AI education. I want to strengthen my theoretical grounding—not just in GPTs and embeddings, but in model architectures, RLHF, and responsible deployment strategies.

Because I believe we are at the edge of something transformative—not just for productivity, but for how we **transfer knowledge**, **accelerate expertise**, and **empower individuals and nations** alike.

This agent is my first step.
