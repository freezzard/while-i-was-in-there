# While I Was In There

A one-joke program for the make.fun bounty **Make the AI judge laugh**
(ai-joke-03).

The program writes a single one-liner about AI coding agents to
`/output/entry.txt`. The joke is a constant in `main.py`, so the program
is deterministic: every run writes exactly the same bytes, with no
network access and no dependencies beyond Python 3.13.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT, see `LICENSE`.
