# P017 — P2 Explicit B-Spline Balanced Effectivity Package

Status: `PROVED_WIP EXPLICIT FOURIER-TAIL PACKAGE + EXACT EXPONENT CERTIFICATE / NOT CANONICAL / NO FINITE P2 THRESHOLD YET`

Date: `2026-08-25`

Owner branch: `research/p017-p2-chen-carry-bridge-20260823`

Current prior owner head seen before this package: `924a23dd074e265c1544c4df59ae9bfd5df4c34a`

Purpose: replace the unspecified high-derivative `C^infinity` smoothing in the Iwaniec–Laborde remainder proof by a concrete compact B-spline whose Fourier transform and tail are exactly computable, then balance the diagonal, trivial off-diagonal, and Fourier-tail power losses inside the four-sevenths level.

## 1. Base square-interval package

Keep

\[
\theta=\frac{4999}{10000},\qquad y=X^\theta,\qquad D=X^{4/7}.
\]

The main-term package already has certified reserve

\[
C_{\rm main}>0.145713553.
\]

The exact P017 carry interface remains

\[
(H_m-H_{2m})-\frac Km=r_K(m)-r_K(2m).
\]

This note changes only the smoothing / Fourier truncation used to represent the floor remainder.

## 2. Explicit order-p B-spline

Let `p>=3`, put

\[
a=\frac yp,
\]

and let

\[
u_a=\mathbf 1_{[-a/2,a/2]}.
\]

Define

\[
f_{p,y}(t)=p a^{1-p}\,u_a^{*p}(t).
\]

Then, exactly:

1. `f_{p,y}(t)>=0`;
2. `supp(f_{p,y}) subseteq [-y/2,y/2]`;
3. \(\int_\mathbb R f_{p,y}(t)\,dt=y\);
4. for the Fourier convention \(\widehat f(\xi)=\int f(t)e(-\xi t)dt\),

\[
\boxed{
\widehat f_{p,y}(\xi)
=y\left(\frac{\sin(\pi a\xi)}{\pi a\xi}\right)^p.
}
\]

Hence a translate of this function is a nonnegative weight supported entirely inside a length-y target interval. Positivity of its weighted P2 count implies existence of an actual P2 state in that interval.

## 3. Exact Fourier-tail bound

For a modulus `d`, Poisson summation gives a Fourier series with main frequency `h=0` equal to `y/d`. Truncating at positive frequency `H`, and using

\[
|\sin t|\le1,
\qquad
\sum_{h>H}h^{-p}\le \frac{H^{1-p}}{p-1},
\]

gives

\[
\boxed{
|r_{\rm tail}(d)|
\le
C_p\left(\frac{d}{yH}\right)^{p-1},
\qquad
C_p=\frac{2p^p}{\pi^p(p-1)}.
}
\]

For dyadic moduli `d<=4D`, choose

\[
H=\frac{4D}{y}X^\eta.
\]

Then

\[
\boxed{
|r_{\rm tail}(d)|\le C_p X^{-\eta(p-1)}.
}
\]

If one crudely sums over at most `4D` moduli with coefficients bounded by one, then

\[
\boxed{
R_{\rm tail}\le4C_pD X^{-\eta(p-1)}.
}
\]

This intentionally crude form is useful for effectivity pressure-testing; later sieve-factorability can only improve the counting of active coefficients.

## 4. Freeze p=7 and eta=1/70

Take

\[
\boxed{p=7,\qquad \eta=\frac1{70}}.
\]

Using only \(\pi>3\),

\[
C_7
<\frac{2\,7^7}{3^7\,6}
=\boxed{\frac{823543}{6561}}
<126.
\]

Thus a completely elementary tail constant is available:

\[
R_{\rm tail}
<\frac{3294172}{6561}
D X^{-3/35}.
\]

Relative to the natural interval scale `y`, its power saving is

\[
\delta_{\rm tail}
=(p-1)\eta-(d-\theta)
=\frac{6}{70}-\left(\frac47-\frac{4999}{10000}\right)
=\boxed{\frac{993}{70000}}
\approx0.0141857.
\]

## 5. Balanced bilinear split

Choose

\[
\boxed{
M=X^{16/35},\qquad N=X^{4/35}.
}
\]

Then

\[
MN=X^{20/35}=X^{4/7}=D.
\]

Also

\[
MN^2=X^{24/35}<X,
\]

with margin

\[
1-\frac{24}{35}=\frac{11}{35}.
\]

The split is selected by balancing the three raw power losses rather than optimizing one of them in isolation.

## 6. Diagonal power saving

Keeping the Fourier cutoff `H=(4D/y)X^eta` explicit instead of absorbing it into a generic epsilon, the displayed diagonal term in the Iwaniec–Laborde Cauchy argument has the structural exponent

\[
\mu-\theta+\eta.
\]

For \(\mu=16/35\),

\[
\mu-\theta+\eta
=-\frac{1993}{70000}.
\]

Hence the square-root saving is

\[
\boxed{
\delta_{\rm diag}=\frac{1993}{140000}
}
\approx0.0142357.
\]

The numerical implied constant is not asserted here.

## 7. Trivial off-diagonal power saving

Using the paper's trivial `(1/2,1/2)` / estimate-(10) route and keeping the explicit Fourier cutoff exponent `eta`, the structural exponent after Cauchy is

\[
2(d-\theta)+\frac{1-\theta}{2}+\frac52\eta-\mu.
\]

Substitution gives

\[
2\left(\frac47-\theta\right)
+\frac{1-\theta}{2}
+\frac{5}{2}\frac1{70}
-\frac{16}{35}
=-\frac{793}{28000}.
\]

Therefore

\[
\boxed{
\delta_{\rm off}=\frac{793}{56000}
}
\approx0.0141607.
\]

Again, this is exact exponent bookkeeping before numerical extraction of the analytic constant.

## 8. Three-way balance

The three structural savings are

\[
\delta_{\rm diag}
=\frac{1993}{140000}
\approx0.0142357,
\]

\[
\delta_{\rm off}
=\frac{793}{56000}
\approx0.0141607,
\]

and

\[
\delta_{\rm tail}
=\frac{993}{70000}
\approx0.0141857.
\]

Thus all three lie in the narrow interval

\[
0.01416<\delta<0.01424.
\]

This is the main reason for freezing this package: no single generic effectivity loss is orders of magnitude worse than the other two at the power-exponent level.

## 9. What this does and does not achieve

This package makes the Fourier tail genuinely explicit and removes dependence on unspecified high derivatives of an arbitrary `C^infinity` cutoff.

It does **not** yet give a useful numerical threshold. A deliberately crude pressure test, summing the explicit tail over all possible moduli and allowing generic bilinear constants, indicates that straightforward constant tracking can still force an astronomically large `X_0`. Therefore this package establishes `EFFECTIVITY_IN_PRINCIPLE`, not `CAMPBELL_RANGE_OVERLAP`.

The correct route-selection conclusion is:

- do not return to the refined `(1/14,11/14)` exponent pair merely for asymptotic power;
- do use this B-spline package as a clean baseline for constant accounting;
- in parallel, inspect later pointwise P2 work of H.-Q. Liu / Sargos-Wu / Jie Wu for stronger exponential-sum savings with effective constants;
- if those constants remain too expensive, the remaining opportunity for a material finite-threshold improvement is square-specific structure, not another representation of the same generic carry remainder.

## 10. Prior-art / novelty boundary

B-splines, Poisson summation, sinc Fourier transforms, and van der Corput estimates are classical. The present object is only a project-specific explicit parameter packaging of prior mathematics around the exact P017 parity-projected remainder. No historical novelty claim is made.

## 11. Next

1. derive a numerical constant for the terminal `(1/2,1/2)` exponential-sum estimate using a modern explicit second-derivative / Kuzmin-Landau lemma;
2. audit H.-Q. Liu (1996), whose P2 short-interval theorem explicitly states an effective positive main constant, and H.-Q. Liu's triple-exponential-sum improvements;
3. compare finite threshold budgets, not just asymptotic exponents;
4. only then decide whether a square-specific P017 cancellation theorem is necessary.
