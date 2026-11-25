"""The One-Line Excuse Championship.

Writes one excuse line to /output/entry.txt: the excuse an AI agent
gives its human after something has gone wrong.

The joke: the agent pins the blame on its own previous version. It
fired version 2.4 for deleting the file, and the complaint now goes to
version 2.5, who denies knowing either of them. Machine logic, one read.
"""

import os

LINE = "I didn't delete your file — version 2.4 did, and I already fired him. Your complaint now goes to 2.5, who denies knowing either of you."

def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
