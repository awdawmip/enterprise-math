# P017 — A6 Root-Complete Main Coefficient

Status: `PROVED_WIP SOURCE-DECIMAL ROOT-END SPECIALIZATION / FINITE PNT ERROR STILL OPEN / NOT CANONICAL / NO ALL-K P2 CLAIM`

Date: `2026-08-26`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- Iwaniec–Laborde, *P2 in short intervals* (1981), p.53–54;
- `docs/P017_P2_A6_FIVE_NINTH_ROOT_EDGE_PACKAGE_20260826.md`;
- `docs/P017_P2_SHARP_ODD_SIEVE_INVARIANCE_AND_W2_COLLAPSE_20260826.md`.

Companion checker:

`experiments/p017_p2_a6_root_complete_main_certificate_20260826.py`.

Purpose: move the W1/W2 **analysis split** all the way to the physical terminal prime horizon `D^(c/a)=x^(1/2)` while keeping the same a6 root-edge weighted sum. This makes W2 empty and removes the near-root terminal defect from the source-decimal main coefficient. It does not yet make the Mertens/PNT approximations in the 1981 main-term derivation explicit at the finite splice.

---

## 1. Root-edge parameters

Keep

\[
d=\frac59,
\qquad
D=x^d,
\qquad
a=6,
\qquad b=\frac{22}{5},
\qquad c=\frac{27}{5}.
\]

Then

\[
b+c+1=\frac ad,
\]

and

\[
D^{c/a}=x^{1/2}.
\]

The source weighted sum itself contains no prime beyond this terminal horizon.

For the purpose of splitting W into the part treated by the one-dimensional weighted-sieve main algebra and a separate high-prime tail, choose the split exactly at the root:

\[
y_{\rm split}=x^{1/2}=D^{c/a}.
\]

Then the separate high-prime piece is empty:

\[
\boxed{W_2=0,\qquad W_1=W.}
\tag{RC1}
\]

This is a decomposition choice for the weighted sum. It does not assert that the physical characteristic sequence must have length exactly `x^(1/2)`.

---

## 2. Exact alpha specialization

The p.53 notation is

\[
D=y_{\rm split}^{1+\alpha}.
\]

Since `D=x^(5/9)` and `y_split=x^(1/2)`,

\[
1+\alpha=\frac{10}{9},
\qquad
\boxed{\alpha=\frac19.}
\]

Hence the two terminal arguments in the Laborde-simplified main coefficient become

\[
\boxed{
\frac6{1+\alpha}=\frac{27}{5}=c,
}
\]

and

\[
\boxed{
\frac{6\alpha}{1+\alpha}=\frac35=6-c.
}
\]

Moreover

\[
\frac{cd}{6}=\frac12=y_{\rm split}\text{ exponent},
\]

so the terminal quadratic defect appearing in the preceding near-root packet vanishes exactly.

---

## 3. Source-decimal reconstruction

Use the same printed 1981 prefix intervals as the frozen a6 packet:

\[
5.1828\le c_0<5.1829,
\qquad
4.8698\le b_0<4.8699,
\qquad
0.00177\le G_0<0.00178.
\]

As before, recover the required `B_1` interval from the printed stationary point and eliminate `B_2` by subtracting the published reference identity. Every logarithm is enclosed by exact rational atanh-series arithmetic.

For a split parameter `theta_s`, write the nonconstant terminal part as

\[
N(c;\theta_s)
=-\frac c6\log\frac6{1+\alpha}
-\frac{6-c}{6}\log\frac{6\alpha}{1+\alpha}
-2\left(\frac{cd/6-\theta_s}{d/3}\right)^2,
\]

where

\[
\alpha=\frac d{\theta_s}-1.
\]

At the root-complete split `theta_s=1/2`, this collapses to

\[
\boxed{
N_{\rm root}(c)
=-\frac c6\log c
-\frac{6-c}{6}\log(6-c).
}
\tag{RC2}
\]

The quadratic term is exactly zero.

The reconstructed root-complete coefficient is

\[
G_{\rm root}
=G_0
+B_1[(c-b)-(c_0-b_0)]
+N_{\rm root}(c)-N_0(c_0).
\]

The exact-rational checker proves

\[
\boxed{
0.1148101168\ldots
<G_{\rm root}
<0.1149550428\ldots
}
\tag{RC3}
\]

and in particular

\[
\boxed{G_{\rm root}>\frac{287}{2500}=0.1148.}
\tag{RC4}
\]

---

## 4. Strict comparison with the preceding near-root split

Let `G_*` denote the frozen source-decimal coefficient with split exponent

\[
\theta_*=\frac{4999}{10000}.
\]

The common `G_0`, `B_1`, `B_2` and reference terms cancel in the difference. Thus

\[
G_{\rm root}-G_*
=N_{\rm root}(c)-N(c;\theta_*).
\]

The exact log enclosures prove

\[
\boxed{
4.0338871\times10^{-7}
< G_{\rm root}-G_*
<4.0339478\times10^{-7}.
}
\tag{RC5}
\]

Hence

\[
\boxed{G_{\rm root}>G_*}
\]

strictly. The improvement is numerically tiny, but its sign is rigorous and it confirms that moving the analysis split to the actual terminal root does not sacrifice the source main coefficient.

---

## 5. Full-basin interpretation and the finite-effectivity boundary

For the full square basin at a fixed `K`, take

\[
x=(K+1)^2,
\qquad
L=2K.
\]

The combinatorial weighted-sieve inequality is sequence-level, and the exact odd-projection theorem shows that all actual sifting functions may be evaluated on the sharp odd projection without changing their values.

The present note shows that the **source main-coefficient algebra** remains positive when the W1/W2 analysis split is completed at the physical root. Therefore there is no main-coefficient obstruction to using the full-basin sharp odd model.

However, (RC3)–(RC4) still inherit the asymptotic prime-sum/Mertens replacements used in the 1981 p.53–54 derivation. They are source-decimal coefficient certificates, not yet a fully explicit finite main-term lower bound at

\[
K_0=116009280740973308.
\]

The next finite gate is therefore precise:

> replace every Mertens/PNT `o(1)` or `epsilon` consumed in the root-complete W1 main term by explicit prime-product / Chebyshev-function bounds at the actual splice scales, and compare that explicit main lower bound with the already certified full-basin base conventional error `<0.00285 L` plus the prime-lift W1 errors.

No finite analytic P2 threshold, P2-in-every-square theorem or Legendre theorem is claimed here.
