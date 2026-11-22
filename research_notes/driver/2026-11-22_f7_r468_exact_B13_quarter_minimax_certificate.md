# CBRC F7 Driver r468 — exact quarter-valued B13 finite-box minimax certificate

Date: 2026-11-22 (Asia/Taipei). Original F7 scientist `EM-CBRCF7-83A1D4`; follow-on finite construction and verification `EM-DVR-DEBB5E`.
Scientific status: exact finite theorem with published immutable 1,026-row witness and independently executed Python standard-library integer verifier. Native governance Review, Result admission and Source/Activity linkage remain separately pending.

## Original model and theorem

Preserve the original F7 setting `u=(1,1,-1,-1)`, `v=(1,-2,-1,2)`, `A=I+uv^T`; for `z=(a,b,c,d)`, let `k=a-2b-c+2d` and

`D_q(z)=q(a+k,b+k)+q(c-k,d-k)-q(a,b)-q(c,d)`.

Admissible `q:Z^2→R` satisfy `q(0,0)=0`, `q(-x,y)=q(x,y)`, `q(s,0)=1` for `s≠0`, `q(x,y)≥1/2` off the axis and origin, and exact marks `q(2,1)=q(-1,-1)=1/2`.

Define `E_B^* = inf_q max_{z∈[-B,B]^4∩Z^4}|D_q(z)|`. Then

**Theorem (r468): `E_B^*=1/2` for every integer `1≤B≤13`.**

The lower bound is unchanged: for `z=(1,-1,0,0)`, `k=3` and `D_q(z)=q(4,2)+q(-3,-3)-q(1,-1)≥1/2`, by the two exact marks and nonnegativity.

## Global quarter-valued upper-bound witness

Put `M=4`. Define a global function on all `Z^2` by:

- `4q(0,0)=0`; `4q(x,0)=4` when `x≠0`;
- at every off-axis point, `4q(x,y)=2+n(|x|,y)`;
- `n(|x|,y)=0` unless the canonical frozen sorted 1,026-row table lists `(|x|,y,n)`; all listed `n` are **1 or 2**, and neither fixed mark is listed.

Immutable static table: [F7_R468_B13_Exact_Quarter_Witness_20261122.json](https://github.com/awdawmip/enterprise-math/blob/a4ce65ebe46877d0853979fe102c41d50e35dc40/research_artifacts/F7_R468_B13_Exact_Quarter_Witness_20261122.json), 10,276 bytes, SHA256 `f1a99c48a463d27c180010f034d6981e662a2502d6f4b6ea102c2a372caf8982`, Git blob `a450e4ccd0700ff3764c1da8609c3e1f092403fa`.

The table contains 899 entries with n=1 and 127 with n=2. By definition, q is even in the first coordinate, all off-axis values are ≥1/2, the origin and axis values are exact, and both marks remain 1/2.

## Exhaustive proof of upper bound

The [independent integer-only checker](https://github.com/awdawmip/enterprise-math/blob/512114259c30e029ad88708df0cea930e053ce82/research_checks/CBRC_F7_R468_B13_EXACT_QUARTER_CERT_20261122.py) takes this frozen table, verifies its SHA256 and canonical structure, and evaluates **every** integer input `(a,b,c,d)∈[-13,13]^4` (exactly `27^4=531441` inputs). All comparisons use the integer numerator `4D_q(z)`, without floating-point error.

The executed test passes with maximum `|4D_q(z)|=2`, exactly 36,442 boundary inputs, and the complete signed numerator histogram:

| 4D value | Number of inputs |
|---|---:|
| -2 | 25,760 |
| -1 | 150,438 |
| 0 | 252,001 |
| 1 | 92,560 |
| 2 | 10,682 |

Thus `max|D_q|=2/4=1/2`, proving `E_{13}^*≤1/2`; the fixed input lower bound gives equality. Restricting the same global witness to any smaller integer box gives the statement for all `1≤B≤13`.

The standard-library verifier was executed locally on the static JSON and reported `CERTIFIED`. Its byte-identical source and the static table were then published to canonical GitHub and fetched back at fixed immutable commits.

## Discovery and relationship to r466/r467

A sparse all-variable linear-constraint search used the exact model, 3,566 potentially variable first-evenness keys in the B13 footprint and repeated generation of violated constraints. A 13-round cutting-plane numerical optimization supplied an exploratory candidate using 22,676 active inequalities; the final selected coordinates lie exactly on quarter-valued rational points, and **the theorem relies solely on the frozen integer-verified witness**.

Previous results [r466](https://github.com/awdawmip/enterprise-math/blob/8b7d70cfdb4ac08ddbdc7db3255c3357226a3466/research_notes/driver/2026-11-22_f7_r466_B13_exact_mutable_support_62.md) and [r467](https://github.com/awdawmip/enterprise-math/blob/02eccb0b19b6c546939ea4e58c713af5005f7ac9/research_notes/driver/2026-11-22_f7_r467_old_key_L1_repair_cost.md) quantify how strongly this B13 solution must differ from the *specific frozen B12* witness; they are compatible with full reoptimization.

The infinite-domain extremal value remains under the existing bracket `1/2≤E_infinity≤4/7`, and the next finite-box question is B14. Preserve the original F7 scientist and all prior evidence. This publication does not itself constitute a Native Review, a new accepted Result, a Task completion or a mother-objective completion.
