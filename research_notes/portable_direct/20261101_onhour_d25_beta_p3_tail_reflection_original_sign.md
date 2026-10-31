# D25: exact beta clipped-boundary p³ reflection; p≡19 third-digit Gauss lift

2026-11-01; AUTHOR-SIDE / ALGEBRAIC THEOREM PROVED (with explicitly cited external B theorem) / EXECUTED EXACT FINITE CHECK / UNREVIEWED / NOT_ADMITTED. Parent task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen SCIENTIFIC Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. This is not Source CLAIM/run/checkpoint/Result or native H0/B0.

## Source and statements

Let p>3 be prime. Use original beta Gauss coefficients
\[
\beta_k=\frac{(1/8)_k(3/8)_k}{9^k(k!)^2},\quad G_p=\sum_{k=0}^{p-1}\beta_k,\quad H_p=\sum_{k=0}^{p-1}(16k+1)\beta_k.
\]
The signed *two-index* clipped Clausen boundary and distinct original weighted2304 series are
\[
T_{\beta,p}=\sum_{0\le i,j<p;\ i+j\ge p}[8(i+j)+1]\beta_i\beta_j,\qquad
B_p=\sum_{k=0}^{p-1}(8k+1)\frac{\binom{4k}{2k}\binom{2k}{k}^2}{2304^k}.
\]
Consume, do not re-prove, exact Clausen B_p=G_pH_p-T_{\beta,p}. The Guo–Zudilin published 2019 theorem gives B_p≡p(-3/p) modulo p³ for all p>3 (https://arxiv.org/abs/1803.01830). Prior author algebra proved T_beta≡0 modulo p² *termwise* for p=1,3 mod8. **New here:** the nonzero next boundary digit for p=3 mod8.

**Theorem 1 (all p=8t+3>3).** Define b_0=1 and, in F_p,
\[
b_{i+1}=b_i\frac{(8i+1)(8i+3)}{576(i+1)^2}\ (0\le i<t),\qquad
Q_0=1,\quad Q_{r+1}=Q_r\frac{576(r+1)^2}{(8r+13)(8r+15)}\ (0\le r<t-1).
\]
Put S_i=Σ_{r<i}Q_r and M_i=Σ_{r<i}rQ_r. Then the precisely source-typed signed boundary scalar
\[
\boxed{U_{\beta,p}=\frac6{35}\sum_{i=1}^{t}b_i[(8i-7)S_i-8M_i]\in\mathbb F_p}
\]
obeys the UNIVERSAL congruence
\[
\boxed{T_{\beta,p}\equiv p^2 U_{\beta,p}\pmod{p^3}.}
\]
It costs O(t) field operations, with p-unit denominators. This U_beta is NOT the different original-216 upper-tail U or the p373 H0/B0/Frobenius object. The truncated *signed* two-index source is kept until the terminal scalar is known to preserve the specified observer.

**Proof.** The exact ratio is β_{k+1}/β_k=(8k+1)(8k+3)/(576(k+1)²). For p=8t+3 the only numerator factors divisible by p in k=0,...,p-2 occur at k=t (8k+3=p) and k=3t+1 (8k+1=3p). All denominators k+1<p,576 are p-units. Thus v_p(β_k)=0 on [0,t], 1 on [t+1,3t+1], and 2 on [3t+2,p-1], *exactly*. Two indices at most 3t+1 have sum ≤6t+2<p; any contributing pair of total valuation ≤2 must therefore have one low index 1≤i≤t and one high index j=p-1-r with 0≤r<i. Pairs of valuation 1+2 or 2+2 vanish mod p³, and both low/high orientations occur.

For a=1,3 the map k→8k+a modulo p permutes F_p. The product of its nonzero residues is −1 by Wilson. Excluding k=p−1 removes the factor a−8; isolating its unique root leaves reduced products (3p)/p·(−1)/(1−8)=3/7 for a=1, and p/p·(−1)/(3−8)=1/5 for a=3. The denominator 576^{p−1}((p−1)!)² is 1 modulo p. Hence β_{p−1}/p²≡3/35 modulo p. Reversing the exact ratio gives
\[
\beta_{p-1-r}/p^2\equiv(3/35)Q_r\pmod p\quad(0\le r<t).
\]
The signed weight at the two-index source is 8(i+p−1−r)+1≡8(i−r)−7 mod p. Substitution into both orientations yields
\[
T_{\beta,p}/p^2\equiv (6/35)\sum_{i=1}^t b_i\sum_{r=0}^{i-1}[8(i-r)-7]Q_r\pmod p,
\]
which is the stated two-prefix-moment formula. p≥11 and 8r+13,8r+15<p over the recurrence range, so all displayed inversions are justified. QED.

**Theorem 2 (all p=3 mod8, and selected p19).** By the already established exact Clausen relation and external Guo–Zudilin p³ theorem,
\[
\boxed{G_pH_p\equiv p\left(\frac{-3}p\right)+p^2U_{\beta,p}\pmod{p^3}.}
\]
On target p≡19 mod24 the existing CM(-24) zero selector proves G_p≡0 mod p and H_p is a p-unit, and (-3/p)=1. Therefore the genuinely new selected-factor *third digit* satisfies
\[
\boxed{G_p/p\equiv H_p^{-1}(1+pU_{\beta,p})\pmod{p^2},\quad p\equiv19\pmod{24}.}
\]
If H_0 is H_p modulo p and H_1=(H_p−H_0)/p modulo p, the same exact formula is H_0^(-1)+p(U_beta H_0^(-1)−H_1 H_0^(-2)) modulo p². It is NOT legitimate to use only the previous Legendre derivative H_0 and silently drop H_1 or U_beta. The non-target p≡11 mod24 branch has G a unit and H/p≡G^(-1)(−1+pU_beta) modp², which can be used as an adversarial check.

## Sharp witness and exact execution

For p=19,t=2, b_1=10,b_2=8,Q_0=1,Q_1=5 modulo19. The sum before prefactor is 10·1+8·(9+5)=122≡8; 6/35=17 modulo19, hence U_beta,19=3. Original signed boundary T_beta,19=1083=3·19² modulo19³. Original Gauss residues are G_19=532,H_19=853 modulo6859; H_19=131 modulo361, and G_19/19=28 modulo361. Explicitly (1+19·3)·131^(−1)≡28 modulo361. Other nonzero (p,U_beta) values: (43,14),(67,46),(139,102).

The attached executed Python stdlib program d25_beta_p3_reflection_cert_compact_20261101.py checked all **108 primes p≤3000, p≡3 mod8**, including **54 p≡19 mod24 target primes**: valuation pattern for every beta coefficient, Wilson endpoint, exact signed two-index tail via independent O(p) suffix moments modulo p³, new O(t) reflected formula, original weighted2304 sum via independent 3F2 recurrence, and both selected factor third digits. At p=11,19,43,67,139 it additionally cross-checked **279 individual beta coefficients and five whole B sums** from direct integer factorial/binomial definitions. All assertions passed. Finite checks support but do not establish the universal theorem; the proof above and the explicitly cited 2019 external result do. No formal Lean checker was run.

## Parent frontier and honest control state

The parent remains to prove original A_p≡p modp³ for p≡13,19 mod24, equivalently the frozen Delta_p−R_p=0 modp; the stronger A_p−2B_p+pχ_{−3}(p) modp⁴ affine relation remains UNPROVED. **Next exact scientific action**: integrate the now explicit p19 beta p³ signed carry and H_1 into the original weighted216 low I0–I2 with previously proved high I3–I5, or produce a counterexample. For p13 the independent G_p≡0 modp²/three-port beta-tail cancellation remains unproved. Prior beta p², Legendre, CM selector and upper original reflection are consumed, not re-proved.

Native fixed p373 **original** H0/B0 divided-power [X]U mod139129, real semilinear Frobenius direction/normalization and rank, signed odd Green/Hesse, κ and independent replication remain **NOT_RUN/PENDING_OWNER** in existing Enterprise Math issue #1559. This scalar p19 computation is not an alternative benchmark or a substitute result. Research logical conversation is chatgpt-research-onhour-enterprise-math-20260923, never the maintenance lane. Own bridge recovery awdawmip/kimi-query-bridge#6632 was read without winning CLAIM/run; exact dispatch request research-onhour-20261031-0205-dispatch-r15 in #6633 was FAILED/UPSTREAM_CODE_REVIEW_REQUIRED, not replayed. Current gateway 0.6.11 reports research_authority_granted=false, executor_binding_configured=false; author-only preservation is **REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / UNREVIEWED / NOT_ADMITTED**. Older three neutral staging files remain separate. P000, ACTIVE worldview, immutable scientific Source pin and existing scheduler settings are unchanged.