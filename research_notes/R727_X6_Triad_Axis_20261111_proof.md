# R727 — X6 equal-quantum triad incidence: exact decomposability, labeled BRC multiplicity, and a two-source lift obstruction

Date: 2026-11-11. Research mode: TASK_RESEARCH, author-side candidate math. Parent task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, immutable publication `TP2-8B7E13C5904A2D6F1142`. Frozen scientific input: `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. The last relevant author-side frontier was R726 / PR #2104. P000, the six signed native axes, three-dimensional slice terminology, and independent time typing remain unchanged.

## Typed scope and first concrete native-adjacent model

At one chosen native Cell `c`, a primitive *candidate* quantum is a source-labeled tuple `(source_id,c,axis_i,sign,positive_quantum,port_id,branch_id)`. Distinct sources are not identified; `axis_i` is one of the SIX existing positive axis families and `sign` is preserved as a separate field. Fix a common positive quantum magnitude. A candidate triad groups exactly three distinct source IDs at this Cell, with pairwise DISTINCT axis families (hence the three positive-axis labels satisfy P000 `PERP_E`). This is the **axis-incidence eligibility layer** of canonical equal-quantum three-force closure. A separate native `TRIADIC_CLOSURE_E` relation/certificate must decide which eligible triples really close. Axis distinctness by itself is not promoted to stability.

For one family of admissible witnesses, a typed cyclic port-incidence token `kappa=(p0->p1->p2->p0)` can be stored with an eligible triple, its source identities, signs and Cell. Port cyclicity is an explicit candidate operation, **not** an identification of native force closure with a classical vector sum or with an arbitrary three-force configuration. The group `S6` acts on the Cell's SIX signed chart coordinates and on axis-family labels by the same coordinate permutation; it transports source IDs, signs and the witness token without deletion. This supplies a mathematically exact finite rotation-skeleton action on the candidate typed incidence graph. A real Link/Port event law and lawful closure/witness generation remain to be extracted from the frozen native V29/V39 material.

## Theorem 1: sharp axis-incidence decomposition criterion

Let `m>=1`, and let `a=(a0,...,a5)` be the SIX axis-family occupation counts of `3m` individually labeled equal-magnitude nonzero sources attached to the same Cell. A decomposition into `m` unordered triples, each using three different axis families, exists **if and only if**

```
sum_i a_i = 3m   and   0 <= a_i <= m for every i.
```

This concerns the declared axis-incidence carrier. It is a necessary decomposition screen for an X6 canonical closure hypothesis that uses only pairwise-distinct positive-axis families; it does not alone produce native closure certificates.

**Proof.** A triple uses a family at most once, so `a_i<=m` is necessary. Conversely, order the six residual occupation counts nonincreasingly and choose the three *largest* positive counts. There are at least three positive counts, because their sum is `3m` and each is at most `m`. Every family with count equal to `m` must be among these three: four such families would already sum to `4m>3m`. Decrement the chosen three counts by one. The remaining counts are all between 0 and `m-1` and sum to `3(m-1)`. Apply induction. This constructs a decomposition in exactly `m` steps; sorting six counts each step gives an O(m) fixed-six-axis greedy algorithm. QED.

Example: `a=(3,1,1,1,0,0)`, `m=2`, has six total sources but needs three copies of axis 0 across only two triples, so no such decomposition exists. `a=(2,2,2,0,0,0)` is feasible; it permits multiple DISTINCT source-labeled decompositions even though every axis-identity triple is `012`.

## Theorem 2: exact number of BRC provenance-preserving decompositions

Set `E3(x)=sum_{0<=i<j<k<6} x_i x_j x_k`. For `sum a_i=3m`, let `L(a)` be the number of **unordered partitions of the distinct source IDs** into distinct-axis triples (each source used once). Then

```
L(a) = (prod_i a_i! / m!) * [x_0^a0 ... x_5^a5] E3(x)^m.
```

**Proof.** Expand `E3^m`; its monomials select one eligible axis triple in each of `m` *ordered* slots. The displayed coefficient counts these ordered axis-triple slots with the requested family occupations. For each such selection, source identities within each axis family may be assigned to the chosen appearances in exactly `prod_i a_i!` ways. Every resulting partition of distinct sources into unlabeled triples occurs exactly `m!` times under permutations of the triad slots. Therefore division by `m!` yields the asserted nonnegative integer. QED.

Explicit validated examples: `L(1,1,1,1,1,1)=10`; `L(2,2,2,0,0,0)=4`; `L(2,1,1,1,1,0)=6`; `L(3,1,1,1,0,0)=0`. The independent direct source-label recursion in the companion checker matches the coefficient formula for **all 56+462+2002** occupation vectors with `m=1,2,3`, including all impossible cases.

The full labeled decomposition is the BRC/Port provenance carrier. The axis occupation vector is a deliberate projection: it retains the existence decision and the above multiplicity, but cannot reconstruct the actual decomposition when `L(a)>1`. In particular, at `a=(1,1,1,1,1,1)` there are ten distinct pair-of-triad source assignments with identical occupation counts.

## Theorem 3: precise two-source hidden-axis residual

Fix an ordered pair of nonzero equal-magnitude source quanta attached at Cell `c` with **distinct** positive-axis families `i,j`. In the candidate incidence layer, exactly FOUR positive-axis families `k not in {i,j}` are eligible as the *third axis family*. Projecting an eligible triple to its two visible sources therefore has an exact 4-element hidden-axis fiber; recovering ONLY that axis choice requires at least `ceil(log2 4)=2` binary bits, and a two-bit index suffices. If a hidden sign is also an unrestricted part of the requested observable, the resulting 8 sign-and-axis choices require three bits. Additional source IDs, ports, branches or actual closure constraints have their own fibers.

For each candidate hidden family `k`, the future exact typed query `Q_k(T)=1[k is present among T's source axis families]` distinguishes it from the other three. Thus discarding the hidden family is not future-safe for the declared set of four queries. If a genuine native closure law excludes some candidates, replace this 4-element carrier by the *verified admissible* subset; its actual BRC entropy and observer-safe quotient are then computed from that subset.

The lift `two visible sources + hidden third source + actual closure certificate` supplies an exact candidate realization of the P000 apparent-two-force projection rule. The visible pair alone never constitutes a primitive stable event.

## Theorem 4: S6 covariance and candidate rotation dynamics

For every axis permutation `tau in S6`, permute all SIX Cell chart coordinates and every source's positive-axis family label by the same `tau`, leaving source identities, sign, quantum and cyclic port-witness ordering available. The distinct-axis triad predicate and equal-magnitude condition are preserved; the source-labeled partition sets are in bijection under `tau`, so `L(tau.a)=L(a)`. The maps `U_tau` on typed candidate states satisfy `U_tau U_sigma=U_(tau sigma)`. A cyclic permutation of the three ports preserves the explicitly typed 3-cycle incidence witness. These are exact combinatorial update/covariance laws on the current candidate model, not yet the physical X6 time evolution or a V29 PASS/TRANSFER event.

## Exact validation and scope

Companion Python standard-library checker `research_notes/R727_X6_Triad_Axis_20261111_verify.py` executes integer-only finite source-incidence calculations, with independent greedy construction, formal-coefficient recursion, and direct source-labeled partition recursion. It exhausts all `2520` count vectors for `m=1,2,3` (56+462+2002); eligible vector counts are `20,141,580`. The maximum labeled partition multiplicities are `1,10,124`, respectively. Verified marker: `R727_X6_TRIAD_AXIS_PARTITION_EXACT_PASS`. This computation is a finite-model check, while Theorems 1–4 have the stated combinatorial proofs.

## Unfinished mother-task dependency / decisive next input

Retrieve one exact LEGAL native `Cell/Link/Port` plus V29 `PASS/TRANSFER` or V39 loop-flow `j` event from the pinned scientific input or its true cited dependency. Write its force source identities, signed axes, exact Cell incidence, branch/port witness and native `TRIADIC_CLOSURE_E` decision. Apply the sharp criterion and exact BRC source count as an incidence *pre-screen*, then test whether the native closure law selects (a) all eligible triads, (b) an exact subset, or (c) a different incidence class. This identifies the exact missing native closure predicate without reverting to classical vector equilibrium or silently discarding provenance.

Formal source state at author publication: no CLAIM, semantic checkpoint, independent Driver review or P000/Foundation promotion is inferred.
