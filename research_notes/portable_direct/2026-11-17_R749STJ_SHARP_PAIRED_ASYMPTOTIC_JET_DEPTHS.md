# R749STJ — Exact hierarchy of maximal legal asymptotic jet depth across paired phase classes

Date: 2026-11-17. Evidence: AUTHOR_EXACT_NOT_REVIEWED. Frozen five-source auxiliary scalar model: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389. Continuation: R749SSY, R749STH, R749STI. Scientific scope: positive weighted five-source counts and fixed real errors in [-2,2]^2. No native X6 Port/Cell mapping is asserted.

## Classification

For any integer k≥0, compare the same-index six-step tails \(Y_{q+6j}(e,d)\) and \(Y_{p+6j}(E,D)\), with all four nuisance parameters fixed throughout the tail. Let \(x=(6j)^{-1}\) and call the largest integer m for which their series agree through \(x^m\) the legal asymptotic jet depth (the zeroth limiting term is equal in these pairs).

**Class {1,5}.** For \(q=73+6k,\ p=q+4\), the maximal legal depth is exactly **three**. A rational legal witness is

\[
e=-\frac{6455}{8748},\quad d=-1,\quad
E=\frac{12319}{8748},\quad D=-\frac{91}{81}.
\]

Its first three inverse-time difference coefficients vanish, and its first surviving coefficient is \(7002200/27>0\) at order four. No parameters in [-2,2]^4 can also cancel that coefficient.

**Class {2,4}.** For \(q=74+6k,\ p=q+2\), the maximal legal depth is exactly **four**. The unique legal quadruple is

\[
e=\frac{69402481}{101966688},\quad d=-\frac{656227}{472068},\quad
E=\frac{194725627}{101966688},\quad D=-\frac{755303}{472068}.
\]

Here the first four coefficients vanish, while the fifth is \(55842420440/39339>0\), as established with a full certificate in R749STI.

Hence the two paired asymptotic phase classes have **different maximal nuisance-mask depths: 3 versus 4**. For both classes, the exact residual eventually distinguishes the branches, despite increasingly small finite-resolution differences.

## Proof for the {1,5} family

The model and exact quasi-polynomial counts are those of R749STI. For base cutoffs (73,77), let \(a_i\) be the coefficient of \(x^i\) in \(Y_{73+6j}(e,d)-Y_{77+6j}(E,D)\). Their common limit is \(-295/36\). Exact rational expansion gives

\[
\begin{aligned}
a_1&=-\tfrac{80}{9}(-81D+81d-10),\\
a_2&=\tfrac{80}{3}(-2808D-162E+2700d+162e-107),\\
a_3&=-\tfrac{40}{81}(-15398181D-1609632E+14208453d+1539648e+312038),\\
a_4&=\tfrac{40}{3}(-56875743D-8197308E+50298219d+7497468e+3495995).
\end{aligned}
\]

The affine system \(a_1=a_2=a_3=a_4=0\) has coefficient determinant \(77035520655360000\ne0\), so its only real solution is

\[
(e,d,E,D)=\left(
-\frac{439960}{3265191},
-\frac{658787}{483732},
\frac{7355183}{3265191},
-\frac{718507}{483732}
\right).
\]

The third coordinate is \(E=7355183/3265191>2\), outside the frozen permitted error interval. Hence no admissible four-jet coincidence exists. Substituting the displayed legal three-jet witness gives \(a_1=a_2=a_3=0\), \(a_4=7002200/27\). This proves sharpness.

For arbitrary \(k\ge0\), replacing (73,77) with (73+6k,77+6k) replaces \(j\) by \(j+k\). The transformation of inverse-time coefficients is triangular with diagonal entries 1; vanishing of the first m coefficients is invariant under such a finite index shift. The sharp depths therefore hold for the entire two infinite cutoff families.

## Verification, interpretation, continuation

The companion Python/SymPy certificate verifies the exact determinant, the unique inadmissible four-jet solution, a strictly admissible three-jet construction, and the positive fourth coefficient. The R749STI executable supplies the independent exact generating-function construction and the complete class {2,4} fifth-order certificate. Author execution of both: PASS. The branch/family extension is an algebraic index-shift argument, not numerical extrapolation.

The two classes define different depths of observer-induced source hiding under a truncated asymptotic BRC readout. A source-preserving carrier must distinguish the two residue labels or retain an equivalent future-sensitive repair coordinate. The model's existing global finite-exact-read bound \(5\le m_*\le11\) is unchanged.

Next: classify all other pairs of cutoff residue orbits, bound the first nonzero residual uniformly over the admissible nuisance box, and test a typed BRC Port with explicit source-label and future-operation semantics.
