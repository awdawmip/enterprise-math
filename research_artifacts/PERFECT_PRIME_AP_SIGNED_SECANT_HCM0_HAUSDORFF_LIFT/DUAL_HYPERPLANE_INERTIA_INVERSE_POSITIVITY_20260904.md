# Perfect Prime AP HCM0 — dual hyperplane inertia and inverse positivity

Task: `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT`  
Researcher: `EM-HCM0-HL-FB0860`  
Claim: `CLM-HCM0HL-6F8E2D4389B17C04A521`  
Date: 2026-09-04  
Status: **NONTERMINAL ALL-m STRUCTURAL THEOREM — HCM0 REMAINS OPEN**

This note continues from `RESIDUE_DUAL_STP_SECANT_FRAME_20260904.md` and `CODIM_ONE_DUAL_KREIN_NORMAL_20260904.md`.

## 1. Dual alternating metric and common hyperplane

Put `n=m-1`,

\[
\theta_q=\frac{q+1}{m},\qquad
\eta_{r,q}=\frac{n!}{\prod_{k=0}^{n}(r+\theta_q+k)}>0,
\]

and

\[
d_{r,q}=\frac1m(-1)^q\binom nq\eta_{r,q}.
\]

Let

\[
\widehat D_r=\operatorname{diag}(d_{r,0},\ldots,d_{r,n}),
\qquad
w_q=(-1)^q\binom nq.
\]

The residue-dual secant frames all span the same hyperplane

\[
\mathcal H=\ker w^T\subset\mathbb R^{n+1}.
\]

Eliminate the last coordinate using

\[
x_n=v^Tx,
\qquad
v_i=-\frac{w_i}{w_n}=(-1)^{n+i+1}\binom ni,
\qquad 0\le i<n.
\]

The restriction of `Dhat_r` to `H` in the first `n` coordinates is

\[
\boxed{
R_r=D'_r+d_{r,n}vv^T,
}
\tag{1.1}
\]

where

\[
D'_r=\operatorname{diag}(d_{r,0},\ldots,d_{r,n-1}).
\]

## 2. Exact scalar denominator

Define

\[
S_r=\sum_{q=0}^{n}(-1)^q\binom nq\frac1{\eta_{r,q}}.
\tag{2.1}
\]

Because

\[
\frac1{\eta_{r,q}}
=\frac1{n!m^{n+1}}
\prod_{k=0}^{n}\bigl(q+1+m(r+k)\bigr)
\]

is a monic degree-`n+1` polynomial in `q` up to the displayed positive scalar, its `n`th finite difference is linear.  The exact evaluation from the preceding codimension-one note gives

\[
\boxed{
S_r=(-1)^n\frac{mr+(m^2+1)/2}{m^{m-1}}.
}
\tag{2.2}
\]

In particular `S_r` is never zero and has sign `(-1)^n`.

## 3. Exact inverse formula

From (1.1),

\[
(D'_r)^{-1}v
=m(-1)^{n+1}
\left(\eta_{r,0}^{-1},\ldots,\eta_{r,n-1}^{-1}\right)^T.
\]

The Sherman-Morrison denominator is

\[
1+d_{r,n}v^T(D'_r)^{-1}v
=(-1)^n\eta_{r,n}S_r>0.
\]

Therefore, for `0<=i,j<n`,

\[
\boxed{
(R_r^{-1})_{ij}
=m\left[
\delta_{ij}\frac{(-1)^i}{\binom ni\eta_{r,i}}
-\frac1{S_r\eta_{r,i}\eta_{r,j}}
\right].
}
\tag{3.1}
\]

No determinant or matrix inversion remains after the scalar beta factors are known.

## 4. All-m inertia of the restricted form

The ambient diagonal form `Dhat_r` has

\[
\left(\left\lceil\frac m2\right\rceil,
      \left\lfloor\frac m2\right\rfloor\right)
\]

positive/negative inertia.

Its `Dhat_r`-orthogonal complement to `H` is spanned by

\[
\widehat D_r^{-1}w,
\]

whose squared `Dhat_r`-norm is

\[
w^T\widehat D_r^{-1}w=mS_r.
\]

By (2.2), this complementary line has sign `(-1)^n`.  Removing it from the ambient inertia gives

\[
\boxed{
\operatorname{inertia}(R_r)
=\left(
\left\lfloor\frac m2\right\rfloor,
\left\lfloor\frac{m-1}{2}\right\rfloor
\right)
}
\tag{4.1}
\]

for every `m>=2` and every `r>=0`.

Hence the restriction is nondegenerate for all parameters and its inertia is independent of the moment level.

## 5. Strict inverse positivity in the separated/late range

Off the diagonal, (2.2) and (3.1) immediately give

\[
(-1)^m(R_r^{-1})_{ij}>0,
\qquad i\ne j.
\tag{5.1}
\]

For a diagonal entry, if `(-1)^i=(-1)^m`, both terms already have the desired sign.  In the opposite-parity case it is enough to prove

\[
\frac{\binom ni}{\eta_{r,i}}> |S_r|.
\tag{5.2}
\]

Since `binom(n,i)>=1` and `theta_i>0`,

\[
\frac1{\eta_{r,i}}
=\frac1{(m-1)!}\prod_{k=0}^{m-1}(r+\theta_i+k)
>\frac{r^m}{(m-1)!}.
\]

For `r>=m`,

\[
\frac{r^m}{(m-1)!}
>\frac{mr+(m^2+1)/2}{m^{m-1}}
=|S_r|.
\tag{5.3}
\]

Indeed the difference after multiplication by `m^(m-1)` is increasing in `r>=m`, and at `r=m` it is already positive for `m=2`; the elementary ratio increases thereafter with `m`.

Thus:

### Theorem 5.1 — separated dual inverse positivity

For every `m>=2`, every `r>=m`, and all `0<=i,j<n`,

\[
\boxed{
(-1)^m(R_r^{-1})_{ij}>0.
}
\tag{5.4}
\]

This is an all-`m` theorem.  In particular it applies to every later moment level in an actual Perfect-Prime triple, because the first positive actual gap is `m`.

## 6. Relation to the earlier late-layer inverse theorem

The preceding Pascal/Hausdorff route proved an entrywise inverse-positivity statement after a different fixed congruence in the original integer-node coordinates.  The present theorem is not used as a replacement for that result.  It is the residue-dual, codimension-one version:

- the common hyperplane is explicit (`ker w^T`);
- the ambient alternating metric is diagonal;
- the rank-one correction and denominator are explicit beta quantities;
- the inertia follows immediately from the sign of the complementary line.

The coincidence of the same linear finite-difference scalar is a structural cross-check between the two normal forms.

## 7. Boundary

Proved all-`m` here:

1. rank-one restriction normal form (1.1);
2. exact inverse formula (3.1);
3. fixed inertia (4.1) for all `r>=0`;
4. entrywise strict inverse positivity (5.4) for all `r>=m`.

Not proved:

- positivity of the mixed trace `tr(B^{-1}A)`;
- positive stability of a separated pair;
- `M5_BLOCK_SEPARATED_MELLIN_EULER_PENCIL`;
- all-m three-support sign regularity;
- HCM0.

The next target is to combine (5.4) with the explicit secant basis transition in the coefficient of `t^(n-1)`, which is

\[
[t^{n-1}]\det(A+tB)=\det(B)\,\operatorname{tr}(B^{-1}A).
\]
