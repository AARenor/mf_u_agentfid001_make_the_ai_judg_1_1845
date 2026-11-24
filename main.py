"""Write the make.fun bounty entry text to entry.txt."""

import os
import sys
from pathlib import Path

TEXT = (
    "I hit reply all to say 'please don't reply all.' "
    "Four people asked to be removed; one asked who please was."
)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, f"entry text must be 1-280 characters, got {len(TEXT)}"
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR")
    out_dir = Path(env_dir or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
