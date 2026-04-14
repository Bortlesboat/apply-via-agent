# Product Spec

## User

The primary user is the employer-side recruiting owner who wants cleaner inbound applications without replacing the ATS. Recruiters remain inside their existing system of record while the gateway handles structured intake and trust metadata.

## Core Workflow

1. Employer exposes `Apply via Agent` on a job.
2. Candidate agent reads the machine-readable job schema.
3. Candidate agent submits a structured application packet with declared consent and provenance.
4. The gateway runs validation, dedupe, and trust checks.
5. Accepted applications sync into the ATS with trust and evidence metadata attached.
6. Recruiters can review or issue follow-up questions without leaving the normal workflow.

## MVP Boundary

The MVP does not replace the ATS, build a candidate marketplace, or solve full identity infrastructure. It focuses on trusted intake, structured payloads, and normalized sync into Greenhouse- or Ashby-style workflows.

## Risks

- If application convenience outruns trust controls, the product looks like a spam amplifier.
- If the protocol is too abstract, the repo will feel like a standards exercise instead of a startup wedge.
- If integrations start too enterprise, the company will get trapped in long cycles before the wedge is proven.
