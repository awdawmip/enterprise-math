# Perfect Prime AP HCM0 — codimension-one dual Krein normal

Task: `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT`  
Researcher: `EM-HCM0-HL-FB0860`  
Claim: `CLM-HCM0HL-6F8E2D4389B17C04A521`  
Date: 2026-09-04  
Status: **NONTERMINAL ALL-m COROLLARY — HCM0 REMAINS OPEN**

This note continues directly from `RESIDUE_DUAL_STP_SECANT_FRAME_20260904.md`.

## 1. Common codimension-one polynomial subspace

Let

\[
\theta_q=\frac{q+1}{m},\qquad X_q=r_0+\theta_q,
\qquad q=0,\dots,n,\quad n=m-1.
\]

The residue-dual secant frame factors as

\[
\widehat G_M^{(r_0)}=\Phi_X C_M,
\]

where

\[
\Phi_X[q,k]=\binom{X_q+k-1}{k},\qquad 0\le k\le n-1,
\]

and `C_M` is invertible upper triangular with diagonal `M`.

Therefore

\[
\boxed{
\operatorname{col}\widehat G_M^{(r_0)}
=\operatorname{col}\Phi_X
}
\tag{1.1}
\]

for every positive integer `M`.

Thus all synchronized secant frames with the same base index `r0` occupy one fixed codimension-one polynomial-value subspace in `R^(n+1)`; the parameter `M` changes only the internal polynomial basis.

## 2. Exact left-null vector

Because the nodes `X_q` are equally spaced with step `1/m`, the `n`th finite-difference vector

\[
w_q=(-1)^q\binom nq
\]

annihilates every polynomial of degree `<n`.  Hence

\[
\boxed{
w^T\Phi_X=0,
\qquad
w^T\widehat G_M^{(r_0)}=0.
}
\tag{2.1}
\]

Since the frame has rank `n`, this spans its entire left kernel.

## 3. Fixed-J normalization and the moving hyperplane normal

The dual signed metric is

\[
\widehat D_r=J\Lambda_r,
\qquad
J=\operatorname{diag}((-1)^q),
\]

with

\[
\Lambda_r[q,q]
=\frac1m\binom nq\eta_{r,q}>0,
\]

\[
\eta_{r,q}
=\frac{n!}{\prod_{k=0}^{n}(r+\theta_q+k)}.
\]

Put

\[
Z_{M,r}=\Lambda_r^{1/2}\widehat G_M^{(r_0)}.
\]

Then

\[
S Q_{r_0,r}S=Z_{M,r}^TJZ_{M,r}.
\]

The Euclidean left normal of the fixed-`J` frame is therefore

\[
\boxed{
a_r=\Lambda_r^{-1/2}w,
\qquad
a_r^TZ_{M,r}=0.
}
\tag{3.1}
\]

In particular, after passing to a common alternating Krein metric `J`, the frame subspace depends only on the moment index `r`, while `M` still changes the chosen internal basis.

## 4. Closed all-m formula for the Krein type of the normal

We can evaluate the `J`-norm of `a_r` exactly:

\[
a_r^TJa_r
=\sum_{q=0}^{n}(-1)^q\frac{w_q^2}{\Lambda_r[q,q]}
=m\sum_{q=0}^{n}(-1)^q\binom nq\frac1{\eta_{r,q}}.
\tag{4.1}
\]

Now

\[
\frac1{\eta_{r,q}}
=\frac1{n!m^{n+1}}
\prod_{k=0}^{n}\bigl(q+1+m(r+k)\bigr).
\tag{4.2}
\]

The product in (4.2) is monic of degree `n+1` in `q`.  For a monic polynomial

\[
P(q)=q^{n+1}+c q^n+\cdots,
\]

one has

\[
\Delta^nP(0)=n!\left(\binom{n+1}{2}+c\right).
\]

Here

\[
c=\sum_{k=0}^{n}\bigl(1+m(r+k)\bigr).
\]

Substitution into (4.1) yields the closed formula

\[
\boxed{
a_r^TJa_r
=(-1)^n\,
\frac{mr+(m^2+1)/2}{m^{m-2}}.
}
\tag{4.3}
\]

It is never zero.  Consequently the codimension-one hyperplane `col Z_(M,r)` is a regular Krein subspace for every `m>=2`, `r>=0`, `M>0`; its complementary `J`-line has the fixed sign `(-1)^n`.

This is the residue-dual analogue of the linear finite-difference denominator that appeared earlier in the exact late-layer inverse formula.

## 5. Monotone row-scaling between two moment indices

For `s>r`,

\[
\frac{\eta_{s,q}}{\eta_{r,q}}
=\prod_{k=0}^{n}
\frac{r+\theta_q+k}{s+\theta_q+k}.
\tag{5.1}
\]

As a function of `theta>0`,

\[
\frac{d}{d\theta}\log
\prod_{k=0}^{n}\frac{r+\theta+k}{s+\theta+k}
=\sum_{k=0}^{n}
\left(\frac1{r+\theta+k}-\frac1{s+\theta+k}\right)>0.
\]

Therefore

\[
\boxed{
q\mapsto\frac{\eta_{s,q}}{\eta_{r,q}}
\text{ is strictly increasing.}
}
\tag{5.2}
\]

Hence the fixed-`J` frames at two moment levels differ, at the ambient-row level, by a positive **strictly monotone diagonal scaling**, in addition to the explicit internal secant basis change.

## 6. Boundary

Proved all-`m` here:

1. common codimension-one polynomial subspace before the row metric normalization;
2. exact barycentric left-null vector `w`;
3. fixed-`J` normal `a_r`;
4. closed nonzero Krein norm (4.3);
5. strict monotonicity of the positive row scaling (5.2).

Still open:

- a positive Lyapunov certificate for the separated pair;
- `M5_BLOCK_SEPARATED_MELLIN_EULER_PENCIL`;
- all-m three-support mixed sign regularity;
- HCM0.

The immediate structural target is now sharply finite-dimensional: combine

- a strictly-TP codimension-one frame,
- a regular alternating `J`-hyperplane with explicit normal,
- a strictly monotone positive row scaling as `r` increases,
- and the explicit TN internal secant-basis factor `C_M`,

to control the generalized `J`-Gram pencil in the separation range `M>=m`.
