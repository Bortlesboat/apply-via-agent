# Application Packet

## Purpose

The application packet is the structured payload a candidate agent submits on behalf of a job seeker. It should preserve enough context for recruiters to evaluate the candidate without requiring a human-style form-fill workflow.

## Required Fields

- `application_id`: Unique identifier for the submission event
- `job_id`: The target role identifier
- `candidate`: Core candidate identity and contact data
- `agent`: The submitting agent's identity and version
- `consent`: Candidate authorization metadata
- `provenance`: Signals about which fields were provided, transformed, or generated
- `answers`: Structured responses to role-specific questions

## Field Notes

The packet should bias toward evidence and structured answers, not free-form prose. Narrative summaries can exist, but the packet should remain inspectable enough for trust checks, dedupe, and ATS normalization.

## Example Payload

See [`../examples/application-packet.sample.json`](../examples/application-packet.sample.json).

## Implementation Notes

- Candidate identity and agent identity should be explicit, not inferred.
- Keep answers keyed to employer-issued question identifiers.
- Support attachments later, but do not block the first draft on file uploads.
