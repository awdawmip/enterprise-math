# R239 — Effective parameter-uniform one-mode horizon for the six-source ideal observer

Date: 2026-11-17 (Asia/Shanghai). Status: **AUTHOR_PROVED / EXACT_INTEGER_CHECKED / NOT_REVIEWED**. Native typed BRC: **NOT_EXECUTED**.

## Frozen provenance, model and question

This is a quantitative continuation of R237/R238 at immutable commit db8856bdf3f3d8e1567232572b474e7d6493079e, R234 at 37786e0e0acb51ce36fa9ae68ec84ce28ad46dc6, and exact ideal weights R220 at a51ddb6ed7e91842c567855bf3fbee118a6816c8. Original science input remains frozen at 43ec6098b1330ae86d0a7863be336c5d97f6ef34.

We work only in the auxiliary scalar seven-source stationary sticky-reset Markov model of R234, for all real s in I=(39/100,41/100). P000 and native X6/BRC source, sign, port, provenance, branch multiplicity and cross moments are unchanged.

Recall R237/R238:
\[
\Phi_n(s):=\mathbb E[F_n]-W_6
=A(s)r(s)^{n-1}+R_n(s),\quad
0\le R_n(s)\le (T(s)-A(s))\theta^{n-1},
\]
for integer n>=L=2, with \(\theta=9847338/10000000<1\),
\(r(s)>594323/600000\), \(A(s)>0\),
and
\[
A(s)=W_5\,\frac{S(s)^2}{Z(s)Q(s)},\quad
S(s)=\sum_{j\ne3}\frac{b_j}{(1-\alpha_j)(r-\alpha_j)},\quad
Z(s)=\sum_{j=0}^6\frac{b_j}{(1-\alpha_j)^2},\quad
Q(s)=\sum_{j\ne3}\frac{b_j}{(r-\alpha_j)^2}.
\]
Here alpha and b are the exact R234 rational family, and T is the total nonconstant spectral coefficient. R220's m=12,k=6,L=2 weights are
\[
(W_0,\ldots,W_6)=(144,576,1440,4320,17280,86400,518400).
\]

## Theorem: uniform positive Perron fraction and rational horizons

For **every real s∈I** the leading Perron amplitude satisfies the explicit strict inequalities
\[
\boxed{\frac{A(s)}{W_5}>
\frac{20510899}{118592100}>0.1729}
\]
and
\[
\boxed{\frac{A(s)}{T(s)}>
\eta:=\frac{2159042}{128474775}>0.0168.}
\]
Therefore, for every integer n>=2,
\[
\boxed{
0\le\frac{\Phi_n(s)-A(s)r(s)^{n-1}}
{A(s)r(s)^{n-1}}
<
\frac{126315733}{2159042}
\left(\frac{14771007}{14858075}\right)^{n-1}.}
\]
In particular, simultaneously for **all real** \(s\in I\),
\[
\boxed{n\ge1477\ \Longrightarrow\
\frac{R_n(s)}{A(s)r(s)^{n-1}}<\frac1{100},}
\]
\[
\boxed{n\ge1869\ \Longrightarrow\
\frac{R_n(s)}{A(s)r(s)^{n-1}}<\frac1{1000}.}
\]
These integer horizons are the **first values certified by this explicit bound** for the two specified tolerances; they do not assert that the true minimal horizons cannot be earlier.

## Proof

Set \(c=5/18\), \(\alpha_3=9/20\). The fixed omitted-source datum is
\[
b_3=c(1/2-\alpha_3)=1/72,\qquad
z_3=\frac{b_3}{(1-\alpha_3)^2}=\frac{50}{1089}.
\]
The full stationary normalization satisfies
\[
Z=\sum_j \frac{\pi_j}{1-\alpha_j}> \sum_j\pi_j=1,
\]
since every \(0<\alpha_j<1\). R235/R236 give \(r(s)<1\). Thus for each retained \(j\ne3\),
\[
r-\alpha_j<1-\alpha_j,\quad
\frac{b_j}{(1-\alpha_j)(r-\alpha_j)}>
\frac{b_j}{(1-\alpha_j)^2}.
\]
Summing shows \(S>Z-z_3\).

The leading killed-block secular equation is
\[
\sum_{j\ne3}\frac{b_j}{r-\alpha_j}=1.
\]
All retained holding parameters are below 4/5 by R234, while r>99/100. Hence
\[
Q=\sum_{j\ne3}\frac{b_j}{(r-\alpha_j)^2}
<\frac{100}{19}
\sum_{j\ne3}\frac{b_j}{r-\alpha_j}
=\frac{100}{19}.
\]
For \(Z>1>z_3\), the function \(g(z)=(z-z_3)^2/z=z-2z_3+z_3^2/z\) increases since \(g'(z)=1-z_3^2/z^2>0\). Consequently
\[
\frac{S^2}{ZQ}>
\frac{19}{100}\frac{(Z-z_3)^2}{Z}>
\frac{19}{100}(1-z_3)^2
=\frac{20510899}{118592100}.
\]
This proves the first bound.

R220's exact weights give
\[
\Gamma_0=\sum_{u=0}^5\binom6uW_u=889200,\qquad
\Gamma_1=\sum_{u=1}^5\binom5{u-1}W_u=655776.
\]
The R237 spectral coefficient sum is the stationary convex combination
\(T=\rho_0\Gamma_0+(1-\rho_0)\Gamma_1\le\Gamma_0\). Therefore
\[
\frac AT>\frac{W_5}{\Gamma_0}\,
\frac{20510899}{118592100}
=\frac{24}{247}\frac{20510899}{118592100}
=\eta.
\]
Thus \( (T-A)/A <(1-\eta)/\eta=126315733/2159042.\)

Finally, R238's uniform cutoff \(\theta\) and R236's lower bound r give
\[
\frac{R_n}{A r^{n-1}}\le\frac{T-A}{A}(\theta/r)^{n-1}
<
\frac{126315733}{2159042}\left(\frac{14771007}{14858075}\right)^{n-1}.
\]
The integer comparisons
\[
\frac{126315733}{2159042}
\left(\frac{14771007}{14858075}\right)^{1476}
<\frac1{100}
<
\frac{126315733}{2159042}
\left(\frac{14771007}{14858075}\right)^{1475},
\]
and similarly exponents 1868/1867 for 1/1000, hold by exact integer cross-multiplication. As \(0<q<1\), these imply the stated thresholds for all larger n. QED.

## Verification, status and next frontier

The companion standard-library Fraction checker verifies the Stirling-fiber weights and binomial sums from R220, every derived rational constant, the signed exact integer inequalities bracketing both thresholds, and independent monotonicity bounds in the proof. The script returns PASS with a machine-readable JSON file. Symbolic argument covers the stated continuum of real s; the integer verification checks its rational certificates. Independent mathematics review NOT_REVIEWED; BRC native EffectHistogram execution NOT_EXECUTED.

Next: obtain less conservative amplitude-fraction bounds by rational interval subdivision of s and certified enclosing of r(s), and optimize exact bit complexity of the one-mode approximation against 230-order recurrence and 256-state propagation. Preserve typed native BRC joint provenance separately.
