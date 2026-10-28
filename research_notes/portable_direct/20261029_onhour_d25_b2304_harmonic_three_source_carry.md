# D25 / SECOND-DIGIT-LIFT — exact binomial/harmonic transport of the B2304 high-degree carry

**Research date:** 2026-10-29 Asia/Hong_Kong. **Evidence grade:** AUTHOR-SIDE / EXACT FINITE-RING DERIVATION / EXECUTED 18-PRIME INTEGER GUARD / UNREVIEWED / NOT_ADMITTED / NATIVE_H0_B0_NOT_EXECUTED / SOURCE_CHECKPOINT_PENDING.

Mother objective: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Canonical Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. **Frozen scientific Source pin:** c47e13e4aba0e006366f989d6334d443f6333ae3 (unchanged). Research logical conversation: chatgpt-research-onhour-enterprise-math-20260923, distinct from control-plane maintenance chatgpt-hourly-enterprise-math-20260921. Earlier UR/CM0 and frozen Result authorship/claims remain undisturbed. This note is not a formal Source CLAIM, Source publication, Result, independent review or native H0/B0 run.

## Selected mathematical bottleneck

The previous author-side note at Enterprise Math commit 3fe386d2578dbf2825a76a7f9a7ef360e85ada80 proved the exact coefficientwise B2304 mod-p³ Clausen cutoff repair and a three-level carry filtration. It computed the fixed p=373 total high-degree carry but did not supply a closed **binomial/harmonic transport of each of its three original source classes**. This unit constructs such a transport without changing the original kernel, cutoff degree, weighted observer or frozen scientific Source.

For every prime \(p\ge13\) with \(p\equiv5\pmod8\), put
\[
a=(5p-1)/8,\quad b=(7p-3)/8,\quad t=b-a=(p-1)/4,\qquad
\beta_n=\frac{(1/8)_n(3/8)_n}{(n!)^2}.
\]
Work throughout in \(\mathbb Z_{(p)}\), reduce only after exact \(p\)-local division, and set
\(w=1/9\), \(\theta=z\,d/dz\), \(D_B=1+8\theta\).
The *original* high-degree carry of the finite Clausen square is
\[
H_B=[D_B\Pi_{\ge p}K_b(z)^2]_{z=w},\qquad
K_b(z)=\sum_{n=0}^{b}\beta_nz^n,
\]
where \(\Pi_{\ge p}\) retains original polynomial degrees at least \(p\), **before** differentiation or finite-field evaluation. The present nonzero-carry branch contains the frozen target class \(p\equiv13\pmod{24}\). For the other target class \(p\equiv19\pmod{24}\), previously established \(2b<p\) directly gives \(H_B=0\); do not apply the present \(p\equiv5\pmod8\) formulas there.

## Theorem: p³-precise three-source harmonic transport

For \(0\le i\le a\), define
\[
L_i=\binom ai\binom bi,\quad
X_i=\frac58\sum_{k=0}^{i-1}\frac1{a-k}+
\frac78\sum_{k=0}^{i-1}\frac1{b-k},
\]
\[
Y_i=\frac{25}{64}\sum_{k=0}^{i-1}\frac1{(a-k)^2}+
\frac{49}{64}\sum_{k=0}^{i-1}\frac1{(b-k)^2},\quad
U_i=L_i\left(1-pX_i+\frac{p^2}{2}(X_i^2-Y_i)\right)\pmod{p^3}.
\tag{1}
\]
For \(0\le r<t\), define
\[
P_r=\prod_{k=0}^{r-1}\frac{(8k+8)(8k+10)}{(8k+15)^2},
\]
\[
Z_r=-X_a+\frac{15}{14}+
5\sum_{k=0}^{r-1}\left(\frac1{8k+8}+\frac1{8k+10}-\frac2{8k+15}\right),
\qquad
E_r=\binom ba\frac{10}{49}P_r(1+pZ_r)\pmod{p^2}.
\tag{2}
\]
Then the following congruences are exact at their asserted precisions:
\[
\boxed{
\beta_i\equiv U_i\pmod{p^3}\quad(0\le i\le a),\qquad
\frac{\beta_{a+1+r}}p\equiv E_r\pmod{p^2}\quad(0\le r<t).
}
\tag{3}
\]

Put \(U(z)=\sum_{i=0}^{a}U_iz^i\) and \(V(z)=\sum_{r=0}^{t-1}pE_rz^{a+1+r}\). The entire original weighted carry therefore satisfies
\[
\boxed{
H_B\equiv[D_B\Pi_{\ge p}(U^2+2UV+V^2)]_{z=1/9}\pmod{p^3}.
}
\tag{4}
\]
The three named terms carry distinct original source tags (low-low, low-middle, middle-middle) and **none may be removed merely by order-of-magnitude reasoning about a different term**. The middle-middle term is divisible by \(p^2\), not generally by \(p^3\).

**Exact derivation.** The finite Pochhammer shifts
\[
(1/8)_i=(-a+5p/8)_i,\qquad (3/8)_i=(-b+7p/8)_i
\]
have the leading signed-factorial product \(\binom ai\binom bi\); the two signs cancel. The remaining factors are
\[
\prod_{k=0}^{i-1}\left(1-\frac{5p}{8(a-k)}\right)
\left(1-\frac{7p}{8(b-k)}\right).
\]
Their first two logarithmic coefficients are \(-X_i\) and \(-Y_i\), giving (1) and the low congruence in (3). The exact junction recurrence is
\[
\frac{\beta_{a+1}}p=\beta_a\frac{5(5p+2)}{(5p+7)^2}
\equiv\binom ba\frac{10}{49}\left[1+p\left(-X_a+\frac{15}{14}\right)\right]
\pmod{p^2}.
\]
For successive middle indices,
\[
\frac{\beta_{a+2+k}}{\beta_{a+1+k}}
=\frac{(5p+8+8k)(5p+10+8k)}{(5p+15+8k)^2}.
\]
Factoring the zeroth-order ratio yields \(P_r\); the first-order \(p\)-logarithmic derivative adds \(5[(8k+8)^{-1}+(8k+10)^{-1}-2(8k+15)^{-1}]\). This gives (2) and the middle congruence in (3). All denominators really used are \(p\)-units: \(a-k,b-k\in\{1,\dots,b\}\), and in the middle ratio \(k\le t-2\); none of \(8k+8,8k+10,8k+15\) is divisible by this \(p\). Also \(p\ge13\) makes \(2,8,9,14,49\) units. The middle has exactly one explicit \(p\) factor through index \(b\). Consequently \(K_b=U+V\pmod{p^3}\) coefficientwise. Squaring and preserving original degree before applying \(D_B\) proves (4) in the p-local polynomial ring, with no analytic continuation or unproved CM premise.

As a possible smaller subsequent finite-hypergeometric input, the zeroth-order transport is exactly \(P_r=(1)_r(5/4)_r/(15/8)_r^2\), **only on the displayed finite unit-denominator range**.

## Reproducible exact checks and sharp p373 provenance witness

Executed actual standard-library integer script:
[verified checker](d25_b2304_harmonic_three_source_carry_20261029.py).
It compares every low/middle coefficient of (3) to a separately computed original beta hypergeometric recurrence, then compares the full tagged convolution (4) to a separate unsplit original coefficient pair sum. It also checks the old three-level endpoint valuation markers. Prime coverage is exactly
\(p=13,29,37,53,61,101,109,149,157,173,181,197,229,269,277,317,349,373\), all \(p\equiv5\pmod8\).

**Observed:** PASS_D25_B2304_HARMONIC_THREE_SOURCE_CARRY 18 primes.

At \(p=373\), \(p^3=51{,}895{,}117\), \(a=233,b=326,t=93\), the independently verified source-separated residues are:

| \(D_B\Pi_{\ge p}\) source | Modulo 51,895,117 |
| --- | ---: |
| \(U^2\), low-low | 10,219,454 |
| \(2UV\), low-middle | 9,814,749 |
| \(V^2\), middle-middle | **46,190,828 = 332\(\cdot373^2\)** |
| Full \(H_B\) | **14,329,914** |

The three reduced components add to 66,225,031, congruent to 14,329,914 modulo \(373^3\), agreeing with the earlier independent p373 full-beta carry. Thus dropping the middle-middle branch is an **exact false shortcut**: it alters the third digit by \(332\equiv-41\pmod{373}\). The previous sharp endpoint residues at degrees \(2a,a+b,2b\) are respectively 43,133,524; 32,001,535; 39,512,636, with exact valuations \(0,1,2\); those are regressions, not newly claimed lemmas. No finite scan proves the all-prime scalar LIFT.

## BRC, original task and next precision action

**BRC route: COMPOSE_APPLIED.** Carrier: finite original ordered pairs \((i,j)\) in \(K_b^2\), source band, original degree, integer numerator/denominator units, \(p\)-valuation and signed weight \(1+8(i+j)\). Future observer is the **ordered** cutoff then derivative at \(z=1/9\). Equation (4) justifies a lossless binomial/harmonic compression for exactly this observer and precision \(p^3\), not for a pointwise finite-field quotient. The calculation is external finite-polynomial algebra, **not** the native P000 six-axis/three-dimensional-slice or original H0/B0 operator.

Exact smallest next mathematical task: evaluate the complete original-source residual
\[
\mathcal D_p=(U_A-U_B)+H_B+2p^2(R_A-R_B)\pmod{p^3}
\]
for both frozen classes \(p\equiv13,19\pmod{24}\), replacing the \(13\)-branch \(H_B\) by the three explicit terms in (4), and respecting \(H_B=0\) for the \(19\)-branch. Seek a finite-character/CM or nonlocal-WZ uniform certificate that cancels the A216 contribution. The original LIFT observer is still \(\Delta_p-R_p\), with the author-side exact source-port alignment in
[2026-10-26 note](20261026_onhour_d25_native_lift_source_port_identity.md). Neither a 373 numerical zero nor this p³ decomposition proves the all-prime bridge or LIFT.

**Native requirement remains separate and highest priority:** [support issue #1559](https://github.com/awdawmip/enterprise-math/issues/1559) OPEN/PENDING_OWNER at read time, no authorized executor identified. The original p373 H0/B0 divided-power \([X]U\bmod139129\), real module rank, semilinear Frobenius direction and normalization \(\eta\), signed odd Green/Hesse, native \(\kappa\), original \(\Delta_p-R_p\) and raw reproducible native code/version/inputs are **NOT_EXECUTED** by this work. The responsible route is the canonical Source owner/authorized native researcher or designated implementation maintainer; a portable scalar substitute cannot close the native benchmark. No new support task or artificial completion is asserted.

**Control and continuation:** Site configuration observed static machine read-only with research_authority_granted=false and write_relay_enabled=false; current native adapter quota 5/5 and Source code-review gate not fully verified. Historical Research-lane recovery bridge #6575 yielded no own confirmed Source claim/run, only a historical session pointer and neutral staging; dispatch #6576 failed TimeoutExpired. Current site-scoped native lookups of those old request IDs returned CONTROL_REQUEST_NOT_FOUND; this is not a license to replay. No current authenticated Researcher session, claim, open, result or Source checkpoint is asserted. For a genuinely authorized executor, first read own recovery_status, reconcile old exact requests and exact Source continuation, then use only the current schema with the same Research logical conversation, frozen pin and distinct maintenance identity. All other owner and prior author provenance remains intact.

**Continuation status:** NEW PROVED AUTHOR ALGEBRA / 18 EXECUTED CHECKS / PROJECT-NOTE AND SCRIPT / NO INDEPENDENT REVIEW / SOURCE_SYNC_DEBT / D25-LIFT-JT2 OPEN. No scheduler, hosted actions or notification changes.
