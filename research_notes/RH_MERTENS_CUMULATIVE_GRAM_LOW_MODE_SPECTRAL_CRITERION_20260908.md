# RH Mertens cumulative Gram: exact low-mode spectral criterion

Status: `RESEARCH FRONTIER / EXACT FINITE SPECTRAL REFORMULATION / NOT A PROOF OF RH`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Scope: `Mertens / q=1 positive Gram / Brownian covariance / additive low modes / zero-free strength`

## 0. Prior-art boundary

The matrix with entries `min(i,j)` and its sine spectrum are classical (Brownian covariance / inverse discrete Laplacian). Möbius Fourier/Laplace criteria for RH are also a large classical and current literature; recent examples include Verjovsky 2026 (`arXiv:2607.25002`) and Liflandsky 2026 (`arXiv:2607.09797`).

The project contribution claimed here is only the organization of the q=1 cumulative-Mertens positive Gram into an exact finite spectrum, the unconditional high-mode cutoff, and the resulting square-root low-mode/zero-free-strength interface. No novelty is claimed for the underlying classical matrix spectrum.

---

## 1. Cumulative operator

Let

`mu_N=(mu(1),...,mu(N))^T`

and let `L_N` be the lower-triangular cumulative matrix

`(L_N)_{tn}=1[n<=t]`.

Then

`Mvec_N=L_N mu_N`

and

`sum_{t<=N}M(t)^2 = mu_N^T L_N^T L_N mu_N`.

The kernel is

`(L_N^T L_N)_{mn}=N-max(m,n)+1`.

Reverse integer order by `j=N+1-n`. The kernel becomes

`C_N(i,j)=min(i,j)`.

Thus the q=1 flux Gram is unitarily/permutationally equivalent to the finite Brownian covariance matrix.

---

## 2. Exact spectrum of the min kernel

For `k=1,...,N`, define

`theta_k=(2k-1)pi/(2N+1)`

and normalized vectors

`v_k(j)=sqrt(4/(2N+1)) sin(j theta_k)`, `j=1,...,N`.

Then the `v_k` form an orthonormal basis and

`C_N v_k=lambda_k v_k`,

where

`lambda_k=1/[4 sin^2(theta_k/2)]`.

Equivalently, `C_N^{-1}` is the standard second-difference tridiagonal matrix with the terminal Neumann-type boundary row, and its eigenvalues are `4 sin^2(theta_k/2)`.

Let

`mu_rev(j)=mu(N+1-j)`

and

`c_k=<mu_rev,v_k>`.

Then exactly

`sum_{t<=N}M(t)^2 = sum_{k=1}^N lambda_k |c_k|^2`.

Using `(N+1/2)theta_k=(2k-1)pi/2`, one may write the coefficients directly in original integer order as

`c_k=(-1)^(k-1)sqrt(4/(2N+1))`
`    * sum_{n<=N}mu(n) cos((n-1/2)theta_k)`.

Thus the positive cumulative Gram energy is a weighted finite family of very-low-frequency additive Möbius cosine coefficients.

---

## 3. Parseval and unconditional high-mode safety

Parseval gives

`sum_k |c_k|^2=sum_{n<=N}mu(n)^2=Q(N)asymp N`.

For `k` not too close to N,

`lambda_k asymp N^2/(2k-1)^2`.

More generally the monotonicity of lambda_k gives, for every K,

`sum_{k>K}lambda_k|c_k|^2`
`<=lambda_(K+1) Q(N)`
`<<N^3/K^2`.

Take

`K=ceil(sqrt N)`.

Then

`sum_{k>sqrt N}lambda_k|c_k|^2 << N^2`.

This is already at the natural q=1 RH energy scale.

Freeze:

`ADDITIVE_HIGH_MODES k>sqrt(N) ARE UNCONDITIONALLY RH-SCALE SAFE BY PARSEVAL`.

No arithmetic cancellation theorem is needed for these modes.

---

## 4. Exact square-root low-mode RH criterion

For `k<=sqrt N`,

`lambda_k=N^2/[(2k-1)^2 pi^2]` up to absolute multiplicative constants.

Therefore

`sum_{t<=N}M(t)^2 <= N^(2+o(1))`

is equivalent to

`sum_{k<=sqrt N} |c_k|^2/(2k-1)^2 <= N^o(1)`,

because the high-mode contribution is already `O(N^2)`.

The fixed-p Mellin audit established

`RH <=> sum_{t<=N}M(t)^2 <= N^(2+o(1))`

in the full epsilon-family sense.

Hence

`RH <=> sum_{k<=sqrt N}|c_k|^2/(2k-1)^2 <= N^o(1)`.

In unnormalized cosine-sum coordinates

`C_k(N)=sum_{n<=N}mu(n)cos((n-1/2)theta_k)`,

this is equivalently

`sum_{k<=sqrt N}|C_k(N)|^2/(2k-1)^2 <= N^(1+o(1))`.

Freeze project interface:

`RH_LOW_ADDITIVE_MODE_WEIGHTED_ENERGY_CRITERION`.

The mode count is `O(sqrt N)`.

---

## 5. Spectral-width to zero-free-width law

Let

`K=N^alpha`, `0<alpha<=1/2`.

The unconditional high-mode estimate is

`E_high(K)<=N^(3-2alpha)`.

Suppose one could prove the matching low-mode estimate

`E_low(K)=sum_{k<=K}lambda_k|c_k|^2`
`<=N^(3-2alpha+o(1))`.

Then

`sum_{t<=N}M(t)^2 <= N^(3-2alpha+o(1))`.

For p=2, the general Mellin strength calibration says that a moment exponent beta gives a zero-free half-plane

`Re(s)>(beta-1)/2`.

Here `beta=3-2alpha`, hence

`Re(s)>1-alpha`.

Therefore:

`N^alpha CONTROLLED LOW MODES -> ZERO-FREE HALF-PLANE Re(s)>1-alpha`.

At `alpha=1/2` this reaches RH.

This is a one-way implication/strength calibration; no converse for arbitrary alpha is asserted here.

---

## 6. Additive-mode count is not multiplicative critical rank

Previous Mellin/Newton/Euler analyses found a multiplicative **critical rank one**: only the primitive prime power-sum channel can carry critical zero singularities after stable channels are removed.

The current q=1 cumulative Gram has instead `sqrt N` potentially dangerous **additive low-frequency modes**.

These statements are not contradictory because they are different observer decompositions:

- multiplicative Dirichlet/Mellin channel rank;
- additive inverse-difference spectral bandwidth.

Freeze:

`MULTIPLICATIVE_CRITICAL_RANK_1 != ADDITIVE_LOW_MODE_COUNT_sqrtN`.

Do not identify the latter with new spatial dimensions or factor-provenance directions.

---

## 7. Why current short-interval uniformity does not immediately close the low modes

The low modes correspond to frequencies

`theta_k/(2pi) ~ k/N`, `1<=k<=sqrt N`,

so the dangerous frequency window extends from scale `1/N` to `1/sqrt N`.

Current strong short-interval Möbius theorems give logarithmic or qualitative `o(H)` savings in local sums/correlations, not a square-root-variance estimate strong enough to force the weighted low-mode energy `N^o(1)`.

The all-scale Mellin audit also shows that proving the full `sqrt N` low-mode criterion would already prove RH, so any transfer from existing local uniformity must be checked for a hidden RH-strength step.

---

## 8. Observer-specific compression

Discarding modes above `sqrt N` is safe for this one q=1 cumulative Gram observer. It is not a universal arithmetic quotient and does not permit deleting integer Cell identity or prime provenance for other future operations.

BRC/T6 typing:

`HIGH-FREQUENCY SPECTRAL QUOTIENT = OPERATION-SAFE FOR q=1 FLUX ENERGY ONLY`.

---

## 9. Next target

A potentially useful intermediate problem is to obtain, for some scale-dependent alpha tending slowly to zero or for a subpower K, an improved low-mode weighted energy over what follows from uniform Davenport/logarithmic cancellation.

Any fixed positive alpha with the matching `N^(3-2alpha)` bound would already give a fixed-width zero-free half-plane and is therefore a major breakthrough.

The correct goal calibration is spectral/analytic, not merely numerical mode compression.
