from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
checks = {
    "README.md": [
        "# Apply via Agent",
        "Don't fight AI applicants. Give them an official door.",
        "## What It Is",
        "## Why Now",
        "## Repo Map",
        "## What We Are Building",
    ],
    "spec/job-schema.md": [
        "# Job Schema",
        "## Purpose",
        "## Required Fields",
        "## Example Payload",
    ],
    "spec/application-packet.md": [
        "# Application Packet",
        "## Purpose",
        "## Required Fields",
        "## Example Payload",
    ],
    "spec/consent-and-provenance.md": [
        "# Consent and Provenance",
        "## Purpose",
        "## Required Fields",
        "## Example Payload",
    ],
    "spec/status-and-follow-ups.md": [
        "# Status and Follow-Ups",
        "## Status Values",
        "## Follow-Up Questions",
        "## Example Payload",
    ],
}

errors = []
for relative_path, expected_strings in checks.items():
    text = (ROOT / relative_path).read_text(encoding="utf-8") if (ROOT / relative_path).exists() else ""
    for value in expected_strings:
        if value not in text:
            errors.append(f"{relative_path} missing: {value}")

if errors:
    sys.exit("\n".join(errors))

print("Required sections are present.")
