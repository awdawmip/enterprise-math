# P017 — c=103/20 T1–T2 Second-Buchstab Ordered Pair-Shell Reduction

Status: `PROVED_WIP EXACT BUCHSTAB REINDEXING / ORDERED TWO-PRIME HARD SECTOR / NOT CANONICAL / NO FINITE P2 CLAIM`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_C515_T1_T3_SOURCE_MAP_AND_T3_BUCHSTAB_COLLAPSE_20260827.md`;
- `docs/P017_P2_C515_T12_HIGH_LPF_POINTWISE_COLLAPSE_20260827.md`.

Purpose: apply Buchstab once more to the fixed-cutoff T1 family and simultaneously to T2, turning the remaining T1–T2 problem into a single ordered two-prime shell with a small least-prime anchor.

---

## 1. Least-prime and ordered-pair shells

For a prime `p>=z`, define the least-prime shell

\[
L_p=S(\mathcal A_p,p).
\]

For primes

\[
z\le r<p,
\]

define

\[
\boxed{
P_{r,p}=S(\mathcal A_{rp},r).
}
\tag{P1}
\]

Thus `P_{r,p}` counts states divisible by `rp` whose remaining cofactor has no prime factor below `r`. Equivalently, `r` is the least prime factor of the state and `p` is a larger distinct divisor prime.

Buchstab's identity on the cofactor sequence gives exactly

\[
\boxed{
S(\mathcal A_p,z)
=L_p+
\sum_{z\le r<p}P_{r,p}.
}
\tag{P2}
\]

Repeated powers of the least prime are retained correctly: if the cofactor after removing `p` still has least prime `p`, the state belongs to `L_p`; the ordered-pair sum only uses `r<p`.

---

## 2. T1 after the second Buchstab decomposition

For c=103/20,

\[
T_1
=\frac12
\sum_{z\le p<D^{31/40}}S(\mathcal A_p,z).
\]

Using (P2),

\[
\boxed{
T_1
=\frac12
\sum_{z\le p<D^{31/40}}L_p
+
\frac12
\sum_{z\le r<p<D^{31/40}}P_{r,p}.
}
\tag{P3}

---

## 3. T2 after the same decomposition

Put

\[
s_0=\frac16,
\qquad
U=\frac{113}{240}.
\]

For fixed `s` and `p>=D^s`, Buchstab from the moving cutoff `D^s` up to `p` gives

\[
S(\mathcal A_p,D^s)
=L_p+
\sum_{D^s\le r<p}P_{r,p}.
\tag{P4}

Write

\[
t=\frac{\log p}{\log D},
\qquad
u=\frac{\log r}{\log D}.
\]

For the least-prime shell `L_p`, the allowed T2 integration length is

\[
\left[
\min(t,U-t)-s_0
\right]_+.
\]

Hence its T2 coefficient is

\[
\boxed{
\chi(t)
=6\left[
\min(t,U-t)-\frac16
\right]_+.
}
\tag{P5}

For an ordered pair shell `P_{r,p}`, the condition `D^s<=r` adds `s<=u`. Since `u<t`, the T2 integration length is

\[
\left[
\min(u,U-t)-s_0
\right]_+.
\]

Therefore

\[
\boxed{
T_2
=
\sum_p\chi(t)L_p
+
\sum_{z\le r<p}
6\left[
\min(u,U-t)-\frac16
\right]_+
P_{r,p},
}
\tag{P6}

where positivity of the brackets automatically restricts the sums to the source T2 range.

---

## 4. One triangular pair kernel replaces T1 and T2

Combining (P3) and (P6), every ordered pair shell carries the single coefficient

\[
\boxed{
\kappa(u,t)
=\frac12
+6\left[
\min(u,U-t)-\frac16
\right]_+.
}
\tag{P7}

For orientation, with

\[
u_*=U-\frac16=\frac{73}{240},
\]

the kernel is

\[
\kappa(u,t)=
\begin{cases}
\frac12+6(u-\frac16)=6u-\frac12,
& t\le U-u,\\[1mm]
\frac12+6(U-t-\frac16)=\frac{93}{40}-6t,
& U-u<t<u_*,\\[1mm]
\frac12,
& t\ge u_*.
\end{cases}
\tag{P8}

The maximum is

\[
\boxed{\kappa\le\frac{73}{80}.}
\]

This is an exact reindexing of the source T1–T2 terms; no sieve approximation has yet been made.

---

## 5. Combine with the high-LPF collapse

The preceding pointwise theorem proves that states with

\[
p_{\min}\ge D^{73/240}
\]

already have nonnegative T1–T2 contribution after base/T3 is included. Therefore any ordered-pair shell that remains analytically dangerous has

\[
\boxed{
 z\le r<D^{73/240}.
}
\tag{P9}

The larger prime still satisfies the T1 range

\[
r<p<D^{31/40}.
\]

Consequently the former two-family problem is reduced to

\[
\boxed{
\sum_{z\le r<D^{73/240}}
\sum_{r<p<D^{31/40}}
\kappa\!\left(
\frac{\log r}{\log D},
\frac{\log p}{\log D}
\right)
S(\mathcal A_{rp},r),
}
\tag{P10}

plus the least-prime shell terms, which are already coupled to base/T3 through the first Buchstab collapse.

At the Tier-A scale

\[
D^{73/240}=W^{73/216}\approx5.85\times10^5.
\]

Thus every genuinely dangerous T1–T2 state now has a small first anchor `r` below roughly 585,000.

---

## 6. Why this matters for P017

The source proof treats T1 and T2 by upper linear sieves whose errors are subsequently factorized into generic bilinear forms. The exact reindexing above exposes more structure before that step:

1. the first variable is an actual least prime `r`, not an arbitrary factorable coefficient;
2. `r` lies in a finite small range at the splice;
3. the second prime `p` is ordered above `r`;
4. the remaining cofactor is `r`-rough;
5. the coefficient is the explicit bounded triangular kernel `kappa(u,t)`.

This is the correct carrier on which to reuse P017 adaptive-anchor, complement-window and collision tools. One should not return to treating T1 and T2 as unrelated generic bilinear remainder families unless this ordered-pair structure fails to yield a cheaper estimate.

---

## 7. Next hard target

For fixed least-prime anchor `r`, study

\[
\sum_{r<p<D^{31/40}}
\kappa(u,t)S(\mathcal A_{rp},r)
\]

by separating physical moduli `rp` below and above the root. Above the root, P017 Boolean carry/complement geometry is immediately available; below the root, adaptive interval-length anchoring can strip the fixed factor `r` with zero floor error on suitable anchored subintervals.

No finite P2 theorem or all-K claim is made here.
