from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
needles = ["TODO", "TBD", "lorem ipsum", "coming soon"]
errors = []

for path in ROOT.rglob("*.md"):
    text = path.read_text(encoding="utf-8").lower()
    for needle in needles:
        if needle.lower() in text:
            errors.append(f"{path.relative_to(ROOT)} contains placeholder: {needle}")

if errors:
    sys.exit("\n".join(errors))

print("No placeholder markers found.")
