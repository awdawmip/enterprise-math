# P019 Supplement 19 — Matrix Quotients of Weighted Relations and the Refinement Forest

Status: `RESEARCH WIP / EXACT INTEGER RECONSTRUCTION PROVED`

## 1. Goal

Supplements 15–18 established that the weighted relation field is a tree-independent current relation object, partition coarsening composes exactly, each binary merge deletes one internal relation, coarsening-only quotients may erase those relations permanently, and exact refinement requires sufficient relation memory.

This supplement answers two structural questions:

1. Is there a compact matrix form for arbitrary partition quotients?
2. How many internal relations are sufficient for exact present-state refinement?

## 2. P019-X61 — Weighted relation matrix as an integer wedge form

Write current block totals and capacities as column vectors

\[
c=(c_1,\ldots,c_k)^T,
\qquad
m=(m_1,\ldots,m_k)^T.
\]

The weighted relation matrix is

\[
Z_{ij}=m_jc_i-m_ic_j,
\]

or

\[
\boxed{Z=cm^T-mc^T.}
\]

Skew symmetry is automatic. General exterior/wedge algebra is established linear algebra; P019 only uses this integer representation.

Ordinary matrix rank must not be confused with P019 relation dimension. The decomposable skew matrix has low linear-algebra rank, while the fixed-total integer state generating it still has `k-1` independent degrees.

## 3. P019-X62 — Arbitrary partition quotient is `AZA^T`

Let the current state have `k` blocks and a coarse partition have `ell` blocks. Let

\[
A\in\{0,1\}^{\ell\times k}
\]

be the partition incidence matrix, with each fine-block column containing exactly one `1` in its coarse group.

Then

\[
\boxed{c'=Ac,}
\qquad
\boxed{m'=Am.}
\]

Hence

\[
Z'=c'{m'}^T-m'{c'}^T
\]

becomes

\[
\boxed{Z'=AZA^T.}
\]

This is the matrix version of the double cut-sum rule from Supplement 16.

## 4. Partition composition in one line

If

\[
A_1:k\to\ell,
\qquad
A_2:\ell\to r,
\]

then the total coarsening matrix is `A=A_2A_1`, and

\[
A_2(A_1ZA_1^T)A_2^T
=(A_2A_1)Z(A_2A_1)^T.
\]

Therefore

\[
\boxed{Q_{A_2}\circ Q_{A_1}=Q_{A_2A_1}.}
\]

Again, a binary tree is not needed to define the present coarse state.

## 5. P019-X63 — Relation-dimension loss is `k-ell`

Fine totals with fixed grand total have `k-1` free integer degrees. A coarse partition with `ell` totals and the same fixed grand total has `ell-1`. Thus quotient-fiber rank is

\[
\boxed{(k-1)-(\ell-1)=k-\ell.}
\]

Equivalently, a coarse group containing `r_alpha` fine blocks has internal redistribution rank `r_alpha-1`, and

\[
\sum_\alpha(r_\alpha-1)=k-\ell.
\]

## 6. P019-X64 — A spanning tree of internal relations is sufficient inside one coarse block

Consider one coarse block containing `r` fine child blocks with capacities `m_i`, unknown totals `c_i`, and known coarse total

\[
C=\sum_i c_i.
\]

Choose any spanning tree on the `r` children. Store on every tree edge `(i,j)` the weighted relation

\[
\boxed{Z_{ij}=m_jc_i-m_ic_j.}
\]

There are exactly `r-1` such relation coordinates.

They, together with `C` and the capacities, uniquely recover every child total.

### Uniqueness proof

Suppose `c_i` and `c'_i` give the same tree-edge relations and the same total. Let

\[
\delta_i=c_i-c'_i.
\]

Every tree edge gives

\[
m_j\delta_i-m_i\delta_j=0.
\]

Connectivity forces all `delta_i/m_i` to be equal, expressible entirely by cross multiplication. Hence `delta_i=lambda m_i` for one common proportional factor. But `sum delta_i=0` and all capacities are positive, so `lambda=0`. Therefore every `delta_i=0`. ∎

Existence/integer legality is guaranteed when the relation data came from an actual fine state; arbitrary external tags must still pass exact divisibility checks.

## 7. P019-X65 — Refinement Forest relation count exactly matches lost dimension

Choose one internal spanning tree inside every coarse partition block. Together these trees form a forest.

The number of stored internal relations is

\[
\sum_\alpha(|A_\alpha|-1).
\]

Since the fine partition has `k` blocks and the coarse partition has `ell`, this equals

\[
\boxed{|E_{forest}|=k-\ell.}
\]

X63 gives exactly the same relation-rank loss

\[
\boxed{k-\ell.}
\]

Thus the Refinement Forest restores precisely the missing number of independent relation coordinates in the natural rank sense.

This is not a claim about arbitrary information-theoretic integer encodings; the minimality is in independent linear/relation degrees.

## 8. Binary merge is the smallest special case

If a coarse block merges exactly two children, `r=2`, the internal spanning tree has one edge and the Refinement Forest stores only

\[
\boxed{Z_{12}=z,}
\]

recovering Supplement 15 X47.

## 9. P019-X66 — Full process history is not required for exact present-state refinement

If the goal is only to recover the present totals of a known fine partition, then

\[
\boxed{
\text{coarse weighted quotient}
+
\text{Refinement Forest}
}
\]

is sufficient.

It need not retain which blocks merged first, the chronological order of independent merges, the binary contraction tree, or the actual selected-boundary process path. Those are process-provenance data and are needed only when the future language asks for them.

## 10. Integer relation-tree recovery algorithm

Use a rooted internal relation tree and store edge values

\[
Z_{parent,child}.
\]

First propagate weighted relations to a chosen root. If `Z_{u,r}` is known and edge `Z_{u,v}` is stored, weighted closure gives

\[
\boxed{
m_u Z_{v,r}
=-m_r Z_{u,v}+m_v Z_{u,r}.}
\]

A legal fine state guarantees exact divisibility by `m_u`.

Once all `Z_{v,r}` are known, recover the root total from

\[
M c_r
=m_r C-\sum_{v\ne r}Z_{v,r},
\]

then recover all remaining child totals. Every division is exact integer division.

## 11. Three levels of relation memory

### 0. Pure coarsening state

Retain only the coarse quotient. This is sufficient for a quotient-closed future language.

### 1. Exact current refinement state

Retain coarse quotient plus a Refinement Forest. This recovers a specified fine partition's present totals without merge chronology.

### 2. Process provenance state

Additionally retain actual historical witnesses, contraction order, and boundary selections for history-sensitive future languages.

These levels should not be conflated.

## 12. Implementation and validation

`src/enterprise_math/weighted_relation_field.py` adds `tree_internal_relations` and `recover_totals_from_relation_tree`.

`tests/test_weighted_relation_field.py` checks exact round-trip recovery from `k-1` spanning-tree weighted relations plus grand total under multiple capacities/totals and verifies that different relation-tree choices recover the same present state.

## 13. Prior-art boundary

Spanning-tree bases, incidence matrices, cut/flow coordinates, and exterior products are established graph-theoretic/linear-algebraic tools. P019 makes no originality claim for those general constructions.

The current research interface is their combination with finite-precision dimensional contraction to obtain a weighted relation quotient, a deleted-relation rank, an exact Refinement Forest, and a future-safe erasure hierarchy.

## 14. Next steps

1. build local basis changes between different Refinement Forests, analogous to Contraction Atlas rotations;
2. determine which forest subsets suffice for partial/demand-driven refinements;
3. connect the `k-ell` relation-memory count to P018 precision-refinement cost;
4. use P021 witness joins to test whether present-state forests suffice for future causal composition or additional provenance is required;
5. study Smith normal form / integer-lattice invariants of weighted relation quotients to obtain canonical legal-coordinate forms.
