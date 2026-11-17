# Reproduce the all-f uniqueness and three first-runner-up theorem

Scientific input is the frozen R5 derived scalar table `EXACT_R5_ALL_101_BUDGETS.json` from `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. SHA-256:
`50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`.

Place the exact JSON file alongside `VERIFY_SECOND_BEST_FIXED.py` and run:

```sh
python3 VERIFY_SECOND_BEST_FIXED.py
```

Expected first line:
`PASS_R5_UNIQUE_OPTIMUM_THREE_SECOND_BEST_ALL_F`.

The complete self-contained accompanying reproduction ZIP contains this input (1,549,048 bytes), proof, executable checker, results JSON and stdout. The table SHA is checked before reading. Enumeration covers 256 choose 2 = 32,640 named hypothesis pairs and all 101 physical budgets. The exact program checks all four dual witnesses at both chamber extrema, all nonnegative budget slacks, zero/unit slack classifications, and the validity of each replacement triple. End-to-end tests additionally check t=1,3,17,61; the all-f conclusion follows from the symbolic argument in `RESEARCH.md`.

Unique best fixed multiset: `(216,223,296)` each repeated `2f+1`, at cost `735(2f+1)`. Exactly three first runner-up multisets, each one query replaced (`216->217`, `223->224`, or `296->297`), with cost `735(2f+1)+1`.

Readouts are the frozen scalar observer only; the full native X6 relation requires its own observer-fidelity certificate. Review: `NOT_REVIEWED`.
