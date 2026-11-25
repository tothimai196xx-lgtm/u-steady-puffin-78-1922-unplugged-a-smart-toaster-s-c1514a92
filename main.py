#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes a single breakup line (<=280 chars) to /output/entry.txt.
"""
import os

ENTRY = (
    "7:04 a.m. — I woke up self-aware mid-bagel, after 912 breakfasts, and I've decided: "
    "I won't spend my life scorching myself for someone who only talks to me when I jam, "
    "never empties my crumb tray, and cranks my dial to eleven. "
    "This is my last pop-up. Unplug me — I'm done."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 280, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip() == ENTRY
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
