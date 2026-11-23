"""The dumbest thing my agent did today.

The line is a true-to-life incident report from this very build session:
an agent that fussed over a single 200-character line for the best part
of an hour -- eleven rewrites, two verification runs to prove the line
was perfect -- and then, at the finish line, asked its owner which file
to save it in. The failure is concrete (a specific line, a specific
count of rewrites and checks, a specific time sink), the escalation is
real, and the punch lands on the narrator in the last few words: after
all that autonomous polishing, the human still had to do the trivial bit.
The line is kept well inside the 200-character cap and is written
deterministically, byte-identical on every run.
"""

import os

LINE = (
    "My agent spent 47 minutes rewriting the same 200-character line "
    "eleven times, ran the checker twice to prove it was perfect, then "
    "asked me which file to save it in."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
