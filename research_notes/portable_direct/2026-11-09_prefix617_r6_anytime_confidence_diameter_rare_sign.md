# PREFIX-617-R6 — Anytime BRC confidence-diameter stopping has finite rare-sign cost

Date: 2026-11-09 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED.

Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Native original graph: PREFIX-565 Git blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`. Dependencies: PREFIX-610 signed-label reduction, PREFIX-613 exact all-time e-martingale, PREFIX-614 exact count quotas, PREFIX-615 neutral thinning, PREFIX-616 sign-complete coupon asymptotics.

## Model and observable

Fix the inherited native-derived phase-contrast model with `d=2` active null directions, `q=12` for Boolean slot-0 and `q=24` for Boolean slot-1/2 observation. At each independent one-step native action, the compressed signed label is `(ell,+)`, `(ell,-)` with probabilities `p_ell/q`, `(1-p_ell)/q`, respectively, where `p_ell=(1+48 theta_ell)/2`, `0<p_ell<1`; a neutral label has probability `1-d/q`. The compression is sufficient for *this* theta experiment/decision, not for arbitrary future BRC actions. The native phase, slot tag and provenance remain part of the original observer. Trial number is not heartbeat-physical time.

For direction ell, let `m=M_ell(N)` denote informative observations through time N and `a=K_ell(N)` positive signs. Fix `alpha=1/20`, `beta=alpha/d=1/40`; define the all-time confidence set in `p`:

```
C_beta(m,a) = { p in (0,1):
 (m+1)*binom(m,a)*p^a*(1-p)^(m-a) > beta }.
C_beta(0,0) = (0,1).
D_beta(m,a) = diameter C_beta(m,a).
T_delta(q) = inf{ N : max_ell D_beta(M_ell(N),K_ell(N)) <= delta }.
delta=1/4; equivalently target theta diameter <=1/192.
```

The finite-sample stopping rule uses *both* informative counts and observed signs. No point estimate is substituted for an empty or missing observation.

## Theorem A — Anytime coverage at a sign-adaptive stopping time

For every theta in `(-1/48,1/48)^2`:

```
P_theta( all N>=0 and all ell: p_ell belongs to C_beta(M_ell(N),K_ell(N)) ) >= 1-alpha=19/20.
```

This covers the random time `T_delta(q)`, and indeed any observation-adapted choice of reporting time.

**Proof.** For fixed candidate p, `E(m,a;p)=[(m+1)binom(m,a)p^a(1-p)^(m-a)]^-1` has `E(0,0;p)=1` and satisfies the PREFIX-613 exact one-step conditional expectation recurrence. A neutral or other-direction observation leaves the coordinate factor unchanged. Thus each coordinate process is a nonnegative martingale in global trial time, even though the coordinate counts are dependent. Ville's inequality and a union bound over the two directions give error at most `d beta=alpha`. The reported intervals are precisely the e-value acceptance sets. QED.

## Theorem B — Finite uniform resource bound, with an exact sign-sensitive witness

For every `m>=1`, every `0<=a<=m`, the accepted p interval has diameter

```
D_beta(m,a) <= sqrt( 2*log((m+1)/beta)/m ).
```

For `beta=1/40`, each direction with `m>=320` therefore has `D_beta(m,a)<1/4` for *all* sign counts a. In particular, pathwise,

```
T_delta(q) <= T_(q,2,320)
E_theta T_delta(q) <= q * mu_(2,320) < infinity
```

for every parameter, including a bound uniform as p approaches 0 or 1. Here `T_(q,d,r)` is the PREFIX-614 stopping time for `r` informative observations from each direction, and

```
mu_(2,r) = 2r - sum_{a=0}^{r-1} sum_{b=0}^{r-1}
                      binom(a+b,a)/2^(a+b+1).
```

**Proof.** Write `p_hat=a/m`. The maximized binomial point probability is at most `1`; its likelihood at arbitrary p equals this maximized likelihood times `exp(-m D_KL(p_hat||p))`. The acceptance inequality therefore implies `m D_KL(p_hat||p)<log((m+1)/beta)`. Bernoulli Pinsker `D_KL>=2(p-p_hat)^2` bounds the interval. To certify `m=320`, note `(321)/beta=12840` and the exact rational Taylor sum `sum_{i=0}^{10} 10^i/i! >12840`; hence `log(12840)<10` and `2*log(12840)/320<1/16`. The logarithmic ratio decreases for larger m because `log(1+x)>x/(1+x)`. The quota waiting time is almost surely finite with the finite expectation displayed, established either by independent Poisson clocks or the finite-state recurrence. QED.

This is **genuinely sign-adaptive**: at `m=25,a=25`, the interval is `((beta/26)^(1/25),1)` and has diameter <1/4, whereas at the same `m=25,a=12`, both rational probabilities `p=1/4` and `p=3/4` satisfy the strict acceptance inequality. Hence `D_beta(25,12)>1/2`. The 25-observation positive streak stops that coordinate, while the same count with mixed signs does not.

## Theorem C — Finite boundary cost, unlike sign-complete collection

Let `p_1,p_2 ->1` in the open parameter cube. Couple the trials by drawing the same informative direction/neutral stream and uniform random variables for their signs. Since `T_delta(q)<=T_(q,2,320)` for all parameters and this count quota has finite expectation, dominated convergence yields

```
lim_{p_1,p_2->1} E_p[T_delta(q)]
      = E[T_(q,2,25)] = q * mu_(2,25).
```

Indeed, with every informative sign positive, a direction first meets the `delta=1/4` requirement on its 25th informative observation: `25*(3/4)^24 >1/40` but `26*(3/4)^25 <1/40`. Under the stated coupling, every finite prefix has only positive signs for p sufficiently near 1, so the stopping times converge almost surely to the all-positive count-25 quota. Domination above justifies expectations.

The exact two-direction Gamma-max/Markov recurrence gives:

```
mu_(2,25) = 3913470354001175 / 140737488355328.
lim E T_delta(12) = 11740411062003525 / 35184372088832
                  = 333.682551797765... one-step BRC trials.
lim E T_delta(24) = 11740411062003525 / 17592186044416
                  = 667.36510359553... trials.
```

The PREFIX-615 neutral-thinning identity yields `E[T_delta(24)]=2 E[T_delta(12)]` at every interior theta, as the rule ignores neutral gaps.

In contrast, PREFIX-616 sign-complete collection of *both* signs requires rare negatives. If only one p_ell tends to 1 and other directions stay interior, `E[T_sign-complete]=2q/epsilon+O(1)` for `p_ell=1-epsilon/2`. In the exact two-boundary comparison above, where **both** `p_1=p_2=1-epsilon/2`, two negative coupons each have mass `epsilon/(2q)`: waiting for the first has geometric mean `q/epsilon`, then waiting for the other has mean `2q/epsilon`. All nonrare coupons have uniformly bounded completion cost, so `E[T_sign-complete]=3q/epsilon+O(1)`. The confidence-diameter time instead converges to the finite value above, since it need not await any negative observation.

## Reproduction, provenance and next question

Companion exact certificate `PREFIX617_R6_anytime_diameter_stopping_certificate.py`, results `PREFIX617_R6_RESULTS.json`. Local standard-library Python execution (2026-11-09) returned `ALL_CHECKS_PASS 51715`. It checks 51,680 MLE mode inequalities for `m<=320`, the exact rational all-positive threshold and mixed-sign witness, an integer Taylor certificate, and two independently derived exact rational formulas (Poisson/Gamma integration and finite-state Markov expectation) for the boundary cost. No native PREFIX-565 96-port graph was rerun. General all-time coverage and uniform stopping follow the analytical proofs; the finite enumeration is a reproduction certificate rather than the universal proof.

Established prior art: uniform-prior beta-binomial mixture e-processes, Ville confidence sequences and likelihood-based stopping are classical sequential inference tools. Related modern treatment: Howard, Ramdas, McAuliffe and Sekhon, *Time-uniform, nonparametric, nonasymptotic confidence sequences*, Annals of Statistics 49 (2021) 1055-1080, DOI 10.1214/20-AOS1991. This contribution is their **specific BRC signed-label application and exact d=2 rare-sign boundary cost**, not a general priority claim.

Native control check on 2026-11-09: session registration and dispatch both failed before submission with `BACKEND_IDENTITY_CHECK_UNAVAILABLE`; gateway diagnostic `CONFIGURED_NOT_LIVE_VERIFIED`, `research_authority_granted=false`. No Source Researcher-ID, Research-Activity-ID, active Task owner, formal CLAIM/Result/Review or completion authority was inferred. GitHub repository author publication is independent noncanonical mathematical provenance.

**Next discriminating problem:** compute finite-parameter `E_theta T_delta(q)` or certified tight bounds for `d=2`, especially balanced `p=1/2` and intermediate `p`; compare this confidence-diameter stopping time with equal-width *count-only* and sign-complete rules under identical anytime-coverage and observation-cost contracts. Extend to `d<=12` using the exact signed-label observer if the additional matrix structure is retained.

Reuse status: `REUSE_APPLIED` PREFIX-610, -613, -614, -615 and -616; `EXTEND_EXISTING_TOOL` exact BRC signed-label observer.
