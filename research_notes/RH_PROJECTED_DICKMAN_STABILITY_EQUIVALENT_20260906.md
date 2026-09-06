# Projected Dickman stability as the current RH equivalent target

Status: `RESEARCH FRONTIER / PRIOR-ART-DEPENDENT EXACT REDUCTION + PROJECT-DERIVED CONTINUUM BOUND / NOT A PROOF OF RH`
Date: `2026-09-06`
Project: `Enterprise Math / 进取数论`
Depends on: `RH_KUBILIUS_ALLADI_CROSS_SCALE_PARITY_REDUCTION_20260906.md`

## 0. Purpose

The preceding Kubilius-Alladi reduction proved, for

`Y=(logX)^2`,
`V(Y)=prod_{p<=Y}(1-1/p)`,

and the rough parity bias

`G_Y(U)= [sum_{m<=U,P^-(m)>Y}mu(m)] / #{m<=U:P^-(m)>Y}`,

that

`M(X)/X=(D_Y F_X)(0)+O(X^-1/2+o(1))`,

where

`F_X(t)=G_Y(Xe^-t)`

and

`D_Y=V(Y)prod_{p<=Y}(I-p^-1 T_(logp)).`

This note proves that the natural continuum Dickman-Buchstab response already has RH-scale projection under `D_Y`. Therefore RH is equivalent to controlling only the projected discrete-minus-continuum error.

P000 and the BRC typing rules are unchanged.

---

## 1. Independent squarefree small-prime model

Condition the independent Kubilius geometric model on all small-prime exponents being 0 or 1. Then

`B_p~Bernoulli(1/(p+1))`

independently, and

`D(B)=prod_{p<=Y}p^(B_p)`.

Let

`C_Y=prod_{p<=Y}(1-1/p^2)`.

For every bounded function F of `log D`,

`(D_Y F)(0)`
`=C_Y E[(-1)^(sum B_p) F(log D(B))].`

Hence absolutely

`|(D_Y F)(0)| <= E|F(logD(B))|`.

Define the normalized small-factor depth

`V_B=logD(B)/logY`.

---

## 2. Dickman-scale large deviations for the independent small factor

For theta>=0,

`log E exp(theta V_B)`
`=sum_{p<=Y} log[1+(e^(theta logp/logY)-1)/(p+1)]`
`<=sum_{p<=Y}(e^(theta logp/logY)-1)/p.`

Standard PNT/Mertens estimates for the last sum give, in the saddle range relevant below,

`log E exp(theta V_B) <= O(1)+O(e^theta/(theta+1)).`

Choosing theta of order `log(v+2)+loglog(v+3)` in Chernoff's inequality yields the uniform coarse Dickman large-deviation bound

`P(V_B>=v) <= exp[-v log(v+1)+O(v loglog(v+2))]`

for `v>=1` in the range needed up to the critical depth.

Only the power-scale consequence is needed; no sharp Dickman constant is asserted here.

---

## 3. Continuum rough parity response

Let

`u=logX/logY ~ (1/2)logX/loglogX`.

For remaining rough depth r, use the continuum parity bias

`g(r)=omega_-1(r)/omega(r)=rho'(r)/omega(r)`

for r in the ordinary rough regime, with any uniformly bounded natural extension over the finite initial regime.

Buchstab omega is positive and bounded away from 0 after the initial compact interval. Also

`rho'(r)=-rho(r-1)/r`.

The classical bound

`rho(v) <= 1/Gamma(v+1)`

therefore gives the coarse uniform estimate

`|g(r)| <= exp[-r log(r+1)+O(r)]`

for large r, while `|g(r)|=O(1)` on bounded r.

Define

`F_cont(t)=g(u-t/logY)`.

---

## 4. Convolution-of-depths bound

Partition the random depth `V_B` into unit intervals `j<=V_B<j+1`.

For `0<=j<=u+O(1)`, combine the preceding two bounds. The contribution of the jth block is at most

`exp[-j log(j+1) -(u-j-O(1))log(u-j+1) + O(u loglog(u+2))]`.

By convexity of `x log x`, uniformly for `0<=j<=u`,

`j log j +(u-j)log(u-j) >= u log(u/2)`.

Hence the sum of all blocks is bounded by

`exp[-u logu + O(u loglogu)]`.

The tail `V_B>u+O(1)`, where the continuum response is only bounded by O(1), satisfies the same power-scale bound by the Chernoff estimate.

At

`u=logX/(2loglogX)(1+o(1))`,

we have

`u logu=(1/2+o(1))logX`,

whereas

`u loglogu=o(logX)`.

Therefore

`E|g(u-V_B)| <= X^-1/2+o(1)`.

Consequently

`|(D_Y F_cont)(0)| <= X^-1/2+o(1)`.

This is the required unconditional continuum bound.

### Interpretation

Splitting the total critical depth between a small-prime Cell and the remaining rough Cell can enlarge the local Dickman amplitudes by an entropy factor `exp(O(u))`, but at the RH depth `u~logX/loglogX` this factor is only `X^o(1)` and cannot change the square-root exponent.

This is the precise power-scale content behind the earlier BRC block/shuffle discussion. No claim is made that positive shuffle multiplicity itself creates signed cancellation.

---

## 5. RH equivalent projected-stability criterion

From the prior Kubilius reduction,

`M(X)/X=(D_Y F_X)(0)+O(X^-1/2+o(1)).`

Write

`F_X=F_cont+E_X`,

where

`E_X(t)=F_X(t)-F_cont(t)`

is the discrete rough-parity error.

Section 4 gives

`(D_Y F_cont)(0)=X^-1/2+o(1)`

in absolute value. Therefore

`M(X)/X=(D_Y E_X)(0)+O(X^-1/2+o(1)).`

Using the classical equivalence

`RH <=> M(X)=O_epsilon(X^(1/2+epsilon))`,

we obtain the exact project target:

`RH <=> (D_Y E_X)(0)=O_epsilon(X^(-1/2+epsilon))`

for every epsilon>0, with `Y=(logX)^2`.

Freeze:

`RH <=> PROJECTED_DICKMAN_STABILITY_AT_CRITICAL_KUBILIUS_DEPTH`.

This is an equivalent reformulation, not a proof.

---

## 6. Why this target is strictly narrower than uniform Dickman stability

The criterion does NOT require

`sup_t |E_X(t)| <= X^-1/2+epsilon`.

Large pointwise errors are permitted provided they have small projection under the complete small-prime parity operator

`D_Y=V(Y)prod_{p<=Y}(I-p^-1 T_logp)`.

Thus the research target is a single high-order signed functional of the error, not a uniform approximation theorem for all smooth/rough counts.

This distinction matters because uniform Dickman approximation at the Hildebrand critical range is already RH-strength.

---

## 7. Spectral warning

For a pure exponential budget mode `F(t)=e^(lambda t)`,

`D_YF(0)=V(Y)prod_{p<=Y}(1-p^(lambda-1)).`

A zeta-zero mode in the linear rough numerator is therefore propagated by the matching finite Euler factor. Modewise linear factorization is zero-transparent and cannot prove RH.

The projected-stability route can only gain from structure not visible in the linear numerator alone, notably:

- the bounded nonlinear rough bias `G_Y=R_Y/S_Y`;
- collision/Gram information;
- the full Cell endpoint budget;
- provenance-preserving dependence of the error on the small-factor product.

Do not replace `G_Y` by an arbitrary linear source and claim contraction.

---

## 8. New smallest unit

Study

`E_X(t)=G_Y(Xe^-t)-g(u-t/logY)`

under the independent squarefree Kubilius measure on `t=logD(B)`.

The next useful theorem would be any nontrivial structural bound on the single parity correlation

`E[(-1)^(sum B_p) E_X(logD(B))]`

that is stronger than the generic norm bound and does not assume RH-strength prime discrepancy.

Natural diagnostics:

1. biased-Fourier degree/influence of the budget response;
2. finite-difference smoothness of a Riesz-smoothed version of `G_Y`;
3. whether the Green rank-one dominant component of `E_X` has an arithmetic annihilation identity at finite scale;
4. high-order Alladi moment cancellation after factorial normalization.

No RH proof is claimed.