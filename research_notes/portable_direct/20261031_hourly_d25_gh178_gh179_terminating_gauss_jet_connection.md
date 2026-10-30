# D25/LIFT GH-178–GH-179: terminating Gauss parameter jets and inhomogeneous connection

Date: 2026-10-31 (Asia/Hong_Kong). Research lane: chatgpt-research-hourly-enterprise-math-20260923, distinct from maintenance. State: AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. P000 ACTIVE_LOCKED, no native X6 theorem asserted.

## Consumed frontiers and unchanged hard target

Let p=6m+1 prime, p mod24 in {13,19}. Write

\[
b_k=\frac{(1/6)_k(1/3)_k}{2^k(k!)^2},\quad
a_k=\frac{\binom{2k}{k}^{2}\binom{3k}{k}}{216^k},
\]
\[
G_p(X)=\sum_{k=0}^{p-1}b_kX^k,\qquad
\mathcal A_p(X)=\sum_{k=0}^{p-1}(6k+1)a_kX^k.
\]

The original fixed-X hard target is \(\mathcal A_p(1)\equiv p\pmod{p^3}\), NOT proved here for the infinite prime family. Existing original-source CM0 and first digit are used at their prior proof status. This new unit *consumes* rather than recredits GH-166/167's signed original R and three-port residual, GH-170/171's Gauss boundary, GH-172/175's p-adic cutoff and p4 tail, and the separately published GH-176/177 weighted-root classification / 1436-prime census. The present 166-prime regression is not a larger census or an independent review.

## GH-178: exact two-parameter-jet reconstruction of original LIFT

Define the genuine terminating-parameter deformation in \(\mathbb Z_{(p)}[t,X]\):

\[
J_p(t,X)=\sum_{k=0}^{p-1}\frac{(-m+t/6)_k(-2m+t/3)_k}{2^k(k!)^2}X^k
=P_0+tP_1+t^2P_2+O(t^3).
\]

Here P2 is the coefficient of t², already including any ordinary Taylor factorial. Since -m+p/6=1/6 and -2m+p/3=1/3, coefficientwise

\[
\boxed{G_p=P_0+pP_1+p^2P_2\pmod{p^3}.}\tag{A}
\]

There are exact support bounds \(\deg P_0\le m\), \(\deg P_1\le2m\). For 2m<k<p, the two original parameter factors each have a zero at t=0, so \(b_k/p^2\equiv [X^k]P_2\pmod p\). Coefficients \(c_{k,r}=[X^k]P_r\) obey, for 0<=k<p-1:

\[
\begin{aligned}
2(k+1)^2c_{k+1,0}&=(k-m)(k-2m)c_{k,0},\\
2(k+1)^2c_{k+1,1}&=(k-m)(k-2m)c_{k,1}+\frac{3k-4m}{6}c_{k,0},\\
2(k+1)^2c_{k+1,2}&=(k-m)(k-2m)c_{k,2}+\frac{3k-4m}{6}c_{k,1}+\frac1{18}c_{k,0}.
\end{aligned}\tag{B}
\]

Proof: expand the exact hypergeometric ratio in t and compare its first three coefficients; all divisors 2(k+1)² are p-units.

Put \(\theta=X\partial_X\), \(W=1+6\theta\), and let \(\Pi_{\ge p}\) keep only polynomial degrees >=p. Classical Clausen identity implies that the untruncated square of the Gauss hypergeometric series has coefficients a_k. Truncating both sides below p gives the *exact* finite identity

\[
\mathcal A_p=W\bigl(G_p^2-\Pi_{\ge p}(G_p^2)\bigr).
\]

Using (A), the degree support of P0 and P1, and noting the P1P2 and P2² terms have p-adic order >=3, the only high-degree contribution modulo p³ is \(2p^2\Pi_{\ge p}(P_0P_2)\). Hence the NEW full-polynomial identity

\[
\boxed{\mathcal A_p(X)\equiv W\left[(P_0+pP_1+p^2P_2)^2-2p^2\Pi_{\ge p}(P_0P_2)\right]\pmod{p^3}.}\tag{C}
\]

The source-signed projection

\[
E_p:=2\left.W\Pi_{\ge p}(P_0P_2)\right|_{X=1}\pmod p
\]

equals the actual frozen original R_p. Indeed, any degree >=p term from P0(index i<=m)P2(index j=p-a) requires a<=i; its signed weight is \(1+6(i-a)\pmod p\). Thus

\[
\boxed{E_p=R_p=
2\sum_{i=1}^m b_i\sum_{a=1}^i
[1+6(i-a)]\frac{b_{p-a}}{p^2}\pmod p.}\tag{D}
\]

The existing original-source recurrence identifies \(b_{p-a}/p^2\) with its frozen C_a. No reflected-3347 alternative or new source definition is substituted.

Write \(S_r=P_r(1)\), \(Q_r=[(1+12\theta)P_r](1)\), \(U=S_0/p+S_1\). Under the consumed CM input \(p\mid S_0\) and known first digit \(UQ_0\equiv1\pmod p\), (C) gives the exact fixed-parameter residual:

\[
\boxed{\frac{\mathcal A_p(1)-p}{p^2}\equiv
\underbrace{\frac{UQ_0-1}{p}}_{\text{carry}}+
\underbrace{S_2Q_0+UQ_1}_{\text{first and second jets}}-
\underbrace{E_p}_{\text{signed high-degree projection}}\pmod p.}\tag{E}
\]

The quotient is integral by the explicitly stated first-digit hypothesis. Equation (E) reconstructs, but does **not** globally evaluate, the old target.

## GH-179: exact triangular Picard–Fuchs boundary

Define \(L_0=\theta^2-\frac X2(\theta-m)(\theta-2m)\), \(D=\frac X{12}(3\theta-4m)\). The deformed Gauss operator has the exact parameter expansion

\[
L(t)=L_0-tD-\frac{t^2X}{36}.
\]

The *finite* polynomials must retain their boundary defect at X^p. Comparing t-jets produces

\[
\boxed{\begin{aligned}
L_0P_0&=0,\\
L_0P_1&=DP_0,\\
L_0P_2&=DP_1+\frac X{36}P_0-e_{2,p}X^p,
\end{aligned}}\tag{F}
\]
\[
e_{2,p}=\frac{(p-1-m)(p-1-2m)}2[X^{p-1}]P_2
=10m^2[X^{p-1}]P_2.
\]

Proof: (B) cancels all X^k coefficients for 0<=k<p. At k=p, the missing c_{p,r} leaves precisely the negative term from c_{p-1,2}; the P0 and P1 exit coefficients vanish by their exact supports. By prior original-series Wilson/reflection unit \(b_{p-1}/p^2=1/10\pmod p\), we obtain

\[
\boxed{[X^{p-1}]P_2=1/10,\qquad e_{2,p}=m^2=1/36\pmod p.}\tag{G}
\]

This supplies a parameter-jet realization of the *already known* GH-170 Gauss p² boundary -p²X^p/36 modulo p³, rather than falsely replacing the equation by a higher-precision homogeneous one. (A)–(C),(F) hold for all primes p=6m+1>=7; (E) uses CM/first digit and is stated for the frozen classes only.

## Evidence, BRC, unfinished objective

The actual stdlib exact-integer program d25_gh178_gh179_terminating_gauss_jet_check.py executed with terminal marker PASS_GH178_GH179_TERMINATING_GAUSS_JET_AND_TRIANGULAR_CONNECTION_EXACT. For all 330 primes p<5000,p mod6=1, it verified coefficientwise triangular ODE through degree p, support and exit unit. For the 166 target-class primes it independently formed the raw 216 and original Gauss ratios and frozen R_p, checked equation (E), plus short complete polynomial Clausen checks. This is verification/regression, not a universal LIFT proof, independent review, Lean certificate or native p373 experiment.

Sample exact scalar ports (p : carry, jets, signed projection, boundary mod p):
13:(0,0,0,4); 19:(16,15,12,9); 37:(34,14,11,36); 157:(56,26,82,48); **373:(81,115,196,114)**. In particular 81+115-196=0 mod373; none of its three contributing ports is individually zero.

BRC: COMPOSE_APPLIED to original signed tail, p-adic valuation and bound. Carrier \(\mathbb Z_{(p)}[t,X]\); branch labels (p,k,t-degree,X-degree,v_p,original-ratio), observer fixed-X=1 weighted scalar mod p³, future operations theta, parameter jets, signed high-degree projection and division by p². Total-only/low-jet compression erases necessary information; retaining the three ports in (E) is safe for this exact observer. Parameter t is an external arithmetic deformation, not a native Enterprise X6 axis.

The all-prime condition that the whole RHS of (E) vanish remains OPEN. Next scientific action: a genuinely independent finite WZ/CM/Gauss–Manin special-value certificate for the **joint signed carry + jet − projection**, with both mod24 classes preserved. Do not assume each port vanishes or change X=1. D25 H0/B0 divided-power, [X]U mod p², semilinear Frobenius, normalization eta, signed Hesse/Green and native p373 Source experiment remain separate obligations.

Gateway 0.6.11 read status: Research authorized=false, executor binding=false, active quota 5/5, control CODE_REVIEW_REQUIRED/UPSTREAM_CODE_REVIEW_REQUIRED. Own recovery_status advertised but not exposed as callable on this read-only client. Historical Source-verified checkpoint described by control support #1558 does not establish current winning successor claim; no old session or staging was modified or borrowed. Native experiment support #1559 remains distinct. No new native CLAIM, authorized OPEN, Source checkpoint, Result or review. Author-side GitHub publication requires its own readback and is not canonical scientific admission. Preserve all immutable contributions, logical conversation ID and frozen source pin.
