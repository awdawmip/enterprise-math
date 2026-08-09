# P019 Supplement 22 — Partition Kernel, State–Motion Co-Kernel, and Arbitrary-Dimension Ball Quotients

Status: `RESEARCH WIP / EXACT INTEGER QUOTIENT THEOREMS PROVED`

## 1. Goal

State relation quotients, invisible updates, binary directional excavation, and arbitrary partition coarsening all share one integer kernel. This supplement identifies that kernel and extends the one-merge excavation theorem to arbitrary partitions.

## 2. Partition kernel lattice

For a partition matrix `A: Z^k -> Z^ell`, define

\[
\boxed{K_A=\{\eta\in\mathbb Z^k:A\eta=0\}.}
\]

It consists exactly of integer changes whose sum vanishes inside every coarse group, and

\[
\boxed{rank\,K_A=k-\ell.}
\]

## 3. P019-X75/X76 — State fibers and invisible motions are the same kernel

All fine total vectors with the same coarse totals as `c` are

\[
\boxed{c+K_A.}
\]

All additive integer updates invisible to the same coarse quotient are exactly

\[
\boxed{K_A.}
\]

Thus the state-fiber direction and invisible-motion direction are not merely equal in rank: they are the same integer lattice.

## 4. Primitive transfers under coarsening

For a fine primitive transfer `delta=e_i-e_j`,

\[
A\delta=0
\]

when `i,j` lie in the same coarse block; otherwise it becomes the corresponding coarse primitive transfer `e_alpha-e_beta`. Primitive adjacency therefore either disappears as internal motion or survives as primitive coarse adjacency.

## 5. P019-X77 — Weighted relation dynamics commute with partition quotients

For

\[
Z=cm^T-mc^T
\]

and any zero-total integer update `delta`,

\[
\boxed{Z'=Z+\delta m^T-m\delta^T.}
\]

Coarsening gives

\[
\boxed{
Q_A\circ T_\delta=T_{A\delta}\circ Q_A.
}
\]

All predeclared additive updates therefore commute exactly with relation coarsening. Unsafe behavior arises only when the update-selection rule itself reads distinctions erased by the quotient.

## 6. Update-lattice exact sequence

The total-preserving update lattice `U_k` has rank `k-1`, `U_ell` has rank `ell-1`, partition aggregation is surjective, and its kernel is `K_A`. In compact form,

\[
\boxed{0\to K_A\to U_k\to U_\ell\to0.}
\]

This statement is used only as an exact integer kernel/surjection identity; no continuous homological machinery is required.

## 7. Arbitrary-partition collision-power fiber minimum

For

\[
E_{\mathbf m}^{(s)}(c)=\sum_i\Psi_{m_i,s}(c_i)
\]

and coarse totals `y=Ac`, the exact fiber minimum is

\[
\boxed{
\min_{Ac=y}E_{\mathbf m}^{(s)}(c)=E_{A\mathbf m}^{(s)}(y).
}
\]

Each coarse group minimizes independently by the same min-plus block-addition law.

## 8. P019-X78 — The image of every fine ball is exactly the lower tagged ball

For the fixed-total ball

\[
B_{\mathbf m}^{(s)}(T),
\]

\[
\boxed{
Q_A\bigl(B_{\mathbf m}^{(s)}(T)\bigr)=B_{A\mathbf m}^{(s)}(T).
}
\]

A fine ball point maps inside the coarse ball because the coarse fiber minimum cannot exceed its fine cost; every coarse ball point has a fine minimizer with exactly the same coarse cost.

## 9. P019-X79/X80 — Oriented contraction flags give exact boundary sections

Factor a coarse partition into a sequence of oriented binary merges. Each step has the Supplement 16 unique directional-boundary lift. Composing those lifts gives

\[
\boxed{L_\mathcal F:B_{A\mathbf m}^{(s)}(T)\hookrightarrow B_{\mathbf m}^{(s)}(T)}
\]

with

\[
\boxed{Q_A\circ L_\mathcal F=id.}
\]

The quotient is tree-independent, but the selected fine boundary witness can depend on the contraction flag. This is exactly the earlier witness-nonassociativity phenomenon: present coarse state is unique while representative/provenance selection is not.

## 10. Higher-codimension boundaries

Repeating `r` binary boundary lifts embeds a `p-r` dimensional tagged ball as a nested directional-boundary flag inside the original `p` dimensional ball. Every step uses the same one-unit endpoint theorem; no new high-dimensional formula is required.

## 11. Implementation

Added `src/enterprise_math/relation_dynamics.py`, `src/enterprise_math/partition_dynamics.py`, and corresponding tests for relation updates, update/coarsening naturality, kernel bases, exact coarse-update lifts, and primitive-transfer images.

## 12. Current unified statement

One finite dimension quotient acts simultaneously on

\[
c\mapsto Ac,
\qquad
Z\mapsto AZA^T,
\qquad
\delta\mapsto A\delta,
\qquad
B_{\mathbf m}^{(s)}\mapsto B_{A\mathbf m}^{(s)},
\]

with hidden detail

\[
\boxed{K_A=\ker A.}
\]

Thus

\[
\boxed{
\text{state fiber}
=
\text{invisible motion lattice}
=
\text{dimension-loss kernel}.
}
\]

## 13. Next steps

1. identify Refinement Forest coordinates directly as a basis/dual coordinate system on `K_A`;
2. use discrete-convex exchange structure on higher-rank collision-power fibers;
3. classify the minimum witness quotient needed to make boundary sections flag-independent for a declared future language;
4. formalize the kernel and sphere-quotient results in Lean;
5. rewrite P018 precision refinement and P021 witness composition in the same partition-kernel language.
