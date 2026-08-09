# P019 — Relation LEGO Core

Status: `RESEARCH WIP / DISTILLED CORE`

Purpose: distill the common structure that has remained stable across the P019 proof supplements. This is not a final foundation and does not claim that physical space has been proved to be `A_p/FCC`; detailed proofs, counterexamples, implementation, and prior-art boundaries remain in the supplements.

## 1. Unit invariance

For

\[
\Psi_{m,s}(c)=\min_{a_1+\cdots+a_m=c}\sum_{u=1}^m|a_u|^s,
\]

\[
\boxed{\Psi_{m,s}(1)=1}
\]

for every finite `m>=1,s>=1`. Changing the number of structural slots does not change the numerical identity of one unit.

## 2. Present block state

A current state has `k` distinguishable blocks with positive integer capacities `m_i`, integer totals `c_i`, and fixed grand total `C=sum c_i`. Its relation dimension is

\[
\boxed{dim_{relation}=k-1.}
\]

## 3. Canonical weighted relation field

Define

\[
\boxed{Z_{ij}=m_jc_i-m_ic_j,}
\qquad
\boxed{Z=cm^T-mc^T.}
\]

Unit blocks reduce to ordinary differences. The field is skew and obeys

\[
\boxed{m_kZ_{ij}+m_iZ_{jk}+m_jZ_{ki}=0.}
\]

Given capacities, grand total, and a legal field,

\[
\boxed{c_i=(m_iC+\sum_jZ_{ij})//M,\quad M=\sum_i m_i.}
\]

Thus `(m,C,Z)` is a tree-independent present-state relation representation.

## 4. Dimension contraction as partition quotient

Let `A` be a 0-1 incidence matrix of a partition from `k` fine blocks to `ell` coarse blocks. Then

\[
\boxed{m'=Am,\qquad c'=Ac,\qquad Z'=AZA^T.}
\]

Nested coarsening composes exactly:

\[
\boxed{Q_{A_2}\circ Q_{A_1}=Q_{A_2A_1}.}
\]

A binary contraction tree is an execution/chart choice, not necessary present-state ontology.

## 5. Dimension-loss kernel

Define

\[
\boxed{K_A=\ker_{\mathbb Z}A.}
\]

Then

\[
\boxed{rank K_A=k-\ell,}
\]

fine states with one coarse image form `c+K_A`, and coarse-invisible additive motions are exactly `K_A`. Hence

\[
\boxed{\text{state fiber}=\text{invisible motion lattice}=\text{dimension-loss kernel}.}
\]

A binary merge deletes one independent internal relation `z=Z_ij`; retaining it exactly reverses the two child totals.

## 6. Relation dynamics

For any zero-total integer update `delta`,

\[
\boxed{Z\mapsto Z+\delta m^T-m\delta^T.}
\]

Partition coarsening commutes exactly:

\[
\boxed{Q_A\circ T_\delta=T_{A\delta}\circ Q_A.}
\]

A fine primitive transfer becomes zero inside one coarse block or the corresponding primitive transfer between two coarse blocks.

## 7. Collision observation family

Define

\[
\boxed{E_{\mathbf m}^{(s)}(c)=\sum_i\Psi_{m_i,s}(c_i).}
\]

If `c=mq+r`, `0<=r<m`, then

\[
\boxed{\Psi_{m,s}(c)=(m-r)|q|^s+r|q+1|^s.}
\]

Its integer forward slope is

\[
\boxed{\Psi(c+1)-\Psi(c)=|q+1|^s-|q|^s,}
\]

so fiber optimization can use finite one-unit exchange rather than calculus.

## 8. Balls as relation-state sublevel sets

Define

\[
\boxed{B_{\mathbf m}^{(s)}(T)=\{c:\sum c_i=C,\ E_{\mathbf m}^{(s)}(c)\le T\}.}
\]

Because `(m,C,Z)` recovers `c`, the ball is a sublevel set on weighted relation state.

At zero total, `s=1` satisfies

\[
\boxed{M E^{(1)}=2\max_S Z(S,S^c),}
\]

and for unit zero-sum states the square layer satisfies

\[
\boxed{\sum_{i<j}Z_{ij}^2=2Nq.}
\]

Graph and radial geometry are therefore different integer observation channels on one relation state.

## 9. Arbitrary-dimensional ball quotient

For any partition `A`,

\[
\boxed{\min_{Ac=y}E_{\mathbf m}^{(s)}(c)=E_{A\mathbf m}^{(s)}(y)}
\]

and hence

\[
\boxed{Q_A(B_{\mathbf m}^{(s)}(T))=B_{A\mathbf m}^{(s)}(T).}
\]

Every finite-dimensional tagged ball therefore contracts to the exact lower-dimensional member of the same family, with no limit, integral, or continuous projection.

## 10. Directional excavation and boundary sections

For one oriented binary merge, the finite energy fiber is an integer interval and the unique directional exiting state is its endpoint. Therefore

\[
\boxed{C_{\mathbf m,j\to i}^{(s)}(T)\cong B_{\mathbf m'}^{(s)}(T).}
\]

An oriented contraction flag composes these endpoint lifts into a section `L_F` with

\[
\boxed{Q_A\circ L_F=id.}
\]

The quotient is tree-independent, while the selected fine boundary witness can be flag-dependent.

## 11. Exact refinement memory

If future operations are quotient-compatible, deleted internal relations may be erased permanently. If exact refinement is allowed, a spanning tree of internal weighted relations inside each coarse block recovers all child totals. Across a `k -> ell` coarsening the Refinement Forest needs exactly

\[
\boxed{k-\ell}
\]

independent relation witnesses, equal to the lost relation rank. Full merge chronology is provenance, not necessary present-state reconstruction.

## 12. Relation precision scale

Let

\[
\boxed{g=\gcd(m_i).}
\]

Then

\[
\boxed{m=g\hat m,\qquad Z=g\hat Z,\qquad\gcd(\hat m)=1.}
\]

Define relation quantum `g` and field-preserving translation period `tau=M/g`; then

\[
\boxed{g\tau=M.}
\]

Partition coarsening satisfies `g_fine | g_coarse`. Primitive-state coarsening produces an integer scale carry `g'=g h`.

## 13. Three internal readings of dimension

In the current `A_p` working model,

\[
\boxed{dim_{growth}=dim_{contract}=dim_{relation}=p.}
\]

Dimension is therefore measurable by independent discrete procedures rather than only declared by coordinate count.

## 14. Common minimum relation geometry for `s>=2`

Write `C=Mq+r`, `0<=r<M`. Every global minimizer for every `s>=2` uses unit values `q/q+1`. If block `i` contains `h_i` of the `q+1` units,

\[
c_i=m_iq+h_i,\qquad\sum h_i=r,
\]

and

\[
\boxed{Z_{ij}=m_jh_i-m_ih_j,\qquad |Z_{ij}|\le m_im_j.}
\]

Power order changes the minimum value but not the minimum relation geometry.

## 15. Future-safe collapse rule

A quotient `Q` is safe for an operation `T` only when

\[
\boxed{Q(x)=Q(y)\Rightarrow Q(Tx)=Q(Ty),}
\]

or equivalently `Q\circ T=bar T\circ Q`. If all future generators and observations factor through `Q`, distinctions erased by `Q` can be forgotten permanently.

Thus

\[
\boxed{\text{safe collapse}=\text{quotient by future operational indistinguishability}.}
\]

## 16. Layering discipline

**Canonical/tree-independent:** weighted relation state `(m,C,Z)`, partition quotient `Q_A`, kernel `K_A`, collision observation `E^(s)`, relation scale `g`.

**Charts/computational tools:** unit pair field, spanning-tree flow chart, Contraction Atlas imbalance chart, Refinement Forest.

**Witness/provenance:** directional boundary sections, contraction flags, actual process history / P021 witness relations.

These layers must not be conflated.

## 17. Prior-art discipline

The core reuses established mathematics including `A_n` root lattices, integer incidence/cut/flow spaces, spanning-tree bases, Smith normal form, separable/discrete convex minimization, quotient congruence/bisimulation-type ideas, and exterior/wedge matrix representations. P019 does not rename these as original. Any novelty claim must concern the verified overall finite-precision/dimension-contraction combination and requires a dedicated lineage audit.

## 18. Single next research question

Do not add more primitives horizontally. The next stage asks only:

\[
\boxed{\text{Given a future operation language, what is the minimum exact relation state?}}
\]

This includes automatic safe erasure of internal relations, demand-driven refinement, identifying which P021 witness identities must remain as provenance, connecting P018 precision selection to relation-state refinement cost, and formalizing the partition quotient/kernel/directional-ball core in Lean.
