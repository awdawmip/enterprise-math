# R63 — Absolute-phase persistent source index (seam-free circle queries)

2026-11-11. Frozen scientific pin: `43ec6098b1330ae86d0a7863be336c5d97f6ef34` (unchanged). Predecessor R62 draft PR #2058 / `c05df2a23f345ffd8c8d2afced449b1a5166f488`. Status: author-side mathematical proof with executable exact rational verification; independent mathematical review and task Result pending. Scope: exact labelled auxiliary circle rotation observer, with P000/native X6 ontology unchanged.

## The model

Fix a rational parameter `theta=p/q`, `0<p<q` integers. Let `h_z={z theta}`, `z=0,...,m-1`, be pairwise distinct (sufficient and necessary: `m<=q/gcd(p,q)`). Each original label z owns the counterclockwise half-open arc `A_z=[h_z,next(h_z))` on the circle, respecting the original label rather than its sorted rank. If `m=1`, the sole arc is the entire circle.

Given observation time `j`, observer phase `x in Q/Z` and finite active timestamp set `S subset {t in Z:t<j}` (each timestamp unique), define

```
tau_z(j,x,S) = min{ j-t : t in S, {x-(j-t)theta} in A_z },
```

with EMPTY for no matching source. Distinct timestamps may carry identical source phase.

## Theorem A — anchor-invariant index

Put `phi_t={t theta}` and `b(j,x)={x-j theta}`. Then

```
{x-(j-t)theta}={phi_t+b(j,x)}
tau_z(j,x,S) = j-max{ t in S : phi_t in A_z-b(j,x) }.
```

The tree's keys depend on the source timestamp and fixed parameter, **not** on observation time or observer phase. Changing j or x changes only the query arc; existing indexed versions require no rotation, split/join at a moving seam, or re-keying. Source phase is an integer residue `P_t=t*p mod q` and the unique index key is `(P_t,t)`. If several timestamps have equal phase, all share arc membership and the maximum t determines the minimum age. A wrapped query arc is a union of at most two disjoint half-open linear intervals. The m=1 query uses the whole-tree maximum.

**Proof.** Rewrite x-(j-t)theta=(x-j theta)+t theta, reduce modulo one and translate the entire half-open membership arc by the shared offset. For fixed j the minimum of ages j-t is achieved at the maximum eligible timestamp t. The branch at the circular cut is a disjoint interval partition, including every left boundary and excluding every right boundary. Two equal phases have the same arc membership; timestamp order selects the correct winner. QED.

This is a constructive implementation alternative to R62-C's moving-cut representation, obtained from its algebraic anchor-transport identity.

## Theorem B — persistent indexed queries

Use an immutable randomized Treap ordered by (phase,t), with `max_t` at each subtree. To compute the maximum timestamp among phases in `[L,U)`, first descend to a split node whose phase is inside the interval; if none exists the answer is EMPTY. Scan the lower-bound spine in its left subtree: at each qualifying node include the entire *right* subtree maximum; scan the upper-bound spine in its right subtree, including entire *left* subtree maxima. Every interval member lies on a spine or under one of these wholly included subtrees, and no excluded node contributes. Thus one interval query uses O(h) tree nodes for height h; a circular query uses at most two intervals.

Treap split/merge, insertion and deletion copy nodes only on changed spines and recompute `max_t` from children. Untouched subtrees share their exact immutable roots. By induction over updates, all prior versions retain their original source populations and exact queried ages. For independent random priorities and a non-adaptive fixed update schedule, expected height is O(log(n+1)). Hence an update takes expected O(log(n+1)) copied/visited nodes, a sparse label query expected O(log(n+1)) visits, and Q arbitrary old/new checkpoint queries expected O(Q log(n_max+1)) visits. Across U updates, retained roots use expected O(n_0+U log(n_max+1)+m) nodes plus O(U) root references and the priority dictionary. One-time history arc sorting costs O(m log m) comparisons and O(m) metadata; later original-label endpoint lookup is O(1).

**Proof.** Persistent split/merge preserve the ordered-key and priority-heap invariants. Each copied node recomputes the exact aggregate of its immutable subtree. The range-query spine decomposition contains every qualifying node exactly as a visited node or wholly included subtree. Standard random-priority Treap height bounds apply with the stated independence; structural sharing makes the inductive version invariant immediate. Theorem A converts the returned maximum timestamp to the desired original-label source age. QED.

## Precision and resources

For rational p/q, building a source key requires modular multiplication `t*p mod q`. For an observation, calculate `j*p mod q` and exact rational shifted arc endpoints, then perform tree key comparisons; returning the output subtracts `j-t`. Thus the expected logarithmic bounds above concern **tree operations**, not multi-precision bit work. Include initialization O(n log n) expected with individual insertions, history-boundary sorting, source identities and versions, random-priority generation, arithmetic bit length, and output size in total-cost comparisons. The code samples reproducible 128-bit pseudorandom priorities; the probabilistic height theorem assumes ideal independent priorities.

A frozen irrational theta inside `[p/q,(p+1)/q]` may alter the order of phases for huge timestamps. An exact rational-endpoint tree proves results only at that endpoint; a uniform interval claim requires certified comparisons or query-selective stability evidence. A large absolute timestamp can require extra precision even when the observed age window is short. The next task addresses this certification cost. This study keeps original source provenance in the carrier and outputs only the requested latest-age observer; no native six-dimensional physics conclusion follows from the auxiliary circle model.

## Executed verification and boundaries

Locally executed standard-library `check_r63.py` compared independent exact `Fraction` phase assignment against path-copy Treap queries: 360 random rational models (denominators 5–65); 14,400 arbitrary updates; 64,616 fresh exact label queries; 8,045 historical-version queries; 8,557 changed-observer queries with the tree unchanged; 360 timestamp pairs with equal phase and deletion of the newer source. All passed. The compact, independently executable `check_r63_min.py` also passed 3,000 updates, 15,198 exact current queries and 3,848 historical-version queries. Both used exact arithmetic.

Frozen S23/AV rational enclosure endpoints: `p=262204504569236716045286`, `q=10^24`, theta endpoints p/q and (p+1)/q, `m=128,H=225,j=10^12+128`. For each endpoint all original-label ages from a 225-node persistent tree equal independent direct assignment, with all 128 labels occupied and first 12 ages 61,60,...,50. Two nonzero/large-shift observer changes at each endpoint were independently checked without changing the tree. These are exact finite tests, not an independently accepted Result.

**Next R64:** query-selective parameter-interval certification for persistent trees (actual search comparisons plus relevant boundary crossings); a case of sparse stable output alongside changed unrelated phases; same-t multiple branch identifiers; matched integer-bit cost comparisons with R49/R56/R58/R59/R60/R61/R62.
