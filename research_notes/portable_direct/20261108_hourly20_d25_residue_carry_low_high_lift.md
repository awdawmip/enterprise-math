# D25 — Residue-carry first-digit lift and linear Hasse-source normal form

Date: 2026-11-08 Asia/Hong_Kong. Lane: chatgpt-research-hourly-enterprise-math-20260923 (not the maintenance lane). Author-side TASK_RESEARCH / REGISTER_PENDING. Mathematical status: PROVED FINITE ALGEBRA, exact finite-ring tests PASS; UNREVIEWED / NOT_ADMITTED.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; taskbook blob 53a3ef039325534e3715add837f0eee332289984. Frozen scientific pin c47e13e4aba0e006366f989d6334d443f6333ae3. D24 UR/JT0 (RR-AC9B3BA5BD277CE043F5) is accepted input.

**Consumed, not claimed anew:** the on-hour 20261108 mixed-band Clausen second-reflection theorem and its normalized K-H middle port, along with the original reflected R source and earlier finite Green/Cartier work. The new contribution is an explicit first p-digit for the low/high source *without high-index b-series* and its linear-time Hasse-prefix contraction, expressed in residue-carry/observer coordinates.

## Exact objects and retained sources

Let p=6m+1 be prime, p>=7. Work over Z_(p); all denominators below are units in the stated ranges. Set

\[
b_k=\frac{(1/6)_k(1/3)_k}{2^k(k!)^2}\ (0\le k<p),\qquad
q_i=2^{-i}{m\choose i}{2m\choose i}\ (0\le i\le m).
\]

Let c_1=1/10, c_{a+1}/c_a=36a^2/((6a+5)(3a+2)) for 1<=a<2m. Define w(i,a)=1+6(i-a) and the *original*, independently defined reflected lift

\[
\mathcal R_m=2\sum_{i=1}^{m}q_i\sum_{a=1}^{i}w(i,a)c_a.
\]

This is the original R_p mod p, not a value fitted from Delta. Retain the full source fibers (i,a) and (j,residue,carry), including signs and integer quotients; the scalar sums below are declared observers for this finite second-digit task, not a global collapse of BRC or X6 states.

For j in {0,...,p-2} excluding m, uniquely write 6j+1=p e_j+r_j with 1<=r_j<p. For j excluding 2m, write 3j+1=p f_j+s_j with 1<=s_j<p. Put

\[
U_6=\sum_{\substack{0\le j\le p-2\\j\ne m}}\frac{e_j}{r_j},
\quad
U_3=\sum_{\substack{0\le j\le p-2\\j\ne2m}}\frac{f_j}{s_j},
\quad
q_p(36)=\frac{36^{p-1}-1}{p}\pmod p,
\]

\[
\boxed{\beta_p=\frac7{10}+U_6+U_3-q_p(36)\pmod p.}\tag{CARRY}
\]

This is a literal quotient/residue reconstruction of the factors, not a heuristic fit. Define finite sums

\[
L_i=\sum_{j=0}^{i-1}\left(\frac1{6j+1}+\frac1{3j+1}\right),\quad 0\le i\le m,\quad L_0=0,
\]

\[
T_a=\sum_{r=1}^{a-1}\left(-\frac2r+\frac6{6r+5}+\frac3{3r+2}\right),\quad1\le a\le2m,\quad T_1=0.
\]

## Theorem 1 — complete first-digit lifts of both reflected ports

For every prime p=6m+1>=7,

\[
\boxed{\frac{b_i-q_i}{p}\equiv q_iL_i\pmod p\quad(0\le i\le m),}\tag{LOW}
\]

\[
\boxed{\frac{b_{p-a}/p^2-c_a}{p}\equiv c_a(\beta_p+T_a)\pmod p
\quad(1\le a\le2m).}\tag{HIGH}
\]

Each division precedes reduction and is p-integral. The high-port base case is

\[
\boxed{\frac{10b_{p-1}/p^2-1}{p}\equiv\beta_p\pmod p.}\tag{BASE-DIGIT}
\]

**Proof.** Exactly over Z_(p), the binomial expression for q_i gives
\(q_i=b_i\prod_{j<i}(1-p/(6j+1))(1-p/(3j+1))\). For i<=m all factors are p-units, and first-order multiplication proves (LOW).

For (BASE-DIGIT), remove the unique p factors 6m+1=p and 3(2m)+1=p from b_(p-1). The nonzero residues of 6j+1, j=0..p-2 excluding m, are precisely 1..p-1 with p-5 omitted; for 3j+1 excluding 2m they are precisely 1..p-1 with p-2 omitted. Thus the following is an **exact rational identity**, before reduction:

\[
\frac{b_{p-1}}{p^2}
=\frac{1}{(p-5)(p-2)36^{p-1}}
\prod_{j\ne m}\left(1+\frac{pe_j}{r_j}\right)
\prod_{j\ne2m}\left(1+\frac{pf_j}{s_j}\right),
\]

with both products over 0<=j<=p-2. Use
\(10/[(p-5)(p-2)]\equiv1+7p/10\pmod{p^2}\) and
\(36^{-(p-1)}\equiv1-pq_p(36)\pmod{p^2}\).
Their first-order product gives (CARRY) and (BASE-DIGIT).

Finally put B_a=b_(p-a)/p^2. The exact backward ratio is
\[
\frac{B_{a+1}}{B_a}=
\frac{36(p-a)^2}{(6p-6a-5)(3p-3a-2)}.
\]
Its quotient by \(c_{a+1}/c_a\) is
\(1+p[-2/a+6/(6a+5)+3/(3a+2)]\pmod{p^2}\).
Induction from a=1 proves (HIGH). QED.

## Theorem 2 — separate global and local low/high contributions

The on-hour source decomposition gives
\[
S_{\rm low}=2\sum_{i=1}^{m}\sum_{a=1}^{i}
[w(i,a)(d_ic_a+q_iv_a)+6q_ic_a]\pmod p,
\]
where \(d_i=(b_i-q_i)/p\), \(v_a=(b_{p-a}/p^2-c_a)/p\) modulo p. Using Theorem 1,

\[
\boxed{
S_{\rm low}=\beta_pR_p+
2\sum_{i=1}^{m}q_i\sum_{a=1}^{i}
c_a\{w(i,a)(L_i+T_a)+6\}\pmod p.
}\tag{LOW-SOURCE}
\]

Thus the global Fermat/carry normalization multiplies the *original* reflected R_p, while the local portion retains individual low/high sources. This is a law for the stated second-digit scalar observer; it does not erase the underlying labeled fibers.

The local portion admits an O(m)-arithmetic finite-field contraction. Write
\[
A_i=\sum_{a\le i}c_a,\quad B_i=\sum_{a\le i}ac_a,\quad
A_i^T=\sum_{a\le i}c_aT_a,\quad B_i^T=\sum_{a\le i}ac_aT_a,
\]
\[
H_i=(1+6i)A_i-6B_i,\qquad H_i^T=(1+6i)A_i^T-6B_i^T.
\]
Then
\[
\boxed{S_{\rm low}=\beta_pR_p+
2\sum_{i=1}^{m}q_i(L_iH_i+H_i^T+6A_i)\pmod p.}\tag{LINEAR-PORT}
\]
The proof is direct expansion of w(i,a)=1+6i-6a, so all four prefix moments are explicitly sufficient for this **declared observer**. No signed (i,a) information is asserted redundant for subsequent unscoped operations.

**Combination with the independent on-hour middle-band theorem (not claimed here):** let K_1=1 and K_(r+1)/K_r=3r(6r+1)/(6r+5)^2, r<m. Then the known \(S_{\rm mid}=q_m/25\sum_{r=1}^mK_rH_{m+r}\) yields the complete normalized correction
\[
\boxed{
\frac{\mathcal Q_p/p^2-\mathcal R_m}{p}\equiv
\beta_pR_p+
2\sum_{i=1}^{m}q_i(L_iH_i+H_i^T+6A_i)
+\frac{q_m}{25}\sum_{r=1}^{m}K_rH_{m+r}
\pmod p.
}\tag{FULL-PORT}
\]
Here \(\mathcal Q_p=\sum_{i+j\ge p}(6(i+j)+1)b_ib_j\); its first-digit alignment and valuation partition were proved in the on-hour work. The numerator is p-divisible **after the indicated p^2 division**. The new first-two terms are established in this note; the third is a reused, independently sourced theorem.

## Independent finite-ring verification

Executable: research_notes/portable_direct/d25_reflection_carry_firstdigit_20261108.py. Direct arithmetic in Z/(p^4), using modular inverses only for p-units and exact integer quotients; no floating point. For **all 148 primes p<=2000 with p=1 mod 6** (including all 77 frozen residue-class primes p=13,19 mod24), the checker independently tests: (BASE-DIGIT), all LOW indices, all HIGH indices through 2m, the source-resolved double sum, four-prefix contraction, independently reconstructed middle band, and the entire Clausen cutoff via suffix zeroth/first moments. All PASS.

Representative (p, beta, R modp, S_low, S_local, S_mid, S_total):
- (13,10,0,9,9,2,11)
- (19,10,12,18,12,2,1)
- (43,12,15,13,5,5,18)
- (67,55,21,33,17,15,48)
- (373,17,196,252,277,157,36)
- (997,798,626,647,596,550,200)

Example p=373: \(\beta R=17\cdot196=348\bmod373\), so \(348+277=252=S_{\rm low}\), and \(252+157=36\). This agrees with the independent full-cutoff quotient.

## Frontier, authorization and next action

This produces an explicit *BRC-style typed residue/quotient carrier* (j,r_j,e_j) for a finite arithmetic observable and a provably observer-safe prefix-moment factorization at the specified p-digit. It does **not** claim a new standalone Enterprise BRC theorem family or native X6 arithmetic experiment.

Mother LIFT: \(\Delta_p-R_p\equiv0\pmod p\) for p=13 or 19 mod24, still OPEN. The on-hour NEXT-DIGIT and this FULL-PORT give a new precise task: compare the local low/high prefix correction, normalized middle K-H port and the Cartier 4m divided-boundary \(\mathcal C_m\) against the original Gauss \((ZH_0-1)/p,SH_0,ZH_1,\Phi_{xx}\) sources without fitted second-digit coefficients. Start at p=19,373; then seek an exact Fricke/Cartier signed intertwiner.

Source-native Researcher status: not verified. Site CONFIGURED_NOT_LIVE_VERIFIED; backend read returned BACKEND_IDENTITY_OR_VERSION_MISMATCH / UPSTREAM_STATUS_TOOL_ERROR / STATUS_DATABASE_UNAVAILABLE, operation_sent=false. Preserve original requests em-h20-20261106-1324-d25-task-r13 and em-h20-20261106-1324-d25-cont-r13, unknown old session/claim/run/staging, issue #1558. No native CLAIM, OPEN, checkpoint, freeze, review or p373 native experiment is asserted. Author-side portable evidence only, awaiting independent review.
