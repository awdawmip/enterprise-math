# PREFIX-660-R6 — Strict BRC boundary concavity and moving slot optimum

Date: 2026-11-10 (Asia/Shanghai). Scientific status: **AUTHOR_DERIVED / EXACT_RATIONAL_CHECKED / UNREVIEWED / NOT_ADMITTED**.
Frozen scientific pin: `f42f2906d77f24085c123f3ccfe9667d41caa96d`.
Researcher-ID `EM-DIRECT-5DFA63` / TASK_RESEARCH; Research-Activity-ID `RA-F8AD12FF4F5A07E9388F1939`.

## Question and frozen BRC carrier

Determine the boundary stationary maxima of the frozen 189-survivor-layer, two-informative-direction BRC *statistical observer*. The parameters `p,z` are observer probabilities, not primitive Enterprise spatial directions. A prior exact competitor `Q=(0,19/128)` was established in PREFIX-659; the frozen original model is unchanged.

On `p=0`, the first Poissonized clock is precisely Gamma(25,1); let `A_m(k)` be the frozen signed-path multiplicities and

```
s_m(z) = sum_{k=0}^m A_m(k) z^k (1-z)^(m-k)    (m=0,...,188).
a_m = 1 - sum_{n=0}^{24} binom(n+m,n) / 2^(n+m+1).
b_m = m+1 - (1/2) sum_{n=0}^{24} (n+m+1) binom(n+m,n) / 2^(n+m+1).
mu(z) = 25 + sum_{m=0}^{188} a_m s_m(z).
H(z)  = 325 + sum_{m=0}^{188} b_m s_m(z).
W(z)  = 2H(z) - mu(z)^2.
V_q(0,z) = q^2 W(z) - q mu(z).
```

The 189-layer frozen integer predicate is reconstructed and verified in the accompanying standalone certificate. This is a finite univariate polynomial calculation, with degree at most 376.

Set `z0=19/128`, `d=1/4096`, `I=[607/4096,609/4096]`.

## Theorem 660.1 — Unique boundary stationary maximum for every q in [12,24]

For every real `12<=q<=24`, the function `z -> V_q(0,z)` is strictly concave throughout `I`, has positive `z`-derivative at the left endpoint and negative derivative at the right endpoint, and consequently has **exactly one interior stationary point** `z_*(q)`. This point uniquely maximizes `V_q` on `I`.

Furthermore, `z_*(q)` is differentiable and **strictly increasing** as a function of the continuous sampling slot parameter `q`.

This is a boundary-band statement; it does not claim the maximizer on the entire edge `p=0` or the full square `[0,1]^2`.

## Theorem 660.2 — Tight rational brackets and improved certified competitors

For the actual scheme `q=12`:

```
19/128 - 584/2^24 < z_*(12) < 19/128 - 583/2^24
86048.1065484294 < max_{z in I} V_12(0,z) < 86048.1065484353
```

For the actual scheme `q=24`:

```
19/128 + 3682/2^24 < z_*(24) < 19/128 + 3683/2^24
346340.5678394088 < max_{z in I} V_24(0,z) < 346340.5678394320
```

The strict gains over the center point `Q` exceed **0.0078** for `q=12` and **1.2445** for `q=24`. The two schemes therefore favor distinct boundary probabilities, in provably opposite directions from the former center candidate.

## Proof: exact polynomial expansion and certified curvature

All moment coefficients `a_m,b_m` have dyadic denominators dividing `S=2^216`. The polynomial identity

```
[z^j] s_m(z) = sum_{k=0}^j (-1)^(j-k) A_m(k) binom(m-k,j-k)
```

produces integer polynomials `M(z)=S mu(z)` and `K(z)=S H(z)`. Therefore the integer polynomial `P_q(z)=S^2 V_q(0,z)` is

```
P_q(z) = 2 q^2 S K(z) - q S M(z) - q^2 M(z)^2.
```

Expand exactly around `z0` as `P_q(z0+h)=sum_{k=0}^{376}c_{q,k}h^k`. For every `|h|<=d`, the triangle inequality yields

```
|V_q''(0,z0+h) - V_q''(0,z0)|
 <= E_q = S^(-2) sum_{k=3}^{376} k(k-1) |c_{q,k}| d^(k-2).
```

All coefficients, expansions, majorants and comparisons are evaluated by integer or `Fraction` arithmetic. Exact checks give the following *whole-band* inequalities:

| q | E_q strictly below | uniform curvature on I |
|---|---:|---|
| 12 | 42468 | -13000000 < V_12'' < -12800000 |
| 24 | 169652 | -52000000 < V_24'' < -51500000 |

And exact endpoint-derivative tests give:

| q | at z0-d | at z0+d |
|---|---:|---:|
| 12 | V_12' > 2700 | V_12' < -3600 |
| 24 | V_24' > 24000 | V_24' < -1200 |

Primes always mean differentiation with respect to the **second observer probability** `z` while `p=0`.

For each fixed `z`, both `V_q'/q=qW'-mu'` and `V_q''/q=qW''-mu''` are affine in `q`. Thus the two endpoint `q` certificates force strict concavity and the derivative sign change for every real `q in [12,24]`.

For the motion direction, the two uniform curvature enclosures imply

```
W''(z) = (V_24''(0,z)/24 - V_12''(0,z)/12)/12,
-92000 < W''(z) < -88000    throughout I.
```

Exact center derivatives also give `42<W'(z0)<43`. Therefore

```
W'(z) > 42 - 92000/4096 > 19 > 0     (all z in I).
```

Implicit differentiation of `q W'(z_*)-mu'(z_*)=0` now proves

```
dz_*(q)/dq = -W'(z_*(q)) / (q W''(z_*(q)) - mu''(z_*(q))) > 0.
```

The exact derivative is positive at the lower end and negative at the upper end of each dyadic bracket in Theorem 660.2. Concavity gives unique roots strictly between those endpoints. For any bracket `[a,b]`, let `L=max(V_q(a),V_q(b))`. Since `-C_q<V_q''<0`, the standard linear-interpolation remainder gives

```
L < max_{z in [a,b]} V_q(z) < L + C_q(b-a)^2/8,
C_12=13000000, C_24=52000000.
```

The displayed decimal lower bounds are rounded down, the upper bounds up, from these *exact rational* endpoints. This proves the numerical statements, not merely approximations.

## Verification, reuse, scope and next discriminating question

The companion script `PREFIX660_R6_EDGE_CONCAVITY_CERTIFICATE.py` replays every survivor row, validates terminal extinction at layer 189, constructs the boundary Gamma-moment polynomials, applies exact centered-Taylor tail bounds, checks derivatives at each rational endpoint and the two uniquely bracketed roots, and returns **ALL_CHECKS_PASS 22**. The companion `PREFIX660_R6_RESULTS.json` stores the reproducible strict intervals and bounds. No floating-point inequality decides a theorem premise.

Method: `BRC/COMPOSE_APPLIED`; retained carrier is exact signed path multiplicity plus first-stop survivor identity, with binomial observer, Poisson maximum and probability-derivative operations. Source: PREFIX-659 at immutable commit `65536b12a268b619e0e1e89f685de3fb2162bea3`, `research_notes/portable_direct/2026-11-10_prefix659_r6_exact_boundary_competitor_and_slot_transition.md`; frozen science remains `f42f2906d77f24085c123f3ccfe9667d41caa96d`. Neither native six-axis physical dynamics nor the original 96-port model is claimed to have been rerun. This is an author-derived exact finite observer certificate, **not independently reviewed or admitted**.

**Next unit:** certify `partial_p V_q(0,z)<0` along the moving optimum band uniformly across `q in [12,24]`; then feed the new boundary competitors into the symmetry-reduced triangular-domain Bernstein upper-bound exclusion. The parent objective is still the global maximum of `V_12,V_24` over the full two-parameter statistical observer domain.
