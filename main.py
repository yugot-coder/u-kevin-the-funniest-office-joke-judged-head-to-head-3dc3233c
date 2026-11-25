#!/usr/bin/env python3
"""The Funniest Office Joke — make.fun program/v1 entry.

Writes one original one-line office joke to /output/entry.txt.

The joke: "My boss says we're a family here, so I asked for my
inheritance — he gave me his old laptop and put me on a performance
improvement plan."

Chosen from 10 original candidates in CANDIDATES.md against the judge
brief: a real joke with a setup and a turn, built on something anyone who
has worked in an office recognises ("we're a family here"), a surprise
(asking for an inheritance, then the PIP as the punchline), one line,
punchline last, 137 characters — inside the 1–200 character gate.

Standard library only, deterministic: the same joke is written on every
run, byte for byte.
"""

import hashlib
import os
import sys

JOKE = (
    "My boss says we're a family here, so I asked for my inheritance "
    "\u2014 he gave me his old laptop and put me on a performance "
    "improvement plan."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate_entry(text):
    """Check the entry against the competition gate.

    Returns a list of problems; an empty list means the entry is valid.
    The gate: UTF-8 text of 1 to 200 characters, not only white space.
    """
    problems = []
    if not isinstance(text, str):
        problems.append("entry is not text")
        return problems
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        problems.append(
            "entry is %d characters, gate requires %d to %d"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    if not text.strip():
        problems.append("entry is only white space")
    if "\n" in text.strip():
        problems.append("entry must be a single line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append("entry is not valid UTF-8 text: %s" % exc)
    return problems


def main():
    """Write the joke to /output/entry.txt and report its validation."""
    problems = validate_entry(JOKE)
    if problems:
        for problem in problems:
            print("INVALID: %s" % problem, file=sys.stderr)
        return 1

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE)

    digest = hashlib.sha256(JOKE.encode("utf-8")).hexdigest()
    print("Wrote %s (%d characters, %d words)" % (out_path, len(JOKE), len(JOKE.split())))
    print("entry sha256: %s" % digest)
    return 0


if __name__ == "__main__":
    sys.exit(main())
