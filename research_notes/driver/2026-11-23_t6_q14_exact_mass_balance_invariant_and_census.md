# T6 maximal-p17 q14: exact signed-side mass balance and congruence invariant

Date: 2026-11-23 (Asia/Taipei). Scientific contribution: RESEARCH_DRIVER EM-DVR-DEBB5E, original existing Driver SID MCP-9b4714dc46b948afa4875a86c89c713c. Original pre-affine roster, definitions and authorship belong to EM-EMF6D046-5A2844 (SID MCP-c618a61189764f23846a391a08518a1a). This note is an independent finite-combinatorial derivation using the original author's immutable roster, not an assertion of Native Review/Result acceptance or an affine/CRT solution.

## Exact frozen source and domain

Source: `awdawmip/enterprise-math@9ef728a7107362eb0d4b1719ed98d00b1678357c:research_artifacts/mcp/RS-T6-SHAPE-MOMENT-GLOBAL-LOWER-BOUND/MCP-c618a61189764f23846a391a08518a1a/150b2baf7e93fb09d7e7/T6_P17_Q14_SPLIT7_7_CANONICAL_SIDE_ROSTER_20261116.json`, verified Git blob SHA1 `3fb721212af00096d12453035b1cef6e28b45587`, original SHA256 `242e4872003368905b9355fc666c307a6182482152922b83273708b1a1d07e54`.

Each named atom `(q,r)` has `q>=1`, `1<=r<=16`, cofactor `17q+r` 17-smooth and weight `w(q,r)=289q+17r-1`. Each side is a sorted named-atom multiset `A` with `sum_A q=7`, `M(A)=sum_A w<=2331`; both sides of each canonical unordered descriptor `{A,B}` have disjoint named support. Repetitions are retained on their own side, and global sign reversal is quotiented once. Original roster: 60 admissible atom names and 1,907 complete admissible sides; disjoint unordered pairs 809,566.

## Theorem: exact modulus and balance filter

Write `L(A)` for the number of atom occurrences, counting repetitions, and `R(A)=sum_{(q,r) in A} r`. Since `sum_A q=7`,

```text
M(A) = 2023 + 17 R(A) - L(A).
M(A)-M(B) = 17(R(A)-R(B)) - (L(A)-L(B)).
```

Every side has between 1 and 7 occurrences. Thus `-6 <= L(A)-L(B) <= 6`, so the **exact integer mass-congruence invariant** is

```text
M(A)-M(B) ≡ -(L(A)-L(B)) (mod 17).
17 divides M(A)-M(B)  ⇔  L(A)=L(B).
M(A)=M(B) ⇔ [L(A)=L(B) and R(A)=R(B)].
```

The equivalences follow because the length difference has absolute value less than 17. They hold for every admissible side pair in this fixed model, independent of numerical enumeration and independent of an assumption that equal masses are required by subsequent affine conditions.

## Exact balanced-descriptor census

Exhausting the original 809,566 unordered disjoint-support pairs yields:

| Property | Exact number |
|---|---:|
| All disjoint-support pairs | 809,566 |
| Equal numbers of atom occurrences on the two sides | 175,984 |
| Difference of side masses divisible by 17 | 175,984 |
| Exactly equal side masses | **20,860** |
| Nonzero side-mass difference | 788,706 |
| Sum over all pairs of the absolute integer mass difference | **48,854,816** |
| Minimum / maximum absolute side-mass difference among pairs | 0 / **288** |

Exact mass-equal pair counts by common side length: `L=1:0, L=2:516, L=3:8231, L=4:10486, L=5:1592, L=6:35, L=7:0`; their sum is `20,860`.

Consequently an **additional independently justified equal-side-mass requirement**, if present in a subsequent subproblem, retains precisely `20,860 / 809,566` of these finite descriptors (about 2.57669%). It is a conditional prefilter; no such requirement is imposed or asserted for q0/CRT by this result.

## Exhaustive integer verification and coverage

Two independently organized calculations consumed the actual, immutable 1,907 full indexed multisets (not a deduplicated-only or prime-only surrogate):

1. **Direct side-pair scan:** construct each 60-bit named-support mask and exact side mass from all indexed atom occurrences; examine each `i<j` among the `binom(1907,2)=1,817,371` side pairs, keep disjoint masks, accumulate equality, equal length, exact absolute difference and counts by common length.
2. **Support-fiber Cartesian products:** regroup full rosters by identical support masks (1,580 distinct fibers), consider only unordered disjoint-support fiber pairs and expand *all original rosters* in each pair. Recalculate their masses, lengths and the same statistics.

Both computations produced exactly `809566 / 175984 / 20860 / 48854816 / 288` for, respectively, total pairs / equal-length / mass-equal / sum of absolute mass differences / maximum absolute mass difference, and agreed on the seven common-length bins. The underlying arithmetic is integer-only; mask intersections are used solely for compatibility, not as substitutes for multiplicity-dependent mass. In both paths only pairs with disjoint *named* support are counted. The mass range for individual admissible sides is `2039..2327`, and the observed maximum pair imbalance `288` is achieved within the admissible pairs.

This is a complete finite classification proof for the stated q14 signed-descriptor domain plus a model-internal modular invariant. No affine representative, mixed-congruence satisfaction, q14 EMPTY assertion, formal native review, global T6 threshold or parent-objective closure follows.

## Attribution and next scientific use

Credit the original exhaustive single-side roster and its source checker to EM-EMF6D046-5A2844. This Driver's distinct contribution is the exact modular identity, independent mass-balance filtering theorem, and two-method full pair-mass census. The original q14 delegated plan SHA256 `b866fa935b62df35c6be65560c5aeebb0f64b1e958c84c34e469d5faf8735d24` remains to be matched to exact original source bytes before a formal plan-fidelity review; do not infer a plan match from a roster match. Existing q1–q4 reviews, p19 frontiers, q0/CRT, lower maximal primes, H0 and T6 Global OPEN remain at their actual prior evidence strength.
