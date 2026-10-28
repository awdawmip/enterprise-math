# D25/LIFT GH-77–GH-78: transverse Laurent amplitude and odd-degree source operator

2026-10-29 Asia/Hong_Kong. TASK_RESEARCH portable author-side research for stable logical conversation chatgpt-research-hourly-enterprise-math-20260923, separated from maintenance. Mother ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION OPEN; task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Frozen science Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Status AUTHOR-DERIVED / AUTHOR-EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Exact previous source interfaces

GH-15/16 (commit c5fab90f2bbe1cbe8581cef4179aa532cf040388): for prime p=4d+3>=7, rank 0<=r<=d and z unequal 0 or 1, source weights C_0(z)=1 and C_{r+1}(z)/C_r(z)=z(4r+1)^3/[(4r+2)(4r+3)(4r+4)]. Laurent double-pole coefficients of the actual rankwise resolvent satisfy C_r(z)A_r(z)=A_0(z), where

\[
A_0(z)=\frac{\alpha_p z^{2d+2}}{z-1}\,\mathcal H_d(z),\qquad
\mathcal H_d(z)=\sum_{r=0}^{d}(8r+5)h_rz^r,\qquad
h_0=1,\quad h_{r+1}/h_r=\frac{(4r+3)^3}{(4r+4)(4r+5)(4r+6)}.
\]

The explicit GH-16 factor alpha_p is a nonzero element of F_p, depending on the original ordered source and the two valuation poles.

GH-17/18 (commit c9732de542130f4d376f9833973b1538b1306d47): if p=8m+3, d=2m, then \(\mathcal H_d=F_mG_m\) as entire polynomials in F_p[z], where \(F_m={}_2F_1(-m,-m;2m+2;z)\), \(G_m=(16z\partial_z+5)F_m\), and
\[
16z(1-z)G'_m=(7z+1)G_m+(z-5)F_m.
\]

GH-74/75 (commit 6a7cbaebed0ca6ce1050bb97047e320569e41200) gave an author-side CM/Cartier classification, awaiting independent review:
\[
p\equiv11\pmod{24}:G_m(9)=0,\ F_m(9)\ne0,\qquad
p\equiv19\pmod{24}:F_m(9)=0,\ G_m(9)\ne0.
\]
This classification is a stated dependency, not newly proved or independently admitted here.

## GH-77 — exact nonzero first-order Laurent slope at every original rank

**Theorem, using the GH-75 classification:** For every prime p=8m+3>=11, d=2m,
\[
\boxed{\mathcal H_d'(9)=
\begin{cases}
-F_m(9)^2/288,&p\equiv11\pmod{24},\\
 G_m(9)^2/144,&p\equiv19\pmod{24}.
\end{cases}}\tag{77.1}
\]
Both quantities are nonzero in F_p.

Define \(Q_p=\alpha_p9^{2d+2}/8\in\mathbb F_p^\times\). For each original rank \(0\le r\le d\):
\[
\boxed{A_r'(9)=\frac{Q_p}{C_r(9)}
\begin{cases}
-F_m(9)^2/288,&p\equiv11\pmod{24},\\
 G_m(9)^2/144,&p\equiv19\pmod{24},
\end{cases}\quad A_r'(9)\ne0.}\tag{77.2}
\]
Thus \(A_r(9+\varepsilon)=\varepsilon A_r'(9)\) in the dual-number ring \(\mathbb F_p[\varepsilon]/(\varepsilon^2)\), with a nonzero exact slope at every rank. This *formal first-order parameter* statement is not automatically a congruence modulo p² for any chosen integer source lift.

**Proof.** If p=11 mod24, GH-75 gives G(9)=0, F(9) nonzero. GH-18 at z=9 gives \(-1152 G'(9)=4F(9)\), i.e. \(G'(9)=-F(9)/288\). Hence \((FG)'(9)=-F(9)^2/288\). If p=19 mod24, F(9)=0 and \(G(9)=144F'(9)\), hence \((FG)'(9)=G(9)^2/144\). Nonzero follows since p is neither 2 nor 3 and the surviving GH-75 channel is nonzero. Differentiating the GH-16 original-source relation gives \(A'_0(9)=Q_p\mathcal H'_d(9)\), because \(\mathcal H_d(9)=0\). Differentiating \(C_r A_r=A_0\), since \(A_r(9)=0\) and \(C_r(9)\) is a unit, yields \(A'_r(9)=A'_0(9)/C_r(9)\). The dual-number result is exact Taylor evaluation. QED.

**Observer distinction.** GH-76 proved only that the order-two pole coefficient vanishes at the exact z=9 fiber. The source-relative rank slopes in (77.2) survive a permitted perturbation of z and are needed for any derivative or higher-digit bridge. In BRC terms the adequate carrier retains (p,d,r,z,C_r,alpha_p,F/G port, A_r,A'_r, Laurent order, arithmetic signs/valuations); reducing this to the scalar snapshot A_r(9)=0 loses future-operational information. Source-faithful COMPOSE_APPLIED, not a claim about native X6 geometry.

## GH-78 — exact third-order hypergeometric operator for *all* p=3 mod4

For any prime p=4d+3>=7, define \(U_d(z)=\sum_{r=0}^d h_rz^r\) using the same GH-16 coefficients. Let \(\theta=z\partial_z\). Then:
\[
\boxed{\left[\theta(\theta+\tfrac14)(\theta+\tfrac12)-z(\theta+\tfrac34)^3\right]U_d(z)=0\quad\text{in }\mathbb F_p[z].}\tag{78.1}
\]
The unique polynomial of degree at most d with constant coefficient 1 satisfying this ODE is U_d, with degree exactly d. The full GH-16 observed obstruction is
\[
\boxed{\mathcal H_d=(8\theta+5)U_d,\qquad \mathcal H_d(9)=72U_d'(9)+5U_d(9).}\tag{78.2}
\]

**Proof.** At z^k for 1<=k<=d the operator gives \(k(k+1/4)(k+1/2)h_k-(k-1/4)^3h_{k-1}=0\), exactly the original GH-16 recurrence. The coefficient at z^{d+1} is \(-(d+3/4)^3h_d=-(p/4)^3h_d=0\) in characteristic p; all other coefficients are zero. For k=1,...,d, the coefficient multiplying h_k is a unit, proving uniqueness from h_0=1. All original numerator and denominator recurrence factors through r=d-1 are units, so h_d is nonzero. The observer identity is immediate from its original source definition. QED.

**Odd-degree no-go.** If p=8m+7, d=2m+1 and the top coefficient of \(\mathcal H_d\) is \((8d+5)h_d\equiv-h_d\ne0\pmod p\). Hence
\[
\boxed{\deg\mathcal H_{2m+1}=2m+1.}\tag{78.3}
\]
Therefore it is *impossible* to extend the GH-17 same-half-degree factorization in the form \(\mathcal H_{2m+1}=P_mQ_m\), with deg P_m and deg Q_m both <=m: the product has degree <=2m. This does not exclude an asymmetric (m,m+1) factorization, a different arithmetic representation or a vanishing at z=9. At z=9 the third-order operator's highest-derivative coefficient z³(1-z) is a unit, so local differential initial data alone do not enforce the CM special value; retain global arithmetic constraints.

## Exact local verification and scientific boundary

The accompanying Python standard-library checker independently constructs h_r, F_m, G_m and the GH-16 alpha_p product. It checks (78.1) coefficientwise *through degree d+1* for every prime 7<=p<2000 with p=3 mod4. For p=3 mod8, it checks the entire polynomial factorization, both formulas in (77.1), the GH-16 rational obstruction derivative via quotient rule, and the transported nonzero slope at every original rank.

Executed output:
\`\`\`
PASS_GH77_SLOPE_CM_CLASS 76 primes p< 2000 rank slope checks 17342
PASS_GH78_HYPERGEOMETRIC_OPERATOR 154 primes p=3(mod4) coefficient checks 35512
PASS_GH78_ODD_DEGREE_NO_GO 78 primes p=7(mod8)
OBSERVED_ONLY_GH78_ODD_CLASS_H9_ZERO 78 of 78
\`\`\`
The last observation is finite-sample evidence only, not an all-prime theorem. All GH-77 universal claims inherit GH-75's **unreviewed author proof** as an explicit dependency. No Source/Driver admission, native experiment, claim/open or canonical Source checkpoint is represented by GitHub persistence.

## Continuation

Parent: GH-3 truncated-sum all-prime congruence and D25/LIFT/JT2 OPEN. For p=3 mod8, GH-76's original-source residual \(C_d(H_d+8d+1)-H_0+BL\) retains independent endpoint and first-order Laurent obligations; do not confuse the Laurent constants H_0,H_d with the obstruction polynomial \(\mathcal H_d\). For p=7 mod8, GH-78 supplies a precise full-rank differential operator but the odd-degree source obstruction at 9 still needs an independent CM/arithmetic certificate. Next useful unit: seek an **asymmetric, source-faithful (m,m+1) factorization** or a genuine finite-field characteristic sum at z=9 for p=7 mod8; do not re-run GH-17 as a symmetric factorization. A genuine p² lift must be established before consuming dual-number sensitivity as the next p-adic digit.

Native control diagnosis as observed 2026-10-29: gateway 0.6.11, research_authority_granted=false, executor_binding_configured=false, source_sync.control.state=CODE_REVIEW_REQUIRED, authenticated subject active_jobs=5/5, new_job_allowed_by_quota=false. The gateway exposes a recovery_status contract but no corresponding direct callable tool here. Research lane historical recovery/continuation receipts and protected staging remain under enterprise-math Issue #1558; these do not establish current winning Source ownership. No mutation to sessions/claims/requests/staging was made. Preserve unknown protected old state; register native role/research activity and publish Source checkpoint only under its proper current contract.

P000/ACTIVE Heartbeat X6 discrete Cell ontology and separate time remain fixed. z and rank r are external auxiliary scalar parameters. Science source pin remains unchanged; the author proof is UNREVIEWED/NOT_ADMITTED and the result stays a portable candidate.