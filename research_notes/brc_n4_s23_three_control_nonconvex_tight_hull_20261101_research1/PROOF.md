# BRC N=4 / S23: nonconvex three-control lawful image with zero Chebyshev convexification gap

Date: 2026-11-01. Author-side analytic theorem; independently executed Node.js safe-integer sanity verifier. **UNREVIEWED / NOT_ADMITTED**. Direct continuation of PR #1765 predecessor e9414e966b113c84eead473b6eefd6d0e6588ce9.

## Model, hypotheses and scope

Retain the six distinct BRC statistical source labels (AU0,AU1,AV,BU0,BU1,BV), four stopping times and positive matrix 20M with rows
(10,10,0,0,0,0), (9,11,0,0,0,0), (0,0,20,0,0,0),
(0,0,0,10,10,0), (0,0,0,2,18,0), (0,0,0,0,0,20).
Source kernel F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)).
Original causal maps A=(0,0,0,1,1,1), B=(2,2,3,2,2,4), C=(5,6,7,8,9,10) refer to the eleven legal controls (a_A,a_B,b_U,b_AV,b_BV;c_AU0,c_AU1,c_AV,c_BU0,c_BU1,c_BV).

Vary exactly a=a_A, b=b_U, c=c_AV in Q=[1/4,3/4]^3. Freeze a_B=1/4,b_AV=0,b_BV=1/3 and five remaining third-stage controls c_AU0=c_AU1=c_BU0=c_BU1=c_BV=1/2. In particular, b_U is the SAME legal control on AU and BU: no independently reselected source hazards. After labeled positive mixing the six prepared laws are
AU0=AU1=(a,(1-a)b,(1-a)(1-b)/2,(1-a)(1-b)/2),
AV=(a,0,(1-a)c,(1-a)(1-c)),
BU0=BU1=(1/4,3b/4,3(1-b)/8,3(1-b)/8),
BV=(1/4,1/4,1/4,1/4).
Equalities of selected prepared rows are due to explicit freezes, NOT a general source-identification permission.

For joint six-row P(theta) define D(P,Q)=max_i TV(P_i,Q_i), TV(p,q)=sum_t |p_t-q_t|/2.
Define R_lawful=min_{z in Q} max_{theta in Q}D(P(theta),P(z)), and R_hull=min_{v in conv P(Q)} max_{theta in Q}D(P(theta),v). Both compare the SAME joint six-row object, not freely selected row-wise centers.

## Theorem 1: full real continuum, exact unique lawful center and tight hull relaxation

R_lawful=R_hull=7/24; the **unique** lawful center is z=(11/24,1/2,1/2). The parameter midpoint (1/2,1/2,1/2) has radius 5/16 >7/24.

Lower bound, also valid for ANY convex-hull center: every AV row in conv P(Q) is (alpha,0,beta,1-alpha-beta). Write y=(1-a)c. Across all real a,c in [1/4,3/4], the ranges of a, y, a+y respectively are [1/4,3/4], [1/16,9/16], [7/16,15/16]. For a three-atom zero-sum signed difference, TV equals the maximum absolute coordinate difference. Three valid AV-event risk inequalities are:
r>=3/4-alpha;
r>=9/16-beta;
r>=alpha+beta-7/16.
Adding yields 3r>=3/4+9/16-7/16=7/8, so r>=7/24. This is an explicit nonnegative exact rational dual combination and DOES NOT assume the center is lawful. Equality forces alpha=11/24, beta=13/48. Any lawful center then has a=alpha=11/24 and c=beta/(1-a)=1/2.

Upper bound: at the lawful z=(11/24,1/2,1/2), prepared rows are:
AU0=AU1=(11/24,13/48,13/96,13/96);
AV=(11/24,0,13/48,13/48);
BU0=BU1=(1/4,3/8,3/16,3/16);
BV=(1/4,1/4,1/4,1/4).
At EACH of eight vertices (a,b,c) in {1/4,3/4}^3, direct rational evaluation of six TV risks gives EXACTLY
(7/24,7/24,7/24,3/16,3/16,0).
For fixed z, P(theta) is separately affine in each of a,b,c; TV to its fixed center is separately convex, as is the maximum of six TVs. Iterating the one-variable endpoint maximum shows its maximum over the entire real cube occurs at a vertex. Hence r<=7/24 throughout Q. Together with the AV lower bound this proves both R_lawful and R_hull.

Uniqueness of b: once a=11/24, the center AU stage-2 event has mass (13/24)b and center AU event {3,4} mass (13/24)(1-b). At legal input a=1/4,b=3/4,c=1/4, the AU stage-2 event has mass 9/16; r<=7/24 requires 9/16-(13/24)b<=7/24, i.e. b>=1/2. At legal input a=1/4,b=1/4,c=1/4, AU event {3,4} has mass 9/16; r<=7/24 requires 9/16-(13/24)(1-b)<=7/24, i.e. b<=1/2. Thus b=1/2 uniquely.

## Theorem 2: the lawful joint preparation image is NONCONVEX

Take two legal strategies theta_low=(1/4,1/4,1/2), theta_high=(3/4,3/4,1/2). Their joint-law midpoint V=(P(theta_low)+P(theta_high))/2 lies in conv P(Q). If a single lawful (a,b,c) realized V, its AV first-outcome mass 1/2 would force a=1/2. Its BU second-outcome mass 3/8 would force b=1/2. Both endpoint AU second-outcome masses are 3/16, hence V_AU(time2)=3/16, while any lawful a=b=1/2 gives AU time-2 mass (1-a)b=1/4, discrepancy 1/16. Contradiction for every c. Therefore P(Q) is nonconvex despite all source and prepared laws being valid positive distributions. The hidden correlation introduced by mixing two strategies is not a realizable single shared causal control assignment.

## Exact LP implication and boundary

Multi-affinity implies each P(theta) is a nonnegative barycentric mixture of its eight joint vertex images, so conv P(Q)=conv{P(v):v vertex}. The convex-hull Chebyshev center and all vertex TV risks yield a finite LP. On arbitrary three-control boxes it is a LOWER BOUND ONLY: nonconvexity prevents treating an LP center as a lawful strategy without a representation witness. Here the explicit rational lawful z certifies equality; the result does not prove general rational-box tightness.

Actual verification: Node.js v22.16.0 ran VERIFY.js with exact integer probability scale 384; 125 legal grid triples, 750 prepared-row TV checks, all 8 vertices and 48 exact vertex-row checks, the dual rows, the two uniqueness events and the nonconvexity witness. RUN_EVIDENCE.json is actual stdout. All-real statements follow from analytic dual plus multi-affine vertex theorem, never from the 125 samples.

Scope: model-local finite BRC positive-source statistics, not the native P000 six-axis Cell, independent time or three-dimensional slice. No native embedding, readout, future-operation preservation, signed-phase or physics claim. Independent S2 transfer/review remains open. This has not improved the full free ten-label minimax range 1/2 <= R_beh(k,10) <= 2/3 for k=4,6. Source and exact next tasks in SOURCES.md and NEXT_TASK.md. **AUTHOR_ANALYTIC_PROOF / NODE_EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED.**
