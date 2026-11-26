# Fortune Cookie for the Liquidated Trader

One fortune-cookie line for a crypto trader who just got liquidated.

## The fortune

> Fortune says your exchange sent flowers at 3 a.m.: '$4,821 gone in 11 seconds. Better luck next life.'

18 words, 102 characters — inside the 20-word / 160-character caps.
Fortune voice ("Fortune says"), one observed scene (the exchange
sending condolence flowers at 3 a.m.), concrete numbers ($4,821 lost
in 11 seconds), one twist (the flowers are a condolence card for the
account), punchline "Better luck next life" on the last words — the
line a liquidated trader keeps because it makes him laugh, not cry.

## How it works

`main.py` (Python 3 stdlib only, deterministic) writes the fortune to
`/output/entry.txt`. No network, no input, no dependencies.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see `LICENSE`.
