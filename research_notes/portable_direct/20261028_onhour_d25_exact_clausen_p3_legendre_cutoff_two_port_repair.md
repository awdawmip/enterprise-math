# D25 — exact third-digit Clausen denominator lift and two-port Legendre/finite-cutoff repair

2026-10-28 Asia/Hong_Kong. **AUTHOR-SIDE / TWO EXACT ALL-p≡1 mod6 DERIVATIONS / EXECUTED 11-PRIME INTEGER CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_NOT_EXECUTED.** Research logical lane: \`chatgpt-research-onhour-enterprise-math-20260923\` (NOT maintenance). Mother: \`ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION\`; Task: \`RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT\`; publication: \`TP2-B6F4FC938FF94941C1B7\`. **Frozen scientific Source pin remains \`c47e13e4aba0e006366f989d6334d443f6333ae3\`.** This note does not claim native Task execution, Source Result, admitted review, full original LIFT or a change to any P000 axiom.

## Exact starting point and discovered type error

Original signed object (all original cutoff indices and weights retained):
\[
W_p=\sum_{n=0}^{p-1}(6n+1)t_n,\qquad
t_n=\frac{\binom{2n}{n}^2\binom{3n}{n}}{216^n},\quad p=6m+1>3.
\]
The inherited original one-parameter jet, **already proved**, is \(W_p\equiv J_0+pJ_1+p^2J_2\pmod{p^3}\). The explicit old \(J_1,J_2\) include the low/middle/high valuation bands; we consume their exact previously recorded definitions and do not count them as new results. Target \(W_p\equiv p\pmod{p^3}\) for both \(p\equiv13,19\pmod{24}\), equivalently the source-typed \(\Delta_p-R_p\equiv0\pmod p\), is still OPEN.

**Rational identification erratum, not silent history rewrite:** the earlier author note \`20261028_onhour_d25_legendre_exact_cm_moment_p2_defect.md\` equates \(A_m(z)=\sum_j\binom mj\binom{2m}j(z/2)^j\) with \(\widetilde A_m(z)=P_{2m}(\sqrt{1-z/2})\) over Q. They are equal **only modulo \(p=6m+1\)**. Example \(m=1,p=7\): \(A_1(z)=1+z\), \(\widetilde A_1(z)=1-3z/4\). The previously proved rational Legendre moment identity remains valid for the **Legendre-defined** observer \(I_P\), but its identification with the original rational \(A\)-finite moment is invalid. In particular the earlier \(p=373\) numerical \(I_P=122350\pmod{p^2}\) is retained at precisely that scope. Do not treat a mod-p match as a rational identity or transport it one digit for free.

## Theorem A — original third digit via exact Clausen denominator

Work in \(\mathbf Z_{(p)}\). For \(0\le n\le2m\), put
\[
T_n^{(0)}=\frac{(-3m)_n(-2m)_n(-4m)_n}{2^n(n!)^3},
\quad f_n^{(0)}=(6n+1)T_n^{(0)},\quad
H_n=\sum_{j=1}^n1/j,\quad H_n^{(2)}=\sum_{j=1}^n1/j^2.
\]
Define the terminating modified-denominator polynomial
\[
G_m(z)={}_2F_1(-m,-2m;1-p/2;z/2),\quad g=G_m(1),\quad g'=G'_m(1),
\]
and the **low-band** correction sources
\[
C_1=\sum_{n=0}^{2m}f_n^{(0)}H_n,\qquad
C_2=\sum_{n=0}^{2m}f_n^{(0)}(9H_n^2+5H_n^{(2)}),
\]
\[
D_1=J_1-\tfrac32C_1,\qquad D_2=J_2-\tfrac18C_2.
\]
All displayed denominators through \(2m\) are \(p\)-units.

**Proved for every prime \(p\equiv1\pmod6\), \(p>3\):**
\[
\boxed{W_p\equiv g^2+12gg'+pD_1+p^2D_2\pmod{p^3}.}\tag{A}
\]
The standard Clausen polynomial-square identity (NIST DLMF §16.12.2, https://dlmf.nist.gov/16.12.E2), specialized to \(a=-m,b=-2m,a+b+1/2=1-p/2\), gives the coefficientwise **rational terminating identity**
\[
G_m(z)^2=\sum_{n=0}^{2m}T_n^{(0)}E_nz^n,\quad
E_n=\frac{(n!)^2}{(1-p/2)_n(1-p)_n}
=\prod_{j=1}^n(1-p/(2j))^{-1}(1-p/j)^{-1}.
\]
No denominator zero is reached: the displayed finite degree is \(2m\) and \(2m<p\), before the first zero of the formally negative integral parameter \(1-p\). Apply \(1+6z\partial_z\) at \(z=1\):
\(g^2+12gg'=\sum f_n^{(0)}E_n\).
The exact \(p\)-local product expansion is
\[
E_n\equiv1+\tfrac{3p}{2}H_n+\tfrac{p^2}{8}(9H_n^2+5H_n^{(2)})\pmod{p^3}.
\]
The already proved **original** jet has \(J_0=\sum f_n^{(0)}\), with \(J_1,J_2\) retaining middle and high terms. Subtract and substitute the definitions of \(D_1,D_2\) to prove (A). No target congruence is assumed.

In target CM0 classes accepted D24 input yields \(g\equiv0\pmod p\). Put \(\gamma=g/p\), a genuine \(p\)-integer. Then the **original signed cutoff** obeys
\[
\boxed{W_p/p\equiv12\gamma g'+D_1+p(\gamma^2+D_2)\pmod{p^2}.}\tag{A'}
\]
Formula (A') is the next precise original LIFT proof operand; its RHS has no original \(W_p\) variable, retains all low/middle/high jets and CM-root derivative, and is not asserted to equal 1 for all target primes.

## Theorem B — exact rational Legendre transport defect at p²

Define **distinct** rational polynomials
\[
A(z)=\sum_{j=0}^m b_jz^j,\quad b_j=\binom mj\binom{2m}j2^{-j},
\quad\widetilde A(z)=P_{2m}(\sqrt{1-z/2}),
\]
\[
B(z)=-\sum_{j=1}^mb_j(H_{2m}-H_{2m-j})z^j.
\]
Since \(m+1/2=-2m+p/2\), coefficientwise multiplication in \(\mathbf Z_{(p)}[z]\) proves
\[
\widetilde A\equiv A+\tfrac p2 B,\qquad
\widetilde A^2-A^2\equiv pAB\pmod{p^2}.\tag{B0}
\]
For any polynomial \(C\) of degree \(\le m\), define its source-typed finite moment
\[
F_C=(1+6z\partial_z)C(z)^2,\quad
\mathfrak I(C)=\sum_{s=0}^{2m-1}u_s[z^s]\frac{F_C(1)-F_C(z)}{1-z},\qquad
u_s=\frac{8^s(s!)^2}{(2s+1)!}.
\]
The difference quotient is polynomial, and \(2s+1<p\). Put \(I_A=\mathfrak I(A)\), \(I_P=\mathfrak I(\widetilde A)\), \(V=(1+6z\partial_z)(AB)\) and
\[
\mathcal L_p=\sum_{s=0}^{2m-1}u_s[z^s]\frac{V(1)-V(z)}{1-z}\pmod p.
\]
Apply the same linear differential, difference-quotient and finite-moment operations to (B0). Every denominator is a \(p\)-unit, proving the new all-\(p\) transport identity
\[
\boxed{I_P-I_A\equiv p\mathcal L_p\pmod{p^2}.}\tag{B}
\]
It corrects the former over-Q identification while retaining the old Legendre rational identity \(I_P=6+a\Lambda_m\) solely at its actual Legendre-defined observer.

## Theorem C — source-preserving two-port bridge, no original LIFT claim

On the target CM0 classes, the inherited mod-p Cauchy/CM0 argument gives \(I_A\equiv I_P\equiv6\pmod p\) and accepted first-digit UR gives \(W_p\equiv p\pmod{p^2}\). Combine (A') and (B) to obtain
\[
\boxed{\frac{W_p}{p}-\frac{I_P}{6}
\equiv \underbrace{12\gamma g'+D_1+p(\gamma^2+D_2)-\frac{I_A}{6}}_{\mathcal E_{\rm cut}}
\ -\underbrace{\frac{p}{6}\mathcal L_p}_{-\mathcal E_{\rm Leg}}\pmod{p^2}.}\tag{C}
\]
This is a genuine formula entirely in terms of the terminating \(G\)-polynomial, its signed original \(J_1,J_2\) ports and **distinct** A/Legendre moments. The original full finite cutoff has not been replaced by an unsourced Legendre rational lift. The uniform cancellation to \(W_p/p=1\pmod{p^2}\) remains OPEN.

At fixed \(p=373\), \(p^2=139129\), \(p^3=51895117\), independent exact modular computations give:
\[
(g,g',\gamma)=(22795149,118162,61113),\quad
(J_0,J_1,J_2)=(15521276,47909,133),
\]
\[
(C_1,C_2,D_1,D_2)=(84271,20,130196,317),\quad
(I_A,I_P,\mathcal L_p)=(77590,122350,120),\quad W_{373}=373.
\]
Here residues use mod \(p^3\) for \(g,J_0,W\), mod \(p^2\) for \(g',\gamma,J_1,C_1,D_1,I_A,I_P\), mod p for \(J_2,C_2,D_2,\mathcal L_p\). In normalized second-digit units,
\[
\mathcal E_{\rm cut}\equiv-159p,\quad -p\mathcal L_p/6\equiv-20p,\quad
W_{373}/373-I_P/6\equiv-179p\pmod{p^2}.
\]
Thus the earlier unexplained 179p defect has TWO mathematically distinct retained branches: 159 from original finite weighted cutoff/Clausen and 20 from rational Legendre lift. The scalar values neither yield the native Frobenius coefficient nor prove an all-prime zero.

## Actually executed independent checks and precise continuation

Companion source \`research_notes/portable_direct/d25_clausen_p3_lift_guard_20261028.py\` was run locally using standard-library **integer modular** arithmetic on primes \(7,13,19,31,37,43,61,67,73,211,373\); marker \`PASS_D25_CLAUSEN_DENOMINATOR_P3_SOURCE_BANDED_BRIDGE 11 primes\`. Tests cover all \(2m+1\) Clausen coefficients, mod \(p^3\) denominator expansions, full original \(n<p\) binomial-coefficient sum, separately generated triple-factor parameter jets and valuation bands, polynomial A/Legendre coefficient defect, moments (B), original target (A') and p373 exact fixtures. This checks implementations/instances, **not** universal validity or formal admission. A Lean proof and native H0/B0 were NOT run.

BRC \`COMPOSE_APPLIED\`: typed signed carrier \((p,m,n,6n+1,t_n,\text{original cutoff},\text{low/middle/high valuations},J_1,J_2,g,g',I_A,I_P,\mathcal L_p,\Delta/R)\); declared output \(W_p\bmod p^3\), \(W_p/p\bmod p^2\) on CM0 classes and separately typed moments; preserved full signed joint source and future native operator requirements. External scalar arithmetic does NOT replace the P000 six-axis discrete Heartbeat X6 Cell substrate, separately typed time, or establish native X6 propagation; **no native plane**.

Highest original-class native benchmark remains \`awdawmip/enterprise-math#1559\`: actual H0/B0 divided-power \(p=373\), \([X]U\bmod139129\), module rank, semilinear Frobenius direction and \(\eta\), odd signed Green/Hesse, original \(\kappa\), \(\Delta_p-R_p\), original raw source-bound reproducible evidence. The issue was OPEN/unassigned at current read; executor remains pending. This Site has \`research_authority_granted=false\`, \`write_relay_enabled=false\`, active native control quota \(5/5\) and upstream review gate. Old own bridge \`awdawmip/kimi-query-bridge#6575\` is merely historical local ACTIVE session pointer without winning CLAIM/run; \`#6576\` final FAILED/TimeoutExpired. Do NOT replay requests, borrow maintenance identity, or fold neutral staging into accepted Source. No native CLAIM/open/Source checkpoint/Result/Driver review was performed.

**Next exact science:** use (A') retaining \(D_1,D_2,\gamma,g'\) and original signed middle/high factorial ports for a **uniform** target-class cancellation proof or precise counterexample; retire the false rational A=Legendre identification at p² and apply explicit repair (B). D25/LIFT/JT2 and #1559 remain OPEN; frozen scientific pin unchanged. Formal Research-Activity registration, native Source checkpoint and independent review remain pending genuine authorized execution. No scheduler, Action, cron or hosted chain has been created.