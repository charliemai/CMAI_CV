---
title: "VideoTranslate"
description: "Upload an MP4/MOV to S3 and EventBridge triggers AWS Batch to generate Whisper subtitles (and optional translation) — designed for long videos beyond Lambda limits."
updatedDate: "Feb 27 2026"
heroImage: "/project_videotranslate.png"
badge: "Prototype"
demo: "/lab#videotranslate"
tech:
  - AWS S3
  - Amazon EventBridge
  - AWS Batch (EC2)
  - DynamoDB
  - Whisper
  - (Optional) Amazon Translate
  - Python
highlights:
  - "S3 upload triggers the pipeline automatically (no manual steps)."
  - "Runs on AWS Batch to avoid Lambda’s 15-minute runtime limit — suitable for long videos."
  - "Writes subtitles back to S3 and tracks processing in DynamoDB for idempotency."
metrics:
  - "Event-driven subtitle factory: raw/ → translated/ → processed/."
  - "A reusable pattern for turning media into searchable knowledge."
tags:
  - Serverless
  - Media
  - AI
---

## What it is

**VideoTranslate** is an automation tool that turns uploaded videos into usable text artifacts.

It’s designed specifically for the “long video” case where **AWS Lambda’s 15-minute limit** becomes a constraint.

1. You upload a video file (`.mp4` / `.mov`) to an S3 bucket.
2. An EventBridge rule detects the new object under a target prefix (e.g. `raw/`).
3. AWS Batch runs a containerized job on EC2:
   - downloads the video
   - uses **Whisper** to produce subtitle segments
   - optionally uses **Amazon Translate** for `zh-TW`
4. The job uploads `.srt` back to S3 and moves the original video to a `processed/` prefix.
5. A DynamoDB record is written to prevent duplicate processing.

## Why it matters

Transcripts unlock:

- Searchable knowledge (index transcripts into a vector DB)
- Faster summarization and note taking
- Subtitle generation and localization

## Architecture sketch

- **S3** as ingestion (`raw/`) and output (`translated/...`, `processed/`)
- **EventBridge** to trigger jobs on S3 object creation
- **AWS Batch + EC2** for long-running compute
- **Whisper** for speech-to-text subtitles
- **Amazon Translate (optional)** for localization
- **DynamoDB** for idempotency (don’t redo the same video/language combo)

## Demo

See the simulated pipeline UI on the **Lab** page.

## Notes

I also experimented with a Lambda-based version for short clips, but the “main” design goal here is reliability for longer media — so Batch is the default architecture.
