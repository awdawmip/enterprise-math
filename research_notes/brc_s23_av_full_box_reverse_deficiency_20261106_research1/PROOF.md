# S23/AV: sharp global reverse deficiency of the entire lawful two-control box

Date: 2026-11-06. Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34. Status: AUTHOR_ANALYTIC_PROOF / EXACT_RATIONAL_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Exact model and quantifiers

Retain all six tagged positive-source preparations AU0, AU1, AV, BU0, BU1, BV and their common A/B second-stage parameter b, in the lawful box Q=[1/2,7/8] x [1/8,1/2] x [1/2,7/8] for (a,b,c). In this theorem **only the conditional AV observation** is read, for one four-stop trial; its stop2 mass is identically zero.

A_(a,c)=(a,z,1-a-z), z=(1-a)c on (stop1,stop3,stop4).
B_(a,c)=(z,1-z) on (yes=stop3,no=otherwise).

Let K range over all single hypothesis-independent row-stochastic kernels {yes,no}->{stop1,stop3,stop4}. The single kernel must serve **all real** (a,b,c) in Q. Let TV(P,Q)=sum_j |P_j-Q_j|/2 and

delta_box(A|B)=inf_K sup_(a,b,c) in Q TV(A_(a,c),B_(a,c)K).

## Theorem: exact all-real full-box reverse deficiency

**delta_box(A|B)=9/70**, attained by the explicit rational stochastic kernel

K(yes)=(0,1,0), K(no)=(88/105,0,17/105).

Both the uniform upper bound and a sharp binary Bayes-risk lower bound have exact witnesses.

### Upper certificate for the full continuum

Put v=88/105. Applying K to B reconstructs

B_(a,c)K=(v(1-z),z,(1-v)(1-z)).

Its signed first-coordinate error is E(a,c)=v[1-(1-a)c]-a; the stop3 error vanishes and the stop4 error is -E. Hence TV(A,BK)=|E(a,c)|. E is affine in each of a,c separately. Every point of the closed rectangle [1/2,7/8]^2 is a convex combination of its four vertices with nonnegative product interpolation weights; E at that point is the same weighted combination of vertex errors. Thus |E| is at most the largest absolute vertex error.

At (a,c)=(1/2,1/2), (1/2,7/8), (7/8,1/2), (7/8,7/8), respectively, the exact E values are

9/70, -1/35, -5/56, -9/70.

It follows that TV(A,BK)<=9/70 over the entire real box, with equality at the first and last vertices. In particular delta_box<=9/70.

### Lower certificate: two lawful hypotheses, one binary decision problem

Fix the same lawful b on both hypotheses, e.g. b=1/8. Let H_low=(a,c)=(1/2,1/2) and H_high=(a,c)=(7/8,7/8). Their AV distributions are

A_low=(1/2,1/4,1/4), A_high=(7/8,7/64,1/64);

B_low=(1/4,3/4), B_high=(7/64,57/64).

Put prior t=P(H_high)=16/35. For the optimum binary zero-one hypothesis test, R(P_low,P_high;t)=sum_i min{(1-t)P_low(i), t P_high(i)}. Direct exact arithmetic yields

R_A=23/70, R_B=16/35, R_B-R_A=9/70.

For any row-stochastic K, write e=max_h TV(A_h,B_hK). Take a Bayes-optimal A-decision rule, and simulate it on the B-observation by first applying K. Under each hypothesis, the expected 0-1 loss changes by at most e by the TV variational inequality. Hence R_B<=R_A+e, so e>=9/70. Each candidate K has sup_Q TV>=e>=9/70. Taking inf_K gives delta_box>=9/70. The constructed kernel attains the lower bound. QED.

## Consequences and precise scope

Every finite-action decision problem with loss bounded in [0,1] and prior supported on this conditional AV family can be simulated by B with excess optimum Bayes risk at most 9/70. The displayed two-corner binary decision problem attains that bound. Therefore the sharp deficiency is already visible to a two-state test, even though the kernel is universal over the continuum.

The predecessor PR #1776 established a different, pair-specific exact deficiency <=1/14 when a is FIXED and only c changes (and the optimizing kernel may depend on that fixed pair). The present uniform inf_K sup_(a,c) theorem varies both a and c and has sharp value 9/70. Both results hold in their stated quantifier order.

BRC use: source provenance and the legal common b are retained; the deterministic AV stop3 projection removes the stop1/stop4 distinction, with exact 9/70 worst-case recoverable risk penalty for this conditional row. The reverse K is decision-side randomization, **not** a lawful source-policy or encoder change. The legal joint ten-label S23 decoder/encoder bridge and mother minimax order remain to be investigated. Previously recorded R_beh(k,10) in [1/2,2/3] for k=4,6 is unchanged by this source-conditional calculation.

## Exact verification

The actual Python standard-library fractions.Fraction checker executed 60 exact assertions: kernel rows/stochasticity, four corner signed errors and TV, sharp corners, precise Bayes-risk dual, and a supplementary 25-point rational grid. Universal real coverage follows from the analytic multiaffine vertex proof, not finite sampling. VERIFY.py and RUN_EVIDENCE.txt contain reproducible code and actual stdout. Formal CLAIM/owner, independent review and mathematical admission are separate from author proof.
