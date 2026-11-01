# D25 — Complete p-adic coefficient filtration for the 2304 weighted finite sum

2026-11-02 (+08:00); follow-on portable TASK_RESEARCH proof. AUTHOR-DERIVED / EXACT-CHECKED / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING. Original frozen D25 scientific input pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

Define R_{p,k}=(8k+1)(4k)!/((k!)^4*2304^k) for prime p>=5 and 0<=k<p.

**Theorem (all-index exact coefficient filtration).** For every such p,k,
    v_p(R_{p,k}) = floor(4k/p) + v_p(8k+1).                    (1)
There is exactly one k=k_* in {0,...,p-1} with v_p(8k+1)>0: the index k_*=(mp-1)/8 for unique m in {1,3,5,7} satisfying m*p≡1 (mod8). There v_p(8k_*+1)=1+v_p(m); elsewhere the weight valuation is zero.

**Proof.** Since k<p, neither k! nor 2304 is divisible by p. Since 4k<=4(p-1)<p^2 for p>=5, Legendre's formula has only v_p((4k)!)=floor(4k/p). The weight is linear in k with invertible coefficient 8 modulo p, giving one root in [0,p-1]. For that root the weight equals mp, with m the unique odd integer from {1,3,5,7} satisfying mp≡1 mod8. Therefore the additional valuation is 1+v_p(m), exactly. QED.

**Observer-specific p^3 truncation corollary.** The floor(4k/p) term is >=3 for every k with 4k>=3p. Therefore
    T_p=sum_{k=0}^{p-1}R_{p,k}
       ≡sum_{k=0}^{ceil(3p/4)-1}R_{p,k} (mod p^3).         (2)
The baseline valuation is 0/1/2/3 in four successive k-intervals, with exactly one extra resonance bump. If p≡13 mod24, k_*=(5p-1)/8 has base valuation 2 and extra 1, so its term vanishes modp^3. If p≡19 mod24, k_*=(3p-1)/8 has base valuation1 and extra1, giving an observable nonzero p^2 term. See preceding D25 note for the Wilson formula for its unit. Distinguish the individual weight-resonance port from the earlier Clausen high-degree cutoff.

BRC COMPOSE_APPLIED: the carrier is the source-tagged indexed signed rational summand list with k and valuation; the observer is the full weighted sum modulo p^3; the permitted operation is high-index deletion (2). This exact congruence certifies that deletion for this observer/modulus. It is not a certificate for derivatives, other operators, Clausen products or higher precision. This is external arithmetic; no native X6 transfer is claimed.

**Exact execution:** d25_2304_full_filtration_20261102.py independently constructs all coefficients via the rational 4-factor recursion modulo p^7 and validates (1), unique bumped index and p^3 upper-tail vanishing. All 166 primes 5<=p<=997 and all 76,122 coefficients PASS. The tail checks cover 18,946 coefficients. Boundary p5,p7 and target p13,p19 were included. Finite checks corroborate the infinite-domain factorial proof.

Next: establish a true modp^3 signed-ensemble relation S_p-T_p for p≡13,19 mod24; preserve the p19 p^2 resonance, separately preserve the earlier p13/p19 Clausen cutoff and the 216 resonance (valuation1 in both classes). Do not repeat prior proof units.

Research logical lane chatgpt-research-hourly-enterprise-math-20260923; no maintenance-lane operation. Gateway 0.6.11 at 2026-11-02: research_authority_granted=false, executor_binding_configured=false, UPSTREAM_CODE_REVIEW_REQUIRED; own historical #6637 recovery read-only, #6638 exact continuation definitively failed. Support #1558; no new native claim/open/checkpoint/admission, staging retained. P000, ACTIVE worldview, frozen science pin, scheduler and notifications unchanged.