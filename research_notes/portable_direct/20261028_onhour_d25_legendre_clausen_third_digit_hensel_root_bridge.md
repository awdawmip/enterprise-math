# D25 original 216 — exact third-digit Legendre–Clausen transport and Hensel root

2026-10-28 (Asia/Hong_Kong). AUTHOR-SIDE / ALL-PRIME EXACT ALGEBRAIC TRANSPORT / CONDITIONAL TARGET-CLASS ROOT REDUCTION / EXECUTED 11-PRIME INTEGER CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / NATIVE_NOT_EXECUTED.

Logical Research lane: chatgpt-research-onhour-enterprise-math-20260923; separate from maintenance. Mother: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Source task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 remains unchanged. This document claims no native H0/B0 run, Source Result, formal Lean proof, independent admission, or proof of the original universal LIFT.

## Original object and distinct coefficient sources

For every prime p=6m+1>3, work in Z_(p) and retain the full original weighted cutoff
\[
W_p=\sum_{n=0}^{p-1}(6n+1)\frac{\binom{2n}{n}^{2}\binom{3n}{n}}{216^n}.
\]
Set \(b_j=\binom mj\binom{2m}j2^{-j}\), for 0<=j<=m, and define three *distinct* rational polynomials:
\[
A(z)=\sum_{j=0}^m b_jz^j,\qquad
P^\flat(z)=P_{2m}(\sqrt{1-z/2})={}_2F_1(-m,m+1/2;1;z/2),\qquad
G(z)={}_2F_1(-m,-2m;1-p/2;z/2).
\]
The Legendre square root is only an external coordinate notation: the even P_(2m) makes P^flat an actual rational polynomial. It is NOT an Enterprise native X6 plane or primitive direction. The prior author-side rational identification erratum distinguishes A from P^flat above mod p. We consume, without re-proving, the prior fully signed low/middle/high original cutoff Clausen bridge [onhour 978a262](https://github.com/awdawmip/enterprise-math/blob/978a2622d1f25389f8edd6e7bc1ac8a36be5424d/research_notes/portable_direct/20261028_onhour_d25_exact_clausen_p3_legendre_cutoff_two_port_repair.md):
\[
\boxed{W_p\equiv g^2+12gg'+pD_1+p^2D_2\pmod{p^3}},\quad
g=G(1),\quad g'=G'(1),\quad D_1=J_1-\tfrac32C_1,\quad D_2=J_2-\tfrac18C_2.
\tag{OLD}
\]
The original old jets J1,J2 and correction C1,C2 retain their published definitions and their valuation-band sources. No assumption about the desired p^3 cancellation is used.

## New Theorem A — complete third-digit G-to-Legendre coefficient transport

Let \(H_k^{(r)}=\sum_{u=1}^ku^{-r}\), \(H_k=H_k^{(1)}\), and
\[
M_j=H_{2m}-H_{2m-j},\qquad
M_j^{(2)}=H_{2m}^{(2)}-H_{2m-j}^{(2)}.
\]
Define two separately typed transport polynomials
\[
E(z)=\sum_{j=1}^m b_j(H_j+M_j)z^j,
\quad
F(z)=\sum_{j=1}^m b_j\left(H_j^2+H_j^{(2)}-M_j^2+M_j^{(2)}\right)z^j.
\]
All denominators through 2m are p-units. **For every prime p=6m+1>3, coefficientwise in Z_(p)[z],**
\[
\boxed{G(z)-P^\flat(z)\equiv \frac p2E(z)+\frac{p^2}{8}F(z)\pmod{p^3}.}\tag{A}
\]
**Complete proof:** Direct multiplication of the terminating Pochhammer coefficients yields the *exact rational* product identities
\[
\frac{[z^j]G}{b_j}=\prod_{r=1}^j(1-p/(2r))^{-1},\qquad
\frac{[z^j]P^\flat}{b_j}=\prod_{r=2m-j+1}^{2m}(1-p/(2r)).
\]
Indeed m+1/2=-2m+p/2. Expanding the first finite product to second order gives
\(1+(p/2)H_j+(p^2/8)(H_j^2+H_j^{(2)})\).
Expanding the second gives
\(1-(p/2)M_j+(p^2/8)(M_j^2-M_j^{(2)})\).
Their subtraction, multiplied by b_j, gives every coefficient of (A); j=0 contributes zero. Differentiation preserves coefficientwise congruence. No empirical inference, custom axiom, CM theorem or original LIFT is used. QED.

Write \(a=P^\flat(1)\), \(a'=(P^\flat)'(1)\), \(e=E(1)\), \(e'=E'(1)\), \(f=F(1)\). Then
\[
g-a\equiv pe/2+p^2f/8\pmod{p^3},\quad
g'-a'\equiv pe'/2\pmod{p^2}.\tag{A1}
\]
For the target p≡13,19 mod24, consume the previously accepted *CM0* statement \(a\equiv0\pmod p\) (hence \(g\equiv0\pmod p\)). Put \(q=a/p\), \(\gamma=g/p\). Then
\[
\gamma\equiv q+e/2+pf/8\pmod{p^2}
\]
and direct substitution in (OLD) gives the **original cutoff with separate Legendre and valuation sources**:
\[
\boxed{
W_p/p\equiv
12(q+e/2+pf/8)(a'+pe'/2)
+D_1+p\left[(q+e/2)^2+D_2\right]\pmod{p^2}.}\tag{B}
\]
The original D1,D2 middle/high bands remain; a bare rational Legendre replacement is NOT licensed. The p f/8 term is a genuine third-digit correction.

## New Theorem B — simple CM0 root and third-digit Hensel displacement

Let \(n=2m<p\) and \(x_0=\sqrt2/2\in\mathbb F_{p^2}\) (the quadratic algebra notation covers either splitting behavior). CM0 means \(P_n(x_0)=0\). The derivative cannot vanish: the standard identity
\((1-x^2)P_n'=n(P_{n-1}-xP_n)\)
would then imply \(P_{n-1}(x_0)=0\), since \(x_0^2\ne1\) and n is a p-unit. Descending the Legendre three-term recurrence with every coefficient <p would force \(P_0(x_0)=0\), contradiction. Therefore \((P^\flat)'(1)=-P_n'(x_0)/(4x_0)\ne0\pmod p\), and (A1) shows \(g'=G'(1)\not\equiv0\pmod p\).

Hensel's lemma produces a **unique** \(z_p\in1+p\mathbb Z_p\) with \(G(z_p)=0\); put \(d_p=(z_p-1)/p\in\mathbb Z_p\). For this exact terminating hypergeometric G, its differential equation at z=1 yields
\[
G''(1)=3mG'(1)+2m^2G(1).
\tag{ODE}
\]
Taylor expand the zero at \(1+pd_p\), divide by p, and retain two p-adic digits:
\[
\gamma\equiv-d_pg'-\frac p2d_p^2g''\pmod{p^2},\qquad
g''\equiv3mg'\pmod p.
\]
Substitute into (OLD), using 18m=3p-3, to obtain the exact **Hensel-root reduction of the original third digit**, for both CM0 target classes:
\[
\boxed{W_p/p\equiv D_1-12d_p(g')^2+
p(D_2+4d_p^2(g')^2)\pmod{p^2}.}\tag{C}
\]
The coefficient 4 comes from the ODE and the 18m factor, not from numerical fitting. The next original proof obligation is *exactly*
\[
\boxed{D_1-12d_p(g')^2+p(D_2+4d_p^2(g')^2)\stackrel?\equiv1\pmod{p^2}}
\]
for all p≡13,19 mod24. The global cancellation is OPEN; (C) is a new reduction, not a claim that it is solved.

## Executed integer evidence, p=373 and precision boundary

An independently implemented companion standard-library Python guard executed full original \((6n+1)t_n\) binomial sum for every n<p, independently computed three-factor original J0,J1,J2 and D1,D2, both distinct G/Legendre polynomials, harmonic p^3 transport, a quadratic-algebra Legendre recurrence and derivative, and Newton/Hensel roots under CM0 for 11 primes:
7,13,19,31,37,43,61,67,73,211,373. All assertions passed:
PASS_D25_TRIPLE_PORT_LEGENDRE_CLAUSEN_EXACT_P3 (11 primes).
This is a finite arithmetic implementation check, not universal proof or native Source acceptance.

For p=373, p²=139129, p³=51895117, exact modular readouts:
\[
(a,g)=(44816696,22795149)\ (\bmod p^3),\quad
(a',g')=(85711,118162)\ (\bmod p^2),
\]
\[
(e,e',f)=(110944\bmod p^2,174\bmod p,155\bmod p),\quad
(q,\gamma)=(120152,61113)\ (\bmod p^2),
\]
\[
z_p=10790145\bmod p^3,\quad d_p=28928\bmod p^2,\quad
D_1=130196\bmod p^2,\quad D_2=317\bmod p.
\]
In (A1), \((g-a)\bmod p^3=29873570\) decomposes into the separate port contributions \(pe/2=20691056\) and \(p^2f/8=9182514\). Dropping f changes gamma by 66p modulo p².
In (C), \(D_1-12d_p(g')^2=114139\) and \(p(D_2+4d_p^2(g')^2)=24991\), modulo 139129, sum 1. Independent original W_373=373 mod p³.

**BRC COMPOSE_APPLIED:** retained typed source carrier (p,m,j,b_j,H_j,M_j,coefficient origins,G,P^flat,E,F,d_p,g',D1,D2,original signed n<p cutoff); outputs scalar W_p/p mod p². Permitted operations: exact product, valuation-band differentiation, finite quadratic-algebra Legendre recurrence, Hensel lifting. No compression of E/F or middle/high sources; no inference to P000 native X6 propagation or the original H0/B0 module.

## Source/frontier and exact next action

The research proof and computation are author-side only. Canonical Research session/CLAIM/run and formal Research-Activity publication remain pending actual role authorization. At this run the current Site gateway returned research_authority_granted=false, write_relay_enabled=false and an exact continuation query failed CONTROL_QUOTA. Historical own recovery request awdawmip/kimi-query-bridge#6575 projected a local ACTIVE pointer without Source ownership; old dispatch #6576 concluded FAILED/TimeoutExpired. No new native CLAIM/open/dispatch, no role borrowing or replay of ambiguous request. Three old neutral staging sources remain separate.

Scientific frontier: consume proven previous Cauchy second digit and original Clausen/three-band jet; use (C) next to seek an all-target-class telescoping identity for D1, D2 and the Hensel root/derivative, or an exact counterexample with all original source ports retained. The **higher-priority native evidence** is still awdawmip/enterprise-math#1559 OPEN/PENDING_OWNER: authorized executor must actually run original p=373 H0/B0 divided-power benchmark yielding [X]U mod139129, native rank, semilinear Frobenius direction/eta, signed Green/Hesse, original kappa, Delta_p−R_p, full raw reproducible data. No standard scalar replacement meets that gate. The frozen scientific source pin and P000 are unchanged; this note creates no scheduler, Action or hosted cron.
