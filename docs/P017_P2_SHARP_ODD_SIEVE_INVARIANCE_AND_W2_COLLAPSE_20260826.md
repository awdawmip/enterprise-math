# P017 — Sharp Odd-Sieve Invariance and W2 Trivial Collapse

Status: `PROVED_WIP EXACT PARITY MODEL CHANGE + FINITE W2 COLLAPSE / NOT FULL W1 CLOSURE / NOT CANONICAL / NO ALL-K P2 CLAIM`

Date: `2026-08-26`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- Iwaniec–Laborde, *P2 in short intervals* (1981), especially (3), (4), Lemma 1 and Lemma 6;
- `docs/P017_P2_A6_FIVE_NINTH_ROOT_EDGE_PACKAGE_20260826.md`;
- `docs/P017_P2_CHEN_CARRY_BRIDGE_20260823.md`.

Companion checker:

`experiments/p017_p2_sharp_odd_w2_trivial_collapse_20260826.py`.

Purpose: replace the smoothing-first view by the parity actually selected by the source sieve. Every source sifting cutoff is above 2, so all actual sifted states are already odd. This permits a sharp odd model in which the one-dimensional congruence errors are literal P017 odd-quotient carries. In the root-edge W2 band, the vanishing terminal weight is so small that a completely trivial upper bound already beats the finite main scale by orders of magnitude.

---

## 1. Exact parity invariance of all source sifting functions

For a nonnegative sequence of weights `A={a_n}`, define its odd projection

\[
a_n^{\rm odd}=a_n\mathbf 1_{2\nmid n}.
\]

For every cutoff `u>2`,

\[
P(u)=\prod_{p<u}p
\]

contains the prime 2. Hence

\[
(n,P(u))=1\Longrightarrow 2\nmid n.
\]

Therefore, identically,

\[
\boxed{S(\mathcal A^{\rm odd},u)=S(\mathcal A,u).}
\tag{O1}
\]

If `p` is an odd prime and `u>2`, the same statement holds for the prime-lift sequence:

\[
\boxed{S(\mathcal A_p^{\rm odd},u)=S(\mathcal A_p,u).}
\tag{O2}
\]

Every sifting cutoff occurring in the source weighted sum (3) is either `D^s`, `D^(1/a)` or the odd prime `p`, and is above 2 in the present finite range. Thus every source term is unchanged by odd projection.

Consequently

\[
\boxed{
W(\mathcal A^{\rm odd})=W(\mathcal A),\qquad
W_1(\mathcal A^{\rm odd})=W_1(\mathcal A),\qquad
W_2(\mathcal A^{\rm odd})=W_2(\mathcal A).
}
\tag{O3}
\]

This is an exact equality of the actual sifted quantities, not merely an asymptotic equality of their main terms.

---

## 2. Exact one-dimensional normalization on a sharp even-length interval

Let `J` be any interval of `L` consecutive integers, with `L` even, and let

\[
\mathcal A_J^{\rm odd}=\{n\in J:2\nmid n\}
\]

with unit weights. Then exactly

\[
|\mathcal A_J^{\rm odd}|=\frac L2.
\]

For an odd squarefree sieve modulus `d`, the odd multiples of `d` in `J` are obtained by writing `n=dq` and requiring `q` odd. The odd positions in `J` form a step-2 arithmetic progression, and 2 is invertible modulo `d`. Hence one residue class modulo `d` is selected among `L/2` consecutive progression positions. Therefore

\[
\boxed{
A_d^{\rm odd}(J)=\frac{L}{2d}+e_J(d),
\qquad |e_J(d)|<1.
}
\tag{O4}
\]

For an external odd prime `p` coprime to `d`, the same argument gives

\[
\boxed{
A_{pd}^{\rm odd}(J)=\frac{L}{2pd}+e_J(pd),
\qquad |e_J(pd)|<1.
}
\tag{O5}
\]

Thus every one-dimensional sharp odd remainder is a literal P017-type odd-quotient carry.

If the sieve prime set is restricted to odd primes, its local product is

\[
V_{\rm odd}(u)=\prod_{3\le q<u}\left(1-\frac1q\right)=2V(u).
\]

Since the sharp odd population is `L/2`,

\[
\boxed{
\frac L2\,V_{\rm odd}(u)=L\,V(u).
}
\tag{O6}
\]

The same identity persists after an external odd prime lift, with both sides divided by `p`. Hence parity projection does not cost a factor 2 in the one-dimensional linear-sieve main term.

---

## 3. Why W2 is also parity-safe

The source split is

\[
W(\mathcal A)=W_1(\mathcal A)+W_2(\mathcal A),
\]

where

\[
W_2(\mathcal A)
=\frac1{2c-b-1}
\sum_{y\le p<D^{c/a}}
\left(c-a\frac{\log p}{\log D}\right)
S(\mathcal A_p,D^{1/a}).
\]

The cutoff `D^(1/a)>2`, so every actual state counted by `S(A_p,D^(1/a))` is already odd. Thus W2 is exactly invariant by (O2), independently of the two-dimensional Selberg presentation later used to estimate it.

For the live a6 root-edge packet,

\[
a=6,\qquad b=\frac{22}{5},\qquad c=\frac{27}{5},\qquad D=X^{5/9},
\]

and

\[
2c-b-1=c=\frac{27}{5}.
\]

Put

\[
w=D^{c/a}=X^{1/2}.
\]

Then the W2 weight is exactly

\[
\boxed{
c-a\frac{\log p}{\log D}
=\frac{a}{\log D}\log\frac wp.}
\tag{O7}
\]

It vanishes linearly at the root endpoint `p=w`.

---

## 4. A sharp trivial W2 upper bound

Let `J` have even length `L<=Y`, where

\[
Y=X^{4999/10000}.
\]

Discarding the roughness condition only enlarges the prime-lift sifting function:

\[
S(\mathcal A_{J,p}^{\rm odd},D^{1/6})
\le
\#\{n\in J:p\mid n\}
\le \frac Lp+1.
\]

Use (O7), then enlarge the prime sum to all integers. With

\[
\delta=\log\frac wY=\frac{\log X}{10000},
\]

monotonicity and integral comparison give

\[
\sum_{Y\le n<w}\frac{\log(w/n)}n
\le
\frac\delta Y+\frac{\delta^2}{2},
\]

and

\[
\sum_{Y\le n<w}\log(w/n)
\le
\delta+w-Y(1+\delta).
\]

For `0<delta<1`,

\[
e^\delta-1-\delta
\le
\frac{\delta^2}{2(1-\delta)}.
\]

Since here

\[
\frac{a}{(2c-b-1)\log D}
=\frac2{\log X},
\]

we obtain an entirely elementary finite upper bound for W2.

At the conservative Tier-A scale

\[
K_0=116009280740973308,
\qquad X_0=K_0^2,
\]

the exact rational checker uses only

\[
10^{34}<X_0<10^{35},
\qquad
2.3<\log10<2.303,
\]

together with `L>Y-2`, and certifies

\[
\boxed{
\frac{W_2(\mathcal A_J^{\rm odd})}{L}
<\frac{17}{10^7}
=1.7\times10^{-6}.
}
\tag{O8}
\]

No Selberg two-dimensional sieve, no Poisson summation and no smooth cutoff are used in (O8).

---

## 5. Consequence for the finite route

The source-decimal a6 main package has final normalized main coefficient

\[
W(\mathcal A)
>\frac{y}{\log D}\frac{12}{2c-b-1}[G_*-\varepsilon],
\qquad G_*>0.1148.
\]

At the Tier-A scale this is naturally of order `5.8e-3` times the interval length. The elementary W2 bound (O8) is more than three orders of magnitude smaller.

Therefore the finite root-edge obstruction is no longer W2. The correct remaining problem is W1:

> apply direct Rosser–Iwaniec upper/lower sieve weights to the sharp odd sequence, consume the exact carry bound `|e_J(q)|<1` before any factorable decomposition, and quantify the actual Rosser support across the W1 prime-lift terms.

The old order-4 B-spline/factorable machinery remains a fallback, but it is no longer the preferred finite route for W1.

This note does not yet prove a full W1 finite lower bound, a finite analytic P2 threshold, P2 in every square interval, or Legendre's conjecture.
