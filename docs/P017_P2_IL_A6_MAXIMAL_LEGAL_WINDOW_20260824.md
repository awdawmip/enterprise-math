# P017 — Iwaniec–Laborde `a=6` maximal legal window for the P2 short-interval bridge

Status: `PROVED_WIP PARAMETER COMPATIBILITY + NUMERICAL MAIN-TERM DIAGNOSTIC / NOT CANONICAL / NO EXPLICIT ALL-K P2 CLAIM`

Date: `2026-08-24`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Current canonical main seen before this checkpoint: `63f9c86a52bb1545b89903a8b204bc4b00041048`.

This supplement corrects one earlier exploratory parameter packet and isolates the maximal interval exponent compatible with the original Iwaniec–Laborde 1981 `a=6` architecture.

## 1. Setup

Write the short-interval length as

\[
y=x^\theta,
\]

and the linear-sieve level as

\[
D=x^d.
\]

Iwaniec–Laborde Lemma 4 gives bilinear control when the two factor blocks obey

\[
M\le yx^{-\varepsilon},\qquad
N\le yx^{-5/14-\varepsilon}.
\]

Thus the largest available product level is

\[
MN\le x^{2\theta-5/14-2\varepsilon},
\]

so asymptotically

\[
\boxed{d\le 2\theta-\frac5{14}.}
\]

In their fixed `a=6` weight, the small-prime cutoff is

\[
z=D^{1/6},
\]

so

\[
z^2=x^{d/3}.
\]

For the high-prime tail, Lemma 6 uses

\[
D_1=(y^3/x)^{1/2}x^{-2\varepsilon}
=x^{(3\theta-1)/2-2\varepsilon}
\]

and requires

\[
D_1\le z^2.
\]

Ignoring only the explicit epsilon slack, this forces

\[
\boxed{\frac d3\ge \frac{3\theta-1}{2}.}
\]

## 2. Maximal legal exponent

Combining

\[
\frac32(3\theta-1)\le d\le 2\theta-\frac5{14}
\]

gives

\[
9\theta-3\le4\theta-\frac57,
\]

hence

\[
\boxed{\theta\le\frac{16}{35}.}
\]

Therefore `16/35` is the maximal interval exponent compatible with *both* the original Lemma-4 bilinear factor range and the original Lemma-6 two-dimensional Selberg tail while keeping `a=6`.

At the boundary

\[
\boxed{\theta_*=\frac{16}{35}},
\]

one has

\[
d_*=2\theta_*-\frac5{14}=\frac{39}{70},
\]

so

\[
D=x^{39/70},\qquad
z=D^{1/6}=x^{13/140},\qquad
z^2=x^{13/70}.
\]

Also

\[
\frac{3\theta_*-1}{2}=\frac{13}{70},
\]

so the two principal exponents meet exactly:

\[
\boxed{z^2=x^{13/70},\qquad (y^3/x)^{1/2}=x^{13/70}.}
\]

The actual Lemma-4 product loses an `x^{-2\varepsilon}` factor while `D_1` itself also carries `x^{-2\varepsilon}`. Taking

\[
d=\frac{39}{70}-2\varepsilon
\]

gives

\[
z^2=x^{13/70-(2/3)\varepsilon},\qquad
D_1=x^{13/70-2\varepsilon},
\]

so the required strict inequality has positive epsilon slack.

## 3. Relation with the internal alpha parameter

Iwaniec–Laborde write

\[
D=x^{(1+\alpha)\theta}.
\]

At the limiting boundary,

\[
1+\alpha_*=\frac{d_*}{\theta_*}=\frac{39}{32},
\]

hence

\[
\boxed{\alpha_*=\frac7{32}.}
\]

Their weight relation becomes

\[
b+c+1=\frac6{(1+\alpha_*)\theta_*}=\frac{140}{13},
\]

so

\[
\boxed{b+c=\frac{127}{13}.}
\]

## 4. Negative boundary: the earlier theta=1/2, D=x^(5/9), a=6 packet is invalid

For

\[
\theta=\frac12,\qquad d=\frac59,\qquad a=6,
\]

we would have

\[
z^2=x^{5/27},
\]

whereas Lemma 6 requires comparison with

\[
(y^3/x)^{1/2}=x^{1/4}.
\]

Since

\[
\frac5{27}<\frac14,
\]

that packet violates `D_1 <= z^2`. It must not be reused as an Iwaniec–Laborde-valid parameter set.

This does **not** say a square-root-length P2 theorem is impossible. It says only that the unchanged original `a=6` high-prime-tail architecture cannot be pushed to `theta=1/2`.

## 5. Numerical main-term diagnostic at theta=16/35

The 1981 paper prints, for its `theta=0.45` optimum,

\[
c=5.1828\ldots,\qquad b=4.8698\ldots,\qquad G(b,c)=0.00177\ldots.
\]

Using the paper's explicit formula for `G`, these printed values determine the Laborde constants `B_1,B_2` to far more precision than is needed for route selection. Re-optimizing the same printed `a=6` main-term formula at

\[
\theta=\frac{16}{35},\qquad \alpha=\frac7{32},\qquad b+c=\frac{127}{13}
\]

gives approximately

\[
\boxed{b\approx4.61285,\qquad c\approx5.15638,\qquad G\approx0.0630.}
\]

A corner check over the uncertainty implied by the displayed `5.1828...` and `0.00177...` digits keeps the recomputed value above `0.0630` to the displayed precision.

Classification: this is a **robust numerical main-term diagnostic**, not promoted here to a theorem about the exact constants of Laborde 1979 because that source's exact `B_1,B_2` values have not yet been independently recovered from the primary paper in this branch.

The important route-selection fact is that the original `theta=0.45` proof's very small printed margin is not intrinsic once one uses the larger legal exponent available inside a square interval.

## 6. Square-basin consequence at the asymptotic level

The consecutive-square basin has width

\[
2K\asymp x^{1/2}.
\]

Since

\[
\frac{16}{35}<\frac12,
\]

a terminal subinterval of length `x^(16/35)` fits inside the square basin for all sufficiently large `K`.

Thus the 1981 theorem already supplies an asymptotic P2 existence route inside every sufficiently large consecutive-square interval. The project-specific open problem is **not** asymptotic existence itself. The live targets are:

1. make the constants effective enough to overlap a finite verification range;
2. determine whether the special square endpoint / P017 carry structure can lower that effective threshold;
3. alternatively, modify the high-prime tail architecture so the full `theta=1/2` basin can be used without violating Lemma 6.

## 7. P017 bridge retained

For the full square-basin hit count

\[
H_m(K)=\left\lfloor\frac{K^2+2K}{m}\right\rfloor-\left\lfloor\frac{K^2}{m}\right\rfloor,
\]

define

\[
O_m(K)=H_m(K)-H_{2m}(K).
\]

Then

\[
O_m(K)=\#\{n\in I_K:n/m\text{ is odd}\},
\]

and with

\[
r_K(m)=H_m(K)-\frac{2K}{m}
\]

one has the exact Chen-transfer identity

\[
\boxed{O_m(K)-\frac Km=r_K(m)-r_K(2m).}
\]

This means any bilinear theorem for the classical floor remainder transfers to the P017 odd-multiple carry remainder with no new distribution conjecture. What remains nontrivial is to exploit the *special square endpoint* strongly enough to improve explicit constants, rather than merely rewriting the classical remainder.

## 8. Current verdict

`PROVED_WIP`:

- exact maximal `a=6` compatibility exponent `theta_max=16/35`;
- exact limiting parameter identities `d=39/70`, `alpha=7/32`, `z=x^(13/140)`;
- exact invalidation of the prior `theta=1/2, d=5/9, a=6` packet;
- exact P017-to-Chen odd-remainder transfer.

`NUMERICAL_ROUTE_DIAGNOSTIC`:

- `b≈4.61285`, `c≈5.15638`, `G≈0.0630` from the printed 1981 calibration.

`OPEN`:

- source-exact recovery of Laborde's constants and a fully rigorous positive main-term bound at `theta=16/35`;
- explicit constants for Lemmas 4 and 6 sufficient for a concrete finite threshold;
- a full-basin `theta=1/2` modification (likely requiring a changed `a` or a different high-prime-tail estimate);
- any proof of a new all-K theorem beyond already-known classical asymptotic P2 results.
