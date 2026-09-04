# Perfect Prime AP HCM0 — normalized endpoint determinant monotonicity

Task: `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT`  
Publication: `TP2-7A2D91C5E40B836F19D2`  
Researcher: `EM-HCM0-HL-FB0860`  
Recovery claim: `CLM-HCM0HL-RECOVER-20260904T205700`  
Date: 2026-09-04  
Status: **NONTERMINAL ALL-m STRUCTURAL THEOREM — HCM0 REMAINS OPEN**

## 1. Setup

Put `n=m-1` and

\[
F(r)=\mu_r^{-1}
=\frac1{(m-1)!}\prod_{a=1}^{m}(mr+a).
\]

The accepted Pascal/Hausdorff quotient form is

\[
Q_{r_0,r}=T_M^TH_rT_M,
\qquad M=r-r_0>0,
\]

where `T_M` is triangular with every diagonal entry equal to `M`.  Define the scalar-normalized form

\[
\mathcal H_{r_0,r}:=M^{-2}Q_{r_0,r}.
\tag{1.1}
\]

Then

\[
\det(M^{-1}T_M)=1,
\]

hence

\[
\boxed{\det\mathcal H_{r_0,r}=\det H_r.}
\tag{1.2}
\]

Thus the determinant of the normalized quotient form depends only on the terminal moment level `r`, not separately on the initial level `r0` or the gap `M`.

## 2. Closed determinant formula

From the already proved rank-one normal form

\[
K_r=P_<^{-T}H_rP_<^{-1}
=D'_r+d_{n,r}\zeta\zeta^T,
\]

with unit-triangular `P_<`, one has `det H_r=det K_r`.  The matrix determinant lemma and the frozen Sherman-Morrison denominator give

\[
\det K_r
=\det D'_r\,\mu_{r+n}\Delta^nF(r).
\]

Since

\[
D'_r[i,i]=(-1)^i\binom ni\mu_{r+i},
\]

we obtain

\[
\boxed{
\det H_r
=(-1)^{n(n-1)/2}
\left(\prod_{i=0}^{n-1}\binom ni\right)
\left(\prod_{i=0}^{n}\mu_{r+i}\right)
\Delta^nF(r).
}
\tag{2.1}
\]

Using `mu=1/F`,

\[
\boxed{
|\det H_r|
=C_m\,
\frac{\Delta^nF(r)}{\prod_{i=0}^{n}F(r+i)},
\qquad
C_m=\prod_{i=0}^{n-1}\binom ni>0.
}
\tag{2.2}
\]

The previously proved finite-difference identity is

\[
\Delta^nF(r)
=m^m\left(mr+\frac{m^2+1}{2}\right).
\tag{2.3}
\]

## 3. Strict monotonicity

Let

\[
L_i(r)=\frac{F'(r+i)}{F(r+i)}
=\sum_{k=0}^{m-1}\frac1{r+i+(k+1)/m}.
\]

From (2.3),

\[
\frac{(\Delta^nF)'(r)}{\Delta^nF(r)}
=\frac1{r+(m^2+1)/(2m)}.
\tag{3.1}
\]

But already the first summand of `L_0(r)` satisfies

\[
\frac1{r+1/m}
>
\frac1{r+(m^2+1)/(2m)},
\]

and all other `L_i` terms are positive.  Therefore

\[
\sum_{i=0}^{n}L_i(r)
>
\frac{(\Delta^nF)'(r)}{\Delta^nF(r)}.
\]

Taking the logarithmic derivative of (2.2) gives

\[
\boxed{
\frac{d}{dr}\log|\det H_r|<0
\qquad(r\ge0).
}
\tag{3.2}
\]

Hence `|det H_r|` is strictly decreasing on the entire nonnegative parameter range.

## 4. Consequence for every normalized pair

For `r<s`, equations (1.2) and (3.2) imply

\[
\boxed{
\frac{|\det\mathcal H_{r_0,r}|}
{|\det\mathcal H_{r_0,s}|}>1.
}
\tag{4.1}
\]

Equivalently, for the relative operator

\[
C_{r,s}=\mathcal H_{r_0,s}^{-1}\mathcal H_{r_0,r},
\]

whose determinant is positive because both forms have the same frozen inertia,

\[
\boxed{\det C_{r,s}>1.}
\tag{4.2}
\]

For an actual triple with block lengths `a>0,c>0`, this applies to

\[
r=m(s_0+a),\qquad s=m(s_0+a+c).
\]

## 5. Tangent at coalescence

Fix an earlier normalized form and allow the later terminal level to vary continuously.  At coalescence the relative operator is the identity, so

\[
\operatorname{tr}C_{r,r}=n.
\]

Jacobi's formula gives

\[
-\frac{d}{ds}\log|\det\mathcal H_{r_0,s}|\bigg|_{s=r}>0.
\]

Equivalently, the one-sided first variation of the relative trace away from the coalesced endpoint has the correct positive direction.  This is a local all-m statement; no global trace monotonicity is asserted.

## 6. Boundary

Proved all-`m` here:

1. gap-normalized determinant depends only on terminal level;
2. closed determinant formula (2.1)-(2.2);
3. strict decrease of its magnitude for every `r>=0`;
4. every later/earlier normalized relative determinant is strictly greater than `1`.

This does **not** imply

\[
\operatorname{tr}(C_{r,s})>n
\]

without an additional spectral or coefficient argument: actual quotient pencils can have nonreal generalized eigenvalues.  The result therefore supplies determinant control and the correct coalescence tangent, while `M6_ACTUAL_TWO_BLOCK_NEWTON_TRACE_POSITIVITY` remains open.

No Result-ID is frozen; HCM0 and parent determinant nonvanishing remain open.
