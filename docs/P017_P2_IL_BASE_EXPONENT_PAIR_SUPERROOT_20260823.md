# P017 — Base Exponent-Pair Super-Root Margin for the Square P2 Route

Status: `PROVED PARAMETER SPECIALIZATION OF IWANIEC–LABORDE + ROUTE SIMPLIFICATION / NOT AN EXPLICIT P2 THEOREM / NOT CANONICAL`

Date: `2026-08-23`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on:

- `docs/P017_P2_CHEN_CARRY_BRIDGE_20260823.md`;
- `docs/P017_P2_IL_SQUARE_PARAMETER_MARGIN_20260823.md`;
- Iwaniec–Laborde (1981), especially Lemma 4 and equations `(A4)`, `(16)`, `(17)`.

## 1. Question

The 1981 proof of the pointwise short-interval `P2` theorem ultimately uses the exponent pair

\[
(\kappa,\lambda)=\left(\frac1{14},\frac{11}{14}\right)
\]

in order to push the interval exponent down to `theta=0.45`.

For the square interval we have the wider exponent

\[
\theta=\frac12.
\]

The question is whether the advanced exponent pair is still necessary for crossing the square-root sieve level.

The answer is **no**.

The circle-method rearrangement of Iwaniec–Laborde is still needed, but after that rearrangement the basic exponent pair

\[
\boxed{(\kappa,\lambda)=(1/2,1/2)}
\]

already allows a total sieve level strictly beyond `x^(1/2)`.

## 2. Why the pre-circle-method trivial bound cannot cross the root

Before the circle-method rearrangement, Iwaniec–Laborde obtain condition `(A4)` from their direct use of equation `(10)`.  At the power level, suppressing only the additional negative epsilon loss, `(A4)` is

\[
MN^2\le y^2x^{-1/2}.
\]

For a square interval

\[
y=x^{1/2},
\]

this becomes

\[
MN^2\le x^{1/2}.
\]

But the linear-sieve total level is

\[
D=MN.
\]

Since `N>1`,

\[
MN^2>MN=D.
\]

Therefore any choice

\[
D>x^{1/2}
\]

violates `(A4)` already at the power level.

Hence:

\[
\boxed{\text{the direct pre-circle-method bound cannot cross the square-root level.}}
\]

This is a genuine negative boundary.

## 3. Iwaniec–Laborde equation (17)

After their Lemma 5 / circle-method reorganization, Iwaniec–Laborde replace `(A4)` by the exponent-pair condition

\[
N
\le
 y^{\frac32+\frac54\kappa-\frac34\lambda}
 x^{\frac14\lambda-\frac12-\frac34\kappa-4\varepsilon}.
\]

This formula is consistent with their printed specialization

\[
(\kappa,\lambda)=\left(\frac1{14},\frac{11}{14}\right)
\Longrightarrow
N\le yx^{-5/14-4\varepsilon}.
\]

## 4. Specialization to the base pair `(1/2,1/2)`

Substitute

\[
\kappa=\lambda=\frac12.
\]

The `y` exponent becomes

\[
\frac32+\frac58-\frac38=\frac74,
\]

and the `x` exponent becomes

\[
\frac18-\frac12-\frac38=-\frac34.
\]

Therefore equation `(17)` gives

\[
\boxed{
N\le y^{7/4}x^{-3/4-4\varepsilon}.
}
\]

For the square-window exponent `y=x^(1/2)`, this is

\[
\boxed{
N\le x^{1/8-4\varepsilon}.
}
\]

## 5. Total level

The diagonal condition in the same proof requires

\[
M\le yx^{-6\varepsilon}.
\]

Thus we may take, at the power level,

\[
M=x^{1/2-6\varepsilon},
\qquad
N=x^{1/8-4\varepsilon},
\]

which yields

\[
\boxed{
D=MN=x^{5/8-10\varepsilon}.
}
\]

Consequently the base exponent pair supports every fixed level

\[
\boxed{D=x^d\quad\text{with}\quad d<5/8}
\]

once the epsilon bookkeeping is chosen sufficiently small.

This is already strictly beyond the parity/square-root level `x^(1/2)`.

## 6. Reference level `d=5/9`

For the Matomäki-like reference choice

\[
d=\frac59,
\]

the power gap to the base-pair ceiling is exactly

\[
\boxed{
\frac58-\frac59=\frac5{72}\approx0.0694444.
}
\]

The displayed epsilon bookkeeping permits any

\[
\varepsilon<\frac1{10}\left(\frac58-\frac59\right)
=\frac1{144}.
\]

At `x=10^31`, the bare power ratio corresponding to the full `5/72` exponent gap is

\[
x^{5/72}\approx1.42\times10^2.
\]

The last number is only a scale diagnostic: the published proof replaces the true gap by several `x^{\pm\varepsilon}` cushions and has unspecified implied constants.

## 7. Better explicit-engineering tradeoff

The companion main-term computation shows that `d=5/9` is not sacred.  With the reconstructed Laborde constants, near

\[
d\approx0.54184
\]

one still has a positive main-term coefficient about

\[
G\approx0.06682,
\]

while the base-pair level gap is

\[
\frac58-d\approx0.08316.
\]

At `x=10^31`, the bare corresponding power ratio is about

\[
3.8\times10^2.
\]

This is again a numerical route diagnostic, not an error theorem.  It strongly suggests that an explicit proof should optimize `d` against actual constants rather than maximize the sieve level.

## 8. Consequence for explicitization

The advanced exponent pair `(1/14,11/14)` is essential to the **1981 record exponent `theta=0.45`**, but it is not load-bearing for the **square-window specialization `theta=1/2`**.

The minimum analytic mechanism needed for the square route is:

1. Iwaniec's bilinear linear-sieve remainder representation;
2. Iwaniec–Laborde's Lemma-5 circle-method reorganization of the off-diagonal remainder;
3. only the terminal/base exponent pair `(1/2,1/2)`.

Modern explicit analytic-number-theory literature supplies corrected explicit second-derivative / terminal `B(0,1)` machinery, so the remaining task is no longer to explicitize a deep exponent-pair chain.

The real remaining work is to replace the 1981 `O`, `<<`, smoothing and `x^{epsilon}` bookkeeping by explicit constants while preserving enough of the actual exponent gap.

## 9. P017 interface

P017 still transfers the ordinary interval remainder to the binary-carry observable exactly:

\[
\left(H_m-H_{2m}\right)-\frac Km
=
\left(H_m-\frac{2K}{m}\right)
-
\left(H_{2m}-\frac K m\right).
\]

Thus no new carry-distribution theorem is required after an explicit bilinear remainder estimate is obtained: the ordinary short-interval estimate applies twice, at moduli `m` and `2m`.

## 10. New frontier

Do **not** spend effort explicitizing `(1/14,11/14)` first.

The next load-bearing question is:

> Can the Iwaniec–Laborde circle-method proof with terminal `(1/2,1/2)` be re-run with exact dyadic/smoothing constants so that, for some optimized `0.53<d<0.56`, the resulting error is below the positive Laborde main term at `x=10^31`?

If yes, Campbell's finite `P2` range and the explicitized asymptotic square-window sieve overlap.
