# P019 Supplement 20 — Legal-Lattice Index of the Refinement Forest and Adaptive Tree Choice

Status: `RESEARCH WIP / EXACT INTEGER DETERMINANT THEOREM PROVED`

## 1. Problem

Supplement 19 proved that when one coarse block contains `r` fine child blocks, any spanning tree of `r-1` weighted internal relations, together with the coarse total and capacities, recovers all child totals exactly.

Those `r-1` edge relations are not arbitrary points of ambient `Z^(r-1)`: capacities impose exact divisibility conditions. This supplement computes the legal-lattice index and optimizes it over tree choice.

## 2. Augmented relation-tree chart

Let child blocks be `(m_i,c_i)`, choose any oriented spanning tree `T`, and output the grand total

\[
C=\sum_i c_i
\]

plus one weighted relation

\[
Z_{uv}=m_vc_u-m_uc_v
\]

for every tree edge. This is an `r x r` integer linear map `A_T` from child totals to `(C, edge relations)`.

## 3. P019-X67 — Relation-tree chart determinant

Let

\[
M=\sum_i m_i
\]

and let `deg_T(i)` be the undirected tree degree of vertex `i`. For `r>=2`,

\[
\boxed{
|\det\mathcal A_T|
=
M\prod_{i=1}^r m_i^{\deg_T(i)-1}.
}
\]

For `r=1`, the determinant/index is one.

### Proof

Let `B_T` be any oriented tree-incidence matrix. Multiply column `i` of `A_T` by `m_i`. The first row becomes `m^T`, while edge `u->v` becomes

\[
m_um_v(e_u-e_v).
\]

Hence

\[
\det(A_T)\prod_i m_i
=
\left(\prod_{uv\in E(T)}m_um_v\right)
\det\begin{pmatrix}m^T\\B_T\end{pmatrix}.
\]

Every reduced tree-incidence matrix has determinant `±1`, so expansion along the first row gives

\[
\left|\det\begin{pmatrix}m^T\\B_T\end{pmatrix}\right|
=\sum_i m_i=M.
\]

Also

\[
\prod_{uv\in E(T)}m_um_v
=
\prod_i m_i^{\deg_T(i)}.
\]

Divide by `prod_i m_i`. ∎

## 4. P019-X68 — The fixed-total edge-relation chart has the same index

The grand-total map is surjective onto `Z`, so after fixing any total `C`, legal tree-edge relation tuples form an affine sublattice of ambient `Z^(r-1)` with index

\[
\boxed{
I_{rel}(T)
=M\prod_i m_i^{\deg_T(i)-1}.
}
\]

Thus the Refinement Forest is rank-tight and its exact divisibility density is known.

## 5. Unit capacities

If every child is a unit block, `m_i=1`, then for every tree shape

\[
\boxed{I_{rel}(T)=r.}
\]

Tree choice does not change relation-coordinate density at the unit-refinement layer. This differs sharply from the binary Contraction Atlas imbalance-chart index `prod_v |v|`, which depends strongly on hierarchical tree shape.

## 6. P019-X69 — Minimum index is a star centered at minimum capacity

For any tree,

\[
\deg_i\ge1,
\qquad
\sum_i(\deg_i-1)=r-2.
\]

Therefore minimizing

\[
M\prod_i m_i^{\deg_i-1}
\]

places all `r-2` excess degree on a minimum-capacity vertex. A star centered there realizes that degree sequence. Hence

\[
\boxed{I_{rel}^{min}=M m_{min}^{r-2}.}
\]

Similarly,

\[
\boxed{I_{rel}^{max}=M m_{max}^{r-2},}
\]

attained by a star centered at a maximum-capacity vertex. Existence of the relevant labeled tree degree sequences is standard Prüfer-sequence combinatorics.

## 7. Star optimality is objective-specific

`I_rel` measures legal-lattice density only. It does not directly measure future-operation locality, bit length, partial-refinement cost, direction-orbit locality, or historical interpretability. A star is optimal for this index objective, not automatically for every future language.

## 8. Contrast with the Contraction Atlas index

The binary contraction imbalance chart has

\[
I_{contraction}(T)=\prod_{v\in Internal(T)}|v|,
\]

adjacent to established tree-factorial/Q-shape statistics. Complete/greedy-from-bottom shapes minimize that product while caterpillar/chain shapes maximize it in the established tree-shape setting.

The Refinement Forest instead has

\[
I_{rel}(T)=M\prod_i m_i^{\deg_i-1}.
\]

For unit capacities it is shape-independent; for unequal capacities it allocates excess degree according to vertex capacity, with the minimum-capacity star minimizing the index.

The two charts optimize different coordinate systems and should not share one automatic tree heuristic.

## 9. P019-X70 — The relation-tree index depends only on the degree sequence

Tree topology enters X68 only through the labeled degree sequence. Thus two spanning trees with the same vertex degree sequence satisfy

\[
\boxed{I_{rel}(T_1)=I_{rel}(T_2).}
\]

This is coarser than the Contraction Atlas subtree-size product, which reads more of the full hierarchy.

## 10. Implementation and validation

Added `src/enterprise_math/refinement_forest.py` with the index formula, augmented matrix, exact Bareiss determinant, star helpers, and Prüfer degree enumeration. `tests/test_refinement_forest.py` checks direct determinants against X67, shape-independence for unit capacities, star formulas, and min/max extrema over small complete Prüfer enumerations.

## 11. Prior-art boundary

Tree incidence matrices, reduced-incidence unimodularity, Prüfer sequences, and degree-sequence combinatorics are established mathematics. P019 makes no general graph-theory priority claim. The project-specific research interface is their role in capacity-weighted exact-refinement coordinates.

## 12. Next steps

1. compare `I_rel` with actual relation-tag bit lengths;
2. optimize trees for partial-refinement operation families rather than global index alone;
3. derive determinant/index ratios for local relation-tree basis exchanges;
4. support adaptive forest rerouting as capacities change;
5. combine rank cost `k-ell` and lattice density `I_rel` in P018 precision-selection costs.
