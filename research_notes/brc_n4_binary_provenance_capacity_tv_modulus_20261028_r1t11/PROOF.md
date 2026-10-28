# BRC N4 — Binary provenance capacity walls: exact all-policy TV bounds

2026-10-28. Author-side derivation, UNREVIEWED / NOT_ADMITTED. Exact control snapshot: GLOBAL_KNOWLEDGE_V1 main@3b7e06025122de7ed30ee8c0521c36b8607b68eb; Enterprise Math frozen scientific input main@48646138c85602b8a9eec46ac6bc47da25e67e15. Predecessor: research_notes/brc_n4_binary_provenance_zero_phase_20261028_r1t11/PROOF.md at Enterprise Math commit 9e83fc5d85159bf95cc51138e3da34a1843f0282.

## Finite BRC model and scope

Use exactly the predecessor's strictly positive two-law N=4 tree: at t1 the A/B Q masses are (1/2,1/2) and P/Q ratios are (1/2,3/2); at t2 AU,AV,BU,BV have (Q mass, P/Q)=(1/6,1),(1/3,1/4),(1/4,1),(1/4,2), with strictly positive mass-preserving tail splits. The full-history strategy F(a,b,cA,cB) continues at t1 A/B with rates a,b, otherwise stops Q; continues at t2 AU/BU with cA,cB, otherwise stops Q; at t3 stops P only below AU, otherwise Q; at t4 stops Q. All real parameters 0<a,b<=1, 0<=cA,cB<=1.

S2 comprises every causal randomized strategy with shared complete (stop-P,stop-Q,continue) probabilities at AU/BU at t2, permitting changes everywhere else including early stopping and future relabeling. S23 additionally merges same-likelihood-ratio t3/t4 actions. Z_H records whether prefix H=AU or BU reached t3. The observable is the full joint (T,decision,Z_H); define dJ^H(F)=inf_{G in SJ} max(TV_Q(O_H(F),O_H(G)),TV_P(O_H(F),O_H(G))). Then S23 subset S2.

## Theorem: explicit capacity-violation modulus

Set r=b/a, R=a/b and [v]+ = max(v,0). Define

C_QA=max((4+6r)/7,8/7), C_PA=max(2/3,(6r+4)/21),
C_QB=(3+2R)/7+max(1/7,(2R+3)/28),
C_PB=max(4/7,(2R+3)/14).

For ALL real parameters above, all allowed causal randomized competitors, and either binary observer,

d2^AU >= [3b(cB-cA)-7a]+ / [21(C_QA+C_PA)],
d2^BU >= [2a(cA-cB)-7b]+ / [28(C_QB+C_PB)],

d23^H >= d2^H, and
d23^H <= U := (a/6)(b/4)|cA-cB|/(a/6+b/4).

Exact rational capacity-wall witnesses:

AU tag: F=(1/20,1,0,1): 53/9920 <= d2^AU <= d23^AU <= 1/124.
BU tag: F=(1,1/20,1,0): 33/6020 <= d2^BU <= d23^BU <= 1/86.

These are proved bounds, NOT exact minimax values. The bounds quantify the strict-positive capacity-wall regime of the predecessor's exact zero-loss classification; they do not exhaust opposite-direction positive-loss mechanisms.

## Proof of lower bounds, including arbitrary future behavior

Fix G in S2. Denote its t1 A/B continuation rates a',b', its common t2 AU/BU continuation rate c in [0,1], and its t2 AV/BV continuation rates u,v. The conditional Q mass continuing from AV/BV is x=a'u/3, y=b'v/4, whence x<=a'/3 and y<=b'/4. No assumption is imposed on other G decisions or later actions.

Let all differences be F minus G, and use measurable events in the declared joint observation:

s=Q(T=1)_F-Q(T=1)_G=(a'-a+b'-b)/2,
t=P(T=1)_F-P(T=1)_G=(a'-a+3(b'-b))/4,
zq=Q(T=2)_F-Q(T=2)_G,
zp=P(T=2)_F-P(T=2)_G,
hA=Q(Z_A=1)_F-Q(Z_A=1)_G=(a cA-a'c)/6,
hB=Q(Z_B=1)_F-Q(Z_B=1)_G=(b cB-b'c)/4.

T=1 and T=2 sum over BOTH stop decisions. The tag event is fixed once its prefix reaches t3 and hence is independent of future decisions. With m=a cA/6+b cB/4-a'c/6-b'c/4, Q/P t2 stopping mass conservation yields

x+y=m+s+zq, x/4+2y=m+t+zp.

Thus x=(4m+8s-4t+8zq-4zp)/7,
y=(3m-s+4t-zq+4zp)/7;
and a'-a=3s-2t, b'-b=2t-s.
Algebraic elimination gives two exact identities for EVERY G:

x-a'/3 =
[3b(cB-cA)-7a]/21 + (4+6r)hA/7
+ (1+c(3r+1))s/7
+ (2-6c(r+1))t/21 +8zq/7-4zp/7.

y-b'/4 =
[2a(cA-cB)-7b]/28 + (3+2R)hB/7
+ (3/28-c(R+3)/14)s
+ (1/14+c(R+1)/7)t +4zp/7-zq/7.

Both are exact rational identities, also certified by the accompanying executable SymPy source. In particular, the first LHS and second LHS must be nonpositive by the capacities.

Elementary TV dual: if E_i are pairwise disjoint measurable events in a probability space and f=sum(lambda_i 1_{E_i}), then for distributions mu,nu,
|sum lambda_i(mu(E_i)-nu(E_i))| <= (max(0,lambda_i)-min(0,lambda_i))*TV(mu,nu).
It follows from the oscillation norm of f and the zero total mass of mu-nu.

For AU, the Q coefficients on the disjoint events Z_A=1,T1,T2 are -(4+6r)/7,-(1+c(3r+1))/7,-8/7; their coefficient range is at most C_QA. P coefficients on disjoint T1,T2 are (6c(r+1)-2)/21,4/7; their coefficient range is at most C_PA. Hence [3b(cB-cA)-7a]/21 <= C_QA TV_Q+C_PA TV_P. Taking the positive part and dividing by C_QA+C_PA gives d2^AU.

For BU, Q coefficients on disjoint events Z_B=1,T1,T2 are -(3+2R)/7,(2c(R+3)-3)/28,1/7, whose coefficient range is at most C_QB; P coefficients on T1,T2 are -(1+2c(R+1))/14,-4/7, whose range is at most C_PB. Thus [2a(cA-cB)-7b]/28 <= C_QB TV_Q+C_PB TV_P, giving d2^BU. Future stopping/decisions do not enter these event identities. Taking infimum over all competitors proves both full-policy bounds and S23 inclusion gives the stronger-class bounds.

## Constructive upper bound

Let alpha=a/6, beta=b/4, cstar=(alpha*cA+beta*cB)/(alpha+beta). Genuine causal Gstar uses F's t1 actions; at t2 AU and BU both continue with cstar, AV/BV stop Q; at t3 AU descendants stop P and all other descendants stop Q; at t4 stop Q. As AU and BU have likelihood ratio 1 and alpha*(cstar-cA)+beta*(cstar-cB)=0, both laws have identical t2 total stopping mass in F and Gstar; their differing tagged t3 leaf coordinates exchange masses plus/minus U. All other observable coordinates match. Hence TV_Q=TV_P=U. Gstar belongs to S23, proving the shared upper bound. No noncausal occupancy mixture is used.

## Scientific verification and remaining obligations

This run executed two exact symbolic identities via SymPy (PASS_SYMBOLIC_BINARY_CAPACITY_IDENTITIES) and an independent rational full-tree Fraction script (PASS_EXACT_N4_BINARY_CAPACITY_TV_MODULUS) checking 1300 sampled fully causal S23 policies over finite rational parameter slices, positive mass and terminal-distribution conservation. The all-real statement follows from the displayed identities and TV dual argument, not from sampling. Executed full-tree script and its result are preserved in the supplementary research evidence ZIP accompanying this publication.

BRC reuse: REUSE_APPLIED to explicitly positive Q/P branch mass, likelihood-ratio fibers, tagged ancestry and causal capacities. The scope is an external finite two-law stopping model. P000 native Heartbeat X6 Cell and time dynamics, three-axis slice typing and future-observer-preserving embedding require a separate proof; no external probability-tree result is promoted to P000.

Next: close actual d2,d23 minimax bounds in either displayed witness by an executable strategy and matching full-policy dual certificate, or strictly sharpen one endpoint.
