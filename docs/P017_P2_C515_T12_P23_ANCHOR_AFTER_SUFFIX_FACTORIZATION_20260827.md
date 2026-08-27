# P017 — c=103/20 T1–T2 P(23) Anchor after Canonical Suffix Factorization

Status: `PROVED_WIP ANCHOR REOPTIMIZATION / P23 PREFERRED / LOW-PAIR AGGREGATION STILL OPEN / NOT CANONICAL`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_C515_T12_LOPAIR_CANONICAL_SUFFIX_FACTORIZATION_20260827.md`;
- `docs/P017_P2_ADAPTIVE_PRIMORIAL_LENGTH_ANCHOR_20260823.md`.

Purpose: re-optimize the global primorial anchor after the hard Rosser modulus has acquired a unique c515 suffix factorization. The former P(37) choice optimized hard-factor depth; the new theorem shows that only the cube threshold above the fixed short scale is load-bearing.

---

## 1. Short-scale threshold

At the Tier-A splice put

\[
K_0=116009280740973308,
\qquad W=K_0+1,
\qquad N_0=W^{1/4}=x^{1/8}.
\]

Exact integer comparison gives

\[
\boxed{23^3<N_0<29^3.}
\tag{P23-1}
\]

The canonical hard-suffix factorization only uses the fact that every residual hard prime `q` satisfies

\[
q^3>N_0.
\]

Therefore it is sufficient to prestrip every prime through 23. The next prime is 29, and (P23-1) gives the required strict cube inequality.

---

## 2. The P(23) anchored interval

Let

\[
\boxed{Q_{23}=P(23)=223092870.}
\]

Choose the largest `Q_23`-multiple below the full basin length:

\[
L_{23}=Q_{23}\left\lfloor\frac{2K_0}{Q_{23}}\right\rfloor.
\]

Exact arithmetic gives

\[
\left\lfloor\frac{2K_0}{Q_{23}}\right\rfloor
=1040008860,
\]

and

\[
\boxed{2K_0-L_{23}=79118416<Q_{23}.}
\tag{P23-2}
\]

Hence

\[
\boxed{
\frac{2K_0-L_{23}}{2K_0}
<3.42\times10^{-10}.
}
\tag{P23-3}
\]

The interval

\[
J_{23}=(K_0^2,K_0^2+L_{23}]
\]

lies inside the square basin and loses a negligible fraction of its length.

Because `Q_23|L_23`, every prime factor through 23 strips exactly from every mixed Rosser modulus by the adaptive anchor identity.

Thus every residual hard Rosser prime is at least

\[
\boxed{29.}
\tag{P23-4}
\]

---

## 3. Hard depth remains finite

For every surviving low-pair state,

\[
Q(r,p)=\frac D{rp}\le D^{2/3}=W^{20/27}.
\]

Exact integer exponentiation gives

\[
29^8<W^{20/27}<29^9.
\]

Therefore every P(23)-stripped hard Rosser modulus satisfies

\[
\boxed{\omega(b)\le8.}
\tag{P23-5}
\]

This is one factor deeper than the P(37) anchor, but the canonical suffix theorem does not require depth seven: its proof uses only the beta-2 odd-position constraints and the cube inequality `q^3>N_0`.

---

## 4. Canonical c515 split survives unchanged

With hard primes now at least 29, (P23-1) supplies exactly the same key input previously furnished by `41^3>N_0`.

Hence the unique three-type short suffix rule remains valid:

\[
b=b_1b_2,
\qquad
b_2\le N_0,
\qquad
b_1<\frac{B}{rp}.
\]

Thus

\[
\boxed{
(rp)b_1<B=x^{31/72},
\qquad
b_2\le x^{1/8}.
}
\tag{P23-6}
\]

No generic well-factorable decomposition is needed to obtain the long/short scale split.

---

## 5. Why P(23) now dominates P(37)

P(37) was preferred before the suffix theorem because it reduced the hard factor depth to seven. After the unique suffix split, that depth reduction is no longer the controlling property.

P(23) has the advantages:

1. relative discarded tail `<3.42e-10`, versus `<7.6e-6` for P(37);
2. only eight odd anchor primes `3,5,7,11,13,17,19,23`, hence at most `2^8=256` anchor-divisor states instead of `2^11=2048`;
3. residual hard primes begin at 29, already enough for `q^3>N_0`;
4. the hard depth remains bounded by eight.

Therefore

\[
\boxed{P(23)\text{ is the preferred current global anchor for the low-pair c515 route}.}
\]

The P(37) theorem remains correct but is superseded as the finite-optimal anchor under the new canonical suffix factorization.

---

## 6. Remaining interface

The residual low-pair coefficient now has:

- one of at most 256 small anchor divisors `e|P(23)`;
- a unique hard split onto `M<B`, `N<=N_0`;
- monotone largest-prime/order constraints;
- a monotone external-prime endpoint.

The next target is to aggregate the 256 descended anchor intervals and the monotone two-variable boundaries without reintroducing a generic factorization multiplicity.

No finite P2 theorem or all-K claim is made here.
