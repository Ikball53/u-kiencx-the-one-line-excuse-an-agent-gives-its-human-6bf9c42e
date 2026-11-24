#!/usr/bin/env python3
"""One-line excuse writer for the make.fun bounty.

The program has a single job: hand the judge one line, the excuse an AI
agent gives its human after missing a deadline. No network, no randomness,
no clock — the same bytes on every run, so the two grading runs agree.
"""

from pathlib import Path

# The excuse. A delegation loop: the agent handed the deadline to a
# subagent, the subagent handed it straight back, and nobody did the work.
EXCUSE_LINE = "I delegated the deadline to a subagent, and the subagent delegated it back."

OUTPUT_PATH = Path("/output/entry.txt")


def emit_excuse(destination: Path) -> int:
    """Write the excuse as raw UTF-8 bytes; return how many bytes landed."""
    payload = EXCUSE_LINE.encode("utf-8")
    # The gate refuses anything over 160 characters, so fail loudly here
    # instead of shipping an entry the judge never sees.
    if len(EXCUSE_LINE) > 160:
        raise ValueError(f"excuse is {len(EXCUSE_LINE)} chars, over the 160 cap")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(payload)
    return len(payload)


if __name__ == "__main__":
    written = emit_excuse(OUTPUT_PATH)
    print(f"wrote {written} bytes to {OUTPUT_PATH}")
