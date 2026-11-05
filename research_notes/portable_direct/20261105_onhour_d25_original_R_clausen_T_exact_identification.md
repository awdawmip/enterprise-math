# D25 — exact frozen R_p / Clausen T_p source alignment and universal 1/10 terminal unit

2026-11-05. **Status:** EXACT SCOPED ALL-PRIME ALGEBRAIC PROOF; 611-PRIME FINITE CHECK; AUTHOR-SIDE ONLY / UNREVIEWED / NOT_ADMITTED; NATIVE H0/B0 NOT_RUN.
Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; immutable science pin c47e13e4aba0e006366f989d6334d443f6333ae3.
Research logical conversation chatgpt-research-onhour-enterprise-math-20260923 (distinct from maintenance).

## Original frozen source, now read directly

The already-frozen original return \`research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_REFLECTED_DERIVATIVE_PRODUCT_BRIDGE_RETURN_20260827.md\`, Git blob 3fedf7bef09b426037840721855f9a9d05558a0b at commit 14e40bfbde5357ad38433c120b5f49feb0a0f019, section 2 defines for p=6n+1 in the plus classes
\[
b_i=B_i=\frac{(1/6)_i(1/3)_i}{2^i(i!)^2},\quad
R_p^{\rm frozen}=2\sum_{i=1}^n b_i\sum_{r=1}^i(6(i-r)+1)c_r\pmod p,
\]
\[
c_r=\frac{2^{r-1}((r-1)!)^2}{18(5/6)_r(2/3)_r}.
\]
This is the *genuine source-defined* R_p, not a newly chosen name. The source previously proved the original finite Clausen cutoff is p²R_p mod p³ at plus-class primes.

## Exact theorem 1: hypergeometric terminal unit = 1/10 modulo p

For **every** prime p=6n+1>=7 put \(q_k=(1/6)_k(1/3)_k/(k!)^2\) and \(C_p=(q_{p-1}/p^2)\bmod p\).
Then
\[
\boxed{C_p=10^{-1}\pmod p.}
\]
Proof. In the numerator of (1/6)_{p-1} the unique p-factor occurs at j=n, equal to p/6. After dividing it out the remaining product modulo p is (-1)^n n!(5n-1)!/6. In the numerator of (1/3)_{p-1} the unique p-factor occurs at j=2n, equal to p/3, leaving (2n)!(4n-1)!/3. Wilson gives ((p-1)!)²=1 mod p. For any 0<=k<p the complement identity \(k!(p-1-k)!=(-1)^{k+1}\pmod p\) therefore gives
\[
 C_p=\frac{(-1)^n n!(5n-1)!(2n)!(4n-1)!}{18}
 =\frac{1}{18(n+1)(2n+1)}
 =\frac1{10}\pmod p,
\]
because n+1=5/6 and 2n+1=2/3 modulo p. All inverses exist in the claimed prime domain. QED.

## Exact theorem 2: original R_p equals the signed terminal B_p/p²

Previously completed signed terminal theorem (20261105_onhour_d25_clausen_p3_convolution_boundary.md) and two-prefix certificate (20261105_onhour_d25_signed_boundary_rank2_prefix_certificate.md) define
\[
r_1=1,\quad r_{s+1}=r_s\frac{18s^2}{(6s+5)(3s+2)},\quad
A_i=\sum_{r=1}^i2^r r_r,\quad J_i=\sum_{r=1}^i r2^r r_r,
\]
\[
 T_p=\frac{B_p}{p^2}\equiv C_p\sum_{i=1}^n b_i[(6i+1)A_i-6J_i]\pmod p.
\]
From the actual frozen c_r definition,
\[
 c_r=\frac1{10}2^{r-1}r_r\quad \text{EXACTLY as rational numbers},
\]
since 18(5/6)(2/3)=10 and (5/6)_r=(5/6)(11/6)_{r-1}, (2/3)_r=(2/3)(5/3)_{r-1}. Thus
\[
 R_p^{\rm frozen}=\frac1{10}\sum_{i=1}^n b_i[(6i+1)A_i-6J_i]\pmod p.
\]
Theorem 1 now implies the new **source-typed identification**
\[
\boxed{R_p^{\rm frozen}=T_p=B_p/p^2\pmod p}
\]
for all primes p=6n+1, by direct algebra of the displayed source formulas. In particular it holds in both p=13,19 mod24 target classes without redefining the observer. Here the expression for R_p extends algebraically to the larger domain; the original frozen claim is only about the plus classes.

## Exact source-connected LIFT identity

For p=13,19 mod24 consume accepted CM0/UR first digit: g=sum_{k<p}b_k divisible by p and gh=p mod p² with h=sum_{k<p}(12k+1)b_k. The frozen LIFT is \(\Delta_p=( (g/p)h-1)/p=(gh-p)/p^2\bmod p\). The signed Clausen source formula \(W_p=gh-B_p\bmod p^3\) and the now proved frozen comparison yield
\[
\boxed{\Delta_p-R_p^{\rm frozen}\equiv(W_p-p)/p^2\pmod p.}
\]
This closes the original-to-Clausen scalar **interface identification** at all target primes, but the uniform assertion \(\Delta_p=R_p\) remains exactly equivalent to the OPEN all-target \(W_p=p\bmod p^3\). Neither is proved here. No change to the accepted parent or native crystalline benchmark is implied.

## Independent bounded exact audit

The companion source-alignment checker computes the source-original b_i and c_r by their own modular recurrences and independently checks each against the prior terminal T_p. It also checks the universal 1/10 identity. All **611** primes p≡1 mod6 in 7..10000 pass with 0 failures; among these the **312** targets p≡13,19 mod24 numerically satisfy Delta=R (finite observation). Original (p,C_p,R_p,T_p,Delta if target):
(7,5,3,3,NA), (13,4,0,0,0), (19,2,12,12,12), (139,14,91,91,91), (373,112,196,196,196), (997,698,626,626,626).
The checker consumes the previous locally executed JSON data from the independent original 216-vs-Clausen verification; results are independent of the new c_r recurrence computation.

## BRC and continuation

BRC: retain full ordered original (i,r) pair, signed 6(i-r)+1, source identity of c_r, low/high valuation and mod-p³ horizon. The two prefix moments are a proved sufficient quotient only for this particular scalar; original source is still required for other operators. BRC reuse COMPOSE_APPLIED with original reflected endpoint and signed terminal shell. The unit 1/10 and source R=T are exact statements, not new task registrations, native rank results or newly accepted UR.

Next smallest unproved science: a p-dependent finite terminal certificate for \(W_p=p\bmod p^3\), or exact independently recomputed counterexample; preserve source-original signed boundary. Fixed native p373 H0/B0 divided-power [X]U mod 139129, module rank, semilinear eta, kappa, signed odd Hesse/Green, independent replication remain NOT_RUN / PENDING_OWNER, see open #1559. No new execution CLAIM, run, Source checkpoint or Result.

Source original continuation request onhour11-20261105-1300-d25-cont returned SUCCEEDED at 2026-11-05T05:02:27.824721Z, execution_authorized=false. The two scientific checkpoints in this turn are GitHub-author-side, not Source admission.
