# PREFIX-1038 — Explicit strictly positive neighborhoods of both interior spectral critical values

Date: 2026-11-23 (Asia/Shanghai).
Parent frontier: PREFIX-1037 (derived six-phase scalar spectral observer).
Status: AUTHOR_EXACT_CONDITIONAL_PROOF / EXACT_RATIONAL_BOUND_CHECK / NOT_INDEPENDENTLY_REVIEWED.

## Scientific inputs and type boundary

Frozen P000 V5: enterprise-math@f42f2906d77f24085c123f3ccfe9667d41caa96d:p000_reality_foundation.json. The associated Stage46 signed BRC candidate, native six-axis X6 joint Cell–terminal-port–grade observer, paths, provenance and noncollapsed residuals remain unchanged. This note concerns a **derived auxiliary six-phase scalar spectral functional** only; no new native BRC propagation has been executed or certified.

Inherited scalar formula and effective positive critical-value bounds are in:

* PREFIX-1037: enterprise-math@928461a6f8c675b9a7bd38586cf47db9d25835e9:research_notes/portable_direct/2026-11-23_r6_prefix1037_certified_critical_density_positivity.md
* Earlier scalar representation: PREFIX-1033 and PREFIX-1036, as cited by PREFIX-1037.

Their shared scalar premise is the absolutely convergent representation, for 0<y<36 and r=sqrt(y),

\[
g(y)=\int_0^\infty K(t;y)\,dt,\quad
K(t;y)={J_0(t)^6\over5}\left[
A(y)tJ_0(rt)-B(y)t^2J_1(rt)
+C(y)\left(D(y)J_1(rt)-{E(y)\over t}J_2(rt)\right)
\right],
\]

\[
H=y^2(36-y)^2,\quad P=y(y-36)(17y-91),\quad
A=2H'-P,\quad B=H/r,\quad C=12(11+y),\quad
D=r(y-6),\quad E=2y.
\]

At t=0, J_2(rt)/t denotes its continuous extension. PREFIX-1037 supplies the previously certified rational bounds

\[
g(4)>6371/60,\qquad g(16)>919/90.
\]

## New theorem: explicit uniform half-Hölder modulus

**Theorem.** Subject to the exact inherited scalar representation above, for every x,y in [3,17] with \(\delta=|x-y|\le1\),

\[
\boxed{|g(x)-g(y)|\le 1\,500\,000\sqrt{\delta}.}
\]

Consequently,

\[
\boxed{ |y-4|\le10^{-9}\ \Longrightarrow\
g(y)>3371/60>56,}
\]

\[
\boxed{ |y-16|\le10^{-11}\ \Longrightarrow\
g(y)>469/90>5.}
\]

These are **numerically explicit, nonempty, certified positive closed neighborhoods**. In particular, neither conclusion relies on an unknown existential radius, a floating-point sign probe or a Picard–Fuchs continuation with unbounded remainder.

### Proof: coefficient bounds

For every y in [3,17], 1<r<5, |r'|<1/2, |y(36-y)|<=324, |36-2y|<=30, |17y-91|<=198 and |y-6|<=11. Elementary differentiation and the triangle inequality give the following deliberately loose *integer* bounds:

| coefficient | magnitude bound | derivative bound |
|---|---:|---:|
| A=2H'-P | 111000 | 20000 |
| B=H/r | 105000 | 76000 |
| C=12(11+y) | 336 | 12 |
| D=r(y-6) | 55 | 11 |
| E=2y | 34 | 2 |

For checking A': H''=2(36-2y)^2-4y(36-y), and P'=(2y-36)(17y-91)+17y(y-36); hence |2H''|<=6192, |P'|<=11448 and |A'|<20000. Also |H'|<=19440, |H|<=104976<105000, giving B' below 76000. These inequalities are valid throughout the full connecting segment [3,17], not just at the two centers.

For integer Bessel orders the angular-integral formula implies |J_nu^(j)(u)|<=1 for j>=0 and real u. Consequently, on 0<=t<=1, |J_2(rt)/t|<=r<=5 and the y derivative of J_2(rt)/t has magnitude <=1/2. Direct Leibniz differentiation of K yields

\[
\sup_{y\in[3,17],\,0\le t\le1}|\partial_y K(t;y)|
\le\frac{20000+55500+76000+52500
+12(55+5\cdot34)+336(11+55/2+10+17)}5
<50000.
\]

For x>=1, use the ν=0,1 Bessel inequalities already derived in PREFIX-1037,

\[
|J_\nu(x)|\le\sqrt{2/\pi}\,x^{-1/2}
\exp(|\nu^2-1/4|/x).
\]

The elementary estimates sqrt(2/pi)<4/5, exp(1/4)<4/3 and exp(3/4)<9/4 imply |J_0(x)|< (11/10)/sqrt(x), |J_1(x)|<2/sqrt(x). The last exponential bound follows directly by bounding the power-series tail from n=3 geometrically (ratio <=3/16).

Use the integer-order recurrences J_0'=-J_1, J_1'=J_0-J_1/x, J_2=2J_1/x-J_0 and J_2'=J_1-2J_2/x. As rt>=1 and r>=1, the following bounds hold for t>=1:

\[
|J_0(t)|^6\le2t^{-3},\quad
|J_0(rt)|\le(11/10)t^{-1/2},\quad
|J_1(rt)|\le2t^{-1/2},\quad |J_2(rt)|\le6t^{-1/2},
\]
\[
|J_0'(rt)|\le2t^{-1/2},\quad
|J_1'(rt)|\le4t^{-1/2},\quad
|J_2'(rt)|\le14t^{-1/2}.
\]

By inserting the integer coefficient bounds into K and its y derivative, and using t>=1 to compare each lower power, we obtain

\[
|K(t;y)|\le {2\over5}
(111000\cdot 11/10+105000\cdot2+
336(55\cdot2+34\cdot6))\,t^{-3/2}
={875208\over5}\,t^{-3/2}
<200000t^{-3/2},
\]

and

\[
|\partial_yK(t;y)|\le{2\over5}
(20000\cdot 11/10 +111000+76000\cdot2+
105000\cdot2+12(55\cdot2+34\cdot6)
+336(11\cdot2+55\cdot2+2\cdot6+34\cdot7))
\,t^{-1/2}
=250848\,t^{-1/2}<300000t^{-1/2}.
\]

The derivative estimate is **used only on a finite integration interval**; no invalid differentiation under the improper integral is needed.

For 0<δ<=1 choose T=1/δ>=1. The fundamental theorem of calculus on [0,T], and the two absolutely convergent tails, imply

\[
|g(x)-g(y)|
\le\delta\left(50000+\int_1^T300000t^{-1/2}dt\right)
+2\int_T^\infty 200000t^{-3/2}dt
\]
\[
\le 50000\delta+600000\delta\sqrt T+
800000/\sqrt T
\le1450000\sqrt\delta<1500000\sqrt\delta.
\]

The case δ=0 is immediate. The uniform tail bound also establishes continuity without assuming differentiability of g at the Morse critical values.

Finally, sqrt(10^{-9})<1/30000 and sqrt(10^{-11})<1/300000, so the two modulus losses are <50 and <5 respectively. Subtracting them from the PREFIX-1037 rational inequalities yields the displayed explicit lower bounds. QED.

## Exact rational verification / reproducibility

The coefficient and kernel bounding arithmetic was checked with Python fractions (not numerical quadrature):

small-kernel derivative majorant = 228708/5 = 45741.6 < 50000;
large-t kernel majorant = 875208/5 = 175041.6 < 200000;
large-t y-derivative majorant = 250848 < 300000.

The identity 6371/60 - 50 = 3371/60 and 919/90 - 5 = 469/90 is exact. Squaring the positive rational comparison endpoints proves 10^-9 < 1/30000^2 and 10^-11 < 1/300000^2.

No float integration, new numerical spectral samples or native BRC experiment is claimed in this unit.

## Scientific scope, remaining work, provenance

1. Mathematical classification: a complete author-written *conditional* theorem over the inherited derived-scalar integral, with explicit rational bounds. The correctness of that inherited reduction and its match to the native signed X6–BRC observer remain separate unresolved audit obligations.
2. Next: reduce the admittedly conservative 1/2-Hölder constant with intervals local to 4 or 16, or use interval Bessel quadrature on the remaining compact spectral intervals; certify positivity or locate a rigorous negative witness. A positive neighborhood alone does not settle the full Hausdorff cone.
3. Preserve frozen P000 V5, joint relation/provenance, Stage46 signed BRC W=J12−6I12, incoming −e1, blocked bidirectional Link {0,e1}, exactly one negative outgoing step. No scalar quotient is declared native-state sufficient.
4. Prior authorship: historical EM-DIRECT-FBEA5D / RA-3FB2D033BE6048D8712FF056 (PREFIX-1037); attribution only, not current authentication or CLAIM. Current logical-session Researcher identity and formal owner snapshot are still to be verified. No Result, independent Review, Working Truth or Foundation promotion occurs with this note.
