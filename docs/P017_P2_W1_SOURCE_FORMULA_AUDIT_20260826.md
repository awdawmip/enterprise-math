# P017 — P2 W1 Source-Formula Audit and Corrected Rational Reserve

Status: `CORRECTION / PROVED_WIP SOURCE-FORMULA AUDIT + EXACT RATIONAL CERTIFICATE / NOT CANONICAL / NO ALL-K P2 CLAIM`

Date: `2026-08-26`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Supersedes only the **W1 numerical reserve claims** in:

- `docs/P017_P2_EFFECTIVE_FOUR_SEVENTHS_PACKAGE_20260825.md`;
- `docs/P017_P2_EFFECTIVE_FIVE_NINTH_PACKAGE_20260825.md`.

The parameter identities and exponent-window checks in those notes are not invalidated by this audit.

Prior-art source audited: H. Iwaniec and M. Laborde, *P2 in short intervals*, Ann. Inst. Fourier 31 (1981), 37–56, especially the unsimplified lower bound for `W_1` on p. 53.

---

## 1. Audit finding

Let

\[
C_0=2e^\gamma.
\]

In the exact linear-sieve zone used by the `a=4` packages,

\[
F(s)=\frac{C_0}{s}.
\]

The source p. 53 formula contains, among its four negative integrals, the terms

\[
-\int
\left(\frac{b+1}{a}-2t\right)
F\!\left(\frac{1-t}{t}\right)\frac{dt}{t}
\]

and

\[
-2\int
(c-at)F(a-at)\frac{dt}{t}.
\]

Two transcription/normalization errors entered the 2026-08-25 parameter notes.

### Error A — third integral

After dividing by `C_0`,

\[
\frac{F((1-t)/t)}{C_0}
=\frac{t}{1-t}.
\]

Because the source measure already contains `dt/t`, the normalized integrand is therefore

\[
\left(\frac{b+1}{a}-2t\right)\frac{dt}{1-t},
\]

not the expression obtained by inserting an additional factor `1/t`.

### Error B — fourth integral

The source formula has a literal leading factor `2` in front of the fourth integral. The 2026-08-25 packages effectively used half of this contribution.

These two errors partially offset numerically in the four-sevenths package, but not enough to preserve its old stated reserve. In the five-ninth package the corrected `W_1` coefficient changes sign.

---

## 2. Rigorous logarithm enclosure used below

For rational `x>0`, put

\[
z=\frac{x-1}{x+1}.
\]

Then

\[
\log x
=2\sum_{k=0}^{N}\frac{z^{2k+1}}{2k+1}+R_N,
\]

with the elementary tail bound

\[
\boxed{
|R_N|
\le
\frac{2|z|^{2N+3}}
{(2N+3)(1-z^2)}.
}
\]

Thus every logarithm used in this note admits an exact rational lower and upper enclosure. The companion script performs only `fractions.Fraction` arithmetic.

---

## 3. Corrected `D=X^(4/7)` package

Keep

\[
\theta=\frac{4999}{10000},\qquad
D=X^{4/7},\qquad
a=4,\quad b=\frac52,\quad c=\frac72.
\]

The source-normalized integrals are:

\[
J_1=\frac14\log5,
\]

\[
8J_2=
\log\left(\frac{8^8 3^7 5^5 7}{63^8}\right),
\]

\[
\boxed{
J_3
=\frac38+\frac98\log\frac34,
}
\]

and, with the exact upper endpoint `theta/d=34993/40000`,

\[
\boxed{
J_4
=\frac14\log\left[
\left(\frac{34993}{25000}\right)^7
\frac{1669}{5000}
\right].
}
\]

Here

\[
\Delta=2c-b-1=\frac72,
\qquad
\frac{2a}{\Delta}=\frac{16}{7}.
\]

Hence the corrected normalized `W_1` coefficient is

\[
\boxed{
C_1^{(4/7)}
=2\log3
-\frac{16}{7}(J_1+J_2+J_3+J_4).
}
\]

Numerically this is approximately

\[
C_1^{(4/7)}\approx0.1066640276.
\]

Using only the rational logarithm enclosure above with `N=6`, the executable certificate proves the simpler exact lower bound

\[
\boxed{
C_1^{(4/7)}>\frac{533}{5000}=0.1066.
}
\]

The previously derived Lemma-6 tail coefficient is unaffected by the present normalization audit:

\[
C_2^{(4/7)}
=\frac{128}{174790063}.
\]

Therefore the corrected certified net reserve is

\[
\boxed{
C_1^{(4/7)}-C_2^{(4/7)}
>
\frac{93162463579}{873950315000}
\approx0.1065992677.
}
\]

So the four-sevenths package remains genuinely positive, but the former claim `>0.145713553` is superseded.

---

## 4. Corrected `D=X^(5/9)` package

Keep

\[
\theta=\frac{4999}{10000},\qquad
D=X^{5/9},\qquad
a=4,\quad b=\frac{13}{5},\quad c=\frac{18}{5}.
\]

The source-normalized integrals are:

\[
J_1=\frac14\log\frac{39}{7},
\]

\[
20J_2=
\log\left(
\frac{5^{20}13^{13}7^7}{3^{21}11^{22}}
\right),
\]

\[
\boxed{
J_3
=\frac25+\frac{11}{10}\log\frac{11}{15},
}
\]

and

\[
\boxed{
J_4
=\frac15\log\left[
\left(\frac{44991}{32500}\right)^9
\frac{5009}{17500}
\right].
}
\]

Since

\[
\Delta=\frac{18}{5},
\qquad
\frac{2a}{\Delta}=\frac{20}{9},
\]

the corrected coefficient is

\[
\boxed{
C_1^{(5/9)}
=2\log3
-\frac{20}{9}(J_1+J_2+J_3+J_4).
}
\]

Numerically,

\[
C_1^{(5/9)}\approx-0.0026546768.
\]

More importantly, the exact rational logarithm enclosure with `N=20` proves

\[
\boxed{
C_1^{(5/9)}< -\frac{3}{2500}=-0.0012.
}
\]

Thus the `a=4`, root-edge five-ninth package is **not a positive `W_1` package**. Its previous stated reserve `>0.04666595` is invalid and must not be used in any downstream effectivity comparison.

This does not say that level exponent `5/9` is intrinsically impossible with some other choice of sieve parameters; it invalidates this particular `a=4, b=13/5, c=18/5` specialization.

---

## 5. One-parameter root-edge family

For later re-optimization, keep `a=4` and force the upper weighted-prime cutoff to the root by

\[
D^{c/a}=X^{1/2}.
\]

Writing

\[
D=X^d,
\]

gives

\[
\boxed{
c=\frac2d,\qquad b=\frac2d-1.}
\]

Then

\[
b+c+1=\frac4d=\frac ad,
\]

and

\[
\Delta=2c-b-1=\frac2d,
\qquad
\frac{2a}{\Delta}=4d.
\]

Numerical evaluation of the **corrected** source formula places the positivity boundary near

\[
\boxed{d_*\approx0.55591.}
\]

This value is diagnostic only until a rational bracketing certificate is frozen. It explains why `d=5/9` lies on the wrong side of the corrected boundary while `d=4/7` remains safely positive.

For the trivial-pair bilinear route with the asymptotic loss parameters temporarily suppressed, balancing the diagonal and off-diagonal powers gives

\[
\mu=d+\frac14-\frac{3\theta}{4},
\]

and the structural square-root saving

\[
\boxed{
\delta_{\rm triv}(d)
=\frac{7\theta}{8}-\frac d2-\frac18.
}
\]

Hence moving `d` upward improves main-term reserve but weakens the bilinear power saving. The corrected finite-threshold problem is therefore a genuine one-dimensional tradeoff, not the previous four-sevenths versus five-ninth comparison.

---

## 6. Effectivity consequence

The source audit changes the active route selection:

1. retain `d=4/7` as a valid positive baseline, now with certified net reserve `>0.1065992677`;
2. retire the existing `d=5/9` `a=4` package from the positive comparison set;
3. do not continue explicit-constant optimization against the obsolete `0.145713553` or `0.04666595` budgets;
4. re-optimize `d` using the corrected `W_1` formula before doing further Fourier/B-process constant engineering;
5. keep the P017 square-specific complement, collision-kernel and primorial-anchor reductions as independent ways to reduce the analytic remainder.

No P2-in-every-square theorem, no Legendre theorem, and no finite analytic threshold is claimed by this audit.
