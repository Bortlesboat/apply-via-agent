# Job Schema

## Purpose

The job schema gives candidate agents a machine-readable version of an employer's role requirements so they can assemble cleaner, more comparable application packets than a generic autofill flow.

## Required Fields

- `job_id`: Stable identifier for the role
- `title`: Human-readable role title
- `employer`: Employer metadata including name and ATS
- `required_qualifications`: Must-have skills or experience
- `knockout_questions`: Structured yes/no or typed questions that gate submission
- `submission`: Submission settings for the role, including whether a human form is still available

## Field Notes

The first version should stay intentionally narrow. It only needs enough structure to support role discovery, application assembly, and trust-preserving intake. Richer concepts like compensation bands, work authorization rules, and jurisdiction-specific disclosures can be layered in once real employers react to the first draft.

## Example Payload

See [`../examples/job-schema.sample.json`](../examples/job-schema.sample.json).

## Implementation Notes

- Prefer stable machine IDs over scraped page URLs.
- Keep question shapes simple for V1.
- Let employers expose both human and agent submission modes during rollout.
