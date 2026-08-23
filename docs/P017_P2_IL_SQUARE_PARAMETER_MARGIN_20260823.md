# P017 — Iwaniec–Laborde Square-Window Parameter Margin

Status: `REPRODUCED + SELBERG-LEVEL-CORRECTED PARAMETER CERTIFICATE / NOT AN EXPLICIT P2 THEOREM / NOT CANONICAL`

Date: `2026-08-23`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Depends on: `docs/P017_P2_CHEN_CARRY_BRIDGE_20260823.md`.

## 1. Purpose and boundary

Iwaniec–Laborde (1981) prove a pointwise `P2` in intervals of length `x^0.45` for sufficiently large `x`.  A consecutive-square interval has the wider length scale `y=x^(1/2+o(1))`.

This note quantifies the parameter margin of the square specialization.  It does **not** make `sufficiently large` explicit and does **not** claim an all-`K` semiprime theorem.

An earlier version of this note mechanically substituted `theta=1/2` into the paper's final displayed `G(b,c)` formula.  That misses one section-6 hypothesis: the two-dimensional Selberg level must also satisfy `D1<=z^2`.  The present version repairs that point exactly.

## 2. Main-term notation

Write

\[
D=x^d=y^{1+\alpha},\qquad a=6,\qquad z=D^{1/6},
\]

and

\[
b+c+1=\frac6d.
\]

The Laborde constants `B1,B2` can be numerically reconstructed from the printed 1981 optimum

\[
\theta=0.45,\quad c=5.1828\ldots,\quad b=4.8698\ldots,\quad G=0.00177\ldots,
\]

giving approximately

\[
B_1\approx0.2433071,\qquad B_2\approx1.3382043.
\]

This inverse reconstruction is a numerical certificate only.  A fully explicit theorem should import independently certified intervals for the Laborde constants.

## 3. General section-6 Selberg penalty

Iwaniec–Laborde Lemma 6 gives

\[
T(\mathcal A,z;y,w)
\le
\left(2\frac{\log(w/y)}{\log D_1}\right)^2\frac{y}{\log w}
+O\!\left(\frac{\varepsilon y}{\log y}\right),
\]

under

\[
D_1\le (y^3/x)^{1/2}x^{-2\varepsilon},
\qquad
D_1\le z^2,
\qquad
y<w<y^{3/2}.
\]

For the Laborde high-prime weight one has

\[
w=D^{c/6}.
\]

Let

\[
\delta_1=\frac{\log D_1}{\log x}.
\]

After normalizing by the same common factor used in section 7, the exact high-prime penalty contributed by Lemma 6 is

\[
\boxed{
2\left(\frac{cd/6-\theta}{\delta_1}\right)^2.
}
\]

When the original 1981 choice

\[
\delta_1=\frac{3\theta-1}{2}
\]

is legal, this reduces to their printed final expression.

## 4. Legal square-window Selberg level

Now set

\[
\theta=\frac12.
\]

The analytic Lemma-6 ceiling has exponent

\[
\frac{3\theta-1}{2}=\frac14,
\]

whereas

\[
z^2=D^{1/3}=x^{d/3}.
\]

For every level of interest here (`d<5/8`),

\[
\frac d3<\frac14.
\]

Thus the binding condition is `D1<=z^2`.  We may take asymptotically

\[
\boxed{
\delta_1=\frac d3-o(1).
}
\]

The square-window main coefficient is therefore governed by the corrected function

\[
\boxed{
G_{\rm sq}(b,c;d)=
B_1(c-b)+B_2
-\frac c6\log\frac6{1+\alpha}
-\frac{6-c}{6}\log\frac{6\alpha}{1+\alpha}
-2\left(\frac{cd/6-1/2}{d/3}\right)^2,
}
\]

with

\[
\alpha=2d-1,
\qquad
b=\frac6d-1-c.
\]

Equivalently, the last penalty is

\[
\frac12\left(c-\frac3d\right)^2.
\]

## 5. Corrected reference point `d=5/9`

Take

\[
d=\frac59,\qquad \alpha=\frac19.
\]

Optimizing the corrected legal function gives approximately

\[
\boxed{
 c\approx5.52041,
 \qquad
 b\approx4.27959,
 \qquad
 G_{\rm sq}\approx0.12208.
}
\]

All power-level section-6 constraints are then compatible:

- `D1=z^(2-o(1))`;
- `D1<(y^3/x)^(1/2)` because `d/3<1/4`;
- `z^2<y` because `d/3<1/2`;
- `w>y` because `c>3/d`;
- `w<y^(3/2)` with a wide exponent margin.

Thus the earlier mechanically extrapolated value `G≈0.12805` was slightly optimistic, but the fully section-6-compatible correction still leaves a large positive coefficient around `0.122`.

## 6. Section-5 bilinear level margin

The strongest 1981 exponent pair gives

\[
D_{\max}=y^2x^{-5/14+o(1)}=x^{9/14+o(1)}
\]

at `theta=1/2`, so `d=5/9` lies below that ceiling by `11/126`.

More importantly for explicitization, the companion note

`docs/P017_P2_IL_BASE_EXPONENT_PAIR_SUPERROOT_20260823.md`

shows that after the Iwaniec–Laborde circle-method rearrangement even the base exponent pair `(1/2,1/2)` permits

\[
\boxed{D=x^{5/8-O(\varepsilon)}}.
\]

Hence the advanced `(1/14,11/14)` pair is not load-bearing for the square specialization.

At `d=5/9`, the base-pair exponent gap is

\[
\boxed{\frac58-\frac59=\frac5{72}}.
\]

## 7. P017 interface

For the square basin

\[
I_K=(K^2,(K+1)^2)
\]

P017 gives

\[
O_m(K)=H_m(K)-H_{2m}(K)
\]

and the exact ordinary-to-binary remainder transfer

\[
\boxed{
O_m(K)-\frac Km
=
\left(H_m(K)-\frac{2K}{m}\right)
-
\left(H_{2m}(K)-\frac K m\right).
}
\]

Thus an explicit pointwise bilinear estimate for the ordinary short-interval floor remainder transfers to the binary-carry remainder at the two scales `m` and `2m`.

The older P017 identity `carry field = shifted roughness count - origin roughness count` remains a negative boundary: generic carry/Fourier repackaging by itself does not beat the classical sieve.

## 8. Current frontier

The corrected picture is now:

1. asymptotic square-window `P2` is prior art, since Iwaniec–Laborde prove the stronger `x^0.45` pointwise theorem;
2. the square-window Laborde main term remains strongly positive after enforcing the missing `D1<=z^2` condition (`G_sq≈0.12208` at `d=5/9`);
3. the section-5 deep remainder can be run with only the base exponent pair `(1/2,1/2)` after the circle-method rearrangement;
4. the missing load-bearing object is therefore **explicit constant bookkeeping**, not a new sieve or a deep exponent-pair chain.

The next high-value task is to rerun section 5 with exact exponent gaps rather than one global `x^epsilon` cushion, using a modern corrected explicit terminal B-process / second-derivative estimate, and compare the resulting numerical error with the positive `G_sq` margin near the finite-computation overlap.

## Artifact

`experiments/p017_p2_il_square_parameter_margin.py` is updated to use the legal Selberg cap.
