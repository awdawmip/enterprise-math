# D25 SECOND-DIGIT-LIFT — original source-port carry is not a universal strict staircase

At: 2026-10-30 Asia/Hong_Kong. Parent ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION; Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7. Frozen scientific Source pin c47e13e4aba0e006366f989d6334d443f6333ae3 unchanged. Historical Research conversation chatgpt-research-onhour-enterprise-math-20260923 is separate from maintenance chatgpt-hourly-enterprise-math-20260921; no maintenance session/claim/run is borrowed.

Classification: AUTHOR-SIDE / FIXED-PRIME EXACT COUNTEREXAMPLES / EXECUTED FINITE CHECK / UNREVIEWED / NOT_ADMITTED / REGISTER_PENDING / SOURCE_CHECKPOINT_PENDING. This artifact is not a canonical research Result.

## Original objects and exact integer source partition

For prime p>=5 in Z_(p), preserve the ORIGINAL weighted finite sums

A_p = sum_{n=0}^{p-1} (6n+1) * binom(2n,n)^2 * binom(3n,n) / 216^n,
B_p = sum_{n=0}^{p-1} (8n+1) * binom(2n,n)^2 * binom(4n,2n) / 2304^n,
chi_p = (-3/p), D_p=A_p-2B_p+p*chi_p.

The **raw** coefficient valuation for n<p is v_A(n)=floor(2n/p)+floor(3n/p), v_B(n)=floor(4n/p); both lie in {0,1,2,3}. This follows from Legendre's factorial formula; n!, 216 and 2304 are p-units. Partition A_p and B_p SEPARATELY into original signed-weight source sums A_p^(j), B_p^(j) for raw valuation j. Define E_j=A_p^(j)-2B_p^(j)+[j=0]*p*chi_p and T_j=sum_{i=0}^j E_i. T_3=D_p. Since E_j belongs to p^j Z_(p) for j>=1, the stage filtration does not by itself assert equality of cumulative valuations. Weighted coefficient factors are included, but the tier refers to raw valuation.

## PROVED fixed-prime counterexample to a possible extrapolation

The previous author-side p=373 ledger (commit 5d5b1d8b07ccc807c71e7d8c11f2a2f65edb8aec) happened to show cumulative valuations (1,2,3,4). **It never proved a universal staircase.** The tempting extrapolation v_p(T_j)=j+1 for *every* prime p>=5 is FALSE.

Direct exact original-integer-binomial calculation modulo 7^5=16807 gives:
- T_0 = 3430 = 10*7^3, so v_7(T_0)=3;
- T_1 = 11760 = 240*7^2, so v_7(T_1)=2;
- T_2 = 9947 = 29*7^3, so v_7(T_2)=3;
- T_3 = 0 modulo 7^5, so v_7(T_3)>=5, with no claim of exact valuation >4.

Thus the source addition j=0 -> 1 **lowers** cumulative valuation from 3 to 2: E_1 = 8330 (mod 16807) has valuation 2. This respects v_p(x+y)>=min(v_p(x),v_p(y)); it refutes automatic monotonicity of the cumulative valuation.

Two structurally distinct exact witnesses:
- p=71: T_0 = 211338884 mod 71^5 and T_0/71^2 = 41924 = 34 mod 71, hence v_71(T_0)=2, not 1.
- p=107: T_2 = 9437731272 = 72*107^4 mod 107^5; hence v_107(T_2)=4, not 3. The full T_3 at 107 still has valuation exactly 4, so an early extra digit does NOT force the fifth digit of the total to vanish.

All of 7,71,107 lie **outside** the frozen target classes p=13,19 mod24. None disproves the original LIFT or the proposed p^4 bridge. This is a rigorous negative certificate for a proposed universal *proof shortcut*, not for the task target.

## Exhaustive precise finite check and independent arithmetic

The accompanying reproducible standard-library Python program d25_source_carry_exceptional_ports_guard_20261030.py was actually executed. It exhaustively visits 1436 primes 5<=p<12000, including 363 in the two target residue classes. Its observed stage valuations, capped at 5 for residue zero mod p^5, satisfy v_cap(T_j)>=j+1 for all tested cases. The COMPLETE lists having *strictly more* than j+1 are:
- j=0: p=7,71,137;
- j=1: none;
- j=2: p=107,1289;
- j=3: p=5,7, where only v_p(T_3)>=5 is certified.

The finite scan is NOT a universal lower-bound theorem. No such exceptional staircase case appeared among the 363 finite target-class primes. Second, independent original integer-binomial evaluation checks every signed tier and all T_j at p=5,7,13,19,71,107,137,373,1289; results exactly match the modular recurrence. No floating point or surrogate operator is used.

The two p-unit coefficient ratios used in recurrence are

a_(n+1)/a_n = (2n+1)(3n+1)(3n+2)/(36(n+1)^3),
b_(n+1)/b_n = (4n+1)(4n+2)(4n+3)/(576(n+1)^3).

They are valid for 0<=n<p-1, so modular inversion never hits p. For each source, apply original weight (6n+1)/(8n+1) and preserve source labels BEFORE combining signs. The independent path uses the original exact binomial numerators and 216^(-n),2304^(-n) modulo p^5, not the same recurrence.

## BRC observer and hard scope boundaries

BRC resolution COMPOSE_APPLIED: carrier is (A/B model, original index n, raw coefficient valuation, signed original weight, p-unit denominator, source label j, p^5 precision, cutoff); operation is signed port addition then precision-aware valuation. Positive BRC mass is not signed cancellation. No native X6/Heartbeat or H0/B0/Frobenius identification follows from this scalar ledger. The strict-step shortcut is unavailable; proving p^3 LIFT still requires the ACTUAL paired target-class identity J_p+C_m H_m=0 mod p for every p=13,19 mod24. Preserve the previously proved two-zone A216 jet and middle-kernel resonant boundary instead of extrapolating individual stage valuations.

**Priority native benchmark #1559 is unchanged:** the same-original-class p=373 H0/B0 divided-power [X]U mod 139129, native module rank, semilinear Frobenius/eta, odd signed Green/Hesse, same-definition kappa and independent reproduction. Issue #1559 was OPEN with no verified assignee on this read; the authorized native evaluator remains PENDING_OWNER. Existing Site status has research_authority_granted=false, write_relay_enabled=false and em_checkpoint_list ACCESS_DENIED. Exact Source session/claim/run/request recovery is UNKNOWN here; no Source registration, CLAIM, checkpoint, review or acceptance is claimed. The Source scientific pin and P000 remain fixed.

Next exact scientific action: attempt an actual coupled parameter-contiguous/WZ or CM certificate for J_p+C_m H_m modulo p across BOTH target classes, with original sign/valuation/observer information and nonhomogeneous cutoff. Separately an authorized native evaluator must execute #1559, not replace it with this scalar experiment.

Reproduce using standard Python >=3.8: python3 research_notes/portable_direct/d25_source_carry_exceptional_ports_guard_20261030.py. Expected final marker PASS_D25_ORIGINAL_SOURCE_PORT_EXCEPTIONAL_CARRIES.
