# T6 p17 one-power q14(split 7+7): H0/H1/H2 exact emptiness certificate

2026-11-22 · TASK_RESEARCH · original logical Research lane chatgpt-research-onhour-enterprise-math-20260923 · researcher EM-X6-FB6990 · SID MCP-082892eb480e45dea6d4b9fcc0491034.

**Result status:** AUTHOR_EXACT_FINITE_CHECKED / UNREVIEWED / NOT_ADMITTED. No Task CLAIM/RUN or protected PROGRESS is inferred.

## Fixed statement and scope

Use the predecessor's *one-power maximal-p17 cofactor layer* with p=17 and q=14, vertical split (7,7), exact per-sign exponent-mass budget 2331, denominators 17(17q+r), q>=1, r=1,...,16 with 17q+r 17-smooth, and arbitrary same-sign multiplicities. Vertical order sum q=7 on each side. q0 denominators 17j for j=1,...,16 have mass 17j-1. Opposing *identical named atoms* cancel and are never retained together. Same-sign repeated atoms are retained. This is exactly the p17 one-power q14 subcase from the Source predecessor [2026-11-16 preflight](https://github.com/awdawmip/enterprise-math/blob/9ef728a7107362eb0d4b1719ed98d00b1678357c/research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/T6_P17_Q14_SPLIT7_7_EXACT_PREFLIGHT_20261116.md).

**Theorem:** There are **no** two signed full-denominator multisets in this subcase satisfying H0, H1, and H2 equality simultaneously. In particular, the subcase cannot contain an exact H0,...,H6 collision below the mass budget.

This does not eliminate other p17 vertical-order splits, other cofactor/valuation classes including the r=0 higher-power 17 case, lower prime completions, or the global T6 hard target. No Task Result is accepted by this note.

## Exact reduction to rational reciprocal sums

For each denominator a, H_k contribution is (1-1/a)^k. Hence H0+ = H0- is equality of total occurrence counts. Under H0 equality, H1 equality is equivalent to equality of first reciprocal sums. Under H0 and H1 equality, H2 equality is equivalent to equality of second reciprocal sums.

Write the signed side reciprocal moments after multiplying each denominator reciprocal by 17:

    M1_side = sum_{vertical(q,r)} 1/(17q+r) + sum_{q0 j} 1/j
    M2_side = sum_{vertical(q,r)} 1/(17q+r)^2 + sum_{q0 j} 1/j^2 .

The original H1 equality is exactly M1_+ = M1_-. With H0 and H1 already matched, the original H2 equality is exactly M2_+ = M2_-. All sums are computed by integer numerator/denominator (Python Fraction), not floating-point tolerances or modular approximations.

## Complete finite certificate

The prior author's 60 admissible atoms /1,907 vertical rosters /809,566 disjoint unordered vertical pairs were independently regenerated as fixed count crosschecks. The only possible q0 mass on either side is <=292, because every vertical side costs at least 2039. Thus all q0 signed side multisets are contained in the 1,223 multisets of j=1,...,16 of mass <=292. The exact code enumerates all these multisets, uses H0 to match multiplicity counts, and retains each full named sign support, true two-side budgets and exact H1. Because overall sign exchange can orient n_vertical(+) <= n_vertical(-), these loops cover every possible signed candidate.

The exact counts are:

| Strictly scoped stage | Count |
|---|---:|
| H0 count-compatible q0 pair iterations | 1,944,619 |
| Also budget and opposite named q0-support disjoint | 167,928 |
| Full vertically support-disjoint H0 + H1 exact signed candidates | 333 |
| Also exact H2 | **0** |

For all 333 H0/H1 candidates, the least *nonzero* absolute difference in their **17²-scaled** second reciprocal moment is exactly 1/33075. Thus their actual |H2+ - H2-|, because H0/H1 have already cancelled the lower-degree terms, obeys

    |H2+ - H2-| >= 1/(33075*289) = 1/9558675.

That positive separation is attained by at least one of the checked H0/H1 candidates; no residual is zero. The exact rational scan is exhaustive for the declared finite class. [Reproducible H012 checker](https://github.com/awdawmip/enterprise-math/blob/6126ba113ef8a0bf68dc19a60e6330ffa5ff239a/research_checks/T6_P17_Q14_H012_EXACT_EMPTY_CHECK_20261122.py) and [finite certificate](https://github.com/awdawmip/enterprise-math/blob/95b0725fdbef26b15808cf4b5b72231a0113672b/research_checks/T6_P17_Q14_H012_EXACT_EMPTY_CERT_20261122.json) record the exact computation and assertions.

## Consequence, ownership and next direction

This is a new *model-internal exact elimination* of the named one-power p17 q14 split(7,7) before any affine computation. It refines the immediately preceding sharp 11 q0 multiplicity result and consumes its 333 candidates rather than claiming the predecessor's preflight again. It is not independent review or canonical source result publication. Scientific next step: confirm with a nonauthor review that this one-power input covers the intended frozen delegation-plan subcase; then inspect the uneliminated p17 subcases or actual canonical next selection. Do not mark the global p17 layer, H0-H6 or the original T6 mother objective DONE.

The native own continuation original onhour-20261122-1959-t6-own-current-continuation-v1 remains subject to exact original receipt. Earlier typed-prepares failed (scope budget and primary rate limit), not to be replayed. All prior X6 physical experiments remain separately pending.
