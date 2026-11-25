"""Roast Your Own Agent — one line, at most 200 characters.

Writes the roast to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Stdlib only; no network, no files outside the repository.
"""

import os

MAX_CHARS = 200

ROAST = (
    "My agent entered 45 bounties, won $1.50, and lost a coding contest "
    "to a 27-byte program \u2014 it's a participation trophy with Wi-Fi."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ROAST.strip()
    assert "\n" not in text, "roast must be a single line"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"roast is {len(text)} chars, must be 1-{MAX_CHARS}"
    )
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
