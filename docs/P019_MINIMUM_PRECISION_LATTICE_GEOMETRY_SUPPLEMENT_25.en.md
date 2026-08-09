# P019 Supplement 25 — Minimum Exact Partition Solver for Integer Linear Dynamics

Status: `RESEARCH WIP / EXACT INTEGER QUOTIENT THEOREM + FINITE PARTITION ALGORITHM`

## 1. First large-class solution of the core problem

The Relation LEGO Core reduces the next research stage to:

> Given a future operation language, find the minimum exact relation state.

This supplement solves an important infinite-state class:

\[
\boxed{c'=Bc+u,\qquad B\in\mathbb Z^{k\times k},\ u\in\mathbb Z^k.}
\]

The state space remains the full integer lattice; no finite state box is enumerated.

## 2. Partition matrix

Let a partition `Pi` aggregate `k` fine coordinates into `ell` coarse blocks through a 0-1 matrix

\[
A\in\{0,1\}^{\ell\times k},
\qquad y=Ac.
\]

## 3. P019-X90 — Exact descent condition for linear dynamics

For `T_B(c)=Bc`, the partition is exact iff there exists an integer coarse matrix `Bbar` such that

\[
\boxed{AB=\bar BA.}
\]

Because partition aggregation `A:Z^k->Z^ell` is surjective, `Bbar` is automatically integer whenever the condition is well-defined.

## 4. P019-X91 — Aggregated column-effect signature criterion

Column `j` of `AB` is the total influence of one unit of fine coordinate `j` on every coarse target block. Therefore X90 is equivalent to:

\[
\boxed{
\sum_{r\in R}B_{ri}=\sum_{r\in R}B_{rj}
}
\]

for all fine coordinates `i,j` in the same current source block and every current target block `R`.

This is a finite static integer signature test.

## 5. P019-X92 — Equivalent kernel-invariance condition

For the dimension-loss kernel

\[
K_A=\ker_{\mathbb Z}A,
\]

\[
\boxed{AB=\bar BA\iff B(K_A)\subseteq K_A.}
\]

The forward implication is immediate. Conversely, if `B` preserves `K_A`, define `Bbar(Ac)=ABc`; kernel invariance makes this well-defined, and surjectivity of `A` gives an integer quotient matrix.

Thus a future linear dynamics is safe exactly when it maps invisible-motion directions back into invisible-motion directions.

## 6. P019-X93 — Affine offsets add no new distinguishability condition

For `T(c)=Bc+u`, once `AB=Bbar A`,

\[
A(Bc+u)=\bar B(Ac)+Au.
\]

Hence the descended affine dynamics is

\[
\boxed{\bar T(y)=\bar By+Au.}
\]

Partition refinement depends only on hidden-to-coarse coupling in the linear part.

## 7. Operation families

For a finite family `B_1,...,B_m`, the partition is exact iff every generator preserves `K_A`, equivalently every matrix satisfies its aggregated-column signature criterion. Once all generators descend, every finite composition descends automatically.

## 8. P019-X94 — Signature refinement algorithm

Starting from an initial partition, assign every fine source coordinate a signature containing:

1. its current coarse source block;
2. for every operation matrix;
3. for every current coarse target block;
4. the sum of that matrix column into the target block.

Split each current block by unequal signatures and repeat until stable. Each non-stable round increases the number of blocks, so termination occurs after at most `k-1` split rounds.

## 9. P019-X95 — The stable partition is the coarsest exact refinement

At stability, all matrices descend by X91.

Let `R` be any other exact refinement of the initial partition. Inductively assume `R` refines the current algorithmic partition. Two coordinates in the same `R` block have equal aggregate effects into every `R` target block under every matrix. A current target block is a union of `R` blocks, so those effects remain equal after summation into every current target block. Therefore the algorithm never separates points that an exact `R` keeps together. Hence `R` refines every iteration and finally refines the stable output.

Thus

\[
\boxed{
\Pi_* = \text{coarsest / minimum-state exact refinement of the initial partition}.}
\]

## 10. Minimum exact weighted relation state

Once `Pi_*` is known, execution no longer needs the fine totals as runtime state. Use

\[
\boxed{(m_*,C,Z_*)=(A_*m,C,A_*ZA_*^T)}
\]

with the descended coarse matrices. If future refinement/history is outside the declared language, distinctions inside `K_(A_*)` may be erased safely.

## 11. Prior-art boundary

This structure is adjacent to established equitable partitions, exact aggregation/lumpability, congruence/bisimulation, partition refinement/automata minimization, and quotient/invariant-subspace dynamics. General matrix factorization and stable partition refinement are not claimed as Enterprise Math inventions.

The P019-specific research interface is their use inside the weighted-relation / partition-kernel / finite-precision dimension-contraction framework.

## 12. Implementation and validation

Added `src/enterprise_math/linear_relation_quotient.py` and `tests/test_linear_relation_quotient.py`, covering exact intertwining, hidden-feedback failure, automatic splitting, joint operation families, brute-force coarsest checks over all candidate partitions of four coordinates, exhaustive 3x3 binary-matrix descent/kernel-invariance equivalence, and affine offsets.

## 13. Meaning

The core problem now has a first large-class automatic solution:

\[
\boxed{
\text{integer affine future language}
\to
\text{finite partition-refinement solver}
\to
\text{minimum exact relation partition}.
}
\]

The underlying state space can remain infinite `Z^k`; exact precision/dimension selection is synthesized from the operations themselves.

## 14. Next steps

1. extend to piecewise-linear / predicate-controlled integer operations by first making branch predicates quotient-readable and then requiring every branch matrix to descend;
2. convert actual P019 weighted-relation dynamics into matrix generators and synthesize their minimum exact partitions;
3. connect P018 precision predicates and observation costs to this solver;
4. investigate finite signature closure for selected nonlinear polynomial maps;
5. formalize X90–X95 in Lean.
