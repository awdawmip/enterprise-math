# D25: explicit harmonic forms of the original 216 third-digit jet (author-side)

Date: 2026-10-28 Asia/Hong_Kong.
Classification: AUTHOR-SIDE / EXACT ALL-p=6m+1 ALGEBRAIC COEFFICIENT FORMULAS / INDEPENDENT ORIGINAL-SUM FINITE CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING.
Research lane: \`chatgpt-research-onhour-enterprise-math-20260923\` (NOT maintenance).
Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT.
Publication TP2-B6F4FC938FF94941C1B7.
Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 is UNCHANGED.

## Scientific increment and relationship to prior work

The prior *single-parameter jet* established that the EXACT original finite sum
\[
W_p=\sum_{n=0}^{p-1}(6n+1)\binom{2n}{n}^2\binom{3n}{n}216^{-n}
\]
is congruent to \(J_0+pJ_1+p^2J_2\pmod {p^3}\), for \(p=6m+1>3\), where \(J_i=[s^i]\Phi_m(s)\). This note derives **fully explicit, finite ordinary harmonic sums** for *each* coefficient (including its two zero-crossing bands) without taking a symbolic derivative or dropping any high-band contribution. It is a new explicit *computable port* for attacking the original p^3 cancellation, NOT a proof of its zero. The previous jet and the signed high-band reflection are consumed, not claimed again.

Write \(H_r=\sum_{j=1}^rj^{-1}\), \(H^{(2)}_r=\sum_{j=1}^rj^{-2}\), \(H_0=H_0^{(2)}=0\). All rational denominators below are p-units in the bands where they are used. Set
\[
A_n=(6n+1)(-1)^n2^{-n}
\binom{3m}{n}\binom{2m}{n}\binom{4m}{n},\quad 0\le n\le2m.
\]
For this low band put
\[
\begin{split}
L_n={}&-\tfrac12(H_{3m}-H_{3m-n})
-\tfrac13(H_{2m}-H_{2m-n})
-\tfrac23(H_{4m}-H_{4m-n}),\\
E_n={}&\tfrac14(H^{(2)}_{3m}-H^{(2)}_{3m-n})
+\tfrac19(H^{(2)}_{2m}-H^{(2)}_{2m-n})
+\tfrac49(H^{(2)}_{4m}-H^{(2)}_{4m-n}).
\end{split}
\]
For \(2m+1\le n\le3m\), define the *one-zero middle port*
\[
C_n=\frac{(6n+1)(3m)!(4m)!(2m)!(n-2m-1)!}
{3\cdot2^n(n!)^3(3m-n)!(4m-n)!}
\]
and
\[
M_n=-\tfrac12(H_{3m}-H_{3m-n})
-\tfrac23(H_{4m}-H_{4m-n})
+\tfrac13(H_{n-2m-1}-H_{2m}).
\]
For \(3m+1\le n\le4m\), define the *two-zero high port*
\[
D_n=\frac{(6n+1)(-1)^{m+n}(3m)!(2m)!(4m)!
(n-3m-1)!(n-2m-1)!}
{6\cdot2^n(n!)^3(4m-n)!}.
\]

## Theorem (exact coefficient identities)

For every prime \(p=6m+1>3\), the SAME \(\Phi_m(s)\) defined in the earlier original-class jet obeys the **exact rational identities**
\[
\boxed{J_0=\sum_{n=0}^{2m}A_n,}
\]
\[
\boxed{J_1=\sum_{n=0}^{2m}A_nL_n+
             \sum_{n=2m+1}^{3m}C_n,}
\]
\[
\boxed{J_2=
 \sum_{n=0}^{2m}\tfrac12A_n(L_n^2-E_n)
 +\sum_{n=2m+1}^{3m}C_nM_n
 +\sum_{n=3m+1}^{4m}D_n.}
\]
Consequently,
\[
\boxed{W_p\equiv J_0+pJ_1+p^2J_2\pmod{p^3},}
\]
where the \(J_i\) on the right are now given by the ordinary harmonic formulas, not by unevaluated formal derivatives. The original third-digit conjecture on \(p\equiv13,19\pmod{24}\) is still precisely
\[
\frac{J_0+pJ_1-p}{p^2}+J_2\stackrel?{\equiv}0\pmod p,
\]
using the already accepted first-digit divisibility. The numerator quotient here must be taken from p-local representatives; it is NOT an independent arbitrary division in \(\mathbf F_p\).

### Proof

Retain the previous exact original-class deformation
\[
\Phi_m(s)=\sum_{n=0}^{p-1}\frac{6n+1}{2^n(n!)^3}
 (-3m+s/2)_n(-2m+s/3)_n(-4m+2s/3)_n,
\quad\Phi_m(p)=W_p.
\]
For \(n\le2m\), none of the three factors has an \(s=0\) zero. Its constant term is \(A_n\); its logarithmic first coefficient is \(L_n\). Since
\(\log\prod_j(1+s\lambda_j/d_j)=s\sum_j\lambda_j/d_j-(s^2/2)\sum_j\lambda_j^2/d_j^2+O(s^3)\),
the quadratic coefficient is \(A_n(L_n^2-E_n)/2\) exactly.

For \(2m<n\le3m\), the factor \((-2m+s/3)_n\) has exactly one simple zero at its \(j=2m\) member. Removing that zero, its linear coefficient is \((2m)!(n-2m-1)!/3\). Multiplying the other factors gives \(C_n\). The logarithmic first coefficient of all remaining nonzero factors is \(M_n\), including the positive tail \(H_{n-2m-1}\) and the negative portion \(-H_{2m}\) of the factor that crossed zero. Thus its quadratic coefficient is \(C_nM_n\).

For \(3m<n\le4m\), the \(-3m\) and \(-2m\) Pochhammer factors each have exactly one simple zero, while \(-4m\) does not. Multiplication of their two linear coefficients gives \(D_n\), with sign \((-1)^{m+n}\), and no \(s^0,s^1\) coefficient. Finally, \(4m<n\le6m\) has all three zeros, hence contributes only \(O(s^3)\). Coefficient extraction proves the three boxed rational identities; the substitution \(s=p\) and \(n! \in\mathbb Z_{(p)}^\times\) establish the modulo \(p^3\) reconstruction. No target supercongruence was assumed. QED.

## Exact executed checks (scope explicit)

A Python standard-library *modular integer* implementation (companion file d25_original216_explicit_harmonic_jet_20261028.py) computes \(J_0\bmod p^3\), \(J_1\bmod p^2\), \(J_2\bmod p\) from the above harmonic formulas and independently computes the original full \(\binom{2n}{n}^2\binom{3n}{n}/216^n\) sum, retaining every \(n<p\). It was actually executed at p=7,13,19,31,37,43,61,67,73,211,373; all eleven reconstructions matched.

At p=373 (\(m=62\), \(p^2=139129\), \(p^3=51895117\)) the exact certificate is
\[
(J_0,J_1,J_2)=(15521276\bmod p^3,\ 47909\bmod p^2,\ 133\bmod p).
\]
The first-order source ports are
\[
\sum_{\rm low}A_nL_n=3122,\quad \sum_{\rm middle}C_n=44787
\pmod {p^2};
\]
the separately labelled second-order ports are
\[
\left(\sum_{\rm low}\tfrac12 A_n(L_n^2-E_n),\
\sum_{\rm middle}C_nM_n,\
\sum_{\rm high}D_n\right)=(82,158,266)\pmod p.
\]
Thus \(82+158+266\equiv133\pmod{373}\), and
\((J_0+373J_1-373)/139129\equiv240\pmod{373}\), yielding \(240+133=373\equiv0\).
The \(266\) high-band digit independently matches the earlier source-retaining \(\Theta_{373}\) port. This is a numerical fixture, not an infinite-prime proof. There is **no** claim of native \([X]U\), Frobenius, module rank, or mathematical admission.

## Observer typing, external limitations and exact continuation

Carrier: \((p,m,n,\text{Pochhammer factor source},\text{zero-crossing count},6n+1,\text{cutoff},\text{sign},\text{valuation},\text{CM/Delta/R provenance})\). Permitted operations: p-local coefficient extraction, signed factorial reduction, ordinary harmonic sums, and congruence of the exact **original** scalar \(W_p\bmod p^3\). The three second-order ports cannot be merged before the cancellation identity is proven; they are NOT a complete observer for the original native H0/B0 or X6 dynamics. This remains external scalar arithmetic, with P000 six-axis Cell semantics and separately typed time unchanged.

NEXT MATHEMATICS: use the explicit low/middle/high harmonic sums as concrete WZ/creative-telescoping operands, seeking a valid **uniform** cancellation proof of the displayed quotient for both \(p\equiv13,19\pmod{24}\). Do not substitute another finite sweep for that proof. Avoid duplicated GH17–23 parallel-owner work and previously completed Cauchy p² theory.

HIGHEST NATIVE EVIDENCE: awdawmip/enterprise-math#1559 is OPEN/PENDING_OWNER/NOT_EXECUTED as read at this turn. The responsible path is a Source-authorized H0/B0 executor; evidence needed is the actual fixed p=373 \([X]U\bmod139129\), module rank, semilinear Frobenius direction/eta, signed odd Green/Hesse, \(\kappa\), \(\Delta_p-R_p\), and raw reproducibility. This note is not that experiment. Site v0.6.11 currently exposes only read scope, research_authority_granted=false/write_relay_enabled=false. Historical bridge recovery #6575 and dispatch #6576 are different transport scope and their target request IDs return CONTROL_REQUEST_NOT_FOUND in this Site; no blind retry, no current own winning claim/run or formal checkpoint verified. The three old staging sources remain independent. \`REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NOT_ADMITTED\`. No scheduler, Action, cron, task ownership or frozen Source mutation.
