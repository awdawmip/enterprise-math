# EC49FYC — Exact first-row-1 adaptive depth 15 and a forbidden-query path lemma

Date: 2026-11-23. **Frozen scientific pin:** `BRC16943`.
Parents: EC49FYA at `19a04cf3410c979ceb6502eae1fdbaba84ec5b68` (the depth-15 tree and state-certificate bound); EC49FYB at `4ff425bf1abc0e00fe3c5d2d81bd74b3aecb1dad` (exact nonadaptive cost 37); EC49FXU at `5e33d4576bb0c1ef09e9169f8e17df469b8b7692` (all 600 normalized states realized by genuine anchors).
Status: **AUTHOR_PROVED / EXACT_CONSTRUCTIVE_FINITE_CROSSCHECK / PARENT_DEPENDENT / NOT_REVIEWED**.

## Observer, quantifiers and result

Use the same 50 frozen nonzero ten-bit P10 support masks `U`, and 12 factors `z ∈ {-1,0,...,10}`, where `z=-1` means no missing column. The 600 states have readouts

```
W_(U,z)(t,j) = 1{(U & (1<<t)) != 0} * 1{z != j},
0 <= t < 10, 0 <= j < 11.
```

A deterministic observer makes adaptive, noiseless, unit-cost site reads and must identify the hidden state in the worst case. Its complete indexed reflection spectrum is **not** given for free. Define `Q_row1` as the minimum worst-case number of queries among observers **whose first site has row t=1**, with any column `j`. Then

`Q_row1 = 15.`

This is a *restricted-root exact theorem*. The unrestricted optimum remains `14 <= Q <= 15`; this note does not claim to distinguish 14 from 15 globally.

## Lower bound — a row-1 read cannot occur on a depth-14 path for one genuine state

Choose `s=(U=788,z=-1)`. The support rows of `788` are exactly `{2,4,8,9}`. The 11 genuine one-hole states `(788,j)` (`j=0,...,10`) differ from `s` exclusively at the `j`-th physical column, with positive bits on those four support rows. Thus distinguishing `s` from every one-hole variant forces **at least eleven distinct positive-site queries**, one in *each* column.

The same frozen atlas contains three strict full-factor supermasks:

- `789 = 788 | (1<<0)`: extra support `{0}`;
- `828 = 788 | (1<<3) | (1<<5)`: extra support `{3,5}`;
- `980 = 788 | (1<<6) | (1<<7)`: extra support `{6,7}`.

These three disjoint extra-support sets force **at least three additional negative-site queries** along the path for `s`, each from a different set. They cannot coincide with the eleven required positive readings. Consequently the path to `s` has length at least `11+3=14`.

Crucially, the row `t=1` is absent from `788`, from all eleven holes and from all three strict supermasks. **Every site `(1,j)` returns zero on all fifteen of these witness states.** It rules out none of the fourteen competitors. Therefore if an observer queries *any* row-1 site anywhere on the path to `s`, the same eleven-plus-three useful observations remain necessary: that path must have length **at least 15**.

In particular any observer beginning at `(1,j)` has worst depth at least 15. Moreover, any prospective *unrestricted* depth-14 tree is forbidden from reading row 1 at **any node along its path to `(788,-1)`**. This is a structural search/pruning condition, not a claim that all other root rows work in 14.

## Upper bound — a completely specified depth-15 observer with root (1,0)

Enumerate the 72 primitive P10 direction representatives with the frozen formula and deduplicate their ten-step supports to obtain the same 50 masks, then form all 600 states. Encode each site as `k=11*t+j` in `0,...,109`.

Use `(1,0)` as the fixed first query. Generate one priority permutation of the 110 physical sites with **xorshift32 seed 1**, Fisher–Yates shuffle from `i=109` down to 1. At every later non-singleton candidate set, choose the physical site minimizing the larger of its two response-class sizes. Resolve ties by that fixed permutation priority. Stop at a unique remaining state.

The accompanying exact verifier rebuilds and traverses the entire tree:

| Check | Exact outcome |
|---|---:|
| P10 primitive representatives | 72 |
| distinct support masks | 50 |
| genuine normalized states | 600 |
| first split `(1,0)` | 314 zero / 286 one |
| internal tree nodes / leaves | 599 / 600 |
| correctly identified states | 600 / 600 |
| worst-case physical reads | **15** |
| total depths over all 600 states | 6516 |
| uniform mean depth | **6516/600 = 10.86** |

Full depth histogram (depth: count): `7:49, 8:64, 9:125, 10:76, 11:50, 12:50, 13:50, 14:64, 15:72`.

All calculations of signatures, branch sizes and path lengths use exact integer arithmetic. No search-solver optimality claim is used: the analytic adversary gives the lower bound, and the fully generated binary tree gives the constructive upper bound. Changing the first column `0` to any other column is an isomorphism under mod-11 column translation; hence the same exact restricted optimum holds for all `(1,j)`.

## Reproduction / epistemic boundary

Run `node EC49FYC_ROOT_ROW1_15_VERIFY.js` (Node.js without third-party packages). Compare its JSON output with `EC49FYC_ROOT_ROW1_15_OUTPUT.json`. The independent local Python implementation using exact 600-bit query masks also reproduced first-row-1 depth `15` and total path depth `6516` with the same deterministic xorshift permutation.

This result concerns the **auxiliary normalized P10/C11 Farey–CRT observation model** only. Genuine-anchor realization is inherited from the pinned EC49FXU result rather than reproved here. It makes no transfer claim to native X6 dynamics, acquisition of height, noisy observations, or alternative cost models. It is neither a formal CLAIM/Result nor independent Review/Foundation promotion.

**Next discriminating research unit:** Determine whether a depth-14 global tree exists. Apply the new row-1-path exclusion for `(788,-1)` in exact branch-and-bound or adversary construction, exploiting column translation and the three critical full masks `101,788,833`; any impossibility verdict must cover all admissible root-row classes, not just this restricted family.
