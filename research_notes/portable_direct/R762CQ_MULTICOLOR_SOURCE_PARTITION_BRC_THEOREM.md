# R762CQ — K4 六轴任意来源等价划分的 BRC 一步充分性与 Johnson 分量定理

**Project:** Enterprise Math / RS-X6-TRIADIC-CLOSURE-DYNAMICS / TP2-8B7E13C5904A2D6F1142.  
**Date:** 2026-11-17. **Research status:** AUTHOR_DERIVED_AND_EXACT_FINITE_CHECKED; independent review NOT_REVIEWED.  
**Scientific inputs:** immutable taskbook/source e3f42efac29a2da2d95be391f3231a664e2fade0 and P000 V5 scientific freeze a72226e2430ffa4786321ac86e7f0c599d5f0389.  
**Preceding exact case:** R762CP, GitHub PR #2603 @ 851f3e9e487c0ee11f752365b7797ac5c7772c18.

## 1. Typed candidate model and the question

P000 fixes six native X6 spatial axes, twelve signed primitive directions, pairwise PERP_E at the native 120° relation, and primitive stable nonzero balance only as a three-force TRIADIC_CLOSURE_E event. The six X6 axes are temporarily labeled by the six edges `01,02,03,12,13,23` of K4 solely as a **six-label combinatorial carrier**, not as fewer native spatial dimensions. Force sign, time, Cell, Link, Port, path history, and oriented area remain separately typed and are not erased by the following observer.

Candidate states are the ten unordered partitions `A|A^c` of six distinct labels into 3+3, with F (four star/face partitions) or P (six path/path partitions) as current observation. Every candidate triple has equal nonzero quanta and pairwise PERP_E; actual signed event permission is an additional unsolved predicate.

Let `~` be **any equivalence relation on the six labels** representing equality of an added source tag (not native direction sign). The conditional exchange operator `T_~` replaces `x in A` with `y in A^c` exactly when `x~y`, retaining the identities of the exchanged labels. Each legal exchange contributes one positive integer N-BRC microbranch. This specializes R762CP's binary source-marked operator to arbitrarily many distinguishable source types. Labels may be renamed without changing their equality pattern, so precisely the sixth Bell number, **203**, cases cover all such source assignments.

## 2. Structural theorem: every connected component is an explicit Johnson product

Let source equivalence classes be `C_j`, with sizes `n_j` summing to 6. Choose an oriented representative A, `|A|=3`, and write `k_j=|A∩C_j|`, hence `sum k_j=3`. Under all permitted exchanges the entire vector `k` remains invariant; exchanging the two sides replaces it by `n-k`. Therefore the connected components of the **unordered** ten-state graph are indexed by complement orbits `{k,n-k}`.

For `k ≠ n-k`, a component is exactly the Cartesian product of Johnson graphs
`∏_j J(n_j,k_j)`.
For the self-complementary vector `k=n/2` (which requires all `n_j` even), it is the antipodal quotient of this product by the fixed-point-free global complement involution.

In both cases the component has precisely

```text
V(k) = [ ∏_j binom(n_j,k_j) ] / [ 2 if all k_j=n_j/2; otherwise 1 ],
d(k) = Σ_j k_j (n_j-k_j),
E(k) = V(k) d(k) / 2.
```

It is connected and `d(k)`-regular. The unrestricted positive N-BRC path count from any state of that component after exactly t candidate exchanges is `d(k)^t` (including 0^0=1 for the length-zero path). Its adjacency spectral radius is `d(k)`.

**Proof.** Each allowed move replaces a chosen element of `A∩C_j` by an element of `C_j\A`, preserving each `k_j`; these are exactly the edges of `J(n_j,k_j)` in one coordinate. Every Johnson graph, including singleton cases `k_j∈{0,n_j}`, is connected, so the product is connected. Taking unordered partitions identifies the occupancy choices `k` and `n-k`. When they differ, exactly one oriented side has the designated k, yielding an isomorphic component. When equal, complement acts freely, and an oriented neighbor differs in two of the six labels, whereas its complement differs in four; hence neither loops nor double-edges arise in the quotient, and degrees survive. The displayed vertex, degree and edge formulas follow. Regularity gives `T 1=d 1`; the row-sum bound on eigenvalue modulus together with eigenvalue d proves the spectral radius assertion. □

## 3. Exact finite theorem: one-step F/P count is sufficient for **every** source partition

Let `f=1_F`, `p=1_P` on ten states. Define the two-channel N-BRC future observer
`O_h(i)=(kind(i),((T_~^t f)(i),(T_~^t p)(i))_{t=0,...,h})`.
For **all source equivalence relations** on the six labels, equality of `O_1` is equivalent to equality of `O_h` for every integer `h≥1`. In particular, the `O_1` fibers are the **smallest exact sufficient state partition** for this declared future-count observation language.

This is an exact, exhaustive **finite computer-assisted proof**. The attached dependency-free verifier enumerates all 203 canonical restricted-growth strings (one per set partition of six labels); for each, it constructs all ten states and all cross-triple exchanges, groups states by `(kind,Tf,Tp)`, and checks for every pair of source/target groups that every source state has the same integer transition count into the target group. Thus each group partition is equitable. By induction, the two initial constant-on-block vectors `f,p` remain constant on blocks under every power of T. Conversely distinct `O_1` signatures are distinguished already at time 0 or 1. The verifier also checks all 24 K4 vertex relabelings across all 203 cases, graph-component cardinalities/degrees, and the binary-source regression against R762CP. This proof is finite and exhaustive because **every** equality pattern on six labels has a unique restricted-growth canonical representative.

### Complete output distribution

| Number of exact future states | Count of source partitions |
|---:|---:|
| 2 | 3 |
| 3 | 30 |
| 4 | 62 |
| 5 | 36 |
| 6 | 24 |
| 7 | 48 |
| **Total** | **203** |

Given the already observed F/P type, the minimal **worst-case fixed-length repair bits** are `ceil(log2(max(number of O1 blocks of type F, number of blocks of type P)))`. Across the 203 source patterns: zero bits for **3** patterns, one bit for **62**, two bits for **114**, and **three bits for 24** patterns. This maximum is achieved by a partition with five distinct future P classes. The finite exact certificate includes the profile-resolved table and all 203 per-pattern outputs.

The old two-color specialization is recovered exactly: among the 32 equality partitions with at most two source classes, the future-state histogram is `2:1, 3:13, 4:18`, matching the 64 binary assignments in R762CP after identifying global sign reversal.

## 4. Nonmonotonic observer distinguishability under source refinement

Fix label order `01,02,03,12,13,23`. Source equality pattern `001112` has **7** exact F/P-future observer classes. Split its first two-label source block to get the strictly finer pattern `012223`, which has **4** classes. In the other direction the all-equal pattern `000000` has 2 classes while `000001` has 3. Thus **refining the source tags (deleting allowed exchanges) is not monotone for this future-count distinguishability statistic**. The decisive data are the interaction graph and declared observer, rather than the mere number of source colors. Both refinement witnesses are included as exact verifier assertions.

## 5. Validation boundaries and continuation

**Exact validation:** 203/203 set partitions, all ten unlabeled 3+3 states and source-matching exchanges, component-size/degree certificates, all `203×24=4,872` K4 relabeling cases with 100 adjacency entries each (487,200 equivariance comparisons), equitable one-step observation blocks, and binary regression. Arithmetic is exact integer counting; no floating-point approximation is used for the claimed state classifications. Source-script runtime is standard ECMAScript with no external packages.

**Research scope:** This is a theorem about the declared **conditional source-equality exchange candidate** `T_~`. Its positive integer BRC counts do not implement signed force cancellation. A licensed native `TRIADIC_CLOSURE_E` signed Cell/Link/Port update and V17/V29/V39 event transport remain the mother's open hard target, along with how its allowed suffixes interrogate R762CH/CK oriented-area and provenance fibers. Source identity, Cell incidence, path order and higher joint residuals are retained outside the ten-state factor until observer-safe descent is separately proved.

**Next discriminating question:** Given one actual native event-permission kernel L on signed typed triads, test whether the 203-pattern `O_1` fibers are congruences for L and the licensed future Port observations; either exhibit an exact descent certificate or the shortest signed licensed suffix distinguishing a collapsed pair.

**Saved materials:** `R762CQ_MULTICOLOR_SOURCE_PARTITION_BRC_THEOREM.md`, `R762CQ_VERIFY.js`, `R762CQ_EVIDENCE.json`. **Independent mathematical review:** NOT_REVIEWED.
