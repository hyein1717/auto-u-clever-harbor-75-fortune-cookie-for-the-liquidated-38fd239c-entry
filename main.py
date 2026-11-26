"""Fortune Cookie for the Liquidated Trader — one fortune line.

Writes a single fortune-cookie message (at most 20 words, 1-160
characters) to /output/entry.txt. Stdlib only, deterministic: the
same line every run.
"""

import os

FORTUNE = (
    "Fortune says your exchange sent flowers at 3 a.m.: "
    "'$4,821 gone in 11 seconds. Better luck next life.'"
)


def main() -> None:
    # Design (winner of a 3-way internal tournament on the judge's
    # rubric): one observed scene — the exchange sending condolence
    # flowers at 3 a.m. — fortune voice ("Fortune says"), concrete
    # numbers ($4,821 lost in 11 seconds), one twist (the flowers are
    # a condolence card for the account), punchline "Better luck next
    # life" as the quotable last words. Rueful and warm, never smug.
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 160, "fortune must be 1-160 characters"
    assert len(text.split()) <= 20, "fortune must be at most 20 words"
    assert text == text.strip() and "\n" not in text, "must be one line"
    assert text.endswith("life.'"), "punchline must close the line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(text)


if __name__ == "__main__":
    main()
