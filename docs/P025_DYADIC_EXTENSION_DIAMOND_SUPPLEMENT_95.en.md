# P025 Supplement 95 — Biaxial Extension Diamond and Representation Pareto Frontier

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-orbit-normal-stage91`  
Depends on: P025 Supplements 93–94  
Hard block: `NONE`

## 1. Two extension languages act on the same semantic state

Stage 94 identifies two primitive future extensions of the finite Ferrers precision state:

1. insert one new threshold;
2. append one new orbit node.

Each operation is exact, but their preferred local coordinates differ.

Stage 95 asks two structural questions:

- do the two extension operations commute on the semantic state?
- can one representation dominate the others simultaneously in storage and both update directions?

The answers are respectively **yes** and **no** on every nontrivial two-dimensional grid.

## 2. P025-T225 — threshold/orbit extension diamond commutes

Start from any dyadic threshold staircase `S` and choose a new threshold `T` not already present.

There are two routes to the enlarged grid:

\[
\boxed{
S
\xrightarrow{+T}
S_T
\xrightarrow{+j}
S_{T,j}
}
\]

and

\[
\boxed{
S
\xrightarrow{+j}
S_j
\xrightarrow{+T}
S_{j,T}.
}
\]

Both final states are computed from the same old orbit plus one appended pressure value and the same old threshold set plus `T`.

Therefore every final cell is the same Boolean statement

\[
\rho_j\ge T_k.
\]

Hence

\[
\boxed{S_{T,j}=S_{j,T}.}
\]

The equality holds simultaneously for:

- activation matrices;
- crossing-depth vectors;
- node-rank vectors;
- Ferrers boundary words.

Thus the biaxial extension square is flat.

## 3. P025-T226 — boundary path sees `VH` versus `HV`

By Stage 94:

- a threshold extension inserts one `V`;
- an orbit extension inserts one `H`.

So the two routes around the extension diamond have edge labels

\[
\boxed{(V,H)}
\]

and

\[
\boxed{(H,V)}.
\]

The intermediate boundary words generally differ, but the final boundary word is identical.

This is the boundary-coordinate expression of the commuting semantic diamond.

## 4. P025-D40 — unweighted representation cost vector

To compare the three exact representations without inventing arbitrary numerical weights, record only three integer coordinates:

\[
\boxed{
C=(\text{storage coordinates},
\text{threshold-extension worst-case writes},
\text{orbit-extension worst-case writes}).
}
\]

This is not a runtime model. It is a structural envelope in unit coordinate writes.

For `s` thresholds and `h+1` orbit nodes:

### Crossing coordinates

Storage uses `s` depths.

A threshold insertion writes one crossing coordinate, while one new orbit node may resolve every previously infinite threshold, so the worst case is `s` crossing rewrites.

Thus

\[
\boxed{C_{\rm cross}=(s,1,s).}
\]

### Rank coordinates

Storage uses `h+1` ranks.

An orbit extension appends one rank, while a very low new threshold can increment every existing rank.

Thus

\[
\boxed{C_{\rm rank}=(h+1,h+1,1).}
\]

### Boundary word

Storage uses one symbol for every threshold and every orbit node:

\[
s+h+1.
\]

Both axis extensions are one-symbol insertions. Hence

\[
\boxed{C_{\rm path}=(s+h+1,1,1).}
\]

## 5. P025-T227 — full Pareto frontier on nontrivial grids

Assume

\[
\boxed{s\ge2,
\qquad h+1\ge2.}
\]

Then:

- crossing beats rank on threshold-update locality, while rank beats crossing on orbit-update locality;
- path beats crossing on orbit-update locality but uses more storage;
- path beats rank on threshold-update locality but uses more storage.

Therefore none of the three cost vectors dominates another in all coordinates.

Hence

\[
\boxed{
\{\text{crossing},\text{rank},\text{path}\}
}
\]

is exactly the nondominated representation family under this declared structural cost envelope.

The first full Pareto grid is already

\[
s=2,
\qquad h+1=2.
\]

## 6. P025-C33 — one-threshold degeneracy collapses the frontier

If

\[
s=1,
\]

then

\[
C_{\rm cross}=(1,1,1).
\]

For any horizon with more than one node, this dominates both alternatives:

- rank uses more storage and may rewrite more than one coordinate under threshold extension;
- path uses more storage with no update advantage.

Thus a one-threshold future has no reason, under this cost envelope, to leave the crossing scalar representation.

## 7. P025-C34 — one-node degeneracy is the dual boundary

If

\[
h=0,
\]

there is only one orbit node and

\[
C_{\rm rank}=(1,1,1).
\]

For more than one threshold this dominates both alternatives.

So the threshold and orbit degeneracies are exact duals.

## 8. Exact working Pareto calibration

For the `4 x 4` Stage-93 grid,

\[
s=4,
\qquad h+1=4.
\]

The cost vectors are

\[
\boxed{
C_{\rm cross}=(4,1,4),
}
\]

\[
\boxed{
C_{\rm rank}=(4,4,1),
}
\]

and

\[
\boxed{
C_{\rm path}=(8,1,1).
}
\]

The path doubles the coordinate count relative to either one-axis chart, but it is the only representation local in both extension directions.

No scalar ranking can be extracted from these data without adding an external workload/cost preference.

## 9. P025-T228 — representation choice is only partially ordered

Semantic equivalence gives a bijection among the three representations, but operational cost gives only a Pareto partial order.

Therefore the statement

> representation A is more precise / better than representation B

is underspecified unless the future operation language or cost criterion is declared.

The correct object is

\[
\boxed{
\text{semantic quotient}
+
\text{coordinate chart}
+
\text{future operation profile}.
}
\]

This strengthens Stage 94's axis-relative coordinate policy.

## 10. Relation to the Stage-85 Hasse diamond

Stage 85 found flat diamonds in exponent-transport space: multiplying an exponent by two distinct cover primes in either order gives the same long-range pressure multiplier.

Stage 95 finds a different flat diamond in precision-state space: adding threshold precision and orbit depth in either order gives the same final Ferrers state.

The common structural theme is not that the operations are identical, but that local generators commute on the declared semantic quotient.

This is a useful cross-route pattern but is not yet promoted to a common theorem.

## 11. Architectural meaning

Two lessons now coexist:

1. **state choice is future-relative** — Stage 90;
2. **coordinate choice inside one state is operation-relative** — Stages 94–95.

A precision architecture that stores one canonical representation for all workloads may therefore be overcommitting.

The weaker, safer principle is to keep a semantic state with interchangeable charts and choose a chart according to the next expected operation family.

## 12. Prior-art / novelty discipline

Commuting squares, Pareto dominance, sparse coordinate updates and chart selection are broad prior mathematical/computational concepts.

P025 claims none of them in isolation.

The project-side result is the exact arithmetic/Ferrers instantiation and the proved cost vectors induced by its two future extension axes. Historical novelty remains `NOVELTY_UNVERIFIED`.

## 13. Executable assets

Added:

- `src/enterprise_math/abc_dyadic_extension_diamond.py`;
- `tests/test_abc_dyadic_extension_diamond.py`.

The executable layer verifies both routes of the biaxial extension diamond, final crossing/rank/path equality, exact cost vectors, the nontrivial Pareto frontier, and the one-threshold/one-node degeneracy boundaries.

## 14. Next frontier

No hard block exists. Continue with:

1. define the Ferrers activation area as a scalar potential for biaxial extensions;
2. compute its threshold-axis and orbit-axis finite differences;
3. test whether the mixed second difference is exactly the new corner activation bit;
4. compare this discrete potential law with existing P024 action-language / P023 composition structures;
5. only after that, decide whether Stage91–95 should produce a new Foundation Feedback Packet or merely extend the Stage90 packet.
