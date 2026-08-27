# P017 — c=103/20 T1–T2 High-Pair Pointwise Absorption

Status: `PROVED_WIP EXACT POINTWISE ABSORPTION / LOW-PAIR SECTOR REMAINS / NOT CANONICAL / NO FINITE P2 CLAIM`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_C515_T12_SECOND_BUCHSTAB_PAIR_SHELL_20260827.md`;
- `docs/P017_P2_C515_T12_SUPERROOT_PAIR_ABSORPTION_20260827.md`;
- `docs/P017_P2_C515_T12_P37_ANCHOR_AND_BN_SPLIT_20260827.md`.

Purpose: remove the entire sub-root high-pair sector `rp>=B` pointwise, before any Rosser upper sieve or analytic factorization is charged.

---

## 1. Setup

Keep the c515 packet

\[
a=6,\qquad b=\frac{93}{20},\qquad c=\frac{103}{20},\qquad D=W^{10/9}.
\]

Write

\[
u=\frac{\log r}{\log D},\qquad t=\frac{\log p}{\log D}
\]

for an ordered pair shell with

\[
\frac16\le u<\frac{73}{240},\qquad r<p,\qquad rp\le W.
\]

The T1–T2 pair kernel is

\[
\kappa(u,t)
=\frac12+6\left[\min\left(u,\frac{113}{240}-t\right)-\frac16\right]_+.
\]

Put

\[
\boxed{B=D^{b/a}=D^{31/40}.}
\]

The high-pair sector is

\[
\boxed{rp\ge B,\qquad u+t\ge\frac{31}{40}.}
\]

---

## 2. Kernel collapse on the high-pair sector

From

\[
t\ge\frac{31}{40}-u
\]

we get

\[
\frac{113}{240}-t
\le
\frac{113}{240}-\frac{186}{240}+u
=u-\frac{73}{240}<0<\frac16.
\]

Hence the positive part vanishes identically and

\[
\boxed{rp\ge B\Longrightarrow\kappa(u,t)=\frac12.}
\tag{HP1}
\]

---

## 3. At most three high-pair larger primes

Fix one basin state `n<W^2=D^(9/5)` with least prime exponent `u`.

If `k` distinct larger divisor primes all satisfy `rp_i>=B`, then

\[
t_i\ge\frac{31}{40}-u
\]

and therefore

\[
\log_D n
\ge
u+\sum_{i=1}^k t_i
\ge
\frac{31k}{40}-(k-1)u.
\tag{HP2}
\]

For `k=4`, using `u<73/240`,

\[
\frac{124}{40}-3u
>
\frac{31}{10}-\frac{219}{240}
=\frac{35}{16}
>\frac95.
\]

Thus four such primes are impossible:

\[
\boxed{\#\{p>r:p\mid n,\ rp\ge B\}\le3.}
\tag{HP3}
\]

For `k=3`, (HP2) requires

\[
\frac{93}{40}-2u<\frac95,
\]

hence

\[
\boxed{u>\frac{21}{80}.}
\tag{HP4}
\]

Consequently

\[
\boxed{
\begin{array}{ll}
1/6\le u\le21/80 &: \#p\le2,\\
21/80<u<73/240 &: \#p\le3.
\end{array}}
\tag{HP5}
\]

---

## 4. Base-minus-T3 absorbs the whole high-pair penalty

On the dangerous least-prime range, the already-combined base-minus-T3 numerator is

\[
\boxed{12u-1.}
\]

The common denominator is

\[
\Delta=2c-b-1=\frac{93}{20}.
\]

If `u<=21/80`, then

\[
12u-1\ge1
\]

while by (HP1),(HP5) the total high-pair penalty numerator is at most

\[
2\cdot\frac12=1.
\]

If `u>21/80`, then

\[
12u-1>
12\frac{21}{80}-1
=\frac{43}{20}
>\frac32,
\]

while the total high-pair penalty numerator is at most

\[
3\cdot\frac12=\frac32.
\]

Therefore, pointwise on every basin state,

\[
\boxed{
(\text{base}-T_3)(n)
-\frac1\Delta
\sum_{\substack{p>r,\ p\mid n\\B\le rp\le W}}
\kappa(u,t)
\ge0.
}
\tag{HP6}
\]

No Rosser upper sieve, factorable decomposition, Fourier expansion, or average estimate is used.

---

## 5. New hard carrier

The super-root sector `rp>W` was already absorbed pointwise. The present result removes the remaining high-pair sub-root sector `B<=rp<=W`.

Hence every ordered pair that still requires analytic treatment satisfies

\[
\boxed{
\begin{aligned}
&z\le r<D^{73/240},\\
&r<p,\\
&rp<B=D^{31/40}.
\end{aligned}}
\tag{HP7}
\]

For this low-pair sector the natural c515 factorization is

\[
Q(r,p)=\frac D{rp}=\frac{B}{rp}\,D^{9/40},
\]

with

\[
D^{9/40}=x^{1/8}=W^{1/4}.
\]

The P(37) anchor and fixed-depth hard Rosser analysis should therefore be charged only on (HP7), not on the high-pair sector eliminated here.

No finite P2 theorem, all-K theorem, or canonical promotion is claimed.
