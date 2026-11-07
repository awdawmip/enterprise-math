# S23/AV: permanent scaled-gap adjacency and 4,813 exact arithmetic-progression anomaly certificates

Date: 2026-11-08 (Asia/Shanghai). Status: AUTHOR_SIDE_EXACT_THEOREM_WITH_FINITE_INTEGER_CERTIFICATE; independent mathematical review pending.
Frozen scientific source: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Continuation: Draft PR #1777; exact finite precursor at e02f5504983f9cc5784c49cc86aa54c3cff89491, rotation reduction and h=219..240 at 94ed0ad01dd9156532b522de648273974a7516be.

## Experiment, carrier and future observer

The lawful two-point S23/AV auxiliary experiment has single-step three-label distributions on labels (1,3,4):

- P0=(1/2,1/4,1/4) at theta0=(1/2,1/2);
- P1=(5/7,1/4,1/28) at theta1=(5/7,7/8).

The compressed Bernoulli label-3 observer has identical probability z=1/4 at both points. For prefix joint counts (k,ell) of labels (1,4), the likelihood ratio is Lambda(k,ell)=7^(k+ell)/10^k. Label 3 pads to any length n>=k+ell. The finite-future sign observer for suffix length <=h uses the threshold set

T_h = {10^i/7^s : 0<=i<=s<=h}.

Let N(h) be the least padded prefix length whose attainable Lambda values meet every open cell between successive thresholds, including both unbounded outer cells. The extreme left threshold gives n_tail(h)=min{n>=1:7^(n+h)<10^n}. All results below refer to this exact two-point auxiliary problem.

## Theorem A: downward 7-adic scaling preserves threshold adjacency for all future h

Let h,t be arbitrary nonnegative integers. If A<B<=1 are consecutive members of T_h, then A/7^t<B/7^t are consecutive members of T_(h+t).

Proof. Both scaled endpoints belong to T_(h+t). If C=10^i/7^s from T_(h+t) lay strictly between them, multiplying by 7^t gives A<10^i/7^(s-t)<B<=1. If s<t, the middle quantity is 10^i 7^(t-s)>=1, contradiction. If s>=t, write v=s-t, so 0<=v<=h. If i>v, 10^i/7^v>1, again contradiction. Otherwise 0<=i<=v<=h, yielding a member of T_h strictly between A and B, contrary to adjacency. QED.

A finite exact 71-row integer certificate establishes that A0=10^60/7^71 and B0=1 are consecutive in T_71: for each 1<=s<=71, the largest 10^i/7^s strictly below 1 is at most A0, with equality at (i,s)=(60,71). Therefore the intervals

I_t = (10^60/7^(71+t), 7^(-t))

are adjacent open threshold cells of T_(71+t) for EVERY integer t>=0, even after h=240. This is an infinite-index exact structural theorem rather than an extrapolation from finite saturation tables.

## Theorem B: exact long 79-step return sequence and first deviation

Let A0=10^60/7^71, x=7^439/10^371, W=7^510/10^431. The integer inequalities 0<A0<x<1 and W>1 hold. For v>=0 write K(v)=min{k>=0:7^(k+v)<10^k}, and R(v)=7^(K(v)+v)/10^K(v). Then R(v) belongs to (A0,1) exactly when v can be a first-below-1 prefix witness for the base gap.

The exact finite seed certificate (all v=0,...,146) proves:
- v=0,...,67: R(v)<=A0;
- v=68: K(68)=371 and R(68)=x;
- among v=69,...,146, the maximum R(v) is x^2 at v=136 with K(136)=742;
- the next largest value in this range occurs at v=125 with K(125)=682.

For m>=0, v in [68,146], and k=K(v), the exact identity

Lambda(k+431m,(v+79m)-(k+431m)) = R(v) W^m

is simply the exponent law 7^(v+k+510m)/10^(k+431m)=R(v)W^m; here the displayed second argument denotes the label-4 count, whereas v+79m is the total non-3 count. More directly, for each total non-3 count v'=v+79m, its candidate first-below-one k'=K(v)+431m has ratio R(v)W^m. The candidate is indeed K(v') for m<=4813: R(v)W^m<=x W^4813<1, while its predecessor k'-1 has ratio >=1, by K(v)'s minimality and W>1.

The following four large comparisons are EXACT integer comparisons (no logarithms):

(1) 7^(439+510*4813) < 10^(371+431*4813), i.e. x W^4813<1.

(2) 7^(949+510*4812) < 10^(802+431*4812), i.e. x^2 W^4812<A0.

(3) 7^(949+510*4813) > 10^(802+431*4813), i.e. x^2 W^4813>A0.

(4) 7^(878+510*4813) < 10^(742+431*4813), proving the second-largest seed ratio (v=125) stays below A0.

It follows that ALL returns R(v) in (A0,1) up to v=380294 occur exactly at

v_m=68+79m, K(v_m)=371+431m, 0<=m<=4812.

The next return is v_4813=380295; an additional non-79-aligned return occurs at v=380363, whose seed residue is 136 (not 68). Thus the exact 79-step pattern survives 4,813 consecutive return positions, and its first deviating gap is 68, occurring between 380295 and 380363. This proves a long finite periodic window and an exact transition, not a periodicity assertion for all v.

The only finite scan in the proof is v<=146 (plus the 71 base-adjacency rows); all m<=4813 are handled by monotonicity and four endpoint power comparisons.

## Theorem C: 4,813 strict finite-horizon anomalies with a uniform excess of 116

For each integer m=0,...,4812 set

h_m=140+79m, t_m=h_m-71=69+79m.

By Theorem A, I_(t_m) is an open adjacent cell in T_(h_m). To enter this cell, a prefix with total non-3 count s and label-1 count k must satisfy

A0 < 7^(s+t_m)/10^k < 1.

Write v=s+t_m. Because t_m=v_m+1 and the next return is v_(m+1)=147+79m, Theorem B gives the first possible v and its unique smallest k=802+431m. Therefore the shortest prefix entering I_(t_m) has exact length

F(t_m)=(147+79m)-(69+79m)+(802+431m)=880+431m.

Consequently N(h_m)>=880+431m. Its extreme-tail bound is exactly

n_tail(h_m)=764+431m.

For this, at n=764+431m the ratio 7^(n+h_m)/10^n equals (7^904/10^764)W^m, increasing with m because W>1. It is <1 at the last m=4812 by the exact integer comparison 7^(904+510*4812)<10^(764+431*4812). At n-1, the corresponding ratio starts >=1 at m=0 by 7^903>=10^763 and increases with m. Monotonicity in n then establishes the exact n_tail formula.

Thus for EVERY integer 0<=m<=4812:

N(140+79m) >= 880+431m = n_tail(140+79m)+116.

There are 4,813 distinct certified horizons, from h=140 through h=380288. In particular the previously uncomputed h=298 satisfies N(298)>=1742, while n_tail(298)=1626. This is a rigorous lower bound for N, not an exact determination of N at every listed h.

## Machine-checked verification and limitations

VERIFY.py uses only Python standard-library big integers and Fraction. It checks every base-row adjacency comparison, all k-minimality and ranking claims for v<=146, and the large integer boundary comparisons. Its actual stdout is preserved in RUN_EVIDENCE.txt. Mathematical quantification over all t>=0 in Theorem A is by the analytic argument. The long arithmetic family of Theorems B/C is derived from finitely many exact comparisons and monotonic exponent identities.

BRC resolution: REUSE_APPLIED. The carrier retains the joint count pair (#label1,#label4), with the label-3 padding source, and the declared future operation is a likelihood-sign test for suffixes of length <=h. Bernoulli-z compression erases this joint relation; threshold cells are a scope-typed finite-future sign observer, not a universal replacement for full ordered statistics. The underlying Heartbeat X6/P000 basis remains unchanged. This is author-side mathematics; formal native CLAIM/Owner/Research-Activity and independent review require their own current authority/verification.

## Next exact questions

1. Determine whether infinitely many h satisfy N(h)>n_tail(h), now that 4,813 separate horizons are certified, using Diophantine approximations to ln(7)/ln(10/7) and the return-time structure.
2. Investigate whether N(298)=1742 by a full finite occupancy certificate, or identify a different last gap.
3. Resume the independent full-lawful delta_4 minimax equality problem and six-source ten-label mother-model bridge without conflating them with these two-point sign-observer claims.
