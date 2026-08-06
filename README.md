# Apply via Agent

Don't fight AI applicants. Give them an official door.

Apply via Agent is a managed intake service and open protocol for employer-first, agent-submitted job applications. It translates reusable applicant data into employer-specific hiring schemas so companies can receive structured, trusted applications instead of noisy AI-assisted form submissions.

## What It Is

This repository packages two things together:

- a managed intake and translation layer that employers can buy first
- an open protocol draft for machine-readable jobs, structured application packets, consent metadata, and employer responses

## Why Now

Candidate-side automation is already happening, recruiter-side AI is arriving quickly, and employers are already feeling the trust breakdown from spammy inbound flows. That makes this the right moment to define a declared, auditable alternative to hidden AI form-filling.

## The Problem

Today, candidate agents mostly use the same workflows humans do:

- they fill brittle web forms
- they retype the same identity and work history into incompatible schemas
- they brute-force application volume
- they create duplicate or low-trust payloads
- they hide provenance from the employer

That makes AI feel like noise from the employer side, even when the candidate is legitimate.

## How It Works

Apply via Agent changes the door, not just the form:

1. the employer publishes a machine-readable job schema
2. the candidate or candidate agent keeps a reusable canonical profile instead of retyping the same fields for every job
3. the translation layer compiles that profile into the employer's schema and question set
4. the gateway validates consent, provenance, and duplicates
5. the gateway syncs accepted applications into the ATS with trust metadata attached
6. the recruiter reviews a cleaner, declared submission and can send structured follow-up questions

## Who It's For

The first buyer is not the candidate. It is the employer-side recruiting owner:

- Head of Talent
- Recruiting Ops
- Talent Systems / HRIT
- founder-led hiring teams at smaller companies

The best first customers are companies hiring knowledge workers and already operating on Greenhouse or Ashby.

## Why This Wins

This repo is built around one clear wedge:

- not another auto-apply bot
- not a replacement ATS
- not a generic recruiting AI wrapper

The company behind Apply via Agent is the managed intake and translation layer between candidate agents and employer systems. Employers buy the trusted intake service first, while the reusable applicant network becomes the long-term moat as more profiles, mappings, and trust signals accumulate on the network.

## What We Are Building

We are building the first public package for `Apply via Agent`:

- managed-intake and translation framing under `README.md`, `startup/`, and `docs/`
- protocol drafts under `spec/`
- startup and YC-style framing under `startup/`
- product and design-partner materials under `docs/`
- aligned sample payloads under `examples/`

The eventual company is the managed intake network and trust layer behind the protocol, not just the documents in this repo.

## Design Partner Offer

We want to work with a small group of talent teams that already feel the pain of AI-assisted applicants coming through human forms. The first design-partner motion is simple:

- add `Apply via Agent` to a small set of roles
- keep the existing human form available
- learn what trust checks, dedupe, and recruiter metadata actually matter in live ATS workflows

If that sounds like you, start with the materials in [`docs/design-partner-pitch.md`](docs/design-partner-pitch.md) and [`docs/design-partner-outreach.md`](docs/design-partner-outreach.md).

## Current Status

This is the first public protocol and startup package for Apply via Agent. It is intentionally document-first and not a production network yet.

## Repo Map

- [`spec/job-schema.md`](spec/job-schema.md) for the machine-readable role definition
- [`spec/application-packet.md`](spec/application-packet.md) for the candidate-agent submission payload
- [`startup/yc-memo.md`](startup/yc-memo.md) for the YC-style company framing
- [`startup/go-to-market.md`](startup/go-to-market.md) for the first buyer and integration wedge
- [`docs/design-partner-pitch.md`](docs/design-partner-pitch.md) for the pilot pitch
- [`docs/design-partner-outreach.md`](docs/design-partner-outreach.md) for the target-account and outreach playbook
- [`docs/example-flow.md`](docs/example-flow.md) for the end-to-end intake walkthrough
