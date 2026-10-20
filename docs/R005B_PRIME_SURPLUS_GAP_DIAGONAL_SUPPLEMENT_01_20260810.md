# R005-B — Prime-surplus decomposition, P018 overlap audit, and forcing phase

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

The high-degree front closes exactly: every width-degree argument lies below
the **next factor-horizon square**, so the partial-sieve survivors above `1`
are actual primes, not an unspecified rough-number population.

A second apparent discovery — a fixed-gap square near-horizon forcing theorem —
was independently derived and then checked against current `main`.  The overlap
audit shows that theorem is exactly the already-canonical P018 centered-shell
theorem after a change of coordinates.  It is therefore recorded here as
**consumed prior Enterprise Math structure, not a new R005-B theorem**.

The genuinely new cross-route consequence retained from that overlap is an
infinite non-saturation theorem for the square divisor-witness forced core.

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

that integer prime divisor satisfies `ell<=F`, contradicting survival.  Thus
every surviving `m>1` is prime.  Conversely every prime `r>F` is coprime to
`Q_F` and survives.  This proves the identity.

### Prior-art boundary

This is an elementary square-root-sieve fact.  `Psi_F` is the classical
partial-sieve function usually written `phi(x,a)` after choosing `a=pi(F)`.
R005 does **not** claim invention of the partial sieve or of this elementary
subsquare observation.

The R005-specific content begins when the identity is inserted into the exact
collapse-basin degree/carry decomposition.

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

Then

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

The high-degree terms are not an unspecified rough-number population.  Under
the basin horizon they are actual **prime surplus shells**.  The p-dimensional
count state separates into

`universal binomial baseline + post-horizon prime shells + local Moebius carry`.

This does not make the formula computationally efficient: the naive carry
sum still enumerates the square-free divisors of `Q_F` exponentially.

---

## 4. T-B10 — one-large-prime factor normal form below a basin horizon

The same subsquare bound gives a factor-support normal form.

For every integer `n<=U`, there can be at most one prime factor `r>F`, and its
exponent is one.  Indeed two such factors, or the square of one such factor,
would give

`n >= (F+1)^2 > U`.

After stripping all prime-power factors with prime at most `F`, the remaining
cofactor is therefore either

- `1`, or
- one prime `r>F`.

### Singleton candidate-support corollary

Fix a candidate prime `q<=F`.  A basin composite whose candidate
prime-divisor support is exactly `{q}` must have one of the two forms

`q^a`

or

`q^a r`,

where `a>=1` and `r` is a single prime above `F`.

Thus the arithmetic existence criterion is

`exists a>=2 with A<q^a<=U`

or

`exists a>=1 and prime r>F with A<q^a r<=U`.

Equivalently, in the second branch,

`max(F, A/q^a) < r <= U/q^a`.

This is an exact finite normal form.

### Ownership boundary

R005-B owns the factor-horizon/factor-support normal form.

R005-A already owns the generic bridge from singleton rejection support to a
forced/mandatory witness, plus the forced-core/residual-hypergraph least-basis
machinery.  This supplement consumes that bridge and does not duplicate it.

---

## 5. Overlap correction — the apparent fixed-gap theorem is exactly P018-T71

During this continuation pass the following square statement was independently
derived.

Let `h>=0`, let `q` be an odd prime with

`q>h^2+2h`,

and set `k=q+h`.  Then a square-basin singleton candidate-support state for
`q` exists exactly when

`q+2h+2`

is prime, with product

`q(q+2h+2)`.

This initially looked like a new R005-B fixed-gap diagonal theorem.

It is **not new inside Enterprise Math**.

Set

`c=k+1`,

`r=h+1`,

`p=c-r=q`.

Then

`q+2h+2=c+r`

and

`q(q+2h+2)=(c-r)(c+r)=c^2-r^2`.

For a prime `q`, the integer threshold `q>h^2+2h=r^2-1` is equivalent to the
P018 size range `q>r^2`: equality `q=r^2` cannot occur for a prime `q>=3`.

Canonical P018-T71 already proves precisely

`L_p(k) != empty  iff  c+r is prime`,

and when nonempty

`L_p(k)={(c-r)(c+r)}={c^2-r^2}`.

Therefore the attempted R005-B fixed-gap theorem is a direct coordinate
re-expression of P018-T71 and is **demoted from novelty immediately**.

No duplicate executable API is kept in `prime_collapse_surplus.py` for this
statement.  R005-B should call/consume the P018 centered-shell surface if an
implementation bridge is later needed.

### Why the failed novelty attempt is still useful

The overlap identifies the exact conceptual bridge:

`R005-B near-horizon factor support`

is already the same arithmetic object as

`P018 centered symmetric-prime shell`.

So the correct integration task is not to prove another theorem, but to expose
this existing P018 shell as one boundary face of the R005 Prime Toolkit.

---

## 6. R005-B/P018/R005-A cross-route corollary: twin-prime horizon diagonal

Although the fixed-gap theorem itself is P018 prior project structure, its
forced-witness interpretation yields a useful R005 cross-route specialization.

Take P018-T71 at radius `r=1`.  Then

`c=q+1`, `k=q`, `p=q`,

and for every odd prime `q`:

`L_q(q) != empty  iff  q+2 is prime`,

with shell state

`q(q+2)`.

In the square basin `q^2<n<(q+1)^2`, the right prime `q+2` lies above the
factor horizon `F_2(q)=q`.  Hence this shell state has candidate divisor support
exactly `{q}`.

By the R005-A forced-witness bridge:

`horizon witness q is forced in I_{2,q}`

if and only if

`q+2 is prime`.

Thus the ordinary twin-prime condition is the **horizon-diagonal forced-core
condition** in the R005 square divisor-witness language.

This is an exact equivalent encoding, not a proof of the twin-prime
conjecture.  The prime-pair problem is classical; the R005 content is the typed
transport from the existing P018 shell to the R005-A mandatory-observation
language.

---

## 7. T-B11 — square full-forcing saturation fails infinitely often

The bounded R005-A scan found many square basins with non-forced candidate
witnesses.  The P018/R005-A horizon bridge turns that finite evidence into an
unconditional infinite theorem.

### Lemma

There are infinitely many odd primes `q` for which `q+2` is composite.

### Proof

Assume only finitely many such primes existed.  Then every sufficiently large
prime `q` would have `q+2` prime.  Choose such a prime `q>3`.  The prime `q+2`
is also sufficiently large, so the same assumption forces `q+4` prime.  But
among

`q, q+2, q+4`

one is divisible by `3`; since all three are greater than `3`, they cannot all
be prime.  Contradiction.

### Corollary B11.1

For infinitely many prime basin coordinates `k=q`, the horizon candidate
witness `q` is not forced.

Hence there is **no** threshold `K` after which every square basin has its full
candidate divisor-witness set forced.

This is stronger than the earlier bounded scan and is the first unconditional
asymptotic negative result for the R005 square forced-core saturation question.

Its ingredients are individually classical/P018/R005-A; the result is a
cross-route structural corollary for the Prime Toolkit, not a new prime-gap
theorem.

---

## 8. Collapse-exponent forcing phase diagram

Combining this supplement with the already supplied R005-A bridge results gives
a sharper exponent classification.

### p=2 — provable infinite non-saturation

- factor horizon self-aligns: `F_2(k)=k`;
- zero post-horizon width-degree surplus;
- no lower positive-integer-exponent pure-power inheritance channel;
- residual witness-choice hypergraphs occur in exact finite scans;
- full forced-core saturation fails infinitely often by T-B11.

### p=3 — critical unresolved regime

The bounded cross-route atlas found a non-forced witness at

`k=23, q=109`,

but no basin without a least divisor-witness basis inside the stated finite
bound.  No asymptotic saturation/non-saturation theorem is claimed here.

### p=4 — critical unresolved regime

The bounded cross-route atlas found full forcing throughout its finite range.
The R005-A even-dimension recursion proves that Legendre's conjecture would be
sufficient for fourth-power full forcing, but that implication is one-way and
proves neither converse nor Legendre.  No unconditional eventual-saturation
theorem is claimed here.

### fixed p>=5 — eventual full saturation from established short-interval theory

R005-A already derived, from the Baker–Harman–Pintz short-interval theorem,
that for every fixed `p>=5` all candidate divisor witnesses are eventually
forced.

Thus the current forcing phase is

`p=2: infinite non-saturation theorem`

`p=3,4: transition cases open`

`p>=5: eventual saturation theorem`.

This is a statement about the R005 divisor-witness language, not a new
prime-gap theorem.

---

## 9. Prime Toolkit interface after the overlap audit

The bridge is now more precise and has less duplication.

R005-B supplies:

`p-basin -> factor horizon -> prime-surplus shells -> one-large-prime normal form`.

P018 already supplies:

`near-diagonal factor shell <-> centered symmetric prime pair`.

R005-A supplies:

`factor/test rejection support -> forced/mandatory core -> residual hypergraph
 -> least/minimal/minimum witness languages`.

A2/P023 supplies the generic quotient/kernel sufficiency layer.

The common interface should therefore be

`arithmetic certificate -> typed observation support -> mandatory state
 -> truth-safe quotient`,

not a merged object that erases owner boundaries.

---

## 10. Prior-art and novelty boundary

Do not claim the following as Enterprise Math inventions:

- partial sieve `phi(x,a)` / inclusion-exclusion survivor counts;
- square-root factor screening;
- twin primes or fixed even prime-pair questions;
- classical small-gap or short-interval prime theory;
- ordinary factorization into prime powers.

Do not claim the centered fixed-gap shell as a new R005 result either: the
current main branch already contains it as P018-T71.

The remaining R005-B candidate contribution in this supplement is narrower:

1. exact substitution of the subsquare survivor collapse into the p-basin
   degree/carry decomposition, producing weighted post-horizon prime-surplus
   shells;
2. the one-large-prime horizon normal form as a factor-support interface;
3. the R005-A/P018 cross-route corollary that square full forcing fails
   infinitely often;
4. the resulting exponent forcing phase split `2 / {3,4} / >=5`.

External-literature novelty of this packaging remains unverified.  It stays
R005-local and noncanonical.

---

## 11. Executable checkpoint

New owner-local executable surface:

- `src/enterprise_math/prime_collapse_surplus.py`
- `tests/test_prime_collapse_surplus.py`

The module implements only the nonduplicative R005-B arithmetic surface:

- exact post-horizon prime counts;
- exact classical Moebius survivor counts for bounded probes;
- the subsquare survivor closed form;
- weighted degree-prime surplus;
- the complete prime-surplus/carry basin count.

The focused regression file checks the subsquare identity, verifies that every
width-degree argument lies below the next horizon square, checks the complete
basin prime-count decomposition against direct primality counting, and records
first nonzero surplus examples for `p=3` and `p=4`.

The independently derived fixed-gap executable was removed after the P018
ownership audit rather than being kept as a duplicate API.

No floating-point value is a truth source.

---

## 12. Foundation-feedback candidates

### FF-B4 — factor-horizon prime-surplus decomposition

Type: `reusable_tool / layering_law`.

Candidate payload:

`N<(F+1)^2 => partial-sieve survivor = {1} union primes above F`,

with the R005-specific consequence that every p-basin width degree is exactly
an above-horizon prime shell plus the universal `1`, yielding the complete
`2^p-2 + prime surplus + carry` formula.

The underlying sieve lemma is classical; only the collapse-degree interface is
a candidate for project-specific promotion.

### FF-B5 — P018 shell is the existing near-horizon factor-support owner

Type: `ownership correction / cross-route interface`.

Payload: the independently rediscovered fixed-gap square theorem is exactly
P018-T71 under

`c=k+1`, `r=h+1`, `p=c-r`.

Action: `CONSUME`, not duplicate.

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
2. can `p=4` eventual full forcing be characterized by a lower-dimensional
   prime-existence condition closer to an equivalence than the current one-way
   Legendre implication?
3. can the weighted post-horizon prime-surplus shells give a rigorous lower or
   upper bound on R005-A mandatory-witness counts?
4. can the P018 centered-shell owner be exposed as a stable Prime Toolkit
   adapter without moving or copying the P018 theorem itself?

Those are structural fronts.  Larger raw scans are secondary evidence only.
