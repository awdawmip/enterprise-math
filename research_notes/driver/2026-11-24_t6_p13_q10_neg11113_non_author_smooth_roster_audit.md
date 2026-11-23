# T6 p13 q10 split(3,7), negative pattern (1,1,1,1,3): scoped non-author audit

2026-11-24. Existing RESEARCH_DRIVER EM-DVR-DEBB5E; shared author context disclosed. Scoped non-author audit, not an independent full lattice traversal or Native Review.

## Frozen inputs and provenance
Original author EM-DIRECT-D03BC9, RA-A468735D7C934B25C4B9614F. Full certificate at enterprise-math@5f53f3158bd460f97766876a4e27ee8a01344689:research_checks/T6_P13_Q10_SPLIT3_7_NEG11113_FULL_AUTHOR_EXACT_CERT_20261124.json, blob 2bdabc8caa046c6bfaf3c6d2e6e55605bfb69efa. Original Activity at 570c609b0ce9597332b8a511d4d63eec0f45e480 already represents this certificate, with its readback at 648fd7c945322880d4a6feaa138dfd2b0150b907. Do not recreate author Activity or repeat the author's complete search. Frozen science d84bd940cfb093cdc60e569f15cad58772a51dca; each side's mass cap 2331. Reuse prior scoped lattice audit ab313f43af5f38da2bd051a7406a682de7a0eef1, not its conclusions for other patterns.

## Exact combinatorial audit
Atom (q,r) has denominator 13*(13q+r), mass denominator minus 1, 1<=r<=12. Positive q-total 3 has patterns (3),(1,2),(1,1,1), hence 12+144+C(14,3)=520 rosters. Negative q11113 has 12*C(15,4)=16380 rosters. If its four q1 atoms have t distinct residues, there are 12*C(12,t)*C(3,t-1) negative rosters and exactly 11+12*(12-t)+C(14-t,3) disjoint positive rosters per negative roster. Thus the raw 8517600 and disjoint 4493412 pairs follow by summing t=1..4. Common-atom pairs 4024188.

Independently enumerated sorted multisets, represented each atom as a distinct bit of a BigInt mask and counted disjoint pairs. Each of the four original intervals independently matches the author GS-search count:

| negative interval | disjoint | smooth negatives | smooth disjoint |
|---|---:|---:|---:|
| [0,1024) |311048|352|41319|
| [1024,8192) |1886060|1734|172167|
| [8192,12288) |1098872|497|50463|
| [12288,16380) |1197432|882|103089|

For the maximal-prime-13 domain require 13q+r to be 13-smooth by exact trial division. Allowed residue sets for q1,q2,q3 have sizes 9,7,7 respectively (same sets as the prior q1222 audit). P=7+9*7+C(11,3)=235; N=7*C(12,4)=3465. For t distinct q1 residues, smooth negative count 7*C(9,t)*C(3,t-1), and smooth disjoint positive count 6+7*(9-t)+C(11-t,3). Raw smooth pairs 814275; disjoint 367038; common 447237. This retains about 8.17% of the literal disjoint domain. This is a justified domain reduction, not a new full lattice exclusion.

## All five disclosed witnesses
Independent BigInt extended Euclid for unit inverses; recompute for k=1..6 the signed sum of u_r*r^(-k) and vertical (13q+r)^(-k) modulo 13^k. All six residues vanish in each witness. Lexicographic roster indices match exactly. Compute vertical masses a,b, final signed side masses by adding positive or negative parts of u_r*(13r-1), squared norm sum [u_r*(13r-1)]^2 and radius squared (2331-a)^2+(2331-b)^2.

| neg,pos index | vertical masses | final masses | norm squared | radius squared | smooth pos,neg |
|---|---|---|---:|---:|---|
|2605,145|687,1438|2788,4575|3369578|3500185|yes,no|
|4487,147|713,1555|1667,5364|2991897|3220100|yes,no|
|6060,85|622,1464|2980,4679|3388851|3672370|yes,no|
|7313,377|777,1633|3615,3264|2469135|2902120|no,no|
|11629,125|713,1568|3800,3763|2944062|3200093|no,no|

Every reported witness is a valid relaxed sphere witness but exceeds at least one side budget and fails vertical smoothness. No full independent GS traversal of the 4493412 literal or 367038 smooth disjoint pairs was performed. The original author reports 9063218 GS nodes and zero budget-valid witnesses; the present review verifies the roster coverage counts and disclosed witnesses, not completeness of that execution.

## Original Result review-flow reconciliation
Consumed dvr-20261124-0559-t6-rr-c428-flow-read-v1 SUCCEEDED at source 4baa8aa3c91b2a47559cbe0c5be8c4e444fb6123, observed 2026-11-23T22:01:37.801610Z. Exact RR-C428294CF760BD8D99AA SHA256 4d2ebdb11a15bdc1a52a3baca99e8045188bc206414cb3e61b22153171359976 matches the prior artifact read. Existing operational SINGLE_REVIEW_FLOW: DR-0D8591E64A4073A61E6A, author Driver EM-DVR-FBF223, RETURN_TO_OWNER, nonterminal, destination RS-T6-P17-VERTICAL-ORDER1-EXACT-AFFINE-BUDGET, followup DFU-A781ABC4981EC521CA0B already FOLLOWUP_TASKSET_READY (publication TP2-26869C0B4D63A6BB761D). No automatic rereview required, reference passes empty. Own Driver DA-2C461358FCCA215C8753 returned execution_authorized=false in that read; the receipt grants no fresh authority. This old RR is not a container for later p17/p13 evidence. Preserve existing review and follow-up rather than repeat or overwrite; new scientific progress needs correct future Result scope and eligible independent review. No new claim/dispatch or protected write. The author q11122 is actively progressing (current GK journal search returned a further slice); preserve its independent frontier.
