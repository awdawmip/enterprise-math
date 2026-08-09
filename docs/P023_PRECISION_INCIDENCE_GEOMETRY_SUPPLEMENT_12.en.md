# P023 — Precision Incidence Geometry, Supplement 12

Status: `PROVED RESEARCH NOTE`  
Owner: A2 / P023, with a bridge to P012 intrinsic discrete geometry  
Depends on: P023-S9/S10/S11, P012 metric discipline  
Discipline: bipartite block-incidence graphs, set partitions, directed/quasi-metric ideas, and integer coding depths are established mathematical ingredients. This supplement records their exact finite-precision synthesis; no historical-priority claim is made for the general structures.

## 1. Two precision states define a bipartite graph

Let `E,F` be two equivalence relations on the same finite nonempty state set `X`.

Construct the **precision incidence graph** with:

- left vertices `X/E`;
- right vertices `X/F`;
- an edge between blocks `B in X/E` and `C in X/F` exactly when
  \[
  B\cap C\ne\varnothing.
  \]

Write the edge set as

\[
\boxed{
\Gamma(E,F)
=
\{(B,C):B\cap C\ne\varnothing\}.
}
\]

This graph is invariant under renaming block labels. It depends only on the two precision relations.

## 2. P023-S12-T01 — Realized product classes are graph edges

Status: `PROVED`.

The common refinement `E cap F` has one block for each nonempty block intersection. Hence

\[
\boxed{
|X/(E\cap F)|
=|\Gamma(E,F)|.
}
\]

The formal Cartesian candidate count is

\[
|X/E|\,|X/F|,
\]

so the exact number of unrealized product-class tuples is

\[
\boxed{
U(E,F)
=|X/E|\,|X/F|-|\Gamma(E,F)|.
}
\]

Thus P023-S9's "realized tuples, not formal products" rule is exactly the sparse-versus-complete bipartite graph distinction.

## 3. P023-S12-T02 — Directed repair factor is maximum incidence degree

Status: `PROVED`.

Suppose precision `E` is already known and task `F` is added. The target precision is the common refinement `E cap F`.

For one `E` block `B`, the number of target blocks inside `B` is exactly the number of `F` blocks meeting it, namely its incidence degree

\[
\deg_F(B).
\]

Therefore the exact minimum repair alphabet is

\[
\boxed{
\rho(E,F)
=
R(E\to E\cap F)
=
\max_{B\in X/E}\deg_F(B).
}
\]

This quantity is generally asymmetric:

\[
\rho(E,F)\ne\rho(F,E).
\]

That asymmetry is meaningful: adding task `F` when `E` is already known need not cost the same as adding `E` when `F` is already known.

## 4. P023-S12-T03 — Directed repair spectrum is the degree spectrum

Status: `PROVED`.

The full relative repair spectrum for adding `F` to `E` is

\[
\boxed{
\mathcal R_k(E\leftarrow E\cap F)
=
\sum_{B\in X/E}
\binom{\deg_F(B)}k.
}
\]

So the S11 quotient-projection spectrum is the binomial degree spectrum on one side of the incidence graph.

The reverse task uses the opposite side degrees:

\[
\mathcal R_k(F\leftarrow E\cap F)
=
\sum_{C\in X/F}
\binom{\deg_E(C)}k.
\]

The two directions share the same edges but can have very different local repair profiles.

## 5. Extremes

### Already sufficient precision

\[
\boxed{
\rho(E,F)=1
\iff
E\subseteq F.
}
\]

Indeed every `E` block meets exactly one `F` block exactly when every `E` block lies inside an `F` block.

Thus directed repair factor one means: the currently retained precision `E` already determines task `F`.

### Complete incidence

If every `E` block meets every `F` block, then the incidence graph is complete bipartite and

\[
\boxed{
\rho(E,F)=|X/F|,
\qquad
\rho(F,E)=|X/E|.
}
\]

This is the maximal formal product case. It should not be called probabilistic independence without extra structure; it is only complete combinatorial incidence.

## 6. P023-S12-T04 — Multiplicative triangle inequality

Status: `PROVED`.

For any three finite precision relations `E,F,G`,

\[
\boxed{
\rho(E,G)
\le
\rho(E,F)\rho(F,G).
}
\]

### Proof

Fix an `E` block `B`. Every `G` block `D` meeting `B` contains some state `x in B cap D`. That state belongs to an `F` block `C` that meets both `B` and `D`.

The block `B` meets at most `rho(E,F)` distinct `F` blocks. Each such `F` block meets at most `rho(F,G)` distinct `G` blocks. Therefore `B` can meet at most their product many `G` blocks.

Taking the maximum over `E` blocks gives the inequality. ∎

Thus `rho` is a multiplicative directed distance-like quantity on finite precision states.

## 7. Integer symbol-depth

Fix an integer alphabet base

\[
B\ge2.
\]

Define the integer symbol depth

\[
L_B(n)
=
\min\{\ell\in\mathbb N_0:n\le B^\ell\}.
\]

This is already a natural integer information-level construction in the project and requires no logarithm.

Define the directed precision depth

\[
\boxed{
d_B(E,F)=L_B(\rho(E,F)).
}
\]

It is the minimum number of base-`B` repair symbols/digits sufficient in the worst local `E` fiber to add task `F`.

## 8. P023-S12-T05 — Directed integer triangle inequality

Status: `PROVED`.

For any `E,F,G`,

\[
\boxed{
d_B(E,G)
\le
d_B(E,F)+d_B(F,G).}
\]

### Proof

Let

\[
a=d_B(E,F),
\qquad
b=d_B(F,G).
\]

Then

\[
\rho(E,F)\le B^a,
\qquad
\rho(F,G)\le B^b.
\]

T04 gives

\[
\rho(E,G)
\le B^{a+b},
\]

so by minimality of `L_B`,

\[
d_B(E,G)\le a+b.
\]

∎

Moreover,

\[
\boxed{
d_B(E,F)=0\iff E\subseteq F.}
\]

Thus zero directed distance means "no extra precision is needed to answer `F` from `E`", not necessarily equality of the two precision states.

This is the expected preorder behavior of a directed task-upgrade cost.

## 9. P023-S12-T06 — Symmetric integer metric on precision relations

Status: `PROVED`.

Define

\[
\boxed{
D_B(E,F)
=
d_B(E,F)+d_B(F,E).
}
\]

Then `D_B` is a metric on finite equivalence relations on the fixed state set `X`:

1. `D_B(E,F)>=0`;
2. `D_B(E,F)=D_B(F,E)`;
3. `D_B(E,F)=0` iff `E=F` as equivalence relations;
4. triangle inequality:
   \[
   \boxed{
   D_B(E,G)
   \le
   D_B(E,F)+D_B(F,G).
   }
   \]

### Proof

Only definiteness and triangle need comment.

If `D_B(E,F)=0`, both directed depths vanish, so `E subseteq F` and `F subseteq E`; hence `E=F`.

For triangle, apply T05 to `E -> F -> G` and independently to `G -> F -> E`, then add the two inequalities. ∎

So finite precision states acquire an intrinsic, integer-valued geometry derived from exact repair requirements rather than an externally imposed Euclidean coordinate.

## 10. Relation to P012

P012 requires geometry to come from explicitly declared discrete structure rather than hidden rounded Euclidean distance.

S12 supplies a new derived geometry whose primitive data are:

- one finite underlying state set;
- two precision equivalence relations;
- nonempty block intersection;
- exact minimum repair multiplicity.

The result should therefore be read as a **precision-state geometry**, not as physical-space geometry.

It may nevertheless serve as a reusable P012-style graph metric on proof/observation state spaces.

## 11. Relation to P023-S8/S9/S10/S11

The incidence graph compresses four earlier views:

- S8 label recovery: maximum relevant degree equals one;
- S9 minimum task repair: maximum block degree;
- S10 admissible-relation ambiguity: observation-side degree;
- S11 higher repair spectrum: binomial degree spectrum.

So "image separation", "minimal repair", "incidence repair", and "relative repair spectrum" are not separate mechanisms; they are increasingly rich observables of the same finite incidence structure.

## 12. Research-tool meaning

For two candidate precision descriptions, a standard preflight can now be:

1. construct their block-incidence graph;
2. count realized edges rather than formal Cartesian tuples;
3. inspect side degrees to obtain exact directed repair factors;
4. use the degree binomial spectrum when worst-case repair alone is insufficient;
5. use `d_B` or `D_B` when a compact integer transition/geometry cost is needed.

This gives a common finite language for task addition, state compression, and precision comparison.

## 13. Executable specification

- `src/enterprise_math/precision_incidence_geometry.py`
- `tests/test_precision_incidence_geometry.py`

Regression enumerates all 15 partitions of a four-state set and checks all `15^3=3375` triples for the multiplicative repair triangle, directed integer triangle, and symmetric metric triangle. It also cross-checks the incidence degree spectrum against the S11 quotient-projection repair spectrum.

## 14. Foundation boundary

`D_B` is a metric on mathematical precision relations, not automatically a physical spatial distance or an ontological information metric. Its meaning is operational and exact: discrete repair capacity needed to translate between declared finite observation/task states.
