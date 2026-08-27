# P017 — c=103/20 T1–T2 Least-Shell Budget Correction and D^(1/2) Residual Census

Status: `CORRECTION / PROVED_WIP EXACT ONE-PAIR CREDIT + EXACT FINITE ROSSER CENSUS / SUPERSEDES OVERSTRONG PAIR-ABSORPTION CLAIMS / NOT CANONICAL / NO FINITE P2 CLAIM`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Corrects/supersedes the pointwise-budget conclusions in:

- `docs/P017_P2_C515_T12_SUPERROOT_PAIR_ABSORPTION_20260827.md`;
- `docs/P017_P2_C515_T12_HIGH_PAIR_POINTWISE_ABSORPTION_20260827.md`;
- `docs/P017_P2_C515_T12_TWO_PAIR_CREDIT_Z2_RESIDUAL_20260827.md`.

The source-map, second-Buchstab pair kernel, unique top-two-prime encoding, adaptive-anchor identities, canonical hard-suffix factorization, and P(23) anchor arithmetic remain valid. The error was narrower: the full base-minus-T3 numerator `12u-1` was reused for ordered pairs without first charging the least-prime-shell T1–T2 term.

---

## 1. Correct state-level bookkeeping

Keep

\[
U=\frac{113}{240},\qquad
\Delta=\frac{93}{20},\qquad
\frac16\le u<\frac{73}{240}.
\]

For a state whose least prime factor is `r=D^u`, the exact least-prime-shell T1–T2 penalty numerator is

\[
\boxed{
\ell(u)
=\frac12
+6\left[\min(u,U-u)-\frac16\right]_+.
}
\tag{C1}
\]

On the whole dangerous range the bracket is nonnegative. Thus

\[
\ell(u)=
\begin{cases}
6u-\frac12,&\frac16\le u\le\frac{113}{480},\\[1mm]
\frac{93}{40}-6u,&\frac{113}{480}\le u<\frac{73}{240}.
\end{cases}
\tag{C2}
\]

The exact base-minus-T3 numerator is

\[
B(u)=12u-1.
\]

Therefore the amount genuinely available for ordered-pair penalties is

\[
\boxed{C(u)=12u-1-\ell(u).}
\tag{C3}
\]

Explicitly,

\[
C(u)=
\begin{cases}
6u-\frac12,&\frac16\le u\le\frac{113}{480},\\[1mm]
18u-\frac{133}{40},&\frac{113}{480}\le u<\frac{73}{240}.
\end{cases}
\tag{C4}
\]

---

## 2. Exactly one maximal pair is always free

The ordered-pair kernel is

\[
\kappa(u,t)
=\frac12+6\left[\min\left(u,U-t\right)-\frac16\right]_+.
\]

For fixed `u`, it is nonincreasing in `t` and obeys

\[
\boxed{\kappa(u,t)\le6u-\frac12.}
\tag{C5}
\]

From (C4):

- on `u<=113/480`, `C(u)=6u-1/2` exactly;
- on `u>=113/480`,
  \[
  C(u)-\left(6u-\frac12\right)
  =12u-\frac{113}{40}\ge0.
  \]

Hence

\[
\boxed{C(u)\ge\max_t\kappa(u,t).}
\tag{C6}
\]

Therefore the correct pointwise conclusion is:

\[
\boxed{
\text{base-minus-T3 absorbs the least-prime shell and the single largest ordered-pair penalty.}
}
\tag{C7}

It does **not** in general absorb two ordered-pair penalties. At `u=1/6`, for example, the least shell costs `1/2`, the remaining pair budget is only `1/2`, and two larger primes with pair kernel `1/2` are compatible with the basin exponent constraint. This is the explicit obstruction to the superseded two-pair claim.

Because `kappa(u,t)` is nonincreasing in `t`, the absorbed pair is the smallest distinct larger divisor prime when one exists.

---

## 3. Every residual pair has a canonical three-prime witness

Let `p_1` be the smallest distinct divisor prime above the least prime `r`. After crediting the pair `(r,p_1)`, any still-penalized ordered pair `(r,p)` has

\[
\boxed{r<p_1<p.}
\tag{C8}

Thus every residual pair occurrence is supported on a state divisible by three distinct primes

\[
\boxed{r p_1 p.}
\tag{C9}

All three are at least

\[
z=D^{1/6}.
\]

Therefore

\[
\boxed{r p_1p\ge z^3=D^{1/2}.}
\tag{C10}

If one upper-sieves the remaining cofactor after conditioning on such a three-prime witness, the available level satisfies

\[
\boxed{
Q_{\rm res}\le\frac{D}{z^3}=D^{1/2}=W^{5/9}.
}
\tag{C11}

This replaces the overstrong `D^(1/3)=z^2` ceiling in the superseded two-pair note.

As before, (C11) is a valid ceiling for a conditioned residual shell; a canonical aggregate reindexing of all residual pair occurrences is still required before a complete remainder theorem is obtained.

---

## 4. Tier-A hard-prime alphabet

At

\[
K_0=116009280740973308,
\qquad W=K_0+1,
\]

the beta-2 first-position inequality at level `Q<=W^(5/9)` gives

\[
q_1^3<W^{5/9}.
\]

Since `z=W^(5/27)`, this is simply

\[
q_1<z.
\]

The already-frozen exact cutoff is

\[
1439<z<1447,
\]

so after P(23) prestripping the hard Rosser prime alphabet is exactly the primes

\[
\boxed{29\le q\le1439.}
\tag{C12}

There are

\[
\boxed{219}
\]

such primes.

---

## 5. Hard Rosser depth is at most four

For a descending hard tuple

\[
d=q_1\cdots q_s,
\]

define

\[
q_{\rm crit}(d)
=\max_{j\ \mathrm{odd}}q_1\cdots q_{j-1}q_j^3.
\]

The minimum possible critical value among five distinct hard primes is achieved by the five smallest hard primes `{29,31,37,41,43}`. Exact integer comparison gives

\[
q_{\rm crit}(29\cdot31\cdot37\cdot41\cdot43)^9>W^5.
\]

Since `q_crit` is monotone in every ordered prime coordinate,

\[
\boxed{\omega(d)\le4}
\tag{C13}

for every P(23)-stripped beta-2 state at level at most `W^(5/9)`.

---

## 6. Exact finite census at the worst residual level

The maximal residual level is

\[
Q_*=W^{5/9}.
\]

Let

\[
Q_0=\lfloor W^{5/9}\rfloor.
\]

The checker computes exactly

\[
\boxed{Q_0=3021855833.}
\tag{C14}

For one or two hard primes, the only active Rosser condition is the first-position cube inequality, so all choices are supported:

\[
\#\omega=1=219,
\qquad
\#\omega=2=\binom{219}{2}=23871.
\]

For three primes, writing them increasingly as `a<b<c`, the nontrivial condition is

\[
cb a^3\le Q_0.
\]

Exact enumeration gives

\[
\boxed{\#\omega=3=18808.}
\tag{C15}

For four primes `d<a<b<c`, the Rosser condition is the same condition on the top three `a<b<c`, and the fourth prime may be any hard prime below `a`. Exact enumeration gives

\[
\boxed{\#\omega=4=31126.}
\tag{C16}

Thus the complete P(23)-stripped hard inner Rosser support at the worst corrected residual level contains

\[
\boxed{
1+219+23871+18808+31126=74025
}
\tag{C17}

states.

This is larger than the superseded `254`-state `z^2` census, but remains a fixed finite depth-four family rather than a generic factorization family.

---

## 7. Corrected frontier

The valid T1–T2 reductions now are:

1. high-LPF states `p_min>=D^(73/240)` are pointwise nonnegative by the original all-term theorem;
2. T3 is exactly a least-prime/Buchstab shell and is not an independent upper-sieve remainder;
3. the second Buchstab decomposition gives one least-prime shell plus ordered pairs with kernel `kappa`;
4. after charging the least-prime shell, the remaining pointwise credit absorbs exactly one maximal ordered-pair penalty uniformly;
5. every residual pair therefore has a three-distinct-prime witness and a conditioned inner level at most `D^(1/2)`;
6. after the P(23) exact prestrip, that worst inner Rosser family has depth at most four and exactly 74025 hard states.

The load-bearing next problem is:

> construct a canonical three-prime residual-shell reindexing (or a safe one-sided majorant with controlled multiplicity), then aggregate its finite depth-four inner Rosser family and the finite main normalization inside the remaining c515 budget.

No finite P2 theorem, all-K theorem, Legendre theorem, or canonical promotion is claimed.
