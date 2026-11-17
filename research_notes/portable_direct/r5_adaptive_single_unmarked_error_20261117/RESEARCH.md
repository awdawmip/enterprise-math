# R5 — Exact adaptive cost with one unmarked arbitrary error

Date: 2026-11-17 (Asia/Shanghai). Frozen scientific commit: `435e77af0d180eac32bd1f9c4c464bc4010b7551`. Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED. This is a theorem for the **derived 256-mask scalar integer observer** with budgets 214–314, not a proof of a native P000/X6/BRC equivalence.

## Statement (sharp worst-case adaptive result)

Let the true closure mask be any `b in {0,...,255}`, with exact count `N_b(k)` for integer budget `k=214,...,314` as in the immutable R5 source-cohort data. A query at budget `k` costs `k`. A normal real-valued response obeys `|y-N_b(k)| <= eta`; over the complete (adaptively chosen) query sequence the adversary may replace **at most one** response by any real number without an erasure mark. Require certainty of recovering every mask for every permitted response transcript. The objective is to minimize the maximum total queried budget.

Set
`delta = 76289178155959966960189440`.
For every real `eta >= 0` satisfying `2 eta < delta`, the **exact minimum worst-case adaptive total budget** is

```
C_adaptive(eta, e=0, f=1) = 1676.
```

The already proved sharp fixed-query cost in this interval is `3*(214+223+294)=2193`. Thus adaptivity saves exactly 517 budget units, around 23.57% relative to fixed. An intact transcript consumes 1462 units in the optimal adaptive protocol.

## Constructive strategy

For each single-budget response, identify its exact **count-symbol**: when the reported `y` lies in the closed interval `[N_b(k)-eta,N_b(k)+eta]` for any one distinct integer count value at this budget, output that center; otherwise output an out-of-alphabet marker. These intervals are disjoint because `2 eta < delta`. Every uncorrupted response maps to its true count-symbol, and an arbitrary bad reading maps to some symbol or the marker.

Read budgets in order `294,223,214`. At each budget while no discrepancy has yet been observed, query it **twice**. If the two count-symbols coincide, that symbol is true: there is at most one corruption in the entire transcript. If they differ, query the **same budget a third time**; the third symbol is true, since the unique corruption has already occurred in the differing pair. From then on query each remaining budget once, since the corruption budget has been exhausted. Finally use the known injective three-count signature `(N_b(294),N_b(223),N_b(214))` to recover the mask.

All possible branch costs are:

- No discrepancy: `2*(294+223+214)=1462`.
- First discrepancy at 294: `3*294+223+214=1319`.
- First discrepancy at 223: `2*294+3*223+214=1471`.
- First discrepancy at 214: `2*294+2*223+3*214=1676`.

Therefore the worst cost is **1676**. This works for all real adversarial corruptions; discretization is a proof device based on the measured gap, not an assumption that the original bad response is an integer.

The exact data show 32 distinct count centers at budget 214, 4 at 223, and 4 at 294; their minimum positive spacings are respectively `13883516118328421520506880000`, `267753525139190986466918400000`, and `76289178155959966960189440`. The three-count map has 256 distinct signatures on the 256 allowed masks.

## Matching adversarial lower bound

The following three exact source-witness pairs share mask `b*=16`. For each pair, their counts differ **only** at the indicated, mutually disjoint budget window, across *all* 101 permitted budgets:

| alternative to 16 | entire difference window | cheapest budget |
|---|---|---|
| 17 | 214..221 | 214 |
| 80 | 223..291 | 223 |
| 32 | 294..313 | 294 |

Follow any adaptive protocol on the transcript of six or more **honest** responses for true mask 16. It must query each window at least **twice** before it can safely terminate. Otherwise, a competing state that differs from 16 only in that window could reproduce the entire honest transcript by corrupting its sole distinguishing response, making unique identification impossible. Thus this particular honest path costs at least `2*(214+223+294)=1462`.

If the honest path already uses seven or more queries, the six mandatory window queries plus an extra query each of cost >=214 imply a cost of at least `1462+214=1676`.

Suppose instead it uses exactly six queries. By the preceding necessity, precisely two belong to each window. On the sixth query, give the exact count of the corresponding competing state (17, 80, or 32) in its window rather than the exact count of 16. This six-response transcript has two valid adversarial explanations:

1. True state 16, with exactly the sixth query corrupted.
2. True competing state, with the *earlier* one of the two queries in that window corrupted.

All other responses in both explanations are honest and identical, because the two states have equal counts outside their one difference window. Adaptivity does not help: the first five displayed answers are exactly the same as on the honest path, so the first six chosen budgets are the same. Any correct protocol must make at least one further query (cost >=214) before it can distinguish the two explanations. The original six queries cost at least 1462. Consequently its worst path costs at least **1676**.

The lower bound is already witnessed by noiseless valid responses, so it applies unchanged to every allowed `eta`. Combined with the construction above, it proves equality for all `0<=2 eta<delta`. Randomized protocols with zero error for every random seed have the same bound.

## Exact finite evidence and reproducibility

The accompanying `COHORTS_3_BUDGETS.json` transcribes the three small source-cohort coefficient dictionaries from the self-contained prior R5 frozen reproduction archive. The source's full-cohort-input SHA-256 is `a781cf89e534587009e207e51bbda2f411e4147746f7d6a0b72a1354e80f0d4d`. Full independent 101-budget table SHA-256 is `50e87f0194cfb3780e84b7bbb6f9a2dca4f79bb4901cab06f1a5b59256fb470b`. The three-budget compact input itself is SHA-256 `efbbdad49f602b94eb593e3491827f0a4b1bf712f006d332174171888d22b1fb`. Reconstruct all 256 exact counts per budget by eight subset-zeta passes.

The executed Python verifier:
- reconstructed and cross-checked 768 integer counts against the existing 101-budget full table;
- confirmed all 256 three-count signatures are distinct and measured the minimum positive per-budget count spacings;
- checked the three source difference windows at every one of the 101 budgets;
- checked all six permutations of the three query budgets;
- simulated 22,272 no-fault/single-fault symbolic response runs, covering every mask, every first/second reading position, every possible count center and the out-of-alphabet marker.

Executed stdout: `PASS_R5_SHARP_ADAPTIVE_SINGLE_UNMARKED_ERROR_1676`. The compressed cohort file alone suffices for constructive upper verification; checking the *global lower-bound windows* requires the previous complete 101-budget frozen table (provided in the referenced R5 reproduction package), not a newly inferred global statement from three budgets.

## Scope, source typing, and next question

The theorem is exact under its stated finite mask population, fixed scalar observation map, real bounded reading noise, one unmarked arbitrary corruption, and charged sum of budgets; it does not assume any relation-preserving replacement for native path, signed branch, joint observer, or X6 time trace. All unobserved structural information and source provenance remain separate from this 8-bit scalar quotient.

The open next problem is the exact adaptive min-max cost with `f>=2` unmarked errors or with `2 eta >= delta`, where the singleton-symbol quantizer is no longer disjoint. Another independent original R5 frontier is optimizer `max-new/min-old` recourse over budgets 214..291.

Researcher provenance: registered `EM-DIRECT-C52C70`, Activity `RA-E56F584D739D86CC48916236`; no new formal CLAIM is asserted by this note. Authored mathematics remains `NOT_REVIEWED`.
