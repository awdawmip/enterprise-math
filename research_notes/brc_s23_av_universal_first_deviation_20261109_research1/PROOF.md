# S23/AV: universal exact first deviation of finite-horizon Bayes risk

Date: 2026-11-09 (Asia/Shanghai).
Status: AUTHOR-SIDE MATHEMATICAL PROOF; integer-only finite checks passed; independent review pending.
Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Immediate predecessor: research_notes/brc_s23_av_finite_horizon_bayes_20261109_research1/PROOF.md at 540863cb933fe4c5b76523c08f5379fe04b66d8f.
Model scope: external auxiliary 79-symbol S23/AV irrational circle observer with uniformly distributed initial phase. This is an observer-level result; native X6/heartbeat operations remain separately typed.

## Definitions and inherited exact identity

Take any irrational real theta, not only the frozen S23/AV value. For m,L >= 1, let t_j = {-j theta}, with t_0=0, and let P_n be the circular partition of [0,1) by t_0,...,t_{n-1}. For an old P_m cell I, let J(I) range over the refined cells of P_{m+L} contained in I. Define

R(m,L) = 1 - sum_{I in P_m} max_{J in J(I)} |J|.

For the actual S23/AV auxiliary observer, theta=79 alpha-46, alpha=(2074774-380295r)/(79r-431), r=ln(7)/ln(10/7). The predecessor proved this R is the minimum probability of at least one mistake when forecasting a whole future L-symbol block from m past symbols under uniform phase. The following theorem works for any irrational theta for which this partition model applies.

Write ||x|| for distance to the closest integer and define the record distance

e_m = min_{1<=d<=m} ||d theta|| > 0,

and the next strict record-return denominator

q(m) = min{q>m: ||q theta|| < e_m}.

Dirichlet approximation (or irrational-rotation density) ensures that q(m) exists.

## Theorem — exact entire linear segment and its first departure

For every irrational theta and all integers m>=1:

(A) For every integer L>=1,
    0 <= R(m,L)-R(m,L-1) <= e_m, where R(m,0)=0.

(B) For every integer 0<=L<=q(m)-m,
    R(m,L) = L e_m.

(C) At the very next horizon L*=q(m)-m+1,
    0 <= R(m,L*)-R(m,L*-1) <= ||q(m) theta|| < e_m.
    In particular R(m,L*) < L* e_m, and L* is the EXACT FIRST
    horizon at which the identity R(m,L)=L e_m fails.

Equivalently: if q_s<=m<q_{s+1} are consecutive strict record-return denominators of ||d theta||, then the last linear horizon is q_{s+1}-m and the first failure horizon is q_{s+1}-m+1.

### Proof

1. (Single-insertion upper bound.) Let n>=m. Adding t_n splits exactly one current subgap, say G, of some original P_m cell into two pieces of lengths a,b>0. Its old local maximum M becomes M' after replacing a+b by a,b. Every other old P_m cell is unchanged; therefore 0<=R(m,n-m+1)-R(m,n-m)=M-M'<=min(a,b). Select d in 1,...,m with ||d theta||=e_m. The already present point t_{n-d} (n-d>=0) is at circular distance e_m from t_n. Along the shorter arc between them there may be intervening cutpoints, but the nearest existing cutpoint on that side is within e_m. Consequently min(a,b)<=e_m. This proves (A).

2. (Uniform lower bound before next record.) Set N=m+L<=q(m). For any two distinct cutpoints t_i,t_j of P_N, their circular distance is ||(i-j)theta||>=e_m, because 1<=|i-j|<=N-1<q(m) and q(m) is the FIRST strict improvement beyond m. In particular, every gap between consecutive P_N cutpoints is at least e_m. Inside an old P_m cell containing r>=1 refined subgaps, its contribution to R is the sum of all except one longest subgap; hence it is at least (r-1)e_m. The sum of (r-1) over old cells is exactly L because each of the L newly inserted cutpoints adds one subgap. Thus R(m,L)>=L e_m. Part (A) telescoped from R(m,0)=0 gives the reverse inequality, so (B) follows.

3. (First strict improvement.) Put q=q(m) and insert the point t_q. The old cutpoint t_0 is at circular distance ||q theta||<e_m from t_q and is already in the partition. Repeating the single-insertion argument with this PARTICULAR old point gives 0<=R(m,q-m+1)-R(m,q-m)<=||q theta||<e_m. This is (C). QED.

This proof is exact, with no floating-point assumptions or finite-search extrapolation. It identifies the first deviation for every m by the next strict return of theta, thereby resolving the predecessor's first-deviation question as a universal auxiliary-circle theorem.

## Frozen S23/AV exact consequences

The existing certified strict rational bound is
P/Q < theta < (P+1)/Q,
P=262204504569236716045286, Q=10^24.
The original log-series proof of this enclosure is inherited from the predecessor's cited materials; this note does not replace its derivation.

For m=128, the exact best return is d=61, with
e_128=16-61 theta, and q(128)=164.
Thus universally for this frozen theta:

R(128,L)=L(16-61 theta)  for all integers 0<=L<=36,

and the first departure is EXACTLY L=37. The predecessor's verified finer value
R(128,37)=533-2032 theta
agrees. The incremental loss at 37 is 164 theta-43 < 16-61 theta.

The same first-deviation rule is certified for m=1,3,4,19,42,61,128,200,553,717 by the integer-only VERIFY_FIRST_DEVIATION.py, which recomputes both partition risks directly. Full output is in RUN_EVIDENCE.txt. These finite certificates validate the worked coordinates; the theorem for all m and all irrational theta follows from the proof above.

## Impact and next question

The horizon at which the best finite-history forecast ceases to accumulate constant per-step error is controlled EXACTLY by the next strict Diophantine return. This makes the first nonlinear threshold computable from the continued-fraction record sequence without running repeated horizon partitions.

A stronger candidate, supported in all ten checked S23/AV cases, is that the first incremental loss equals ||q(m)theta||, not merely that it is at most this amount. Prove or produce a counterexample for general irrational theta and m. Also investigate whether the resulting return-time classifications transfer any geometric critical-cell covering witness for plateau 413; those covering claims require their own exact geometric certificate.
