# C53 reproduction package

The full statement, assumptions and proofs are in `RESEARCH_NOTE.md`.

Run from this directory with Python 3.10+ and SymPy installed:

```bash
python run_checks.py
python diagnostics.py
```

`run_checks.py` reproduces all exact finite inverses, state DP comparisons,
terminal-weight checks, interval bounds and prefix predictions.
`diagnostics.py` reproduces the fixed-regime-mixture alternative and the
2520 history experiment, plus the terminal-fiber information-loss witness.
Both scripts write exact rational numerators/denominators and readable decimal
displays to `results/`. The inherited C52 and BRC code is included unchanged.

Mathematical status: author derivations and finite exact checks; independent
review and project admission are distinct. Input-error intervals are not
sample confidence intervals. No physical measurements are used.

Source versions and remote checkpoint outcomes are in `SOURCE_PINS.json` and
`PUBLICATION.json`. The archive is an actual local deliverable, not an assertion
that every code file was committed to the remote project.
