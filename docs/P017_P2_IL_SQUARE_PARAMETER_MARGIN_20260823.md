# P017 — Iwaniec–Laborde Square-Window Parameter Margin

Status: `REPRODUCED PARAMETER CERTIFICATE + ROUTE NARROWING / NOT AN EXPLICIT P2 THEOREM / NOT CANONICAL`

Date: `2026-08-23`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on: `docs/P017_P2_CHEN_CARRY_BRIDGE_20260823.md`.

## 1. Why this checkpoint exists

The 1981 Iwaniec–Laborde theorem proves a pointwise `P2` in intervals of length `x^0.45` for sufficiently large `x`.  For the square basin we only need the wider scale `y=x^(1/2)`.

The purpose of this checkpoint is to quantify how far the square-window specialization lies from the 1981 critical parameter boundary.

It does **not** make the ineffective phrase `sufficiently large` explicit, and it does **not** claim an all-`K` semiprime theorem.

## 2. Published Iwaniec–Laborde main-term function

In the notation of section 7 of Iwaniec–Laborde, set

`D=x^d=y^(1+alpha)`, `a=6`.

Their final lower-bound coefficient is controlled by

\[
G(b,c)=B_1(c-b)+B_2
-\frac c6\log\frac6{1+\alpha}
-\frac{6-c}{6}\log\frac{6\alpha}{1+\alpha}
-2\left(\frac{c\theta(1+\alpha)-6\theta}{3(3\theta-1)}\right)^2,
\]

with

\[
b+c+1=\frac6d.
\]

The paper reports at its critical choice `theta=0.45`

\[
c=5.1828\ldots,\qquad b=4.8698\ldots,\qquad G=0.00177\ldots.
\]

The constants `B1,B2` are the constants `B,D` from Laborde's 1979 Buchstab-weight paper.

## 3. Numerical reconstruction of the Laborde constants

The published critical-point equation

\[
c=
\left(2B_1+\frac16\log\alpha\right)
\left(\frac{3(3\theta-1)}{2(1+\alpha)\theta}\right)^2
+\frac6{1+\alpha}
\]

allows `B1` to be reconstructed from the printed `theta,c`; substituting the printed `G,b,c` into the displayed formula for `G` then reconstructs `B2`.

Using the printed values gives approximately

\[
B_1\approx0.2433071,\qquad B_2\approx1.3382043.
\]

This inverse reconstruction is used only as a numerical certificate.  To make a formal explicit theorem one should import independently certified explicit values/intervals for Laborde's constants rather than rely on printed-decimal inversion.

## 4. Square-window specialization at `D=x^(5/9)`

Take

\[
\theta=\frac12,\qquad d=\frac59,\qquad \alpha=\frac19.
\]

The constraints

\[
3\le b<\frac{6\theta}{d}<c\le6
\]

are satisfied near the optimum

\[
\boxed{
 c\approx5.61945,\qquad b\approx4.18055.
}
\]

Substitution into the published `G` formula gives

\[
\boxed{G\approx0.12805.}
\]

This should be compared with `0.00177...` at the original `theta=0.45` critical point: the square-window main term is not close to zero.

### Coarse robustness check

To avoid leaning on the final printed digit, widen the published critical data far beyond the displayed rounding:

\[
5.182\le c_0\le5.184,
\quad
4.869\le b_0\le4.871,
\quad
0.0017\le G_0\le0.0019.
\]

Reconstruct `B1,B2` at all endpoint combinations and evaluate the square case at the simple fixed choice `c=5.62`.  The resulting minimum is still

\[
\boxed{G>0.1271.}
\]

Thus the conclusion that the square specialization has a large positive main-term margin is insensitive to the displayed numerical rounding.

## 5. Independent analytic level margin

The same 1981 bilinear framework permits, up to its small epsilon loss,

\[
D_{\max}=y^2x^{-5/14}
=x^{2\theta-5/14}.
\]

At `theta=1/2`,

\[
\boxed{D_{\max}=x^{9/14+o(1)}}.
\]

Our reference choice `D=x^(5/9)` therefore lies below the ceiling by

\[
\boxed{
\frac9{14}-\frac59=\frac{11}{126}\approx0.0873016.
}
\]

At `x=10^31` the bare power ratio is only

\[
x^{11/126}\approx5.08\times10^2.
\]

That number is important: it is a real margin, but it is **not** large enough to dismiss explicit constants and logarithmic losses by handwaving.

## 6. A more favorable level/main-term tradeoff exists

Using the same reconstructed constants and optimizing `G` for `theta=1/2` over the admissible Laborde family shows that positivity begins numerically near

\[
d\approx0.52855.
\]

This is diagnostic, not a formal theorem because of the reconstructed constants.  It shows that the square problem does not need to run near `D_max=x^(9/14)`.

A useful middle choice is around `d≈0.54`: it retains a visibly positive main term while increasing the power separation from the bilinear ceiling.  Therefore an explicit proof should optimize **main-term margin versus explicit remainder constants**, not maximize the sieve level.

## 7. Interface with P017

For the square basin

\[
I_K=(K^2,(K+1)^2),\qquad x\asymp K^2,
\]

P017 supplies

\[
O_m(K)=H_m(K)-H_{2m}(K),
\]

and the exact remainder transfer

\[
\boxed{
O_m(K)-\frac Km
=
\left(H_m(K)-\frac{2K}{m}\right)
-
\left(H_{2m}(K)-\frac K m\right).
}
\]

Thus any explicit pointwise Iwaniec–Laborde bilinear estimate for the ordinary interval remainder transfers to the binary-carry remainder with at most the two scales `m` and `2m`.

The earlier P017 identity expressing the full Möbius carry field as a roughness-displacement discrepancy is a negative boundary: generic carry/Fourier reformulation alone does not improve the sieve.  Any project-specific gain must exploit the square diagonal/low-height coupling or improve explicit constants.

## 8. Current frontier after this checkpoint

The mathematical route is now separated cleanly:

1. **Asymptotic existence:** already prior art, since Iwaniec–Laborde prove the stronger `x^0.45` pointwise `P2` theorem.
2. **Square-window parameter positivity:** strongly noncritical; reproduced here with `G>0.127` at `D=x^(5/9)`.
3. **Analytic level room:** `11/126` power separation from the 1981 ceiling at that choice.
4. **Missing load-bearing object:** a fully explicit version of the relevant bilinear/Fourier remainder bounds, with constants small enough to start at or below the finite `P2` overlap supplied by the modern consecutive-square computation.

The next attack should test whether, at the wider square exponent and a deliberately shallower `D`, the pre-`(1/14,11/14)` second-derivative estimate in Iwaniec–Laborde is already sufficient.  If yes, explicitization reduces to standard explicit second-derivative van der Corput constants.  If not, make only the exact surviving exponent-pair step explicit.

## Artifact

`experiments/p017_p2_il_square_parameter_margin.py`
