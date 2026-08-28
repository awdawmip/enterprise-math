# Prime-Coordinate N-only Valuation-Wall GCD Extractor — Harvested Theorem Package

Status: `DRIVER_HARVESTED / AUDITED_RESEARCH_THEOREM_PACKAGE / NO_FOUNDATION_PROMOTION / NO_SPEEDUP_CLAIM`

Date: `2026-08-28`

Source result: `RR-F24971D684C868A325E2`

Source task: `RS-PRIME-COORD-FACTOR-NONLY-VALUATION-WALL-GCD-EXTRACTOR-INDEPENDENT-REPLAY`

Source publication: `TP2-DF186CDB4959BEA10875`

Accepted Driver review: `DR-37DE6540A87C2FC33A4D`

## 1. Purpose of this harvest

This note extracts the reusable mathematics from the accepted PCF4R result without promoting it to Foundation or claiming a factoring speedup.

The key reusable structure is not merely one semiprime factorization recipe. It is a threshold mechanism:

1. a public integer sequence creates a sharp prime-divisibility activation wall;
2. sparse public probes detect the first hidden threshold crossing through `gcd`;
3. a total gcd at first crossing is reinterpreted as a synchronization certificate rather than failure;
4. synchronization bounds the hidden-factor ratio;
5. a second public scale, here `sqrt(N)`, localizes a guaranteed proper split.

The exact PCF4R theorem is one concrete realization of this pattern.

## 2. Exact observable

Define

\[
A_s=\frac{(2s)!(3s)!}{(s!)^5}
=\binom{2s}{s}^2\binom{3s}{s},\qquad A_0=1.
\]

It satisfies the exact recurrence

\[
\boxed{
A_s=A_{s-1}\frac{6(2s-1)(3s-2)(3s-1)}{s^3}
}.
\]

This gives a modular streaming implementation whenever `s` is a unit modulo the working modulus.

## 3. Theorem node V1 — local valuation wall

Let `r>3` be prime and `0<=s<r`. Then

\[
\boxed{
v_r(A_s)=
\left\lfloor\frac{2s}{r}\right\rfloor+
\left\lfloor\frac{3s}{r}\right\rfloor
}.
\]

Hence

\[
\boxed{r\mid A_s\iff 3s\ge r}
\qquad(0\le s<r).
\]

Because a prime `r>3` is not divisible by three, `3s>=r` and `3s>r` are equivalent here.

The exact first activation index is

\[
\boxed{h_r=\left\lceil\frac r3\right\rceil}.
\]

Interpretation: the hidden prime is converted into a public threshold location.

## 4. Theorem node V2 — first dyadic hit dichotomy

Let

\[
N=pq,\qquad 3<p<q
\]

with distinct odd primes. Probe only public dyadic indices

\[
1,2,4,8,\ldots
\]

and let `s` be the first probe with `gcd(A_s,N)>1`.

Let `d` be the least power of two at least `ceil(p/3)`. Since `p=6k-1` or `6k+1`, one has `d<p`. Therefore the first nonunit probe satisfies

\[
\boxed{s<p<q}.
\]

At that seed the local wall applies to both factors, and monotonicity in the hidden prime gives the exact dichotomy

\[
\boxed{\gcd(A_s,N)\in\{p,N\}}.
\]

No factor-labelled seed is used.

## 5. Theorem node V3 — synchronization certificate

Suppose the first nonunit dyadic probe gives the apparently uninformative value

\[
\gcd(A_s,N)=N.
\]

Write `u=s/2` for the preceding dyadic probe. Since the preceding probe is a unit while the current probe activates both factors,

\[
3u<p<q\le 3s=6u.
\]

Thus

\[
\boxed{q<2p}.
\]

This is the synchronization theorem:

> A total gcd at the first activation crossing is not a dead end. It compresses the unknown factor geometry from arbitrary separation to a strict bounded-ratio regime.

## 6. General harvested lemma — activation-wall synchronization ratio

The previous argument does not depend on the factorial form once an exact activation wall is available.

### Activation-Wall Synchronization Lemma

Let `N=pq` with `p<q`. Suppose a public integer-valued sequence `X_s` has, throughout the relevant range, the exact hidden-prime activation law

\[
r\mid X_s\iff cs\ge r
\]

for each `r in {p,q}`, where `c>0` is public.

Let `u<s` be consecutive probes in a public schedule satisfying

\[
s\le\lambda u
\]

for a public `lambda>1`. Assume

\[
\gcd(X_u,N)=1,
\qquad
\gcd(X_s,N)=N.
\]

Then

\[
cu<p,
\qquad
q\le cs\le c\lambda u,
\]

and therefore

\[
\boxed{q<\lambda p}.
\]

For PCF4R, `c=3` and the dyadic schedule has `lambda=2`, recovering `q<2p`.

This lemma is the main theory-level harvest because it separates the reusable synchronization mechanism from the special factorial observable.

## 7. Theorem node V4 — square-root two-seed fallback

Under the synchronized branch `q<2p`, set

\[
t=\left\lfloor\frac{\sqrt N}{3}\right\rfloor.
\]

Since `N` is nonsquare,

\[
3t<\sqrt N<3t+3,
\]

and since `q<2p`,

\[
\sqrt N<\sqrt2\,p<\frac32p.
\]

Hence

\[
\boxed{t+1<p}.
\]

So the local wall is valid at both `t` and `t+1` for both hidden primes.

Also `3t<sqrt(N)<q`, so `q` does not divide `A_t`. Thus

\[
\gcd(A_t,N)\in\{1,p\}.
\]

If it is `p`, extraction is complete. Otherwise `3t<p`. If also `q<=3t+3`, then the two distinct odd primes `p<q`, both greater than three, would have to lie in

\[
3t+1,\quad 3t+2,\quad 3t+3.
\]

Among the first two one is even, while the last is divisible by three. That block cannot contain two distinct odd primes greater than three. Hence

\[
q>3(t+1)>p,
\]

and therefore

\[
\boxed{\gcd(A_{t+1},N)=p}.
\]

Equivalently,

\[
\boxed{
\gcd(A_t,N)=p
\quad\text{or}\quad
\bigl(\gcd(A_t,N)=1\ \text{and}\ \gcd(A_{t+1},N)=p\bigr).
}
\]

## 8. Theorem node V5 — streaming legality

Every modular denominator used before theorem termination is a unit modulo `N`.

The first dyadic stop satisfies `s<p`. In the synchronized fallback, `t+1<p`. Thus every actually inverted index `j` satisfies

\[
1\le j<p<q,
\]

so

\[
\gcd(j,N)=1.
\]

Therefore the recurrence

\[
a_s\equiv a_{s-1}
6(2s-1)(3s-2)(3s-1)(s^3)^{-1}\pmod N
\]

is exact throughout the promised-domain constructor path.

A production implementation should nevertheless test `gcd(s,N)` before inversion; if that gcd is already nontrivial, it is itself a valid factor certificate.

## 9. Theorem node V6 — exact N-only extractor

For every promised input

\[
N=pq,\qquad 3<p<q
\]

with distinct odd primes, the following deterministic public constructor returns a nontrivial factor:

1. stream `A_s mod N` from `s=1` upward;
2. test gcd only at dyadic seeds;
3. if the first nonunit gcd is proper, return it;
4. if it equals `N`, use the two public fallback seeds `floor(sqrt(N)/3)` and `+1` and return the guaranteed proper gcd.

Constructor-side inputs are only `N` and public constants. Hidden `p,q` occur only in the proof of correctness.

Thus

\[
\boxed{\texttt{EXACT_N_ONLY_GCD_EXTRACTOR}}
\]

is an accepted research theorem at this promised-domain strength.

## 10. Complexity boundary

The theorem does not imply a factoring speedup.

The first dyadic stopping index is `Theta(p)` in the worst case, and the current streaming realization requires `O(p)` recurrence updates. With `n=ceil(log2 N)` and multiplication cost `M(n)`, a conservative bit bound is

\[
O(p\,M(n)\log n),
\]

with `O(n)` working memory.

For balanced semiprimes, `p=Theta(sqrt(N))=2^{Theta(n)}`. Therefore

\[
\boxed{
\texttt{EXACT_N_ONLY_GCD_EXTRACTOR}
\ne
\texttt{FACTORIZATION_SPEEDUP}
}.
\]

The active complexity-compression successor remains a separate problem.

## 11. Compatibility with the fixed-prefix no-go

There is no contradiction with the accepted fixed-public-prefix obstruction.

A fixed finite family of public probes has fixed finite prime support. PCF4R escapes that obstruction by allowing the public observable support and the probe range to grow with `N` while remaining factor-blind.

The reusable distinction is:

\[
\boxed{
\text{factor-blind}
\not\Rightarrow
\text{fixed-support}
}
\]

and the positive extractor uses precisely this gap.

## 12. Harvest classification

Theory harvest:

- `LOCAL_VALUATION_WALL_THEOREM`;
- `FIRST_DYADIC_HIT_DICHOTOMY`;
- `ACTIVATION_WALL_SYNCHRONIZATION_RATIO_LEMMA`;
- `SQUARE_ROOT_TWO_SEED_FALLBACK_THEOREM`;
- `STREAMING_DENOMINATOR_UNIT_THEOREM`;
- `EXACT_N_ONLY_GCD_EXTRACTOR_THEOREM`.

Tooling consequence:

- admit a domain operator under `T1_SCALE_ENUMERATION_VALUATION`;
- do **not** create a new top-level global tool family;
- do **not** infer Foundation status, Working Truth promotion, polynomial-time factoring, or novelty against external literature.
