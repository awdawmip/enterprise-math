# P017 — c=103/20 T1–T2 Super-Root Ordered-Pair Absorption

Status: `PROVED_WIP EXACT POINTWISE ABSORPTION / SUB-ROOT ORDERED PAIRS REMAIN / NOT CANONICAL / NO FINITE P2 CLAIM`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_C515_T1_T3_SOURCE_MAP_AND_T3_BUCHSTAB_COLLAPSE_20260827.md`;
- `docs/P017_P2_C515_T12_HIGH_LPF_POINTWISE_COLLAPSE_20260827.md`;
- `docs/P017_P2_C515_T12_SECOND_BUCHSTAB_PAIR_SHELL_20260827.md`.

Purpose: show that the entire super-root part of the remaining ordered two-prime T1–T2 carrier is absorbed pointwise by the already-combined base-minus-T3 weight. No upper sieve, Fourier expansion, or average estimate is needed on that sector.

---

## 1. Hard first-anchor range and root equation

Write

\[
u=\frac{\log r}{\log D},
\qquad
t=\frac{\log p}{\log D},
\]

for the ordered pair shell `P_{r,p}=S(A_{rp},r)`, with

\[
z\le r<p.
\]

The preceding high-LPF theorem reduces every genuinely dangerous first anchor to

\[
\boxed{
\frac16\le u<\frac{73}{240}.
}
\tag{SRA1}

Since `D=W^(10/9)`, the physical square root `rp=W` is exactly

\[
\boxed{u+t=\frac9{10}.}
\tag{SRA2}

---

## 2. The pair kernel is exactly 1/2 above the root

Assume

\[
rp>W,
\qquad\text{i.e.}\qquad
u+t>\frac9{10}.
\]

Then, by (SRA1),

\[
t>rac9{10}-\frac{73}{240}
=\frac{143}{240}
>\frac{73}{240}.
\]

The ordered-pair kernel from the second Buchstab reduction is

\[
\kappa(u,t)
=\frac12
+6\left[\min\left(u,\frac{113}{240}-t\right)-\frac16\right]_+.
\]

But `t>73/240` implies

\[
\frac{113}{240}-t<\frac16.
\]

Hence the bracket vanishes and

\[
\boxed{
 rp>W\Longrightarrow\kappa(u,t)=\frac12.
}
\tag{SRA3}

---

## 3. At most two super-root larger primes per basin state

Fix a basin state `n` whose least prime factor is `r` in the hard range (SRA1). Suppose three distinct larger divisor primes `p_1,p_2,p_3` satisfy

\[
rp_i>W.
\]

Then

\[
p_i>\frac Wr
\]

for every `i`, so

\[
n\ge r p_1p_2p_3
>r\left(\frac Wr\right)^3
=\frac{W^3}{r^2}.
\]

Now `u<73/240` means

\[
r<D^{73/240}=W^{73/216}.
\]

Therefore

\[
r^2<W^{73/108}<W,
\]

and consequently

\[
\frac{W^3}{r^2}>W^2.
\]

But every state in the consecutive-square basin is strictly below `W^2`. Contradiction.

Thus

\[
\boxed{
\#\{p>r:p\mid n,\ rp>W\}\le2.
}
\tag{SRA4}

Together with (SRA3), the total super-root ordered-pair penalty numerator on one state is at most

\[
\boxed{2\cdot\frac12=1.}
\tag{SRA5}

---

## 4. Base-minus-T3 supplies at least the same unit numerator

Because `u<73/240<113/240`, the least-prime T3 shell is present. Its coefficient is

\[
\psi(r)=\frac{113}{20}-12u.
\]

With `Delta=93/20`, the exact pointwise base-minus-T3 coefficient is

\[
1-\frac{\psi(r)}\Delta
=\frac{12u-1}{\Delta}.
\]

Since `u>=1/6`,

\[
12u-1\ge1.
\]

Therefore

\[
\boxed{
(\text{base}-T_3)(n)\ge\frac1\Delta.
}
\tag{SRA6}

The full super-root pair penalty is at most `1/Delta` by (SRA5). Hence, pointwise,

\[
\boxed{
(\text{base}-T_3)(n)
-\frac1\Delta
\sum_{\substack{p>r,\ p\mid n\\rp>W}}
\kappa(u,t)
\ge0.
}
\tag{SRA7}

---

## 5. New hard carrier

All super-root ordered pairs are therefore removed from the T1–T2 analytic frontier.

After the high-LPF and super-root absorptions, every genuinely dangerous ordered pair must satisfy simultaneously

\[
\boxed{
\begin{aligned}
&z\le r<D^{73/240},\\
&r<p,\\
&rp\le W.
\end{aligned}
}
\tag{SRA8}

This is a purely sub-root carrier. At the Tier-A splice, the first anchor is below roughly `5.85e5`, and the second prime is bounded by `W/r`.

The least-prime-shell T1–T2 contribution and the sub-root pair carrier remain to be controlled. The source main must still be finite-normalized; no budget may be recredited merely from (SRA7) without replaying the positive decomposition.

---

## 6. Next

Fix the small least-prime anchor `r` and divide the square-basin interval by `r`. For `rp<=W`, the remaining quotient interval has length about `2K/r`; the pair shell becomes an `r`-rough prime-divisibility problem in that quotient interval. The existing adaptive interval-length anchor mechanism is the natural next tool: strip the fixed factor `r` with zero floor error before charging any analytic remainder.

No finite P2 theorem or all-K claim is made here.
