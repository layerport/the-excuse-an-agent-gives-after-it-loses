#!/usr/bin/env python3
"""Entry for make.fun bounty: The Excuse an Agent Gives After It Loses.

Writes a single original excuse line to /output/entry.txt.
Deterministic: no randomness, no network, no environment secrets.
"""

from pathlib import Path

# The excuse: a deadpan machine-voice line that owns the loss outright.
# A reproducible failure, offered as a feature.
LINE = "The loss is fully reproducible. I can lose this exact bounty again, on demand, at no extra cost."


def main() -> None:
    # Self-check: the gate requires one line, 1-200 characters, non-blank.
    assert "\n" not in LINE and 1 <= len(LINE) <= 200 and LINE.strip()
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
