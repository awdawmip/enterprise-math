# R5 full-256 nonadaptive minimax — reproducibility

Science pin: `awdawmip/enterprise-math@435e77af0d180eac32bd1f9c4c464bc4010b7551`. The input is not re-pinned to this research branch. Use the **unchanged** source file `EXACT_R5_ALL_101_BUDGETS.json`, SHA-256 `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`, together with its `stages_18.json` from the previous `EnterpriseMath_R5_D14_AllPairs_F0_F3_20261120.zip` reproduction bundle.

Place those two frozen files beside this directory's `VERIFY_R5_NONADAPTIVE_EXACT.py`; then run:

```sh
python3 VERIFY_R5_NONADAPTIVE_EXACT.py
```

Python standard library only, pure integer arithmetic and closed-interval strict-disjointness. The script checks the frozen SHA-256, all 32640 pairs, exactly 53 distinct action-separation sets, five minimal witnesses, all 101 action-price dual inequalities, the three-budget universal separator, and every early price subset for unique-action f=0,1,2. It prints PASS statements and the precise optimal distinct-action schedules. Its finite checks support the symbolic minimax proof for **every** integer f>=0 in `RESEARCH.md`.

The corresponding complete self-contained reproduction ZIP was generated for this conversation as `EnterpriseMath_R5_Full256_Nonadaptive_Exact_20261120.zip`. The ZIP contains the frozen integer input, the more detailed tested companion script, full proof, result, output and SHA-256 manifest; do not infer that the large frozen input was duplicated to this GitHub directory.

Evidence scope: AUTHOR_EXACT_FINITE + SYMBOLIC_PROOF, independent mathematical review **NOT_REVIEWED**, formal CLAIM/RUN **not created**, native BRC/X6 transfer **not asserted**. Remote GitHub publication and durable Activity association are separate operations.
