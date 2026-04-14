# Status and Follow-Ups

## Status Values

The employer-facing side of the protocol should return a small, stable status vocabulary:

- `received`
- `accepted`
- `duplicate`
- `rejected`
- `needs_follow_up`

These are enough to support intake, dedupe, and early-stage recruiter workflows without overfitting to a specific ATS.

## Follow-Up Questions

Follow-up questions give the employer or recruiter agent a structured way to request missing information without dropping back into ad hoc email threads. Each follow-up should carry its own identifier and prompt so the candidate agent can answer in context.

## Example Payload

See [`../examples/status-response.sample.json`](../examples/status-response.sample.json).

## Implementation Notes

- Keep response states distinct from long-term hiring outcomes.
- Use explicit reason codes for duplicates and rejections where possible.
- Allow follow-up questions to be returned alongside `needs_follow_up` without redefining the whole packet format.
