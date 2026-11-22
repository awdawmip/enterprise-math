# T6 maximal-p13 valuation-one vertical order7 — exact two complete split exclusions and a partial third

2026-11-23, Asia/Hong_Kong. Original Research lane `chatgpt-research-onhour-enterprise-math-20260923`; Researcher `EM-X6-FB6990`, SID `MCP-082892eb480e45dea6d4b9fcc0491034`. Frozen mother task `RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND` (global (T_6=2332) or smaller exact (H_0,dots,H_6) collision), *remains OPEN*. This document is **AUTHOR_EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**, not a Native semantic PROGRESS, Result or mathematical review.

## Original representation and dependencies

Preserve every named original denominator (a=e+1), signs, repeat multiplicities, both side exponent masses separately bounded by **2331**, and the exact observer (H_k=sum(e/(e+1))^k), (k=0,ldots,6). Previous author-level lemma eliminates all p13 valuation ≥2 atoms; q0–q6 prior finite work is consumed at its original strength. The p13 valuation-one atom ((q,r)) with (q\ge1,,1\le r\le12) is denominator (13(13q+r)), cost (169q+13r-1). Signed q0 residues (u_r) refer to denominators (13r), weights (13r-1).

For each (j=1,ldots,6), the global original observer equality implies the mixed necessary congruence
```
sum_{r=1..12} u_r r^(-j)
 + sum_{(q,r) in V+} (13q+r)^(-j)
 - sum_{(q,r) in V-} (13q+r)^(-j) = 0 (mod 13^j).
```
This holds with arbitrary p13-free lower-prime denominators. Reuse the original saturated q0 integer lattice of index (13^{21}) and exact Fraction Gram–Schmidt (`min(GS_diag²) > 18,515,039`), with necessary ball radius at most (2\cdot2331^2=10,867,122). The floor/ceil recursion enumerates every affine q0 candidate inside the safe ball, then tests genuine two-side mass budgets. Opposite-sign identical named vertical atoms cancel to an already handled smaller order; they are not recounted as new q7 primitive outcomes.

Canonical full signed roster counts for vertical side orders 0 through7 are (1,12,90,520,2535,10908,42614,153960). Order7 up to exchanging global signs has four splits: `(0,7)`, `(1,6)`, `(2,5)`, `(3,4)`. This computation **does not assert the latter two are complete**.

## Actual bounded author execution

| Split | Actual exact scope | Raw pairs | Common-support removed | Primitive evaluated | Fraction GS nodes | Relaxed sphere leaves | Budget-valid |
|---|---|---:|---:|---:|---:|---:|---:|
| (0,7) | **COMPLETE** | 153,960 | 0 | 153,960 | 447,638 | 2 | **0** |
| (1,6) | **COMPLETE**, first-side residues 1..6 | 255,684 | 65,448 | 190,236 | 512,749 | 4 | **0** |
| (1,6) | **COMPLETE**, first-side residues 7..12 | 255,684 | 65,448 | 190,236 | 492,985 | 2 | **0** |
| (2,5) | **PARTIAL**, first 15 of 90 sorted order2 states only | 163,620 | 64,220 | 99,400 | 254,294 | 1 | **0 in visited range only** |
| **Visited total** | **not all q7** | **828,948** | **195,116** | **633,832** | **1,707,666** | **9** | **0 visited** |

All nine relaxed-ball survivors were rechecked using exact integer inverses modulo (13^j), j=1..6, together with their original side masses. Every candidate exceeds a cap on at least one side. Exact integer signed q0 vectors, named positive/negative vertical atoms, both masses, radius squares and ordered enumeration digests are retained in the <https://github.com/awdawmip/enterprise-math/blob/2df0ebd18efb020dfd150dd388344308f2af0bab/research_checks/T6_P13_Q7_PARTIAL_AUTHOR_EXACT_CERT_20261123.json>.

Example: for (2,5) within the **first 15** order2-side states, one modular/sphere leaf was
```
V+ = [(1,1),(1,1)]
V- = [(1,5),(1,6),(1,6),(1,7),(1,9)]
u  = [48,2,-17,-6,1,16,-11,-9,2,-1,4,-2]
actual side masses = [3084,4577] (>2331 each)
```
The full searched `(2,5)` range is only indices `[0,15)` (zero-based) of 90; order2-side indices `[15,90)` are **NOT EXECUTED**. The entire `(3,4)` split is **NOT EXECUTED**. The `(2,5)` first15 sub-run took 734.359 s, so next research should optimize/repartition with bounded resources without repeating already hashed ranges. The quick full splits (0,7), (1,6) are complete author exclusions.

Author source scripts and original machine certificates were run locally in four independent bounded slices, with distinct ordered source fingerprints (all in compact JSON). A newer derived portable in-repository script `research_checks/T6_P13_Q7_BOUNDED_AUTHOR_AFFINE_CHECK_20261123.py` is published for parameterized exact replay; it has **not** been separately rerun after GitHub publication. No independent reviewer, Native claim/progress or global T6 acceptance is asserted. q7 (0,7) and (1,6) are author-exact excluded **conditional on saved p13 valuation≥2 and saturated lattice lemmas**. Remaining q7 splits and lower primes are open.

## Scientific/control continuation

- No replay of q0–q6 or already complete q7 (0,7)/(1,6). Consume their immutable proof/certificate.
- Next precision step: close `q7 (2,5)` first-side index `[15,90)` in smaller bounded parcels, and `q7 (3,4)`; distinguish every completed subrange from one still in progress.
- Original native continuation request `onhour-20261123-0431-t6-own-exact-continuation-v1` has terminal SUCCEEDED/error=null, but current winning T6 CLAIM and native semantic PROGRESS have not been verified. Own SID remains provenance, not execution authority; do not use maintenance lane identity.
- P000 remains ACTIVE_LOCKED, frozen scientific task pin unchanged, no scheduler changes. Global T6 remains OPEN.
