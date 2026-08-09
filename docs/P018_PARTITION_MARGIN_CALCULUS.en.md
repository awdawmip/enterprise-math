# P018 — Exact Partition-Margin Calculus

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact coarse/fine proof-margin transport under finite partition refinement  
Origin: distilled from the P017 MC08 precision hierarchy  
Novelty: `NOVELTY_UNVERIFIED`; the identities are elementary finite algebra, while the project-specific content is their role as an exact precision-compensation calculus.

## 1. Block margin

Let a finite precision block `B` carry signed integer coordinates `x_s,y_s`. Define

\[
X_B=\sum_{s\in B}x_s,
\qquad
Y_B=\sum_{s\in B}y_s,
\qquad
Z_B=\sum_{s\in B}x_sy_s.
\]

The block capacity margin is

\[
\boxed{D_B=X_BY_B-Z_B.}
\]

Expanding the product gives

\[
\boxed{
D_B=\sum_{s\ne t\in B}x_sy_t.
}
\]

Thus the margin is exactly the off-diagonal interaction removed by retaining only the diagonal observable `Z_B`.

## 2. Exact partition transport

For any finite partition

\[
B=\bigsqcup_i B_i,
\]

write `X_i=X_{B_i}`, and similarly for `Y_i,D_i`. Then

\[
\boxed{
D_B
=
\sum_iD_i
+
\sum_{i\ne j}X_iY_j.
}
\]

This is an identity, not an estimate.

For a binary split `B=L sqcup R`,

\[
\boxed{
D_B
=D_L+D_R
+X_LY_R+X_RY_L.
}
\]

The two final terms are the exact sibling compensation present at coarse precision and removed when `L` and `R` are observed separately.

## 3. Positive-cone persistence

Suppose a hypothesis forces every child block into

\[
X_i\ge0,
\qquad Y_i\ge0,
\qquad D_i\ge0.
\]

Then every cross term `X_iY_j` is nonnegative. Hence

\[
D_B\ge\sum_iD_i\ge0.
\]

Contrapositively,

\[
\boxed{
D_B<0
\Longrightarrow
\text{at least one refined child also leaves the admissible cone.}
}
\]

So a coarse certificate cannot disappear under compatible refinement. The persistence follows from the exact transport law rather than from an independent monotonicity assumption.

## 4. Exact masking and unmasking

Outside the positive cone, a fine negative margin can be hidden by a positive coarse compensation term.

Take

- left block: `x=(-1,0)`, `y=(0,1)`, giving `D_L=-1`;
- right singleton: `x=(3)`, `y=(0)`, giving `D_R=0`.

The sibling compensation equals

\[
X_LY_R+X_RY_L=3.
\]

Therefore

\[
\boxed{D_B=-1+0+3=2.}
\]

The coarse observation has positive margin even though the left child already carries a negative certificate. Refinement does not merely improve a numerical approximation: it removes a precisely identified integer interaction term.

## 5. Telescoping precision shells

Repeatedly refine blocks until singleton resolution. Let

\[
M_m=\sum_{B\in\mathcal P_m}D_B
\]

be the total block margin at precision level `m`.

For one binary refinement step define the shell compensation

\[
C_m
=
\sum_{B\in\mathcal P_m}
\bigl(X_{L(B)}Y_{R(B)}+X_{R(B)}Y_{L(B)}\bigr),
\]

with zero contribution from blocks already singleton.

The binary transport identity gives

\[
\boxed{M_m=M_{m+1}+C_m.}
\]

At singleton resolution every block contains one state, so `D=xy-xy=0` and `M_term=0`. Therefore

\[
\boxed{
M_0=\sum_{m<\mathrm{term}}C_m.
}
\]

The entire coarse margin is exactly decomposed into precision-shell compensation. No limit, derivative, probability model, or hidden continuum is required.

## 6. P017 MC08 specialization

For the canonical P017 mirror precision certificate, put

\[
x_r=a_r-1,
\qquad y_r=b_r-1.
\]

Then on each radius block `B`,

\[
X_B=U_-^{(B)},
\qquad
Y_B=U_+^{(B)},
\]

and

\[
D_B=U_-^{(B)}U_+^{(B)}-V^{(B)}.
\]

The MC08 product certificate is exactly `D_B<0`. Under hypothetical prime-free behavior every singleton `x_r,y_r` is nonnegative, so all compatible merge compensations lie in the nonnegative cone and certificate persistence follows immediately.

This identifies what the precision hierarchy is doing algebraically: coarse blocks contain cross-radius compensation terms; refinement removes those terms layer by layer until the signed local structure becomes visible.

## 7. Scope boundary

The partition identity is valid for arbitrary signed integer sequences and therefore cannot by itself prove the P017 prime target. It is a foundational accounting law, not a hidden number-theoretic theorem.

Its value is structural: it gives P018 an explicit answer to the question “what information is removed when proof precision is lowered?” for a nontrivial class of bilinear proof margins.

The next foundation question is whether other P018 proof observables admit exact merge laws of the same type, so that low/high precision cancellation can be represented by finite shell terms rather than informal approximation language.

## 8. Executable assets

- `src/enterprise_math/precision_partition_margin.py`
- `tests/test_precision_partition_margin.py`

The tests verify the general partition identity, the binary transport law, positive-cone persistence, a genuine coarse-masking example, and exact telescoping to singleton precision.
