---
title: "UCD Sport Auto Booker"
description: "A scheduled automation that logs into a sports booking site, secures the best available slot, and sends email notifications — so you don’t have to refresh the page every day."
updatedDate: "Feb 27 2026"
heroImage: "/project_ucd_sport_booker.png"
badge: "Automation"
demo: "/lab#ucd-sport-booker"
tech:
  - AWS SAM
  - AWS Lambda (Python)
  - EventBridge Scheduler
  - DynamoDB
  - CloudWatch Logs
  - Requests / BeautifulSoup
  - SMTP notifications
highlights:
  - "Scheduler-driven: warmup + precise timing to hit competitive booking windows."
  - "Idempotent: stores booking state so it won’t double-book the same date."
  - "Supports multi-user coordination with a shared DynamoDB flag (first success wins)."
metrics:
  - "Hands-off booking: no more waiting at the website release time."
  - "A practical example of reliability engineering for ‘small personal automations’."
tags:
  - Automation
  - Serverless
  - AWS
  - DevOps
---

## What it is

This is a personal automation tool I built for **high-demand sports slot booking**.

Instead of sitting in front of the booking website and refreshing at the right minute, the system:

1. runs on a schedule
2. logs in
3. searches for preferred courts/time ranges
4. adds the best available option to the basket
5. notifies me immediately by email

## Why it matters

It sounds small — but it’s a great real-world DevOps problem:

- time-critical behavior (booking windows are competitive)
- retries and backoff
- idempotency (don’t repeat the same booking)
- observability (logs + notifications)
- safe deployment (config/secrets, rate limiting, guardrails)

## Architecture

- **EventBridge Scheduler** triggers the Lambda at specific times (timezone-aware)
- **Lambda (Python)** performs login + slot search + “add to basket”
- **DynamoDB** stores booking state to avoid duplicates and to coordinate multiple deployments
- **SMTP** sends notification when a slot is secured

This is deployed with **AWS SAM** and runs without a VPC (so it can access the public internet without NAT).

## Demo

See the simulated workflow on the **Lab** page.

## Responsible use

This type of automation should be used responsibly:

- respect the target site’s terms of service
- avoid aggressive traffic patterns
- add delays/retries that behave like a reasonable user
