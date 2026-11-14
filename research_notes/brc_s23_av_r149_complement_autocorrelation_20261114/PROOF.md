# R149 — Exact complement duality and common-residue autocorrelation

Date: 2026-11-14 (Asia/Shanghai).
Frozen scientific input: `43ec6098b1330ae86d0a7863be336c5d97f6ef34`.
Status: author-side derivation and exact computational crosscheck; `NOT_REVIEWED`.
Model: external scalar tied-phase S23 finite mechanical-word observation, with integer phase-index multiplicity. Native Heartbeat X6 identity is not asserted.
Prior: R146 `b02b0c242b274bc6a82111dbd3600126a2867319`; R147 `2b81c43614889ccb638bb7d8feb329c3c467ff02`; R148 `06f79f0d3c04f6c73a056c552793f48b9254ad08`.

## Exact definitions

For a binary finite Sturmian word `w=(w_0,...,w_{m-1})` with prefix sums `s_0=0, s_j=sum_{i<j}w_i`, its nonempty free-intercept slope support `(alpha,beta)` is obtained from
`alpha=max(0,max_{i<j}(s_j-s_i-1)/(j-i))`,
`beta=min(1,min_{i<j}(s_j-s_i+1)/(j-i))`.
Write the reduced endpoint fractions `alpha=a/b < beta=c/d`, with `b,d>=1`, and put
`U=min_{0<=j<=m}(b(s_j+1)-ja)`,
`V=max_{0<=j<=m}(ds_j-jc)`.
For `L=K-1>=1`, the number of admissible integer phase indices is
`C_w(K)=ceil((Lc-V)/d)-floor((La-U)/b)-1`.
Define `g=gcd(b,d)`, `q=(g-1)/2` and the R148 joint-residue covariance
`Gamma_w=(1/(gbd))*sum_{t=0}^{g-1}( ((at-U) mod g)-q )*( ((V-ct) mod g)-q )`.

## R149.1 — Exact complement fiber duality

**Theorem (all m>=1, all finite Sturmian binary w and all integer K>=2).**
For the bitwise complement `bar(w)`, the endpoint and envelope parameters are exactly
`(a_bar,b_bar,c_bar,d_bar,U_bar,V_bar)=(d-c,d,b-a,b,d-V,b-U)`.
Consequently `C_bar(w)(K)=C_w(K)` for every K, with identical occurrence, disappearance and recovery coefficients. Their full integer-fiber count sequences and all statistics of these sequences coincide. In particular `Gamma_bar(w)=Gamma_w`.

**Proof.** The complemented prefix is `s'_j=j-s_j`. Every substring count is sent to its length minus its original count, so its free-intercept support maps under `theta -> 1-theta`, giving `alpha'=1-beta=(d-c)/d` and `beta'=1-alpha=(b-a)/b`; the transformed fractions remain reduced. Direct substitution gives
`U'=min_j[d((j-s_j)+1)-j(d-c)]=d-max_j(ds_j-jc)=d-V` and
`V'=max_j[b(j-s_j)-j(b-a)]=-min_j(bs_j-ja)=b-U`.
Let `A=(La-U)/b`, `B=(Lc-V)/d`. For the complement the arguments of ceiling and floor are `L-1-A` and `L-1-B`, respectively. Their difference is
`ceil(L-1-A)-floor(L-1-B)-1=ceil(B)-floor(A)-1=C_w(K)`.
The fluctuation covariance is a complete-period statistic of this very sequence with the same support width `beta-alpha`; hence it is identical. QED.

At the level of generic (non-breakpoint) parameters, `theta -> 1-theta` maps integer phase labels `N=floor(L theta)` to `N'=L-1-N`; this is a direct fiber bijection (breakpoint values may be avoided because a qualified phase interval is open).

## R149.2 — Closed autocorrelation formula in the common-residue class

**Theorem (all reduced endpoints and integer U,V satisfying `a+c≡0 (mod g)`).**
Let `lambda=(U+V) mod g` chosen in `{0,...,g-1}`. Then the entire R148 covariance has the closed form

`Gamma_w=[g^2-1-6 lambda(g-lambda)]/(12 b d).`   (R149.2)

The formula includes `g=1`, when covariance is zero. For `g>1` the sign is determined exactly by comparing `6 lambda(g-lambda)` with `g^2-1`. This computation uses one gcd and modular sum, rather than a length-`g` dot product.

**Proof.** Since `c≡-a (mod g)`, setting `r=(at-U) mod g` yields `z=(V-ct) mod g=(r+U+V) mod g=(r+lambda) mod g`. Coprimality `gcd(a,g)=1` makes `r` run through every residue once. Put `f(r)=r-(g-1)/2`. Its squared norm is `sum_r f(r)^2=g(g^2-1)/12`. Exactly `g-lambda` of the shifts `r -> (r+lambda) mod g` change `f` by `lambda`, while the other `lambda` change it by `lambda-g`. Therefore
`sum_r (f(r)-f(r+lambda mod g))^2=g lambda(g-lambda)`.
The polarization identity gives
`sum_r f(r)f(r+lambda mod g)=g(g^2-1)/12-g lambda(g-lambda)/2`.
Divide by `gbd` as in R148.1. QED.

## R149.3 — Conditional reversal covariance invariance

**Theorem (any finite Sturmian word with `a+c≡0 (mod gcd(b,d))`).**
Let `rev(w)` reverse the digit order. Then `Gamma_rev(w)=Gamma_w`. In contrast, `C_rev(w)(K)` need not equal `C_w(K)` pointwise; for example `w=001`, `K=2` gives one index versus zero.

**Proof.** Reversal preserves the multiset of substring lengths and counts, so it preserves `alpha,beta`. If `g=1`, both covariances vanish. For `g>1`, the endpoints are interior (`b,d>1`). Set `A_j=bs_j-ja` and `B_j=ds_j-jc`. The slope-support strict inequalities hold just inside the interval. At the lower endpoint there is a tight pair of lines and hence `max A-min A=b`; at the upper endpoint `max B-min B=d`. As `min A=U-b`, `max A=U`, `max B=V` and `min B=V-d`. For reversed prefix sums `s'_j=s_m-s_{m-j}`, direct substitution yields
`U_rev=b(s_m+1)-am-U`, `V_rev=d(s_m+1)-cm-V`.
Because `g` divides `b,d` and `a+c`, the shifted sum satisfies
`lambda_rev=(U_rev+V_rev) mod g=(-lambda) mod g`.
The R149.2 expression depends on lambda only through `lambda(g-lambda)`, which is invariant under `lambda->-lambda mod g`. QED.

## Finite evidence and unresolved question

The exact checker examines every binary word of lengths `1..15`; 1,906 have nonempty free-intercept Sturmian support. It checks 11,436 complement fiber equalities at `K=2,3,4,7,15,31`, all 1,906 applicable closed covariance formulas, and 1,906 reversal covariance equalities. Among these, 298 have noncoprime endpoint denominators. All 298 happen to satisfy `a+c≡0 (mod g)`; **this last observation is only a finite conjecture-generating result, not a proved all-length premise**. Six words have positive covariance. Output marker: `R149_COMPLEMENT_AUTOCORRELATION_PASS`.

Next: prove or disprove `a+c≡0 (mod gcd(b,d))` for *every* finite Sturmian word. If proved, R149.2–R149.3 become unconditional all-word formulas; if false, classify the exceptional endpoint residues. Then use explicit offset `lambda` and R146B single-fiber-loss tests at `K=E(m)` to advance permanent saturation.
