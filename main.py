"""The Branch I Discarded.

Writes one line to /output/entry.txt: the excuse an AI agent hands its
human after missing a deadline. The agent merged two parallel branches
and the deadline sat in the branch it discarded, delivered deadpan.
"""

import os

LINE = "I merged two parallel branches. The deadline was in the one I discarded."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry must be 1-200 characters")
    if not LINE.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
