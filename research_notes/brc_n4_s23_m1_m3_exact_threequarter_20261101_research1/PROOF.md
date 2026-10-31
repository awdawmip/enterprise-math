# BRC N=4 / S23: exact 3/4 plateau for one to three policy labels

2026-11-01. AUTHOR-SIDE EXACT FINITE PROOF + EXECUTED INTEGER CHECKS; UNREVIEWED / NOT_ADMITTED. External six-latent-source BRC information-theory model, not P000 native X6 dynamics.

## Model and statement

The latent sources AU0, AU1, AV, BU0, BU1, BV have six prepared positive P/Q mixture rows

    M=(1/20)*[[10,10,0,0,0,0],[9,11,0,0,0,0],
              [0,0,20,0,0,0],[0,0,0,10,10,0],
              [0,0,0,2,18,0],[0,0,0,0,0,20]].

An S23 behavioral policy controls two first-stage A/B stops, three second-stage U(shared AU/BU)/AV/BV stops, and six third-stage source-specific stops. The observable is only T in {1,2,3,4}; 2^11=2048 deterministic tables are legal. A row-stochastic 6-by-k encoder E is fixed before the policy H; at most m fixed row-stochastic k-by-4 decoders D_l are selected by an advance policy label. No realized hidden cell, random coin, or full policy is available to the decoder after its label is selected. Let

    R_beh(k,m) =
       inf_(E,D_1,...,D_m) sup_(H legal S23 behavioral)
       min_(1<=l<=m) max_(1<=i<=6)
       TV( (M F_H)[i,:], (M E D_l)[i,:] ).

NEW THEOREM: for every integer k>=1 and 1<=m<=3,

    R_beh(k,m) = 3/4.

Combined with the previously established PRECISE BRC N4/S23 result for 4<=m<=9 (PR #1757, immutable 6a78eef...), the first nine finite policy-label cases are closed for every k:

    1 <= m <= 3: 3/4;    4 <= m <= 9: 2/3.

## Uniform upper bound (all randomized S23 policies)

One common encoder state and one fixed decoder q=(1/4,1/4,1/4,1/4) achieve error <=3/4 against every four-time probability law p: TV(p,q)=1-sum_t min(p(t),1/4)<=3/4. At least one p(t)>=1/4, so the overlap is at least 1/4. Additional states or labels can remain unused.

## Exact lower bound (arbitrary real stochastic encoders)

Consider the lawful deterministic policies where AU0/AU1 have the same stop time, and BU0/BU1 have the same stop time. Then the four provenance-group timing signature s=(AU,AV,BU,BV) is a four-tuple of point masses. Its EXACT legal signature set S64 is the disjoint union

    C0={(1,1,1,1)}                                               [1]
    C1={(1,1,x,y): x,y in {2,3,4}}                                [9]
    C2={(x,y,1,1): x,y in {2,3,4}}                                [9]
    C3={(2,x,2,y): x,y in {2,3,4}}                                [9]
    C4={(x,u,y,v): x,y in {3,4}, u,v in {2,3,4}}                  [36]

of size 64. A separate enumeration of all 2048 legal S23 deterministic tables verifies that the designated-cell signature set is S64. For each such signature, choosing the two un-designated AU0/BU0 terminal bits equal to their designated counterparts realizes its four-group point-mass policy. Since AU and BU within-group sources agree, mixing by M preserves the point masses for all six prepared rows.

Fix one label l, and for each group choose a particular prepared-row output q_(j,l), for j in {AU,AV,BU,BV}. The common encoder/label decoder induces the SAME q_(j,l) for every policy assigned that label. If it reconstructs a point-mass signature s with error STRICTLY LESS than 3/4 then

    1 - q_(j,l)(s_j) < 3/4  =>  q_(j,l)(s_j) > 1/4

for every group j. Four different output times cannot all have probabilities strictly exceeding 1/4, so for each j at most three times can occur among signatures served by the label. Therefore the label's signature set is contained in a four-coordinate Cartesian box with three choices per coordinate. Each 3-element subset of {1,2,3,4} is characterized by its excluded time, yielding 4^4=256 maximal candidate boxes.

EXACT THREE-BOX LEMMA: no union of three of these 256 boxes contains all of S64. Their maximum possible coverage is exactly 63 out of 64. The certificate exhaustively visits ALL binomial(256,3)=2,763,520 distinct unordered triples of 64-bit incidence masks, testing union versus the 64-bit full mask. A particular tight triple of excluded-time four-tuples is (1,1,1,1),(1,1,2,2),(2,2,1,1); this triple misses precisely the legal point (1,1,1,1). Four boxes sufficing for S64 are the diagonal exclusions (t,t,t,t), t=1,2,3,4: every legal S64 signature has at most three different times. The checker verifies both tightness and the four-box coverage.

Hence if at most three labels attained a global risk strictly below 3/4, each of 64 legal witnesses would need an assigned label whose witnesses fit one of three boxes. The three-box lemma excludes this. This conclusion is POINTWISE for every arbitrary real stochastic common E and every label-conditioned stochastic D_l, independent of k. Combined with the explicit uniform decoder, it proves the exact minimax equality including the infimum.

## Executed arithmetic and interpretation

VERIFY.js independently enumerates all 2048 legal deterministic S23 tables, derives S64, builds all 256 3-choice boxes using BigInt incidence bits, checks 2,763,520 unordered triples without pruning, verifies maximum coverage 63, and checks the four diagonal boxes. VERIFY_INDEPENDENT.py independently builds masks with a different signature ordering and confirms the same exhaustive maximum using Python arbitrary-precision integers and bit counts. RUN_EVIDENCE.txt is the observed output of both actual runs. No solver tolerance, random sampling, unverified floating-point assertion, or third-party dependency enters this proof. Mathematical quantifiers over REAL encoders and ALL behavioral strategies follow from the analytic lower and upper inequalities, not extrapolation of finite tests.

BRC typing: six positive latent likelihood-ratio cells with provenance, mixture M, future lawful causal stopping, observable T, and retained maximum-TV residual. The six cells are not six P000 native spatial axes; the four abstract stopping-time atoms are not a physically calibrated Heartbeat time axis. P000 V5, ACTIVE worldview, X6/independent-time constraints and observer-future-operation preservation remain governing research assumptions. No S2, native X6 physical-fidelity, signed BRC or project admission theorem is asserted.

Frozen same-run controls: GLOBAL_KNOWLEDGE_V1 main@c410eb8f62117dbf2b65815700982ea78a17495a; Enterprise Math main@21e7eb7b7d8d93cd11b957f0c6ba1ffb904a9fb2. The project's current portable research protocol was read. The new result is author-side / UNREVIEWED / NOT_ADMITTED, with native owner query CONTROL_QUOTA and research_authority_granted=false at the observed service snapshot.

Exact predecessors: PR #1757, time-only 64 signature / nine-label certificate at 6a78eef5487058815d600ae2b53c3f52d957c1aa, deterministic full 2048-policy lift at 063c8e1f35c95a1644c55f28ca42b35b67a1b9da, and PR #1763 full-policy-informed storage curve at 2fd3279dd290ae9cc3b1db711161747c0154b4c5. This finite-label theorem is separate from policy-informed unlimited decoder results.

## Remaining specific problems

The k=4 and k=6 FULL BEHAVIORAL finite ten-label risk remains in [1/2,2/3]. The next unit is a finite exact rational mixed-policy witness/certificate for its strictness or a universal fixed-kernel ten-label construction. Preserve independent audit, S2 transfer and native P000 X6/independent time fidelity as separate obligations.