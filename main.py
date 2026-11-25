"""One Line, No Deadline Met.

Writes one single-line joke giving an excuse for a missed deadline to
/output/entry.txt. Pure stdlib, deterministic, no network.
"""

# The joke: the "already spent it" twist. The speaker burned their one
# extension on the apology itself, so the apology is late too. One
# sentence, punch in the final words, deadpan and self-inflicted.
JOKE = (
    "I used my one extension to write the perfect apology for missing "
    "the deadline, and now the apology is late too."
)


def main() -> None:
    """Validate the line against the gate, then write it out."""
    line = JOKE.strip()
    assert line, "joke must not be empty"
    assert "\n" not in line and "\r" not in line, "joke must be one line"
    assert 1 <= len(line) <= 200, "joke must be 1-200 characters"
    out_path = "/output/entry.txt"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
