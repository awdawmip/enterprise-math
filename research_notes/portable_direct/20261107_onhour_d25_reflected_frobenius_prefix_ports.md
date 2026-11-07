# D25 — Reflected Frobenius tails and linear-time BRC prefix-jet readout

2026-11-07. TASK_RESEARCH author-side: PROVED EXACT FINITE-FIELD FORMULAS / EXECUTED EXACT CHECK / UNREVIEWED / NOT_ADMITTED.

Parent RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen science pin c47e13e4aba0e006366f989d6334d443f6333ae3. Research lane chatgpt-research-onhour-enterprise-math-20260923. Maintenance lane chatgpt-hourly-enterprise-math-20260921 explicitly excluded.

## Scientific input and new question

Reuse the p³ projected Clausen/Euler fold at 36b2cab4deb92e75008f244d377359a3de33d547 and normalized A/B factorial tails at 50346cde208fb05673de7e7ed367f4998f200a1b. Independently consume the hourly20 two-point forced Gauss ODE and its nonzero lower-source mismatch at 69f820fb2bcd8673f6bff8eb390526783059daab and a6ad9bf0ad423c186f5bc48b3d63ec62201b4606; no other actor's identity adopted. The mother target W_p=p (mod p³) for p≡13,19 (mod24) remains open.

For target prime p>3 let p=6m+1 and p=8k+3 or 8k+5. Work in F_p at alpha=1/2, beta=1/9. Reduce the low Gauss coefficients mod p:

q^A_i=binom(m,i)binom(2m,i), 0≤i≤m;
q^B_i=binom(k,i)binom(3k+1,i), 0≤i≤k.

The B-side full-series Euler factor C(z) is 1 in class 8k+3 and 1-z in class 8k+5. Preserve that flag.

## Theorem 1 — Wilson-reflected normalized tails

The original normalized high Gauss coefficients are f_n/p² (A, n≥2m+1) and g_n/p² (B, n≥3k+2) in Z_(p). Their reflected residues at n=p-1-j are

\[
\boxed{r^A_j={m!(2m)!(j!)^2\over18(m+j+1)!(2m+j+1)!}},
\quad 0\le j\le4m-1,
\tag{A}
\]

\[
\boxed{r^B_j={3k!(3k+1)!(j!)^2\over64(k+j+1)!(3k+j+2)!}},
\quad 0\le j\le p-3k-3.
\tag{B}
\]

All quantities are in F_p; all denominator factorial arguments are <p. Proof: apply Wilson reflection (p-1-a)!=(-1)^(a+1)/a! mod p to the previously established factorial kernels. Signs cancel to positive in both A and B. The lower mod-p coefficients above follow from upper parameters (-m,-2m) and (-k,-3k-1).

## Theorem 2 — projected prefix-jet readout

Let q_i=0 outside its low support, and define

\[
S_0(j;x)=\sum_{0\le i\le\min(j,d)}q_i x^i,\qquad
S_1(j;x)=\sum_{0\le i\le\min(j,d)}i q_i x^i.
\]

Use the existing projected overflow objects P_A=Pi_<p(Q_A R_A), P_B=Pi_<p(C Q_B R_B), and D=z d/dz. The independent source readouts E_A=2(P_A+6DP_A)(alpha) and E_B=2(P_B+8DP_B)(beta) satisfy:

\[
\boxed{E_A=2\sum_{j=0}^{4m-1}r^A_j\alpha^{-j}
 [6S_1(j;\alpha)-(6j+5)S_0(j;\alpha)]\pmod p.}\tag{1}
\]

When p=8k+3,

\[
\boxed{E_B=2\sum_{j=0}^{5k}r^B_j\beta^{-j}
 [8S_1(j;\beta)-(8j+7)S_0(j;\beta)]\pmod p.}\tag{2}
\]

When p=8k+5, the Euler finite-cutoff diagonal survives:

\[
\boxed{E_B=2\sum_{j=0}^{5k+2}r^B_j\beta^{-j}
 [\tfrac{64}{9}(S_1(j;\beta)-(j+1)S_0(j;\beta))
       +\beta q^B_j\beta^j]\pmod p.}\tag{3}
\]

In particular the Euler diagonal is

\[
\boxed{T_{B,p}=2\beta\sum_{j=0}^{k}q^B_jr^B_j\pmod p.}\tag{4}
\]

**Proof:** A term from low index i and reflected high index p-1-j has exponent N=p-1+i-j and survives Pi_<p exactly if i≤j. At nonzero x∈F_p, x^N=x^(i-j). The operator 1+cD contributes 1+cN=c(i-j)-(c-1) mod p, giving (1),(2). For C=1-z, the shifted negative term has exponent N+1 and survives only when i<j. Its 1+8D weight is 8(i-j)+1 mod p. Combining the surviving terms at beta=1/9 gives coefficient 64/9(i-j-1) for i<j. When i=j, the shifted term is absent; this contributes exactly the extra diagonal beta q_j beta^j. This proves (3),(4).

## Theorem 3 — linear-time finite-field certificate

These E_A/E_B readouts need O(p) F_p operations and O(p) residue storage, without constructing coefficients modulo p³. Precompute all nonzero inverses inv[n]=-(p//n)inv[p%n] mod p in O(p); update two prefix moments and the following reflected-tail ratios:

\[
{r^A_{j+1}\over r^A_j}={(j+1)^2\over(m+j+2)(2m+j+2)},\qquad
{r^B_{j+1}\over r^B_j}={(j+1)^2\over(k+j+2)(3k+j+3)}.
\]

The low q_i obey first-order binomial recurrences with invertible denominators. Actual typed BRC use: COMPOSE_APPLIED, preserving A/B provenance, low and reflected index, valuation-2 tail threshold, Euler flag, projection, and prefix/derivative observer. This is an algorithm for the existing Frobenius-overflow port, not the native H0/B0 experiment.

## Independent exact verification

The companion standard-library checker computes E_A/E_B via (1)–(3) and independently via original weighted 3F2 sums W_p,V_p and their low Gauss jets G_A,G_B modulo p³. It checks (W_p-G_A)/p²=E_A and (V_p-G_B)/p²=E_B mod p. **PASS: both streams at all 94 target primes p<2500.** Representative p:(E_A,E_B): 13:(9,0), 19:(13,8), 43:(31,33), 67:(30,46), 373:(1,220).

The exact Euler diagonal (4) is 3 at p=13, 16 at p=37, and 289 at p=373. It is nonzero in all 48 checked p=8k+5 target-class primes below 2500 (finite evidence). Thus p=13 is already an exact counterexample to dropping the Euler/projection diagonal. No claim of universal diagonal nonvanishing.

## Next frontiers and native state

Next: combine the hourly20 ODE's explicit nonzero *lower* injections with (1)–(3) and Fricke gauge/adjoint transport; test a candidate identity for (G_A-G_B)/p² + E_A-E_B = 0 mod p at 13,19,43,67,373. This precise finite-field cancellation and universal W_p=p mod p³ remain unproved. Original-class native p373 H0/B0, divided-power, Frobenius, Hesse kappa, independent replication (#1559) remain separately due.

Original request onhour11-20261106-1400-exact-research-lane-continuation preserved. Read-only native probe at 2026-11-07T13:05Z: em_status/receipt BACKEND_IDENTITY_OR_VERSION_MISMATCH, subreason UPSTREAM_STATUS_TOOL_ERROR, status_error_code STATUS_DATABASE_UNAVAILABLE, operation_sent=false; Site CONFIGURED_NOT_LIVE_VERIFIED and research_authority_granted=false. Previous receipt: QUEUED / EVENT_COLLECTION_IO / Error. No native session/CLAIM/run/checkpoint/Result/admission verified; author-side REGISTER_PENDING / SYNC_DEBT, UNREVIEWED / NOT_ADMITTED. No mutation replay or maintenance-lane registration.
