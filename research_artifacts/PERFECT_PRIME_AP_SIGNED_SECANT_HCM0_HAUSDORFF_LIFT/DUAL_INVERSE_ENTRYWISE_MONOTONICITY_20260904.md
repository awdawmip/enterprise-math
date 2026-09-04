# Perfect Prime AP HCM0 — separated dual inverse entrywise monotonicity

Task: `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT`  
Publication: `TP2-7A2D91C5E40B836F19D2`  
Researcher: `EM-HCM0-HL-FB0860`  
Recovery claim: `CLM-HCM0HL-RECOVER-20260904T205700`  
Date: 2026-09-04  
Status: **NONTERMINAL ALL-m STRUCTURAL THEOREM — HCM0 REMAINS OPEN**

This note continues from `DUAL_HYPERPLANE_INERTIA_INVERSE_POSITIVITY_20260904.md` and proves a new monotonicity property of the same explicit inverse.

## 1. Frozen inverse formula

Put `n=m-1`,

\[
\theta_i=\frac{i+1}{m},\qquad
F_i(r)=\eta_{r,i}^{-1}
=\frac1{(m-1)!}\prod_{k=0}^{m-1}(r+\theta_i+k),
\]

and

\[
\sigma(r)=\frac{mr+(m^2+1)/2}{m^{m-1}}>0.
\]

The preceding codimension-one theorem gives

\[
S_r=(-1)^n\sigma(r)
\]

and, for `0<=i,j<n`,

\[
(R_r^{-1})_{ij}
=m\left[
\delta_{ij}\frac{(-1)^iF_i(r)}{\binom ni}
-\frac{F_i(r)F_j(r)}{S_r}
\right].
\]

Define

\[
P_r:=(-1)^mR_r^{-1}=(-1)^{n+1}R_r^{-1}.
\]

Then

\[
(P_r)_{ij}=m\frac{F_i(r)F_j(r)}{\sigma(r)},\qquad i\ne j,
\tag{1.1}
\]

and

\[
(P_r)_{ii}
=m\left[
\frac{F_i(r)^2}{\sigma(r)}
+\varepsilon_i\frac{F_i(r)}{\binom ni}
\right],
\qquad
\varepsilon_i=(-1)^{m+i}.
\tag{1.2}
\]

The earlier theorem already proves `P_r` entrywise strictly positive for `r>=m`.

## 2. A logarithmic derivative inequality

Write

\[
L_i(r)=\frac{F_i'(r)}{F_i(r)}
=\sum_{k=0}^{m-1}\frac1{r+\theta_i+k}
\]

and

\[
s(r)=\frac{\sigma'(r)}{\sigma(r)}
=\frac1{r+(m^2+1)/(2m)}.
\]

### Lemma 2.1

For every `m>=2`, `r>=0`, and `0<=i<n`,

\[
\boxed{L_i(r)>s(r).}
\tag{2.1}
\]

### Proof

Since `theta_i<=n/m=(m-1)/m<1`,

\[
r+\theta_i<r+\frac{m^2+1}{2m}
\]

for every `m>=2`.  Hence the first positive summand in `L_i(r)` already satisfies

\[
\frac1{r+\theta_i}>s(r),
\]

and all remaining summands are positive. ∎

## 3. Off-diagonal monotonicity

From (1.1),

\[
\frac{d}{dr}\log (P_r)_{ij}
=L_i(r)+L_j(r)-s(r)>0
\]

by Lemma 2.1. Therefore every off-diagonal entry is strictly increasing for all `r>=0`.

## 4. Diagonal monotonicity in the separated range

If `epsilon_i=+1`, both terms in (1.2) are positive increasing products, and explicitly

\[
\frac{d}{dr}(P_r)_{ii}
=mF_i\left[
\frac{F_i}{\sigma}(2L_i-s)
+\frac{L_i}{\binom ni}
\right]>0.
\]

Now let `epsilon_i=-1`.  The derivative is

\[
\frac1{mF_i}\frac{d}{dr}(P_r)_{ii}
=
\frac{F_i}{\sigma}(2L_i-s)
-\frac{L_i}{\binom ni}.
\tag{4.1}
\]

For `r>=m`, the preceding inverse-positivity theorem proved the strict scalar domination

\[
\boxed{\binom ni F_i(r)>\sigma(r).}
\tag{4.2}
\]

Also Lemma 2.1 gives

\[
2L_i-s>L_i.
\]

Consequently

\[
\frac{F_i}{\sigma}(2L_i-s)
>
\frac1{\binom ni}L_i,
\]

so the right side of (4.1) is strictly positive.

Thus every diagonal entry is strictly increasing once `r>=m`.

## 5. Theorem

### Theorem 5.1 — separated dual inverse monotonicity

For every `m>=2` and every pair

\[
r_2>r_1\ge m,
\]

one has entrywise strict inequalities

\[
\boxed{
(-1)^mR_{r_2}^{-1}-(-1)^mR_{r_1}^{-1}>0
\quad\text{entrywise}.
}
\tag{5.1}
\]

Equivalently, every entry of `P_r=(-1)^mR_r^{-1}` is a strictly increasing positive function on `[m,infinity)`.

No spectral or determinant computation is used.

## 6. Relevance and boundary

For an actual Perfect-Prime three-layer configuration, every noninitial endpoint moment level lies in the separated range because the first actual positive moment-index gap is exactly `m`.  Thus the later dual restricted inverse is entrywise larger after the global sign normalization.

This theorem does **not** by itself prove the mixed trace

\[
\operatorname{tr}(Q_{s_0,s_0+a+c}^{-1}Q_{s_0,s_0+a})>0,
\]

because the secant-basis transition has genuine sign cancellations.  In particular, previous exact stress tests ruled out replacing that transition by a totally nonnegative or Pólya-frequency matrix.

The next target remains `M6_ACTUAL_TWO_BLOCK_NEWTON_TRACE_POSITIVITY`.  The new usable input is that all cancellation now lies in the normalized secant transition; the separated metric-inverse motion itself is strictly positive entrywise.

No Result-ID is frozen; HCM0 and parent determinant nonvanishing remain open.
