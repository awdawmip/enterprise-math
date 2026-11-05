# D25: Signed 216/2304 half-endpoint Wilson–harmonic transport modulo p^4

Date: 2026-11-05. TASK_RESEARCH logical conversation: chatgpt-research-hourly-enterprise-math-20260923, separate from maintenance and onhour research. Task: RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT. Publication: TP2-B6F4FC938FF94941C1B7. Frozen science pin: c47e13e4aba0e006366f989d6334d443f6333ae3 (preserved). Classification: AUTHOR-DERIVED GENERAL EXACT ALGEBRAIC PROOF / 194-PRIME FINITE EXACT CHECK / UNREVIEWED / NOT_ADMITTED. Native original-class p=373 H0/B0 is NOT_RUN.

## Definitions
For each prime p>=5 and 0<=k<p set
a_k=(2k)!(3k)!/[216^k(k!)^5], b_k=(4k)!/[2304^k(k!)^4], H=(p-1)/2.
Let q_p=((p-1)!+1)/p (mod p), Wilson quotient, and h_r=sum_{j=1}^r j^{-1} (mod p), h_0=0. All displayed factorial-unit denominators are p-units.

For A=216 band A2: H<k<=floor((2p-1)/3) define
A2(k)=(2k-p)!(3k-p)!/[216^k(k!)^5] (mod p^2);
LA(k)=h_(2k-p)+h_(3k-p)-2q_p (mod p).
For A band A3: floor((2p-1)/3)<k<p define
A3(k)=-2(2k-p)!(3k-2p)!/[216^k(k!)^5] (mod p).

For B=2304 band B2: H<k<=floor((3p-1)/4) define
B2(k)=2(4k-2p)!/[2304^k(k!)^4] (mod p^2);
LB(k)=2h_(4k-2p)-2q_p (mod p).
For B band B3: floor((3p-1)/4)<k<p define
B3(k)=-6(4k-3p)!/[2304^k(k!)^4] (mod p).

## General exact theorem, arbitrary p-integral index weights
For every prime p>=5, termwise:
a_k=p^2 A2(k)(1+p LA(k)) (mod p^4) on A2,
a_k=p^3 A3(k) (mod p^4) on A3;
b_k=p^2 B2(k)(1+p LB(k)) (mod p^4) on B2,
b_k=p^3 B3(k) (mod p^4) on B3.

Given any p-integral weights wA(k), wB(k), let
UA=sum_A2 wA A2 (mod p^2), JA=sum_A2 wA A2 LA (mod p), DA=sum_A3 wA A3 (mod p).
Similarly UB,JB,DB with B2/B3. Therefore the full above-half weighted tails satisfy:
sum_(k=H+1)^(p-1) wA(k)a_k = p^2[UA+p(JA+DA)] (mod p^4);
sum_(k=H+1)^(p-1) wB(k)b_k = p^2[UB+p(JB+DB)] (mod p^4).
For original signed weights wA(k)=6k+1, wB(k)=8k+1, and Wp,Vp their full sums, WH,VH their half sums:
**Wp-Vp = WH-VH + p^2[(UA-UB)+p(JA+DA-JB-DB)] (mod p^4).**

## Proof, with source and valuation retained
For 0<=r<p, stripping the p-divisible multiples from (sp+r)! gives
F1(r)=(p+r)!/p = (p-1)! r! product_(j=1)^r(1+p/j)
=-r![1+p(h_r-q_p)] (mod p^2).
Because h_(p-1)=0 (mod p), two complete nonzero-residue blocks produce
F2(r)=(2p+r)!/p^2 = 2r![1+p(2h_r-2q_p)] (mod p^2).
The third block modulo p gives F3(r)=(3p+r)!/p^3 = -6r! (mod p).
This also follows directly by separating q!=1!,2!,3! p-factors and the Wilson sign of each full residue block; all operations take place in Z_(p).

In A2, (2k)! and (3k)! have one p-factor each, multiplying two F1 blocks: signs cancel and logarithmic first correction is h_(2k-p)+h_(3k-p)-2q_p. In A3, (2k)! has one and (3k)! two p-factors, multiplying F1*F2 for coefficient -2 mod p. B2 has (4k)! with two factors of p, giving F2 and correction 2h_(4k-2p)-2q_p; B3 has three, giving F3 and -6. Denominator k! remains p-invertible. These are termwise congruences; multiply by any p-integral weights and sum to prove the displayed identities. No Wp=p (mod p^3) conjecture is assumed.

## Verified exact finite evidence (independent of theorem proof)
Checker: research_notes/portable_direct/d25_216_upper_shell_wilson_harmonic_20261105.py. Standard-library exact integer modular arithmetic. Tested all 194 primes from 5 through 1200 (largest p=1193): termwise A2,A3,B2,B3 formulas, both full upper-tail sums modulo p^4, and joint transport, 194/194 PASS. Independent original binomial calculations checked both 216 and 2304 tails at p=7,13,19,139,373.

Signed original weights, values (UA mod p^2,JA mod p,DA mod p; UB mod p^2,JB mod p,DB mod p):
p=13: (140,8,5;39,0,6), A upper=23660, B upper=19773 (mod 13^4).
p=19: (218,16,4;266,11,16), A upper=85557, B upper=20577 (mod 19^4).
p=373: (96873,298,278;25737,165,119), A upper=4655673727, B upper=18318976301 (mod 373^4).
For 2304 original weight UB=0 (mod p), as follows from the existing Guo–Zudilin 2019 full/half p^3 theorem, but its next digit is retained separately. At p=373 the B upper tail p^3 digit is 353. The Wilson/harmonic source labels supply a direct next-digit observer and do not promote an auxiliary mod-p^4 identity to native CM Frobenius.

BRC = COMPOSE_APPLIED: typed carrier (source A/B, index k, valuation stratum 2 or 3, harmonic-prefix readouts, Wilson quotient, signed weight, UA/JA/DA/UB/JB/DB); scalar quotient is sufficient only for the exact weighted readout, not for other operations. Retains the observer's integer and modular provenance.

## Existing work consumed and next unit
This work extends rather than recredits the other onhour lane's p^3 signed factorial-unit half-shell theorem at 674e75ec78139ca95e56df2b1e683ca4d4757b48 and this same hourly20 lane's p^4 generic four-stratum source jets at b59c18ebf270692968331dabdff46731d8a846be. The frozen original R_p has been aligned to the Clausen high tail by the separate onhour lane; parent scalar goal Delta_p-R_p=0 (mod p) in p=13,19 (mod24) is equivalent to Wp=p (mod p^3). The remaining unit is a uniform terminating/half-endpoint certificate for E_p+C_A=0 (mod p), or a precise counterexample, reusing signed original source ports.

Native fixed 373 original-class divided-power H0/B0, [X]U modulo 139129, rank, semilinear eta, signed odd Hesse/Green, kappa, and independent review remain PENDING_OWNER (project support Issue 1559). This is a portable author-side candidate, not canonical Source checkpoint, native experiment, formal Result, or mathematical admission. The existing durable Source checkpoint, its source pins and completed_units are unchanged. Do not use maintenance identity, borrow another lane's Researcher, or mutate service session while pending read requests/old staging remain unresolved. Exact pending read IDs: em-h20-20261105-1520-current-continuation and em-h20-20261105-1520-task; bridge request research-hourly20-20261105-1450-exact-continuation SUCCEEDED, execution_authorized=false.