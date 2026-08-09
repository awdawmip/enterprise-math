# P022 — Automatic Central-Binomial Pivots Are Infinite but Zero-Density

Status: `ACTIVE RESEARCH NOTE / STRUCTURAL SCALE CORRECTION`  
Owner: `program/p022-geometry-v2`  
Parent: central-binomial triangular-pivot supplement  
Prior-art input: prime-counting asymptotics are classical

## 1. Exact count of automatic pivot indices

The previous structural theorem gives an automatic triangular `A_n` valuation pivot whenever

\[
2n-1
\]

is prime.

For segment indices

\[
2\le n\le N,
\]

this condition is in bijection with the odd primes

\[
3\le p\le2N-1
\]

through

\[
n=\frac{p+1}{2}.
\]

Therefore the exact number of automatic central-binomial pivot indices up to `N` is

\[
\boxed{
P_A(N)
=\pi(2N-1)-1,
}
\]

where `pi(x)` is the prime-counting function and the subtraction removes the prime `2`.

---

## 2. P022-LI11 — automatic pivot indices have density zero

By the classical prime number theorem,

\[
\pi(x)\sim\frac{x}{\log x}.
\]

Hence

\[
P_A(N)
\sim
\frac{2N}{\log(2N)}.
\]

Dividing by the total number of segment indices gives

\[
\boxed{
\frac{P_A(N)}{N}
\sim
\frac{2}{\log(2N)}
\longrightarrow0.
}
\]

Thus the simple prime-`2n-1` pivot mechanism is:

- infinite;
- structurally exact;
- but asymptotically sparse.

It does **not** explain full-rank growth on a positive-density subset of segment lengths.

---

## 3. Composite indices are asymptotically dominant

The complement consists of indices for which `2n-1` is composite (plus the initial trivial boundary).

Since the automatic-prime indices have density zero,

\[
\boxed{
\#\{n\le N:2n-1\text{ composite}\}
=N-O(N/\log N).
}
\]

So the earlier phrase “Franel defect completion” should not be read as a rare exceptional repair.

Asymptotically, the joint/Franel completion mechanism must explain **almost all segment indices** if the global `(J_1,J_2,J_3)` identifiability conjecture is true.

The conceptual decomposition is therefore better written as

\[
\boxed{
\text{sparse automatic }A_n\text{ pivots}
+
\text{dominant composite-index joint completion}.
}
\]

---

## 4. Consequence for the global proof strategy

A global theorem cannot plausibly be obtained merely by repeating the prime-`2n-1` argument.

That lemma is valuable because it provides infinitely many exact anchors, but the main theorem must address a density-one family of composite indices.

This sharply favors structural routes involving:

1. Franel recurrences/congruences and their p-adic valuation patterns;
2. non-triangular but globally independent central-binomial valuation rows;
3. joint valuation geometry rather than primitive divisors alone;
4. a proof that any hypothetical finite-support multiplicative relation contradicts recurrence/congruence structure.

The finite rank certificate through segment length 150 is evidence that such completion exists at least on a substantial initial range.  LI11 clarifies that the unresolved mechanism is not peripheral; it is the asymptotic core of the low-order identifiability problem.

---

## 5. Prior-art boundary

The prime-counting function and prime number theorem are classical.  P022 uses them only to quantify the density of the already proved automatic-pivot index set.

No novelty claim is made for the analytic number theory input.
