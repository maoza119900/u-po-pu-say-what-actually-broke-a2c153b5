"""Say What Actually Broke — make.fun bounty entry.

Writes one single-line software error message to $MAKEFUN_OUTPUT_DIR/entry.txt.

Fully deterministic: one fixed string, no time, no randomness, no network,
no file traversal. Python 3.13 standard library only.
"""

import os

ENTRY = (
    "The server ran out of memory and fainted. "
    "It is now lying in a dark room, rethinking its life choices. "
    "Give it a minute, then try again."
)

# The gate requires /output/entry.txt to be UTF-8 text of 1 to 200 characters,
# not only white space. Check the line (plus its trailing newline) up front so
# a too-long line fails loudly here instead of silently failing the gate.
assert 1 <= len(ENTRY) + 1 <= 200, "entry line is outside the 1-200 char gate"
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
