# R005-A — Prime-Gap Duality and Cross-Dimension External Evidence Bridge

Status: `PROVED R005 STRUCTURE + EXACT LOCAL CERTIFICATE + EXTERNAL-COMPUTATION TRANSFER / NOT CANONICAL / LEAN PENDING`  
Date: `2026-08-10`  
Track: `R005-A — Enterprise Prime Algorithm Lab`  
Cross-route inputs: `R005-B p-power basin / factor-screen horizon`

---

# 1. Executive result

The p=3 / p=4 frontier has now split into three distinct layers:

1. **prime-anchor existence** — does the basin contain a true prime?
2. **least witness language** — does the forced core already cover every composite?
3. **full forcing saturation** — is every candidate divisor witness mandatory?

These layers must not be identified.

Current certified frontiers are:

## p=3

- exact/internal + explicit-short-interval + exact local prime-gap certificate:
  \[
  2\le k\le 500000;
  \]
- after transferring the double-checked external prime-gap computation:
  \[
  \boxed{2\le k\le 4{,}104{,}076}
  \]
  for existence of a **unique least safe divisor-witness basis**;
- independently, the 2026 consecutive-cubes computation supplies a genuine
  **prime anchor** through
  \[
  \boxed{k\le 25{,}453{,}072{,}734{,}831}.
  \]

The prime-anchor range is vastly larger than the least-basis range.  This is
exactly the logical separation required by the earlier prime-anchor theorem.

## p=4

- external double-checked gap transfer alone gives unique least basis through
  \[
  k\le5{,}472{,}101;
  \]
- the stronger finite Legendre/Oppermann transport gives
  \[
  \boxed{k\le9{,}985{,}091}
  \]
  with the stronger conclusion that **every candidate divisor witness is
  forced**.

Hence for p=4 through that range,

\[
\boxed{
\text{unique least basis}
=
\{\text{all primes }q\le (k+1)^2-1\}.
}
\]

None of the next integers after these endpoints is asserted to be a
counterexample.  They are only the first points not covered by the stated
external certificate.

---

# 2. T-A16 — prime-gap duality

Fix one p-power basin

\[
A=k^p,\qquad U=(k+1)^p-1.
\]

Let \(q\) be a candidate divisor witness and consider only the e=1 cofactor
route.

Put

\[
x=\frac Aq.
\]

Let

\[
a<b
\]

be the consecutive primes satisfying

\[
a<x<b.
\]

Then witness \(q\) fails to obtain an e=1 exclusive-collision certificate
exactly when

\[
b>\frac Uq.
\]

Using \(a<A/q\), this can be rewritten as the reciprocal prime-gap condition

\[
\boxed{
\frac Ub < q \le \frac Aa.
}
\]

Thus:

> an e=1 non-forcing candidate witness is a **prime q captured by the reciprocal
> image of a consecutive cofactor-prime gap**.

For this reciprocal interval to be nonempty one must have

\[
\frac Ub < \frac Aa,
\]

equivalently

\[
\boxed{
\frac ba>\frac UA.
}
\]

So an e=1 failure requires a cofactor-prime **relative gap larger than the
relative width of the original p-power basin**.

This is an exact arithmetic duality, not a heuristic analogy.

It changes the efficient search variable:

`scan all q`
→ `scan only sufficiently large consecutive cofactor-prime gaps`
→ `inspect whether the reciprocal gap interval contains a prime q`.

A fully non-forced witness must in addition fail every higher-power
\(q^e\) certificate, so the prime-gap duality supplies a necessary condition
and an exact e=1 characterization, not by itself the full forcedness
classification.

---

# 3. Exact local use of the duality: p=3 to k=500000

The preceding Axler-based uniform certificate stopped at

\[
k=494034.
\]

Instead of testing every witness for every subsequent basin, the duality lets
us sieve one broad cofactor interval.

For

\[
494035\le k\le500000,
\]

the union of all Axler-uncertified cofactor bands is contained in

\[
491077748
\le x\le
532097503.
\]

An exact segmented Eratosthenes sieve over that interval found:

- primes inside the interval: **2,044,894**;
- predecessor prime: **491,077,739**;
- successor prime: **532,097,507**;
- largest absolute consecutive-prime gap in the certificate interval:
  \[
  250,
  \]
  between
  \[
  516540163,\ 516540413;
  \]
- largest relative gap:
  \[
  \frac{250}{516540163}
  \approx4.8399\times10^{-7}.
  \]

At the worst basin endpoint \(k=500000\),

\[
\frac UA-1
=
0.000006000012.
\]

Thus every exact cofactor-prime relative gap is more than an order of magnitude
below the allowed basin width.

Therefore every p=3 danger witness is forced for every

\[
494035\le k\le500000.
\]

Combined with the prior chain:

\[
\boxed{
2\le k\le500000
}
\]

is now certified without relying on an external large prime-gap database.

---

# 4. External prime-gap computation transfer

Tomás Oliveira e Silva's prime-gap project reports that:

1. gaps between **all primes below \(4\cdot10^{18}\)** were computed;
2. the computation was independently double-checked through
   \[
   4\cdot10^{17};
   \]
3. its top-gap table shows that every gap larger than 1328 has first
   occurrence above \(4\cdot10^{17}\), while gap 1328 already occurs below
   that boundary.

Accordingly this checkpoint uses the external computational premise

\[
\boxed{
g\le1328
\quad\text{for consecutive-prime gaps in the double-checked region below }
4\cdot10^{17}.
}
\]

This is deliberately classified as an **external computation premise**, not a
new analytic prime-gap theorem and not an Enterprise Math proof of the source
computation.

## Transfer condition

For a danger cofactor point \(x=A/q\), let \(a<b\) be the surrounding primes.

If \(b-a\le G\), then

\[
a>x-G.
\]

Since every danger cofactor point obeys

\[
x\ge L_p(k)
=
\frac{\sqrt2\,k^p}{\sqrt{(k+1)^p-1}},
\]

it is enough to have

\[
\boxed{
G\le
u_p(k)\bigl(L_p(k)-G\bigr).
}
\]

For \(G=1328\), this has a huge positive margin already at the beginning of the
external-transfer ranges and becomes easier as k grows.

The remaining endpoint is therefore not controlled by relative-gap size.  It
is controlled by whether the Axler-uncertified cofactor crossover
\(x_{\rm crit}(k)\) remains inside the \(4\cdot10^{17}\) external
double-check region.

---

# 5. p=3 external gap transfer

Starting after the exact local certificate at

\[
k=500001,
\]

the downstream arithmetic check gives:

\[
x_{\rm crit}(4{,}104{,}076)+1328
<
4\cdot10^{17},
\]

whereas the next k crosses that selected external boundary.

The conservative relative-gap margin

\[
u_3(k)(L_3(k)-1328)-1328
\]

is already approximately

\[
1671.99
\]

at the start of the transfer and grows thereafter.

Therefore, under the external double-checked gap premise,

\[
\boxed{
\forall\,2\le k\le4{,}104{,}076,
}
\]

the p=3 basin divisor-witness language has a **unique least safe basis**.

Again,

\[
k=4{,}104{,}077
\]

is not a counterexample.  It is merely the first k whose Axler-uncertified
crossover leaves the chosen external double-check range.

---

# 6. p=4 external gap transfer

The same transfer gives, before using Legendre:

\[
\boxed{
2\le k\le5{,}472{,}101
}
\]

for unique least divisor-witness basis.

The relative-gap inequality is vastly noncritical here: at the beginning of
this external-transfer range its conservative margin already exceeds
\(1.18\times10^7\).

This is superseded below by a stronger p=4-specific dimension transport.

---

# 7. T-A17 — finite Legendre verification transports to p=4 full forcing

For the fourth-power basin,

\[
k^4<n<(k+1)^4,
\]

the exact factor horizon is

\[
F=(k+1)^2-1.
\]

Take any candidate prime witness \(q\le F\).

## Case I — q>k^2

Then

\[
k^4<q^2\le F^2<(k+1)^4.
\]

So \(q^2\) itself is an exclusive collision.

## Case II — q<=k^2

Define

\[
x=\frac{k^2}{\sqrt q},
\qquad
t=\max\left(k+1,\lfloor x\rfloor+1\right).
\]

If there is a prime

\[
t^2<r<(t+1)^2,
\]

then \(r>F\).

Also \(t>x\), so

\[
qr>k^4.
\]

For the upper side:

- if \(t=k+1\), then
  \[
  \sqrt q\,(t+1)\le k(k+2)<(k+1)^2;
  \]
- otherwise \(t+1\le x+2\), so
  \[
  \sqrt q\,(t+1)
  \le k^2+2\sqrt q
  \le k^2+2k
  <(k+1)^2.
  \]

Hence in both cases

\[
qr<(k+1)^4.
\]

Thus \(qr\) is an exclusive collision for q.

So a finite verified Legendre range for all \(t\le N\) forces every p=4
candidate witness whenever the largest possible t remains below N.

The largest t occurs at \(q=2\):

\[
\boxed{
t_{\max}(k)
=
\left\lfloor\frac{k^2}{\sqrt2}\right\rfloor+1
=
\left\lfloor\sqrt{\frac{k^4}{2}}\right\rfloor+1.
}
\]

---

# 8. p=4 transport from the 2025 Oppermann computation

Sorenson and Webster report computational verification of Oppermann's
conjecture through

\[
N=7.05\cdot10^{13}.
\]

Oppermann is stronger than the required Legendre statement, so the verified
range supplies a prime between every consecutive pair of squares for all
indices used below.

Solving exactly

\[
t_{\max}(k)\le70{,}500{,}000{,}000{,}000
\]

gives

\[
\boxed{k_{\max}=9{,}985{,}091}.
\]

Exact endpoint values:

\[
t_{\max}(9{,}985{,}091)
=
70{,}499{,}990{,}193{,}121,
\]

while

\[
t_{\max}(9{,}985{,}092)
=
70{,}500{,}004{,}314{,}173.
\]

Therefore, using that external verified range:

\[
\boxed{
\forall\,2\le k\le9{,}985{,}091,
}
\]

**every** p=4 candidate prime witness is forced.

This is stronger than merely having a least basis:

\[
\boxed{
\operatorname{ForcedCore}_{4,k}
=
\{q\text{ prime}:q\le(k+1)^2-1\}.
}
\]

---

# 9. p=3 prime-anchor range from the 2026 cube computation

The 2026 preprint by Johnston, Sorenson, Thomas and Webster reports a
large-scale computation showing a prime between every pair of consecutive
cubes whenever

\[
n^3\le1.649\cdot10^{40}.
\]

The largest integer n satisfying that published numerical bound is

\[
\boxed{
n=25{,}453{,}072{,}734{,}831.
}
\]

Therefore the p=3 basin has an externally computed **prime anchor** throughout

\[
\boxed{
k\le25{,}453{,}072{,}734{,}831.
}
\]

This does **not** prove the least-basis property through that range.

Its role is different.

Recall the earlier R005 theorem:

`signature primality-safe -> composite rejection cover`

requires the domain to contain at least one actual prime; without a prime,
kernel safety may be vacuous.

The 2026 computation supplies exactly that missing prime-anchor hypothesis for
the enormous stated finite p=3 range.

Thus the three p=3 statements are now kept separate:

1. prime anchor: very large external finite range;
2. unique least witness basis: currently 4,104,076 under the stated gap
   premise;
3. full forced saturation: false in general even at small k, because p=3
   basins with non-forced candidate witnesses already occur.

This separation is architecturally important.

---

# 10. Almost-prime theorem as an A4 support observation

The same 2026 cube preprint proves unconditionally that for every \(n\ge1\),
there is an integer between consecutive cubes with at most two prime factors,
counting multiplicity.

In R005 divisor-support language this means every p=3 basin contains a state
whose complete prime-factor multiset has size at most two.

For the candidate screening support this supplies a globally existing state of
support arity at most two:

- a prime gives support arity 0;
- a product with only one candidate-small factor gives singleton support and
  therefore a forced witness;
- a product of two candidate-small prime factors gives support arity at most 2.

No claim is made that this state is residual or that it alone establishes a
least basis.

It is nonetheless a natural A4 input: cube basins possess a globally bounded
low-arity arithmetic support witness even beyond the prime-anchor computation.

---

# 11. Structural picture after this checkpoint

The p-power Prime Toolkit now has two independent transfer axes.

## Horizontal: within one p-basin

\[
\text{prime gaps}
\leftrightarrow
\text{reciprocal witness intervals}
\to
\text{forced danger witnesses}
\to
\text{no residual fiber}
\to
\text{least basis}.
\]

## Vertical: between collapse exponents

\[
\text{lower-dimensional prime existence}
\to
\text{higher-dimensional exclusive collisions}
\to
\text{higher-dimensional forced-core saturation}.
\]

p=3 and p=4 now behave visibly differently:

- p=3 can have a proper forced core plus non-forced choices, while still
  retaining a unique least basis over a very large certified range;
- p=4 inherits enough square-gap information that all candidate coordinates
  become mandatory throughout the transported finite range.

So “collapse dimension” changes the **minimal observation language**, not only
the count or geometry of primes.

---

# 12. Evidence/status discipline

## Internal exact / proved R005 structure

- forced/mandatory witness criterion;
- residual hypergraph decomposition;
- danger-radius theorem;
- singleton-support factor classification;
- prime-gap duality;
- local segmented-sieve certificate through p=3 k=500000;
- arithmetic transfer calculations from declared external premises;
- finite Legendre-to-p4 forcing theorem.

## External established / computational inputs

- Dusart 2010, Trudgian, Axler explicit prime-in-short-interval theorems;
- Oliveira e Silva / Herzog / Pardi large prime-gap computation and its
  author-maintained double-check record;
- Sorenson-Webster 2025 finite Oppermann/Legendre verification;
- Johnston-Sorenson-Thomas-Webster 2026 consecutive-cubes computation and
  almost-prime theorem.

## Explicit nonclaims

- no new analytic prime-gap theorem;
- no proof of Legendre's conjecture;
- no proof that p=3 always has a least witness basis;
- no claim that the external computations are reproduced inside Enterprise
  Math;
- no claim that the first integer after a certificate endpoint is a failure;
- no Lean-checked status.

Lean remains:

`LOCAL_LEAN_PENDING`.

---

# 13. Next frontier

The best next questions are now sharply defined.

1. **p=3 gap-reciprocal exceptional set.**  
   Search only consecutive cofactor-prime gaps satisfying
   \[
   b/a>U/A,
   \]
   then test whether
   \[
   (U/b,A/a]
   \]
   contains a prime candidate q.  This is much smaller than witness scanning.

2. **Two-nonforced collision requirement.**  
   A no-least basin needs at least two non-forced witnesses whose product can
   fit below U/2.  Search pairs of reciprocal-gap-generated q values rather
   than all composites.

3. **Consume almost-prime support structure.**  
   Determine whether the global \(\Omega\le2\) cube theorem can constrain the
   residual hypergraph beyond merely supplying a low-arity state.

4. **Formalization.**  
   Once `WitnessCover.lean` actually compiles, formalize:
   - residual edge size >=2;
   - danger-radius theorem;
   - prime-gap reciprocal interval equivalence;
   - finite Legendre-to-p4 forcing transport.

5. **Do not chase cutoff alone.**  
   The next valuable step is a theorem about the exceptional reciprocal-gap
   set, not another undifferentiated full-basin sieve.
