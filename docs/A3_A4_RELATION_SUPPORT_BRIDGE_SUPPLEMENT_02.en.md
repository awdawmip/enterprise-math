# A3 ↔ A4 Relation-Support Bridge — Supplement 02

Status: `ACTIVE RESEARCH NOTE`  
Scope: integer metric induced by A3-generated support and an exact geodesic criterion for A4 split-completeness

## 1. Setup

Work on the zero-relation quotient `X0=X/~0` from Stage 01. For quotient classes define

\[
[i]R_r[j]
\iff
|Z_{ij}|\le r m_i m_j,
\qquad r\in\mathbb N.
\]

Stage 01 proves that `(R_r)` is identity at radius zero, monotone, symmetric, and subadditive under relation composition.

The support family therefore has a canonical minimum integer radius between any two quotient states.

## 2. B07 — canonical integer relation metric

Define

\[
\boxed{
\rho([i],[j])
=
\min\{r\in\mathbb N:[i]R_r[j]\}.
}
\]

Equivalently, using only integer arithmetic,

\[
\boxed{
\rho([i],[j])
=
\left\lceil\frac{|Z_{ij}|}{m_i m_j}\right\rceil
=
\frac{|Z_{ij}|+m_im_j-1}{m_im_j}
\text{ under floor division.}
}
\]

No rational-valued state needs to be stored: the last expression is exact integer ceiling division.

### B07a — metric axioms

`rho` is an integer metric on `X0`.

1. `rho>=0` by definition.
2. `rho([i],[j])=0` iff `Z_ij=0` iff `[i]=[j]` on the zero quotient.
3. Symmetry follows from `Z_ij=-Z_ji`.
4. Triangle inequality follows from Stage-01 support subadditivity. If
   `rho(i,j)=a` and `rho(j,k)=b`, then `(i,j) in R_a` and `(j,k) in R_b`, hence `(i,k) in R_(a+b)`, so
   \[
   \rho(i,k)\le a+b.
   \]

Therefore

\[
\boxed{R_r=\{(x,y):\rho(x,y)\le r\}.}
\]

A3-generated A4 support is exactly the radius filtration of this integer metric.

## 3. Unit-support graph

Let `G1` be the undirected graph on `X0` with an edge between distinct states `x,y` iff

\[
\rho(x,y)=1.
\]

Let `d_G1(x,y)` be the usual shortest-path distance in this graph, with `infinity` when no unit-edge path exists.

Every unit-edge path of length `L` satisfies

\[
\rho(x,y)\le L
\]

by the metric triangle inequality. Hence whenever `d_G1` is finite,

\[
\boxed{\rho(x,y)\le d_{G1}(x,y).}
\]

The gap is not a numerical rounding error. It measures whether the represented state set contains enough intermediate states to realize the direct integer relation distance by unit stages.

## 4. B08 — exact global split-completeness/geodesic equivalence

The following are equivalent.

### (A) A4 split-completeness for every integer budget split

For all `r,s>=0`,

\[
\boxed{R_r;R_s=R_{r+s}.}
\]

### (B) Unit-geodesic realization

For every pair `x,y in X0`,

\[
\boxed{d_{G1}(x,y)=\rho(x,y).}
\]

Equivalently, every pair at integer relation distance `n` admits a chain

\[
x=x_0,x_1,\ldots,x_n=y
\]

such that

\[
\rho(x_{t-1},x_t)=1
\]

for every step.

### Proof: (A) implies (B)

Take `x,y` with `rho(x,y)=n`.

- `n=0` is trivial.
- `n=1` is a unit edge.
- for `n>=2`, split completeness with budgets `1` and `n-1` gives a state `z` with
  \[
  \rho(x,z)\le1,
  \qquad
  \rho(z,y)\le n-1.
  \]
  `z` cannot equal `x`, because then the second inequality would contradict `rho(x,y)=n`. Thus `rho(x,z)=1`. The triangle inequality forces `rho(z,y)=n-1`; otherwise `rho(x,y)<n`. Repeat inductively.

This constructs a unit path of length exactly `n`, so `d_G1<=n=rho`. The opposite inequality was proved above.

### Proof: (B) implies (A)

Take `(x,y) in R_(r+s)`, so `n=rho(x,y)<=r+s`. Choose a unit geodesic of length `n`. There exists an integer

\[
k\in[\max(0,n-s),\min(r,n)]
\]

because `n<=r+s`. Let `z` be the `k`-th vertex on the geodesic. Then

\[
\rho(x,z)\le k\le r,
\qquad
\rho(z,y)\le n-k\le s.
\]

Hence `(x,y) in R_r;R_s`. Stage 01 already gives the reverse inclusion.

Therefore global A4 split-completeness in the A3-generated subclass is **exactly** the statement that the integer relation metric is the intrinsic shortest-path metric of its radius-one support graph.

## 5. B09 — geodesic defect

Define the pairwise geodesic defect

\[
\Gamma(x,y)=
\begin{cases}
 d_{G1}(x,y)-\rho(x,y),&d_{G1}(x,y)<\infty,\\
 \infty,&\text{otherwise.}
\end{cases}
\]

Then `Gamma>=0`, and

\[
\boxed{
\Gamma\equiv0
\iff
R_r;R_s=R_{r+s}
\text{ for all }r,s\in\mathbb N.
}
\]

Thus `Gamma` compresses the infinitely many budget-split equalities into one finite metric audit on the finite quotient state set.

This is stronger than counting `missing_interpolations` at one selected pair `(r,s)`: it identifies exactly how much extra unit-path length, or complete disconnection, is caused by missing represented states.

## 6. Examples

### Consecutive unit states

For values `{0,1,2}`, `rho(0,2)=2`, while `0-1-2` is a unit path of length two. `Gamma=0` for every pair, recovering B05.

### Missing midpoint

For values `{0,2}`, `rho(0,2)=2` but the unit graph has no edge and no path. Thus

\[
\Gamma(0,2)=\infty,
\]

recovering B06 and explaining the `1+1` failure as a graph-geodesic hole.

### Weighted/non-unit states

The theorem does not require unit capacities or integer-valued normalized states. Capacities enter only through the exact cross-multiplied integer radius `rho`; after the zero quotient, the geodesic test is purely finite and combinatorial.

## 7. Cross-route consequences

### A4

`split-complete` can now be audited without checking every `(r,s)` composition separately: generate `G1` and compare its shortest-path metric with `rho`.

### A5 / P012 / P022

The bridge lands directly on intrinsic discrete geometry. The radius-one A4 support graph becomes a candidate primitive adjacency, and B08 asks whether its intrinsic graph metric reproduces the A3 direct integer relation metric. Geometry-specific research can study when lattice/root-lattice states have `Gamma=0`, bounded `Gamma`, or disconnected interpolation sectors.

### A2 / P023

A quotient that preserves endpoint `rho` but changes `Gamma` is not future-safe for an operation language that contains staged support composition. Future compatibility must therefore declare whether it needs only endpoint support or also geodesic/intermediate-witness structure.

### A3

`rho` and `Gamma` separate two state properties:

- direct coarse relational separation;
- realizability of that separation by represented intermediate states.

This provides a finite integer interface between relation-state precision and support-composition precision.

## 8. Prior-art discipline

Integer metrics, graph shortest-path metrics, geodesic metric spaces, and relation powers are established mathematics. No novelty claim is made for those general notions.

The project-specific contribution under test is the exact derivation of this metric/geodesic interface from the A3 weighted relation field and its use to connect A4 split-completeness, A5 intrinsic geometry, and A2 future-compatible precision.

## 9. Executable reference

`src/enterprise_math/relation_support_bridge.py` adds:

- integer relation-distance matrix by ceiling division;
- radius-one graph shortest paths;
- geodesic-defect audit;
- global split-completeness criterion via metric equality.

The tests include unit and weighted examples plus the disconnected `{0,2}` defect case.
