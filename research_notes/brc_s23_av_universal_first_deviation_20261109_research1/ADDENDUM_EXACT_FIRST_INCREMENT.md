# S23/AV universal first nonlinear increment — exact next-return identity

Date: 2026-11-09 (Asia/Shanghai).
Status: AUTHOR-SIDE COMPLETE ELEMENTARY PROOF; independent mathematical review pending.
Frozen science: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Dependencies: PROOF.md in this directory (the universal first-deviation theorem) and the predecessor's exact Bayes-risk partition formula at commit 540863cb933fe4c5b76523c08f5379fe04b66d8f.
Domain: auxiliary circle-partition model for any irrational real rotation angle theta and uniform phase. Applies to the frozen S23/AV 79-symbol observer by its exact readout correspondence. No native X6 geometric or heartbeat-dynamics promotion is asserted.

## Stronger exact theorem

For any irrational theta, any m>=1, and the circular partition P_n with cuts t_j={-j theta} (0<=j<n), define

  R(m,L)=1-sum_(old cells I in P_m) max_(new cells J in P_{m+L} inside I) |J| .

Let delta=min_{1<=d<=m} ||d theta|| and let
  q=min{n>m: ||n theta||<delta}.
(The q exists by density of an irrational rotation.) Then for integer horizons:

  R(m,L)=L*delta                         (0<=L<=q-m);
  R(m,q-m+1)=(q-m)*delta+||q theta||.   (*)

In particular, the first deviation is at L=q-m+1 and its EXACT incremental risk is

  R(m,q-m+1)-R(m,q-m)=||q theta||<delta.

This strengthens PROOF.md's previous upper bound on the first increment to equality. Both equations are valid for every irrational theta and every m>=1.

## Exact proof of (*)

Write eta=||q theta||, so 0<eta<delta<1/2. Choose an integer d in [1,m] attaining ||d theta||=delta. By definition of q, all positive integer k<q satisfy ||k theta||>=delta (for k<=m this follows from delta's definition, and for m<k<q from q's minimality).

**1. Opposite orientations.** Let the signed nearest-integer residues of d theta and q theta be s_d and s_q. Thus |s_d|=delta, |s_q|=eta, each in (-1/2,1/2). If s_d and s_q had the same sign, the signed residue of (q-d)theta would have absolute value delta-eta<delta. Since 1<=q-d<q, this contradicts the preceding minimality. Consequently s_d and s_q have opposite signs.

**2. A distinguished gap in P_q.** Because t_j={-j theta}, the circular displacement from t_0 to t_q has length eta in one direction. In that same direction, t_{q-d}=t_q-t_d has displacement eta+delta from t_0: the signs oppose, so the displacements add. As eta+delta<1, the arc t_0 -> t_q -> t_{q-d} is unambiguous and its successive lengths are eta and delta. Both endpoints t_0 and t_{q-d} belong to P_q, while t_q is the new cut to be inserted.

Every two distinct cuts among t_0,...,t_{q-1} have circular distance at least delta: their index difference is an integer k with 1<=k<q. If there were any other old cut strictly between t_0 and t_{q-d} on that length-(eta+delta) arc, at least one of its two distances along the arc to these endpoints would be less than delta, because eta+delta<2delta. This contradicts the pairwise separation. Therefore the arc is one genuine P_q gap G, length |G|=delta+eta; inserting t_q splits G into exactly two gaps of lengths eta and delta.

**3. The gap G wins its old parent cell.** The already-proved all-index linear segment gives
  R(m,q-m)=(q-m)delta.
But in P_q, every gap has length at least delta. Within each original P_m cell that contains r refined P_q gaps, its risk contribution is the sum of the r-1 gap lengths after excluding one longest gap. Each excluded-gap complement has lower bound (r-1)delta. Summing over old cells gives lower bound (q-m)delta. The proven equality forces every non-longest gap of every original P_m cell to have length exactly delta. Since G has length delta+eta>delta, it must be a longest gap in its original parent cell (indeed the only gap longer than delta). Thus the old winning length in that parent cell equals delta+eta.

**4. Exact change when t_q arrives.** Only G is split. After inserting t_q its two pieces have lengths eta<delta and delta, and all other gaps of its parent have length delta (by step 3). The winning length in that original cell therefore falls from delta+eta to delta, exactly eta. All other P_m cells are unchanged. By the defining Bayes-risk formula, the risk increases by eta=||q theta||, proving (*).

QED.

## Certified frozen S23/AV cases

Theta is the original S23/AV irrational number:
  theta=79*(2074774-380295*r)/(79*r-431)-46, r=ln(7)/ln(10/7).
Reuse the predecessor's proved strict enclosure
  262204504569236716045286 / 10^24 < theta <
  262204504569236716045287 / 10^24.
The script VERIFY_FIRST_DEVIATION.py now **asserts equality** of the direct partition risk increment with the certified next record-return distance, for m in
  1,3,4,19,42,61,128,200,553,717.
All ten pass. The earlier RUN_EVIDENCE.txt remains byte-for-byte the actual printed output, because the strengthened assertion produces the same displayed values.

For m=128: d=61, delta=16-61theta, q=164, eta=164theta-43.
Thus R(128,L)=L(16-61theta) for L=0,...,36 and
  R(128,37)=36(16-61theta)+(164theta-43)=533-2032theta.
For the distinct m=61: q=164, last linear horizon L=103 and first nonlinear at L=104 with increment 164theta-43.

## Further research

The first-deviation and exact first incremental loss are solved for all irrational rotations. Next, determine the complete sequence of breakpoints and affine formulas for R(m,L) beyond the first return, using continued fractions and three-gap refinements. In parallel, plateau 413 remains a separate exact S23/AV geometric critical-cell coverage problem under its frozen checker. A proof of the observer risk identity is not a covering certificate.
