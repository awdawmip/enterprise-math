# PREFIX-1036 — Critical-frequency Bessel tail and accelerated signed-density probes

Date: 2026-11-23 (Asia/Shanghai). Parent: PREFIX-1035. Status: AUTHOR_ANALYTIC_PROOF / NUMERICAL_EXPLORATION / NOT_REVIEWED.

## Frozen object and provenance

Scientific foundation stays at awdawmip/enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json (P000 V5). The Stage46 candidate signed BRC kernel W=J12-6I12, incoming -e1, Link {0,e1} blocked in both directions, exactly one outgoing negative step, and the native X6 Cell–terminal-port–grade coherent observer are unchanged. This note analyzes only the **derived six-phase scalar spectral observable**, not native signed state equivalence.

Input sources: PREFIX-1026 fixed signed functional, PREFIX-1033 global continuous density, PREFIX-1034 Morse critical cusp, and PREFIX-1035 all-order collision recurrence / Picard–Fuchs route. In particular, let the six independent unit complex phases be z_j, L=|sum_j z_j|², μ=law(L), ρ=its spectral density, and ν(dy)=g(y)dy, with

\[
5g=4(H\rho)'-2P\rho+12(11+y)U,\quad
H=y^2(36-y)^2,\quad P=y(y-36)(17y-91),\quad
U(y)=\int_y^{36}(6-s)\rho(s)\,ds.
\]

The inherited six-phase moment identity gives \(\int s\,d\mu(s)=6\); hence \(U(y)=\int_0^y(s-6)\rho(s)\,ds\). All assertions about g inherit the PREFIX-1033 density representation and its prior analytic obligations.

## Theorem 1: single-Bessel integral for the signed contrast

For every 0<y<36, set r=√y, and write J_j for the ordinary Bessel function of integer order j. Then

\[
\boxed{g(y)=\int_0^\infty K(t;y)\,dt}
\]
with the **absolutely convergent** integrand
\[
\boxed{
K(t;y)=\frac{J_0(t)^6}{5}
\left[
(2H'(y)-P(y))tJ_0(rt)
-\frac{H(y)}{r}t^2J_1(rt)
+12(11+y)\left(r(y-6)J_1(rt)-\frac{2y}{t}J_2(rt)\right)
\right].
}
\]

The apparent t=0 denominator is removable, since J_2(rt)=O(t²).

Proof. The characteristic function of the planar sum of six independent unit phases is J_0(t)^6. Radial Fourier inversion yields
\[
\rho(y)=\tfrac12\int_0^\infty tJ_0(t)^6J_0(t\sqrt y)\,dt,
\quad
\rho'(y)=-\frac1{4\sqrt y}\int_0^\infty t^2J_0(t)^6J_1(t\sqrt y)\,dt.
\]
For each fixed y>0 both integrals converge absolutely at infinity: J_0(t)^6=O(t^{-3}), J_j(rt)=O_y(t^{-1/2}). Differentiation holds uniformly on compact subintervals of (0,36).

For R=√y, integrate the first formula in s from 0 to y against (s-6), swap absolutely convergent integrals and use
\(\int_0^R xJ_0(tx)\,dx=RJ_1(tR)/t\) and
\(\int_0^R x^3J_0(tx)\,dx=R^3J_1(tR)/t-2R^2J_2(tR)/t^2\).
This gives
\[
U(y)=\int_0^\infty J_0(t)^6
\left[R(y-6)J_1(tR)-\frac{2y}{t}J_2(tR)\right]dt.
\]
Substitute into the inherited g identity. This proves the formula and its convergence. QED.

## Theorem 2: exact resonant truncation law at y=4 and y=16

Define I_T(y)=∫_0^T K(t;y)dt. For each fixed y∈(0,36)\{4,16},
\[
\boxed{g(y)-I_T(y)=O_y(T^{-3/2})\qquad(T\to\infty).}
\]
At the two interior critical spectral values, the leading nonoscillatory tail survives and
\[
\boxed{
g(4)=I_T(4)-\frac{3072\sqrt2}{\pi^{7/2}\sqrt T}
       +O(T^{-3/2}),
}
\]
\[
\boxed{
g(16)=I_T(16)-\frac{3840}{\pi^{7/2}\sqrt T}
       +O(T^{-3/2}).
}
\]

Proof. For fixed r>0 the leading Hankel expansions are
\[
J_0(t)=\sqrt{2/(\pi t)}\cos(t-\pi/4)+O(t^{-3/2}),
\]
\[
J_1(rt)=\sqrt{2/(\pi rt)}\cos(rt-3\pi/4)+O_r(t^{-3/2}).
\]
In K the sole order t^{-3/2} contribution is from the t²J_1(rt) term:
\[
K(t;y)=-\frac{H(y)}{5r}\left(\frac2\pi\right)^3
\sqrt{\frac2{\pi r}}\,
t^{-3/2}\cos^6(t-\pi/4)\cos(rt-3\pi/4)
+O_y(t^{-5/2}).
\]
The exact trigonometric identity
\[
32\cos^6 x=10+15\cos2x+6\cos4x+\cos6x
\]
shows a zero-frequency product only for r=2,4 (r=6 is the excluded endpoint y=36). At nonresonant r, termwise integration by parts yields O_y(T^{-3/2}); the remainder integrates absolutely with the same bound. For r=2,4, the constant Fourier coefficients of the oscillatory product are respectively 15√2/128 and 6√2/128. Hence
\[
K(t;4)=C_4t^{-3/2}+(\text{nonzero-frequency terms})+O(t^{-5/2}),\quad
C_4=-1536\sqrt2/\pi^{7/2},
\]
\[
K(t;16)=C_{16}t^{-3/2}+(\text{nonzero-frequency terms})+O(t^{-5/2}),\quad
C_{16}=-1920/\pi^{7/2}.
\]
The corresponding tail is 2C_y/√T+O(T^{-3/2}). QED.

**Interpretation:** the same spectral critical values 4 and 16 that carry the Morse cusps also cause anomalously slow Bessel-quadrature convergence. Explicit subtraction restores the nonresonant T^{-3/2} asymptotic order. The error O-constants are *not yet effective*, so this theorem is not a finite-T certified interval for g.

## Numerical exploration (not an interval certificate)

The accompanying script PREFIX1036_R6_BESSEL_RESONANT_PROBE.py evaluates ∫_0^20 K by adaptive Gauss–Kronrod and ∫_20^T K by composite Simpson with step 0.05, using SciPy Bessel functions. It then adds 2C_y/√T. All numbers below are approximate:

| y | T | uncorrected I_T | corrected I_T+2C_y/√T |
|---:|---:|---:|---:|
| 4 | 800 | 117.707929 | 114.913027 |
| 4 | 1600 | 116.891259 | 114.914964 |
| 4 | 3200 | 116.312348 | 114.914896 |
| 4 | 6400 | 115.903400 | 114.915253 |
| 16 | 800 | 24.819702 | 22.349334 |
| 16 | 1600 | 24.092547 | 22.345733 |
| 16 | 3200 | 23.582373 | 22.347189 |
| 16 | 6400 | 23.220410 | 22.347003 |

The corrected values are consistent with g(4)≈114.915 and g(16)≈22.347, **numerical estimates rather than strict positive lower bounds**. An independent symbolic check simplifies 2H'-P=-y(y-36)(9y+53), C_4=-1536√2/π^{7/2}, C_16=-1920/π^{7/2}. No native BRC propagation was run.

## Next discrimination

1. Make the Bessel Hankel remainder bounds explicit, enclosing the tail at a concrete T and independently enclosing the finite-interval quadrature, first at y=4 and 16. That would convert the two positive numerical estimates into rigorous signs.
2. Use the same integral and the spectral ODE/Frobenius data to enclose g on compact subintervals of (0,4),(4,16),(16,36). The constants degrade near resonance; use the explicit correction locally.
3. The whole-interval question g≥0 and infinite Hausdorff positivity remain open; B_fix,odd(32)∈{19,20} remains the original mother question.

Scientific artifact may be published as independent portable work. Historical author attribution from PREFIX-1035 remains EM-DIRECT-FBEA5D / RA-3FB2D033BE6048D8712FF056, but this note does not claim a new authenticated logical-session binding, a live Task CLAIM, Activity checkpoint, or independent review.
