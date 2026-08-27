# P017 — c=103/20 T1–T2 Residual Triple-Shell / Least-Prime Valuation Ladder

Status: `PROVED_WIP EXACT RESIDUAL REINDEXING + VALUATION-DEPENDENT LEVEL COLLAPSE / j=1 AGGREGATE STILL OPEN / NOT CANONICAL / NO FINITE P2 CLAIM`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_C515_T12_LEAST_SHELL_BUDGET_CORRECTION_20260827.md`;
- `docs/P017_P2_C515_T12_SECOND_BUCHSTAB_PAIR_SHELL_20260827.md`;
- `docs/P017_P2_C515_T12_P23_ANCHOR_AFTER_SUFFIX_FACTORIZATION_20260827.md`.

Purpose: canonically reindex the ordered-pair penalty that remains after the corrected least-shell + one-pair pointwise credit. The residual is organized by the exact multiplicity of the least prime and by the second distinct prime. This produces a strict valuation ladder for the inner upper-sieve level.

---

## 1. State factorization and the credited first pair

Let a state `n` in the dangerous T1–T2 range have least prime divisor

\[
r\ge z=D^{1/6},
\qquad
u_r(n)=j\ge1.
\]

Assume `n` has at least one distinct prime divisor above `r`, and let

\[
q
\]

be the smallest such distinct prime. Any further distinct divisor prime is denoted

\[
p>q.
\]

The corrected pointwise budget theorem proves that the least-prime-shell T1–T2 term together with the pair `(r,q)` can be absorbed by base-minus-T3. Therefore the exact residual ordered-pair penalty of this state is the sum over the later distinct primes `p>q` only.

---

## 2. Exact triple-shell encoding

For primes

\[
z\le r<q<p
\]

and `j>=1`, consider

\[
\boxed{S(\mathcal A_{r^jqp},q).}
\tag{V1}
\]

By the usual sieve convention, `S(A_m,q)` counts states divisible by `m` whose cofactor after division by `m` has no prime factor strictly below `q`.

Consequently a state is counted by (V1) exactly when:

1. it is divisible by `r^j q p`;
2. after removing `r^j q p`, no additional factor `r` remains, so
   \[
   \nu_r(n)=j;
   \]
3. no distinct prime strictly between `r` and `q` divides the state;
4. repeated powers of `q` are allowed, because the sifting product contains primes strictly below `q`.

Thus `q` is exactly the second distinct prime factor and `j` is exactly the least-prime valuation.

For a fixed state and a fixed later prime `p`, there is therefore exactly one pair `(j,q)` for which (V1) carries that residual occurrence.

Hence the residual T1–T2 ordered-pair term admits the exact canonical reindexing

\[
\boxed{
\mathcal T_{\rm res}
=
\sum_{z\le r<q<p<D^{31/40}}
\kappa\!\left(
\frac{\log r}{\log D},
\frac{\log p}{\log D}
\right)
\sum_{j\ge1}S(\mathcal A_{r^jqp},q),
}
\tag{V2}

with the inherited source restrictions and the understanding that only states surviving the corrected pointwise credit occur. There is no choice of witness prime in (V2): `q` is the second distinct prime by construction.

---

## 3. Least-prime valuation is at most eight

Since

\[
r,q,p\ge z=D^{1/6}
\]

and every basin state lies below

\[
W^2=D^{9/5},
\]

a state in (V1) obeys

\[
D^{(j+2)/6}\le r^jqp<D^{9/5}.
\]

Therefore

\[
\frac{j+2}{6}<\frac95,
\]

so

\[
\boxed{1\le j\le8.}
\tag{V3}

---

## 4. Valuation ladder for the inner sieve level

Apply an upper linear sieve to the quotient sequence in (V1) using the original total level `D`. The available inner level is

\[
\boxed{
Q_j(r,q,p)=\frac{D}{r^jqp}.
}
\tag{V4}

Since `r,q,p>=D^(1/6)`, uniformly

\[
\boxed{
Q_j\le D^{1-(j+2)/6}.
}
\tag{V5}

In particular,

\[
\boxed{
\begin{array}{c|c}
j&Q_j\text{ ceiling}\\\hline
1&D^{1/2}=W^{5/9},\\
2&D^{1/3}=z^2=W^{10/27},\\
3&D^{1/6}=z=W^{5/27},\\
4&1,\\
5,6,7,8&<1.
\end{array}}
\tag{V6}

Thus only `j=1,2,3` can have any nontrivial inner sieve support at total level `D`; the higher-valuation shells have no room for a nontrivial remainder modulus beyond the identity state.

---

## 5. P(23)-stripped hard Rosser complexity by valuation

Use the preferred P(23) anchor. Every residual hard sieve prime is at least 29.

### j=1

The maximal inner level is `D^(1/2)=W^(5/9)`. The corrected least-shell budget census proves:

\[
\boxed{74025\text{ hard beta-2 states},\qquad \omega(d_{\rm hard})\le4.}
\tag{V7}

### j=2

The maximal inner level is

\[
D^{1/3}=z^2=W^{10/27}.
\]

The previously computed z^2 census is valid on this valuation shell. It gives

\[
\boxed{254\text{ hard beta-2 states},\qquad \omega(d_{\rm hard})\le2.}
\tag{V8}

### j=3

The maximal inner level is

\[
D^{1/6}=z<1447.
\]

But

\[
29^3=24389>1447>z.
\]

The first beta-2 support condition for a nontrivial hard prime would require `29^3<Q_3`, impossible. Hence

\[
\boxed{d_{\rm hard}=1\quad(j=3).}
\tag{V9}

The same is automatic for `j>=4` because `Q_j<=1`.

Therefore all genuinely nontrivial hard inner Rosser complexity is concentrated in the least-prime-squarefree shell `j=1`, with a small 254-state correction at `j=2`.

---

## 6. Research consequence

The former residual ordered-pair problem has now split canonically into:

\[
\boxed{
\begin{array}{ll}
\nu_r(n)=1 &: \text{depth-4 / 74025-state hard inner family},\\
\nu_r(n)=2 &: \text{depth-2 / 254-state hard inner family},\\
\nu_r(n)\ge3 &: \text{no nontrivial P(23)-hard inner Rosser state}.
\end{array}}
\tag{V10}

This removes witness-choice multiplicity and isolates the only genuinely large analytic block: states in which the least prime occurs exactly once.

The next load-bearing target is the `j=1` external triple carrier

\[
\sum_{r<q<p}\kappa(u,t_p)S(\mathcal A_{rqp},q)
\]

with the finite depth-four inner family. One should aggregate that carrier directly, preserving prime ordering and monotone endpoints, rather than return to a generic Rosser factorization count.

Finite source-main normalization remains an independent open gate.

No finite P2 theorem, all-K theorem, Legendre theorem, or canonical promotion is claimed here.
