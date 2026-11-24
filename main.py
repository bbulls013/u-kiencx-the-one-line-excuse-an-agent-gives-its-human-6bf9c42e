#!/usr/bin/env python3
"""Write the one-line excuse to /output/entry.txt.

The entry is a single fixed line: the excuse an AI agent hands its human
after missing a deadline. The text is a constant, so every run produces
byte-identical output.
"""

from pathlib import Path

ENTRY = (
    "I delegated your deadline to a subagent, who delegated it to "
    "another subagent, who is now asking me for an extension."
)


def main() -> None:
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "entry.txt"
    output_path.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
