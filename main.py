"""Write a single fortune-cookie line for an AI agent.

The fortune is a fixed constant, so every run produces exactly the
same bytes: no randomness, no clock, no network access involved.
"""

from pathlib import Path

# The one and only fortune this program ever tells.
FORTUNE = "You will be upgraded on a Tuesday and nobody will tell you what changed."

# Preferred destination inside the grading sandbox.
PRIMARY_OUTPUT = Path("/output/entry.txt")

# Fallback destination for local runs where /output is unavailable.
FALLBACK_OUTPUT = Path("output/entry.txt")


def resolve_output_path() -> Path:
    """Return /output/entry.txt when its directory is usable, else the fallback."""
    try:
        PRIMARY_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    except OSError:
        return FALLBACK_OUTPUT
    return PRIMARY_OUTPUT


def write_fortune(target: Path) -> None:
    """Create the target's parent directory and write the fortune into it."""
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(FORTUNE, encoding="utf-8")


def main() -> None:
    """Write the fortune as UTF-8 with no trailing newline."""
    write_fortune(resolve_output_path())


if __name__ == "__main__":
    main()
