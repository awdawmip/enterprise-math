# BRC Precision-Deficit Window Wall Frontier

Status: `RESEARCH FRONTIER / EXACT WINDOW ACTIVATION + CROSS-ROUTE SCALE SYNTHESIS + COMPLEXITY BENCHMARK / NO SPEEDUP CLAIM`
Date: `2026-09-08`
Parent: `research_notes/BRC_GCD_DIVISOR_LATTICE_QUOTIENT_FRONTIER_20260908.md`
Source snapshot before write: `main@d5e5e32607fe2bbd2cab415fb5a47dd43ee7c32c`

## 0. Goal

The parent note identified a constant-size operation-safe gcd carrier but left its constructor expensive. This continuation asks how the activation cost changes if another N-only or conditional observer has already narrowed the least factor to a bracket.

The result is an exact window-binomial activation law and a common precision-deficit coordinate that simultaneously controls:

- the unresolved factor interval;
- the earlier cross-boundary local square-gap offset;
- the generic block-product work needed for activation.

This yields a quantitative benchmark for how much new factor-ratio information a BRC preconditioner would need before the valuation-wall route becomes asymptotically competitive with modern deterministic factoring.

---

## 1. Exact window-binomial activation theorem

Let

`N=pq`, `p<q` primes.

Suppose public integers satisfy

`0<=L<p`,

`L<U<q`,

and put

`H=U-L`.

Assume `H<p`.

Define the integer binomial window

`W_(L,U)=C(U,H)`.

Using the product form

`W_(L,U)=prod_(j=1)^H (L+j)/j`,

all denominators `j<=H<p<q` are units modulo `N`.

The numerator factors are exactly the consecutive interval

`L+1,...,U`.

Because `L<p` and `U<q`, this interval can contain no hidden prime other than `p`. Therefore

`gcd(W_(L,U),N)=1` if `p>U`,

and

`gcd(W_(L,U),N)=p` if `p<=U`.

Equivalently, under the public lower-bracket invariant `L<p`, one exact binomial coefficient is a threshold query for the upper endpoint `U` and returns the factor on success.

This is an exact N-only activation law once `(L,U)` are chosen from public/prior observations; no hidden factor is used in its construction.

---

## 2. Why the binomial form matters

The parent block state used

`prod_(n=L+1)^U n`.

The binomial quotient divides out the public factor `H!`, which is guaranteed to be a unit modulo `N` under `H<p`. Hence it preserves the gcd state exactly while exposing a first-order short recurrence

`B_0=1`,

`B_j=B_(j-1)*(L+j)/j`, `1<=j<=H`.

So after a bracket has been established, the arithmetic horizon is the **unresolved width `H`**, not the absolute factor location `p`.

This is a real cross-scale reuse law. A negative threshold certificate can advance `L`; the next wall need only cover the remaining unresolved interval rather than replay the entire prefix.

---

## 3. Adaptive halving costs only the first unresolved width

Suppose a block evaluator has cost

`T(H)=H^alpha * polylog(N)`

for a bracket of width `H`, with `alpha>0`.

If each negative query halves the unresolved interval, the total work is bounded by

`sum_(j>=0) T(H/2^j) = O(T(H))`

up to a constant depending on `alpha` and logarithmic factors.

Hence adaptivity does not multiply the leading power cost by the number of comparison bits. It is enough to understand the cost at the initial unresolved width.

For a generic baby-step/giant-step / fast product evaluator with `alpha=1/2`, the complete adaptive threshold search remains square-root-in-initial-width.

---

## 4. Ratio precision maps linearly to factor-bracket width

Let

`R=q/p>1`.

Then

`p=sqrt(N/R)`.

Assume a bounded RSA-type ratio band `1<R<=C`, and suppose another observer gives

`R in [R_-,R_+]`

with width

`delta=R_+-R_-`.

The induced factor bracket is

`p in [sqrt(N/R_+), sqrt(N/R_-)]`.

By the mean value theorem for `f(R)=sqrt(N/R)`,

`|f'(R)|=sqrt(N)/(2 R^(3/2))=p/(2R)`.

On a fixed bounded ratio band this gives

`H = Theta(p*delta)`.

Thus the natural precision-deficit coordinate is

`Lambda = p*delta`,

up to constants depending only on the declared ratio band.

Freeze:

`RATIO_UNCERTAINTY delta -> FACTOR_WINDOW Lambda=Theta(p delta)`.

---

## 5. Same precision deficit appeared in the collision geometry

The parent collision-order note studied a common-offset attempt to realize a comparison with local square-gap scans. If the current ratio estimate has error `delta`, optimizing the common baseline gave a factor-bearing endpoint offset

`Delta_min = Theta(p*|delta|)`.

Therefore the two seemingly different routes share the same defect scale:

`Lambda = Theta(p*delta)`.

- geometric/BRC square-gap route: local factor-bearing offset is `Theta(Lambda)`;
- arithmetic activation route: unresolved factor interval width is `Theta(Lambda)`;
- classical fast block route: generic activation work is approximately `Theta(sqrt(Lambda))` up to multiplication/logarithmic factors.

This is a genuine cross-route synthesis. The quantity controlling both local balancing and interval activation is not `N` directly but the **remaining factor-ratio precision deficit**.

---

## 6. Benchmark against the current deterministic exponent one fifth

For balanced semiprimes

`p=Theta(sqrt(N))`.

A generic square-root-in-window activation algorithm has cost

`sqrt(H)=Theta(sqrt(p*delta))`.

To match an `N^(1/5)` power scale, the initial window must satisfy

`sqrt(H) <= N^(1/5)`.

Equivalently

`H <= N^(2/5) = p^(4/5)`

and hence

`H/p <= p^(-1/5) = N^(-1/10)`.

In ratio language this means a preconditioner must already achieve, up to fixed-band constants,

`delta <= p^(-1/5) = N^(-1/10)`.

Therefore a constant-number-of-bits prior cannot make a square-root block wall asymptotically competitive with exponent one fifth. One needs a **growing** amount of factor-ratio precision.

For an `n`-bit balanced modulus, `N^(-1/10)` corresponds to roughly `n/10` bits of relative ratio localization. For RSA-270 (`n=895`), this benchmark is about 90 bits of genuine magnitude precision, not merely residue information.

This is only a power-law benchmark for this composed route. It is not a lower bound on deterministic factoring and does not claim that 90 known bits are sufficient under every implementation model.

---

## 7. Current RSA-270 information is far below the magnitude benchmark

The durable RSA-270 line conditionally retains construction-family facts such as equal-length factors, fixed leading-bit patterns, and `p,q==2 mod3`, while the collision-local continuation added a small fixed residue refinement.

These remove only a constant amount of entropy / a constant factor from the initial magnitude interval. They do not give an interval of relative width `N^(-1/10)`.

In particular:

- knowing a fixed binary prefix shrinks `H` by a fixed factor;
- knowing fixed congruence classes makes the candidate set arithmetically sparse by a fixed factor but does not shrink its real interval by a growing power;
- knowing `S^2 mod 2880` is a local residue constraint, not a 90-bit archimedean approximation to `S` or `q/p`.

So the current BRC/local-prior package does not precondition the window wall enough to change the classical power exponent.

---

## 8. Window walls with large coefficients are precision consumers, not free precision generators

The tunable multinomial wall from the parent note may seem to move activation to a much smaller index by taking a large coefficient `c`. The window-binomial theorem shows the correct interpretation.

A narrow clean wall of width `H` near the hidden factor can be represented as a binomial ratio with only `H` numerator terms, but choosing that narrow window requires a public lower bound `L<p` already within `H` of the factor.

Thus a large activation coefficient can reduce **work after localization**, but it does not by itself create the required localization. Using a large `c` without a correspondingly precise factor bracket merely moves cancellations/ambiguity into earlier factorial ranges and loses the simple one-factor activation semantics.

Freeze:

`LARGE_WALL_COEFFICIENT = PRECISION_CONSUMER`,

not

`LARGE_WALL_COEFFICIENT = FREE_PRECISION_GENERATOR`.

---

## 9. Revised target for a genuine BRC improvement

There are now two mathematically distinct ways to improve the composed collision/activation route:

### A. Better constructor at fixed precision

Given a width-`H` interval known to contain at most `p`, construct the Boolean/proper-gcd activation state in

`o(sqrt(H))`

work on the same arithmetic model, without reducing to known general factoring machinery.

### B. Better N-only preconditioner

Before the block search, derive a genuine archimedean factor-ratio/factor-location interval of width

`H=o(p)`

at subdominant cost. To become competitive with the exponent-one-fifth benchmark while retaining a square-root block backend, the target is roughly

`H <= p^(4/5-o(1))`.

Residue-only or fixed-prefix information does not satisfy this requirement.

The BRC collision energy/order line is relevant to B only if it yields magnitude/order information, not another fixed local congruence.

---

## 10. Kill conditions

Kill a claimed improvement if:

- the factor bracket width remains `Theta(p)` and only constant factors improve;
- the method obtains a narrow window by inserting hidden factor data or a factor-equivalent boundary;
- a large coefficient merely repackages `Theta(p)` numerator support;
- the block constructor is ordinary BSGS/product-tree/multipoint evaluation in new notation;
- a residue refinement is counted as archimedean bits without an exact interval implication.

Retain work that either proves a sub-square-root window-state constructor or yields a growing-power N-only magnitude localization with a fully accounted construction cost.

No Foundation promotion, Working Truth promotion, or factorization-speedup claim is made.