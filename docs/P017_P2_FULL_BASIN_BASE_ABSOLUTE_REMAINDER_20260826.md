# P017 — Full-Basin Sharp-Odd Base Absolute Remainder

Status: `PROVED_WIP FINITE CONVENTIONAL-ERROR CERTIFICATE / MAIN-TERM REPLAY STILL OPEN / NOT CANONICAL / NO ALL-K P2 CLAIM`

Date: `2026-08-26`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- Iwaniec, *A new form of the error term in the linear sieve* (1980), especially the conventional linear-sieve error `R(A,D)=sum_{d<D,d|P(z)} |r(A,d)|` recorded before the factorable refinement;
- `docs/P017_P2_SHARP_ODD_SIEVE_INVARIANCE_AND_W2_COLLAPSE_20260826.md`;
- the canonical full square-basin P017 carry representation.

Companion checker:

`experiments/p017_p2_full_basin_base_absolute_remainder_20260826.py`.

Purpose: quantify the conventional one-dimensional linear-sieve error on the **entire** consecutive-square basin before any bilinear/factorable decomposition is introduced. This note does not transfer the previously frozen source-decimal `G_*` coefficient to the new full-basin normalization and does not yet control the prime-lifted W1 terms.

---

## 1. Full-basin normalization

At the finite splice put

\[
K_0=116009280740973308,
\qquad W=K_0+1,
\qquad x=W^2.
\]

The square basin is

\[
I_{K_0}=\{K_0^2+1,\ldots,K_0^2+2K_0\},
\]

with exact length

\[
L=2K_0.
\]

Its odd projection contains exactly `K_0` states.

Keep the a6 root-edge level and sifting scale relative to this right-end scale:

\[
D=x^{5/9}=W^{10/9},
\qquad
z=x^{5/54}=W^{5/27}.
\]

Then the terminal prime horizon remains exactly

\[
D^{(27/5)/6}=x^{1/2}=W.
\]

For every odd squarefree `d`, the sharp odd divisibility count on an even-length interval satisfies

\[
A_d^{\rm odd}=\frac{L}{2d}+e(d),
\qquad |e(d)|<1.
\]

Thus the conventional absolute remainder is bounded by the **number of active odd squarefree sieve moduli**.

---

## 2. Exact finite prime cutoff

The checker proves by integer exponentiation

\[
1439^{27}<W^5<1447^{27}.
\]

Since `1439` and `1447` are consecutive primes,

\[
\boxed{p<z\iff p\le1439}
\]

for primes at the splice. Excluding the already-projected prime `2`, there are exactly `227` relevant odd primes.

---

## 3. Rankin count of all conventional sieve moduli

Let

\[
N(D,z)
=
\#\left\{
 d<D:
 d\mid\prod_{3\le p<z}p
\right\}.
\]

Take

\[
\sigma=\frac47.
\]

Rankin's inequality gives

\[
N(D,z)
\le
D^{4/7}
\prod_{3\le p<z}\left(1+p^{-4/7}\right).
\]

Since

\[
D=W^{10/9},
\]

this is

\[
N(D,z)
\le
W^{40/63}
\prod_{3\le p\le1439}\left(1+p^{-4/7}\right).
\tag{F1}
\]

For each of the 227 odd primes, the checker upper-encloses `p^(-4/7)` using exact integer seventh roots. For `0<t<1`, use the alternating-series upper bound

\[
\log(1+t)
\le
 t-\frac{t^2}{2}+\frac{t^3}{3}-\frac{t^4}{4}+\frac{t^5}{5}.
\]

The resulting all-rational certificate gives

\[
\boxed{
\sum_{3\le p\le1439}\log(1+p^{-4/7})
<9.16811.
}
\tag{F2}
\]

No prime number theorem, Dickman asymptotic or floating-point inequality is used in the certificate.

---

## 4. Comparison with K

Because `K_0=W-1`, (F1) yields

\[
\frac{N(D,z)}{K_0}
\le
\exp\left(
-\frac{23}{63}\log W
+\log\frac{W}{W-1}
+\sum_{3\le p\le1439}\log(1+p^{-4/7})
\right).
\]

Use

\[
\log\frac{W}{W-1}<\frac1{K_0}.
\]

The checker lower-bounds `log W` with positive atanh-series partial sums after writing

\[
W=10^{17}\frac{W}{10^{17}}.
\]

Combining this with the rational product upper bound gives

\[
\frac{23}{63}\log W
-\frac1{K_0}
-\sum_{3\le p\le1439}\log(1+p^{-4/7})
>5.1767557\ldots.
\]

A positive Taylor lower bound for the exponential, through degree 11, already proves

\[
\exp(5.1767557\ldots)>rac{10000}{57}.
\]

Therefore

\[
\boxed{
N(D,z)<\frac{57}{10000}K_0.
}
\tag{F3}
\]

---

## 5. Base conventional linear-sieve remainder

The conventional error term in the one-dimensional linear sieve is

\[
R_0
=
\sum_{\substack{d<D\\d\mid P_{\rm odd}(z)}}|e(d)|.
\]

Since `|e(d)|<1`, (F3) gives

\[
\boxed{
R_0<\frac{57}{10000}K_0.
}
\tag{F4}
\]

Relative to the **full basin length** `L=2K_0`,

\[
\boxed{
\frac{R_0}{L}<\frac{57}{20000}=0.00285.
}
\tag{F5}
\]

This is the first full-basin conventional-error certificate at the existing finite splice.

---

## 6. What this does and does not establish

The finite advantage of the full-basin model is now rigorous at the remainder level:

- the odd population is exactly `K`;
- every one-dimensional sieve remainder remains pointwise `<1`;
- the available physical interval length is `2K`;
- the entire base conventional error is `<0.00285` of that length.

However, the source-decimal a6 coefficient

\[
G_*>0.1148
\]

was extracted from the 1981 short-interval W1/W2 analysis with `y=x^(4999/10000)`. This note deliberately does **not** assert that the same normalized main coefficient transfers unchanged when the characteristic sequence is enlarged to the whole square basin.

The next required theorem is therefore one of the following equivalent forms:

1. replay the W1 weighted linear-sieve main term directly for the full-basin sharp odd sequence using conventional absolute errors; or
2. prove a monotone embedding that consumes the old short-interval main certificate inside the full basin while charging full-basin carry errors only where justified.

Only after that normalization is fixed may (F5) be compared directly with a positive weighted-sieve reserve.

Prime-lift W1 remainder terms also remain to be bounded. No finite analytic P2 threshold, P2-in-every-square theorem or Legendre theorem is claimed here.
