# Perfect Prime AP HCM0 — late-layer rank-one inverse positivity

Task: `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT`  
Publication: `TP2-7A2D91C5E40B836F19D2`  
Researcher: `EM-HCM0-HL-FB0860`  
Claim: `CLM-HCM0HL-6F8E2D4389B17C04A521`  
Date: 2026-09-04  
Status: **NONTERMINAL ALL-m STRUCTURAL THEOREM — HCM0 REMAINS OPEN**

## 1. Setup

Put `n=m-1` and

\[
\mu_r=\frac{n!}{\prod_{a=1}^{m}(mr+a)},
\qquad
F(r)=\mu_r^{-1}.
\]

Let `P_<` be the `n x n` lower Pascal matrix on rows/columns `0,...,n-1`, and let the last row of the full `(n+1)x(n+1)` Pascal matrix be

\[
v=(\binom n0,\binom n1,\ldots,\binom n{n-1})^T.
\]

For a moment-index offset `r`, the leading `n x n` Hausdorff/Pascal form from the preceding checkpoint is

\[
H_r=P_<^T D'_rP_<+d_{n,r}vv^T,
\]

where

\[
D'_r=\operatorname{diag}\left((-1)^i\binom ni\mu_{r+i}\right)_{i=0}^{n-1},
\qquad
 d_{n,r}=(-1)^n\mu_{r+n}.
\]

Since `P_<` is invertible, put

\[
K_r=P_<^{-T}H_rP_<^{-1}.
\]

The fixed transformed last-row vector is

\[
\zeta=P_<^{-T}v,
\qquad
\boxed{\zeta_i=(-1)^{n-1-i}\binom ni.}
\tag{1.1}
\]

Hence

\[
\boxed{K_r=D'_r+d_{n,r}\zeta\zeta^T.}
\tag{1.2}
\]

## 2. Exact inverse formula

Set

\[
S_r=\sum_{i=0}^{n}(-1)^i\binom niF(r+i)
=(-1)^n\Delta^nF(r).
\tag{2.1}
\]

Because

\[
(D'_r)^{-1}\zeta
=(-1)^{n-1}(F(r),F(r+1),\ldots,F(r+n-1))^T,
\]

the Sherman–Morrison denominator is

\[
1+d_{n,r}\zeta^T(D'_r)^{-1}\zeta
=(-1)^n\mu_{r+n}S_r
=\mu_{r+n}\Delta^nF(r)>0.
\tag{2.2}
\]

Moreover `d_{n,r}` divided by (2.2) is exactly `1/S_r`. Therefore

\[
\boxed{
(K_r^{-1})_{ij}
=\delta_{ij}\frac{(-1)^iF(r+i)}{\binom ni}
-\frac{F(r+i)F(r+j)}{S_r},
\qquad 0\le i,j<n.
}
\tag{2.3}
\]

This formula contains no determinant or matrix inversion after the scalar sequence `F` is known.

## 3. The n-th finite difference is explicit

Since

\[
F(r)=\frac1{(m-1)!}\prod_{a=1}^{m}(mr+a)
\]

is a degree-`m=n+1` polynomial, its `n`-th forward difference is linear. Direct comparison of the two leading coefficients, or the standard identities for `Delta^n r^{n+1}` and `Delta^n r^n`, gives

\[
\boxed{
\Delta^nF(r)
=m^m\left(mr+\frac{m^2+1}{2}\right)>0.
}
\tag{3.1}
\]

Consequently

\[
\operatorname{sgn}S_r=(-1)^n.
\tag{3.2}
\]

## 4. Actual late-layer inverse positivity

For an actual layer `s>=1`, the offset is

\[
r=ms\ge m.
\]

### Lemma 4.1

For every `m>=2` and `r>=m`,

\[
F(r)>\Delta^nF(r).
\tag{4.1}
\]

### Proof

For `m>=4`,

\[
F(r)>\frac{(mr)^m}{(m-1)!}
=m^m\frac{r^m}{(m-1)!}.
\]

The ratio

\[
\frac{r^m}{mr+(m^2+1)/2}
\]

is strictly increasing for `r>0`. At `r=m`,

\[
\frac{m^m}{(m-1)!}>\frac{3m^2+1}{2}
\]

holds at `m=4` and then by an elementary induction in `m` (the left side grows by a factor `((m+1)/m)^{m+1}`, which dominates the corresponding quadratic ratio). Thus (4.1) holds for `m>=4`.

For `m=2,3`, substituting the explicit quadratic/cubic polynomials gives (4.1) directly for `r>=m`. ∎

Since `F` is increasing and `binom(n,i)>=1`, (4.1) implies

\[
\binom niF(r+i)>\Delta^nF(r)
\qquad(0\le i<n).
\tag{4.2}
\]

Now use (2.3). Off the diagonal, (3.2) gives immediately

\[
(-1)^{n+1}(K_r^{-1})_{ij}>0.
\]

On the diagonal, after multiplying by `(-1)^{n+1}`, either the first term already has positive sign or the only required comparison is exactly (4.2). Hence:

### Theorem 4.2 — late-layer inverse positivity

For every `m>=2`, every actual layer `s>=1`, and all `0<=i,j<n`,

\[
\boxed{
(-1)^{n+1}(K_{ms}^{-1})_{ij}>0.
}
\tag{4.3}
\]

Equivalently, because `n+1=m`,

\[
\boxed{(-1)^mK_{ms}^{-1}\text{ is entrywise strictly positive}.}
\]

This is an all-`m` theorem, not finite discovery.

## 5. Relevance and limit

The theorem applies precisely to non-initial actual layers appearing as the later layer in

\[
Q_{c_{s_e},c_{s_d}},\qquad s_d>s_e,
\]

because then `s_d>=1`.

Together with the earlier exact facts

- `T_{m(s_d-s_e)}` is totally nonnegative;
- `mu` is a strict Hausdorff moment sequence;
- the pointwise Pascal kernel has explicit alternating LDL;

(4.3) gives a new inverse-positive component for the actual quotient forms.

However entrywise inverse positivity alone does **not** imply that every mixed determinant of two or more quotient forms has the required sign. No such inference is made here. The remaining target is still the signed Pascal/Hausdorff mixed-discriminant regrouping.

No Result-ID is frozen; HCM0 and parent determinant nonvanishing remain open.
