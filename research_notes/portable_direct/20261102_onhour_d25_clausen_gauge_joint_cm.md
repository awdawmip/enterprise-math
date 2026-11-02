# D25 — Terminating Clausen denominator gauge and signed CM interaction (2026-11-02)

**Status:** AUTHOR-DERIVED / EXACT HAND DERIVATION / FINITE EXACT REGRESSION / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. This is author-side research evidence, neither a Source Research checkpoint nor the original H0/B0 experiment.

**Mother task:** RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin carried verbatim c47e13e4aba0e006366f989d6333ae3; research logical conversation chatgpt-research-onhour-enterprise-math-20260923, distinct from maintenance. The original scientific pin could not be resolved as a standalone Git commit through this connector; no pin mutation is made.

## 1. Exact coefficientwise terminating Clausen gauge

For every prime p=6m+1>3 let

\[
\mathsf P(z)={}_2F_1(-m,-2m;1-p/2;z)
=\sum_{r=0}^m c_rz^r,\quad
q_k=[z^k]\mathsf P(z)^2.
\]

For 0<=k<=2m put

\[
G_k=\frac{(1-p/2)_k(1-p)_k}{(k!)^2}
=\prod_{j=1}^k(1-p/(2j))(1-p/j).
\]

The terminating Clausen coefficient formula, with a=-m,b=-2m, yields

\[
q_k=\frac{(-2m)_k(-3m)_k(-4m)_k}
{(1-p/2)_k(1-p)_k k!}.
\]

All denominators for these k are p-units. Consequently the **exact rational identity**

\[
\boxed{q_kG_k=\frac{(-2m)_k(-3m)_k(-4m)_k}{(k!)^3}}
\tag{1}
\]

holds coefficient by coefficient. The singularity of the formal lower hypergeometric parameter 1-p arises beyond the finite interval k<=2m and is not inverted or used.

With theta=z d/dz, (1) may be operated on by any polynomial in theta and then evaluated at z=1/2, preserving all such observers coefficientwise. The previously established original W216 three-root low band is

\[
A_0=\sum_{k=0}^{2m}(6k+1)
\frac{(-2m)_k(-3m)_k(-4m)_k}{2^k(k!)^3}.
\]

Expanding the finite gauge product gives

\[
G_k\equiv1-\tfrac{3p}{2}H_k+
\tfrac{p^2}{8}(9H_k^2-5H_k^{(2)})\pmod{p^3}.
\tag{2}
\]

Define the signed Cauchy-gauge ports
\[
\mathcal H_1=\sum_{k=0}^{2m}(6k+1)q_k2^{-k}H_k,\quad
\mathcal H_2=\sum_{k=0}^{2m}(6k+1)q_k2^{-k}(9H_k^2-5H_k^{(2)}).
\]
Writing P=mathsf P(1/2), P'=mathsf P'(1/2), the square and its Euler derivative give
\[
\boxed{A_0\equiv P(P+6P')-\tfrac{3p}{2}\mathcal H_1+
\tfrac{p^2}{8}\mathcal H_2\pmod{p^3}.}
\tag{3}
\]

**Proof:** the exact coefficient formula is the finite-degree specialization of classical Clausen's quadratic-square identity. The log of G_k is -3p H_k/2-5p^2 H_k^(2)/8 modulo p^3; exponentiating gives (2). Apply 1+6 theta to the square and to each harmonic coefficient. This proves (3) as a p-adic consequence of exact rational polynomial identities. The first and second harmonic ports are independently defined signed sums, not fitted corrections.

## 2. Compose with a distinct hourly Research lane's ordinary Gauss Hensel coordinates

The separate hourly author-side note 20261102_hourly_r11_d25_cm_hensel_cauchy_transport.md defines
\[
P_0(z)={}_2F_1(-m,-2m;1;z)=\sum_{r=0}^m\binom mr\binom{2m}r z^r.
\]
Set z0=1/2, j=(theta P0)(z0), C=sum_r binom(m,r)binom(2m,r)2^-r H_r. Expansion of the deformed denominator proves
\[
\boxed{\mathsf P(z)\equiv P_0(z)+
\tfrac p2\sum_r\binom mr\binom{2m}r H_r z^r\pmod{p^2}.}
\tag{4}
\]

In the target classes p≡13,19(mod24), consume the previously accepted CM0 result P0(z0)≡0 mod p and put c=P0(z0)/p mod p. The old D24 first digit gives A0≡0 mod p; thus (3),(4) imply
\[
\boxed{A_0/p\equiv12j(c+C/2)-\tfrac32\mathcal H_1\pmod p.}
\tag{5}
\]

This explicitly connects the original low-band divided carry to the ordinary Hensel c,j coordinate without borrowing the other Research lane's role/session or recrediting its simple-root proof.

## 3. Exact BRC source-interaction repair

Let beta_i=binom(m,i)binom(2m,i)2^-i. Define the ordered, signed interaction
\[
\boxed{\Xi=\sum_{i,j=0}^m(1+6(i+j))\beta_i\beta_j
(H_{i+j}-H_i-H_j)\pmod p.}
\tag{6}
\]

Decompose the genuine pair harmonic H_(i+j) into marginals H_i+H_j and the residual in (6). With C_theta=sum i beta_i H_i, **direct expansion** yields for every p=6m+1:
\[
\mathcal H_1\equiv
2(P_0 C+6(P_0 C_\theta+jC))+\Xi\pmod p.
\tag{7}
\]

For CM0, P0=0 mod p, so H1=12jC+Xi and (5) becomes
\[
\boxed{A_0/p\equiv12j(c-C)-\tfrac32\Xi\pmod p.}
\tag{8}
\]

This is a concrete BRC observer-preserving decomposition: carrier is the original ordered pair (i,j), original signed weight and p-adic coefficient/unit; observer is the low-band divided carry and allowed finite Euler operators. Removing the joint pair and retaining independent marginals requires the repair coordinate Xi. It is not asserted as a native X6/H0/B0 geometric identity.

## 4. Precise reuse by the frozen mother observer

Consume prior on-hour result
\[
\Delta_p-R_p\equiv D_0+A_2+B_2+C_2,\quad
D_0=(A_0+p(A_1+B_1)-p)/p^2\pmod p.
\]
Put
\[
\Psi=P(P+6P')-\tfrac{3p}{2}\mathcal H_1+p(A_1+B_1)-p.
\]
Because D24 established the original first digit and (3) holds mod p^3, p² divides Psi in the target classes. The **same-original-definition, source-aligned equivalence** is
\[
\boxed{\Delta_p-R_p\equiv
\Psi/p^2+\mathcal H_2/8+A_2+B_2+C_2\pmod p.}
\tag{9}
\]

The signed high band C2 remains the earlier Wilson-reflected original B2_W; A2,B2 are the previously computed finite three-root jet ports. The remaining all-target cancellation in (9) is an open mathematical obligation, with no new axiom.

## 5. Independent exact arithmetic coverage

Executed standard-library integer modular checker on **all 207 primes p<=3000 with p≡1(mod6)**, including all **107** D25 target primes. It verifies **94,771 coefficientwise positions**, three Euler observers, the independently constructed original three-factor T_k recurrence, the finite gauge against cubic harmonic expansion, ordinary/deformed Gauss displacement, both CM divided first-digit formulas and signed interaction. Independent direct integer-binomial crosschecks passed for p=7,13,19,37,43,373,1171; **zero mismatches**. The full executed program and 207-prime JSON are also preserved in this run's evidence ZIP.

| p | c | j | C | Xi | H1 | H2 | A0/p mod p |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 13 | 7 | 7 | 3 | 2 | 7 | 12 | 8 |
| 19 | 6 | 1 | 17 | 17 | 12 | 10 | 4 |
| 37 | 21 | 24 | 28 | 22 | 20 | 23 | 23 |
| **373** | **340** | **294** | **321** | **286** | **346** | **317** | **209** |
| 1171 | 1082 | 544 | 161 | 39 | 660 | 1129 | 901 |

For p373 the original low A0 mod p³ is 15,521,276, and ordinary Hensel shift t_CM=-c/(2j) is 276, matching the independently published hourly lane. With prior A1 mod p²=3122 and B1 mod p²=44787, the new divided port Psi/p²=247 and H2/8=366. Retaining the pre-existing A2=82, B2=158, C2=266 gives the **five-source original check**
\[
247+366+82+158+266=1119=3\cdot373\equiv0\pmod{373}.
\tag{10}
\]

For the 107 tested target primes Xi is nonzero in all 107; H2 is nonzero in 106 (p=1453 is an observed zero). These are finite results and do not prove universal nonvanishing.

## 6. Continuation

**Next smallest mathematical unit:** construct and test a terminating contiguous/WZ certificate for Psi/p² + H2/8 + A2+B2 = -C2 for both p≡13,19 mod24. Determine whether Xi can be transported via the distinct original Cauchy slope port or remains an independent joint correction. Check p=13,19,373 and a non-CM p=7 with original coefficients and signs.

**Native p373 H0/B0:** existing issue #1559 remained OPEN/unassigned on 2026-11-02; actual [X]U mod139129, module rank, semilinear Frobenius, eta, signed odd Green/Hesse kappa and independent reproduction remain pending. This scalar proof does not count as that experiment.

**Control:** 2026-11-02 08:06 UTC authenticated read-only gateway 0.6.11 reported research authorization=false and write relay=false; historical dispatch request research-onhour-20261031-0205-dispatch-r15 was not replayed. Read-only reconcile returned STATIC_READONLY_SCOPE_DENIED (operation_sent=false), own checkpoint ACCESS_DENIED, exact continuation CONTROL_QUOTA. No authenticated own Source session, claim, run, checkpoint or formal admission. The necessary execution route is a separately authorized Site-bound Research client, actual executor binding and secure user credential. No maintenance conversation identity used.

**Source provenance:** preceding on-hour three-root, three-band, half-cutoff and original Wilson research notes; independently owned hourly CM Hensel note; finite Clausen source at research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_FINITE_CLAUSEN_DERIVATIVE_BRIDGE_RETURN_20260827.md; P000/ACTIVE Heartbeat/observer-preservation and current account mathematical policy. No scheduler, Actions, hosted cron, cadence or notification modification.
