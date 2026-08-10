# R005-B — Prime-surplus decomposition and square prime-gap diagonals

Status: `PROVED WIP / DRAFT OWNER SUPPLEMENT / NOT CANONICAL`  
Date: `2026-08-10`  
Program: `R005 — Enterprise Prime Toolkit`  
Track: `B — Prime–Collapse Field Geometry`  
Parent owner record: `docs/R005B_PRIME_COLLAPSE_FIELD_RESULTS_20260810.md`

## 1. Why this supplement exists

The first R005-B checkpoint left the high-degree terms in the exact p-basin
formula as partial-sieve quantities

`Psi_F(k^j)`.

It also left the R005-A/R005-B factor-witness bridge at a generic
observation/fiber level.

Both fronts sharpen substantially.

1. Every width-degree argument `k^j`, not only the previously forced low
   degrees, lies below the **next factor-horizon square**.  Therefore the
   partial-sieve survivor set contains no composite number at all: it consists
   only of `1` and actual primes above the horizon.
2. In square basins, singleton factor-support witnesses along every fixed
   near-horizon diagonal encode a fixed even prime separation exactly.  The
   horizon diagonal itself (`offset=0`) is exactly the twin-prime condition.

These are exact finite integer statements.  They do not prove any unresolved
prime-pair conjecture.

---

## 2. T-B9 — subsquare partial-sieve collapse

Let

`Q_F = product_{ell prime, ell<=F} ell`

and

`Psi_F(N) = sum_{d|Q_F} mu(d) floor(N/d)`.

Equivalently, `Psi_F(N)` counts positive integers at most `N` that are
coprime to every prime at most `F`.

### Theorem B9.1 — below the next horizon square, every nontrivial survivor is prime

Assume

`1 <= N < (F+1)^2`.

Then

`Psi_F(N) = 1 + #{r prime : F < r <= N}`.

### Proof

The integer `1` survives.

Let `m` be any surviving integer with `2<=m<=N`.  If `m` were composite, it
would have a prime divisor `ell<=sqrt(m)`.  Since

`sqrt(m) < F+1`,

that integer prime divisor would satisfy `ell<=F`, contradicting survival.
Thus every surviving `m>1` is prime.  Conversely any prime `r>F` is coprime to
`Q_F` and survives.  This proves the identity.

### Prior-art boundary

This is an elementary square-root-sieve fact.  `Psi_F` is the classical
partial-sieve function usually written `phi(x,a)` after choosing `a=pi(F)`.
Modern prime-counting software such as `primecount` exposes exactly that
classical object.  R005 does **not** claim invention of the partial sieve or of
this elementary subsquare observation.

The R005-specific content begins when this fact is inserted into the exact
collapse-basin degree decomposition below.

---

## 3. T-B9.2 — complete prime-surplus/carry decomposition

For one p-power basin, let

- `A=k^p`,
- `U=(k+1)^p-1`,
- `F=F_p(k)=isqrt(U)`,
- `chi_{p,d}(k)` be the polynomial carry from the parent checkpoint.

For `k>=2`, the parent result gives

`P_p(k) = sum_{j=1}^{p-1} C(p,j) Psi_F(k^j)
          + sum_{d|Q_F} mu(d) chi_{p,d}(k)`.

For every `1<=j<=p-1`,

`k^j <= k^(p-1) < k^p=A<U<(F+1)^2`.

Therefore Theorem B9.1 applies to **every degree**, not merely to
`j<=floor(p/2)`.

Define

`Pi_F(N) = #{r prime : F<r<=N}`

and

`C_p(k) = sum_{d|Q_F} mu(d) chi_{p,d}(k)`.

Then the exact p-basin identity becomes

`P_p(k)
 = (2^p-2)
   + sum_{j=1}^{p-1} C(p,j) Pi_F(k^j)
   + C_p(k)`.

This is the **complete prime-surplus/carry decomposition**.

The constant is exact because

`sum_{j=1}^{p-1} C(p,j)=2^p-2`.

The old low-degree visibility theorem is recovered automatically: whenever
`k^j<=F`, the post-horizon count `Pi_F(k^j)` is zero.

### First specializations

For `p=2`:

`P_2(k)=2+C_2(k)`.

There is no post-horizon degree surplus at all.

For `p=3`:

`P_3(k)=6+3 Pi_F(k^2)+C_3(k)`.

For `p=4`, because `F_4(k)=(k+1)^2-1>k^2`:

`P_4(k)=14+4 Pi_F(k^3)+C_4(k)`.

For `p=5`:

`P_5(k)=30+10 Pi_F(k^3)+5 Pi_F(k^4)+C_5(k)`.

Equivalently, primes in `(F,k^3]` carry total binomial weight `15`, while
primes in `(k^3,k^4]` carry weight `5`.

### Interpretation

The high-degree terms are therefore not an unspecified rough-number
population.  Under the basin horizon they are actual **prime surplus shells**.
The p-dimensional state separates into

`universal binomial baseline + post-horizon prime shells + local Moebius carry`.

This does not make the formula computationally efficient: the naive carry
sum still enumerates the square-free divisors of `Q_F` exponentially.

---

## 4. T-B10 — one-large-prime factor normal form below a basin horizon

The same subsquare bound gives a factor-support normal form.

For every integer `n<=U`, there can be at most one prime factor `r>F`, counted
with multiplicity one.  Indeed two such factors would give

`n >= (F+1)^2 > U`.

After stripping all prime-power factors with prime at most `F`, the remaining
cofactor is therefore either

- `1`, or
- one prime `r>F`.

### Singleton candidate-support corollary

Fix a candidate prime witness `q<=F`.  A basin composite whose candidate
prime-divisor support is exactly `{q}` must have one of the two forms

`q^a`

or

`q^a r`,

where `a>=1` and `r` is a single prime above `F`.

Therefore the arithmetic existence criterion is

`exists a>=2 with A<q^a<=U`

or

`exists a>=1 and prime r>F with A<q^a r<=U`.

Equivalently, in the second branch,

`max(F, A/q^a) < r <= U/q^a`.

This is an exact finite normal form, not a heuristic.

### Ownership boundary

R005-B owns this factor-horizon/factor-support normal form.

R005-A already proved the generic bridge

`singleton rejection support <-> forced/mandatory witness`

inside a full prime-sound divisor-witness universe, together with the residual
hypergraph/least-basis theorem.  This supplement consumes that bridge; it does
not duplicate its generic set-cover or kernel machinery.

---

## 5. T-B11 — fixed-gap square diagonal theorem

This is the strongest new square-specific result in this supplement.

Let

- `h>=0` be a fixed near-horizon offset,
- `q` be an odd prime,
- `q > h^2+2h`,
- `k=q+h`.

The square basin is

`k^2 < n < (k+1)^2`,

and its factor horizon is exactly

`F_2(k)=k=q+h`.

### Theorem B11.1

Under these hypotheses, a square-basin composite with candidate prime-divisor
support exactly `{q}` exists **if and only if**

`q+2h+2`

is prime.

When it exists, the singleton-support composite is uniquely

`n=q(q+2h+2)`.

### Proof

Write

`A=(q+h)^2`,

`U=(q+h+1)^2-1`.

The threshold `q>h^2+2h` gives

`floor(A/q)=q+2h`

and

`floor(U/q)=q+2h+2`.

It also implies `q>h^2`, and hence no pure power `q^a` with `a>=2` lies in the
open basin: `q^2<=A`, while `q^3>U`; any `q^a r` with `a>=2` and `r>F` is even
larger.

By the one-large-prime normal form, the only remaining possibility is

`n=q r`

for a prime `r>F` satisfying

`A/q < r <= U/q`.

The floor identities reduce this to the two integer candidates

`r=q+2h+1`

or

`r=q+2h+2`.

Because `q` is odd, `q+2h+1` is an even integer greater than `2` and is not
prime.  Thus an admissible prime cofactor exists exactly when

`r=q+2h+2`

is prime, and then the certificate is unique.

---

## 6. Twin-prime diagonal as the horizon specialization

Set `h=0`.  Then `k=q`, so `q` is literally the horizon witness of the square
basin.

For every odd prime `q`:

`q is singleton-supported/forced at the horizon of I_{2,q}`

if and only if

`q+2 is prime`.

The explicit forcing certificate, when it exists, is

`q(q+2)`.

Therefore the twin-prime conjecture is exactly equivalent to the following
R005 square-field statement:

> infinitely many prime-coordinate square basins have their horizon witness
> forced.

This is an **equivalent encoding**, not a proof of the twin-prime conjecture.
Twin primes and fixed prime-pair gaps are classical prime-distribution
questions; R005 claims no priority over them.

More generally, put the fixed even separation

`g=2h+2`.

For every odd prime

`q > g^2/4 - 1`,

we have

`q and q+g are both prime`

if and only if the witness

`q = k-(g/2-1)`

has singleton candidate support in the square basin with

`k=q+g/2-1`.

Thus every fixed even prime separation is represented by one fixed diagonal
inside the square `(k,q)` factor-support field.  No claim of consecutiveness of
the two primes is made.

---

## 7. T-B12 — square full-forcing saturation fails infinitely often

The bounded R005-A scan had already found many square basins with non-forced
candidate witnesses.  The horizon diagonal now turns that finite evidence into
an unconditional infinite theorem.

### Lemma

There are infinitely many odd primes `q` for which `q+2` is composite.

### Proof

Assume only finitely many such primes existed.  Then every sufficiently large
prime `q` would have `q+2` prime.  Choose such a prime `q>3`.  The prime `q+2`
is also sufficiently large, so the same assumption would force `q+4` prime.
But among the three odd integers

`q, q+2, q+4`

one is divisible by `3`; since all are greater than `3`, all three cannot be
prime.  Contradiction.

### Corollary B12.1

By Theorem B11.1 with `h=0`, infinitely many prime-coordinate square basins
have a non-forced horizon witness.

Hence there is **no** threshold `K` after which every square basin has its full
candidate divisor-witness set forced.

This is stronger than the earlier bounded observation.

---

## 8. Collapse-exponent forcing phase diagram

Combining this supplement with the already supplied R005-A bridge results gives
a sharper exponent classification.

### p=2 — provable infinite non-saturation

- no lower positive-integer-exponent pure-power inheritance channel;
- zero post-horizon width-degree surplus;
- residual witness-choice hypergraphs occur in exact finite scans;
- full forced-core saturation fails infinitely often by T-B12.

### p=3 — critical unresolved regime

The bounded cross-route atlas found a non-forced witness already at

`k=23, q=109`,

but no basin without a least divisor-witness basis inside the stated finite
bound.  No asymptotic saturation/non-saturation theorem is claimed here.

### p=4 — critical unresolved regime

The bounded cross-route atlas found full forcing throughout its finite range.
The R005-A even-dimension recursion proves that Legendre's conjecture would be
sufficient for fourth-power full forcing, but that implication is one-way and
does not prove either statement.  No unconditional eventual-saturation theorem
is claimed here.

### fixed p>=5 — eventual full saturation from established short-interval theory

R005-A already derived, from the Baker–Harman–Pintz short-interval theorem,
that for every fixed `p>=5` all candidate divisor witnesses are eventually
forced.

Thus the current R005 forcing phase is

`p=2: infinite non-saturation theorem`

`p=3,4: transition cases still open`

`p>=5: eventual saturation theorem`.

This is a structural statement about the R005 divisor-witness language, not a
new prime-gap theorem.

---

## 9. R005-A / R005-B bridge after this supplement

The bridge is now more concrete than generic fiber safety.

R005-B supplies:

`factor horizon`

`-> one-large-prime normal form`

`-> singleton factor-support certificates`

`-> fixed-gap square diagonals`.

R005-A supplies:

`singleton rejection support`

`-> forced/mandatory witness`

`-> forced core`

`-> residual hypergraph`

`-> least/minimal/minimum safe witness languages`.

The common Prime Toolkit interface is therefore not

`test witness = factor witness`.

It is the typed transport

`arithmetic certificate -> rejection support -> mandatory observation state`.

That interface preserves the different owners while making the cross-route
coupling exact.

---

## 10. Prior-art and novelty boundary

Do not claim the following as Enterprise Math inventions:

- the partial sieve `phi(x,a)` / inclusion-exclusion survivor count;
- square-root factor screening;
- twin primes or any fixed even prime-pair conjecture;
- classical small-gap or short-interval prime theory;
- ordinary factorization into prime powers.

Modern primary/context anchors include James Maynard's work on small gaps
between primes and the existing prime-counting literature/software implementing
the classical partial-sieve function.

The R005 candidate contribution being tested is narrower:

1. the exact substitution of the subsquare survivor collapse into the
   p-basin degree/carry decomposition, producing explicit weighted
   post-horizon prime-surplus shells;
2. the one-large-prime normal form as the precise interface between the
   factor horizon and witness support;
3. the fixed-offset square-field equivalence between a singleton/forced
   near-horizon witness and a fixed even prime separation;
4. the resulting unconditional infinite non-saturation theorem for square
   full forcing, contrasted with the already-derived eventual saturation for
   fixed `p>=5`.

External-literature novelty of this packaging remains unverified.  It stays
R005-local and noncanonical.

---

## 11. Executable checkpoint

New owner-local executable surface:

- `src/enterprise_math/prime_collapse_surplus.py`
- `tests/test_prime_collapse_surplus.py`

The module implements:

- exact post-horizon prime counts;
- exact classical Moebius survivor counts for bounded probes;
- the subsquare survivor closed form;
- weighted degree-prime surplus;
- the complete prime-surplus/carry basin count;
- the fixed-gap square certificate `q(q+2h+2)` under the exact theorem
  hypotheses.

The focused regression file checks the subsquare identity, the complete basin
prime-count decomposition, zero square surplus, and the fixed-gap certificate
against an independently enumerated singleton factor-support search on a
bounded integer grid.

No floating-point value is a truth source.

---

## 12. Foundation-feedback candidates

### FF-B4 — subsquare survivor collapse as a factor-horizon interface

Type: `reusable_tool / layering_law`.

Candidate payload:

`N<(F+1)^2 => partial-sieve survivor = {1} union primes above F`,

with the R005-specific consequence that every p-basin width degree decomposes
into an exact post-horizon prime shell plus local carry.

The underlying sieve lemma is classical; only the interface/package should be
a novelty candidate.

### FF-B5 — square fixed-gap forced diagonal

Type: `cross-route invariant / application-local theorem`.

Candidate payload:

for fixed offset `h` and sufficiently large odd prime `q`, the square-basin
near-horizon witness at `k=q+h` is forced exactly when `q+2h+2` is prime.

This should remain R005-local until independent novelty review.

### FF-B6 — exponent forcing phase boundary

Type: `negative boundary / layering law`.

Current payload:

- `p=2`: full forcing fails infinitely often;
- `p>=5`: full forcing is eventually saturated by the existing R005-A/BHP
  argument;
- `p=3,4`: unresolved transition cases.

This is currently the cleanest theorem-level evidence that collapse exponent
changes the structure of the minimal primality-witness language rather than
merely changing a visualization.

---

## 13. Next narrow frontier

Do **not** spend the next cycle merely extending the finite cutoff.

The highest-value questions are now:

1. can `p=3` be proved infinitely non-saturated, or eventually saturated?
2. can `p=4` full forcing be characterized by a lower-dimensional prime-gap
   condition that is closer to an equivalence than the current one-way
   Legendre implication?
3. can the weighted post-horizon prime-surplus shells be transported directly
   into R005-A mandatory-witness counts without duplicating the generic A2/A4
   support machinery?
4. does the square fixed-gap diagonal admit a useful multi-edge residual
   hypergraph formulation for prime constellations beyond pairs?

Those are structural fronts.  Larger raw scans are secondary evidence only.
