# R5: exact bridge-resource spectrum, unbounded composition, and provenance residual

**Date:** 2026-11-15 (Asia/Shanghai)  
**Frozen scientific input:** 435e77af0d180eac32bd1f9c4c464bc4010b7551  
**Scope:** auxiliary R5 mixed-weighted indexed-center one-step replacement observer; radius 2.  
**Evidence:** AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.  
**Prior frontier:** [separated-star theorem](../r5_multistar_source_kernel_20261115/SEPARATED_STAR_RESIDUAL_KERNEL_AND_AB_RIGIDITY_THEOREM.md) and [bridge sharpness](../r5_multistar_source_kernel_20261115/OVERLAP_DISTANCE_TWO_BRIDGE_SHARPNESS.md), both at commit c103beb0370288707445bb4e56c8d5d08e91375f.

## 1. Exact shared definitions

The five old indexed cores are O0=0125, O1=0135, O2=0235, O3=0245, O4=0246. The single-a new core/first-bit pairs are (1235,1), (1245,1), (1246,1), (1345,0), (1346,0). Joint closure ab adds (1236,1). An old resource (Oj,s,u) covers a new target (C,t,v) exactly when

~~~text
rho((C,t,v),(Oj,s,u)) = |C \ Oj| + [t != s] + Hamming(u,v) <= 2.
~~~

For old suffix language X and target language Y, kappa_T(X,Y;2) is the minimum number of distinct admissible old resources covering all T-targets. Suffix labels, indexed cores and first bits are retained.

## 2. Local bridge theorem

In the four-bit cube, let

~~~text
Y = {1,2,4,11,13,14}
G5 = {1,4,13}; G10 = {2,11,14}
H subseteq {5,10}; X_H = Y union H.
~~~

The target set has pairwise Hamming distance at least 2, and its exact distance-one neighborhoods at suffixes 5 and 10 are G5 and G10 respectively. For all four old-helper configurations,

**Theorem A.**

~~~text
kappa_a(X_H,Y;2) = 12 - |H|
kappa_ab(X_H,Y;2) = 12.
~~~

Thus the single-a values for H=empty, {5}, {10}, {5,10} are exactly 12, 11, 11, 10.

**Lower bound.** For each y in Y, the target E_y=(1346,0,y) forces exactly one baseline resource, either (O1,0,y) or (O4,0,y). This follows from its core distance row (3,2,3,3,2) and radius-two budget. The six baselines are all distinct. Relative to the three further critical targets B_y=(1245,1,y), C_y=(1246,1,y), D_y=(1345,0,y), an O1 baseline leaves B,C uncovered, and an O4 baseline leaves B,D uncovered.

An old source with suffix in Y can affect only the matching target suffix, because distinct target words have Hamming distance at least 2 and every core distance is >=1. Sources with suffix 5 reach only G5, while suffix 10 reach only G10. At distance one in the suffix, any *single* bridge source (Oj,s,h) can reach at most one of B_y,C_y,D_y for each neighbor y: the core/first-bit terms must consume exactly one remaining unit.

Fix a group Gh of three suffixes. If h is absent, each y needs an additional same-suffix resource for B_y, so at least three resources in addition to its three baselines. If h is available, at least two additional sources are required: a single same-suffix source touches only one of the three y, and a single bridge source repairs at most one of the two outstanding critical types for each y. No resource spans both groups. Total cost is therefore at least

~~~text
6 baselines + (3 if 5 absent else 2) + (3 if 10 absent else 2)
= 12 - |H|.
~~~

**Matching construction.** Keep all six baselines (O1,0,y). For each h=5,10, add (O0,1,h) and (O4,1,h) if h is allowed; otherwise add (O0,1,y) for every y in Gh. Each baseline covers the 1235, 1345 and 1346 targets at y. The corresponding bridge pair covers 1245 and 1246 at every y in Gh; a local O0 source covers both at its own suffix. All five core targets are covered by exactly 12-|H| sources. Joint-closure rigidity from the cited prior theorem gives kappa_ab=2|Y|=12 for every X_H. QED.

## 3. Unbounded guarded bridge family

For any integer k>=1, use d=4+3k suffix bits and guard

~~~text
g_i = 2^(4+3i) + 2^(5+3i) + 2^(6+3i),  i=0,...,k-1.
Y_i = {g_i OR y : y in Y}
X_i = Y_i union {g_i OR h : h in H_i},
H_i any subset of {5,10}.
Y^(k) = union_i Y_i; X^(k) = union_i X_i.
~~~

Distinct guards are Hamming-distance six, and the local four bits are disjoint from guards. Distinct Y_i therefore have mutual Hamming separation at least six. Every source capable of reaching a target belongs to a unique gadget. The inherited separated-target theorem applies, and the local lower/upper arguments tensorize.

**Theorem B, for all k and all 4^k helper assignments:**

~~~text
kappa_a(X^(k),Y^(k);2)  = 12k - sum_i |H_i|,
kappa_ab(X^(k),Y^(k);2) = 12k.
~~~

The maximum exact bridge saving is 2k. These are *cross-star* helper resources 5 and 10; neither is the center 0 or 15 of the two original stars. The construction retains old-source provenance by (core, bit, guard, local suffix).

## 4. Smallest sufficient residual depends on the observer

For the query family consisting of all singleton-gadget queries, the **cardinality-only** vector gives 12-|H_i| for each i. There are 3^k different cardinality response vectors. Thus an exact deterministic cardinality quotient has at least 3^k states, achieved by the ternary residual tuple (|H_i|). Its binary information requirement is ceil(k log2 3).

For the same queries when an **actual optimal source-labeled library** must be produced, all 4^k helper languages are distinguishable. In particular, H={5} and H={10} have the same cardinality 11, but no single eleven-source library is admissible in both worlds: the two old languages intersect only in Y, for which the minimum is 12. Zero-helper and two-helper cases already differ in cardinality. Therefore a deterministic source-witness quotient requires at least 4^k states, i.e. 2k bits. The two helper-membership bits per gadget are sufficient via the displayed construction. This is a proved one-step, query-family-relative minimality statement, not a claim about unrestricted future dynamics.

## 5. Verification, preservation and continuation

Companion standalone Python code recomputes the six core-distance rows and forced baselines from index sets using exact integer operations; it validates the bridge critical-target deficits and every upper witness. All four local cases and all 4^k helper assignments for k=1,2,3,4 are checked (4+16+64+256=340 guarded-family cases). No floating arithmetic, heuristic optimizer, or imported theorem checker is needed for these checks. Universal results are established by the proofs above.

Scientific scope is the inherited auxiliary indexed-center observer, with unchanged frozen input pin; P000, ACTIVE Heartbeat World, and native X6 relation/coordinate contracts are preserved. This note is not a native X6 transfer or independent review.

**Next independent problem:** remove the guard separation and study overlapping *chains* of bridge neighborhoods. Seek a provenance-retaining finite-state transfer for kappa and all optimal-source witnesses, preserving separately the old resource language X and future target language Y.
