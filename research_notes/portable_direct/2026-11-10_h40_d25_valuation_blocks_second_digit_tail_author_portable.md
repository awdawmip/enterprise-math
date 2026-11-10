# D25/LIFT — three exact valuation blocks and a second-digit tail witness

Date: 2026-11-10. Classification: AUTHOR_PROVED / FINITE_EXACT_INTEGER_VERIFIED / UNREVIEWED / NOT_ADMITTED.
Original frozen science: c47e13e4aba0e006366f989d6334d443f6333ae3. Parent: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT, publication TP2-B6F4FC938FF94941C1B7. Exact original scalar interface: research_returns/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_TERMINATING_JACOBI_JET_CERTIFICATE_RETURN_20260828.md.
Author-level portable derivation, not a native CLAIM, checkpoint, Result or independent review.

## Universal arithmetic lemma

For every prime p≥13, p≡13 or 19 (mod24), put a=(p−1)/6, b=(p−1)/3, B_0=1 and B_(k+1)/B_k=(6k+1)(3k+1)/(36(k+1)^2), for 0≤k<p−1.

For 0≤k<p, the exact p-adic valuations are:
- v_p(B_k)=0 for k≤a;
- v_p(B_k)=1 for a<k≤b;
- v_p(B_k)=2 for b<k<p.

Proof: Denominators 36(k+1)^2 are p-units. Because p≡1(mod6), in the allowed index range 6j+1 has precisely one multiple of p, namely p at j=a; 3j+1 has precisely one, namely p at j=b. Each is a simple factor p. Thus the cumulative valuation rises by one at each of k=a+1 and k=b+1.

Split the original frozen rational sums g=sum(B_k) and h=sum((12k+1) B_k), 0≤k<p, into the successive blocks I0=[0,a], I1=[a+1,b], I2=[b+1,p−1]. Let Si=sum(B_k over Ii) and Hi=sum((12k+1)B_k over Ii).

The frozen premise p|g implies p|S0 because p|S1 and p²|S2. Therefore A0=S0/p, A1=S1/p, A2=S2/p² are all p-integral. The exact precision needed is A0,A1 modulo p², A2 modulo p, H0,H1 modulo p². We have:

G_p=g/p ≡ A0+A1+p A2 (mod p²), h≡H0+H1 (mod p²), and H2≡0(mod p²).

The accepted UR first-digit identity G_p h≡1(mod p) makes both second digits well-defined:
Delta_p=(G_p h−1)/p mod p;
Delta_p_trunc=((A0+A1)(H0+H1)−1)/p mod p.

Their exact correction is

**Delta_p − Delta_p_trunc ≡ A2 (H0+H1) (mod p).**

This p-adic BRC residual separates valuation-two contributions invisible in h mod p² and G_p mod p from the part necessary to compute the divided second digit. The result does not supply the still-missing frozen original-class R_p/H0/B0 native comparison.

## Explicit p=373 witness

For p=373, a=62, b=124 and the block lengths are 63,62,248; p³=51895117 and p²=139129.

(S0,S1,S2) mod p³ = (15144919,26185346,35060508).
(A0,A1) mod p² = (40603,70202); A2 mod p=252.
(H0,H1,H2) mod p² = (115055,86909,0).
G_p mod p²=65672; h mod p²=62835.
Delta_373=196, Delta_373_trunc=372.
The exact tail correction is A2*h≡252*171≡197(mod373), hence 372+197≡196(mod373).

The omitted valuation-two tail changes the second digit by 197. Seven other previously checked primes (13,19,37,43,61,67,211) have independently recalculated corrections (9,6,10,3,46,51,110). All eight checks are finite, not a universal nonvanishing theorem.

## Verification, source and continuation

The five-file local author research package D25_LIFT_VALUATION_BLOCK_TAIL_AUTHOR_PORTABLE_20261110.zip contains this complete proof, exact eight-prime JSON certificate, a standard-library Python checker, a verification log and an author handoff. The checker computes every B_k both via modular recurrence and via independent accumulated integer numerator/denominator products, verifies the exact valuation at every index and reconstructs original G_p,h,Delta_p and the correction. These are arithmetic author crosschecks, not independent review.

UR V2 original four-file bundle has not been recovered from actual bytes (expected 94687 bytes, SHA256 4eed27397cf4442aeb6464e4bf4af171552fc581c79f8783adb32dc3c19c1b76); its earlier UR mathematics is not repeated. Exact original queued read IDs for reconciliation: h40-20261110-1640-tasks, h40-20261110-1640-d25-continuation, h40-20261110-1640-d25-task. The own recovery interface returned SITE_CONTROL_OWN_ISSUED_SESSION_REQUIRED; there is no verified own winning native CLAIM. The next narrow source-faithful task is to authenticate the actual R_p and H0/B0 from the frozen original-class input, compute R_373 and compare with Delta_373=196. Source-native checkpointing requires legitimate own active session and winning claim. If the continuation seed state is CURRENT_TASK_INPUTS_WITH_NO_RECORDED_OWNER_PROGRESS, its predecessor completed_units remains empty; author-portable evidence is separate staged work.
