# D25 — Original W216 full four-grade reflection and terminal inverse

Date: 2026-11-10 (+08:00). Status: AUTHOR_SIDE / EXACT PROOF / UNREVIEWED / NOT_ADMITTED / NATIVE_NOT_RUN.
Task RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-D24-SECOND-DIGIT-LIFT; publication TP2-B6F4FC938FF94941C1B7; frozen scientific Source c47e13e4aba0e006366f989d6334d443f6333ae3.
Research logical lane chatgpt-research-onhour-enterprise-math-20260923, separate from maintenance.

## Theorem

Let p=6m+1>3 be prime and A_k=binom(2k,k)^2 binom(3k,k)/216^k=(2k)!(3k)!/((k!)^5*216^k) in Z_(p). Let W_p=sum_{k=0}^{p-1}(6k+1)A_k.

For 0<=k<p, v_p(A_k) is 0 on [0,2m], 1 on [2m+1,3m], 2 on [3m+1,4m], and 3 on [4m+1,6m]. For 1<=k<p set B_k=A_k*A_(p-k)/p^3, dividing before reduction. Then:

    B_k = C(k)/k^3 (mod p),

    C(k) = -1/18  for 1<=k<=2m,
            +1/36  for 2m<k<=3m,
            -1/36  for 3m<k<=4m,
            +1/18  for 4m<k<=6m.                 (R4)

All rational denominators are p-units. The middle-band case specializes to the previously proved grade-1/2 reciprocity, while the full four-grade atlas, boundary multipliers and terminal inverse are the new unit.

## Exact proof

The original recurrence is
    R(k)=A_(k+1)/A_k=(2k+1)(3k+1)(3k+2)/(36(k+1)^3).

The ratio of the p-local integral units B is exactly
    B_(k+1)/B_k=R(k)/R(p-k-1)
      =(2k+1)(3k+1)(3k+2)(p-k)^3/
       [(k+1)^3(2p-2k-1)(3p-3k-2)(3p-3k-1)].

Away from k=2m,3m,4m, reduce all factors separately: B_(k+1)/B_k=(k/(k+1))^3 (mod p). At these boundaries, first cancel the matching p factors in Q(k)=k^3 B_k:
    k=2m: (3k+1)/(3p-3k-1)=p/(2p), Q_(k+1)/Q_k=-1/2;
    k=3m: (2k+1)/(2p-2k-1)=p/p, Q_(k+1)/Q_k=-1;
    k=4m: (3k+2)/(3p-3k-2)=2p/p, Q_(k+1)/Q_k=-2.
No other factor becomes a p-multiple on 1<=k<p-1.

Seed: A_1=1/18. Wilson/factorial products give
    binom(2p-2,p-1)/p = -1 (mod p),
    binom(3p-3,p-1)/p = -1 (mod p).
For the second identity preserve the 2p^2 factor from the p,2p multiples inside (3p-3)!, before reduction. Since 216^(p-1)=1 (mod p), A_(p-1)/p^3=-1 (mod p). Thus Q_1=-1/18. Multiply successively by -1/2,-1,-2 to obtain the four constants in (R4). The valuation partition follows from the p-multiples in (2k)! and (3k)! while k! is always a unit for k<p.

## New signed AF4 grade-3 observation

Let W_(3,p)=sum_{k=4m+1}^{p-1}(6k+1)A_k, i.e. the FULL third-valuation band of the original 216 model. With h=p-k in [1,2m], (R4) gives
    A_(p-h)/p^3 = -1/(18h^3 A_h) (mod p).
The original signed weight 6(p-h)+1 reduces to 1-6h. Therefore

    W_(3,p)/p^3 = sum_{h=1}^{2m} (6h-1)/(18h^3 A_h) (mod p).  (G3)

This is a p^4-precision original cutoff identity; all h-denominators are units. The last original k=p-1 term contributes +5 to W_(3,p)/p^3 (mod p), matching the previously established terminal cutoff. (G3) captures all the other nontrivial grade-3 terms as well; replacing it with the last term alone would lose data.

## Exact computation / independent source

Checker: research_notes/portable_direct/d25_w216_full_four_grade_reflection_20261110.py. 148 primes p<=2000, p=1 (mod6), 137712 ordered pair checks of (R4), 148 full original signed grade-3 sum checks of (G3): PASS. The exact recurrence is checked against independent original integer binomial coefficients at p=7,13,19,37,73,109,181,373,997. Selected W_(3,p)/p^3 modp: p=7:6, 13:5, 19:4, 37:26, 73:10, 109:80, 181:92, 373:278, 997:347.
At p=373 the independently evaluated original W_373 modulo 373^4 is 11832087049 and (W_373-373)/373^3=228 (mod373); this is a finite check only.

## Position in frozen research

BRC typed carrier: (original k, valuation grade, reversed p-k, p-integral unit, signed weight); readout: R4 pair plus G3 original weight, exact modulo p^4. This port does not reconstruct the missing grade-0 third jet or grade-1 second jet; those are needed to assemble full fourth-digit W_p. Preserve the already completed grade-0 second jet, grade-1 first jet and grade-2 first jet; do not recredit them. Next independent algebraic unit: construct the missing extra jets and test the complete signed cross-grade finite telescoper, respecting both m parities and the original 216/2304 bridge.

Mother Delta_p-R_p (mod p) for p=13,19 (mod24) remains OPEN. Native fixed original-class p=373 H0/B0 divided-power [X]U mod139129, rank, semilinear Frobenius/eta, odd signed kappa and Delta-R plus independent replication remain NOT_RUN/PENDING_OWNER; support Issue #1559. No claim/run, formal native checkpoint, Result, admission or independent review is asserted.
