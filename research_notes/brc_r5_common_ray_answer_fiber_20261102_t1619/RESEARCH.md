# R5: Common-ray source-answer kernels — projection equality and four-observer fiber classification

Date: 2026-11-02 Asia/Shanghai.
Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / SYMBOLIC_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.

## Provenance and frozen sources

Scientific predecessor: enterprise-math@a8a2137585ac13b695fcc27a6f460b185986bcfe, research_notes/brc_r5_two_law_antisymmetric_answer_20261102_t1444/RESEARCH.md.
Frozen scientific inputs are preserved: GLOBAL_KNOWLEDGE_V1 main@a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math main@86149263e38c22292c9def1e0f69092efa1be77e. Current normative snapshots read separately: Global Knowledge main@b05b335e29b3f7ff175dc6ae73b5bfa487a8a1c2 and Enterprise Math main@c5502908fbc8f3acfc8cfb4421fd71a9e747d809. P000, ACTIVE Heartbeat World, joint-observer preservation, current research method and portable protocol were consulted without changing their definitions.

Mother question: build a strictly positive two-law stopping model with equal FULL/LR four-observer convex hulls but distinct actual real behavioral images, O=(e_P,e_Q,T_P,T_Q). This unit fully classifies a new three-parameter family inside the existing I→J→K source-labelled graph.

## Exact graph and parameter domain

Under both laws, mass 1/2 starts at I at time 1; mass 1/4 starts at J via B at time 2; mass 1/4 starts at K via C at time 3. Stop at I, J or K gives answer P at time 1, 2 or 3 respectively. Continue I splits equally to J via I and K via I. Continue J splits equally between a direct time-3 answer and K via BJ/IJ. On J's direct branch, P(answer P)=3/5 and Q(answer Q)=3/5. Continue K answers at time 4 or 5, with conditional time-5 probabilities p=1/2 under law P and q=1/3 under law Q. Conditional answer/delay randomness may be independent.

At K, for source s in (C,I,BJ,IJ), the continue action answers Q with probability u_s under BOTH P and Q. Set u_BJ=u_IJ=u_B. The three independent real parameters u_C,u_I,u_B are arbitrary in (0,1). Hence the K-continue P-answer probability is 1-u_s under each law, all conditional probabilities are strictly positive, and likelihood-ratio/time collisions remain the predecessor's.

FULL uses seven stop parameters (x,jB,jI,kC,kI,kBJ,kIJ) in [0,1]^7. LR uses three (x,y,z) with jB=jI=y and kC=kI=kBJ=kIJ=z. Observations are e_P=P(answer P), e_Q=Q(answer Q), T_P=E_P(time), T_Q=E_Q(time).

## Source-labelled BRC carrier and reversible four-observer map

Keep all four source arrival masses, instead of collapsing their K provenance:

~~~text
D = ((1-jB)+(1-x)(1-jI))/8
wC=1/4; wI=(1-x)/4; wBJ=(1-jB)/8; wIJ=(1-x)(1-jI)/8
C = sum_s w_s(1-k_s)
U = u_C*wC*(1-kC)+u_I*wI*(1-kI)
    +u_B*(wBJ*(1-kBJ)+wIJ*(1-kIJ))
~~~

Here D is the J-direct mass; C is K-continuing mass, and U is the source-weighted answer deficit. Direct enumeration under both laws yields, for every REAL policy,

~~~text
e_P = 1 - 2D/5 - U
e_Q = 3D/5 + U
T_P = 5/2 - 3x/4 + 2D + 3C/2
T_Q = 5/2 - 3x/4 + 2D + 4C/3.                (1)
~~~

The exact affine inverse is

~~~text
D = 5(e_P+e_Q-1)
U = e_Q - 3D/5
C = 6(T_P-T_Q)
x = (4/3)(5/2 + 2D + 3C/2 - T_P).            (2)
~~~

Thus the joint four-observer map retains the full (x,D,C,U) fiber information. Using its two-answer projection below is a diagnostic; the four-observer conclusions retain every coordinate.

## Theorem A: equality of ALL signed two-answer projected supports

For every real (u_C,u_I,u_B) in (0,1)^3,

~~~text
conv projection_(e_P,e_Q) O(FULL)
  = conv projection_(e_P,e_Q) O(LR).           (3)
~~~

Proof: For arbitrary real signed weights alpha,beta, the objective is

alpha*e_P+beta*e_Q = alpha + (3*beta-2*alpha)*D/5 + (beta-alpha)*U.

At any K source, continuing instead of stopping changes this signed objective by its nonnegative arrival mass times u_s*(beta-alpha). All u_s are positive, so an optimizer can use the SAME K choice for every source, z=0 for beta>alpha and z=1 for beta<alpha (arbitrary when equal). Conditional on this choice, continuing J instead of stopping has exactly the SAME signed incremental value per arriving unit for J sources B and I: the J-direct law is common, and both K routes BJ/IJ use the same u_B. Hence an optimizer can choose jB=jI=y. The only I decision x is already shared. Consequently an LR policy attains each FULL maximum for every signed (alpha,beta). Compactness and support-function uniqueness give (3). This proof quantifies over all real signed directions, not a finite sweep.

## Theorem B: complete all-real four-observer hull classification

For every real (u_C,u_I,u_B) in (0,1)^3,

~~~text
conv O(FULL)=conv O(LR)  iff  u_C=u_I=u_B.    (4)
~~~

When these equalities hold, the ACTUAL real behavioral images coincide as well: O(FULL)=O(LR).

Proof of necessity, first exposed fiber: x>=0,D>=0, so x=D=0 is the face exposed by maximizing -x-D, in coordinates that are invertibly obtained from O. FULL can select x=0,jB=jI=1, K-C continues and K-I stops. The resulting (x,D,C,U) is (0,0,1/4,u_C/4). Any LR point on this face must use x=0,y=1, and therefore C=(1-z)/2, U=(1-z)(u_C+u_I)/4, implying U=(u_C+u_I)C/2. This affine relation survives convex combinations confined to the face. Inclusion of the FULL point forces u_C=u_I. The precise witness's signed fiber defect is (u_C-u_I)/8.

Second exposed fiber: D<=(2-x)/8 and x<=1 imply x+4D<=1+x/2<=3/2, with equality exactly at x=1,D=1/8. FULL realizes this face using x=1, J-B continues, K-C continues and K-BJ stops. Its (x,D,C,U) is (1,1/8,1/4,u_C/4). LR points on this face have x=1,y=0. Their K source weights are 1/4 (C) and 1/8 (BJ); the common z forces C=3(1-z)/8 and U=(1-z)(u_C/4+u_B/8), hence U=(2u_C+u_B)C/3. Inclusion of the FULL point forces u_C=u_B. The signed fiber defect is (u_C-u_B)/12. Both equalities are necessary.

Proof of sufficiency: if u_C=u_I=u_B=u, the P/Q answer and time kernels on K continuation are source-independent. Given any real FULL policy keep x and define

~~~text
y=[jB+(1-x)jI]/(2-x)
z=[sum_s w_s*k_s]/[sum_s w_s].
~~~

Both denominators are positive throughout the closed policy cube, and y,z lie in [0,1]. The LR policy (x,y,z) reproduces the total J stopping flow, K arrival flow and K stopping flow under BOTH laws, hence exactly the same (x,D,C,U) and O through (1). LR is a subset of FULL. Thus the actual images and their convex hulls agree. QED.

## Theorem C: strictly positive rank-four example and an exact mixed Farkas separator

Take (u_C,u_I,u_B)=(1/2,1/4,1/3). The FULL deterministic policy (x,jB,jI,kC,kI,kBJ,kIJ)=(0,1,1,0,1,1,1) yields

W=(7/8,1/8,23/8,17/6).

Let n=(-256,-244,-155,171). In the original four coordinates,

~~~text
L(O)=(n·O+216)/12=U-3C/8-x-D.
~~~

For every REAL LR policy,
U-3C/8=(1-z)(x/32-D/24), whence L(O_LR)<=0, with equality attainable at x=D=0. For every REAL FULL policy,

~~~text
U-3C/8 = wC*(1-kC)/8 - wI*(1-kI)/8
         -[wBJ*(1-kBJ)+wIJ*(1-kIJ)]/24 <=1/32.
~~~

As x,D>=0, L(O_FULL)<=1/32; W attains equality. Consequently

~~~text
h_FULL(n)=-1725/8; h_LR(n)=-216;
h_FULL(n)-h_LR(n)=3/8 > 0.                 (5)
~~~

The exact original-observer distance bound is dist_infinity(W,conv O(LR)) >= (3/8)/826 = 3/6608, since ||n||_1=826.

The four-dimensional structure is nondegenerate. Using LR corner base 000 and differences to 001,010,011,100, symbolic rational expansion gives

~~~text
det_LR=-(2*u_B-u_C-u_I)/2560.
~~~

At the FULL interior all-1/2 behavioral point, the Jacobian minor in (x,jB,kC,kI) is

~~~text
det_JFULL=-(u_C-u_I)/10240.
~~~

At the given rational triple these are 1/30720 and -1/40960. Thus the LR convex hull has affine dimension four and FULL's real behavioral observer image has nonempty four-dimensional interior. The identity is valid for formal real parameters, checked independently with exact symbolic algebra.

## Checks, scientific scope and next question

VERIFY.py (standard-library Fraction) checks seven rational triples and every FULL 128/LR 8 deterministic vertex per triple, all 80 two-answer signed directions in [-4,4]^2 minus (0,0), forward/inverse formulas, exposed-fiber differences, rank minors, 72 nonbinary equal-kernel aggregations, and the exact facet; its actual captured stdout is EXACT_OUTPUT.txt. SYMBOLIC_CHECK.py gives a separate exact SymPy expansion of the two determinant identities, with output in SYMBOLIC_OUTPUT.txt. Universal statements above follow from the algebraic proofs, while finite tests are consistency checks.

The result locates a source-observer distinction invisible to every answer-only signed support direction but visible on the original joint time–answer observer. The two exposed fibers classify the entire chosen three-parameter family; a new coupling or source-conditional J answer mechanism is the next discriminating direction.

Authenticated GitHub connector login is awdawmip, with repository push permission. The separate native Enterprise Math Sites gateway reported research_authority_granted=false, read-only scopes and no write relay; owner lookup returned CONTROL_QUOTA. This record grants no native owner/CLAIM/Result/Driver review, theorem admission or X6 attribution. The attached NEXT_TASK.md specifies an independently executable continuation.