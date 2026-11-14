# EC49FOT — two four-label subset-dependent native BRC gauges in the frozen original corpus

Date: 2026-11-15. Scientific state: AUTHOR_PROVED / EXACT_FINITE_CHECKED / INDEPENDENT_WITNESS_RECALCULATION / NOT_REVIEWED.

**Frozen scientific input pin:** fc0f038e7bfd12c886b4d37f900bfb770c0f61ab. Original input SHA256: cd9a50799536d2b96230777b5392b1d742ceee896da05bb49aa097cf351e1d5e. Dataset: 94 original signed-prefix cache keys, 178,850 codewords, 38,169 seven-key configurations, labels 0..23, actual named roots 03/05/06/07. Prior frontiers: EC49FOR, EC49FOQ, EC49FOS.

## The precise finite theorem

For a frozen configuration K, E_l(K) is label l's set of legal named roots. Let D_r^K(S) be the exact rooted prefix-coverage cost for an attainable required label set S at named root r, computed with the original byte-prefix Trie. Let P(K) be the vector of all reachable rooted costs and T(K) the vector, indexed by every complete legal root allocation rho, of Phi_K(rho)=sum_r D_r^K(S_r(rho)).

The original 38,169 configurations form 625 distinct named legal-root classes. The 147 **entire** classes with between 5 and 64 members, inclusive, contain 3,780 configurations. Exact integer enumeration gives:

| Quantity | Value |
|---|---:|
| Complete legal-root classes | 147 |
| Configurations | 3,780 |
| Distinct within-class unordered configuration pairs | 68,266 |
| Reachable original rooted-cost entries | 682,446 |
| Complete-assignment total-cost evaluations | 1,702,588 |
| P-equal configuration pairs | 15,257 |
| T-equal configuration pairs | 15,261 |
| T-equal but P-unequal pairs | **4** |

The four exceptions, exhaustive in this collection, are:

| Configurations A → B | Representative of legal-root class | Complete allocations | Δ03 | Δ05 | Δ06 | Δ07 |
|---|---:|---:|---:|---|---|---|
| 17741 → 31699 | 105 | 256 | 0 | −4 on all subsets | +4 on all subsets | 0 |
| 24354 → 31700 | 105 | 256 | 0 | −2 on all subsets | +2 on all subsets | 0 |
| **16786 → 19592** | **16786** | **64** | 0 | 0 | conditional +1 | conditional −1 |
| **20706 → 35148** | **17035** | **64** | 0 | conditional +1 | 0 | conditional −1 |

Equal P vectors imply equal T vectors by direct summation. Exhaustiveness and the converse's exact four exceptions follow by enumerating every original configuration signature, every rooted subset cost, and every legal full allocation, comparing complete integer tuples (not approximate/hash-only equality).

## New first four-label gauge: 16786 → 19592

Let Q={7,13,17,21}. Every label in Q has precisely two choices, root 06 or root 07. Root 07 also has independent optional labels 5 and 15, shared with root 05. The actual original-cost differences between these configurations are:

* At root 06, ΔD_06(S)=+1 precisely for optional subset S={17}, and zero for its other 15 reachable subsets.
* At root 07, ΔD_07(S)=−1 precisely when S∩Q={7,13,21}, independently of the membership of optional labels 5 and 15. Exactly four of its 64 reachable subsets change.
* All reachable root 03 and 05 costs are unchanged.

For any complete legal assignment rho, let y_l=1[rho(l)=06] for l in Q. The two original root components have changes

\[
\Delta D_{06}(S_{06}(\rho))=g(\rho),\quad
\Delta D_{07}(S_{07}(\rho))=-g(\rho),\quad
g=y_{17}(1-y_7)(1-y_{13})(1-y_{21}).
\]

Thus **all 64** complete allocations have exactly the same total costs under A and B, while exactly four allocations have nonzero component changes (+1,-1). The multilinear polynomial g has a nonzero degree-four coefficient, namely −1 on y_7 y_13 y_17 y_21.

## New second four-label gauge: 20706 → 35148

Now Q={5,11,15,19}, each label choosing exclusively between root 05 and root 07. Root 07 also has independent optional choices 7 and 17 shared with root 06. The original rooted differences are:

* ΔD_05(S)=+1 precisely for optional subset S={15}, zero for its other 15 reachable subsets.
* ΔD_07(S)=−1 precisely when S∩Q={5,11,19}, independent of the choices for labels 7 and 17. Exactly four of its 64 reachable subsets change.
* The complete reachable root 03 and root 06 tables are unchanged.

With z_l=1[rho(l)=05], the two deltas are h and −h, where

\[
h=z_{15}(1-z_5)(1-z_{11})(1-z_{19}).
\]

All 64 total allocation costs agree exactly; four allocations show nonzero cancelling root changes. The degree-four multilinear coefficient of h is −1.

## Complementary-gate lemma

Let Q be m labels with exactly two legal roots a,b and p∈Q. Suppose the rooted-profile change at a is +c exactly when the selected Q-label subset is {p}, at b is −c exactly when the selected Q-label subset is Q\{p}, independent of all other optional labels; all other root changes vanish. Then the total cost change is zero for every complete legal allocation.

**Proof:** In any complete allocation, the Q subsets assigned to a and b form a partition of Q. The event that the a subset equals {p} is equivalent to the event that the b subset equals Q\{p}. Both changes thus occur together and cancel, or both vanish. For c≠0, a component equals c x_p product_{q∈Q\{p}}(1−x_q), which has a nonzero degree-m multilinear coefficient c(-1)^(m-1). QED.

Both original-corpus examples realize this algebraic lemma with m=4,c=1, under the original signed-prefix cost operator and the original immutable input. This proves that nonconstant root costs can represent an exact invisible total-cost residual, even though the rooted component residual has degree-four dependence on the allocation.

## Computation and independent checks

1. Reconstruct all 625 named legal-root signatures from the original file and select every class with size 5..64. This yields exactly 147 classes and 3,780 IDs. No random sampling.
2. For each selected configuration/root, rebuild the original signed-byte prefix Trie, propagate exact subset-coverage minima with integer arithmetic, and apply subset minima to produce every reachable root cost. The final data has exactly 682,446 unique (configuration,root,optional subset) entries, with all expected subsets of all 3,780 configurations. Interrupted incomplete rows were excluded and recalculated.
3. Enumerate all complete legal allocations, calculate full total integer vectors, and compare entire root and terminal tuples for every within-class pair. The class-results CSV certifies 68,266 comparisons with exactly four nonzero gauges.
4. An **independent Python byte-prefix-Trie implementation** reconstructs the eight source configurations for the four witness pairs from original codewords, checks every affected/unchanged rooted coordinate, and verifies all 256+256+64+64=640 legal allocations. Both four-label support formulas are checked exactly.
5. The original C++17 extractor compiled under both -O2 and -O3 yields identical values on 1,444 rooted-cost coordinates of those eight configurations.

Reproducible material: the evidence archive EC49FOT_SUBSET_DEPENDENT_GAUGE_EVIDENCE_20261115.tar.xz (SHA256 ef45a1b2b23319a000c53e0a208854d7ad55537feba65da6a220252ae0507e25) contains original frozen input, all 682,446 raw root costs, 147-class membership, independent verification programs, C++ source, source logs and SHA256 manifest. The two Python programs run from the extracted evidence directory; the independent program reads only original input to reproduce the four witnesses.

## Boundary and next research unit

Prior EC49FOR completed 390 original legal-root classes (including two larger classes), EC49FOQ completed one 966-config class, and EC49FOS completed one 2368-config class. The additional 147 completed here bring the complete-class coverage to **539/625**, leaving **86** original classes to investigate. The next useful question is whether the remaining classes contain higher-order m≥5 gates or additional mixed-root kernel structures, using exact native subsets before full terminal comparison.

Identity/owner control: a current Research Control Center read returned BACKEND_IDENTITY_CHECK_UNAVAILABLE with operation_sent=false, so a current native researcher identity, active CLAIM, Activity checkpoint or formal Result is not asserted. This material is independent portable mathematical research; mathematical review remains NOT_REVIEWED. GitHub branch/PR publication is Source artifact persistence, not a native task acceptance.
