# D25 original 216 — source-separated Legendre/Clausen Hensel-root transport through the third p-adic digit

2026-10-28 12:58–13:xx Asia/Hong_Kong. Classification: **AUTHOR-SIDE / EXACT CONDITIONAL ALGEBRAIC TRANSPORT / EIGHT EXACT ORIGINAL-SUM CHECKS / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_NOT_EXECUTED**. Independent review and canonical Source checkpoint are separate open duties.

Mother objective: `ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION`.
Canonical Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`.
On-hour Research logical conversation label: `chatgpt-research-onhour-enterprise-math-20260923`; distinct from CONTROL_PLANE_MAINTENANCE. Label is not a native service-signed claimant.
**Frozen scientific Source pin: `c47e13e4aba0e006366f989d6334d443f6333ae3` (unchanged).**
Project P000 is the locked six-dimensional discrete Heartbeat X6 native Cell substrate plus separately typed time. The univariate z below is an **external exact arithmetic observer**, not a native plane, axis, complete X6 state or H0/B0 computation.

## Existing exact ingredients, used without re-proving

For any prime p=6m+1>3 work in \\(\\mathbf Z_{(p)}\\) and its p-adic completion, retaining the original signed finite cutoff:
\\[
W_p=\\sum_{n=0}^{p-1}(6n+1)
\\frac{\\binom{2n}{n}^2\\binom{3n}{n}}{216^n}.
\\]
Define the genuine three distinct terminating polynomials
\\[
P(z)=P_{2m}(\\sqrt{1-z/2})={}_2F_1(-m,m+1/2;1;z/2),
\\quad G(z)={}_2F_1(-m,-2m;1-p/2;z/2).
\\]
With \\(b_j=\\binom mj\\binom{2m}j2^{-j}\\), \\(M_j=H_{2m}-H_{2m-j}\\) and \\(M_j^{(2)}=H_{2m}^{(2)}-H_{2m-j}^{(2)}\\), keep the *separate source corrections*
\\[
E(z)=\\sum_{j=1}^{m}b_j(H_j+M_j)z^j,
\\quad
F(z)=\\sum_{j=1}^{m}b_j(H_j^2+H_j^{(2)}-M_j^2+M_j^{(2)})z^j.
\\]
The prior author-side coefficient theorem at [fa9d94](https://github.com/awdawmip/enterprise-math/blob/fa9d94ada992435820ab9911a4d8127f1e7bde29/research_notes/portable_direct/20261028_onhour_d25_legendre_clausen_third_digit_hensel_root_bridge.md) gives, coefficientwise,
\\[
G=P+\\frac p2 E+\\frac{p^2}{8}F\\pmod{p^3}.
\\tag{input-1}
\\]
The original signed low/middle/high cutoff Clausen bridge from [978a262](https://github.com/awdawmip/enterprise-math/blob/978a2622d1f25389f8edd6e7bc1ac8a36be5424d/research_notes/portable_direct/20261028_onhour_d25_exact_clausen_p3_legendre_cutoff_two_port_repair.md) is
\\[
W_p\\equiv g^2+12gg'+pD_1+p^2D_2\\pmod{p^3},\\quad
g=G(1),\\quad g'=G'(1).
\\tag{input-2}
\\]
The \\(D_1,D_2\\) ports retain all original coefficient and valuation bands; their exact J/C definitions reside in the above immutable source. The previously admitted target-class CM0 gives \\(P(1)\\equiv0\\pmod p\\) for \\(p\\equiv13,19\\pmod{24}\\), and the prior simple-root argument gives \\(P'(1)\\not\\equiv0\\pmod p\\). No use of the desired W_p congruence is made below.

## New Theorem A — exact two-port transport between two simple Hensel roots

For either target class, let \\(\\zeta,\\xi\\in1+p\\mathbf Z_p\\) be the *unique* roots \\(P(\\zeta)=0\\), \\(G(\\xi)=0\\). Define
\\[
a=P'(\\zeta),\\quad b=P''(\\zeta),\\quad
e=E(\\zeta),\\quad e_1=E'(\\zeta),\\quad f=F(\\zeta),
\\quad\\delta=\\xi-\\zeta.
\\]
Since a is a p-adic unit, **for all target primes, conditional on the exact preceding CM0 and transport inputs,**
\\[
\\boxed{\\delta\\equiv
-\\frac{pe}{2a}
+p^2\\left(-\\frac{be^2}{8a^3}
+\\frac{ee_1}{4a^2}-\\frac{f}{8a}\\right)
\\pmod{p^3}.}\\tag{A}
\\]
All displayed divisions are by p-adic units. In particular \\(\\delta/p\\bmod p^2\\) has independent curvature, first-derivative and second-transport provenance.

**Proof.** Input-1 evaluated at \\(z=\\zeta+\\delta\\) and \\(G(\\xi)=P(\\zeta)=0\\) yields \\(0=a\\delta+b\\delta^2/2+p(e+e_1\\delta)/2+p^2f/8\\pmod{p^3}\\). Simple-root uniqueness and input-1 mod p imply \\(\\delta\\in p\\mathbf Z_p\\). Write \\(\\delta=p\\alpha+p^2\\beta\\), solve at p and p²: \\(\\alpha=-e/(2a)\\), \\(\\beta=-be^2/(8a^3)+ee_1/(4a^2)-f/(8a)\\). This proves (A). No hypothesis about original LIFT is used. QED.

**New Theorem B — use the exact Legendre differential equation to eliminate curvature.**
The hypergeometric P satisfies the exact equation
\\[
z(2-z)P''+(2-3z/2)P'+m(m+1/2)P=0.
\\]
At \\(z=\\zeta\\equiv1\\pmod p\\) and \\(P(\\zeta)=0\\), divide by the unit \\(P'(\\zeta)\\): \\(b/a\\equiv-1/2\\pmod p\\). Substituting into (A), for all target primes,
\\[
\\boxed{\\xi-\\zeta\\equiv
-\\frac{pE(\\zeta)}{2P'(\\zeta)}
+p^2\\left(
\\frac{E(\\zeta)^2}{16P'(\\zeta)^2}
+\\frac{E(\\zeta)E'(\\zeta)}{4P'(\\zeta)^2}
-\\frac{F(\\zeta)}{8P'(\\zeta)}
\\right)\\pmod{p^3}.}\\tag{B}
\\]
The full \\(p^2F\\) port is essential: dropping it changes an observable third-digit root displacement in general. This is an *exact algebraic coefficient statement*, not a numerical fit. QED.

## New Theorem C — transport the original signed 216 cutoff into the Legendre-root coordinates

Define \\(d_L=(\\zeta-1)/p\\), \\(t=(\\xi-\\zeta)/p\\), \\(B=P'(1)\\), \\(h=E'(1)\\). The quantities \\(d_L,t\\) are p-adic integers determined by B, and \\(d_G=(\\xi-1)/p=d_L+t\\). From coefficientwise input-1, \\(G'(1)\\equiv B+(p/2)h\\pmod{p^2}\\); therefore
\\[
G'(1)^2\\equiv B^2+pBh\\pmod{p^2}.
\\]
The previously established Hensel-root form of input-2 therefore gives the **complete original cutoff** in these two typed ports:
\\[
\\boxed{\\frac{W_p}{p}\\equiv
D_1-12(d_L+t)B^2+
p\\left[D_2-12(d_L+t)Bh+4(d_L+t)^2B^2\\right]
\\pmod{p^2}.}\\tag{C}
\\]
Equation (B) supplies t mod p² without silently identifying the rational Legendre and original finite hypergeometric polynomials. Equations (B) and (C) are the **new exact finite identities**; the further all-target-prime cancellation that makes the RHS of (C) equal 1 remains **OPEN**.

More sharply, the isolated F-port in (B) gives
\\[
t_F=-\\frac{pF(\\zeta)}{8P'(\\zeta)}\\pmod{p^2}.
\\]
If all other displayed ports are held fixed, its linear contribution to the original normalized RHS (C) is precisely
\\[
\\boxed{\\frac{3p}{2}P'(1)F(\\zeta)\\pmod{p^2}.}\\tag{D}
\\]
Equation (D) is a source-budget contribution, not the full value of \\(W_p/p\\) or an independent third-digit supercongruence. It gives an explicit error witness against dropping the second-order Legendre/Clausen transport.

## Actual integer tests, including an independent original-216 check

Companion source `research_notes/portable_direct/d25_legendre_clausen_root_transport_guard_20261028.py` was actually executed in Python 3 standard-library modular integers for eight target primes
\\[
13,19,37,43,61,67,211,373.
\\]
For each it constructs P/G/E/F by separate finite products, verifies the mod \\(p^3\\) coefficients, separately Hensel-lifts both roots, verifies (A), (B), the exact Legendre ODE consequence and (C). **Critically**, (C) is independently checked against the *original signed* full sum \\(W_p\\) via exact integer binomial coefficients; an independent full triple-Pochhammer jet rebuilds \\(D_1,D_2\\) with all three original valuation bands. Assertions passed:
`PASS_D25_ROOT_TRANSPORT_ALL_TARGET_INSTANCES 8`.
This finite check validates implementation and eight instances; the stated universal algebraic identities are derived above and remain subject to independent review.

At p=373, m=62, p²=139129, p³=51895117, exact integer residues:
\\[
\\zeta=39023261,\\quad\\xi=10790145,\\quad\\delta=23662001
\\pmod{51895117},
\\]
\\[
d_L=104620,\\quad t=63437,\\quad d_G=d_L+t=28928
\\pmod{139129}.
\\]
\\[
P'(\\zeta)=294,\\ E(\\zeta)=163,\\ F(\\zeta)=155\\pmod{373},
\\quad B=P'(1)=85711\\pmod{139129},\\quad h=E'(1)=174\\pmod{373}.
\\]
The first displacement digit \\((\\delta/p)\\bmod p\\) equals 27. The p² correction in (B), **relative to the full first term** \\(-pE(\\zeta)/(2P'(\\zeta))\\), has separately labeled residues
\\[
(\\text{curvature},\\text{E-derivative},\\text{F port})
=(89,110,15)\\pmod{373},\\quad 89+110+15=214.
\\]
The F-port alone gives a **nonzero 96p** contribution through (D) to (C) at this prime. Direct original-sum and independent jets yield
\\[
D_1=130196\\pmod{139129},\\quad D_2=317\\pmod{373},\\quad
\\frac{W_{373}}{373}\\equiv1\\pmod{139129}.
\\]
The complete RHS of (C) independently equals 1 modulo 139129. These are exact integer certificates and do not extrapolate to all primes.

## BRC source/observer typing and continuation

**BRC COMPOSE_APPLIED:** carrier \\((p,m,n,6n+1,\\text{original cutoff},\\nu_p\\text{ by band},J_1,J_2,C_1,C_2,D_1,D_2,P,G,E,F,\\zeta,\\xi,\\delta,B,h)\\). Operators: exact p-adic coefficient transport, source-preserving Taylor/Hensel update, hypergeometric ODE, and original signed weighted summation. Observer: \\(W_p/p\\bmod p^2\\) and separately the root difference \\(\\delta\\bmod p^3\\). Future operations may inspect signed branches and native Green/Hesse operators; no observer-safe quotient has been proven that removes \\(F\\) or the original middle/high bands. The external one-variable model is not native P000 X6 or H0/B0.

**Actual control read 2026-10-28 12:58 Asia/Hong_Kong:** Site gateway v0.6.11 returned `research_authority_granted=false`, `write_relay_enabled=false`, `static_machine_readonly`. This run's one exact `em_control_continuation` call for the above Task returned `CONTROL_QUOTA`. Existing historical research-lane recovery request `awdawmip/kimi-query-bridge#6575` is only a local session pointer, not a Source winning CLAIM; historical dispatch `#6576` has been recorded FAILED/TimeoutExpired. No new service session, registered activity, winning claim, open/run, native checkpoint or official Result is asserted. Old staging/other conversation ownership is separate.

**Native highest-priority support:** [enterprise-math#1559](https://github.com/awdawmip/enterprise-math/issues/1559) was fetched as OPEN and unassigned in this run; retain PENDING_OWNER / NATIVE_NOT_EXECUTED until real authenticated p=373 same-original-class H0/B0 divided-power evidence, \\([X]U\\bmod139129\\), module rank, semilinear Frobenius direction/eta, odd signed Green/Hesse, original \\(\\kappa\\), \\(\\Delta_p-R_p\\), and raw operator/source receipts are supplied by the authorized executor. This task does not replace that benchmark.

**Smallest unfinished mathematical unit:** use (B)–(C) to construct a genuine across-primes cancellation certificate, e.g. a source-preserving summation/telescoper that produces exact \\(D_1,D_2\\) identities in the two target classes. Do not repeat eight-prime checks as proof. **Mother objective and D25/LIFT/JT2 remain OPEN.** Preserve 2026-10-28 author-side proof/program source as a repository artifact and mirror its exact pin into GLOBAL_KNOWLEDGE_V1; formal Research-Activity registration, review and Source checkpoint remain pending actual authorization. No scheduler, Actions or cron created.
