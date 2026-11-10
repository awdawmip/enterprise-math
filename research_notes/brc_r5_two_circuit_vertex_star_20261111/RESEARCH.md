# R5 — All 18 edge rays of the pinned 14-arc vertex have minimal K_{2,3} circuit length at most two

Date: 2026-11-11 (Asia/Shanghai). Status: author-side exact theorem and executed SymPy rational checker; independent Source review pending.

## Scope and frozen inputs

Continue the original seven-ratio, 30-allowed-arc, 21-observer-row auxiliary P/Q–BRC Blackwell model at the **same fixed physically lawful source/target pair** as PR #2017, PR #2021, and PR #2026. Frozen scientific pins from PR #2026: Global `a01383f825ef9d43b4b754254303298c64041568`; Enterprise Math `86149263e38c22292c9def1e0f69092efa1be77e`. The observer matrix and the pinned 14-arc vertex are rebuilt from the exact coefficients of PR #2026. This is an auxiliary observer/transport result, preserving P000 and the native X6 ontology.

Let `D={(i,j): j in {0,1,2,3,5,6}, i in {0,...,6}, j in {0,6} => i=j}`, so `|D|=30`. For `r=(1/10,1/2,3/4,1,5/4,3/2,19/10)`, column `C_(i,j)` has target marginal unit vector `e_i`, source marginal `e_j`, and source first-moment coordinate `r_i e_j`. Then `C` is 21 x 30 and has rank 15. The pinned fixed-fiber vertex `X` has 14 positive arcs, with `rank(C_supp(X))=14`.

## Exact result

For each source pair `j<k` from `J={1,2,3,5}` and target triple `a<b<c` from `{0,...,6}`, define the six-supported vector `H(j,k;a,b,c)` by

[
H_{aj}=r_b-r_c,quad H_{bj}=r_c-r_a,quad H_{cj}=r_a-r_b,
]
[
H_{ak}=-H_{aj},quad H_{bk}=-H_{bj},quad H_{ck}=-H_{cj},
]
with every remaining coordinate zero. Each satisfies `CH=0`, is nonzero on exactly six arcs, and belongs to one of `6*35=210` K_{2,3} circuit types.

Call the *K_{2,3} word length* of a nonzero residual `d in ker(C)` the smallest number of scalar multiples of the 210 types needed to sum to `d`. A scalar may be any nonzero rational in this theorem.

**Theorem.** For the 18 complete incident feasible edge rays at the fixed vertex X of PR #2026:
* Exactly **13** rays have residual support 6 and word length **1**.
* Exactly **2** rays have residual support 9 and word length **2**.
* Exactly **3** rays have residual support 10 and word length **2**.

Moreover, the two support-9 rays each admit exactly **three** unordered decompositions into two distinct K_{2,3} types (including the exact scalar coefficients), while each support-10 ray admits exactly **one** such decomposition.

The 13 length-one statements are checked by direct scalar identification with the 210 circuits. For all remaining five rays, here is one explicit two-circuit certificate. Notation `(j,k;abc)` means `H(j,k;a,b,c)`:

| Newly inserted arcs defining ray | Support | Certified identity `d=αH_1+βH_2` |
| --- | ---: | --- |
| `(1,5)` | 9 | `(-5/7)H(1,3;0,1,5)+(-5/9)H(3,5;0,1,6)` |
| `(1,2),(3,2)` | 10 | `(-5/28)H(1,3;0,1,5)-H(2,3;1,2,3)` |
| `(1,2),(4,2)` | 10 | `(-5/14)H(1,3;0,1,5)-H(2,3;1,2,4)` |
| `(1,2),(5,2)` | 9 | `(-15/28)H(1,2;0,1,5)+(-5/7)H(2,3;0,2,5)` |
| `(1,2),(6,2)` | 10 | `(-23/28)H(1,3;0,1,5)-H(2,3;1,2,6)` |

These identities use the exact ray normalization from `VERIFY_TWO_CIRCUIT_STAR.py` (a single new arc gets coefficient 1; two new arcs use the positive quotient-canceling weights). Every coordinate equality is checked in rational arithmetic. Since each minimum circuit has exactly six nonzero entries, a 9/10-supported ray cannot have word length one. The five exhibited identities complete their optimal length-two proof.

## Why two circuits are sometimes needed together

An edge ray at X is an extreme ray of the feasible tangent cone `T_X={d:Cd=0, d_z>=0 for each zero arc z of X}`. Although a length-two ray is the sum of two legal *observer-kernel* circuits, those two terms need not both belong to `T_X`. In the first displayed certificate, the term `(-5/9)H(3,5;0,1,6)` is negative on the currently zero arc `(1,3)`; the other term restores feasibility when combined. All five certificates have at least one such individually forbidden component, verified against every zero arc.

Thus the 9/10-support edge **directions are not minimal circuits of the linear matroid of C**: they are compound kernel residuals that become extreme under the vertex's one-sided positivity constraints. This sharpens the previous informal terminology “larger adjacency circuits” in PR #2026.

## Verification, exact coverage, provenance

Run `python VERIFY_TWO_CIRCUIT_STAR.py`. It reconstructs the original exact observer matrix, the pinned X, the 14-dimensional column-space basis and 18 positive edge rays. It generates all 210 minimal circuits, checks `CH=0`, computes all 18 residual vectors, tests exact membership in the one-circuit list, then for every remaining ray enumerates all `binom(210,2)=21945` possible distinct circuit pairs and solves for exact coefficients. Nonzero coefficients and all 30 exact coordinate equalities are checked. It asserts the full 13/2/3 count and the five decomposition multiplicities `[1,1,1,3,3]`. The locally executed evidence is in `EXACT_OUTPUT.txt`, ending `PASS_EXACT_TWO_CIRCUIT_STAR_18_OF_18`.

The original physical feasibility of the fixed source/target pair and exhaustiveness of the 18 adjacent rays are inherited from PRs #2017/#2026; this run rechecks the observation rank and the pinned vertex and independently regenerates the 18 algebraic rays. It does not repeat the 26 original physical capacity checks already pinned to the original exact witness.

Next discriminating question: for vertices in the 1775-point radius-four graph ball, determine the distribution and maximum K_{2,3} word length of their tangent edge rays; test whether a third circuit is required. Separately, a floating-point mixed-integer search found an optimal support value of 14 for the fixed fiber, matching the known 14-arc example; an exact global support-14 lower-bound certificate remains to be established. These are two independent continuation directions.
