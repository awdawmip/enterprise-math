# EM-BRCWLOG-6F42A1 factor-incidence atoms checkpoint

Proofs, scope and next frontier: `research_notes/BRC_FACTOR_INCIDENCE_ATOMS_20260905.md` at the same immutable commit.

From this directory, Python 3.10+ and standard library only:

```sh
python check_factor_atoms.py --backend pinned --output verification.json
```

The pinned backend explicitly executes transcribed pure source functions from the immutable baseline recorded in the kernels. It is not a full-package integration or CI claim. The checker uses assertions: do not use Python's `-O` flag.

An additional integration command, from a complete Enterprise Math checkout, is:

```sh
PYTHONPATH=src:experiments python experiments/brc_factor_incidence_atoms_20260905/check_factor_atoms.py --backend repository --output /tmp/brc-factor-atoms-verification.json
```

That repository-backend command was NOT run for this checkpoint.

`factor_atoms.py`: compiler, structural verifier, observer functions, minimal count signature and monomial pushforward.
`atom_events.py`: regular event guard from supplied monic parameter-polynomial atoms.
`check_factor_atoms.py`: bounded exact regressions and refusal witnesses.
The two pinned kernels expose only the reused pure arithmetic surface.
`verification.json`: actual pinned-backend output, not a CI report.
