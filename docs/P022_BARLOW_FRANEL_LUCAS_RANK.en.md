# P022 Barlow low-order identifiability: Franel p-Lucas rank layer

Status: `PROVED_WIP + TARGETED_EXECUTABLE_CHECKED`  
Owner: `P022 / program/p022-geometry-v2`  
Scope: global low-order checkpoint identifiability after central-binomial elimination

## 1. Purpose

Write

\[
F_n=\sum_{k=0}^n {n\choose k}^3
\]

for the Franel numbers.  The P022 low-order reduction has already isolated the
pure Franel defects `D_n` at exactly the indices for which `2n-1` is composite.
The remaining global arithmetic question is therefore whether the Franel
sequence supplies enough independent valuation information at those indices.

This note records the p-Lucas/rank layer needed for that question.  It does not
claim novelty for the underlying Lucas, recurrence, midpoint, or reflection
congruences.

## 2. Prior-art boundary

The following ingredients are external prior mathematics.

1. Lucas' binomial theorem gives the Franel digit factorization

   \[
   F_n\equiv\prod_i F_{n_i}\pmod p
   \]

   for the base-`p` digits `n_i`.  Malik--Straub, *Divisibility properties of
   sporadic Apéry-like numbers*, Research in Number Theory 2 (2016), article 5,
   DOI `10.1007/s40993-016-0036-8`, supplies broader Apéry-like Lucas-congruence
   context.  The digit factorization used here is prior art.

2. Jarvis--Verrill, *Supercongruences for the Catalan-Larcombe-French numbers*,
   arXiv:`0905.4187`, Lemma 2.6, prove for every odd prime `p` and
   `0 <= d <= p-1` that

   \[
   F_d\equiv(-8)^dF_{p-1-d}\pmod p.
   \]

   In particular, zero digits are symmetric under `d -> p-1-d`.  Their work
   also supplies the midpoint information used below.

3. The classical Franel recurrence is

   \[
   (n+1)^2F_{n+1}
   =(7n^2+7n+2)F_n+8n^2F_{n-1}.
   \]

   In the single-digit range `0<=n<p`, every recurrence denominator is a
   p-unit.  P022 uses this only as an exact finite-field scanner.

4. Beukers, *p-linear schemes for sequences modulo p^r*, Indagationes
   Mathematicae 35 (2024), 698--707, DOI `10.1016/j.indag.2023.12.003`, gives
   higher-prime-power structure for Franel and related Lucas sequences.  That
   theory is not needed for the mod-`p` statements below but remains relevant
   to primitive valuation multiplicity.

The P022-specific content here is the way these prior ingredients are combined
with the Barlow pure-defect cutoff and with explicit first-zero certificates.

## 3. The complete mod-p zero language

For a prime `p`, define

\[
Z_p=\{d\in\{1,\ldots,p-1\}:F_d\equiv0\pmod p\}.
\]

### Theorem 3.1 — digit-zero characterization

If `n=sum_i n_i p^i` is the base-`p` expansion of `n`, then

\[
\boxed{
 p\mid F_n
 \iff
 \text{at least one digit }n_i\text{ belongs to }Z_p.
}
\]

**Proof.**  Lucas factorization gives

\[
F_n\equiv\prod_i F_{n_i}\pmod p.
\]

Because `F_0=1`, the product vanishes exactly when one nonzero digit factor
vanishes.  This is precisely membership of some digit in `Z_p`.  ∎

### Corollary 3.2 — rank of apparition is a digit

If

\[
r_p=\min\{n>0:p\mid F_n\}
\]

exists, then

\[
\boxed{r_p=\min Z_p<p.}
\]

Consequently, for `n>0`, a prime `p` is a primitive prime divisor of `F_n` if
and only if

\[
\boxed{r_p=n.}
\]

Thus the first-occurrence question is reduced completely to the first zero in
the single-digit window.

### Corollary 3.3 — exact block counts and density-one basin

Let `z_p=|Z_p|`.  In the full block `0 <= N < p^L`, exactly

\[
(p-z_p)^L
\]

indices have `F_N` nonzero modulo `p`, and therefore exactly

\[
p^L-(p-z_p)^L
\]

indices are divisible by `p`.  If `Z_p` is nonempty, the divisible proportion
along these `p`-power blocks tends to one.

Primitive therefore means **first appearance**, never permanent privacy.

## 4. Reflection geometry of the zero alphabet

### Theorem 4.1 — reflected zero set

For every odd prime `p`,

\[
\boxed{d\in Z_p\iff p-1-d\in Z_p.}
\]

This is the zero-set form of the Jarvis--Verrill reflection congruence.

### Corollary 4.2 — half-prime rank bound

Whenever `r_p` exists for an odd prime `p`,

\[
\boxed{r_p\le\frac{p-1}{2}.}
\]

Reflection sends the first zero `r_p` to another zero `p-1-r_p`; minimality
gives `r_p<=p-1-r_p`.

### Corollary 4.3 — strengthened primitive-prime bound

If an odd prime `p` is primitive at `F_n`, then `r_p=n`, hence

\[
\boxed{p\ge2n+1.}
\]

The only even primitive case is `p=2` at `F_1`.

This separates primitive Franel pivots from the already-solved
central-binomial layer: through segment `n`, the latter uses primes at most
`2n-1`, whereas an odd primitive Franel prime lies at or beyond `2n+1`.

### Corollary 4.4 — reflected reappearance dichotomy

Let an odd prime `p` be primitive at `F_n`.

If

\[
p>2n+1,
\]

then reflection gives a **distinct** later single-digit zero

\[
\boxed{p-1-n\in Z_p},
\qquad
n<p-1-n<p.
\]

Hence the prime necessarily reappears before the base-`p` digit boundary.
In particular,

\[
p-1-n<n+p.
\]

If instead

\[
p=2n+1,
\]

then `n=(p-1)/2` is the self-reflected midpoint, so reflection gives no
distinct one-digit companion.  The p-Lucas index `n+p` is still a canonical
later reappearance, but it should not be called the earliest reappearance
without additional information.

Thus the earlier statement “primitive markers are not permanently private” can
be sharpened: every off-midpoint primitive marker already has a forced
single-digit reflected return.

### Corollary 4.5 — zero-alphabet parity

All non-midpoint zeros occur in reflected pairs.  The midpoint is a zero
exactly in the prior-art classes `p=5,7 mod 8`.  Therefore

\[
\boxed{
z_p\equiv
\begin{cases}
1\pmod2,&p\equiv5,7\pmod8,\\
0\pmod2,&p\equiv1,3\pmod8.
\end{cases}
}
\]

This is a bookkeeping consequence of reflection plus the midpoint criterion,
not a new independent congruence.

## 5. Minimal reflected basins can certify primitivity

Put

\[
m=\frac{p-1}{2}
\]

and let `d<m` satisfy `d in Z_p`.

If `d` were not primitive, there would be another zero `r<d`.  Reflection
would then force the four distinct off-midpoint zeros

\[
r,\ d,\ p-1-d,\ p-1-r.
\]

If the midpoint is also forced, `m` contributes a fifth zero.

Hence:

\[
\boxed{
\begin{array}{ll}
p\equiv1,3\pmod8,\ z_p=2
&\Longrightarrow \text{the unique left-half zero is }r_p,\\[2mm]
p\equiv5,7\pmod8,\ z_p=3
&\Longrightarrow \text{the unique non-midpoint left-half zero is }r_p.
\end{array}
}
\]

Equivalently, a nonprimitive below-midpoint zero forces at least four zero
digits in the non-midpoint classes and at least five in the midpoint classes.

This gives a global-zero-set certificate for primitivity without factoring all
earlier Franel integers.

## 6. Exact large-marker zero alphabets

The recurrence scanner gives the following complete single-digit zero sets:

\[
\boxed{Z_{176459}=\{12,176446\}},
\]

\[
\boxed{Z_{73589}=\{66,36794,73522\}},
\]

and

\[
\boxed{Z_{95257}=\{67,40129,55127,95189\}}.
\]

Consequently

\[
r_{176459}=12,\qquad
r_{73589}=66,\qquad
r_{95257}=67.
\]

The first two are also minimal-basin cases from Section 5:

- `176459=3 mod 8` has the minimal even alphabet `z_p=2`;
- `73589=5 mod 8` has one reflected pair plus the forced midpoint,
  so `z_p=3`.

Their finite privacy through segment 150 is therefore now globally
reinterpreted.  They are genuinely primitive at ranks 12 and 66, but they
cannot stay private:

\[
176459\mid F_{176446},
\qquad
73589\mid F_{73522}.
\]

The explicit `n+p` Lucas returns occur still later.

The third line corrects an important narrative point:

\[
\boxed{95257\text{ is a primitive prime divisor of }F_{67}.}
\]

Thus segment `67` is **not** an example of a Franel term with no primitive
prime divisor.  What the finite global decoder at that segment demonstrates is
only that a successful decoder need not choose a local primitive row even when
one exists.

## 7. Direct consequence for the Barlow pure-defect layer

At a composite boundary `2n-1`, the central-binomial coordinate `A_n` has a
triangular multiplicative expression in earlier `A_j`, and the resulting pure
Franel defect has the form

\[
D_n=F_n\prod_{j<n}F_j^{-\alpha_{n,j}}.
\]

Suppose `p` is primitive at `F_n`.  Then every earlier `F_j`, `j<n`, has
`v_p(F_j)=0`, so

\[
\boxed{v_p(D_n)=v_p(F_n)>0.}
\]

For every earlier defect `D_m`, `m<n`, all Franel factors occurring in its
triangular definition also have index `<n`, hence

\[
\boxed{v_p(D_m)=0.}
\]

Thus primitive rows, ordered by first-zero indices, give a triangular
valuation certificate.  Its diagonal entries are the primitive valuations
`v_p(F_n)`.  If each selected primitive valuation is one, the finite prefix
certificate is unimodular rather than merely rationally full rank.

The separate successor-capture theorem further weakens the sufficient
hypothesis: a primitive event at a prime-boundary rank may be consumed by the
next composite defect.  The global object is therefore a capture map from
first-zero events to defect columns, not a one-to-one local pivot assignment.

## 8. Midpoint divisibility is not primitive divisibility

Jarvis--Verrill's results imply the prior-art midpoint criterion

\[
\boxed{
 p\mid F_{(p-1)/2}
 \iff
 p\equiv5\text{ or }7\pmod8
}
\]

for odd primes `p`.

This supplies a large structured source of Franel divisibility, but it does
not solve the primitive-rank problem.  For example,

\[
Z_{29}=\{12,14,16\},
\]

so `29 | F_14` at the midpoint while `r_29=12`.

The exact midpoint primitivity criterion in the companion zero-geometry note
is `Z_p={m}`.  Midpoint congruences must therefore not be promoted into a
primitive-divisor theorem.

## 9. Executable rank scanner

`src/enterprise_math/p022_barlow_franel_lucas_rank.py` now computes the full
single-digit residue table modulo `p` using the classical second-order Franel
recurrence.  It no longer constructs exact `F_d` for every `d<p` merely to
find `Z_p`.

The module packages:

- `F_0=1` as the Lucas unit;
- independent Lucas-factorization checks on small values;
- recurrence-based digit tables and rank extraction;
- reflection and the half-prime rank bound;
- zero-alphabet parity;
- the reflected reappearance dichotomy;
- exact block counts and density-one basins;
- the strengthened `p>=2n+1` primitive-divisor necessity.

The tests retain an independent direct `sum(comb(n,k)^3)` oracle for small
primes and separately lock the three large zero alphabets above.

## 10. Global question after this compression

The strongest easy primitive sufficient condition is still:

> for every relevant composite-boundary index `n`, find a prime `p` with
> `r_p=n`.

But that is no longer the only useful formulation.  Existing P022 results
already show:

1. infinitely many primitive Franel events occur;
2. primitive events can be captured at their own defect or one step later,
   except for the identified twin-prime deferral geometry;
3. returning/global valuation rows can contribute even after their first
   appearance.

So the real infinite frontier is:

\[
\boxed{
\text{Do first-zero events, successor capture, and returning rows together
generate the full infinite defect valuation lattice?}
}
\]

A proof that an infinite relevant subfamily receives simple primitive pivots
would already be the first genuine infinite theorem family beyond the
finite `N=150` certificate.  A genuine index with no primitive divisor would
show only that the primitive route is sufficient rather than universal; no
such P022 example has yet been established.
