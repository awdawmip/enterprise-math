# EC49AF — Exact eta-robust causal observation statements
Date: 2026-10-29. Author-side proof and exact computations. UNREVIEWED / NOT_ADMITTED.

## Model
For w,z in {0,1,2}, u in {0,1}, eta real in [0,1/2), define
t(w,u)=1/2+(2u-1)(1-w)eta,
P(w,u,z)=t(w,u)*(1/6 if w=z else 1/12), Q(w,u,z)=t(w,u)/9.
Every source has 18 strictly positive normalized leaves. The observer selects STOP, A0/A1 (cost 1) or B0/B1 (cost 2), forgets w, observes u, may buy S (cost 1) to see z, then accepts with fresh local behavioral coins. The fixed source-identical costs are C1=43/48, C2=7/8. Let alpha=P(accept), beta=Q(accept), delta=alpha-beta. No retained strategy seed.

Fix prefix X: w0:A0; w1:A1; w2:(9/16)A0+(1/16)B0+(3/8)STOP; always buy S after a paid first action. It meets both budgets exactly at all eta.

## AF1: sharp GLOBAL upper fiber for every real eta
For all eta in [0,1/2) and all delta in [0,59/576], the largest alpha among ALL valid causal behavioral policies with that delta and the fixed costs is alpha_max=1-3delta, beta=1-4delta.

Proof: Each raw leaf has P/Q in {3/4,3/2}. The same behavioral kernel acts under P and Q, so for every event E, 4P(E)-3Q(E)>=0. Apply to rejection E: 1-alpha>=3delta.

Under X, pure off-diagonal sensed atoms (A0,z1), (A1,z0/z2), (B0,z0/z1), each for both u, have P=3(Q-P). Their total negative difference sum(Q-P) equals (25+32+2)/576=59/576, independent of eta by sum_u t(w,u)=1. Reject each such observable atom with probability delta/(59/576), independently with fresh local coins, and accept every other atom and STOP. Then P(reject)=3delta, Q(reject)=4delta. This attains the upper bound with exact costs. No assumption about the whole region above this delta interval is made.

## AF2: exact TWO eta thresholds in fixed prefix X
For all eta in [0,1/2), X's maximal discrimination D_X is exactly
D_X(eta)=59/576 + max(34eta-1,0)/576 + max(82eta-23,0)/1152.
The thresholds are eta=1/34 and eta=23/82.

Proof: For sensed atom j=(c,u,z), d_j=P_j-Q_j=(1/36) sum_w x_wc t(w,u)(3*1{w=z}-1). All pure off-diagonal atoms remain negative with aggregate negative capacity 59/576. The only other atom differences that can turn negative as eta increases are
d(A0,u=1,z=2)=(1-34eta)/576,
d(A0,u=0,z=0)=(23-82eta)/1152.
The complementary A0 mixed differences are (1+34eta)/576 and (23+82eta)/1152, both positive. All other nonempty atoms have fixed strict sign. Total discrimination sums to zero. Hence the positive capacity equals total absolute negative capacity, yielding the stated hinges exactly.

Equivalently D_X is 59/576 until 1/34, (17eta+29)/288 until 23/82, and (50eta+31)/384 afterward.

## AF3: full UPPER alpha boundary for the fixed prefix X
Define D0=59/576, h1=max(34eta-1,0)/576, h2=max(82eta-23,0)/1152, D=D0+h1+h2. For h1>0, r1=3(17-2eta)/(34eta-1)>3; for h2>0, r2=3(41-46eta)/(82eta-23)>r1. Then for any 0<=delta<=D, the greatest alpha among X terminal acceptance rules is
1-3delta, for delta<=D0;
1-3D0-r1(delta-D0), for D0<delta<=D0+h1;
1-3D0-r1 h1-r2(delta-D0-h1), for D0+h1<delta<=D.
Proof: To maximize accepted P at fixed P-Q=delta, reject only negative-d atoms, filling rejected difference capacity by ascending rejection cost P/(-d). The pure negative atoms give capacity D0 and ratio 3, followed by new mixed negative atoms of capacity h1 and h2, with ratios r1 and r2. All are distinct terminal observation states; fractional knapsack acceptance is implemented with fresh independent Bernoulli decisions. This is an exact theorem WITHIN X, not the global boundary above D0.

## Finite legal endpoint audit, eta=1/4
At support H=alpha-(177/172)beta, the exact checker ENDPOINT_AUDIT.mjs exhausts 288 first-stage endpoint prefixes (144 with high-cost mass b=0 and 144 with b=1/16). Under exact constraint b+m=1/16, the optimal conditional S-skipping for each prefix is found by sorting skip-information loss per source mass at each (c,u). Results:
H_X=3461/33024.
Relaxed b=0 all-S max=27/256=H_X+11/16512 (NOT legal at b=0).
Original-protocol legal b=0 maximum=168127/1618176=H_X-17/18816.
Legal b=1/16 maximum=H_X.
This settles the 288 specified endpoint cases only; interior real-valued first-stage and S probabilities require separate analysis.

## Verification, provenance and scope
VERIFY.mjs and EXACT_REPORT.json contain executed exact BigInt rational tests at seven eta points including thresholds and both post-threshold regimes. ENDPOINT_AUDIT.mjs and ENDPOINT_REPORT.json are a separate, executed exhaustive finite check of 288 endpoint prefixes. The all-real claims AF1-AF3 follow the algebraic proofs above, not a finite sample extrapolation. Frozen GLOBAL_KNOWLEDGE_V1 main 6629bd6fe79d111d72f54b1b01ec1e031254bf64; frozen Enterprise Math main cc55cd808640ebaa973d8605e8bda137192073e5. Previous EC49AD PR #1688 at d974d04c95c1cb67045ad9abf6387d97248b740e; EC49AE authorship source at 1ade545076983c001e112bb689ae6a44d904d39b. Source type is auxiliary positive-labelled BRC probabilities, not signed/phase native BRC, X6, or physical heartbeat.

Native service em_status v0.6.11 reported research_authority_granted=false; native owner inventory returned CONTROL_QUOTA (5/5), with control CODE_REVIEW_REQUIRED. This is an author-side portable draft without formal CLAiM, Result, independent Driver review or mathematical admission. P000 and ACTIVE worldview unchanged.

Next EC49AG: seek a fully lawful rational interior x,s,a support challenger at eta>1/100 or certify universal dominance on another exact parameter interval, preserving b+m=1/16 and the causal erasure of w.