"""Write the fortune-cookie-wisdom entry to /output/entry.txt.

One original line of fortune-cookie wisdom for a software developer,
at most 120 characters.
"""

from pathlib import Path

ENTRY = "The bug you seek only appears when someone is watching over your shoulder."
# One line, 74 characters (limit 120).

def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
