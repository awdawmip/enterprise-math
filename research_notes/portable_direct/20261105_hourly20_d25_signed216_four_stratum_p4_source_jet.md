# D25 — Signed 216 four-stratum mod-p^4 source-jet theorem

Date: 2026-11-05. Kind: TASK_RESEARCH, portable author-side lemma. Task: `RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT`; publication `TP2-B6F4FC938FF94941C1B7`; unchanged frozen scientific pin `c47e13e4aba0e006366f989d6334d443f6333ae3`.
Status: AUTHOR-DERIVED EXACT ALGEBRAIC IDENTITY / 94-PRIME FINITE MOD-p^4 CHECK / UNREVIEWED / NOT_ADMITTED. Original-class native H0/B0 NOT_RUN.

## Theorem (all primes p = 6n+1 >= 7)

In Z_(p), put a_k = (1/2)_k(1/3)_k(2/3)_k / (2^k(k!)^3) and W_p = sum_{k=0}^{p-1} (6k+1) a_k.
For (m_1,m_2,m_3)=(3n,2n,4n), (beta_1,beta_2,beta_3)=(1/2,1/3,2/3), we have the exact equality (1/2,1/3,2/3)=(-m_j+p beta_j) componentwise. For each k<p let I_j(k)=1_{k>m_j}, v(k)=sum_j I_j(k), and define

D_k = [prod_j beta_j^{I_j(k)} prod_{0<=r<k,r != m_j}(r-m_j)]/[2^k(k!)^3].

The exclusions apply individually to each j. Define source-labelled x_{j,r}=beta_j/(r-m_j) for 0<=r<k, r != m_j, and H_{s,k}=sum_{j,r} x_{j,r}^s for s=1,2,3. All their denominators, and those of D_k, are p-adic units because |r-m_j|<p and 1<=k<p.

Define
E_0=1,
E_1=H_1,
E_2=(H_1^2-H_2)/2,
E_3=(H_1^3-3 H_1 H_2+2 H_3)/6,
where H_s=H_{s,k}. Write the four separate residue-class source strata:

S_0 = sum_{k=0}^{2n} (6k+1) D_k [1+p E_1+p^2 E_2+p^3 E_3],
S_1 = p sum_{k=2n+1}^{3n} (6k+1) D_k [1+p E_1+p^2 E_2],
S_2 = p^2 sum_{k=3n+1}^{4n} (6k+1) D_k [1+p E_1],
S_3 = p^3 sum_{k=4n+1}^{p-1} (6k+1) D_k.

**For every prime p=6n+1>=7, W_p = S_0+S_1+S_2+S_3 modulo p^4.**

Proof: In each (-m_j+p beta_j)_k there is exactly one factor p beta_j when k>m_j. All other factors split as (r-m_j)(1+p beta_j/(r-m_j)). Thus

a_k = p^{v(k)} D_k prod_{j,r != m_j} (1+p x_{j,r})

is an exact identity in Z_(p). The elementary symmetric expansion of the final product has first three coefficients E_1,E_2,E_3 by Newton identities; its terms of total degree >=4 are multiples of p^4. For v=0,1,2,3 respectively retain orders 3,2,1,0 in p. Their exact ranges are [0,2n], [2n+1,3n], [3n+1,4n], [4n+1,p-1], yielding precisely S_0..S_3. This proves the theorem, without assuming W_p=p mod p^3.

The p^4 step adds two previously unobserved source types to the earlier mod-p^3 result: an **E_3 cubic harmonic jet** on the v=0 carrier, and the **v=3 high-index tail** (plus the E_2 and E_1 extensions on the two intermediate strata). Dropping either changes the full mod-p^4 observer in general. BRC carrier is the tuple (k,j,r,v(k),x_{j,r},signed 6k+1), while the allowed readout is W_p mod p^4; this is an auxiliary arithmetic observer, not a native crystalline CM assertion.

## Exact finite verification and falsification at the stronger precision

Independent standard-library Python checker `d25_signed216_four_stratum_20261105.py` computes each stratum from the p-factor-extracted source-labelled expansion, and W_p independently by the original 3F2 modular recurrence (2k+1)(3k+1)(3k+2)/(36(k+1)^3). All 94 primes p=1 mod6, 7<=p<=1200, passed equality modulo p^4 and the finite observation W_p=p modulo p^3.

In the frozen target prime classes the NEXT digit is nonzero:

p=13: W_13 mod 13^4 = 19786 = 13 + 9 * 13^3; (S0,S1,S2,S3)=(27144,26104,12675,10985) mod 28561.
p=19: W_19 mod 19^4 = 82327 = 19 + 12 * 19^3; (S0,S1,S2,S3)=(67393,59698,58121,27436) mod 130321.
p=373: W_373 mod 373^4 = 11832087049 = 373 + 228 * 373^3; (S0,S1,S2,S3)=(17724329257,8808962706,9585709842,14426842526) mod 373^4.

Therefore the stronger all-prime claim W_p=p modulo p^4 is false already at p=13 and p=19, both in the frozen two classes. This does not settle the actual second-digit target W_p=p modulo p^3, for which no uniform proof is claimed in this note.

## Highest frontier, ownership and recovery

This portable increment consumes, and does not recredit, `20261105_hourly20_d25_signed216_three_stratum_microscoping.md` (three-stratum exact mod-p^3 proof) and the separate onhour Research lane's original-R signed Clausen tail alignment. Native Source checkpoint `SOURCE_BYTES_AND_RECORDED_CLAIM_VERIFIED`, current-control source pin and frozen science pin remain unchanged. Native H0/B0 rank, [X]U mod p^2, actual Frobenius direction eta, signed Green odd port, kappa and independent review remain unresolved; source support Issue #1559 awaits authorized evaluator (PENDING_OWNER).

Next exact unit: seek a finite telescoper/parameter-derivative certificate for W_p=p modulo p^3 for both p=13,19 mod24, using the three-source cancellation and testing candidates with exact residue certificates. In parallel recover canonical Research owner legally from fresh continuation and own session, then CLAIM/OPEN; do not promote portable work into native Source without authorization.
