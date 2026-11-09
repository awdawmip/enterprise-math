# PREFIX-623-R6 — Exact stationary-point bracket for asymmetric BRC stopping-time variance

Date: 2026-11-09 (Asia/Shanghai). **AUTHOR_PROVED / EXACT_RATIONAL_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED.** Frozen scientific input: `f42f2906d77f24085c123f3ccfe9667d41caa96d`. This result continues PREFIX-622 without re-executing the PREFIX-565 original 96-port action graph. Model and exact survivor recurrence are inherited from PREFIX-610/613/617/621/622.

## Selected question and typed observer

Can the non-monotonic first-passage variance found in PREFIX-622 be located more precisely, and does an asymmetric parameter face of the two-direction model contain a genuine variance turning point? Each native BRC step emits informative label `(i,+)` with probability `p_i/q`, `(i,-)` with probability `(1-p_i)/q`, and otherwise neutral; `i=1,2`, `q=12` for slot-0, `q=24` for slot-1/2. A direction stops at the first informative sample count where exact anytime-confidence width is at most `1/4`, with `beta=1/40`. Let `T_q(p1,p2)` be the native-action count until both directions finish. The probabilities extend continuously to the closed `[0,1]^2` for this parameter extremum study.

The exact first-passage survivor coefficients are `A_n(k)`, and `s_n(p)=sum_k A_n(k)*p^k*(1-p)^(n-k)`, with `s_n=0` for `n>=189`. On the asymmetric face `p1=0`, direction 1's informative sign is always negative, so its stopping count is **deterministically 25**. Thus `s_n(0)=1` for `0<=n<=24`, and zero afterwards.

## Theorem — exact edge polynomial and stationary bracket

For `n=0,...,188` define rational constants:

```text
alpha_n = 1 - sum_{m=0}^{24} binom(m+n,m)/2^(m+n+1)
beta_n  = (n+1) - sum_{m=0}^{24} (m+n+1)*binom(m+n,m)/2^(m+n+2)
mu(p)   = 25 + sum_{n=0}^{188} alpha_n*s_n(p)
H(p)    = 325 + sum_{n=0}^{188} beta_n*s_n(p)
```

Then for each `q in {12,24}`:

```text
E[T_q(0,p)] = q*mu(p)
V_q(p) = Var(T_q(0,p)) = q^2*(2*H(p)-mu(p)^2) - q*mu(p)
V'_q(p) = q^2*(2*H'(p)-2*mu(p)*mu'(p)) - q*mu'(p)
```

These are rational-coefficient polynomials; `deg(V_q)<=376`. **For both q values** the exact-rational certificate verifies

```text
V'_q(37/256) > 0 > V'_q(39/256).
```

Hence there is at least one maximizing stationary point `p_q^*` strictly within `(37/256,39/256)` for the restricted edge interval. It also certifies `V_q(0)<V_q(1/8)` and `V_q(1/2)<V_q(1/8)`. The asymmetric face has a non-monotonic variance profile, beyond the diagonal counterexample in PREFIX-622. Approximate numerical locator only: `p_12≈0.1484027`, `p_24≈0.1486570`; the rational interval and derivative signs are the proved result.

## Proof

PREFIX-622's marked Poissonization gives `mu=S-C` and `H=H1+H2-K`, where the cross weights are `binom(m+n,m)/2^(m+n+1)` and `(m+n+1)*binom(m+n,m)/2^(m+n+2)`. Substituting `s_m(0)=1_{m<25}` into the finite sums produces exactly the displayed `alpha_n, beta_n, mu, H`. The Poisson-gap variance decomposition gives the displayed `V_q`; ordinary polynomial differentiation gives `V'_q`.

The companion self-contained Python standard-library certificate reproduces the corrected PREFIX-621 exact dyadic-width recurrence for all `A_n(k)`, checks forced completion at `n=189` and boundary completion at count 25, then evaluates all displayed rational formulas and derivatives with `Fraction`. Direct integer comparisons verify both derivative signs and the strict variance comparisons, without relying on decimal rounding. A maximizing point on compact `[37/256,39/256]` cannot be either endpoint because the endpoint derivatives point strictly into the interior; at an interior maximum the polynomial derivative is zero. QED.

## Evidence, scope and next work

Author execution: `ALL_CHECKS_PASS`; **357,260** exact dyadic integer comparisons while reconstructing the source survivor recurrence; full rational derivative signs for both q values; q=12/q=24 second-moment thinning identities checked. Companion code: `PREFIX623_R6_boundary_variance_stationarity_certificate.py`; output: `PREFIX623_R6_RESULTS.json` (display decimals plus exact sign decisions). Reuse: `COMPOSE_APPLIED` PREFIX-610/613/621/622, `EXTEND_EXISTING_TOOL` finite polynomial derivative. Observer: retains signed direction label and native action count for this stopping procedure. This is author mathematical proof/checking; Source-native review and Result/Review are separate.

**Next discriminating unit:** determine whether the global variance maximum on `[0,1]^2` lies on an asymmetric boundary face, using exact Bernstein polynomial/interval certificates or rigorous bivariate gradient bounds. Separately test whether the q=24 edge maximum is provably to the right of q=12's. Current service session/owner operations were queued at the time of author publication; reconcile their durable results.
