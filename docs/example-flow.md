# Example Flow

## Candidate and Agent

On April 14, 2026, Jordan Lee authorizes a candidate agent to apply to ExampleCo's Founding Product Engineer role. The agent records explicit consent, keeps Jordan's structured profile on hand, and prepares to answer any employer-issued knockout or follow-up questions.

## Employer Job Schema

ExampleCo publishes the role with an `Apply via Agent` option alongside its normal human form. The machine-readable job schema gives the candidate agent the role ID, employer metadata, required qualifications, and structured knockout questions so the application packet can be assembled against the employer's own field model.

## Gateway Intake

The candidate agent submits a structured application packet that includes Jordan's identity, declared agent identity, consent timestamp, provenance metadata, and answers to the job's knockout questions. The gateway validates required fields, checks whether Jordan has already applied to the same role, and either accepts the submission or marks it as a duplicate with a reason code.

## ATS Sync

If the submission is accepted, the gateway normalizes the packet into the employer's ATS and carries trust metadata alongside the application record. If the candidate or agent resubmits the same packet on April 15, 2026, the gateway can return a duplicate response instead of creating a second ATS application.

## Recruiter Review

The recruiter sees a normal application in the ATS, plus the trust and provenance metadata attached by the gateway. If key evidence is missing, the recruiter or recruiter-side agent can issue a structured follow-up question asking for a shipped product example, and the candidate agent can respond without falling back into an email thread or a brittle human-only form.
