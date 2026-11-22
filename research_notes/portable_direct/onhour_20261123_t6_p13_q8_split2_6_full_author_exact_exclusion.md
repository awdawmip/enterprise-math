# T6 p13, v13=1, vertical order 8, split (2,6): complete author finite exclusion

Date: 2026-11-23, Asia/Hong_Kong. Frozen scientific task: `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND` at `d84bd940cfb093cdc60e569f15cad58772a51dca`. Original **two separate** side exponent-mass caps 2331. Exact named denominators, signed multiplicity, all six mixed 13-adic necessary congruences. **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

## New mathematical result

For maximal-prime-13 atoms of 13-valuation one, the vertical order-8 split `(2,6)` has **no admissible pair** under both side budgets and the six mixed congruences derived from original `H_0,...,H_6`. Conditional dependencies are the previously stored p13 valuation>=2 cancellation and saturated 12-dimensional q0 lattice; this is **not** a claim that all p13 order 8 or global T6 is closed.

Atom `(q,r)` represents denominator `13(13q+r)`, with exponent cost `169q+13r-1`; q0 coordinate `u_r` represents denominator `13r` with exponent cost `13r-1`. For each `j=1,...,6`, require
`
sum_r u_r*r^(-j) + sum_plus (13q+r)^(-j) - sum_minus (13q+r)^(-j) == 0 (mod 13^j).
`
All modular inverses are of 13-units. These are necessary conditions allowing unconstrained smaller-prime atoms; they do not assume local rational-moment equality.

## Complete exact enumeration

Canonical sorted first-side order-2 roster has **90** named multisets; second-side order-6 roster **42,614**. Full **3,835,260** ordered side pairs were visited. Opposite-side common named atoms are cancelled rather than counted as a primitive support. All q0 candidates arise from the exact saturated lattice (index `13^21`), LLL-transformed weighted basis and exact rational Gram-Schmidt recursion. Its minimum diagonal square is

`
78577530278042129705264382752517501995032553011464356025 /
4243983974238642688103181306691645151538473248349
`

which strictly exceeds `2*2331^2=10,867,122`; thus at each coordinate the exact necessary ball includes only the two consecutive nearest integers `floor(-center)`, `floor(-center)+1`. No floating point selects or discards any candidate. Signed q0 vectors are recovered exactly and the two original masses are recomputed.

| First-side sorted-index range | Raw ordered pairs | Common support eliminated | Evaluated primitive pairs | Exact GS recursive nodes | Relaxed leaves | Original-budget valid |
|---|---:|---:|---:|---:|---:|---:|
| [0,1) | 42,614 | 10,908 | 31,706 | 79,117 | 0 | 0 |
| [1,8) | 298,298 | 134,967 | 163,331 | 395,609 | 3 | 0 |
| [8,20) | 511,368 | 222,999 | 288,369 | 687,563 | 1 | 0 |
| [20,40) | 852,280 | 368,874 | 483,406 | 1,141,567 | 2 | 0 |
| [40,65) | 1,065,350 | 448,533 | 616,817 | 1,423,446 | 1 | 0 |
| [65,75) | 426,140 | 176,064 | 250,076 | 562,171 | 3 | 0 |
| [75,82) | 298,298 | 51,237 | 247,061 | 589,978 | 1 | 0 |
| [82,90) | 340,912 | 20,280 | 320,632 | 761,397 | 4 | 0 |
| **Total** | **3,835,260** | **1,433,862** | **2,401,398** | **5,640,848** | **15** | **0** |

All 15 relaxed leaves satisfy the exact modular congruences and ball constraints but fail at least one original mass cap. The smallest excess of the *larger* side mass over 2331 is 1527. No interval was marked complete on interruption; an attempted unsegmented run timed out without a completed result and contributes nothing to this proof. The eight explicitly completed, disjoint slices cover [0,90) without gaps.

Exact source-order SHA-256 for each completed slice:

```
[0,1)    e9993e0b5ceacf6362f6d2a43918e99d327753558db76ae950b4e02ccac3e4cb
[1,8)    99900907f5750e375dd2b32ddc7ac64ec59e0d35b24b41f6453c7b411c561c8b
[8,20)   c43e37ae3a16c147c4304c499986883f7fa05d9cdb9d673ef09b093f0d8b1471
[20,40)  ba8710b58565d72296634ea34a78a48f4204c022cf770a80cda763ae2df2e490
[40,65)  d5be7658aa8ec182f2854e262e9969b2225c28678d1f733d7efd8e7ddd96fc99
[65,75)  a708ff453518d167a7a2864e406a66304fe67ca2e83eca4776576ca938186111
[75,82)  179bb122732eb02e426f6ed1edb9c9c2aee40fe72dd2f419a72d6f70af192998
[82,90)  a7940f32eda14f16d423470ea4864770c875a87b3da391efe14cf9bdd7e42d48
```

## Reproduction and evidence boundaries

The same carrier and slice semantics can be regenerated using existing source `research_checks/T6_P13_Q8_BOUNDED_AUTHOR_AFFINE_CHECK_20261123.py` (which imports `T6_P13_Q2_ALL_SPLITS_GLOBAL_AFFINE_CHECK_20261123.py` and its exact q0 basis) with `2 6 start end` for the eight intervals above. The actual locally executed check rederived the q0 HNF/LLL and exact Gram-Schmidt, retained all original named pairs, and verified all relaxed leaves by exact modular arithmetic and original budgets. The post-publication repository checker is **not independently rerun or reviewed**. An author-local complete detailed JSON certificate and script remain available in the run artifacts; their standalone remote storage is **pending**, rather than falsely claimed as canonical publication.

A full Task Result / review / Source semantic PROGRESS has **not** been published, and no native winning T6 CLAIM is verified. The historical Activity has an unresolved Source-vs-recovery author identity mismatch; do not append a new event under a borrowed Researcher identity.

**Next scientific frontier:** complete order-8 splits `(3,5)`, `(4,4)` with the same exact model, then other p13/lower-prime units. The mother goal `T6=2332` stays OPEN. Do not repeat p13 `q0...q7` or previously closed `(0,8),(1,7)` work. Preserve source Task's separate live owner/continuation authority and the original bridge request `onhour-20261123-0627-own-t6-source-cont-ro-v1` (SUCCEEDED read only).
