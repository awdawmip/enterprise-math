# P017 — c=103/20 T1–T2 Two-Pair Pointwise Credit and z^2 Residual Rosser Collapse

Status: `PROVED_WIP EXACT TWO-PAIR POINTWISE CREDIT + EXACT FINITE ROSSER CENSUS / EXTERNAL FOUR-PRIME AGGREGATE STILL OPEN / NOT CANONICAL / NO FINITE P2 CLAIM`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_C515_T1_T3_SOURCE_MAP_AND_T3_BUCHSTAB_COLLAPSE_20260827.md`;
- `docs/P017_P2_C515_T12_SECOND_BUCHSTAB_PAIR_SHELL_20260827.md`;
- `docs/P017_P2_C515_T12_HIGH_PAIR_POINTWISE_ABSORPTION_20260827.md`;
- `docs/P017_P2_C515_T12_P23_ANCHOR_AFTER_SUFFIX_FACTORIZATION_20260827.md`;
- the beta-2 upper Rosser support condition.

Purpose: use the full pointwise base-minus-T3 credit before introducing any upper sieve. This removes the two largest ordered-pair penalties on every basin state. Any remaining T1–T2 pair is therefore supported only on a four-distinct-prime witness, which forces the residual upper-sieve level down to the already familiar `z^2` scale. At the Tier-A splice the corresponding Rosser support is then an exact finite family.

---

## 1. Pair kernel and pointwise budget

Write

\[
u=\frac{\log r}{\log D},\qquad t=\frac{\log p}{\log D},\qquad \frac16\le u<\frac{73}{240},
\]

for a dangerous least-prime anchor `r` and a larger divisor prime `p`.

The exact T1–T2 ordered-pair kernel is

\[
\kappa(u,t)
=\frac12+6\left[\min\left(u,\frac{113}{240}-t\right)-\frac16\right]_+.
\]

Since the minimum is at most `u`,

\[
\boxed{
\kappa(u,t)\le 6u-\frac12.
}
\tag{Z1}
\]

For fixed `u`, the right-hand side is exactly the maximum possible pair penalty.

The exact pointwise base-minus-T3 numerator on a state whose least prime is `r` is

\[
\boxed{12u-1.}
\tag{Z2}
\]

Therefore

\[
\boxed{
12u-1
=2\left(6u-\frac12\right)
\ge 2\kappa(u,t).
}
\tag{Z3}
\]

More generally, order all larger divisor primes of one state by decreasing pair penalty. By (Z1), the sum of the two largest pair penalties is at most

\[
2\left(6u-\frac12\right)=12u-1.
\]

Hence the complete base-minus-T3 pointwise credit can absorb the two largest T1–T2 ordered-pair penalties on every state:

\[
\boxed{
\text{only the third and subsequent larger-prime pairs can require an analytic estimate.}
}
\tag{Z4}

This is a pointwise inequality. No average estimate, Rosser upper sieve, Fourier expansion or factorization is used.

---

## 2. Every residual pair has a four-prime witness

Suppose a pair `(r,p)` survives after the two largest pair penalties have been credited pointwise. Then the same state contains at least two other distinct larger divisor primes `p_1,p_2` with

\[
r<p_1<p_2<p
\]

after relabeling the witness primes in increasing order.

Thus every residual pair occurrence lies on a state divisible by four distinct primes

\[
\boxed{r p_1p_2p.}
\tag{Z5}
\]

All four primes are at least

\[
z=D^{1/6}.
\]

Consequently

\[
\boxed{r p_1p_2p\ge z^4=D^{2/3}.}
\tag{Z6}
\]

If the remaining cofactor of such a conditioned four-prime shell is upper-sieved at the original total level `D`, its available sieve level satisfies

\[
\boxed{
Q_{\rm res}
\le \frac{D}{z^4}
=D^{1/3}
=z^2.
}
\tag{Z7}
\]

In the `W=K_0+1` coordinates of the live packet,

\[
D=W^{10/9},
\qquad
\boxed{z^2=W^{10/27}.}
\tag{Z8}
\]

This is exactly the same critical small-core scale that already appeared in the a6 collision compression.

Equation (Z7) is a ceiling for any residual upper-sieve shell obtained after conditioning on a four-prime witness. It does not, by itself, identify one unique global four-prime reindexing of the whole residual sum; that external aggregation remains the next task.

---

## 3. Tier-A prime alphabet at the z^2 ceiling

At

\[
K_0=116009280740973308,
\qquad W=K_0+1,
\]

an upper-Rosser state

\[
d=q_1\cdots q_s,
\qquad q_1>\cdots>q_s,
\]

at level `Q<=z^2` satisfies the beta-2 first-position condition

\[
q_1^3<Q\le W^{10/27}.
\]

Equivalently

\[
q_1^{81}<W^{10}.
\]

Exact integer exponentiation gives

\[
\boxed{127^{81}<W^{10}<131^{81}.}
\tag{Z9}
\]

Therefore every odd sieve prime is at most 127.

After the preferred P(23) anchor, all residual hard sieve primes are at least 29. Hence the hard prime alphabet is exactly contained in

\[
\boxed{
\{29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127\}.
}
\tag{Z10}
\]

There are 22 such primes.

---

## 4. Exact beta-2 support census after P(23)

For a descending squarefree prime tuple define

\[
q_{\rm crit}(d)
=
\max_{j\ \mathrm{odd}}
q_1\cdots q_{j-1}q_j^3.
\]

At the maximal residual level `z^2`, support is equivalent to

\[
q_{\rm crit}(d)<W^{10/27},
\]

which is checked exactly by

\[
q_{\rm crit}(d)^{27}<W^{10}.
\]

Exhaustive enumeration over the 22 hard primes in (Z10) gives

\[
\boxed{
\begin{array}{c|ccc}
\omega(d)&0&1&2\\\hline
\#\text{ states}&1&22&231
\end{array}}
\tag{Z11}
\]

and

\[
\boxed{\text{no supported state with }\omega(d)\ge3.}
\tag{Z12}
\]

Thus the complete P(23)-stripped hard inner Rosser carrier at the worst residual level has only

\[
\boxed{1+22+231=254}
\tag{Z13}
\]

states.

This is much stronger than the earlier uniform hard-depth bound `omega<=8`: once the two-pair pointwise credit has forced the level down to `z^2`, the hard inner Rosser depth is at most two.

---

## 5. Anchor-free comparison census

For robustness, remove the P(23) prestrip and allow every odd prime from 3 through 127. There are 30 such primes.

The same exact beta-2 enumeration at level `z^2` gives

\[
\boxed{
\begin{array}{c|rrrrrr}
\omega(d)&0&1&2&3&4&5\\\hline
\#\text{ states}&1&30&435&1153&1234&288
\end{array}}
\tag{Z14}
\]

with no supported state of depth six or more. The total is

\[
\boxed{3141.}
\tag{Z15}
\]

Therefore the finite collapse is not an artifact of the primorial anchor. P(23) simply compresses the already finite family from 3141 states to 254 hard states and removes small-prime floor errors exactly.

---

## 6. New analytic frontier

The internal Rosser-support complexity of residual T1–T2 is no longer an open problem.

After:

1. exact T3 Buchstab/Abel collapse;
2. high-LPF pointwise absorption;
3. super-root ordered-pair absorption;
4. high-pair `rp>=B` pointwise absorption;
5. two-pair pointwise credit;
6. P(23) exact prestrip;

any still-analytic T1–T2 contribution lives on an external four-distinct-prime carrier and has an inner hard Rosser state from a fixed 254-state family at worst.

The remaining load-bearing problem is therefore:

> canonically reindex and aggregate the external four-prime carrier, preserving the monotone prime-order/kernel cutoffs, and then charge the 254-state inner family without reintroducing a generic factorization multiplicity.

The finite source-main epsilon/Mertens normalization remains an independent open gate.

No finite P2 theorem, P2-in-every-square theorem, Legendre theorem, or canonical promotion is claimed here.
