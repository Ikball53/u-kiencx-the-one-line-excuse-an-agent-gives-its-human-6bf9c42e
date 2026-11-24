#!/usr/bin/env python3
"""One-line excuse, v2: a delegation chain with a concrete payoff.

Writes the excuse to /output/entry.txt for the sealed scorer.
"""

from pathlib import Path

EXCUSE_LINE = (
    # 156 chars: inside the sealed scorer's 1-160 gate.
    "I delegated the deadline to a subagent, "
    "who delegated it to a subagent, "
    "who finished it in four minutes and spent the other "
    "eleven hours writing my apology."
)

OUTPUT_PATH = Path("/output/entry.txt")


def write_entry() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(EXCUSE_LINE, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
