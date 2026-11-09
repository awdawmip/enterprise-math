# PREFIX-644-R6 — Higher-order binomial score orthogonality and a 50%-wider signed-BRC valley strip

Date: 2026-11-10 (Asia/Shanghai). Research: independent TASK_RESEARCH. Frozen science: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Native Researcher-ID: `EM-DIRECT-195CD1`; activity `RA-E4ADE429B6BEC0BE16A62CE0` (verified original session publication `83059591f04f1aa2a942a3cbe07ade5ce9ec4803`). Status: `AUTHOR_PROVED_ANALYTIC_LEMMA / EXACT_RATIONAL_IMPLICATION_CHECKED / UNREVIEWED / NOT_ADMITTED`. This is about the fixed signed-BRC *statistical observer*; no new original native 96-port computation or physical residual attribution is claimed.

## Problem and inherited inputs

The mother objective is the global two-parameter sampling-variance extremum of the PREFIX-621/622 observer. The current dependency is unique local variance valleys on `I=[3/20,1/6]` and a large second-parameter interval `Z=[37/256,39/256]`. PREFIX-643 certifies unique first-parameter minimizers on the narrow strip `|z-19/128|<=2^-18` using binomial first- and second-score bounds 20 and 1500. Our discriminating question is whether the orthogonality of higher binomial scores permits a larger rigorous strip, with the same frozen scientific inputs.

Assume PREFIX-622's exact moment identities, PREFIX-631's endpoint-gradient reversal throughout Z, PREFIX-639's center-slice derivative Bernstein certificate, and PREFIX-643's Gamma mean cap and negative-binomial weight identities. Their exact immutable sources are given below.

## Lemma 644.1 — binomial score bound of arbitrary derivative order

Let `K~Bin(n,u)`, `0<u<1`, and let `r:{0,...,n}->[0,1]` be fixed. Put `S_n(u)=E_u[r(K)]`. For each integer `1<=j<=n`,

`|S_n^(j)(u)| <= sqrt(j! (n)_j) / [2 (u(1-u))^(j/2)]`, where `(n)_j=n(n-1)...(n-j+1)`; derivatives of order `j>n` vanish.

**Proof.** Express `K` as the sum of iid Bernoulli variables `X_i`. Their likelihood log-scores are `ell_i=(X_i-u)/(u(1-u))` with `E ell_i=0` and `E ell_i^2=1/[u(1-u)]`. The fixed-sample likelihood is a product of n affine factors in u. Its j-th derivative divided by the likelihood is therefore

`L_j=sum_(i_1,...,i_j mutually distinct) ell_(i_1)...ell_(i_j)`.

Finite differentiation gives `S_n^(j)=E[r(K)L_j]`. For j>=1, `E L_j=0`. When squaring the ordered-tuple sum, independence and centering annihilate every pair except two tuples with exactly the same unordered index set. There are `(n)_j j!` such ordered pairs, giving the exact score second moment

`E L_j^2=j!(n)_j/[u(1-u)]^j`.

Center `r` by one half and use Cauchy–Schwarz:
`|S_n^(j)|=|E[(r(K)-1/2)L_j]| <= (1/2) sqrt(E L_j^2)`. QED.

The j=1,2 cases respectively give `|S_n'|<=sqrt(n)/(2sqrt(u(1-u)))` and
`|S_n''|<=sqrt(n(n-1)/2)/(u(1-u))`. This is an orthogonal binomial/Krawtchouk score observation. No claim of novelty against the classical probability literature is made.

## Lemma 644.2 — tighter mixed partial on the fixed model

Each frozen survivor polynomial is `s_n(u)=sum_k r_n(k)binom(n,k)u^k(1-u)^(n-k)`, `0<=r_n<=1`, `0<=n<=188`. For `p in I`, `p(1-p)>=51/400`; for `z in Z`, `z(1-z)>=8103/65536`. Exact rational comparisons:

`188 < 4(96/5)^2(51/400)`,
`188 < 4(39/2)^2(8103/65536)`,
`188*187/2 < [1040(51/400)]^2`

imply `|s_n'(p)|<Pp=96/5`, `|s_n'(z)|<Pz=39/2`, and `|s_n''(p)|<R=1040`.

Write `w(n,m)=binom(n+m,n)/2^(n+m+1)`. From PREFIX-622 the mean `mu`, second raw half-moment `H`, variance `W=2H-mu²`, and `F_q=W-mu/q` use products `w(n,m)s_n(p)s_m(z)`. The nonnegative extended weights satisfy `sum_(m>=0)w(n,m)=1` and `sum_(m>=0)[(n+m+1)/2]w(n,m)=n+1`. Truncation to `0<=m<=188` decreases those positive sums. Thus, on I×Z,

`|mu_p|<=A=189Pp=14553/4`, `|mu_z|<=E=189Pz=7371/2`,
`|mu_pp|<=B=189R=196560`,
`|mu_pz|<=C=189PpPz=567567/8`,
`|mu_ppz|<=D=189RPz=3832920`,
`|H_ppz|<=J=[189*190/2]RPz=364127400`.

The Gamma-arrival coupling of PREFIX-643 bounds `mu<197`. Two p derivatives and one z derivative of `2H-mu²-mu/q` then imply, for every q>=12,

`|F_q,ppz| < K := 2[J+2AC+EB+197D]+D/12 = 117867680658/25 = 4,714,707,226.32`.

This strengthens PREFIX-643's model-local mixed bound `6,598,084,500` without changing the observer, the branch identity or its probability domain.

## Theorem 644.3 — 50%-wider unique-valley region

Let `z0=19/128`, `h=3/2^19`. For all
`p in [3/20,1/6]`, `z in [z0-h,z0+h]`, `12<=q<=24`,

`273 < mu_p(p,z) < 322`, `122 < F_q,pp(p,z) < 75078`.

**Proof.** PREFIX-639's center-line Bernstein controls are `274<mu_p(p,z0)<321`, `27100<F_q,pp(p,z0)<48100`. Integrating the previous mixed derivative bounds along z changes them by at most `C h` and `K h`, respectively. Exact Fraction comparisons in the companion program establish `Ch<1` and
`K h=176801520987/6553600 <26978`, with `27100-Kh>122`, `48100+Kh<75078`. Apply PREFIX-631's strict endpoint signs `F_q,p(3/20,z)<0<F_q,p(1/6,z)`, valid over all Z and q>=12. Strict convexity supplies a unique interior global minimizer `c(q,z)` over I. The halfwidth `h` is exactly `3/2` times the PREFIX-643 halfwidth.

With `t=1/q`, implicit differentiation of `F_q,p(c,z)=0` yields `c_t=mu_p/F_q,pp>0`. Therefore the actual-slot minimizers satisfy
`c(12,z)-c(24,z)>273/(24*75078)>0`.
For `Phi(t,z)=min_(p in I)[W(p,z)-t mu(p,z)]`, the envelope formula yields
`Phi_tt=-mu_p(c,z)^2/F_q,pp(c,z)`, hence the strict curvature bound
`273²/75078 < -Phi_tt < 322²/122`.

A better-conditioned nested strip `|z-z0|<=5/2^20` (125% of PREFIX-643's width) satisfies the stronger `4600<F_q,pp<70600` and the useful two-sided optimizer-gap inequality
`273/(24*70600) < c(12,z)-c(24,z) < 322/(24*4600)`.
In fact the same proof gives the parameterized family
`274-Ch<mu_p<321+Ch`,
`27100-Kh<F_q,pp<48100+Kh` for any centered substrip inside Z, and strict convexity whenever `h<27100/K`. This is a conditional width/conditioning tradeoff, not a claim that all Z is covered.

## Exact certificate and limitations

A Python standard-library Fraction certificate tests 18 exact rational conditions plus 156 finite sanity equalities for the general binomial score formula and L2 moments on n=1,...,8, j<=4 and u=2/7,3/8: `ALL_CHECKS_PASS 18 SCORE_CHECKS 156`. The analytic lemma, not finite testing, proves its universal claim. The application inherits the exact statements and versions of PREFIX-631, PREFIX-639 and PREFIX-643; those predecessor certificates and the original native 96-port system were not rerun here. No independent review, formal Result, or acceptance was performed.

Next discriminating action: restricted bivariate Bernstein coefficients of `F_12,pp` and `F_24,pp` over I×Z, or survivor-conditioned covariance derivative bounds replacing global score envelopes. A negative exact function value refutes rectangle positivity; a negative Bernstein coefficient alone does not and is an instruction to subdivide. The mother objective is still the full two-parameter global variance maximum.

Provenance: PREFIX-631 `cab564fd9a112feed4a5a1fac0ee5556ebe7d7b6`; PREFIX-639 `6acbf4f472a48d846859a71a31af243808961cff`; PREFIX-643 `ae7872ca18676397fcc0dd9424fb77e08928bee7`.
