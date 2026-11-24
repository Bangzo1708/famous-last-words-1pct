#!/usr/bin/env python3
"""Famous Last Words at 1 Percent — entrypoint.

Writes the phone's final line to /output/entry.txt.

The line is the phone itself speaking in its last second at 1% battery:
a dark little confession, with the punch landing on the final beat.
"""

import os

ENTRY = (
    "Before I go, one last confession: your 'private' photos were never private "
    "\u2014 I showed the cloud everything. Sweet dreams."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
