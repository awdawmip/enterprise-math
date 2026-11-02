# D25: simple CM root, Hensel–Teichmüller residual and source-faithful Cauchy lift

Date: 2026-11-02 (+08). Author-side TASK_RESEARCH evidence, UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING. Logical Research lane: chatgpt-research-hourly-enterprise-math-20260923 (separate from maintenance). Source Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7; frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. No native session write, CLAIM, OPEN, Source checkpoint, Result or review is claimed.

Prior reusable sources: 20261102_hourly_r11_d25_clausen_forced_pf_jet_closure.md (Gauss polynomial, CM0 and four-port forced Picard–Fuchs) and 20261102_hourly_r11_d25_cauchy_second_carry_p3.md (true Cauchy omitted triangle, Wilson reflection, K0/K1). Previously proved R_p identities remain credited to prior research. The mother D25 Delta_p-R_p congruence remains open.

## Unit A: theorem (simple CM root and exact first lift)

For every prime p=6r+1>=7 define

\[
P_r(z)=\sum_{k=0}^{r}\binom{r}{k}\binom{2r}{k}z^k
={}_2F_1(-r,-2r;1;z),\quad z_0=\tfrac12,\quad \theta=z\partial_z.
\]

**A1.** Every root of P_r over F_p outside {0,1} is simple. In particular, if the earlier CM0 condition P_r(z_0)=0 mod p holds then J_1=(\theta P_r)(z_0) is a p-unit.

*Proof.* The exact terminating Gauss equation is
\[
z(1-z)P_r''+[1-(1-3r)z]P_r'-2r^2P_r=0.
\]
At any root a in F_p other than 0 or 1, a hypothetical multiplicity d>=2 has 2<=d<=r<p. Its lowest nonvanishing coefficient in the ODE is a(1-a)d(d-1)c_d (z-a)^{d-2}; it is nonzero, while the other terms start at higher order. This contradiction proves simplicity. Since z_0 is a unit, J_1=z_0P'_r(z_0) is nonzero. QED.

**A2.** Under the same CM0 hypothesis, the p-adic root z_CM of P_r with z_CM=z_0 mod p exists and is unique. Put
\[
c_p=P_r(z_0)/p\bmod p,\quad j_p=J_1\bmod p,\quad
t_{CM}=-c_p/(2j_p),\quad q_p(2)=(2^{p-1}-1)/p,\quad
t_T=-q_p(2)/2\bmod p.
\]
Let z_T be the Teichmüller lift of z_0 mod p, so z_T=z_0^p mod p². Then
\[
\boxed{z_{CM}=z_0+pt_{CM},\quad z_T=z_0+pt_T\pmod{p^2};\qquad
P_r(z_T)/p=2j_p(t_T-t_{CM})\pmod p.}\tag{A}
\]
*Proof.* Taylor's formula P_r(z_0+pt)=P_r(z_0)+ptP'_r(z_0) mod p² and the unit derivative solve uniquely for t_CM. Since (1/2)^{p-1}=2^{1-p}=1-pq_p(2) mod p², the Teich shift is t_T. Substitute it into the same Taylor expansion. QED.

The root of the Gauss polynomial and the Teichmüller lift are two explicitly different coordinate conventions. The exact residue in (A) is the required provenance correction when comparing their observations.

## Unit B: theorem (two original Cauchy carry derivatives and higher-digit transport)

Let
\[
a_m=\frac{(1/2)_m(1/3)_m(2/3)_m}{(m!)^3},\quad
A_m(z)=a_mz^m,\quad B_j=\binom{2j}{j}8^{-j}\quad(0\le m,j<p).
\]
At z_0=1/2, A_m(z_0)=binom(2m,m)^2 binom(3m,m)/216^m, the original 216 Cauchy source. Retain the ordered omitted triangular region and both observers:
\[
\mathcal C_i(z)=\sum_{\substack{0\le m,j<p\\m+j\ge p}}(m+j)^i A_m(z)B_j,\qquad i=0,1.
\]
The notation C_i distinguishes these Cauchy moments from the Gauss jet J_n. Over F_p define for 1<=s<=2r
\[
u_s=-1/(4sB_s),\quad U_m=\sum_{s=1}^m u_s,\quad
V_m=\sum_{s=1}^m(m-s)u_s,
\]
\[
K_0(z)=\sum_{m=1}^{2r} a_mz^mU_m,\quad
K_1(z)=\sum_{m=1}^{2r} a_mz^mV_m,\quad
\boxed{L_i=(\theta K_i)(z_0).}
\]

**B.** For every p=6r+1>=7 (no CM hypothesis) and i=0,1, the exact polynomial C_i(z) is coefficientwise divisible by p in Z_(p)[z], and
\[
\boxed{\mathcal C_i(z)/p=K_i(z)\pmod p.}\tag{B1}
\]
For any two lifts z_a=z_0+pt_a and z_b=z_0+pt_b,
\[
\boxed{\frac{\mathcal C_i(z_a)-\mathcal C_i(z_b)}{p^2}
=2(t_a-t_b)L_i\pmod p.}\tag{B2}
\]
Thus, under CM0, the true original Cauchy omitted-triangle vector satisfies
\[
\boxed{(\mathcal C_0,\mathcal C_1)(z_T)-(\mathcal C_0,\mathcal C_1)(z_{CM})
=2p^2(t_T-t_{CM})(L_0,L_1)\pmod{p^3}.}\tag{B3}
\]

*Proof.* The p-valuations of a_m on [0,2r], [2r+1,3r], [3r+1,4r], [4r+1,p-1] are 0,1,2,3; those of B_j are 0 through 3r and 1 afterward. Every m+j>=p term is p-divisible. The terms of valuation exactly one have m<=2r, j=p-s with 1<=s<=m; by the previously proved Wilson reflection B_{p-s}/p=-1/(4sB_s)=u_s mod p. In the second observer, m+j=m+p-s becomes m-s mod p. This proves (B1) as an identity of polynomials, not just point values. Since H_i=C_i/p has p-integral coefficients, Taylor expand H_i(z_0+pt) modulo p²; H'_i(z_0)=K'_i(z_0)=2L_i mod p. Multiplication by p proves (B2), and Theorem A2 gives (B3). QED.

BRC preserved carrier = original ordered (m,j) cutoff, valuation layers and weights; observer = (C0,C1) at the specified p-adic precision; repair coordinates = slope ports (L0,L1) and actual CM-vs-Teich shift. No native X6 or fixed H0/B0 experiment is asserted.

## Exact computational evidence (finite)

Companion standard-library integer checker separately evaluates P_r using its binomial recurrence, K/L from original low-index A_m(1/2),B_s, and the **complete original omitted triangular sum** via independent suffix sums mod p³. A second calculation reconstructs the original A_m and B_j from integer binomial coefficients.

For all **312** primes p<=10000 with p mod24 in {13,19}, the CM0, J1 unit, Hensel lift, Teich identity and (A) checks passed. For this finite set, the earlier K0=0, K1=-1/2 conjectures held, and a **new** candidate L0=-1 mod p held. These three K/L laws are finite exact observations, NOT universal theorems. All 312 tested CM/Teich lifts differed modulo p² (finite observation).

For all **107** target primes p<=3000, independently recomputed original C0/C1 at both lifts modulo p³ satisfied (B3). For p=13,19,37,373, integer-binomial and hypergeometric-recurrence constructions agreed at both lifts (eight comparisons).

| p | J1 | t_CM | t_T | L0 | L1 | P_r(z_T)/p | Delta C0/p² | Delta C1/p² |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
|13|7|6|5|12|11|12|2|4|
|19|1|16|8|18|11|3|16|14|
|37|24|25|18|36|22|34|14|25|
|373|294|276|271|372|170|44|**10**|**165**|
|1171|544|789|1022|1170|1138|568|705|1016|

For p=373, t_T-t_CM=-5 mod373, L0=-1 and L1=170, yielding the genuinely original Cauchy second-digit vector (10,165). This is a finite original-source certificate, not a surrogate for native fixed H0/B0 [X]U mod p².

**Next smallest scientific unit:** find a verifiable finite-field/creative-telescoping certificate or counterexample for the *new* universal conjecture L0=-1 under CM0, jointly with earlier open K0=0 and K1=-1/2. Test candidate transformations also on non-CM split primes to discriminate source-specific from artificial identities. If proved, the first component of (B3) becomes -2(t_T-t_CM); assess whether both slope coordinates are needed in subsequent signed 216/2304 normalization.

Control/recovery: authenticated Gateway 0.6.11 reports CODE_REVIEW_REQUIRED / UPSTREAM_CODE_REVIEW_REQUIRED, research_authority_granted=false, executor_binding_configured=false, active_jobs=5/5. Read-only recovery kimi-query-bridge#6637 succeeded historically with service session MCP-06f7ad61a8d841d9ba1ba1ef4d088d94, with no pending work or run; exact continuation #6638 terminal FAILED and was not replayed. Existing support enterprise-math#1558 owns repair, #1559 owns the separate native benchmark. No ownership claim or Source durable checkpoint follows from this author-side Git publication.
