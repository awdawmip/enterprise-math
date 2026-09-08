# RH growing-depth Heath-Brown / rough-BRC critical circuit

Status: `RESEARCH FRONTIER / EXACT COEFFICIENT-FILTRATION IDENTITY + NO-GO FOR ABSOLUTE BRANCH CONTROL / NOT RH`
Date: `2026-09-08`
Project: `Enterprise Math / 进取数论`
Scope: `Möbius / Heath-Brown identity / rough sieve / growing BRC depth / critical y=(log X)^2 / P1 barrier`

## 0. Prior-art boundary

Heath-Brown's generalized Vaughan identity and its finite-depth Möbius endpoint are classical. Robles 2026 (`arXiv:2608.07198`) explicitly gives the depth-5 endpoint

`zeta^-1 = 5F_mu - 10 zeta F_mu^2 + 10 zeta^2 F_mu^3 - 5 zeta^3 F_mu^4 + zeta^4 F_mu^5`

through coefficients `n<=V^5`, and explains the general support mechanism `H^K` beyond `V^K`. He uses depth 5 because it is enough for the classical Type I/II `4/5` exponential-sum benchmark.

The present note records the arbitrary-depth endpoint in Enterprise BRC form, introduces a prime-cutoff multiplicative variant, identifies the RH-critical depth `K~(1/2)log X/loglog X` with `y=(log X)^2`, and audits the absolute branch mass. No novelty is claimed for the underlying geometric-series identity.

---

## 1. Arbitrary-depth integer-cutoff endpoint

Let

`F_V(s)=sum_{n<=V}mu(n)n^-s`

and

`H_V(s)=1-zeta(s)F_V(s)`.

For every integer `n<=V`, the coefficient of `zeta F_V` at n is

`sum_{d|n}mu(d)=1[n=1]`.

Hence every Dirichlet coefficient of H_V up to V is zero. Therefore `H_V^K` has no coefficient at `n<=V^K`.

Coefficientwise below `V^K`,

`zeta^-1=F_V(1+H_V+...+H_V^(K-1))`.

Since `H_V=1-zeta F_V`, expand the geometric polynomial:

`zeta^-1 = sum_{j=1}^K (-1)^(j-1) C(K,j) zeta^(j-1)F_V^j`

for every coefficient `n<=V^K`.

At K=5 this is exactly the endpoint identity displayed by Robles.

---

## 2. Prime-cutoff multiplicative variant

For Factor-BRC it is cleaner to use the finite Euler product

`F_y(s)=prod_{p<=y}(1-p^-s)`.

Then

`zeta(s)F_y(s)=prod_{p>y}(1-p^-s)^-1`.

Its Dirichlet coefficient is 1 exactly on integers all of whose prime factors exceed y (the y-rough integers), including coefficient 1 at n=1.

Therefore

`H_y(s)=1-zeta(s)F_y(s)`

has zero constant coefficient and is supported only on y-rough integers `n>1`, hence on `n>y`.

Consequently `H_y^K` is supported on `n>y^K`.

Thus for every `n<=X<=y^K`, exactly

`zeta^-1 = sum_{j=1}^K (-1)^(j-1) C(K,j) zeta^(j-1)F_y^j`.

Freeze project interface:

`GROWING_ROUGH_HEATH_BROWN_IDENTITY`.

It is a coefficient-filtration identity; it does not claim equality of the full Dirichlet functions without the omitted remainder `zeta^-1 H_y^K`.

---

## 3. Exact multiplicative local coefficients

Write

`F_y(s)^j=sum_n a_(j,y)(n)n^-s`.

Since

`F_y(s)^j=prod_{p<=y}(1-p^-s)^j`,

`a_(j,y)` is multiplicative and for a prime p<=y,

`a_(j,y)(p^r)=(-1)^r C(j,r)`, `0<=r<=j`,

while it vanishes on prime factors p>y.

Also

`zeta^(j-1)=sum_n tau_(j-1)(n)n^-s`

with nonnegative divisor coefficient, with the convention `tau_0=delta_1` for j=1.

Therefore for every `n<=y^K`,

`mu(n)=sum_{j=1}^K (-1)^(j-1) C(K,j)`
`      * (a_(j,y) * tau_(j-1))(n)`.

All global signed orientation has been moved into:

1. the outer binomial sign;
2. local small-prime factors `(-1)^r C(j,r)`.

The long branch `tau_(j-1)` is positive.

Typing:

`SMALL_PRIME_SIGNED_PROVENANCE + POSITIVE_LONG_DIVISOR_BRANCH`.

Prime labels remain arithmetic provenance, not X6 axes.

---

## 4. RH-critical depth alignment

Let `L=log X` and choose

`K_RH ~ L/(2 log L)`.

Set

`y=X^(1/K_RH)`.

Then

`log y = L/K_RH = (2+o(1))log L`,

hence

`y=(log X)^(2+o(1))`.

Conversely the canonical choice `y=(log X)^2` gives

`K=ceil(log X/log y) ~ (1/2)log X/loglog X`.

This is exactly the same scale previously reached independently from:

- Hildebrand/Dickman critical smoothness;
- continuum rough parity `rho'(u)` reaching square-root size;
- ordered-factor / Alladi primitive-selector depth;
- fixed-label transport obstruction order.

The growing Heath-Brown identity is therefore an **explicit algebraic circuit at the same critical depth**.

Freeze observation:

`HEATH_BROWN_DEPTH K_RH <-> PRIME_CUTOFF y=(log X)^2`.

This is a scale identity, not an RH proof.

---

## 5. Outer branch count is subpolynomial

The sum of absolute outer binomial coefficients is

`sum_{j=1}^K C(K,j)=2^K-1`.

At the RH-critical K,

`2^K=exp(O(log X/loglog X))=X^o(1)`.

Thus the outer algebraic branch count/coefficient mass is subpolynomial.

This is compatible with a scale-growing BRC circuit: depth diverges, but the outer combinatorial price does not by itself lose a fixed power of X.

---

## 6. Operation-safe two-arm BRC compression

For a final observer depending only on the product integer n (for example the first cosine mode weight `w(n/X)`), do not materialize the `2j-1` convolution variables separately.

Aggregate:

`A-ARM = coefficient a_(j,y)(a)`

and

`B-ARM = tau_(j-1)(b)`.

Then the j-th branch contribution is exactly

`T_j(X;w)=sum_{ab<=X} a_(j,y)(a) tau_(j-1)(b) w(ab/X)`.

The full Möbius weighted sum is

`sum_{n<=X}mu(n)w(n/X)`
`=sum_{j=1}^K (-1)^(j-1)C(K,j)T_j(X;w)`.

This is an observer-specific T6-safe quotient because the declared future operation sees only the final product and coefficient convolution. It is not a universal deletion of the internal factor provenance.

Freeze:

`GROWING_HB_BRANCHES_CAN_BE_COMPRESSED_TO_K TWO-ARM PRODUCT OBSERVERS`.

---

## 7. Absolute branch L1 mass has a hard phase transition at sigma=1

For real `sigma>0`, the weighted absolute Dirichlet mass of the small-prime arm is exactly

`N_1(j,y;sigma)=sum_n |a_(j,y)(n)| n^-sigma`
`=prod_{p<=y}(1+p^-sigma)^j`.

### At sigma=1

Mertens prime summation gives

`log N_1(j,y;1)`
`=j sum_{p<=y}log(1+1/p)`
`=j[loglog y+O(1)]`.

At `y=(log X)^2`, `j<=K~L/(2log L)`, this is

`O(L logloglog X/loglog X)=o(L)`.

Hence

`N_1(j,y;1)=X^o(1)`.

### At any fixed sigma<1

Prime summation gives

`sum_{p<=y}p^-sigma`
`~ y^(1-sigma)/[(1-sigma)log y]`.

The quadratic and higher terms do not change the leading positive growth needed for the lower/upper scale statement. Therefore at j comparable to K,

`log N_1(j,y;sigma)`
`asymp j y^(1-sigma)/log y`
`asymp L^(3-2sigma)/(log L)^2`

(up to a sigma-dependent constant).

For every fixed `sigma<1`,

`L^(3-2sigma)/(log L)^2 >> L`.

Hence

`N_1(j,y;sigma)=X^omega(1)`

(superpolynomial in X in exponent language).

Freeze no-go:

`ABSOLUTE_SMALL-PRIME_BRANCH_CONTROL_IS_TRAPPED_AT_THE_P1_BOUNDARY sigma=1`.

This reproduces the earlier global boundary:

- P2/Hilbert carrier is meaningful in the critical strip;
- P1 absolute summation cannot be pushed below 1 without losing the needed cancellation.

---

## 8. Why the identity does not prove RH by triangle inequality

Although:

- the coefficient identity is exact below X;
- the depth is exactly the RH-critical depth;
- the outer binomial cost is only X^o(1);

one cannot bound each branch absolutely and sum.

At every fixed `sigma<1` the small-prime branch absolute mass is already superpolynomial. The cross-branch signs and the internal small-prime signs are therefore essential.

This is a quantitative version of the sieve parity barrier in the current BRC language:

`ALGEBRAIC EXACTNESS + POSITIVE BRANCH CAPACITY != SIGNED CRITICAL CANCELLATION`.

The growing-depth circuit relocates the cancellation problem; it does not remove it.

---

## 9. Relation to Robles' depth-5 Type I/II analysis

Robles explains that depth K=5 is enough to force every dyadic configuration into a classical Type I or Type II regime and thereby obtain the `x^(4/5)` benchmark for Möbius exponential sums.

Increasing K does not automatically improve that exponent under the same bilinear technology: once the Type I/II structural alternative is available, the bottleneck is the analytic estimate, not the lack of convolution depth.

Therefore

`GROWING_HB_DEPTH + EXISTING_TYPE_I/II != RH`.

Any actual improvement must exploit information that fixed bilinear treatment discards, e.g. multi-branch provenance or a stronger multilinear/global cancellation estimate.

---

## 10. Current frontier

The growing-depth identity gives the clearest current Enterprise realization of

`X6 FIXED WIDTH + SCALE-GROWING BRC PROVENANCE DEPTH`.

At the RH-critical scale it exactly uses:

`small-prime cutoff y=(log X)^2`,

`depth K~(1/2)log X/loglog X`,

`outer coefficient cost X^o(1)`.

But positive absolute analysis is blocked at sigma=1.

Next admissible research question:

Can one identify a signed/PSD cross-branch Gram or operation-safe provenance transform for the K branches that preserves their necessary cancellation without taking absolute values branchwise, and that is not merely a restatement of `1/zeta`?
