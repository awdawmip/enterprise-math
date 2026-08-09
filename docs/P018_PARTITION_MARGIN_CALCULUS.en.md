# P018 — Exact Partition-Margin Calculus

Status: `ACTIVE RESEARCH NOTE`  
Scope: exact coarse/fine proof-observable transport under finite partition refinement  
Origin: distilled from the canonical P017 MC08 precision hierarchy  
Novelty: `NOVELTY_UNVERIFIED`; the algebraic identities are elementary finite algebra, while the project-specific content is their use as an exact precision-compensation calculus.

## 1. Four block observables

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

The natural block observation is therefore

\[
\boxed{
\Phi(B)=(X_B,Y_B,Z_B,D_B).
}
\]

The first three coordinates are additive signed observables; the fourth records the off-diagonal interaction created by coarse aggregation.

## 2. Exact partition transport

For any finite partition

\[
B=\bigsqcup_i B_i,
\]

write `X_i=X_{B_i}` and similarly for the other coordinates. Then

\[
\boxed{
X_B=\sum_iX_i,
\quad
Y_B=\sum_iY_i,
\quad
Z_B=\sum_iZ_i,
}
\]

while

\[
\boxed{
D_B
=
\sum_iD_i
+
\sum_{i\ne j}X_iY_j.
}
\]

These are identities, not estimates.

For a binary split `B=L sqcup R`,

\[
\boxed{
D_B
=D_L+D_R
+X_LY_R+X_RY_L.
}
\]

The last two terms are the exact sibling compensation present at coarse precision and removed when the children are observed separately.

## 3. Merge-closed proof cone

Define the admissible cone

\[
\boxed{
\mathcal K
=
\{(X,Y,Z,D)\in\mathbb Z^4:
X\ge0,\ Y\ge0,\ Z\ge0,\ D\ge0\}.
}
\]

Suppose every child observation `Phi(B_i)` lies in `K`. Then the additive coordinates of the parent satisfy

\[
X_B\ge0,
\qquad Y_B\ge0,
\qquad Z_B\ge0.
\]

Also every `X_iY_j` is nonnegative, so the transport identity gives

\[
D_B
=
\sum_iD_i+\sum_{i\ne j}X_iY_j
\ge0.
\]

Hence

\[
\boxed{
\Phi(B_i)\in\mathcal K\ \forall i
\Longrightarrow
\Phi(B)\in\mathcal K.
}
\]

The admissible proof cone is therefore **closed under coarse merging**.

Contrapositively,

\[
\boxed{
\Phi(B)\notin\mathcal K
\Longrightarrow
\text{at least one refined child lies outside }\mathcal K.
}
\]

So a proof certificate obtained at coarse precision cannot disappear under compatible refinement. This is a structural consequence of the exact merge law, not an independently imposed monotonicity principle.

## 4. Two distinct kinds of coarse masking

The four-coordinate form exposes two mechanisms by which low precision can hide fine information.

### 4.1 Additive sign cancellation

Because `X`, `Y`, and `Z` are additive, a negative child contribution can be hidden by positive sibling contributions:

\[
X_B=\sum_iX_i,
\qquad
Y_B=\sum_iY_i,
\qquad
Z_B=\sum_iZ_i.
\]

Refinement does not change the total; it localizes the signed contributions so a negative block can become visible.

### 4.2 Bilinear sibling compensation

The capacity margin has an additional coarse interaction term. For example take

- left block: `x=(-1,0)`, `y=(0,1)`, giving `D_L=-1`;
- right singleton: `x=(3)`, `y=(0)`, giving `D_R=0`.

The sibling compensation is

\[
X_LY_R+X_RY_L=3,
\]

so

\[
\boxed{D_B=-1+0+3=2.}
\]

The parent margin is positive even though one child has a negative margin. Refinement removes a precisely identified integer interaction; it is not merely a better numerical approximation.

## 5. Telescoping precision shells for the margin channel

Repeatedly refine blocks until singleton resolution. Let

\[
M_m=\sum_{B\in\mathcal P_m}D_B
\]

be the total margin at precision level `m`.

For one binary refinement step define

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

At singleton resolution `D=xy-xy=0`, hence `M_term=0` and

\[
\boxed{
M_0=\sum_{m<\mathrm{term}}C_m.
}
\]

The coarse bilinear margin is therefore exactly decomposed into precision-shell compensation. No limit, derivative, probability model, or hidden continuum is required.

The additive coordinates have an even simpler transport law: their global sums are invariant across refinement, while refinement changes only **where** the signed mass is visible.

## 6. P017 MC08 specialization

For the canonical P017 mirror precision certificate, set

\[
x_r=a_r-1,
\qquad
y_r=b_r-1.
\]

Then for each radius block `B`,

\[
X_B=U_-^{(B)},
\qquad
Y_B=U_+^{(B)},
\qquad
Z_B=V^{(B)},
\]

and

\[
D_B
=U_-^{(B)}U_+^{(B)}-V^{(B)}.
\]

Thus the four MC08 certificate channels are exactly the four ways in which `Phi(B)` can leave `K`:

\[
U_-^{(B)}<0,
\quad
U_+^{(B)}<0,
\quad
V^{(B)}<0,
\quad
U_-^{(B)}U_+^{(B)}-V^{(B)}<0.
\]

Under hypothetical prime-free behavior every singleton has `x_r,y_r>=0`, so every compatible block lies in the merge-closed cone. MC08 refinement persistence is therefore an instance of the general P018 transport law.

This also explains why higher precision can reveal a certificate: it removes additive sign masking and bilinear sibling compensation without changing the underlying finite state set.

## 7. Scope boundary

The partition identities hold for arbitrary signed integer sequences and therefore cannot by themselves prove the P017 prime target. They are foundational accounting laws, not hidden number-theoretic theorems.

Their value is structural: P018 can now identify two exact mechanisms lost under coarse proof precision—signed aggregation and cross-block compensation—and represent their removal by finite integer transport rather than informal approximation language.

The next foundation question is which other proof observables admit merge-closed cones or exact shell laws of this type.

## 8. Executable assets

- `src/enterprise_math/precision_partition_margin.py`
- `tests/test_precision_partition_margin.py`

The tests verify the general partition identity, binary transport, off-diagonal form, positive-cone merge behavior, a genuine coarse-masking example, and exact telescoping to singleton precision.
