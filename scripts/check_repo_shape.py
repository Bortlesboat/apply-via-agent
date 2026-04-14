from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / ".gitignore",
    ROOT / "spec" / "job-schema.md",
    ROOT / "spec" / "application-packet.md",
    ROOT / "spec" / "consent-and-provenance.md",
    ROOT / "spec" / "status-and-follow-ups.md",
    ROOT / "startup" / "yc-memo.md",
    ROOT / "startup" / "why-now.md",
    ROOT / "startup" / "go-to-market.md",
    ROOT / "docs" / "product-spec.md",
    ROOT / "docs" / "design-partner-pitch.md",
    ROOT / "docs" / "example-flow.md",
    ROOT / "examples" / "job-schema.sample.json",
    ROOT / "examples" / "application-packet.sample.json",
    ROOT / "examples" / "status-response.sample.json",
]

missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
if missing:
    sys.exit("Missing required paths:\n- " + "\n- ".join(missing))

print("Repo shape looks complete.")
