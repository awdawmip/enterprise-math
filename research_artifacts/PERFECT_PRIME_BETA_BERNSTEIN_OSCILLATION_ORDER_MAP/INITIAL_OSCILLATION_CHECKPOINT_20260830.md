# Perfect Prime Beta–Bernstein oscillation lane — initial checkpoint

Task: `RS-PERFECT-PRIME-BETA-BERNSTEIN-OSCILLATION-ORDER-MAP`  
Publication: `TP2-2B3DC53DD4066F464AE9`  
Researcher: `EM-PPTBBOSC-ACA29A`  
Claim: `chatgpt-pptbbosc-20260830-1111-aca29a`

This is an execution checkpoint, not a terminal Result.

## 1. Exact raw common-measure matrices

Write `n=m-1` and retain the accepted AP Beta measure factor

\[
\mu_m(du)=\kappa_m(1-u^{m^2})^n\,du.
\]

From the frozen parent formulas define the unnormalised Bernstein moment matrices

\[
M^A=E\widehat A,\qquad M^B=D\widehat B.
\]

Their entries are

\[
M^A_{ik}=\binom nk\int_0^1u^{i+mk}(1-u^m)^{n-k}\,\mu_m(du),
\]

\[
M^B_{jk}=\binom nk\int_0^1u^{mj+k}(1-u)^{n-k}\,\mu_m(du).
\]

(The common positive factor `kappa_m` is already absorbed into `mu_m`.)

Let

\[
R_{ri}=(-1)^i\binom ri\qquad(i\le r).
\]

Then binomial summation gives the exact order-map identities

\[
(RM^A)_{rk}
=\binom nk\int_0^1(1-u)^r u^{mk}(1-u^m)^{n-k}\,\mu_m(du),
\]

\[
(RM^B)_{rk}
=\binom nk\int_0^1(1-u^m)^r u^k(1-u)^{n-k}\,\mu_m(du).
\]

Thus the `u -> u^m` relation converts the two left Möbius/binomial differences into the paired decreasing coordinates `(1-u)^r` and `(1-u^m)^r`.

## 2. New all-m theorem: strict sign regularity before row normalisation

For either raw transformed matrix `N^A=RM^A` or `N^B=RM^B`, every `q x q` minor has the strict sign

\[
\epsilon_q=(-1)^{q(q-1)/2}.
\]

### Proof

Take increasing row indices `r_1<...<r_q` and column indices `k_1<...<k_q`. Andreief reduces the minor of `N^A` to an integral over
`0<u_1<...<u_q<1` of the product of two determinants.

The row determinant is

\[
\det[(1-u_s)^{r_a}]_{a,s}.
\]

Since `1-u_1>...>1-u_q>0`, reversing the sample order converts it to a generalized Vandermonde; hence its sign is exactly `epsilon_q`.

The column determinant is, after factoring positive row and column factors,

\[
\det[t_s^{k_b}]_{s,b},\qquad
 t_s=\frac{u_s^m}{1-u_s^m},
\]

and is strictly positive because `t_1<...<t_q`.
All remaining factors in the Andreief integrand are positive on a set of positive measure. Hence the minor is nonzero with sign `epsilon_q`.

For `N^B` the same argument uses the decreasing row coordinate `1-u^m` and the increasing Bernstein odds coordinate

\[
\frac{u}{1-u}.
\]

Therefore both raw matrices are strictly sign regular with the same signature. Equivalently, reversing their row order makes each one strictly totally positive.

This theorem is genuinely stronger than entrywise positivity and directly uses the special common-measure order map. It is not a generic consequence for two arbitrary STP matrices.

## 3. Exact location of the remaining oscillation difficulty

The accepted half maps are row-normalised:

\[
\widehat A=E^{-1}M^A,\qquad \widehat B=D^{-1}M^B.
\]

Using `R^2=I`,

\[
R\widehat A=(RE^{-1}R)(RM^A),
\qquad
R\widehat B=(RD^{-1}R)(RM^B).
\]

So the raw order-map part is already strictly sign regular. The remaining loss of a direct oscillatory factorisation occurs entirely in the conjugated reciprocal-normaliser matrices.

If `s_j=e_j^{-1}` and `t_j=d_j^{-1}`, then for `i>=j`

\[
(RE^{-1}R)_{ij}
=\binom ij(-1)^{i-j}\Delta^{i-j}s_j,
\]

\[
(RD^{-1}R)_{ij}
=\binom ij(-1)^{i-j}\Delta^{i-j}t_j.
\]

Thus the normalization subproblem is now explicit: classify exactly the finite-difference geometry of the reciprocal AP normalisers, and determine which sign/variation property survives multiplication by the two raw SSR kernels.

## 4. First normalized oscillation sign is all-m and strict

For `k>0`, define

\[
f_k(u)=\binom nk\left(\frac{u^m}{1-u^m}\right)^k.
\]

Under the probability measure proportional to

\[
(1-u^m)^n\mu_m(du),
\]

we have

\[
\widehat A_{ik}
=\frac{\mathbb E[U^i f_k(U)]}{\mathbb E[U^i]}.
\]

Since `U` and `f_k(U)` are strictly increasing on `(0,1)`, strict Chebyshev covariance gives

\[
\widehat A_{1k}>\widehat A_{0k},
\]

hence

\[
(R\widehat A)_{1k}=\widehat A_{0k}-\widehat A_{1k}<0.
\]

Likewise, with

\[
g_k(u)=\binom nk\left(\frac{u}{1-u}\right)^k
\]

and the base measure proportional to `(1-u)^n mu_m(du)`, the row tilt is by `U^{mj}`. Therefore

\[
(R\widehat B)_{1k}=\widehat B_{0k}-\widehat B_{1k}<0
\]

for every `m>=2` and `k>0`.

So first-order sign transport is not the obstruction.

## 5. Exact negative control: naive all-order complete monotonicity fails in the actual AP model

A tempting continuation would assert that every higher normalized binomial difference keeps a fixed alternating sign. That is false for the actual AP matrices, not merely for an abstract STP countermodel.

The exact checker finds already at `m=5`

\[
(R\widehat A)_{3,1}>0,
\qquad
(R\widehat B)_{3,1}>0.
\]

For comparison, at `m=4` the same two entries are negative. Thus there is a genuine sign transition; one cannot close the quotient theorem by declaring the normalized Bernstein-moment rows to be completely monotone or by treating `R E^{-1}` / `R D^{-1}` as if row normalisation commuted with raw binomial differencing.

The checker records the exact rational witnesses and verifies the raw strict-sign-regular signature through the configured finite range. The finite checks are regression only; the raw SSR theorem above is analytic for all `m`.

## 6. Next attack

The next load-bearing question is narrower than the original quotient determinant:

> Determine the weakest exact finite-difference property of `1/e_i` and `1/d_j` which, when composed with the two proven raw SSR kernels, forces the quotient product
> `Q_m = (R Bhat)_{1:,1:}(R Ahat)_{1:,1:}` to have no fixed vector at eigenvalue `1`.

Two immediate subtests are authorized inside this lane:

1. classify the checkerboard-conjugated lower-triangular matrices
   `J R E^{-1} R J` and `J R D^{-1} R J` (`J_ii=(-1)^i`) via exact minors / finite differences;
2. seek a Sturm/variation index for the *pair* of normalized half maps rather than demanding complete monotonicity of either half map separately.

No generic STP, entrywise Perron, ordinary norm contraction, finite-m-as-proof, or previously falsified full-sign-regular shortcut is reopened.
