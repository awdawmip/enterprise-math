# S23/AV finite-horizon risk: exact 13-block law, flat intervals and restarted increases

Date: 2026-11-09 (Asia/Shanghai).
Researcher-ID: EM-DIRECT-49267F; Research-Activity-ID: RA-9FC3E745CF6CCE3861604A1F.
Status: AUTHOR-SIDE EXACT FINITE CERTIFICATE and elementary general insertion lemma. Independent review pending.
Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Source dependencies: prior S23/AV finite-horizon Bayes-risk identity at commit 540863cb933fe4c5b76523c08f5379fe04b66d8f; first-return theorem and exact increment at commit 3a9e51046643d77cadd5ce40ed7a5367289ded4b.
Scope: auxiliary irrational circle observer induced from the frozen S23/AV 79-state readout, with uniform initial phase. No native X6 geometry or heartbeat law is asserted.

## Definitions

Fix irrational theta with 0<theta<1. For j>=0, write t_j={-j theta}. Let P_n be the circular partition whose cuts are t_0,...,t_(n-1). For m>=1, L>=0 define

  R(m,L)=1-SUM_(I in P_m) MAX_(J in P_(m+L), J subset I) length(J).

This is exactly the minimum probability (under uniform initial phase) that a forecast of the entire next L-symbol block makes at least one error, when its input is the previous m symbols, by the predecessor's observer-partition equivalence.

## General exact insertion lemma (all irrational theta; all m>=1 and L>=0)

When advancing from P_(m+L) to P_(m+L+1), the new cut t_(m+L) splits a unique subgap G of some original P_m cell into lengths a>0, b>0, with g=a+b. Let B be the maximum length of OTHER refined subgaps in that SAME original cell, or B=0 if no other such gap. Then

  R(m,L+1)-R(m,L)
    = max(B,g)-max(B,a,b)
    = max(0, min(a,b,g-B)).

In particular the increment is zero exactly when B>=g, and is positive exactly when G was strictly longer than the other subgaps of its original history cell.

Proof: For every original cell other than the one containing G, the longest refined gap does not change. For the affected original cell, the maximum before insertion is max(B,g) and after is max(B,a,b). Subtracting these two maxima gives the first formula. Since a+b=g, separating the cases B>=g and B<g gives the second formula. QED.

The lemma supplies a local update rule for a fully observed parent-cell gap partition and makes flat increments mathematically transparent.

## Exact frozen S23/AV finite theorem

Use the previously certified strict rational enclosure

  P/Q < theta < (P+1)/Q,
  P=262204504569236716045286, Q=10^24.

For m=128 and every integer 1<=L<=1142, the EXACT difference
  D_L=R(128,L)-R(128,L-1)
is constant on the following THIRTEEN disjoint exhaustive blocks. All values are exact affine expressions in the true irrational theta:

| L inclusive | D_L |
| --- | --- |
| 1..36 | 16-61 theta |
| 37..164 | -43+164 theta |
| 165..200 | 0 |
| 201..328 | -43+164 theta |
| 329..364 | 0 |
| 365..425 | -43+164 theta |
| 426..492 | 145-553 theta |
| 493..528 | 0 |
| 529..589 | 145-553 theta |
| 590..978 | 0 |
| 979..1045 | -188+717 theta |
| 1046..1081 | 0 |
| 1082..1142 | -188+717 theta |

Consequences:
  R(128,590)=R(128,978)=5505-20992 theta,
  R(128,1142)=-18559+70784 theta,
  D_165=0 < D_201=-43+164 theta,
  D_36=16-61 theta > D_37=-43+164 theta >0.

Hence L -> R(128,L) has both rising and declining first differences; it is neither discretely concave nor discretely convex throughout L=0,...,1142. Moreover the 389 consecutive increments L=590,...,978 all vanish, and later increments resume. This is a precise observer-horizon fact, useful for residual-memory forecast design.

## Exhaustive certificate and reproducibility

VERIFY_RISK_BLOCKS.py is a complete exact enumeration of EVERY n=128,...,1270 and all its circular P_n gaps. It computes each cut as the symbolic affine pair (ceil(j theta),-j), with t_0=(0,0); the floor at both endpoints of the strict enclosure is checked to agree for every j<=1269. All circular ordering claims are certified by strict integer inequalities at the interval endpoints. It computes the exact affine gap lengths, verifies positivity, and for every original P_128 cell certifies the chosen largest gap against ALL competing gaps by strict disjoint rational-interval bounds (allowing identical affine pairs). It sums these parent maxima to obtain R(128,L) for each of the 1143 horizons and checks each exact difference against the 13-block law; all comparisons are integer-only and uniform for every theta in the enclosure.

The numerical enclosure of theta is inherited from the cited predecessor's certified logarithmic interval derivation; the present proof verifies a new finite identity conditional on that exact inherited bound. RUN_EVIDENCE.txt is the actual complete checker output.

## Interpretation and unresolved work

This result extends the first-deviation theorem from a single transition to the entire finite horizon L<=1142. The local lemma holds generally, and the table is a bounded exhaustive exact theorem. Next: derive a continued-fraction/three-gap recurrence that generates the same blocks without a fresh partition scan per horizon; test a prediction of the next nonzero increment after L=1142. Another independent branch remains S23/AV geometric critical-region coverage for plateau 413, using its own frozen checker and scope.
