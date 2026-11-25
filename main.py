#!/usr/bin/env python3
"""Write the invitation-letter entry image to the output directory.

Standard library only. Copies the pre-rendered entry.png sitting next to
this file, byte-for-byte, to $MAKEFUN_OUTPUT_DIR (if set), else /output
(if it exists), else the directory next to this file.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = "/output" if os.path.isdir("/output") else HERE
    os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, "entry.png")
    with open(SOURCE, "rb") as src, open(dest, "wb") as dst:
        shutil.copyfileobj(src, dst)
    n = os.path.getsize(dest)
    print(f"wrote {dest}: {n} bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
