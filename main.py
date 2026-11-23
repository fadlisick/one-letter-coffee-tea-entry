"""One letter, A, for coffee.

The judge weighs two letters on vividness, humour and truth, in that
order. Coffee is the louder of the two drinks: black, bitter, and the
cup that hauls a person out of sleep and into the day, third refill
and all. Tea is gentle and quiet beside it, and quiet loses on
vividness. A is also the first, plainest answer a coffee drinker
gives when asked, so it reads as the honest one too. The program
writes that single letter and nothing else.
"""

import os
import sys

PICK = "A"
FILE_NAME = "entry.txt"


def destination():
    """Directory the harness grades, from the environment or /output."""
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    if not folder.strip():
        folder = "/output"
    return os.path.join(folder, FILE_NAME)


def check_single_letter(text):
    """Refuse anything that is not exactly one capital A-Z letter."""
    if len(text) != 1:
        raise ValueError("entry must be exactly one character")
    if not ("A" <= text <= "Z"):
        raise ValueError("entry must be a capital A-Z letter")


def emit():
    """Write the pick to entry.txt with no trailing newline."""
    check_single_letter(PICK)
    target = destination()
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "wb") as handle:
        handle.write(PICK.encode("ascii"))
    with open(target, "rb") as handle:
        written = handle.read()
    if written != PICK.encode("ascii"):
        raise ValueError("entry.txt does not hold exactly the pick")
    return target


def main():
    target = emit()
    sys.stdout.write("entry written: " + target + " (1 byte)\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
