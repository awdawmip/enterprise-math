# D25 SECOND-DIGIT-LIFT: exact three-valuation-port certificate for the actual frozen scalar

2026-10-24. Author: ordinary TASK_RESEARCH logical lane chatgpt-research-onhour-enterprise-math-20260923. Status: UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SYNC_DEBT. This research note is an author artifact, not a native claim, run, Source checkpoint, admitted Result, native benchmark or independent review.

Frozen mother task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; taskbook blob 53a3ef039325534e3715add837f0eee332289984; immutable scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3.

## 1. Exact frozen problem, not an auxiliary endpoint

For primes p congruent to 13 or 19 mod 24, the frozen accepted scalar interface is

\[
B_0=1,\qquad B_{k+1}/B_k=\frac{(6k+1)(3k+1)}{36(k+1)^2},
\quad g=\sum_{k=0}^{p-1} B_k,\quad h=\sum_{k=0}^{p-1}(12k+1)B_k,
\quad G_p=g/p.
\]

The live target is precisely
\[
\Delta_p:=\frac{G_ph-1}{p}\stackrel{?}{\equiv}R_p\pmod p.
\]
The frozen parent provides CM0, SIMPLE and accepted UR/JT0 (hence p divides g and p divides G_p h-1). Unlike prior author-side hypergeometric S_m certificates, THIS note operates on the original frozen g, h and Delta_p directly. No unsourced bridge from S_m to Delta_p is presumed; R_p remains the pinned parent target and is not invented here.

## 2. Theorem: exact three-block valuation and jet laws

Set p=6m+1 and w_k=12k+1. For 0<=k<=m let

\[
b_k=\frac{(-m)_k(-2m)_k}{2^k(k!)^2},\qquad
D_k=\frac16\sum_{j<k}\frac1{j-m}+\frac13\sum_{j<k}\frac1{j-2m},
\]
\[
E_k=\frac1{36}\sum_{j<k}\frac1{(j-m)^2}+\frac19\sum_{j<k}\frac1{(j-2m)^2}.
\]

For m+1<=k<=2m let

\[
u_k=\frac{(-1)^m m!(k-m-1)!(-2m)_k}{6\,2^k(k!)^2},
\quad
P_k=\frac16\sum_{\substack{j<k\\j\ne m}}\frac1{j-m}
+\frac13\sum_{j<k}\frac1{j-2m}.
\]

For 2m+1<=k<=p-1 let

\[
v_k=\frac{(-1)^m m!(k-m-1)!(2m)!(k-2m-1)!}{18\,2^k(k!)^2}.
\]

All displayed denominators are p-units in their stated ranges. For every target prime, the following are exact termwise congruences in Z_(p):

\[
\boxed{
\begin{array}{ll}
B_k\equiv b_k[1+pD_k+\frac{p^2}{2}(D_k^2-E_k)]\pmod{p^3},&0\le k\le m,\\
B_k\equiv p u_k(1+pP_k)\pmod{p^3},&m+1\le k\le2m,\\
B_k\equiv p^2 v_k\pmod{p^3},&2m+1\le k\le p-1.
\end{array}}
\]

Proof. In Q, the original term equals

\[
B_k=\frac{(-m+p/6)_k(-2m+p/3)_k}{2^k(k!)^2}.
\]

For k<=m all factors are p-units and finite logarithmic Taylor expansion produces D and E. For m<k<=2m isolate the one factor p/6 at j=m and expand the remaining units one further digit; this gives u and P. For k>2m isolate additionally the factor p/3 at j=2m, giving v at zero derivative order. The only numerator p-zeros within 0<=k<p are j=m and j=2m, and k! is a p-unit. This proves the three congruences and exact valuations 0,1,2, respectively, without inverting p. QED.

## 3. Direct formula for the actual divided LIFT residual

Define eight provenance-preserving finite sums:

\[
L_0=\sum_{k=0}^{m}b_k,\quad L_1=\sum_{k=0}^{m}b_kD_k,\quad
L_2=\frac12\sum_{k=0}^{m}b_k(D_k^2-E_k),
\]
\[
U_1=\sum_{k=m+1}^{2m}u_k,\quad
U_2=\sum_{k=m+1}^{2m}u_kP_k,\quad
V_2=\sum_{k=2m+1}^{p-1}v_k,
\]
\[
H_0=\sum_{k=0}^{m}w_kb_k,\quad
H_1=\sum_{k=0}^{m}w_kb_kD_k+
\sum_{k=m+1}^{2m}w_ku_k.
\]

The accepted frozen terminating-Jacobi CM0 law identifies L_0 as the special H_m(1/2) and proves p divides L_0 for both prescribed residue classes. Consequently

\[
\Gamma_0=L_0/p+L_1+U_1,\qquad
\Gamma_1=L_2+U_2+V_2
\]
are p-integral, with

\[
G_p\equiv\Gamma_0+p\Gamma_1\pmod{p^2},
\qquad h\equiv H_0+pH_1\pmod{p^2}.
\]

The independently accepted UR/JT0 yields Gamma_0 H_0=1 (mod p). Thus all divisions below are legitimate and

\[
\boxed{
\Delta_p\equiv
\frac{\Gamma_0H_0-1}{p}
+(L_2+U_2)H_0
+\underbrace{V_2H_0}_{\text{double-zero upper port}}
+\Gamma_0H_1\pmod p.
}\tag{DIRECT-LIFT-3PORT}
\]

This is a rigorous equivalence, for all target primes, between the original frozen scalar and a typed finite jet certificate. It lowers the upper branches' required derivative precision: two jets in the low block, one in the middle, zero in the upper block, but still retains the upper block's p-adic provenance. The remaining hard task is to compare this exact RHS to the frozen R_p (or exhibit a genuine direct counterexample). No JT2/LIFT completion is claimed.

## 4. BRC observer sufficiency and concrete information-loss witness

Carrier: all source-labeled k terms and their valuations/units; separate original j=m and j=2m numerator zero ports; low first/second jets, middle first jet, and upper zeroth jet. Allowed future operations: divide g by p, multiply h, divide the unit defect by p. The observer is Delta_p mod p, *not* g mod p^2, nor any positive-weight total. The upper B_k have valuation two and disappear from g mod p^2, but after the specified division by p their contribution V_2 H_0 survives in Delta_p mod p.

An exact arithmetic witness: for p=19, m=3, the original source recurrence gives Delta_19=12 mod19, and the displayed RHS decomposes into (16, 5, 6, 4) mod19 (base, low+middle second jets, upper double-zero port, h first jet). Omitting the upper port changes the computed output to 6, an actual incorrect value. At p=211, Delta_211=119 and upper port=110, omission leaves 9. At p=13, the upper port=9 is necessary to cancel the other contributions and obtain Delta_13=0. This is an exact BRC noncollapse witness. These scalar finite-field calculations are typed mathematical readouts, not native Heartbeat X6 spatial dynamics or a claim modifying P000's locked 6D Cell space plus separately typed time.

## 5. Actual arithmetic evidence, scope and continuation

Local standalone companion script d25_lift_direct_three_port_jet_check.py was executed for all 77 target primes p<=2000. It computes the original p-1 term hypergeometric recurrence modulo p^3, and independently calculates the three zero-factor jet branches, comparing each original block mod p^3, G_p and h mod p^2, and Delta_p mod p. All checks passed. Double-zero port is nonzero in 76 of the 77 cases; p=157 is the unique zero in this *finite* tested domain. Independent exact Fraction calculations for p=13,19,37 verify Delta values 0,12,11. Finite checks are falsification/regression, not universal proof or native benchmark; the formal algebra above is the proof of the decomposition, conditional only on already accepted parent CM0/UR when extracting the divided residual.

Next mathematics: obtain the exact parent-pinned R_p expression from its authenticated scalar/CM-divided-power source and prove or refute DIRECT-LIFT-3PORT = R_p (mod p) across both residue classes, keeping the upper port and class labels. This exact mathematical requirement is not satisfied by earlier S_m scans or extra WZ auxiliaries. Original unchanged native benchmark, formal Source publication and independent review remain separate unperformed obligations. Current Sites Gateway 0.6.11 reports research_authority_granted=false / executor_binding_configured=false; exact D25 continuation returned CONTROL_QUOTA; existing recovery issue awdawmip/enterprise-math#1539 remains OPEN. No Source session/CLAIM/open/run/checkpoint/Result or Driver review is asserted; no original ambiguous mutation was replayed, and old unrelated staging remains separate. The original scheduler, notification behavior, scientific pin and ACTIVE protected worldview are unchanged.
