# P019 Supplement 14 — Tree-Independent Relation Field and Tight Integer Flow Charts

Status: `RESEARCH WIP / EXACT INTEGER IDENTITIES PROVED`

## 1. Problem

Contraction Atlas shows that different binary trees can serve as different `z` coordinate charts for the same present fine state.

A deeper question remains:

> Is there a completely tree-independent relation object underneath all of those charts?

Yes. The most direct object is the integer difference relation among every pair of unit slots.

## 2. Complete pair relation field

For integer slots

\[
x=(x_1,\ldots,x_N),
\]

define

\[
\boxed{d_{ij}=x_i-x_j.}
\]

Write the full field as

\[
D(x)=(d_{ij})_{1\le i,j\le N}.
\]

It satisfies

\[
\boxed{d_{ii}=0,}
\qquad
\boxed{d_{ij}=-d_{ji},}
\]

and the three-point closure law

\[
\boxed{d_{ij}+d_{jk}=d_{ik}.}
\]

All of these are integer relations.

## 3. P019-X37 — A closed pair field plus the total uniquely recovers the fine state

Let an integer matrix `D=(d_ij)` satisfy the diagonal, antisymmetry, and three-cycle closure laws.

For every `i`,

\[
\sum_j d_{ij}
=Nx_i-\sum_jx_j.
\]

If the root total is

\[
c=\sum_jx_j,
\]

then

\[
\boxed{x_i=(c+\sum_jd_{ij})//N.}
\]

Thus whenever all numerators are exactly divisible by `N`, `D+c` uniquely reconstructs an integer fine state.

For a zero-sum `A_{N-1}` state, `c=0`, so a legal closed field by itself determines the state.

## 4. P019-X38 — Every contraction imbalance is a relation-field cut sum

Take disjoint slot sets `A,B`. The contraction imbalance is

\[
z(A,B)
=
|B|\sum_{i\in A}x_i
-|A|\sum_{j\in B}x_j.
\]

Then

\[
\boxed{
z(A,B)
=
\sum_{i\in A}\sum_{j\in B}d_{ij}.}
\]

The proof is immediate by expanding the right-hand side.

Therefore every internal `z` coordinate in Contraction Atlas is a directed cut aggregation of one tree-independent relation field. This explains why tree changes are changes of cut basis, why local reassociation transports only `z`, why pentagon coherence holds on legal states, and why `z^2` enters the pair-dispersion merge law.

## 5. P019-X39 — Pair dispersion is the squared relation-field sum

Supplement 11 defined

\[
P(x)=\sum_{i<j}(x_i-x_j)^2.
\]

Hence

\[
\boxed{P(x)=\sum_{i<j}d_{ij}^2.}
\]

For zero-sum `A_{N-1}` states,

\[
\boxed{P=2Nq.}
\]

Thus the square-radial observation can be reconstructed entirely from the tree-independent pair relation field.

## 6. Dimension-invariant primitive unit inside the relation field

For a primitive root state

\[
x=e_i-e_j,
\]

we have

\[
\sum_kx_k^2=2,
\qquad
q=1.
\]

By X39,

\[
\boxed{P=2N.}
\]

As the number of slots/dimension increases, the raw number of pair relations attached to this unit increases, but the exact scale projection remains

\[
\boxed{q=P//(2N)=1.}
\]

This gives another relation-level expression of the principle that `1` remains `1` in every finite dimension: higher dimension adds relations to more slots; it does not enlarge the unit value itself.

## 7. P019-X40 — Relation dimension is `N-1`

The full field contains `N(N-1)/2` undirected pair differences, but the three-cycle closure laws make them highly dependent.

Fix a reference slot `r` and retain only

\[
\delta_i=x_i-x_r,
\qquad i\ne r.
\]

Then

\[
\boxed{d_{ij}=\delta_i-\delta_j}
\]

with `delta_r=0`. The entire closed relation field therefore has only `N-1` free integer relation degrees.

For `A_p`, `N=p+1`, so

\[
\boxed{
dim_{relation}=N-1=p.
}
\]

Together with previous results,

\[
\boxed{
dim_{growth}=dim_{contract}=dim_{relation}=p.
}
\]

Three different discrete procedures now recover the same dimension.

## 8. Anchor-difference chart: `N-1` values with one modulo-`N` legality condition

Given

\[
\delta_i=x_i-x_r
\]

and total `c`,

\[
c=Nx_r+\sum_{i\ne r}\delta_i,
\]

so

\[
\boxed{x_r=(c-\sum\delta_i)//N.}
\]

Legality is the single congruence

\[
\boxed{\sum\delta_i\equiv c\pmod N.}
\]

Thus fixed-total anchor-difference coordinates form an affine sublattice of index `N` in ambient `Z^(N-1)`.

This is denser than a binary contraction `z` chart with

\[
I(T)=\prod_v|v|,
\]

but it still chooses an anchor, and pair differences themselves are not a unimodular fixed-total lattice chart.

## 9. P019-X41 — A spanning-tree subtree-flow chart has index one

Choose any rooted spanning tree `S` connecting all slots. For each non-root vertex `v`, let `Sub(v)` be the rooted subtree below `v` after removing its parent edge. Define

\[
\boxed{f_v=\sum_{i\in Sub(v)}x_i.}
\]

There are `N-1` such integers.

For a non-root vertex,

\[
\boxed{x_v=f_v-\sum_{w\in children(v)}f_w,}
\]

and at the root,

\[
\boxed{x_r=c-\sum_{w\in children(r)}f_w.}
\]

Therefore every arbitrary integer tuple

\[
(f_v)\in\mathbb Z^{N-1}
\]

produces exactly one integer state of total `c`.

Hence

\[
\boxed{
\{x\in\mathbb Z^N:\sum x_i=c\}
\cong
\mathbb Z^{N-1}
}
\]

through a purely integer tree-flow chart, with chart index

\[
\boxed{1.}
\]

For zero-sum `A_{N-1}`, this is a unimodular integer chart.

## 10. Path chart and the standard `A`-type integer basis

If the spanning tree is a path, the flows become successive subtree/prefix sums. With a suitable orientation,

\[
f_1=x_1,
\qquad
f_2=x_1+x_2,
\quad\ldots\quad,
 f_{N-1}=x_1+\cdots+x_{N-1}.
\]

The inverse is

\[
x_1=f_1,
\qquad
x_i=f_i-f_{i-1},
\qquad
x_N=c-f_{N-1}.
\]

At `c=0` this is the standard rank-`N-1` integer-coordinate neighborhood of the `A_{N-1}` zero-sum lattice. `A_n` root lattices and simple-root bases are established mathematics; no originality claim is made here.

## 11. Four present-state representations

At least four equivalent representations now have distinct roles.

### A. Slot values

`x_1,...,x_N` with a fixed-total constraint.

### B. Complete pair relation field

`d_ij`.

Tree-independent and relation-symmetric, but `O(N^2)` redundant.

### C. Spanning-tree flow chart

`N-1` flow integers.

Index one and arithmetically tight, but chooses a spanning-tree chart.

### D. Contraction imbalance chart

`N-1` imbalance integers `z_v`.

Highly local for block merge, fiber minima, pair dispersion, and boundary witnesses, but its legal chart lattice has index

\[
\prod_v|v|.
\]

Thus the purpose of the contraction tree is no longer minimum coordinate count. Rather,

\[
\boxed{
\text{it trades coordinate-lattice density for hierarchical and dimensional-contraction locality.}
}
\]

## 12. P019-X42 — Binary split-flow chart to imbalance chart is triangular scaling

At each internal node `v` of a binary contraction tree, let parent total be `c_v`, left child size `m_v`, total node size `|v|`, and left child total

\[
f_v=a_v.
\]

Then

\[
\boxed{z_v=|v|f_v-m_vc_v.}
\]

Given the root total and all `f_v`, the entire leaf state is recursively recoverable, and every integer `f_v` tuple is legal.

Order internal nodes from root toward leaves. Then `c_v` depends only on the root total and ancestor split flows. Consequently the affine/linear transform from `f` to `z` is triangular with diagonal entries `|v|`.

Hence

\[
\boxed{
|\det(f\to z)|
=
\prod_v|v|
=I(T).
}
\]

This directly explains the chart-index theorem of Supplement 13: imbalance-chart sparsity is exactly the accumulated integer scaling created when a unimodular bulk split-flow chart is rewritten in proportional-deviation coordinates.

## 13. Prior-art boundary

This supplement touches several established tools:

- `A_n` root lattices and simple roots;
- graph incidence and spanning-tree integer coordinates;
- complete-graph Laplacian quadratic forms;
- cut/flow spaces.

These general theories are not Enterprise Math inventions.

The P019 research interface is the combination:

1. pair relation field with finite-precision `q` and unit invariance;
2. every contraction imbalance as a cut sum of one field;
3. index-one flow charts versus high-index imbalance charts as a locality tradeoff;
4. equality of growth, contraction, and relation dimensions.

Primary sources and lineage must be registered before promotion.

## 14. Implementation and validation

`src/enterprise_math/relation_field.py` now contains:

- complete pair field;
- closure checks;
- field+total recovery;
- anchor-difference coordinates and modulo-`N` legality;
- spanning-tree subtree-flow coordinates and exact recovery;
- block cut sums;
- pair dispersion from the field.

`tests/test_relation_field.py` checks:

- full-field closure and recovery;
- round-trip under every anchor;
- anchor-chart index `N`;
- index-one path/star/arbitrary rooted-tree flow round-trips;
- every block imbalance equals its relation-field cut sum;
- zero-sum pair dispersion / quadratic state.

## 15. Next steps

1. identify spanning-tree flow charts with contraction split-flow charts and implement chart routing;
2. optimize charts for a declared future operation family rather than statically minimizing index;
3. use Supplement 08 future-safe quotients to determine when complete fields, flow charts, and imbalance charts may safely replace one another;
4. lift intrinsic automorphism directions directly to the pair relation field instead of binding them to one contraction tree;
5. express spherical-excavation boundaries directly as relation-field cut conditions and further remove external geometric-coordinate interpretations.
