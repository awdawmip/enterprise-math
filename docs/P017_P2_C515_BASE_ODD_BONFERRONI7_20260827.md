# P017 — c=103/20 Base Odd Rough Count by Seventh-Order Bonferroni

Status: `PROVED_WIP FULLY FINITE BASE ROUGH LOWER BOUND > 0.07678 L23 / NO FUNDAMENTAL LEMMA / NOT FULL WEIGHTED MAIN / NOT CANONICAL`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Companion checker:

`experiments/p017_p2_c515_base_odd_bonferroni7_20260827.py`

Purpose: remove the base `S(A,z)` term from the unresolved source-main finite-normalization problem. At the Tier-A splice the sifting alphabet below `z` is finite enough that an elementary seventh-order Bonferroni lower bound is much sharper, and much more explicit, than importing a general linear-sieve fundamental lemma.

---

## 1. Work directly on the odd population

Let `J_23` be the P(23)-anchored interval of even length

\[
L_{23}=232018561402828200.
\]

It contains exactly `L23/2` odd integers.

The exact Tier-A cutoff satisfies

\[
1439<z<1447.
\]

After restricting to odd states, the sifting primes below `z` are therefore exactly the 227 odd primes

\[
3\le p\le1439.
\]

For an odd squarefree modulus `d`, the odd multiples of `d` form one arithmetic progression of spacing `2d`. Hence for any interval of length `L23`,

\[
\boxed{
\left|A_d^{\rm odd}-\frac{L_{23}}{2d}\right|<1.
}
\tag{B7-1}

This is the sharp odd-carry interface; no smooth weight and no Mertens approximation is used.

---

## 2. Seventh-order Bonferroni lower bound

For `0<=j<=7`, let

\[
e_j
=
\sum_{p_1<\cdots<p_j\le1439\atop p_i\text{ odd prime}}
\frac1{p_1\cdots p_j},
\qquad e_0=1.
\]

Bonferroni inclusion-exclusion truncated after the odd degree seven gives a lower bound for the number `S_odd(z)` of odd states with no prime factor below `z`:

\[
S_{\rm odd}(z)
\ge
\sum_{j=0}^7(-1)^j
\sum_{p_1<\cdots<p_j}A_{p_1\cdots p_j}^{\rm odd}.
\tag{B7-2}

Using (B7-1),

\[
\frac{S_{\rm odd}(z)}{L_{23}}
>
\frac12\sum_{j=0}^7(-1)^je_j
-
\frac1{L_{23}}
\sum_{j=1}^7\binom{227}{j}.
\tag{B7-3}

The companion checker computes every `e_j` with exact `Fraction` arithmetic. The main density is

\[
\frac12\sum_{j=0}^7(-1)^je_j
=0.0768143631\ldots
\]

for orientation only.

The total number of possible nonzero carry terms is exactly

\[
\boxed{
\sum_{j=1}^7\binom{227}{j}
=5795560160583.
}
\tag{B7-4}

Relative to `L23`, this is less than `2.498*10^-5`.

The exact rational comparison yields

\[
\boxed{
\frac{S_{\rm odd}(z)}{L_{23}}
>
\frac{3839}{50000}
=0.07678.
}
\tag{B7-5}

---

## 3. Consequence for finite normalization

The base rough-count term is now fully finite at the Tier-A splice. In particular, it no longer needs the source Lemma-2 replacement

\[
X V(z)\{f(6)-E\}-R^-.
\]

The unresolved finite-normalization problem is therefore narrower:

\[
\boxed{
\text{finite normalization remains only in the weighted }T_1/T_2\text{ comparison, not in base }S(A,z).
}
\]

This does not by itself prove positivity of the full weighted sum. The negative weighted prime-shell terms nearly cancel most of the base rough population, so they still require their existing pointwise credits / residual bounds and, on the remaining `j=1` carrier, analytic control.

No finite P2 theorem or all-K claim is made.
