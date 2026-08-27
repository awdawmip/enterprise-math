# P017 — c=103/20 T1–T2 Preferred Global P(41)-Length Anchor

Status: `PROVED_WIP EXACT GLOBAL PRESTRIP + SEVEN-FACTOR HARD DEPTH / PREFERRED OVER P31 / NOT CANONICAL / NO FINITE P2 CLAIM`

Date: `2026-08-27`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_ADAPTIVE_PRIMORIAL_LENGTH_ANCHOR_20260823.md`;
- `docs/P017_P2_C515_T12_GLOBAL_P31_ANCHOR_PRESTRIP_20260827.md`.

Purpose: optimize the common primorial-length anchor at the Tier-A splice. `P(41)` strips two additional hard sieve primes relative to the P31 checkpoint while sacrificing less than `0.08%` of the full basin length. `P(43)` gives no further hard-depth reduction and costs more than `4%` of the interval, so P41 is the preferred finite anchor.

---

## 1. Exact common interval

Put

\[
K_0=116009280740973308,
\qquad W=K_0+1,
\qquad L=2K_0.
\]

The primorial through 41 is

\[
\boxed{
Q_{41}=P(41)=304250263527210<K_0.
}
\]

The largest `Q_41`-multiple below the full basin length is

\[
\boxed{
L_{41}=762Q_{41}=231838700807734020.
}
\tag{P41-1}

The discarded terminal tail is exactly

\[
\boxed{
2K_0-L_{41}=179860674212596<Q_{41}.
}
\tag{P41-2}

Hence

\[
K_0<L_{41}<2K_0
\]

and the common interval

\[
J_{41}=(K_0^2,K_0^2+L_{41}]
\]

lies inside the square basin.

The relative length loss is

\[
\boxed{
\frac{2K_0-L_{41}}{2K_0}<\frac{776}{10^6}=0.000776.
}
\tag{P41-3}

Thus the retained interval exceeds `99.9224%` of the full basin.

---

## 2. Exact prestrip through 41

For every remaining sub-root ordered pair `z<=r<p`, `rp<=W`, and every odd squarefree Rosser modulus `d|P(r)`, put

\[
e=(d,Q_{41}),
\qquad d=e b.
\]

Because `r,p>z>41` and `e|Q_41|L_41`, the adaptive anchor identity gives

\[
\boxed{
H_{rpd}(K_0^2,L_{41})
=H_{rpb}\!\left(
\left\lfloor\frac{K_0^2}{e}\right\rfloor,
\frac{L_{41}}{e}
\right).
}
\tag{P41-4}

The same identity holds for the sharp floor discrepancy.

Therefore every sieve-prime factor through 41 is removed from the hard denominator before analytic estimation. In the odd channel the remaining hard factor `b` has all prime factors at least

\[
\boxed{43.}
\]

---

## 3. Uniform hard depth drops to seven

For a sub-root ordered pair,

\[
r,p\ge z=D^{1/6},
\]

so the inner upper-sieve level is

\[
Q=\frac D{rp}\le D^{2/3}=W^{20/27}.
\]

The stripped hard part satisfies `b<Q`. Exact integer exponentiation at the Tier-A splice proves

\[
\boxed{43^8>W^{20/27}.}
\tag{P41-5}

Equivalently, after clearing the 27th root,

\[
43^{216}>W^{20}.
\]

Hence an eight-prime hard factor is impossible and

\[
\boxed{\omega(b)\le7.}
\tag{P41-6}

The crude size test does not rule out seven hard factors, so seven is the correct uniform depth obtained by this argument.

---

## 4. Why P(41), not P(43)

At the same splice,

\[
P(43)=13082761331670030<K_0,
\]

so a P43 anchored interval exists. But the largest P43 multiple below `2K_0` retains only about `95.86%` of the full basin, a loss greater than `4.1%`.

Prestripping 43 would raise the first hard prime from 43 to 47, but

\[
47^7<W^{20/27}<47^8,
\]

so the uniform hard-depth bound remains seven.

Thus P43 pays a much larger interval cost without improving the depth class. P41 is therefore preferred for the c515 finite route.

The earlier P31 note remains mathematically valid but is superseded as the preferred finite anchor.

---

## 5. Remaining task

The T1–T2 sub-root problem is now a common-interval sieve whose genuinely hard Rosser modulus has at most seven prime factors, all at least 43. The next decision is between:

1. a direct fixed-depth canonical factorization of these at-most-seven hard primes; or
2. the Iwaniec well-factorable upper-sieve variant, for which modern formulations give at most `1/epsilon` convolution pieces for any prescribed two-factor level split.

No finite P2 theorem or all-K claim is made here.
