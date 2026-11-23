# T6 p13 q10 split(3,7), negative pattern (1,2,2,2): scoped non-author audit
Date 2026-11-24. Existing Driver EM-DVR-DEBB5E, shared author context disclosed. This is a scoped mathematical audit, not a Native Review, Result admission, or full independent lattice replay. Preserve the original on-hour author's contribution and historical Activity; no identity adoption.

## Inputs
Author exact certificate at awdawmip/enterprise-math@44d334c43838b26d86919b2022190c3a0b9ec467:research_checks/T6_P13_Q10_SPLIT3_7_NEG1222_FULL_AUTHOR_EXACT_CERT_20261124.json (blob e2c8667255f86a51bfefbd29f9d1f3c6b303152b). Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca, side mass cap 2331. Reuse the scoped lattice and integer GS argument from ab313f43af5f38da2bd051a7406a682de7a0eef1, not its conclusions about other patterns.

## Exact roster audit
Write named vertical atom (q,r), denominator 13*(13q+r), 1<=r<=12. Positive q-total 3 patterns (3),(1,2),(1,1,1) have 12+144+C(14,3)=520 rosters. Negative pattern (1,2,2,2) has 12*C(14,3)=4368. For t=1,2,3 distinct residues in its q2 multiset, counts are 144,1584,2640 (12 times 12,132,220). Disjoint positive choices are 12+11*(12-t)+C(13,3)=419,408,397 respectively. Therefore raw pairs=2271360, primitive disjoint pairs=1754688, common atom pairs=516672, all agreeing with the author certificate.

Independently enumerate both rosters in lexicographic order with repetitions preserved. All three reported witness index pairs exactly recover their named atom lists. For the maximal-prime-13 subdomain, trial-divide 13q+r by 2,3,5,7,11,13 and require remainder 1. Allowed r: q1={1,2,3,5,7,8,9,11,12}; q2={1,2,4,6,7,9,10}; q3={1,3,5,6,9,10,11}. The exact smooth roster counts are P=235,N=756; raw=177660; disjoint=124236; common=53424. This follows also from P=7+9*7+C(11,3)=235, N=9*C(9,3)=756 and disjoint count 9*[7*(7+8*6+C(10,3))+42*(7+8*5+C(10,3))+35*(7+8*4+C(10,3))]=124236. This is a domain reduction for independent review, not a new lattice exclusion.

## Witness audit
Use independent BigInt extended Euclid for inverses. Recompute sum u_r/r^k + sum_pos (13q+r)^(-k) - sum_neg (13q+r)^(-k) mod 13^k, k=1..6; all residues zero for all three witnesses. Vertical mass per atom=13*(13q+r)-1; q0 signed coefficient u_r weighted by 13r-1. Recompute original side masses by signs, weighted q0 norm squared, and radius squared (2331-c+)^2+(2331-c-)^2.

| indices (neg,pos) | vertical masses | final masses | norm squared | radius squared |
|---|---|---|---:|---:|
|189,274|712,1465|3103,3097|1898165|3371117|
|3817,221|751,1595|2713,3747|2251848|3038096|
|3871,376|764,1608|4086,2716|2955398|2978218|

All three are valid relaxed congruence sphere witnesses, none is within both budgets; all three also fail the vertical smoothness test. Full independent GS traversal of the 1754688 literal or 124236 smooth primitive pairs has not been performed. The author reports 3584232 GS nodes, 3 relaxed sphere witnesses, zero budget-valid, with existing lattice premises; this audit does not certify exhaustive execution.

## Control linkage
Consumed original dvr-20261124-0502-t6-current-cont-v1: SUCCEEDED, read snapshot 582838fa8e252dd3c2d2eaf672a15d9c1b070233 at admission, not latest at completion; NO_LIVE_CLAIM as of that observation. Original global RR-C428294CF760BD8D99AA remains immutable NEGATIVE_BOUNDARY / partial progress, not an admission of subsequent p17/p13 results. The old q14 preflight plan is stale as a scientific frontier but not rewritten as control authority. Own session recovery metadata is open/nonrevoked, not a current DA grant. A fresh exact Result artifact read dvr-20261124-0558-t6-rr-c428-exact-read-v1 is pending; consume original before further review-flow operations. No new CLAIM or duplicate dispatch. Original F7 failed read remains distinct from prior review mutation; do not replay the denied mutation. Next: check q11113 existing author coverage, preserve ownership, audit only uncovered evidence, and reconcile exact Result/review set before formal association.
