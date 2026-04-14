# Consent and Provenance

## Purpose

Consent and provenance turn a raw submission into a declared one. They tell the employer that the candidate authorized the submission and give the recruiter or gateway enough context to understand how the packet was assembled.

## Required Fields

- `consent.granted`: Whether the candidate explicitly authorized submission
- `consent.timestamp`: When the authorization was recorded
- `agent.name`: Declared agent identity
- `agent.version`: Agent version or build identifier
- `provenance`: Per-field or grouped origin metadata for important content

## Field Notes

V1 does not need perfect cryptographic proofs to be useful. It does need explicit declarations that distinguish candidate-provided data, transformed data, and agent-generated summaries. That alone is a major step up from hidden AI assistance in human forms.

## Example Payload

See [`../examples/application-packet.sample.json`](../examples/application-packet.sample.json) for the first aligned consent and provenance example.

## Implementation Notes

- Keep provenance vocabulary small for the first draft.
- Treat missing consent as a hard failure for gateway acceptance.
- Make it easy for employer systems to store provenance without needing to understand every future field.
