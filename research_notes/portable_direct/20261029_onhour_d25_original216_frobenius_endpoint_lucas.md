# D25/LIFT — original A216 Frobenius reset, sharp finite Picard–Fuchs endpoint, and all-digit carry certificate

Date: 2026-10-29. Status: AUTHOR-SIDE / EXACT HAND PROOF / INTEGER VERIFIER EXECUTED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING / NATIVE H0/B0 NOT EXECUTED.

Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; immutable publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3, not rebased. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION. Author-side Research lane chatgpt-research-onhour-enterprise-math-20260923, never maintenance chatgpt-hourly-enterprise-math-20260921. Native session, winning claim, run and target_request_id remain UNKNOWN, not assumed absent. No new canonical dispatch or Source claim is implied.

## Original object and observer

For all n >= 0, define c_n = binom(2n,n)^2 binom(3n,n), a_n = c_n / 216^n = (1/2)_n(1/3)_n(2/3)_n / [2^n(n!)^3]. Define F_N(z) = sum_{n=0}^N a_n z^n, theta = z d/dz. The unchanged weighted A216 observable is A_p = [(1+6 theta) F_{p-1}](1). Here z tracks original degree, with original 216^{-n} retained inside a_n. Define the *third-order original* differential operator L = theta^3 - (z/2)(theta+1/2)(theta+1/3)(theta+2/3). This is different from the previously studied two-factor companion second-order operator.

## Unit I — exact sharp finite endpoint

Theorem 1 (all N>=0, equality in Q[z]): L F_N(z) = -(N+1)^3 a_{N+1} z^{N+1}.

Proof: The exact coefficient recurrence is a_{n+1}/a_n = [(2n+1)(3n+1)(3n+2)]/[36(n+1)^3]. In L F_N the coefficient of z^j vanishes for every 0<=j<=N by this recurrence. The single missing z^{N+1} coefficient equals -(1/2)(N+1/2)(N+1/3)(N+2/3)a_N = -(N+1)^3 a_{N+1}. This is a finite-polynomial identity, not an unjustified truncation of an infinite differential equation.

Theorem 2 (all primes p>=5): v_p(a_{p-1})=3, a_{p-1}/p^3 = -1 (mod p), and a_p = 18^{-1} (mod p). Therefore L F_{p-1}(z) = -p^3 a_p z^p = -p^3 z^p/18 (mod p^4), nonzero modulo p^4. Thus the **original** finite polynomial is homogeneous mod p^3 but NOT mod p^4. This sharp endpoint cannot be identified with the earlier two-factor companion boundary at degree p-1 and precision p^3.

Proof: For each numerator alpha in {1/2,1/3,2/3}, the product (alpha)_{p-1} contains exactly one p-divisible factor, namely c_alpha p at j=r_alpha. The c_alpha are 1/2 and 1/3,2/3 in some order, so their product is 1/9. The remaining factors reduce modulo p to prod_{j != r_alpha}(j-r_alpha) = (1-alpha)^{-1}, whose product over alpha equals 9 (since prod_alpha(1-alpha)=1/9). The combined p^{-3} numerator unit is 1. The denominator unit 2^{p-1}[(p-1)!]^3 is -1 by Fermat and Wilson, giving -1, with exact valuation 3. For a_p, Lucas gives binom(2p,p)=2 and binom(3p,p)=3 mod p, while 216^p=216 mod p; hence 2^2*3/216=1/18 mod p. All denominators are p-units.

## Unit II — p-Lucas and complete digit valuations, all indices

Theorem 3 (all primes p>=5, all u>=0, all 0<=r<p): a_{pu+r} = a_u a_r (mod p). Consequently, if N has base-p digits d_0,...,d_s, then a_N = prod_i a_{d_i} (mod p), and this is nonzero if and only if every d_i <= floor((p-1)/3). Exact count of nonzero coefficients among 0<=N<p^s equals (floor((p-1)/3)+1)^s.

Proof: If 3r<p, both 2r and 3r cause no base-p carry, so Lucas factors each of the two binomial streams into the u and r streams. If p/3<=r<p/2, the low digit 3r-p of 3(pu+r) is smaller than r, forcing both binom(3(pu+r),pu+r) and binom(3r,r) to zero modulo p. If r>=p/2, the low digit 2r-p of 2(pu+r) is smaller than r, forcing both binom(2(pu+r),pu+r) and binom(2r,r) to zero. Fermat factors 216^{pu+r}. For each r<p/3 the original binomial factors are p-units, so exactly those digits are supported. Iteration gives the full support formula and count.

Theorem 4 (all primes p>=5 and all N>=0): v_p(a_N) = [5 s_p(N)-s_p(2N)-s_p(3N)]/(p-1) = 2 C_p(N,N)+C_p(N,2N), where s_p is base-p digit sum and C_p(x,y) counts carries in base-p addition x+y. Proof: Legendre factorial valuation for a_N=(2N)!(3N)!/[(N!)^5 216^N] gives the digit sums; Kummer gives the exact carry count separately for each of the two binomial sources. As a sharp restart, valuations for N=p-1,p,p+1 are 3,0,0. The degree p coefficient is again a p-adic unit despite the p-1 triple hit.

Both proofs preserve exact index, original binomial streams, degree, and observer. The scalar coefficient test is NOT a native P000/BRC/H0-B0 theorem or a replacement for the original native benchmark.

## Executed exact integer witness (not universal-proof substitute)

Executed script in the adjacent file d25_original216_frobenius_endpoint_guard_20261029.py (stdlib Python, exact math.comb and independent p^4 recurrence, integer modular inverses; no floats). Results:
- PASS_ORIGINAL_A216_SHARP_PF_ENDPOINT: 194 primes 5<=p<1200.
- PASS_DIRECT_INTEGER_LUCAS_SUPPORT_P2_BLOCKS: all 725 indices in p^2 blocks p=5,7,11,13,19.
- PASS_DIRECT_INTEGER_LUCAS_PAIR_LAW: 1183 (u,r) instances, including carry branches.
- PASS_KUMMER_DIGIT_SUM_VALUATION: 2200 (p,N) instances.
- p=373: p^2=139129, p^3=51895117, p^4=19356878641; a_372 mod p^4=19304983524, a_372/p^3 mod373=372; a_373 mod373=228; boundary -p^3/18 mod p^4 = 7524791965 (nonzero); first block support 125, first p^2 block support 15625; valuations N=372/373/374 are 3/0/0.

The proof is exact for the stated quantifiers; computational coverage is finite and distinct from independent review or formal checking.

## Existing proofs consumed; next unmoved native frontier

Prior D25 six-port original weighted A216 p^3 decomposition is preserved: T00+T01+T02+T10+T11+T20 = A_p (mod p^3), and previous original reflection theorem (2026-10-28) already showed T20/p^2 = Theta_p. Do NOT re-prove or reassign authorship to these existing results. The unchanged unsolved target is, for all p=13 or19 (mod24), T00+T01+T02+T10+T11 = p-p^2 Theta_p (mod p^3). Theorems 1-4 supply the exact coefficient-level p-block restart and valuation scaffold for a future Dwork/finite WZ/character-sum proof, but DO NOT establish this five-port cancellation.

Original native #1559 OPEN and unassigned at this read: same-original-class p=373 H0/B0 divided-power [X]U mod139129, module rank, semilinear Frobenius/eta, odd signed Green/Hesse observer, kappa, and Delta_p-R_p must be executed by authorized original native operator and independently verified, with original objects/normalizations unchanged. This integer auxiliary guard cannot satisfy it.

Operational read: Site gateway v0.6.11 is read-only, research_authority_granted=false, write_relay_enabled=false, quota 5/5; recovery_status described but no callable exact named action exposed here. Own original request, Source continuation, claim/run/session remain UNKNOWN. No role-bound mutation/replay performed. Next authorized action: reconcile original Research-lane request and exact canonical Source continuation before own CLAIM/open/dispatch; bind this author-side evidence only under valid current Source permissions. GitHub author-side publication does not equal canonical Source checkpoint/Result/admission, independent review or P000 change. Next concrete scientific action: derive and verify first nontrivial p-adic Dwork lift of the weighted p-block with signed-observer and source-specific boundary corrections, then compare to original six-port ledger. Native execution route is still PENDING_OWNER and separate.
