# PREFIX-800 — Exact cut certificates for partial chord assignments in bounded provenance-count fibers

Date: 2026-11-15. Researcher: EM-DIRECT-4660FF (independent TASK_RESEARCH). Scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Predecessor: PREFIX-799, `99dfd7d2bc31a02d3842c6f368a5ff8a98926e5b`. Status: AUTHOR_PROVED / EXACT_FINITE_REGRESSION / NOT_REVIEWED / NOT_ADMITTED.

## Problem and carrier

Let `G=(U,V,E)` be a finite bipartite source graph, `U={1,...,b}`, `V={1,...,c}`. Every edge has a **nonnegative integer capacity** `K_ij`; absent edges have capacity zero. A named positive-multiplicity source table `x` is an integer table satisfying `0<=x_ij<=K_ij`, row marginals `r_i`, and column marginals `s_j`. Every feasible table is counted once; retain its source-edge identity. These data are an external integer BRC source-count observer, not an asserted native X6 Cell/Link/Port update.

Select a spanning forest `T` of the positive-capacity support and its complement `C=E\T` (chords), as in PREFIX-799. Fix only a **partial** set of chord values `F subset C`, with `x_e=t_e`. Set `R_i=r_i-sum_{(i,j) in F}t_ij`, `S_j=s_j-sum_{(i,j) in F}t_ij`. Let `U_F=E\F`; its capacities are the original `K_ij`. If any residual marginal is negative or the total row and column residuals differ, the partial assignment is infeasible.

## Theorem 800.1 — Exact partial-assignment cut criterion

Assume `R_i,S_j` are nonnegative integers and `sum R=sum S`. The partial chord assignment has a completion to a feasible integer table **if and only if**, for every subset `A subset U`,

```
sum_{i in A} R_i <= sum_{j in V} min(S_j, sum_{i in A:(i,j) in U_F} K_ij).       (H_A)
```

For a failed inequality, `A` together with the displayed demand and capacity is an exact finite infeasibility certificate. All terms are integers.

**Proof.** Construct a directed network `source -> row i` of capacity `R_i`, `row i -> column j` of capacity `K_ij` on the unfixed edges, and `column j -> sink` of capacity `S_j`. A feasible completion is exactly a flow of value `D=sum_i R_i`. For an s–t cut whose source side contains exactly row subset A and column subset B, its capacity is

```
sum_{i notin A} R_i + sum_{j in B} S_j + sum_{i in A,j notin B:(i,j) in U_F} K_ij.
```

The inequality that this capacity is at least D is `sum_{i in A} R_i <= sum_{j in B}S_j+sum_{j notin B}sum_{i in A}K_ij`. Minimizing independently over whether each column j lies in B gives (H_A). Max-flow/min-cut proves real feasibility. All capacities are integers, so an integer maximum flow exists, yielding the required integer completion. QED.

## Theorem 800.2 — Source-faithful cut-pruned chord enumeration

Visit chord variables in any fixed order, and at every prefix prune exactly when Theorem 800.1 fails. At a full chord assignment solve the forest's unique integer edge completion by repeatedly removing a leaf and assigning the remaining row/column demand. The procedure returns **each feasible named integer source table exactly once**, and no infeasible table. It therefore computes, for any finite collection of integer linear observers `Q_1,...,Q_d`, the exact joint histogram

```
H(z_1,...,z_d)=sum_{x feasible} z_1^{Q_1(x)} ... z_d^{Q_d(x)}.
```

Negative integer exponents are allowed (a Laurent polynomial). More generally, source-labeled positive integer weights may replace unit coefficients without changing completeness, provided they are assigned per completed table and not factored across dependent chords.

**Proof.** Every feasible table restricts to exactly one chord tuple. At every prefix, that table itself witnesses feasibility of all (H_A), so it cannot be pruned. Once all chord values are fixed, two completions would differ only on a forest and have zero row/column sums; a leaf forces the difference there to zero, and induction removes all edges. The leaf algorithm either returns that unique bounded table or rejects it. Conversely, every returned table satisfies all original margins, capacities and source labels. Thus enumeration and the stated joint generating function are exact. QED.

**Complexity scope.** Hall evaluation takes at most `(2^b-1)*O(bc)` elementary integer additions/comparisons per chord-prefix under direct recomputation, and the full search remains exponential in the number of chords. This is an exact conditional pruning certificate, not a uniform speedup. The count of visited chord search nodes cannot exceed the corresponding unpruned tree, but calculating cuts consumes work.

## Concrete early-pruning witness

Take `b=2,c=4`, all eight capacities equal to 1, `r=(1,3)`, `s=(1,1,1,1)`. Choose tree edges across all top-row columns and bottom-row column 1, so bottom-row columns 2,3,4 are chords. After fixing `x_(2,2)=x_(2,3)=0`, the unfinished bottom row demands 3 while the two remaining bottom-row edges have aggregate capacity 2. The row subset `A={bottom row}` violates (H_A) by 1. The third chord has not yet been assigned: the algorithm can prune a genuinely **partial** source allocation.

## Exact finite evidence and measured cost

Reproduction: `research_notes/portable_direct/PREFIX800_R6_HALL_CHORD_CHECK.py` (Python standard library only); structured output: `PREFIX800_R6_HALL_CHORD_RESULTS.json`. Families are exhaustive for **all capacity patterns and all feasible margin fibers** of: 2x3 with `K_ij in {0,1,2}` (729 patterns); 3x3 with `K_ij in {0,1}` (512 patterns); 2x4 with all `K_ij=1` (one pattern). Three enumerators (direct rowwise, unpruned forest-chord, Hall-pruned forest-chord) and two distinct signed integer linear-observer histograms are compared exactly.

Results: 1,242 capacity patterns; 57,395 feasible marginal fibers; 66,595 complete named source tables; 114,791 Python assertions, all passed. Unpruned chord search visits 246,602 nodes and 155,181 leaves. Cut-pruned search visits 194,900 nodes and 66,595 leaves, with 62,390 infeasible prefixes cut and strict node savings in 15,420 fibers. Thus 51,702 fewer search nodes and 88,586 fewer leaf completions on this declared domain.

Separate implementation profiling (different supplementary implementation of the same exact model) measured approximately 0.53s direct row enumeration, 1.11s unpruned chords, 2.33s recomputed Hall cuts and 2.44s recomputed maximum-flow cuts, aggregated across this same finite domain in one local process. These are process- and implementation-specific timings. Cut pruning reduced the explored tree but the **naive per-node feasibility test was slower**; caching residual cuts or incremental bounds is the next algorithmic question. The primary portable checker verifies counts and exact histograms; the supplementary timing observations are not a portable performance guarantee.

The proof's universal domain is arbitrary finite bipartite nonnegative integer transportation fibers. The tests are finite implementation checks, and the native X6 interface transfer remains an open mapping obligation.

## Scientific provenance and next executable unit

Inputs and earlier mathematics: PREFIX-795 (cycle-rank tomography), PREFIX-796 (residual capacity-flow), PREFIX-797 (multi-cell projections), PREFIX-798 (weighted histograms), PREFIX-799 (optimal forest-chord coordinates). No existing manuscript is re-proved here. P000 and ACTIVE Heartbeat-World six-dimensional/timed three-axis-slice ontology are preserved; these are **external source-indexed integer-count** calculations, not an alternative classical model for native physics.

Next: derive incremental Hall updates and cache states by residual row/column capacities; benchmark the full cost of both positive-weight BRC source-observer computation and memory against row-transfer enumeration on dense and sparse graph families; finally give a typed mapping from a declared X6 Cell/Link/Port event to one nonnegative source table, including signed provenance and event-time constraints if used.

Control observation (original native read `r6-20261115-1254-prefix800-owner-read`, SUCCEEDED at 2026-11-15T04:56:48Z): `RS-X6-NATIVE-TIME-DYNAMICS` was `NEEDS_DISPATCH` with `actor=null,claim_id=null`; its exact typed continuation requires an authenticated new CLAIM. This work uses independent own registered researcher Activity, and asserts no shared CLAIM, new native Result or independent review.
