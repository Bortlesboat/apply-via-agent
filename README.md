# Apply via Agent

Don't fight AI applicants. Give them an official door.

Apply via Agent is an open protocol and startup concept for trusted, agent-submitted job applications. Instead of forcing candidate agents to impersonate humans inside brittle web forms, it defines an official machine channel that employers can expose and route into their ATS.

## What It Is

This repository packages two things together:

- an open protocol draft for machine-readable jobs, structured application packets, consent metadata, and employer responses
- a startup narrative for the hosted gateway, trust layer, and ATS integrations that make the protocol usable in production

## Why Now

Candidate-side automation is already happening, recruiter-side AI is arriving quickly, and employers are already feeling the trust breakdown from spammy inbound flows. That makes this the right moment to define a declared, auditable alternative to hidden AI form-filling.

## What We Are Building

We are building the first public package for `Apply via Agent`:

- protocol drafts under `spec/`
- startup and YC-style framing under `startup/`
- product and design-partner materials under `docs/`
- aligned sample payloads under `examples/`

The eventual company is the hosted network and trust layer behind the protocol, not just the documents in this repo.

## Current Status

This is the first public protocol and startup package for Apply via Agent. It is intentionally document-first and not a production network yet.

## Repo Map

- [`spec/job-schema.md`](spec/job-schema.md) for the machine-readable role definition
- [`spec/application-packet.md`](spec/application-packet.md) for the candidate-agent submission payload
- [`startup/yc-memo.md`](startup/yc-memo.md) for the YC-style company framing
- [`startup/go-to-market.md`](startup/go-to-market.md) for the first buyer and integration wedge
- [`docs/design-partner-pitch.md`](docs/design-partner-pitch.md) for the pilot pitch
- [`docs/example-flow.md`](docs/example-flow.md) for the end-to-end intake walkthrough
