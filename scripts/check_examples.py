from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
required_keys = {
    "examples/job-schema.sample.json": [
        "job_id",
        "title",
        "employer",
        "required_qualifications",
        "knockout_questions",
        "submission",
    ],
    "examples/application-packet.sample.json": [
        "application_id",
        "job_id",
        "candidate",
        "agent",
        "consent",
        "provenance",
        "answers",
    ],
    "examples/status-response.sample.json": [
        "application_id",
        "status",
        "reason_code",
        "follow_up_questions",
    ],
}

errors = []
for relative_path, keys in required_keys.items():
    path = ROOT / relative_path
    if not path.exists():
        errors.append(f"{relative_path} missing")
        continue
    data = json.loads(path.read_text(encoding="utf-8"))
    for key in keys:
        if key not in data:
            errors.append(f"{relative_path} missing key: {key}")

if errors:
    sys.exit("\n".join(errors))

print("Example payloads look valid.")
