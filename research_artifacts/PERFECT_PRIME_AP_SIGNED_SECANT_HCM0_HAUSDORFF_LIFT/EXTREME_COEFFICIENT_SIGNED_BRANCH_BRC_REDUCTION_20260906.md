# Perfect Prime AP HCM0 — extreme mixed coefficient signed-branch / BRC reduction

Task: `RS-PERFECT-PRIME-AP-SIGNED-SECANT-HCM0-HAUSDORFF-LIFT`  
Publication: `TP2-7A2D91C5E40B836F19D2`  
Researcher: `EM-HCM0-HL-FB0860`  
Recovery claim: `CLM-HCM0HL-RECOVER-20260906T2125`  
Date: 2026-09-06  
Status: **ALL-m EXACT STRUCTURAL REDUCTION — SIGN COMPARISON REMAINS OPEN**

## 1. Frozen normalized dual forms

Put `n=m-1`. For a fixed initial moment level `r0` and synchronized endpoint `r=r0+M`, the residue-dual checkpoint gives the secant frame

\[
\widehat G_M[q,a]
=h_{M,a}^{(r_0)}(\theta_q),
\qquad
\theta_q=\frac{q+1}{m},
\quad 0\le q\le n,\ 1\le a\le n,
\]

and the alternating diagonal metric

\[
\widehat D_r[q,q]=d_{r,q}
=\frac1m(-1)^q\binom nq\eta_{r,q},
\qquad
\eta_{r,q}=B(r+\theta_q,n+1)>0.
\]

Remove the strictly positive gap square by defining

\[
\overline G_M:=M^{-1}\widehat G_M.
\]

Up to the fixed sign-diagonal congruence already frozen in the residue-dual theorem, the normalized quotient form is

\[
\mathcal A_M=\overline G_M^T\widehat D_r\overline G_M.
\tag{1.1}
\]

For two synchronized endpoints

\[
r=r_0+M,\qquad s=r_0+N,\qquad 0<M<N,
\]
write

\[
A=\mathcal A_M,
\qquad
B=\mathcal A_N.
\]

For actual Perfect-Prime layers,

\[
r_0=mS,\qquad M=ma,\qquad N=m(a+c),
\qquad S\ge0,\ a,c>0.
\]

## 2. All coefficients: exact signed branch expansion

Stack the two frames vertically:

\[
Z=\begin{bmatrix}\overline G_M\\ \overline G_N\end{bmatrix},
\qquad
\mathcal D(t)=\operatorname{diag}(\widehat D_r,t\widehat D_s).
\]

Then

\[
A+tB=Z^T\mathcal D(t)Z.
\]

Cauchy-Binet therefore gives, for every `0<=k<=n`,

\[
\boxed{
[t^k]\det(A+tB)
=
\sum_{\substack{I,J\subset\{0,\ldots,n\}\\|I|=n-k,\ |J|=k}}
\det\!\begin{bmatrix}
\overline G_M[I,:]\\
\overline G_N[J,:]
\end{bmatrix}^{\!2}
\left(\prod_{i\in I}d_{r,i}\right)
\left(\prod_{j\in J}d_{s,j}\right).
}
\tag{2.1}
\]

This is an exact branch decomposition. Every determinant-square factor is nonnegative. The only sign carried by a branch is the explicit parity

\[
(-1)^{\sum_{i\in I}i+\sum_{j\in J}j}.
\tag{2.2}
\]

Thus no hidden matrix-inversion sign remains.

## 3. BRC semantics of (2.1)

Equation (2.1) is the first point in this route where a BRC-style branch carrier is mathematically faithful.

A branch is typed by

\[
(M,N;I,J)
\]

and retains:

- endpoint provenance (`M` or `N`);
- exact row labels;
- the explicit parity/sign class;
- the positive beta/binomial magnitude;
- the nonnegative squared mixed-minor amplitude.

Because the final coefficient is signed, standard positive Weighted-BRC **cannot** replace (2.1) by one total mass. The Foundation `SIGNED_BOUNDARY` remains active. A valid use is to keep two exact populations

\[
W_+=\sum_{\text{even branches}}|w_b|,
\qquad
W_-=\sum_{\text{odd branches}}|w_b|
\]

and prove the required oriented inequality between them. This preserves the cancellation-bearing fibers rather than projecting them away.

## 4. Universal maximal-minor rigidity of the normalized secant frame

Recall the factorization from the strict-TP checkpoint:

\[
\widehat G_M=\Phi_X C_M,
\]

where

\[
\Phi_X[q,k]=\phi_k(X_q),
\qquad
\phi_k(x)=\binom{x+k-1}{k},
\qquad
X_q=r_0+\frac{q+1}{m},
\]

and

\[
C_M[k,a]=\phi_{a-k}(M)\quad(k<a).
\]

After dividing by `M`,

\[
\overline C_M:=M^{-1}C_M
\]

is unit upper triangular because its diagonal entries are `phi_1(M)/M=1`. Hence

\[
\det\overline C_M=1.
\tag{4.1}
\]

All columns of `Phi_X` and of every `Gbar_M` lie in the same hyperplane

\[
\ker w^T,
\qquad
w_q=(-1)^q\binom nq.
\]

The signed maximal-cofactor vector must therefore be proportional to `w`. Strict total positivity fixes the positive orientation. For the minor omitting the last row, the rising-factorial Vandermonde gives

\[
\det\Phi_X[0{:}n,:]
=\frac{\prod_{0\le i<j<n}(X_j-X_i)}{\prod_{k=0}^{n-1}k!}
=m^{-n(n-1)/2}.
\]

Consequently, for every `M>0`, every `r0>=0`, and every `q`,

\[
\boxed{
\det\overline G_M[\widehat q,:]
=m^{-n(n-1)/2}\binom nq.
}
\tag{4.2}
\]

This is independent of both the gap and the initial layer.

Equation (4.2) explains at branch level why the normalized pure-endpoint determinant depends only on the terminal metric level.

## 5. Re-derivation of the endpoint determinant without matrix inversion

Let

\[
\kappa_m=m^{-n(n-1)/2},
\qquad
D_s^{\mathrm{all}}=\prod_{q=0}^{n}d_{s,q},
\]

and define

\[
S_s=\sum_{q=0}^{n}(-1)^q\binom nq\eta_{s,q}^{-1}.
\]

Using (4.2) in the `k=n` Cauchy-Binet sum,

\[
\boxed{
\det B
=\kappa_m^2\,m\,D_s^{\mathrm{all}}\,S_s.
}
\tag{5.1}
\]

The earlier codimension-one theorem gives

\[
S_s=(-1)^n\frac{ms+(m^2+1)/2}{m^{m-1}},
\]

so (5.1) reproduces the known strict endpoint determinant sign and nonvanishing.

## 6. First dangerous coefficient: exact three-index alternating-square formula

For `k=n-1`, the `M`-side row set is a singleton `{i}` and the `N`-side row set has size `n-1`. Write the latter as

\[
J_{p,q}=\{0,\ldots,n\}\setminus\{p,q\},
\qquad 0\le p<q\le n.
\]

Define the normalized mixed-minor amplitude

\[
\rho_{i;pq}
:=\kappa_m^{-1}
\det\!\begin{bmatrix}
\overline G_M[i,:]\\
\overline G_N[J_{p,q},:]
\end{bmatrix},
\tag{6.1}
\]

with any fixed consistent row ordering; only `rho^2` is used below.

Equation (2.1), divided by (5.1), yields the exact inverse-free trace formula

\[
\boxed{
\operatorname{tr}(B^{-1}A)
=
\frac1{S_s}
\sum_{i=0}^{n}
\sum_{0\le p<q\le n}
(-1)^{i+p+q}
\frac{\binom ni\,\eta_{r,i}}
{\binom np\binom nq\,\eta_{s,p}\eta_{s,q}}
\rho_{i;pq}^{\,2}.
}
\tag{6.2}
\]

All factors other than the displayed parity and `S_s` have positive magnitude. Thus the M6 target has been reduced to an explicit labeled three-index signed-mass comparison with no determinant inverse.

At coalescence `M=N`, the formula collapses to `tr(I)=n`, providing an exact regression boundary.

## 7. Branch amplitudes have an exact Vandermonde integral

The normalized secant row has the derivative-average form

\[
\overline g_M(x)_a
=\frac{\phi_a(x+M)-\phi_a(x)}{M}
=\int_0^1\phi_a'(x+tM)\,dt.
\tag{7.1}
\]

For any `n` selected rows with base positions `x_1,...,x_n` and row-specific positive gaps `M_1,...,M_n`, row multilinearity gives

\[
\det[\overline g_{M_\ell}(x_\ell)_a]_{\ell,a=1}^{n}
=
\int_{[0,1]^n}
\det[\phi_a'(x_\ell+t_\ell M_\ell)]_{\ell,a=1}^{n}
\,dt.
\]

Since `phi_a'` has degree `a-1` and leading coefficient `1/(a-1)!`, the inner determinant is exactly a Vandermonde. Therefore

\[
\boxed{
\det[\overline g_{M_\ell}(x_\ell)_a]
=
\frac1{\prod_{k=0}^{n-1}k!}
\int_{[0,1]^n}
\prod_{1\le u<v\le n}
\bigl[(x_v+t_vM_v)-(x_u+t_uM_u)\bigr]
\,dt.
}
\tag{7.2}
\]

For the extreme branch `rho_(i;pq)`, exactly one row uses gap `M` and the remaining `n-1` rows use gap `N`; all base positions are the explicit fractional grid

\[
x_q=r_0+\frac{q+1}{m}.
\]

Thus every branch amplitude in (6.2) is an explicit squared polynomial/Vandermonde integral, not an opaque matrix minor.

## 8. Consequences and next exact target

Proved all `m` here:

1. the full signed branch expansion (2.1) for every mixed coefficient;
2. the exact BRC-safe positive/negative branch carrier;
3. gap- and layer-independent maximal-minor law (4.2);
4. inverse-free endpoint determinant formula (5.1);
5. the three-index alternating-square trace reduction (6.2);
6. the derivative-Vandermonde integral for every branch amplitude (7.2).

This does **not** yet prove the sign of (6.2). In particular, the positive and negative parity branch populations are both nonempty, so a termwise positivity claim would be false.

The next minimal theorem is now sharper than the matrix-level M6 statement:

`M7_EXTREME_BRANCH_PARITY_DOMINATION`:

> For actual synchronized gaps `M=ma`, `N=m(a+c)`, prove that the oriented positive-parity mass in (6.2) strictly dominates the negative-parity mass by at least the coalescent baseline corresponding to `n`, using the beta-weight ratios and the explicit Vandermonde-integral amplitudes.

A proof of M7 is exactly the desired all-m M6 trace theorem, but on a provenance-preserving branch space suitable for BRC pairing or finite-difference summation.