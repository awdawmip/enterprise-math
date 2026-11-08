# PREFIX-616-R6 — Exact sign-complete BRC observation cost and rare-sign instability

Date: 2026-11-09 Asia/Shanghai. Status: AUTHOR_PROVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED.
Frozen science pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Original native graph: PREFIX-565 Git blob `7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41`.
Dependency: PREFIX-610 signed-label native phase+Boolean-slot observation, PREFIX-613 confidence theory, PREFIX-614 count-only moments, PREFIX-615 neutral-invariant geometric stopping-time transfer.

## Defined native-derived experiment

Fix `1<=k<=6`, `d=2k`, `|theta_l|<1/48` and `q=12` (native slot-0 Boolean tag) or `q=24` (native slot-1 or slot-2 Boolean tag). Each trial independently draws a *new* source phase in the inherited PREFIX-610 phase-contrast family and performs one original BRC action. The original observable is terminal phase jointly with the Boolean action-source tag; original phase, branch identity, action provenance and multiplicities are retained.

For only the declared phase-contrast likelihood and the next stopping rule, PREFIX-610 proves the exact signed-label distribution

`P(Y=(l,s)) = p_(l,s)=(1+48*s*theta_l)/(2q)`, `l=1,...,d`, `s=+1,-1`;
`P(Y=neutral)=1-d/q`.

The score sign `s` is the precise PREFIX-610 phase-contrast score, not a physical phase/amplitude sign. Define `T` as the first number of *independent one-step trials* at which every label `(l,+)` and `(l,-)` has appeared. This stopping condition uses the observed signs and ignores neutral insertions. A trial count is not a physical Heartbeat-World trajectory or heartbeat time.

## Theorem A — Exact distribution and first two moments

Let `A` be the set of all `m=2d` signed labels. For `S⊆A`, set `p(S)=sum_{a in S}p_a`. For every integer `n>=0`,

```text
P(T>n) = sum_{empty != S subset A} (-1)^(|S|+1) (1-p(S))^n.
P(T<=n) = sum_{S subset A} (-1)^|S| (1-p(S))^n.
E[T] = sum_{empty != S subset A} (-1)^(|S|+1) / p(S).
E[T^2] = sum_{empty != S subset A} (-1)^(|S|+1)
               * (2/p(S)^2 - 1/p(S)).
Var[T] = E[T^2]-(E[T])^2.
```

*Proof.* The event `T>n` means that at least one signed coupon is absent. For any subset `S`, independent trials avoid all labels in `S` with probability `(1-p(S))^n`; finite inclusion–exclusion proves the CDF and survival formula. All nonempty subset masses satisfy `0<p(S)<=1` in the stated open cube. The positive-integer tail identities `E[T]=sum_{n>=0}P(T>n)` and `E[T^2]=sum_{n>=0}(2n+1)P(T>n)`, with geometric summation, prove the moment formulas. This is an exact native-BRC-observer **specialization of the classical unequal-probability coupon collector**, not a novelty claim for inclusion–exclusion itself. QED.

## Theorem B — Balanced sign regime and sharp quantiles

If `theta=0`, every signed label has probability `1/(2q)`. With `H_m=sum_{i=1}^m1/i` and `H_m2=sum_{i=1}^m1/i^2`,

```text
E[T]=2*q*H_(2d)
Var[T]=(2*q)^2*H_(2d)2 - 2*q*H_(2d)
P(T<=n)=sum_{j=0}^{2d} (-1)^j*C(2d,j)*(1-j/(2q))^n.
```

*Proof.* Group inclusion–exclusion by subset cardinality for the CDF. When `r` distinct signed labels have appeared, the next new label arrives after a geometric wait with success probability `(2d-r)/(2q)`. The independent successive waiting times have the displayed summed means and variances. QED.

For `d=12` all probabilities and thresholds were checked exactly with integer/Fraction arithmetic. Reported decimals are display only:

| Boolean tag | E[T] | Var[T] | smallest N for P(T<=N)>=0.95 | smallest N for >=0.99 |
|---|---:|---:|---:|---:|
| slot 0, q=12 | 90.622996 | 833.352084 | **145** | **183** |
| slot 1/2, q=24 | 181.245993 | 3514.654329 | **293** | **370** |

The code verifies both threshold inequalities and their strict failures at `N-1`. Sign completion dominates count-only `r=2` coverage pathwise, as two distinct signs imply at least two observations. PREFIX-614's count-only `d=12,q=12,r=2` mean is about 58.0450, a different stopping criterion.

## Theorem C — rare-sign asymptotics

Fix all directions except `j` in the interior of the parameter cube and let `theta_j -> 1/48`. Write `epsilon=1-48*theta_j -> 0+`; the negative coupon has probability `p_rare=epsilon/(2q)`. Let `tau` be its first arrival and `U` the time to observe all *other* coupons in the same stream. Then `T=max(tau,U)` and `0<=T-tau<=U`, giving

```text
1/p_rare <= E[T] <= 1/p_rare + E[U],
E[T] = 2*q/epsilon+O(1),
Var[T] = (2*q/epsilon)^2+O(1/epsilon).
```

*Proof.* All other coupon probabilities stay bounded away from zero, so `E[U]` and `E[U^2]` are uniformly bounded. The rare first-arrival time is geometric with `E[tau]=1/p_rare` and `Var(tau)=p_rare^-2-p_rare^-1`. Let `D=T-tau`, with `0<=D<=U`; then `E[D^2]=O(1)`. Cauchy–Schwarz bounds `Cov(tau,D)=O(p_rare^-1)`, proving the variance expression. QED.

This identifies a target-specific distinction: the PREFIX-610 local Fisher information `c_j/(1-2304*theta_j^2)` grows as `theta_j` approaches the boundary, whereas collecting *both* signs necessarily waits for a rare event. These conclusions address different statistical goals and hold together.

Exact `d=2,q=12,theta=(0,(1-epsilon)/48)` examples:

| epsilon | E[T] | 1/p_rare |
|---|---:|---:|
| 1/4 | 104.926407 | 96 |
| 1/8 | 196.925347 | 192 |
| 1/16 | 386.601802 | 384 |
| 1/32 | 769.339229 | 768 |
| 1/64 | 1536.679686 | 1536 |

## Evidence, correspondence and next action

Companion source: `PREFIX616_R6_sign_complete_coupon_certificate.py`, results: `PREFIX616_R6_RESULTS.json`. The script performs **141 exact rational checks**, comparing finite inclusion–exclusion moments against an independent full bitmask Markov recurrence for `d=2,4`, checking occupancy CDF by forward Markov propagation, balanced `d=12` exact quantiles, the PREFIX-615 q=12/24 thinning relation, and the rare-sign expectation sandwich. Observed result: `ALL_CHECKS_PASS 141` (local standard-library Python execution on 2026-11-09). No native 96-port PREFIX-565 graph was rerun in this step.

Bitmask check interface: if `u` is the total mass of unseen coupons and `m_a,w_a` are the remaining first and second moments after a newly seen coupon `a`, then `m=(1+sum_unseen p_a*m_a)/u`, `w=(2*m-1+sum_unseen p_a*w_a)/u`. Terminal state has both moments zero.

Reusable theorem interface: inputs `d,q,theta` restricted as above, outputs exact CDF/moments, uniform sharp thresholds and rare-sign asymptotics. Reuse resolution: `REUSE_APPLIED` PREFIX-610 native signed-label map, PREFIX-615 thinning law and standard weighted coupon inclusion–exclusion; `EXTEND_EXISTING_TOOL` R6 signed-label observer family. The signed-label projection is certified for this defined likelihood and stopping operation, with original raw native data retained for other future operations.

Next discriminating unit: construct the exact PREFIX-613 confidence-diameter sign-adaptive stopping rule, then calculate or rigorously bound its expected trial count as a function of `epsilon,alpha,theta`, first for `d=2`. Compare to both direction-count thresholds and sign-complete collection under the same observation cost. Independent mathematical review and any canonical task Result/Review admission remain open.


## Prior mathematical literature (checked 2026-11-09)

The coupon-collector techniques used in this report are well-established probability results. Nath, *Waiting Time in the Coupon-Collector's Problem*, Australian Journal of Statistics **15** (1973), 132–135, DOI `10.1111/j.1467-842X.1973.tb00018.x`, studies unequal coupon probabilities and waiting-time distributions, means and variances. May, *Coupon Collecting with Quotas*, Electronic Journal of Combinatorics **15** (2008), #N31, DOI `10.37236/906`, derives finite generating-function expressions for nonuniform probabilities and quotas. Shank–Yang, *Coupon Collector Problem for Non-Uniform Coupons and Random Quotas*, Electronic Journal of Combinatorics **20** (2013), #P33, DOI `10.37236/3348`, treats nonuniform and random quotas.

The contribution documented in this note is the **specific exact reduction of the frozen native BRC signed-label readout to a sign-complete sampling target, the parameterized sign-boundary cost, and exact native-observer trial thresholds**, with source-scoped checking; it is not a claim of inventing generalized coupon collection.
