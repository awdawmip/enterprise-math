# D25/LIFT — exact original 216-series / genuine WZ-cutoff bridge and a universal second-digit edge certificate

2026-10-24 | TASK_RESEARCH, original onhour author lane | **UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT**. This is an author-side portable mathematical proof and executable exact check, not a Source CLAIM/run/checkpoint, formal Result, native CM experiment/benchmark, or independent review.

**Immutable scope.** Mother task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3. The accepted first-digit UR/JT0 and the original LIFT observable \(\Delta_p=(G_ph-1)/p\equiv R_p\pmod p\) remain frozen. This source-faithful WZ result does not replace or establish a same-class CM/divided-power correspondence. Logical research source label chatgpt-research-onhour-enterprise-math-20260923 is distinct from CONTROL_PLANE_MAINTENANCE chatgpt-hourly-enterprise-math-20260921 and another hourly Researcher. No service identity is inferred from a label.

**Consumed, not re-credited:** prior exact original two-variable WZ quartic and five moving-tail terms from c7fb90fd7ec451a954b553b963dd85d4ec99fc96; finite 575-prime p³ original rank-m check from c6ba00a05c04ef0bbf1fae4a2ec4a4df4aa06ca0; published author LOW-seed and seam certificates. Other hourly HIGH-Cauchy and normalization proofs are separate operations and authors.

## Theorem 1: exact rectangle from the genuine weighted 216 terminal to the original rank-m cutoff

For nonnegative integers r,n, define the original rational term

\[
A_r=\frac{(6r)!}{3^{6r}((2r)!)^3},\quad
R_{r,n}=\frac{(4r+2n)!((2r)!)^2(3n)!}
{216^n((2r+n)!)^2(4r+n)!(n!)^2},\quad
T_{r,n}=A_r(6n+12r+1)R_{r,n}.
\]

Recall the previously proved exact WZ rational potential

\[
\begin{aligned}
P(r,n)={}&27n^4+(324r+180)n^3+(1836r^2+1746r+429)n^2\\
&+(4320r^3+5940r^2+2706r+412)n\\
&+3456r^4+6336r^3+4128r^2+1184r+128,\\
g(r,n)={}&\frac{4nP(r,n)}
{9(n+2r+1)(n+4r+1)(n+4r+2)(n+4r+3)(6n+12r+1)}.
\end{aligned}
\]

The old exact identity is \(T_{r+1,n}-T_{r,n}=T_{r,n+1}g(r,n+1)-T_{r,n}g(r,n)\), with \(g(r,0)=0\).

Fix a single prime \(p=6m+1\ge7\), and **do not change p while moving the auxiliary rank r**. Set

\[
W_p=\sum_{n=0}^{p-1}T_{0,n},\quad
S_m=\sum_{n=0}^{4m}T_{m,n},\quad
C_p=\sum_{n=4m+1}^{p-1}T_{m,n},\quad
E_{p,r}=T_{r,p}g(r,p).
\]

Here \(W_p\) is exactly the frozen Sun/UR/LIFT weighted 216-series, while \(S_m\) is the different genuine source original WZ/Gosper rank-m finite endpoint. The newly selected **fixed original column** gives the following exact rational identity:

\[
\boxed{W_p-S_m=C_p-\sum_{r=0}^{m-1}E_{p,r}\quad\text{in }\mathbb Q.}\tag{RECT}
\]

**Proof.** Sum the old WZ identity over \(0\le n<p\) at a *fixed* rank r: its right side telescopes to \(E_{p,r}\) because \(g(r,0)=0\). Sum that equality for \(r=0,\ldots,m-1\), obtaining \(\sum_{n<p}T_{m,n}-W_p=\sum_r E_{p,r}\). Split the honest rank-m range \(n<p\) at its real endpoint \(4m\); \(\sum_{n<p}T_{m,n}=S_m+C_p\). Rearrange. All operations are exact over Q, and neither source sum is relabeled as the other. QED.

## Theorem 2: an all-prime modulo-p² evaluation of every genuine WZ column-edge port

Cancellation of the authentic weight \(6p+12r+1\) in the old potential yields the **exact** formula

\[
\boxed{\frac{E_{p,r}}p=
\frac{4A_rR_{r,p}P(r,p)}
{9(p+2r+1)(p+4r+1)(p+4r+2)(p+4r+3)}.}\tag{EXACT-EDGE}
\]

For \(0\le r<m\), all shown factors except P and p are p-units. Thus \(v_p(E_{p,r})=1+v_p(P(r,p))\), *without assuming that the valuation is always exactly one*.

Define \(H_k=\sum_{j=1}^k1/j\), \(H_0=0\), and the integer \(q=q_p(216)=(216^{p-1}-1)/p\). This turn proves the following new universal second-digit unit relation:

\[
\boxed{
R_{r,p}\equiv\frac1{18}
\left[1+p(H_{4r}-2H_{2r}-q)\right]\pmod{p^2}.}\tag{UNIT}
\]

**Proof.** The exact source factorial formula gives

\[
R_{0,p}=\binom{2p}{p}^{2}\binom{3p}{p}216^{-p},\qquad
\frac{R_{r,p}}{R_{0,p}}=
\frac{((2r)!)^2\prod_{j=1}^{4r}(2p+j)}
{\prod_{j=1}^{2r}(p+j)^2\prod_{j=1}^{4r}(p+j)}.
\]

For p>3, the finite product \(\binom{ap}{p}/a=\prod_{j=1}^{p-1}(1+(a-1)p/j)\) and \(H_{p-1}\equiv0\pmod p\) give \(\binom{2p}{p}\equiv2\), \(\binom{3p}{p}\equiv3\pmod{p^2}\). Fermat gives \(216^{-p}\equiv216^{-1}(1-pq)\pmod{p^2}\). The remaining quotient equals \(1+p(H_{4r}-2H_{2r})\pmod{p^2}\). Since \(4r<p\), every inverse is legal. Multiplying proves (UNIT).

Write the exact integer polynomials and rational correction

\[
\begin{aligned}
P_0(r)&=3456r^4+6336r^3+4128r^2+1184r+128,\\
P_1(r)&=4320r^3+5940r^2+2706r+412,\\
L_r&=(2r+1)^{-1}+(4r+1)^{-1}+(4r+2)^{-1}+(4r+3)^{-1},\\
D_r&=H_{4r}-2H_{2r}-q-L_r.
\end{aligned}
\]

**New exact-source second-digit edge theorem, for all p=6m+1>=7 and 0<=r<m:**

\[
\boxed{
\frac{E_{p,r}}p\equiv
\frac{A_r\{P_0(r)+p[P_1(r)+P_0(r)D_r]\}}
{81(2r+1)^2(4r+1)(4r+3)}\pmod{p^2}.}\tag{EDGE-P2}
\]

**Proof.** Insert (UNIT) into (EXACT-EDGE); use \(P(r,p)\equiv P_0+pP_1\pmod{p^2}\), the four-denominator expansion \(D(r,p)^{-1}\equiv D(r,0)^{-1}(1-pL_r)\), and \(4r+2=2(2r+1)\). The rational constant is \(4/(9\cdot18\cdot2)=1/81\). Every denominator is a p-unit, so this is a proof for every prime in scope, not interpolation from samples. QED.

**Resonance / precision firewall.** Genuine exact integer witnesses \((p,r,P(r,p)/p\bmod p)=(31,2,7),(109,9,14),(409,4,397),(1993,5,449),(2027,11,1274)\) have \(P(r,p)\equiv0\pmod p\) but \(P(r,p)\not\equiv0\pmod{p^2}\); hence their true edge has valuation exactly two. Dropping the \(pP_1\) term loses an observable second digit. These are not original LIFT counterexamples.

## Theorem 3: fully source-preserving terminal equation at the required p³ horizon

The genuine last \(2m\) rank-m terms stay explicitly labeled: for \(4m+1\le n\le p-1\), the factorial formula and Legendre's valuation count yield

\[
v_p(R_{m,n})=
\lfloor(4m+2n)/p\rfloor+\lfloor3n/p\rfloor
-2\lfloor(2m+n)/p\rfloor-\lfloor(4m+n)/p\rfloor=1.
\]

The linear weight \(6n+12m+1\equiv6n-1\pmod p\) has its sole zero in this interval at \(n=5m+1\). Hence for p>=13, \(v_p(T_{m,n})=1+\mathbf1_{\{n=5m+1\}}\), and \(C_p/p\in\mathbb Z_{(p)}\). The p=7 exceptional weight is 7p at that n, giving an extra factor but preserving p-integrality.

Combining the exact (RECT) with the proved (EDGE-P2) obtains a p-integral, true-source **modulo-p² divided endpoint bridge**:

\[
\boxed{
\frac{W_p-S_m}{p}
\equiv\sum_{n=4m+1}^{p-1}\frac{T_{m,n}}p
-\sum_{r=0}^{m-1}\widehat E_{p,r}
\pmod{p^2},}\tag{RECT-P2}
\]
where \(\widehat E_{p,r}\) is the explicit right side of (EDGE-P2). Every WZ column-edge unit has now been evaluated to the required second digit. The exact surviving uncompressed input is the genuine last 2m terminal terms, not a HIGH-only or Cauchy substitute.

**Conditional comparison, explicitly not a proof of either conjecture:** if the separate rank-m target \(S_m\equiv p(4/3)^{p-1}\pmod{p^3}\) holds, then \(W_p\equiv p\pmod{p^3}\) is equivalent to

\[
\sum_{n=4m+1}^{p-1}\frac{T_{m,n}}p
-\sum_{r<m}\widehat E_{p,r}
\equiv -p\,q_p(4/3)\pmod{p^2},
\]
with \(q_p(4/3)=((4/3)^{p-1}-1)/p\in\mathbb Z_{(p)}\). Do NOT treat the assumed rank-m congruence, a finite regression, or this source-bridge as the frozen same-class CM/divided-power proof. The original source \(\omega+6\nabla_\lambda\omega\), semilinearity, same-class \(\kappa\) normalization, and unchanged native benchmark are still independent unresolved obligations.

## Executed author evidence, BRC scope, next action

Companion stdlib Fraction checker:
research_notes/portable_direct/20261024_onhour_d25_original_fixed_cutoff_wz_second_digit_edge_check.py

Using the **original factorial summand independently** of the new edge formula, the executed checker compared \(R_{r,p}\) and \(T_{r,p}g(r,p)/p\) with (UNIT)/(EDGE-P2) at *every one of 177* \((p,r)\) pairs for primes \(\{7,13,19,31,37,43,61,67,73,79,97,103,109,127,211\}\): 177/177 passes for each of the two independent checks. For eight primes \(\{13,19,37,43,61,67,73,79\}\), it independently assembled the full original \(W_p,S_m,C_p,\sum E_{p,r}\) using Fraction and checked the exact rational (RECT) and modular (RECT-P2): 8/8 PASS. Five resonance witnesses were verified with exact integers; the two smaller p witnesses were also checked against source Fraction edge values. These finite tests audit implementation; general theorem strength rests on the complete rational/product proofs above.

**BRC: COMPOSE_APPLIED, exact observer-preserving.** Carrier records original weighted n terms and genuine rank/column boundary, source n/r labels, p-valuations and signed p-free units; operation is fixed-p rectangular finite telescope followed by precisely one safe division by p and a mod-p² observer. That quotient is justified only for the declared second-digit observable; it does not identify fixed-p moving-rank summation with moving-p arithmetic, CM class, native X6, or positive unsigned mass.

**Next smallest research obligation:** compute/identify an exact same-class primitive or terminating CM/DP map for the remaining genuine terminal tail under (RECT-P2), explicitly including its unique suppressed tail n=5m+1, and link that observer to frozen \((G_ph-1)/p-R_p\); prove the joint residual zero or obtain a genuine original-source counterexample. Do not rerun the previous 575-prime census or repeat finished LOW/HIGH auxiliary theorems.

**Control truth and recovery:** Current Sites gateway 0.6.11 reports research_authority_granted=false and executor_binding_configured=false. Attempted *read-only* exact continuation request onhour-d25-cont-read-20261024-0800-r11 returned CONTROL_QUOTA; current client checkpoint_get returned ACCESS_DENIED; recovery_status is not callable on this exposed tool surface. No session, winning claim, run, Source checkpoint, result, native experiment or independent review is inferred; unknown historical requests are not replayed. Pre-existing original recovery support enterprise-math#1539 remains the owner path for restoring legitimate Source execution; this author-side GitHub note is NOT formal admission. Keep its own source label separate from maintenance and other Researcher lanes, protect historical staging, and continue from this immutable frontier when legal Source role-bound operations become possible. Frozen scientific pin, active P000/worldview, schedule, phase, enablement and notification settings unchanged.
