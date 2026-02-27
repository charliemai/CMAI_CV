---
title: "Vouchgether"
description: "A voucher-sharing community service in Ireland: WhatsApp bot + web portal + AWS serverless backend with Stripe subscriptions."
updatedDate: "Feb 26 2026"
heroImage: "/project_vouchgether.jpeg"
badge: "Live"
url: "https://lkk.dev"
demo: "/lab#vouchgether"
tech:
  - WhatsApp Business API
  - AWS Lambda
  - API Gateway
  - DynamoDB
  - S3 (private objects + presigned URLs)
  - CloudFront
  - Stripe subscriptions + webhooks
  - Node.js
highlights:
  - "End-to-end product: WhatsApp bot + web pages (upload/claim/buy) + serverless backend."
  - "Anti-abuse & fairness: duplicate prevention (image + serial), weekly limits, idempotent Stripe/WhatsApp webhooks."
  - "Security-first delivery: vouchers stored privately in S3 and downloaded via short-lived presigned URLs."
  - "Operational readiness: monitoring/alerts, runbooks, and a P0/P1 launch test plan."
metrics:
  - "Designed a Go/No-Go checklist with P0 coverage for upload/claim/request/fulfill + payments + race-condition safety."
  - "Built for real users in Ireland (community-oriented cost-saving product)."
tags:
  - Product
  - Serverless
  - Payments
---

## What it is

**Vouchgether** helps people share and claim discount vouchers in a community-friendly way.
Instead of letting vouchers expire unused, contributors can upload vouchers and others can claim them—while the system enforces **fairness rules**, **anti-cheat**, and **secure delivery**.

## Core flows (high level)

- **Upload** voucher → OCR validation → duplicate check → voucher enters the pool
- **Browse** vouchers → claim one → secure claim link
- **Claim page** generates a **short-lived download URL** (S3 presigned URL)
- **Request / Fulfill** flow so people can request specific voucher types
- **Subscriptions** via Stripe (feature gating + reliable webhook handling)

## Architecture snapshot

Event-driven + serverless, optimized for operational simplicity:

- **WhatsApp Bot** for conversational UX
- **Static web** (CloudFront) for upload/claim/buy pages
- **API Gateway + Lambda** for business logic
- **DynamoDB** for voucher/user/request/pledge data
- **S3** private storage for voucher images
- **Stripe** checkout + webhooks for subscription state

## Demo

- Live site: `lkk.dev`
- On this portfolio: see the **UX walkthrough & screenshots** in the **Lab** section.
