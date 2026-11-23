# R284FQ — 持久漏写四代循环：q=2、u=1 时排除全部 16 位标签

Date: 2026-11-23 (Asia/Shanghai)  
Status: AUTHOR_PROVED_BY_EXHAUSTIVE_FINITE_INTEGER_CERTIFICATE / NOT_REVIEWED  
Mode: informed TASK_RESEARCH portable research. No shared CLAIM, formal Result, or independent mathematical Review is asserted.

## 1. Exact claim

Continue R284FP and the frozen R284CO scientific lineage without changing any frozen inputs, P000 or ACTIVE worldview.

Four distinct fixed n-bit tags c0,c1,c2,c3 repeat cyclically. Each phase publication attempts every changed bit exactly once in a fixed but otherwise arbitrary order; at most q=2 attempts may be omitted per publication, and all legacy omitted-bit residuals can survive arbitrarily many cycles. A read may flip at most u=1 arbitrary bit. A stateless decoder is required to identify every completed stable phase correctly and, during non-atomic publishing, to produce no successful third-phase reading and no new-phase success followed by old-phase success.

**Theorem R284FQ-1.** Every such protocol has

    n_min(2,1) >= 17.

The previously available reset-free Gray construction yields n_min(2,1)<=18. Thus the sharp capacity lies in the two-element set {17,18}. R284FP independently proved n_min(2,1)>=16; this note excludes n=16.

## 2. Why 16-bit testing is complete

Normalize c0=0 by complementing whole coordinate histories and delete constant coordinates. Every remaining bit belongs to one of seven nonconstant pattern classes p=1,...,7 defined by its three target bits (c1,c2,c3). Coordinate permutations preserve all endpoint, omission, noise and legal-order conditions when the order is relabeled accordingly. Therefore the nonnegative histogram (x1,...,x7) with sum 16 is a complete quotient of all four-code choices: exactly C(22,6)=74,613 histograms.

The checker enforces each of the four necessary adjacent-phase prefix Hamming distances (at least 2q+4u+1=9), the two opposite distance minima (at least 2(q+u)+1=7), and the R284FM exact stable/noisy flow-cut separation criterion for all six unordered phase pairs. The six cuts are calculated from last-nominal-update provenance, not from an undifferentiated Hamming ball of radius q+u. Exactly **36** histograms pass these necessary conditions.

For any phase i, partition active coordinates into four last-nominal-update groups G_(i,e), e=0,1,2,3. R284FM proves the full unbounded-omission-history stable state set is precisely

    S_i = {c_i XOR (F_0 union F_1 union F_2 union F_3):
           F_e subset G_(i,e), |F_e|<=2}.

The displayed union is disjoint because every coordinate has exactly one most recent nominal update edge. The implementation forms all these exact finite sets, then marks all read words y at Hamming distance at most one from S_i as forced to decode i. A candidate with intersecting stable read balls is rejected. At a physical prefix x, let L(x) be the set of *all* phase labels forced by some permitted one-bit read of x. A third-phase label in L(x) is forbidden, and if L(x) contains both the old and new labels, two reads of that very same prefix can return new followed by old, which is also forbidden.

Of the 36 six-cut survivors, **28** already have some publication edge on which *every possible first successfully written bit* is unsafe, over all stable sources. The remaining **eight** histograms contain only types 3, 5 and 6, making each edge a publication of one or two homogeneous coordinate types.

For each of the eight, each edge and each pair (a,b) of attempted counts from its two changed classes, the checker fixes canonical within-class bit order and exhausts (1) every physical source in S_i and (2) every omission mask of size <=2 among the a+b attempted coordinates. It computes

    prefix = ((source AND NOT attempted_mask) OR (target AND attempted_mask))
             XOR ((source XOR target) AND omitted_mask).

This checks a **necessary** safety condition for every legal prefix, independent of previous read choices. Because every class has identical four-phase target history and its stable source set is invariant under within-class coordinate permutations, any legal fixed bit order induces a monotone (a,b)-path from (0,0) to (A,B). Such an order can work only if every nonzero lattice node on its path is locally safe. The checker performs an exact finite lattice reachability calculation; in all eight cases, at least one publication edge has **no** all-safe path. Stronger history-dependent no-rollback checking would only exclude more schemes. Thus no fixed order survives at n=16.

## 3. Exact computation

Run the companion standalone Python 3 standard-library checker:

    python R284FQ_q2u1_n16_checker.py

All arithmetic, Hamming ball membership, omission masks, flow-cut capacities and grid reachability use exact integers. The program asserts the complete histogram and survivor counts and emits a compact JSON certificate.

| (x3,x5,x6), other counts=0 | Stable state counts (phases 0,1,2,3) | Edges with no locally safe path |
|---|---|---|
| (0,9,7) | (137,1334,137,1334) | 1,3 |
| (1,8,7) | (242,1334,242,1334) | 0,1,2,3 |
| (5,5,6) | (1072,1232,1072,1232) | 0,1,2,3 |
| (6,4,6) | (1232,1232,1232,1232) | 0,1,2,3 |
| (6,5,5) | (1232,1072,1232,1072) | 0,1,2,3 |
| (7,2,7) | (1334,1334,1334,1334) | 0,1,2,3 |
| (7,8,1) | (1334,242,1334,242) | 0,1,2,3 |
| (7,9,0) | (1334,137,1334,137) | 0,2 |

The script was actually run locally with exit status 0 on 2026-11-23. Results: 74,613 histograms, 36 six-flow-cut survivors, eight remaining after all first-bit tests, and zero remaining after full homogeneous-prefix-grid necessary checks. No independent mathematical Review has been performed.

## 4. Source provenance and next question

- Previous R284FP: `research_notes/portable_direct/R284FP_U1_EXTRA_BIT_NEAR_BOUNDARY_OBSTRUCTION_20261123.md`, Enterprise Math commit `687270ced64588283633d28fde17fcefe8cf3df1`.
- R284FO all-parameter bound and type conventions: `research_notes/portable_direct/R284FO_ALL_NOISE_GLOBAL_CYCLE_LOWER_BOUND_20261123.md`, commit `f6869ad1c8ad8896fb60fda9a41bd747375bab49`.
- R284FM exact noisy residual flow-cut theorem: `research_notes/portable_direct/R284FM_NOISY_OBSERVER_FLOW_CUT_AND_ADDITIVE_LOWER_BOUND_20261123.md`, commit `1d1c5dd412719c7aaf016187b6493b77253cd9f9`.
- The finite result is in the inherited four-code observer model; it does not infer native six-axis geometric results, modify P000, or assert a BRC numerical computation.

**Next:** Test whether n=17 is achievable for (q,u)=(2,1). Use full prefix/no-rollback oracle only on candidates surviving the six cuts and the local prefix grid. If n=17 is impossible, the existing 18-bit Gray construction proves the sharp capacity. In parallel, try to generalize the extra-bit prefix obstruction to all q>=3, u=1 without redoing the R284FO analytic work.
