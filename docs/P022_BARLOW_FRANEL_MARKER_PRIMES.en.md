# P022 — Private Franel Marker Primes Read Central-Binomial Relation Coordinates

Status: `ACTIVE RESEARCH NOTE / EXACT FINITE MARKER MECHANISM / PRIOR-ART SENSITIVE`  
Owner: `program/p022-geometry-v2`  
Depends on: central-binomial elimination; Franel defect core saturation  
Cross-route relevance: P011 collision identifiability; adaptive valuation certificate design

## 1. Why the saturation primes looked mysterious

The segment-150 Franel core becomes unimodular after adjoining the two previously unselected valuation rows

\[
v_{73589},
\qquad
v_{176459}.
\]

Their obstruction pairings are

\[
-13311
\qquad\text{and}\qquad
2518,
\]

which are coprime.

At first this looks like another lucky search for large primes.  It is not.

Both primes have a much simpler role in the Franel sequence itself:

\[
oxed{176459\mid F_{12}}
\]

and, among

\[
F_1,\ldots,F_{150},
\]

it divides **no other term**.  Likewise

\[
oxed{73589\mid F_{66}}
\]

and divides no other term through segment 150.

Both divisibilities are simple:

\[
v_{176459}(F_{12})=1,
\qquad
v_{73589}(F_{66})=1.
\]

Moreover

\[
2\cdot12-1=23,
\qquad
2\cdot66-1=131
\]

are prime boundaries.

So these rows are **private Franel markers of prime-boundary segment generators**.

---

## 2. P022-MP01 — private marker definition

Fix a finite horizon `N`.

Call a prime `q` a private Franel marker for index `j` through `N` if

\[
\boxed{
v_q(F_j)=e>0}
\]

and

\[
\boxed{
v_q(F_k)=0
\quad\text{for all }1\le k\le N,\ k\ne j.}
\]

The marker is **simple** when

\[
e=1.
\]

This is a finite-horizon property.  A prime private through `N` may divide a later Franel term beyond `N`.

No infinite primitive-divisor claim is made.

---

## 3. P022-MP02 — marker row equals a relation-coefficient row

Let `j` be a prime-boundary index,

\[
2j-1\text{ prime},
\]

and let `q` be a private marker of `F_j` through horizon `N`, with

\[
v_q(F_j)=e.
\]

Because `j` is a prime-boundary index, there is no pure composite defect `D_j`.

For any composite-boundary index `n<=N`, write its canonical central-binomial relation as

\[
A_n
=
\prod_{k<n}A_k^{\alpha_{n,k}}.
\]

The pure Franel defect is

\[
D_n
=
\frac{F_n}
{\prod_{k<n}F_k^{\alpha_{n,k}}}.
\]

Since `q` divides **only** `F_j` on the entire finite horizon, and `n` itself cannot equal `j`, every other Franel term in this expression has `q`-valuation zero.

Therefore

\[
\boxed{
v_q(D_n)
=-e\,\alpha_{n,j}.}
\]

So a private marker prime does not measure mysterious new Franel arithmetic on the composite defect.  It reads one coordinate of the already known central-binomial elimination relation.

This is the structural explanation of the two saturation rows.

---

## 4. P022-MP03 — the segment-150 saturation rows are private markers

Exact finite divisibility checks give

\[
\boxed{
\{k\le150:176459\mid F_k\}
=\{12\},}
\]

and

\[
\boxed{
\{k\le150:73589\mid F_k\}
=\{66\}.}
\]

Both valuations equal one.

Hence for every composite defect through 150,

\[
\boxed{
v_{176459}(D_n)=-\alpha_{n,12}}
\]

and

\[
\boxed{
v_{73589}(D_n)=-\alpha_{n,66}.}
\]

Thus the two extra rows that kill the historical Smith index are literally two relation-coordinate probes.

---

## 5. P022-MP04 — obstruction pairings need no new Franel factorization once the markers are known

Let

\[
x=(x_n)
\]

be the primitive 40-core obstruction vector.

Then

\[
\begin{aligned}
v_{73589}\cdot x
&=
-\sum_nx_n\alpha_{n,66}\\
&=
\boxed{-13311},
\end{aligned}
\]

and

\[
\begin{aligned}
v_{176459}\cdot x
&=
-\sum_nx_n\alpha_{n,12}\\
&=
\boxed{2518}.
\end{aligned}
\]

So after establishing the two private-marker facts, the saturation pairings can be recomputed **without factoring any composite defect**.  They follow from the integer relation coefficients alone.

The Bézout identity

\[
915(-13311)+4837(2518)=1
\]

then yields the unimodular derived row from the previous saturation theorem.

---

## 6. Why prime-boundary Franel terms still matter after the `A` coordinate is eliminated

The central-binomial reduction says a prime-boundary segment gets its new rational rank from the `A` coordinate, so it produces no `D_j` column.

That does **not** make its Franel number irrelevant.

Its private prime divisors can become exact probes of how later composite `A_n` relations use the earlier prime-boundary generator `A_j`.

So there are two distinct roles:

### At its own index

A prime-boundary segment supplies a new `A` prime pivot.

### At later composite indices

Private Franel markers of that same segment can read the coefficients with which its generator re-enters composite central-binomial relations.

This explains why a row associated to an apparently already-solved prime-boundary segment can later resolve an entangled composite Franel core.

---

## 7. A finite marker-prime strategy

For a fixed cutoff `N`, one possible certificate strategy is now:

1. eliminate all `A` prime directions structurally;
2. form the composite Franel defects;
3. use direct defect primes where available;
4. additionally search prime-boundary Franel terms for private markers;
5. translate those marker rows into exact central-binomial relation-coordinate rows by MP02;
6. test whether the resulting valuation lattice is primitive.

This is more interpretable than selecting arbitrary Franel valuation rows solely by modular determinant search.

The segment-150 certificate demonstrates that marker rows can remove an integer Smith obstruction left by a rationally complete row set.

---

## 8. Global limitation

A finite private marker is not automatically an infinite primitive divisor.

The statements

\[
176459\text{ is private to }F_{12}\text{ through }150
\]

and

\[
73589\text{ is private to }F_{66}\text{ through }150
\]

make no assertion about

\[
F_{151},F_{152},\ldots.
\]

Franel divisibility has established Lucas/congruence structure, and some primes divide no Franel term at all.  A global theorem saying every required segment has an eternally private prime would be a much stronger primitive-divisor statement and is not known here.

Therefore MP02 is a reusable **conditional theorem**; MP03 is a finite exact specialization.

---

## 9. Prior-art boundary

Prime divisibility, valuations and Lucas-type Franel congruence theory are established mathematics.  Existing work studies primes that divide no terms and modular behavior of Apéry-like/Franel sequences.

P022 does not claim a new general primitive-divisor theorem.

The project-specific result is the role of finite private Franel markers as exact coordinate probes for the central-binomial relation lattice created by the Barlow low-order collision problem.

---

## 10. Executable assets

Added:

- `src/enterprise_math/p022_barlow_franel_marker_primes.py`;
- `tests/test_p022_barlow_franel_marker_primes.py`.

The tests recompute Franel divisibility directly through segment 150, verify the two private simple markers, check `v_q(D_n)=-alpha_(n,j)` on every composite defect through 150, and recover the Smith-obstruction pairings from relation coefficients alone.
