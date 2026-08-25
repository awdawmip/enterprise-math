# P017 — Four-Sevenths P2: Trivial Exponent-Pair Reduction

Status: `PROVED_WIP POWER-BOOKKEEPING REDUCTION / EXACT RATIONAL CERTIFICATE / NOT CANONICAL / EFFECTIVE CONSTANTS STILL OPEN`

Date: `2026-08-25`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Base owner checkpoint: `736e6a1308972b39426e1013bd604b76cd457e88`

Prior-art source: H. Iwaniec and M. Laborde, *P2 in short intervals*, Ann. Inst. Fourier 31 (1981), especially Lemma 4 proof, conditions `(A2)–(A4)` and the trivial estimate (10).

## 1. Purpose

The four-sevenths package was originally frozen using the full admissible Iwaniec–Laborde Lemma-4 level. That proof eventually invokes the refined exponent pair `(1/14,11/14)` to weaken condition `(A4)`.

For effectivity this refinement is expensive: it introduces the most delicate oscillatory step and hides additional constants.

The present note shows that the four-sevenths level does **not need that step at all**. One can choose the bilinear split so that the original trivial `(1/2,1/2)` estimate (10) already satisfies `(A4)` with a large fixed rational margin.

## 2. Frozen square-interval parameters

Keep

\[
\theta=\frac{4999}{10000},
\qquad y=X^\theta,
\qquad D=X^{4/7},
\]

and freeze the internal Poisson/smoothing loss parameter at

\[
\varepsilon=\frac1{200}.
\]

Choose the factorization

\[
\boxed{
M=X^{25/56},
\qquad
N=X^{1/8}.
}
\]

Then

\[
MN=X^{25/56+1/8}=X^{32/56}=X^{4/7}=D.
\]

This split is close to the point at which the diagonal and trivial off-diagonal Cauchy losses balance.

## 3. Condition `(A2)` has fixed room

The proof of Lemma 4 bounds the diagonal term using the sufficient condition

\[
M<yx^{-6\varepsilon}.
\]

The exponent margin is

\[
\theta-6\varepsilon-\frac{25}{56}
=
\boxed{\frac{1643}{70000}}
\approx0.0234714>0.
\]

Hence `(A2)` is satisfied with substantial fixed power room.

## 4. Conditions `(A3)` and `(A4)` are automatic

The trivial estimate (10) is used under

\[
(A3)\qquad MN^2<X.
\]

Here

\[
MN^2=X^{25/56+1/4}=X^{39/56},
\]

so the `(A3)` exponent margin is

\[
1-\frac{39}{56}=\boxed{\frac{17}{56}}.
\]

The paper's sufficient trivial-zone condition is

\[
(A4)\qquad
MN^2\le y^{5/2}X^{-1/2-4\varepsilon}.
\]

Its right-hand exponent is

\[
\frac52\theta-\frac12-4\varepsilon
=\frac{2919}{4000}.
\]

Therefore the exact exponent margin is

\[
\frac{2919}{4000}-\frac{39}{56}
=
\boxed{\frac{933}{28000}}
\approx0.0333214>0.
\]

Thus the refined `(1/14,11/14)` exponent-pair argument is unnecessary for this parameter package.

## 5. Direct power saving from the diagonal term

The displayed diagonal estimate in the Lemma-4 proof is

\[
T_{=}(H,M,N)
\ll
M^2 y^{-1}X^{3\varepsilon}.
\]

Since Cauchy gives

\[
M|S(H,M,N)|^2\le T(H,M,N),
\]

the diagonal contribution to `|S|^2` has exponent

\[
\frac{25}{56}-\theta+3\varepsilon
=
-\boxed{\frac{2693}{70000}}.
\]

Consequently its square-root saving is

\[
\boxed{\delta_{\rm diag}=\frac{2693}{140000}}
\approx0.0192357.
\]

This is power bookkeeping from the paper's displayed estimate; the implied numerical constant is not yet extracted.

## 6. Direct power saving from the trivial off-diagonal term

Under `(A3)`, equation (10) gives in the paper

\[
T_{\ne}(H,M,N)
\ll
\left(\frac{MN}{y}\right)^2
\left(\frac{X}{y}\right)^{1/2}
X^{3\varepsilon}.
\]

Dividing by `M` after Cauchy, the exponent of the resulting bound for `|S|^2` is

\[
2\left(\frac47-\theta\right)
+\frac{1-\theta}{2}
+3\varepsilon
-\frac{25}{56}
=
-\boxed{\frac{1073}{28000}}.
\]

Hence

\[
\boxed{
\delta_{\rm off}=\frac{1073}{56000}
}
\approx0.0191607.
\]

The off-diagonal term is the slightly weaker of the two.

Therefore, before explicit treatment of the paper's hidden constants and polylogarithmic factors, the four-sevenths bilinear block has structural power room

\[
\boxed{
|S(H,M,N)|
\ll X^{-1073/56000+o(1)}.
}
\]

## 7. A convenient effective target

For later constant engineering reserve the simpler target

\[
\boxed{|S(H,M,N)|\le C X^{-1/100}}
\]

because

\[
\frac{1073}{56000}-\frac1{100}
=
\boxed{\frac{513}{56000}}
\approx0.0091607.
\]

Thus almost half the available power saving can be spent absorbing explicit logarithmic factors, smoothing constants, Fourier-tail constants, and finite-block decomposition constants.

This note does **not** yet provide the numerical constant `C` or the corresponding finite `X_0`.

## 8. Why this changes the effectivity frontier

The earlier effectivity plan treated the refined `(1/14,11/14)` exponent-pair stage as the central object to make explicit. That is no longer necessary for `D=X^(4/7)`.

The remaining analytic constants come from a substantially simpler chain:

1. choose an explicit compactly supported weight on the square interval;
2. make the Poisson/Fourier truncation quantitative;
3. quantify the diagonal divisor/logarithmic factor;
4. quantify the trivial transformed estimate (10), equivalently the `(1/2,1/2)` exponent-pair/B-process bound;
5. multiply by the explicit number of bilinear blocks from the Rosser–Iwaniec sieve decomposition;
6. compare the resulting error against the already certified main reserve
   \[
   C_1-C_2>0.145713553.
   \]

The delicate refined exponent-pair proof and its `5/14` boundary are no longer on the critical path for this package.

## 9. P017 interface is unchanged

For the square basin the exact parity projection remains

\[
(H_m-H_{2m})-\frac Km
=r_K(m)-r_K(2m).
\]

The present reduction concerns only how the resulting bilinear remainder is bounded; it does not claim that the P017 carry representation itself supplies new cancellation.

## 10. Next

Make step 2 effective using an explicit compactly supported smoothing kernel or an exact P017-compatible Fourier majorant, then derive a numerical constant for the trivial estimate (10). Compare the resulting threshold with the `D=X^(5/9)` package only after the complete finite constant budget is available.
