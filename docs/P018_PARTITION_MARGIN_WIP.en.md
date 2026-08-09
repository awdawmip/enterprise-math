# P018 v2 — Exact Partition-Margin Transport WIP

Status: `ACTIVE PROGRAM RESEARCH / NOT CANONICAL`  
Scope: exact algebra of coarse/fine proof margins under finite partition refinement  
Origin: extracted from the P017 MC08 finite-radius precision hierarchy  
Novelty: `NOVELTY_UNVERIFIED`; the algebraic identities are elementary, while the P018 role is their interpretation as exact precision-compensation accounting.

## 1. Block observables

Let a finite precision block `B` carry signed integer coordinates `x_s,y_s`. Define

\[
X_B=\sum_{s\in B}x_s,
\qquad
Y_B=\sum_{s\in B}y_s,
\qquad
Z_B=\sum_{s\in B}x_sy_s.
\]

Define the capacity margin

\[
\boxed{D_B=X_BY_B-Z_B.}
\]

Expanding the product gives the exact off-diagonal form

\[
\boxed{
D_B=\sum_{s\ne t\in B}x_sy_t.
}
\]

Thus `D_B` measures cross-state interaction that is invisible in the diagonal term `Z_B`.

## 2. Exact partition transport

Let

\[
B=\bigsqcup_{i=1}^m B_i
\]

be any finite partition. Put `X_i=X_{B_i}`, and similarly for `Y_i,D_i`. Then

\[
\boxed{
D_B
=
\sum_iD_i
+
\sum_{i\ne j}X_iY_j.
}
\]

### Proof

Because `X_B=sum_i X_i` and `Y_B=sum_i Y_i`,

\[
X_BY_B
=
\sum_iX_iY_i+
\sum_{i\ne j}X_iY_j.
\]

Also `Z_B=sum_i Z_i`. Therefore

\[
D_B
=X_BY_B-Z_B
=
\sum_i(X_iY_i-Z_i)
+
\sum_{i\ne j}X_iY_j.
\]

∎

For a binary split `B=L sqcup R`, this becomes

\[
\boxed{
D_B
=D_L+D_R
+X_LY_R+X_RY_L.
}
\]

The last two terms are the **exact sibling compensation** present at coarse precision and removed when the block is refined.

## 3. Positive-cone persistence

Suppose a proof hypothesis forces every child block into

\[
X_i\ge0,
\qquad Y_i\ge0,
\qquad D_i\ge0.
\]

Then every cross term `X_iY_j` is also nonnegative, so

\[
D_B\ge\sum_iD_i\ge0.
\]

Hence if the parent violates the nonnegative margin condition, at least one child must violate it after any refinement.

This recovers coarse-certificate persistence from a stronger exact identity rather than from a one-off inequality.

## 4. Precision can remove exact masking terms

Signed coordinates outside the hypothesis cone can make a fine block have negative margin even while the parent has positive margin.

A concrete example is

- left block: `x=(-1,0)`, `y=(0,1)`, so `D_L=-1`;
- right singleton: `x=(3)`, `y=(0)`, so `D_R=0`;
- sibling compensation: `3`.

Therefore

\[
D_B=-1+0+3=2.
\]

At coarse precision the negative fine margin is hidden exactly by a positive cross-block compensation term. Refinement does not improve an approximation; it removes a precisely identified integer interaction.

This is the most direct algebraic form yet of the project heuristic

\[
\boxed{
\text{low precision proof}
\to
\text{refinement}
\to
\text{exact high/low cancellation accounting}.
}
\]

## 5. Telescoping precision shells

Apply binary refinement repeatedly until singleton blocks. Let

\[
M_m=\sum_{B\in\mathcal P_m}D_B
\]

be the sum of block margins at precision level `m`.

For each refinement step define the shell compensation

\[
C_m
=
\sum_{B\in\mathcal P_m}
\bigl(X_{L(B)}Y_{R(B)}+X_{R(B)}Y_{L(B)}\bigr),
\]

with zero contribution from blocks already singleton.

Then

\[
\boxed{M_m=M_{m+1}+C_m.}
\]

At singleton precision every block has one state and therefore `D=0`, so `M_term=0`. Consequently

\[
\boxed{
M_0=\sum_{m<\mathrm{term}}C_m.
}
\]

The coarse margin is therefore exactly decomposed into precision-shell compensation; no limit, derivative, probability model, or hidden continuum is required.

## 6. Relation to P017 MC08

For MC08 use

\[
x_r=a_r-1,
\qquad y_r=b_r-1.
\]

Then

\[
X_B=U_-^{(B)},
\qquad Y_B=U_+^{(B)},
\qquad D_B=U_-^{(B)}U_+^{(B)}-V^{(B)}.
\]

The MC08 product certificate is exactly `D_B<0`, while the other certificate channels test negativity of `X_B`, `Y_B`, or `V_B`.

Under hypothetical prime-free behavior, all singleton `x_r,y_r` are nonnegative, so every sibling compensation is nonnegative. This gives a structural explanation of MC08 refinement persistence.

## 7. Boundary and next question

The partition identity alone cannot prove a prime exists; it is valid for arbitrary signed sequences. Its value is to isolate precisely what coarse precision discards and what refinement removes.

The next foundational question is whether other P018 proof observables admit similar exact merge/shell laws, producing a reusable finite-precision calculus of proof margins rather than one problem-specific decomposition.

Executable WIP assets:

- `src/enterprise_math/precision_partition_margin.py`;
- `tests/test_precision_partition_margin.py`.
