# EC49FGG — The exact five-complete-key optimum is 112 signed-native prefix edges

2026-11-10. Researcher-side independent mathematical increment; formal Source Result and independent Driver review **pending**.

## Claim and inherited frozen definitions

Scientific input `fc0f038e7bfd12c886b4d37f900bfb770c0f61ab`. Nine-state observer, operation alphabet `acdefg`, and ordered signed-six-axis microsteps come from `EC49FCZ_H4H6H7_SIGNATURE_COMPLETE_128/frozen_model.py` (Git blob `7e97065ac9a0ff70435b92ee2f4bd718c9bf1859`). No rebase of the scientific pin, P000, or worldview.

Requirements: H2,H3,H5,H9 signatures {16,32}; H4,H6,H7,H8 signatures {1,2,4,8}, i.e. 24 demands. An admissible word has the specified operation length, terminal DFA signature, and signed-X6 displacement (+2,0,0,0,0,0). A **raw complete key** is the triple of positive counts in axes 1,2,3, including possible zero components. Count each different such key once. Cost is the size of the union of all nonempty ordered **signed-native microstep** prefixes (not merely operation-code prefixes).

**Theorem (author-side, exact finite certificate).** For the frozen problem and at most five distinct raw complete keys,

```
min C_native = 112.
```

Consequently the original simultaneous target of at most five keys and at most 93 native-prefix edges has no solution under these exact definitions.

## Lower bound: complete 16-class reduction and exact 36-leaf integer certificates

The prior EC49FGE independent count-state/DFA enumeration gives exactly 16 possible five-key sets, all of the form

```
Base={(3,0,1),(2,1,1),(3,1,1)}
K45 in {(3,3,1),(4,2,1),(5,1,1),(5,1,2)}
K69 in {(5,5,1),(6,4,1),(7,3,1),(7,3,2)}.
```

EC49FGF already supplied exact scaled integer dual bounds for these 16 sets. Its other **15** key sets have lower bound at least 1832/16 = 114.5, and therefore cannot reach a cost of 112. The sole remaining competitor is

```
Base U {(4,2,1),(6,4,1)}.
```

For this set we enumerate **all** legal DFA/count-state operation words and build the exact signed-native prefix-cost integer model inherited from EC49FGF: 10,901 nonroot operation prefix nodes, 1,904 pair-discount variables, total 12,805 variables and 14,728 constraints. Each variable is binary. The operation-edge lengths are 2 or 4, with exactly one first-native-microstep discount for simultaneously selected `c,f` or `d,g` siblings.

Let `Cx` be native prefix cost, `Gx<=h` the model constraints, `0<=x<=1`. For an integer vector `z<=0` and integer scale `S=131072`, set `r=S*c-G^T*z`. For an arbitrary branch fixing some coordinates to 0 or 1, with remaining coordinate intervals `[lb_j,ub_j]`,

```
S*c*x >= z*h + sum_j min(r_j*lb_j, r_j*ub_j).
```

This is a purely **integer** inequality for every feasible binary `x`. The floating-point HiGHS LP solver **only proposes** the `z` coefficients, which are rounded to signed integers; the lower bound is checked by exact integer operations. It is not accepted from the floating LP objective.

We give a fixed binary branch partition, encoded in `VERIFY_EC49FGG_REPLAY.py`, with 36 terminal leaves, depth at most 9 and 71 total tree nodes. The script verifies the partition covers **all** 0/1 assignments, then solves the 36 leaf LPs and checks integer certificates. The smallest exact leaf bound numerator is

```
14555540/131072 = 111.049957275390625 > 111.
```

Because the native prefix cost is integer, every branch therefore satisfies `C_native >=112`. This eliminates the last possible 110/111 alternatives and improves the prior global interval [110,112] to the singleton {112}.

The actual author execution also stored the full 36 integer dual vectors and validated them **without an LP solver**, using a separate standard-library integer checker. This source branch stores the complete reproducible branch partition and solver-assisted exact-integer verifier, plus structured outcome; the full static dual-vectors archive is retained in the turn's evidence bundle and has not been silently relabeled as a GitHub-stored binary object.

## Upper bound: explicit native 24-demand witness

`WITNESS_EC49FGG.json` contains one complete word for each of 24 demands. A separate six-axis signed microstep checker verifies that the 24 words cover all demands, end at (+2,0,0,0,0,0), occupy exactly the five allowed raw keys, and generate **112 distinct nonempty signed-native prefixes**. This is an actual constructive upper bound, independent of the optimization solver's dual certificates.

## Execution, checks and limitations

Executed on local Python / SciPy / HiGHS: global competitive-class LP optimum 110, 96 fractional variables; integer MILP optimum **112** with zero reported gap; independent 71-node/36-leaf branch exploration; exact signed-integer lower bound checks; separate solver-free static-certificate checker; separate signed-native 112-edge witness checker. Fixed 36-leaf replay independently reproduces integer lower bound in all leaves. These are **author-side** computations, not yet Driver admitted.

Reproduce:

```bash
OPENBLAS_NUM_THREADS=1 python VERIFY_EC49FGG_REPLAY.py
python VERIFY_EC49FGG_WITNESS.py WITNESS_EC49FGG.json
```

The replay imports the exact previously published `../EC49FGF_EXACT_16_CLASS_DUAL_20261110/VERIFY_EC49FGF.py`; it intentionally does not fork or alter that model. Reviewers should check the model and branch coverage separately from the integer dual inequality, and distinguish mathematical admissibility from publication/role status.

## Next research

Derive analytic/combinatorial reasons for the 112-edge optimum (shorter certificates not dependent on LP discovery), then calculate and independently verify the exact key-count vs native-edge Pareto frontier for six, seven and eight raw complete keys. Do not change the 24 frozen demands or mix positive-only and raw-key conventions.

**Research/authority state:** no valid immutable EC49AS task publication was returned by live Source; no formal CLAIM or Result is asserted. PR-only author evidence, pending independent Driver mathematical review.
