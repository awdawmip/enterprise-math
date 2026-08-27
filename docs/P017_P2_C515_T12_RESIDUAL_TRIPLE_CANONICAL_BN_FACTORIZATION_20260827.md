# P017 — c=103/20 Residual Triple Carrier Canonical B×N Factorization

Status: `PROVED_WIP UNIQUE HARD FACTORIZATION FOR CORRECTED RESIDUAL / SHORT STATE SET FINITE / ANALYTIC AGGREGATION STILL OPEN / NOT CANONICAL`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_C515_T12_RESIDUAL_TRIPLE_VALUATION_LADDER_20260827.md`;
- `docs/P017_P2_C515_T12_LEAST_SHELL_BUDGET_CORRECTION_20260827.md`;
- `docs/P017_P2_C515_T12_P23_ANCHOR_AFTER_SUFFIX_FACTORIZATION_20260827.md`;
- the beta-2 upper Rosser support condition.

Purpose: show that every P(23)-stripped hard Rosser state on the **corrected** residual triple carrier has a unique deterministic factorization onto the exact c515 long/short scales. Generic factorable-decomposition multiplicity is not needed to obtain the analytic split.

---

## 1. c515 scales

Keep

\[
D=x^{5/9},
\qquad
\boxed{B=x^{31/72}=D^{31/40}},
\qquad
\boxed{N_0=x^{1/8}=D^{9/40}}.
\]

Thus

\[
\boxed{D=BN_0.}
\tag{BN1}

At the Tier-A splice,

\[
\lfloor N_0\rfloor=18455
\]

and

\[
\boxed{29^3>N_0.}
\tag{BN2}

---

## 2. Corrected residual prefix

The residual valuation theorem canonically writes every residual ordered-pair occurrence with prefix

\[
\boxed{P_j=r^jqp,}
\tag{BN3}

where

\[
z\le r<q<p,
\qquad 1\le j\le8.
\]

The inner upper-sieve level is

\[
\boxed{Q=\frac{D}{P_j}.}
\tag{BN4}

After the P(23) exact prestrip, write the hard Rosser modulus as

\[
b=q_1\cdots q_s,
\qquad q_1>\cdots>q_s\ge29.
\]

Its odd-position beta-2 support constraints are inherited unchanged.

---

## 3. High-prefix shells have no nontrivial hard Rosser modulus

If

\[
P_j\ge B,
\]

then by (BN1),(BN4)

\[
Q\le\frac DB=N_0.
\]

A nontrivial beta-2 hard state would have largest hard prime `q_1>=29` and must satisfy the first-position condition

\[
q_1^3<Q.
\]

But by (BN2)

\[
q_1^3\ge29^3>N_0\ge Q,
\]

a contradiction. Therefore

\[
\boxed{P_j\ge B\Longrightarrow b=1.}
\tag{BN5}

Thus no hard factorization cost exists on the high-prefix side.

---

## 4. Low-prefix shells admit the unique greedy suffix split

Assume

\[
P_j<B
\]

and put

\[
\boxed{D_1=\frac{B}{P_j}>1.}
\]

Then

\[
Q=\frac{D}{P_j}=D_1N_0.
\tag{BN6}

Apply the deterministic suffix rule to the descending hard primes of `b`:

- if `b=1`, take `b_1=b_2=1`;
- if the smallest hard prime exceeds `N_0`, take `b_2=1`;
- otherwise take the smallest hard prime alone when the product of the two smallest exceeds `N_0`;
- otherwise take the two smallest hard primes.

In every case put

\[
b_1=b/b_2.
\]

Because every hard prime satisfies `q^3>N_0`, the case-by-case beta-2 argument from the canonical suffix theorem applies verbatim with the present prefix `P_j`. It gives

\[
\boxed{b_2\le N_0,\qquad b_1<D_1.}
\tag{BN7}

Define

\[
\boxed{M=P_jb_1,\qquad N=b_2.}
\tag{BN8}

Then

\[
\boxed{M<B=x^{31/72},\qquad N\le N_0=x^{1/8}.}
\tag{BN9}

The greedy rule is deterministic, so the hard split is unique.

Since the hard modulus is squarefree,

\[
\mu(b)=\mu(b_1)\mu(b_2).
\]

---

## 5. The short hard state set has only 3001 values

The short factor `N=b_2` contains at most two hard primes and obeys

\[
N\le18455.
\]

The eligible hard primes are the primes from 29 through 18451. Exact prime enumeration gives

\[
\boxed{2105}
\]

single-prime values.

Exact enumeration of distinct prime pairs

\[
29\le q_1<q_2,
\qquad q_1q_2\le18455
\]

gives

\[
\boxed{895}
\]

pair-product values.

Together with `N=1`, the entire short hard carrier therefore contains

\[
\boxed{1+2105+895=3001}
\tag{BN10}

possible values.

No two distinct eligible prime pairs have the same product, so these are 3001 distinct integers.

---

## 6. Arithmetic multiplicity is gone; monotone-domain dependence remains

For `j=1`, the residual-level first-position constraint forces every hard Rosser prime below `z<=r`, so the physical long factor `M` has uniquely recoverable top distinct primes

\[
p>q>r
\]

and least-prime valuation `j`. The lower hard factor `b_1` lies below those primes. Thus the outer triple and the hard long factor are not multiply represented by different source labels.

For higher `j`, the valuation is likewise encoded by the exponent of the third-largest distinct prime `r` once the P(23) anchor part has been stripped.

What remains non-Cartesian is not factorization multiplicity but monotone domain geometry:

1. the prime ordering inside the short/long hard factors;
2. the beta-2 activation threshold inherited from the full hard state;
3. source endpoint restrictions on `p` and the pair kernel;
4. the finite P(23) anchor divisor / descended-interval label.

The next analytic target is therefore a support-sensitive Cauchy/reciprocal estimate over a **canonical** long carrier and the fixed 3001-element short state set, followed by finite aggregation of the P(23) descended intervals.

No finite P2 theorem, all-K theorem, Legendre theorem, or canonical promotion is claimed.
