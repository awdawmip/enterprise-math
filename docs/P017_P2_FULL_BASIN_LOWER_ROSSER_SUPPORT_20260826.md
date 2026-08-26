# P017 — Full-Basin Lower Rosser Support Compression

Status: `PROVED_WIP EXACT FIXED-POINT RANKIN-DP / BASE LOWER-SIEVE REMAINDER HALVED / NOT CANONICAL / NO ALL-K P2 CLAIM`

Date: `2026-08-26`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- the standard Rosser–Iwaniec lower linear-sieve support;
- `docs/P017_P2_FULL_BASIN_BASE_ABSOLUTE_REMAINDER_20260826.md`.

Companion checker:

`experiments/p017_p2_full_basin_lower_rosser_support_20260826.py`.

Purpose: replace the preceding bound that charged **every** odd squarefree `z`-smooth modulus below the level by a support bound for the actual lower Rosser weight. The resulting base lower-sieve remainder at the Tier-A splice is almost halved.

---

## 1. Lower Rosser support

Write an odd squarefree support modulus as

\[
d=p_1p_2\cdots p_r,
\qquad
p_1>p_2>\cdots>p_r.
\]

For the lower Rosser–Iwaniec linear-sieve weight, a necessary support condition is

\[
\boxed{
 p_1\cdots p_{j-1}p_j^3<D
 \quad\text{for every even }j\le r.
}
\tag{LR1}
\]

Since

\[
p_1\cdots p_{j-1}\ge p_j^{j-1},
\]

(LR1) implies the simpler position-wise necessary condition

\[
\boxed{p_j^{j+2}<D\quad(j\text{ even}).}
\tag{LR2}
\]

The set defined by (LR2) is a superset of the true lower Rosser support, so counting it gives a rigorous support upper bound.

---

## 2. Splice data

As in the full-basin note, put

\[
K_0=116009280740973308,
\qquad W=K_0+1,
\]

and

\[
D=W^{10/9},
\qquad
z=W^{5/27}.
\]

The exact cutoff certificate gives

\[
1439<z<1447,
\]

so the relevant odd primes are exactly the 227 primes from `3` through `1439`.

---

## 3. Position-sensitive Rankin bound

Take

\[
\boxed{\sigma=\frac{97}{200}.}
\]

Rankin's inequality gives, for the true lower support,

\[
\#\operatorname{supp}\lambda^-
\le
D^\sigma
\sum_{d\in\mathcal S_-}d^{-\sigma},
\tag{LR3}
\]

where `S_-` is the positional superset defined by (LR2).

The weighted sum in (LR3) can be evaluated by a one-dimensional dynamic program over the primes in **descending** order. If `k` primes have already been selected, selecting the next prime places it at position

\[
j=k+1.
\]

At even `j`, the transition is allowed only when

\[
p^{9(j+2)}<W^{10},
\]

which is (LR2) with the fractional exponent in `D=W^(10/9)` cleared exactly.

---

## 4. Pure-integer fixed-point certificate

To avoid floating-point powers, the checker uses the common scale

\[
S=10^9.
\]

For each odd prime `p<=1439`, it computes the least integer `q_p` such that

\[
\left(\frac{q_p}{S}\right)^{200}p^{97}\ge1.
\]

Hence

\[
\frac{q_p}{S}\ge p^{-97/200}.
\]

If the DP state at selected-prime count `k` is stored with denominator `S^k`, every transition is then exact integer arithmetic.

A useful structural fact falls out automatically: after all 227 primes are processed, the positional superset has no admissible state beyond

\[
\boxed{r=18.}
\]

Thus the finite Rosser support calculation is an 18-layer DP, not a `2^227` subset enumeration.

The exact upper weighted sum produced by the checker is approximately

\[
211490.10284,
\]

but the final theorem is established without converting that value to floating point.

---

## 5. Final support inequality

Since

\[
D^\sigma
=
\left(W^{10/9}\right)^{97/200}
=W^{97/180},
\]

the checker proves the desired comparison by raising both sides to the 180th power, entirely in integer arithmetic. The result is

\[
\boxed{
\#\operatorname{supp}\lambda^-(D,z)
<\frac{29}{10000}K_0.
}
\tag{LR4}
\]

For the sharp odd sequence every one-dimensional carry remainder obeys

\[
|e(d)|<1.
\]

Therefore the actual lower Rosser remainder satisfies

\[
\boxed{
|R^-_0|
<\frac{29}{10000}K_0.
}
\tag{LR5}
\]

Relative to the full square-basin length `L=2K_0`,

\[
\boxed{
\frac{|R^-_0|}{L}
<\frac{29}{20000}
=0.00145.
}
\tag{LR6}
\]

This strictly improves the preceding all-smooth-modulus bound

\[
R_0/L<0.00285.
\]

---

## 6. Finite-route consequence

The base lower-sieve error is no longer the dominant finite cost. The live finite optimization should now use

\[
\boxed{0.00145L}
\]

as the rigorous base-error budget.

This materially changes the parameter tradeoff. Exploratory terminal-band calculations indicate that moving the a6 terminal parameter from the asymptotic root-edge value `c=5.4` toward roughly `c=5.1–5.2` may leave a positive finite budget after both the base error and the terminal upper-Rosser error are charged.

That terminal-band statement is not yet frozen as a theorem. The next tasks are:

1. make the terminal upper-Rosser weighted support bound explicit for selected rational `c` values;
2. retain the source main coefficient in the corresponding terminal-complete split;
3. measure the residual budget available to the T1–T3 bilinear sectors.

No finite analytic P2 threshold, P2-in-every-square theorem or Legendre theorem is claimed here.
