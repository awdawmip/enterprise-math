# P017 — c=103/20 T1–T2 Low-Pair Canonical Hard-Suffix Factorization

Status: `PROVED_WIP UNIQUE THREE-TYPE HARD FACTORIZATION / MONOTONE BOUNDARIES STILL OPEN / NOT CANONICAL / NO FINITE P2 CLAIM`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_C515_T12_P37_ANCHOR_AND_BN_SPLIT_20260827.md`;
- `docs/P017_P2_C515_T12_HIGH_PAIR_POINTWISE_ABSORPTION_20260827.md`;
- `docs/P017_P2_C515_T12_SUBROOT_ROSSER_CANONICAL_CARRIER_20260827.md`;
- the beta-2 upper Rosser support condition.

Purpose: replace the generic well-factorable existence statement on the surviving low-pair sector by a unique deterministic factorization of the P(37)-stripped hard Rosser modulus onto the exact c515 long/short scales.

---

## 1. Surviving low-pair carrier

After super-root and high-pair pointwise absorption, every ordered pair requiring analytic treatment satisfies

\[
z\le r<D^{73/240},\qquad r<p,\qquad rp<B,
\]

where

\[
B=D^{31/40}=x^{31/72}.
\]

Put

\[
\boxed{D_1=\frac{B}{rp}>1}
\]

and

\[
\boxed{N_0=\frac DB=D^{9/40}=x^{1/8}=W^{1/4}.}
\]

Then the inner upper-sieve level is exactly

\[
\boxed{Q(r,p)=\frac D{rp}=D_1N_0.}
\tag{F1}
\]

At the Tier-A splice,

\[
23^3<N_0<29^3,
\]

and in particular

\[
\boxed{41^3>N_0.}
\tag{F2}
\]

---

## 2. P(37)-stripped hard modulus inherits the Rosser constraints

Write a supported upper-Rosser modulus as

\[
d=e b,\qquad e=(d,P(37)),
\]

where every prime factor of `e` is at most 37 and every prime factor of `b` is at least 41.

Write

\[
b=q_1q_2\cdots q_s,
\qquad q_1>q_2>\cdots>q_s\ge41.
\]

Because all hard primes precede all anchor primes in the descending factor order, the positions `1,...,s` are unchanged when passing from `d` to `b`. Hence every odd-position Rosser inequality for `b` is inherited from the full support condition. Define

\[
q_{\rm crit}(b)
=
\max_{\substack{1\le j\le s\\j\text{ odd}}}
q_1\cdots q_{j-1}q_j^3,
\]

with `q_crit(1)=1`. Then

\[
\boxed{q_{\rm crit}(b)<Q=D_1N_0.}
\tag{F3}
\]

---

## 3. Unique greedy short suffix

Define the short hard suffix `b_2` deterministically.

If `s=0`, set

\[
b_1=b_2=1.
\]

For `s>=1`:

1. if `q_s>N_0`, set
   \[
   b_2=1;
   \]
2. if `q_s\le N_0` and either `s=1` or `q_{s-1}q_s>N_0`, set
   \[
   b_2=q_s;
   \]
3. if `s>=2` and `q_{s-1}q_s\le N_0`, set
   \[
   b_2=q_{s-1}q_s.
   \]

Finally put

\[
\boxed{b_1=b/b_2.}
\tag{F4}
\]

This rule is unique and by construction

\[
\boxed{b_2\le N_0.}
\tag{F5}
\]

Because every hard prime is at least 41 and `41^3>N_0`, no product of three hard primes can lie below `N_0`. Thus the rule extracts the maximal possible hard suffix under the short-scale ceiling.

---

## 4. Long factor always lies below D1

We prove

\[
\boxed{b_1<D_1}
\tag{F6}
\]

case by case using only (F3).

### Type 0: b2=1

Here `q_s>N_0`.

If `s` is odd, the final odd-position constraint gives

\[
bq_s^2<D_1N_0.
\]

Since `q_s^2>N_0`,

\[
b<D_1.
\]

If `s` is even, the last odd position is `s-1`, giving

\[
b\frac{q_{s-1}^2}{q_s}<D_1N_0.
\]

But `q_{s-1}>q_s>N_0`, so

\[
\frac{q_{s-1}^2}{q_s}>q_{s-1}>N_0,
\]

and again `b<D_1`.

### Type 1: b2=q_s

Here

\[
q_s\le N_0,
\]

and for `s>=2`,

\[
q_{s-1}q_s>N_0.
\]

If `s` is odd, the final Rosser inequality gives

\[
bq_s^2<D_1N_0.
\]

Thus

\[
\frac b{q_s}
<
D_1\frac{N_0}{q_s^3}
<D_1
\]

by `q_s>=41` and (F2).

If `s` is even, the `s-1` constraint gives

\[
\frac b{q_s}q_{s-1}^2<D_1N_0.
\]

Since

\[
q_{s-1}^2>q_{s-1}q_s>N_0,
\]

we obtain `b/q_s<D_1`.

The case `s=1` is included in the odd argument.

### Type 2: b2=q_{s-1}q_s

Here

\[
q_{s-1}q_s\le N_0.
\]

If `s` is even, the `s-1` Rosser inequality is

\[
\frac b{q_{s-1}q_s}q_{s-1}^3<D_1N_0.
\]

Since `q_{s-1}^3>N_0`, this gives

\[
\frac b{q_{s-1}q_s}<D_1.
\]

If `s` is odd, the final odd-position constraint is

\[
bq_s^2
=
\frac b{q_{s-1}q_s}\,q_{s-1}q_s^3
<D_1N_0.
\]

Since `q_s^3>N_0`, also `q_{s-1}q_s^3>N_0`, hence again

\[
\frac b{q_{s-1}q_s}<D_1.
\]

This proves (F6) in all cases.

---

## 5. Exact c515 physical factorization

Define

\[
\boxed{M=(rp)b_1,\qquad N=b_2.}
\]

Then from `b_1<D_1=B/(rp)` and `b_2<=N_0`,

\[
\boxed{M<B=x^{31/72},\qquad N\le N_0=x^{1/8}.}
\tag{F7}
\]

Moreover, because `b` is squarefree,

\[
\mu(b)=\mu(b_1)\mu(b_2).
\]

Thus every surviving low-pair hard Rosser state lands canonically on the exact long/short scales used by the c515 Lemma-4 window, with no generic factorization existence theorem and no multiplicity in the choice of hard split.

---

## 6. Honest remaining interface

This theorem does **not** yet turn the full coefficient into one Cartesian product `a_M b_N`.

Two monotone dependencies remain:

1. `N=b_2` is the maximal suffix under `N_0`, so the allowed long hard primes are ordered above the prime factors of `N`;
2. the external larger prime `p` is bounded by the intrinsic endpoint `mathcal P(m)` from the canonical carrier theorem.

In addition, the exact P(37) descent leaves an anchor divisor `e|P(37)` encoded through descended intervals

\[
r_{rpb}(\lfloor K^2/e\rfloor,L_{37}/e).
\]

Therefore the next task is a monotone-domain/anchor aggregation theorem, not a generic Rosser factorization theorem.

No finite P2 theorem, all-K theorem, or canonical promotion is claimed.
