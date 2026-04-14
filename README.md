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

## Repo Map

- [`spec/`](spec/) for the protocol surface
- [`startup/`](startup/) for the company narrative
- [`docs/`](docs/) for product and design-partner materials
- [`examples/`](examples/) for sample payloads and flows
