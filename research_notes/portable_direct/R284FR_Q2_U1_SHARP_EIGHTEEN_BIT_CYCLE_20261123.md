# R284FR — 无清除漏写四代循环：q=2、u=1 的十八位全局锐容量

Date: 2026-11-23 (Asia/Shanghai)  
Status: AUTHOR_PROVED / EXACT_EXHAUSTIVE_FINITE_LOWER_CERTIFICATE / NOT_REVIEWED  
Research mode: informed TASK_RESEARCH portable; no shared CLAIM or formal Result is asserted.

## Theorem R284FR-1

Within the inherited R284CO frozen four-fixed-word binary observer model, every publication attempts changed bits once in a fixed arbitrary order with at most two omitted attempts. Previously omitted physical-bit residuals may carry across an unlimited number of generations. A read can flip at most one arbitrary bit. A stateless decoder must always correctly recognize stable phases; during non-atomic publication it must never successfully identify a third phase, and never allow a successful new-phase read followed by an old-phase read.

Then the **global exact minimum number of binary tag coordinates** over *all* fixed four-word encodings, bit orders and stateless decoders is

    n_min(q=2,u=1) = 18.

The upper bound follows from the already published reset-free Gray two-block construction R284FC/R284FE, with group length K=2q+4u+1=9 and two Gray-controlled groups, hence n=2K=18. The lower bound combines R284FP's all-q,u=1 theorem excluding n<=15, R284FQ's exhaustive exclusion of n=16, and the newly completed exhaustive n=17 exclusion below.

## New n=17 lower-bound verification

A constant column can be removed; normalize c0=0 by complementing each coordinate history. Each of n=17 coordinates belongs to exactly one of the seven nonconstant three-bit patterns p=(c1,c2,c3). Histograms of their multiplicities form a complete coordinate-permutation quotient, containing

    C(17+6,6) = 100947

possible nonnegative seven-class vectors.

For every histogram, impose both:
1. the four adjacent publishing-prefix distance necessary bounds d(c_i,c_(i+1))>=2q+4u+1=9 and the opposite distance bounds >=2(q+u)+1=7; and
2. the exact R284FM capacitated last-update residual flow-cut separation for all six pairs of phases, using q=2 and u=1.

Precisely **208** histogram classes survive. For each, the checker calculates *all* stable physical words via the R284FM last-nominal-update group formula, and then all noisy words in the radius-one ball around these stable sets. These forced stable read labels are mandatory for every decoder, regardless of what it does on nonstable read words.

For each publication edge i->i+1 and each individual possible first write bit, the checker tests the legal *successful* first-bit attempt from every reachable stable source. If some resulting physical prefix x can, under permitted noisy reads, force either a third-phase label or both old and new labels, the first-bit choice is impossible. Exactly **108** of the original 208 histogram classes retain at least one permitted first-bit choice on all four edges.

Those 108 are ruled out by a *type-prefix lattice* calculation, whose validity does not assume a chosen complete bit order. Within a fixed column pattern type, all coordinates have identical nominal phase histories, so stable-source sets and mandatory read-label conditions are invariant under permutation of bit positions of that same type. Any fixed order on an edge therefore maps to a monotone lattice path of the count vector of attempted bits from each changed type. At a count vector v the attempted-bit set M(v) is fixed canonically. Exhaust every stable source s and every subset F of M(v) with |F|<=q. The exact prefix word is

    x(s,M,F) = ((s AND NOT M) OR (c_next AND M))
               XOR ((s XOR c_next) AND F).

Let Forced(x) be the union of labels that correct stable decoding would require on at least one radius-one observation of x. A prefix node is *locally safe* only if every s,F produces Forced(x) within {old,new}, with no physical prefix at which both old and new may succeed. Two possible reads at the same prefix with both labels would already violate no-new-to-old rollback.

Starting from all-zero counts, perform a breadth-first search that advances one type count only through locally safe nodes. Such a path is necessary for *any* possible legal write order; historical read choices or stronger no-rollback constraints cannot restore an absent path.

All **108/108** remaining histograms have some edge with no locally safe count path. In **97** cases publication edge 0->1 is already impossible; in the other **11**, edge 1->2 is impossible. Thus no n=17 scheme exists. No heuristic precision, random sampling, timeout-dependent cutoff or order constraint was used.

## Executed certificate

Standalone standard-library checker `R284FR_q2u1_n17_checker.py` imports the previous verified `R284FQ_q2u1_n16_checker.py` in this same directory to reuse the exact seven-pattern flow-cut and stable-state primitives, and adds the generalized multi-type prefix-lattice BFS. It sets the target width to 17 and asserts the precise complete finite counts:

| Classification | Exact count |
|---|---:|
| Seven-pattern histograms (17 bits) | 100947 |
| Pass all six flow cuts and necessary distances | 208 |
| Have at least one safe first bit on all four edges | 108 |
| Blocked on first publication edge | 97 |
| Further blocked on second publication edge | 11 |
| Survive a complete locally safe path on all four edges | 0 |

The checker was executed with Python standard-library exact integer operations on 2026-11-23 and exited with status 0. A companion JSON certificate contains these counts, the exact parameter scope, dependency path, and representative blocked histogram vectors. The earlier R284FQ checker also ran locally and excluded all 74,613 width-16 histograms by the same necessary-conditions method.

The **mathematical proof** is a finite exhaustive quotient plus exact necessary-certificate algorithms, supported by a previously proved explicit Gray upper construction. The result is author-verified, not independently reviewed or adopted as a formal Result.

## Source and exact continuation

- R284FP analytical all-q,u=1 lower bound and complete q=2,n=15 exclusion: `687270ced64588283633d28fde17fcefe8cf3df1:research_notes/portable_direct/R284FP_U1_EXTRA_BIT_NEAR_BOUNDARY_OBSTRUCTION_20261123.md`.
- R284FQ complete q=2,n=16 exclusion: `dbaf932b2f6fac3331084e955b172ec58719ab19:research_notes/portable_direct/R284FQ_Q2_U1_SIXTEEN_BIT_EXCLUSION_20261123.md`.
- R284FM exact residual/noisy cut: `1d1c5dd412719c7aaf016187b6493b77253cd9f9:research_notes/portable_direct/R284FM_NOISY_OBSERVER_FLOW_CUT_AND_ADDITIVE_LOWER_BOUND_20261123.md`.
- Explicit upper construction: R284FC/R284FE under frozen R284CO observer-code lineage, with two groups each 9 bits for q=2,u=1.
- P000, ACTIVE worldview, BRC/X6 and task's frozen inputs remain unchanged.

**Next useful problem:** Determine n_min(q,1) for q>=3. R284FP gives 4q+8 and the existing construction 4q+10, now with a sharp example at q=2. Seek a uniform symbolic prefix obstruction or nonseparable construction resolving one or both remaining bit positions, and later extend to arbitrary positive (q,u) and bank-data omission.
