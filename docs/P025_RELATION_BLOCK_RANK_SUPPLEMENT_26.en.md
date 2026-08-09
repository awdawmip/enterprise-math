# P025 Supplement 26 — Block Count Minus Relation Rank: General Dimension Law for Relation-Conditioned Derivatives

Status: `ACTIVE RESEARCH NOTE / NONCANONICAL`  
Owner generation: `program/p025-access-tail-stage18`  
Depends on: P025 Supplements 19–25; A3/P023 relation and quotient semantics  
Hard block: `NONE`

## 1. Why ABC produced a two-dimensional block-value state

The block-value quotient of Supplements 20–25 repeatedly produces a rank-two lattice for a primitive abc triple.

This is not special to Wronskians and not a numerical accident. It is the first case of a general finite relation-rank law.

Consider positive pairwise-coprime integer blocks

\[
\boxed{n_1,\ldots,n_m}
\]

and a finite family of integer additive relations

\[
\boxed{
L n=0,
\qquad
L\in\mathbb Z^{r\times m}.
}
\]

Pairwise coprimality ensures that the prime-coordinate supports of distinct non-unit blocks are disjoint.

## 2. Block derivative images

For each non-unit block define its raw derivative image generator

\[
\boxed{
A_i
=
\gcd_{p\mid n_i}
\frac{n_i v_p(n_i)}p
>0.
}
\]

Then the possible arithmetic derivative value of block `i` is

\[
t_i\in A_i\mathbb Z.
\]

If `n_i=1`, its derivative value is identically zero; such a block contributes no active derivative coordinate.

Let `I` be the active non-unit block set and let

\[
\boxed{s=|I|.}
\]

Delete unit columns from the relation matrix and call the resulting matrix

\[
L_I.
\]

## 3. P025-T75 — exact block-value relation lattice

Linearity of arithmetic derivations sends every declared integer relation

\[
\sum_i L_{ji}n_i=0
\]

to

\[
\sum_i L_{ji}t_i=0.
\]

Therefore the compressed block-value state space is exactly

\[
\boxed{
\Lambda_{L,A}
=
\left(\prod_{i\in I}A_i\mathbb Z\right)
\cap
\ker_{\mathbb Z}(L_I).
}
\]

Every fine relation-adapted witness maps into this lattice.

Conversely, every point of this lattice has independent prime-coordinate preimages inside the disjoint blocks, and those preimages satisfy all derivative relations by the defining kernel condition. Hence the fine witness family surjects onto `Lambda_(L,A)`.

This is the general block-value quotient theorem for pairwise-coprime relation systems.

## 4. P025-T76 — compressed rank equals active block count minus relation rank

Write

\[
D_A=\operatorname{diag}(A_i)_{i\in I}.
\]

Every compressed state has the form

\[
t=D_Ax,
\qquad
x\in\mathbb Z^s,
\]

with

\[
L_I D_A x=0.
\]

Since `D_A` is invertible over `Q`,

\[
\operatorname{rank}_{\mathbb Q}(L_I D_A)
=
\operatorname{rank}_{\mathbb Q}(L_I).
\]

Therefore

\[
\boxed{
\operatorname{rank}_{\mathbb Z}\Lambda_{L,A}
=
s-\operatorname{rank}_{\mathbb Q}L_I.
}
\]

The rank depends on the number of active blocks and the number of independent relation directions, not on the total number of prime coordinates inside the blocks.

## 5. ABC as the first case

For an ordinary non-unit abc triple,

\[
L=(1,1,-1),
\]

so

\[
s=3,
\qquad
\operatorname{rank}L=1.
\]

Hence

\[
\boxed{
\operatorname{rank}\Lambda_{abc}=3-1=2.
}
\]

This explains the rank-two ceiling used throughout Supplements 20–25.

For the unit boundary `1+b=c`, the unit block is deleted first. Two active blocks remain and the restricted row is `(1,-1)`, so

\[
\boxed{
\operatorname{rank}=2-1=1.
}
\]

This is exactly why the unit Wronskian/floor state collapsed to one common derivative value.

## 6. Many fine prime coordinates can still produce rank two

Take

\[
\boxed{6+35=41.}
\]

The blocks are pairwise coprime. Their fine prime supports are

\[
\{2,3\},
\quad
\{5,7\},
\quad
\{41\},
\]

so the fine arithmetic witness has five prime-coordinate directions.

Nevertheless there are only three active blocks and one independent relation. Therefore

\[
\boxed{
5\text{ fine prime coordinates}
\longrightarrow
2\text{ global block relation directions}.
}
\]

The exact reduction is structural, not approximate.

## 7. Multiple independent relations reduce dimension further

Consider blocks

\[
(1,2,3,5)
\]

with declared relations

\[
1+2=3,
\qquad
2+3=5.
\]

After removing the unit block, the active derivative-value variables correspond to `(2,3,5)`. The restricted relation rows are

\[
(1,-1,0),
\qquad
(1,1,-1),
\]

which have rational rank two.

Thus

\[
\boxed{
\operatorname{rank}\Lambda
=3-2=1.
}
\]

For example the derivative-value state

\[
(0,1,1,2)
\]

satisfies both relations.

## 8. P025-T77 — certificate rank ceiling for general relation systems

Let any future certificate family depend linearly only on the block derivative values:

\[
H:\Lambda_{L,A}\to\mathbb Z^q.
\]

Then automatically

\[
\boxed{
\operatorname{rank}_{\mathbb Q}H(\Lambda_{L,A})
\le
s-\operatorname{rank}_{\mathbb Q}L_I.
}
\]

Thus Stage 25's rank-two certificate ceiling is just the abc specialization of the general relation-rank law.

Adding more certificate outputs can never create more independent state directions than remain after the declared block relations have already been imposed.

## 9. Architectural consequence

The general compression chain is

\[
\boxed{
\text{fine prime coordinates inside blocks}
\to
\text{one derivative value per active block}
\to
\ker(L_I)
\to
\text{certificate/decision quotient}.
}
\]

The decisive dimension is

\[
\boxed{
\text{active block count}
-
\text{independent relation rank}.
}
\]

This separates two levels that should not be conflated:

- internal arithmetic complexity inside a block can be arbitrarily rich by Supplement 19;
- global relation coupling can still have very low rank.

## 10. Scope boundary

Pairwise coprimality is essential to the simple surjective product argument because it gives disjoint prime-coordinate supports. If two blocks share primes, their fine derivative coordinates are coupled before the declared relation matrix is even applied; the present theorem does not silently quotient that overlap away.

Likewise, nonlinear certificate observables or future operations that inspect within-block witness identity require a finer language-specific state.

## 11. Prior-art boundary

Kernel dimension, rank-nullity, diagonal scaling over `Q`, and direct products over disjoint coordinate sets are standard linear algebra/module facts.

P025 does not claim them as new mathematics. The project-side candidate is the exact arithmetic-derivative block compression and its use as a finite-precision dimension law across relation-conditioned certificate systems.

Because this result is broader than abc, it should be relayed to A3/P023 for ownership audit rather than silently promoted as a P025-specific foundation theorem.

## 12. Executable assets

Added:

- `src/enterprise_math/relation_block_rank.py`
  - pairwise-coprime relation-block system validation;
  - exact rational matrix rank;
  - active block/image-generator state;
  - compressed rank calculation;
  - exact derivative-value lattice membership;
  - generic certificate rank ceiling.
- `tests/test_relation_block_rank.py`
  - ordinary abc rank two;
  - unit abc rank one;
  - `6+35=41` five-prime-coordinate reduction;
  - two independent relations leaving one direction;
  - one relation on four active blocks leaving rank three.

## 13. Next frontier

No hard block exists. Continue with:

1. quantify the **rank gain** contributed by a declared certificate family beyond the relation rows;
2. identify the P023-coarsest exact certificate quotient as an image of the relation kernel;
3. extend access-cost/Pareto semantics from one relation row to several relations;
4. study shared-prime blocks as the first genuine failure of the independent-block product model;
5. relay the dimension law to A3/P023 before any Foundation consideration.
