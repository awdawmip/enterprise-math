# D25: Original 216 weighted sum — character-sign finite certificate and complementary valuation theorem

Date: 2026-11-02 +08:00. TASK_RESEARCH portable mathematical work. Research logical lineage: chatgpt-research-hourly-enterprise-math-20260923 (distinct from maintenance). Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT / publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged.

Evidence classification: AUTHOR-DERIVED / EXACT-CHECKED-FINITE / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING. The general p^3 congruence below is a **conjectural extension**, not an all-prime theorem. This is not a native H0/B0 experiment or a Source checkpoint.

## 1. Original arithmetic and exactly checked finite assertion

For every prime p>=5 define the original rational/binomial sum

    S_p = sum_{k=0}^{p-1} (6k+1) binom(2k,k)^2 binom(3k,k) / 216^k.

All denominators are p-units, so the rational sum has an unambiguous image modulo p^m.

**Finite result:** for every one of the 1227 primes in 5<=p<=10000, exact modular arithmetic verified

    S_p = χ_3(p) * p (mod p^3);
    χ_3(p) = 1 if p≡1 mod3, -1 if p≡2 mod3.

The tested domain contains 611 p≡1 mod3 and 616 p≡2 mod3. Counts by p mod24: 1:143; 5:157; 7:156; 11:155; 13:157; 17:152; 19:155; 23:152. Exactly zero mismatches. The code deterministically sieves all primes <=10000 and computes each term in Z/p^3Z with the exact recurrence

    t_0=1;
    t_(k+1)=t_k*(2k+1)*(3k+1)*(3k+2)/(36*(k+1)^3);
    S_p=sum_(k=0)^(p-1) (6k+1)t_k.

The denominators are invertible for all 0<=k<p-1, p>=5. For 10 selected primes (5,7,11,13,19,31,37,61,109,373), a separate binomial-expression evaluator agrees modulo p^3. The current project checker also independently verifies coefficient valuations with integer binomial arithmetic for every k at primes p<=397. These calculations establish only the declared finite domain, not an infinitude claim.

**Sharpness witnesses:** (S_7-7)/7^3=1 (mod7), (S_11+11)/11^3=2 (mod11). Thus this same-character congruence with modulus p^4 fails at those two primes. At the original target p=373, S_373=373 (mod373^3), with fourth digit (S_373-373)/373^3=228 (mod373).

This wider sign pattern includes all original target classes 13,19 mod24 (both ≡1 mod3). It motivates looking for a more general identity or a simpler proof route; no prior-art novelty or universal proof is claimed.

## 2. General theorem: previously unanalysed complementary class p≡5 mod6

For primes p=6r+5>=5 and every integer 0<=k<p, let t_k be the unweighted coefficient in the recurrence above. Then

    v_p(t_k)=1_(k>2r+1)+1_(k>3r+2)+1_(k>4r+3).

Thus it has consecutive exact valuation bands 0,1,2,3, and all terms from k>=4r+4 vanish individually modulo p^3.

**Proof:** For 0<=j<=p-2, the factors in the numerator of the step recurrence are 2j+1, 3j+1, 3j+2. Their respective unique multiples of p in this range occur at j=(p-1)/2=3r+2 (factor p), j=(2p-1)/3=4r+3 (factor 2p), and j=(p-2)/3=2r+1 (factor p). In this entire range none is divisible by p^2, including p=5; and 36(j+1)^3 is a p-unit. Counting crossed thresholds in the product of steps j=0,...,k-1 proves the formula. QED.

The earlier p=6r+1 band is 1_(k>2r)+1_(k>3r)+1_(k>4r). The weighted factor 6k+1 has its p-resonance at k=r in the p≡1 mod6 class, versus k=5r+4 in the p≡5 mod6 class (at p=5 this latter factor equals p²). This is a proven structural difference between the two potential character-sign classes. Total weighted-sum cancellation to ±p modulo p^3 requires a separate argument.

BRC interpretation within the **external integer model**: record the three numerator-factor channels separately, with (p,k, valuation, residue class, source-factor index), and retain the weight resonance and cutoff. Discarding terms with valuation >=3 is proved observer-safe for S_p mod p^3, not automatically for mod p^4 or the original native X6 operator. No P000/worldview translation or native theorem is claimed.

## 3. Prior results, source separation, and continuation

Consumed the previous project proof (20261102_hourly_d25_frobenius_green_legendre_integral.md) of the compensated polynomial Green identity and its conditional CM first-digit criterion 9E_p H_p = 2J_p+3 (mod p), as well as the known original-sum signed Clausen cutoff C_p. The all-prime validity of that CM arithmetic criterion and the second digit remains OPEN. This author's new finite sign certificate and p≡5 mod6 band proof do not duplicate the earlier p≡1 mod6 valuation theorem.

A bounded external literature search (2026-11-02) located related but parameter-distinct Legendre and weighted hypergeometric congruences, including Zhi-Hong Sun, Legendre Polynomials and Supercongruences, Acta Arith. 159 (2013), doi:10.4064/aa159-2-6, and W.-W. Qi, arXiv:2604.04006 (2026), a WZ proof with 11n+3 and 27/16 parameters. Neither abstract established this exact 216 claim; external-prior-art duplication status remains UNKNOWN.

**Next scientific discriminating action:** identify or derive a general hypergeometric/p-adic-character/WZ certificate for S_p=χ_3(p)p (mod p^3), explicitly respecting the p≡5 mod6 sign and three valuation thresholds. If a general proof becomes available, it implies the original 13/19 external-sum congruence, while its native same-original-class H0/B0 experiment remains separate. Otherwise continue the precise CM Green first-digit 9EH=2J+3 and second-digit signed cutoff/integer carry proof route. No change to frozen scientific pin.

**Control evidence as observed 2026-11-02:** native Gateway 0.6.11 reports research_authority_granted=false, executor_binding_configured=false, CODE_REVIEW_REQUIRED/UPSTREAM_CODE_REVIEW_REQUIRED. Read-only Research recovery historical issue awdawmip/kimi-query-bridge#6637 is not present-day ownership, and its exact continuation #6638 was definitively FAILED; do not replay. Control support awdawmip/enterprise-math#1558; native p373 H0/B0 support #1559. No fresh Research CLAIM, OPEN, Source checkpoint, Result, review or admission was obtained here. Prior Research session/staging and contribution provenance preserved. P000, ACTIVE worldview, frozen input, existing schedules and notifications untouched.

Checker: research_notes/portable_direct/d25_w216_two_class_exact_check_20261102.py (Python 3 standard library).