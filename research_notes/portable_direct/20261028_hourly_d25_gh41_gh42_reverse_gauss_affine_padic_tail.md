# D25/LIFT GH-41–GH-42: reverse Gauss affine boundary and first p-adic tail lift

Date: 2026-10-28. TASK_RESEARCH author-side mathematical proof, exact modular computation. UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. No Source CLAIM, authorized run, checkpoint, native X6 experiment, independent review or mathematical admission is asserted.

Parent: ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION (OPEN). Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication TP2-B6F4FC938FF94941C1B7. Frozen science Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 remains unchanged.

Source dependencies: GH-38/GH-39 rational Clausen coefficient identity and full retained high tail; GH-40 reverse-index mod-p coefficient identity. These are author-side, not canonically reviewed. Our new results do not prove the open GH-3 vanishing or substitute for Hasse W/S ports.

## Domain and exact definitions

Let p=4d+3>=7 be prime, d=(p-3)/4, and work in the local ring Z_(p). All denominators below are p-units in the indicated range 0<=r<d. Define

\[
a_0=c_0=\beta_0=1,\quad
\frac{a_{r+1}}{a_r}=\frac{(8r+1)^2}{16(4r+3)(r+1)},\quad
\frac{c_{r+1}}{c_r}=\frac{(4r+1)^3}{(4r+2)(4r+3)(4r+4)},\quad
\frac{\beta_{r+1}}{\beta_r}=\frac{16(r+1)(4r+3)}{(8r+13)^2}.
\]

Put \(B_d(z)=\sum_{r=0}^d a_rz^r\), \(Q_d=B_d+16zB_d'\), \(T_d(z)=\sum_{r=0}^d(8r+1)c_rz^r\), \(V_d(u)=\sum_{r=0}^d\beta_ru^r\), \(D=u\,d/du\). Here \(B_d\) is the auxiliary Gauss polynomial and is not the original Hasse B0 or GH-15 Laurent B0.

Unit check: \(4r+3<p\), \(r+1<p\), and \(13\le8r+13\le 2p-1\); equality \(8r+13=p\) would force p=5 mod 8, impossible for p=3 mod 4. The forward numerator and reverse numerator are also p-units. Hence \(a_d,\beta_d\) are p-adic units.

## GH-41: exact affine reverse differential boundary (PROVED)

Set \(\mathcal A=u(D+\tfrac34)(D+1)-(D+\tfrac58)^2\). The rational polynomial \(V_d\) satisfies

\[
\boxed{\mathcal A V_d(u)=-\frac{25}{64}+\frac{p(d+1)}4\,\beta_du^{d+1}.}\tag{41.1}
\]

Proof: the coefficient at \(u^0\) is \(-25/64\); for 1<=n<=d it is \(n(n-\tfrac14)\beta_{n-1}-(n+\tfrac58)^2\beta_n=0\) by the exact recurrence. The coefficient at n=d+1 is \((d+1)(d+\tfrac34)\beta_d=p(d+1)\beta_d/4\). Because \(d+1\) and \(\beta_d\) are p-units, this upper boundary has p-adic valuation exactly one. QED.

Further let
\[
\mathcal L_3=D(D+\tfrac58)^2-u(D+1)^2(D+\tfrac34)=-D\mathcal A.
\]
Then
\[
\boxed{\mathcal L_3 V_d=-\frac{p(d+1)^2}{4}\beta_du^{d+1}.}\tag{41.2}
\]

Thus the reverse polynomial obeys an *inhomogeneous second-order* equation mod p (constant source -25/64), and an exactly homogeneous third-order equation mod p only because differentiation kills the constant. The rank-three equation retains a nonzero valuation-one resonance mod p^2. This is distinct from GH-38's forward Gauss boundary and cannot be erased by replacing a signed source with a homogeneous approximation.

## GH-42: source-faithful p-adic reversal and full high-tail jet (PROVED)

For 0<=j<d write \(A_j=4j+4,\ B_j=4j+3,\ C_j=8j+13\). Define \(H_0=0\) and
\[
H_r=\sum_{j=0}^{r-1}\left(\frac4{C_j}-\frac1{A_j}-\frac1{B_j}\right)\pmod p.
\]

The exact rational reversal and first p-adic jet are
\[
\boxed{
a_{d-r}=a_d\beta_r\prod_{j=0}^{r-1}
\frac{(1-p/A_j)(1-p/B_j)}{(1-2p/C_j)^2}
\equiv a_d\beta_r(1+pH_r)\pmod{p^2},
\quad 0\le r\le d.
}\tag{42.1}
\]

Proof: reverse the actual forward Gauss ratio:
\[
\frac{a_{d-j-1}}{a_{d-j}}
=\frac{16(4(d-j-1)+3)(d-j)}{(8(d-j-1)+1)^2}
=\frac{4(p-A_j)(p-B_j)}{(2p-C_j)^2}.
\]
Divide by the reverse ratio \(\beta_{j+1}/\beta_j=4A_jB_j/C_j^2\), telescope the resulting exact rational factors, and expand the p-unit denominators to first order modulo p^2. QED.

Keep source labels (i,j) with i+j=r, and for 0<=r<d define
\[
v_r=\sum_{i+j=r}\beta_i\beta_j,\qquad
j_r=\sum_{i+j=r}\beta_i\beta_j(H_i+H_j).
\]
The three distinct inverse-point observers are
\[
M(u)=\sum_{r=0}^{d-1}v_ru^r,\quad
W(u)=\sum_{r=0}^{d-1}(8r+11)v_ru^r,\quad
J(u)=\sum_{r=0}^{d-1}(8r+11)j_ru^r.
\]
Here W is exactly GH-40's W_{d-1}, but M and J cannot be deduced from its one scalar value.

Define the genuine high tail with **all** ordered multiplicities retained:
\[
E_d(z)=\sum_{n=d+1}^{2d}(8n+1)[x^n]B_d(x)^2 z^n.
\]
Set \(u=1/9\) and \(q_p(3)=(3^{p-1}-1)/p\in\mathbb Z\). Then
\[
\boxed{
E_d(9)\equiv\frac{a_d^2}{9}
[-W(u)+p(4M(u)-J(u)-q_p(3)W(u))]\pmod{p^2}.
}\tag{42.2}
\]
Since the rational Clausen formula gives **exactly** \(T_d(z)=B_d(z)Q_d(z)-E_d(z)\) (the tail is never discarded), it follows that
\[
\boxed{
T_d(9)\equiv B_d(9)Q_d(9)+\frac{a_d^2}{9}
[W(u)+p(q_p(3)W(u)-4M(u)+J(u))]\pmod{p^2}.
}\tag{42.3}
\]

Proof: the reverse pair bijection (i,j)->(d-i,d-j), restricted to n=2d-r, gives
\[
[x^{2d-r}]B_d(x)^2\equiv a_d^2(v_r+p j_r)\pmod{p^2}.
\]
Retain the **integer** weight \(8(2d-r)+1=4p-(8r+11)\). Since \(9^{2d}=3^{p-1}/9=(1+pq_p(3))/9\pmod{p^2}\), substituting and grouping the three independent first-jet sources proves (42.2). The complete rational Clausen tail identity then proves (42.3). QED.

The terms qW, -4M and J encode different operations (inverse-point scale, literal weight lift, and pairwise reverse-coefficient deformation). For p=19 each survives separately modulo p: qW=14, -4M=8, J=15. Merely squaring/averaging the signed contributions and keeping only W erases essential future information.

## Executed evidence and boundaries

Companion Python standard-library checker:
research_notes/portable_direct/20261028_hourly_d25_gh41_gh42_reverse_gauss_padic_check.py

Actual author-side local run: all 154 primes 7<=p<2000 with p=3 mod4 passed (i) coefficientwise affine source and its valuation-one boundary, (ii) every reversed coefficient including H, (iii) every high-tail ordered-pair sum against W/M/J/q, and (iv) original T against (42.3), all in exact modular arithmetic mod p^2. Selected certificates (p; T mod p^2; E mod p^2; W,M,J,q mod p):
(19;342;69;5,17,15,18), (43;1634;372;11,7,5,2), (67;201;200;6,36,39,15).
These are **finite tests** supporting the algebra, not independent review, formal proof checking or project admission.

BRC COMPOSE_APPLIED: exact ordered-pair carrier, signed p-adic weight, reverse-index map, truncation rank, source-provenance and derivative/moment observers are preserved. The correction J witnesses why a total-only unsigned quotient is not sufficient for the future p^2 observer. These auxiliary arithmetic coordinates are not native X6 cell identities, a P000 replacement, the original six Hasse ports, or native eta/kappa evidence.

**Next scientific action:** find an independently sourced special-value or nonlocal WZ certificate for W(1/9) relative to B(9)Q(9), not another reversal of the same convolution; alternatively relate the new p-adic correction qW-4M+J to the separately existing GH-20/GH-21 second-digit sources without merging distinct ports. GH-3 all-prime vanishing, original W/S sources, R23/R36 Green, [X]U mod p^2, native p=373, and Driver review remain open. This note creates no new scheduler, claim, run or Source checkpoint.
