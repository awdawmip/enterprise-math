# R5 — Complete exposed-edge fiber classification for four source-conditioned K delays

Date: 2026-11-02 (Asia/Shanghai). Claim status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is an auxiliary dual-measure BRC stopping model, not a native X6/HB embedding or a solution of the original four-observer mother problem.

Scientific pins preserved: GLOBAL_KNOWLEDGE_V1 main@a01383f825ef9d43b4b754254303298c64041568; Enterprise Math main@86149263e38c22292c9def1e0f69092efa1be77e.
Scientific predecessor: enterprise-math@ed1981f5aee3cdfc94e0523d0ccb2b9899606b2c, research_notes/brc_r5_common_p_delay_rotating_obstruction_20261102_t0940/.
Current normative reads were separately taken at Global main@b86c12cadff34477da8ea278b88039da4346c18c and EM main@37319a66cb6417654422f79f57cbccb216c8766f: bootstraps, manual, continuation normative context, P000 with matching original/projection SHA, ACTIVE worldview, portable research protocol, mathematical proof policy, BRC priority and current EM research method.

## Exact process and observer

Under both measures P and Q, the initial masses are 1/2 at I, 1/4 at J through source B and 1/4 at K through source C. True-time/likelihood-ratio decision keys are I=(1,1), J=(2,1), K=(3,1). I continuation sends half its mass to J and half to K; J continuation sends half to a time-3 terminal answer and half to K. Stopping at I/J/K answers P at time 1/2/3 respectively. The J final-answer kernel is (P(answer P),Q(answer P))=(3/5,2/5). K continuation answers P with probability 1/2 under both laws at time 4 or 5. The probability of time 5 is t under P for every K source, while under Q it is c, i, b, j for K sources C, I, BJ, IJ respectively. The observer is O=(eP,eQ,TP,TQ), where eP=P(answer P), eQ=Q(answer Q), and TM is expected terminal time under law M.

FULL variables are (x,jB,jI,kC,kI,kBJ,kIJ) in [0,1]^7; LR variables (x,y,z) impose jB=jI=y, kC=kI=kBJ=kIJ=z. Each map is multiaffine in its own behavioral variables, so the hulls are determined by 128 FULL and 8 LR deterministic corners. Natural transitions are strictly positive when 0<t,c,i,b,j<1; formulas extend algebraically to the closed cube.

## Theorem — necessary and sufficient condition, all real parameters

For every t,c,i,b,j in [0,1],

  conv(FULL) = conv(LR)   if and only if   c = i = b = j.

On this diagonal the actual behavioral images are equal: FULL([0,1]^7)=LR([0,1]^3). Otherwise an explicit rational or real signed support functional separates their convex hulls.

In the inherited two-free-Q-parameter family with fixed i=1/4 and j=1/3, no t,c,b in (0,1) can yield four-observer hull equality.

## Exact geometric necessity proof

Number the LR 3-bit vertices L0,...,L7 by 000,001,010,011,100,101,110,111. The 3D projections p=(eP,eQ,TP) are:

  L0=(21/40,21/40,3(t+5)/4)
  L1=(9/10,3/20,3)
  L2=(3/4,1/4,(t+6)/2)
  L3=(1,0,5/2)
  L4=(61/80,21/80,(3t+19)/8)
  L5=(19/20,3/40,2)
  L6=(7/8,1/8,(t+8)/4)
  L7=(1,0,7/4).

The exact outward 3D face normals, with their complete equality-vertex sets, are:

  A=(6t-4,4t-6,1)           : {0,1,2,3}
  B=(-6t-29,-4t-21,-1)      : {0,2,4,6}
  C=(-1,-1,0)               : {2,3,6,7}
  D=(34-6t,36-4t,-1)        : {0,1,4,5}
  E=(4-6t,6-4t,-1)          : {4,5,6,7}.

Every off-face LR vertex has strictly lower score. The minimum strict slacks over t in [0,1] are 3/4, 3/4, 1/40, 3/4 and 3/4. These differences are independent of t by direct substitution. Thus A+B exposes exactly edge [L0,L2], A+C exactly [L2,L3], and D+E exactly [L4,L5]. Each edge has a unique convex lift inside conv(LR) at a given interpolation parameter.

The following FULL deterministic 7-bit policies, ordered (x,jB,jI,kC,kI,kBJ,kIJ), project to the stated LR edge interpolation, but have a signed TQ displacement from the LR lift:

  edge [L0,L2], λ=1/2: 0010000 gives +(b-j)/16;
  edge [L0,L2], λ=1/2: 0100000 gives -(b-j)/16;
  edge [L2,L3], λ=1/2: 0110100 gives +(c-i)/8;
  edge [L2,L3], λ=1/2: 0111000 gives -(c-i)/8;
  edge [L4,L5], λ=1/3: 1000010 gives +(c-b)/12;
  edge [L4,L5], λ=2/3: 1001000 gives -(c-b)/12.

These identities are obtained by exact source-labelled P/Q probability-flow substitution and are valid for all t,c,i,b,j (the precise flow algorithm is VERIFY.py). If conv(FULL)=conv(LR), each displayed FULL observation must lie in the LR hull. Its projected point is on a uniquely exposed LR edge, so it can use only the edge endpoints in any LR convex decomposition; its TQ coordinate must equal the displayed interpolation. The three pairs give b=j, c=i and c=b. Combining yields c=i=b=j, proving necessity.

## Actual-set sufficiency proof

If c=i=b=j=q, K source information has no effect on the conditional terminal kernel. Since arrival masses under P/Q coincide for each labelled source, any FULL behavior can be pooled exactly. Set

  y = [jB+(1-x)jI]/(2-x);
  aC=1/4, aI=(1-x)/4, aBJ=(1-jB)/8,
  aIJ=(1-x)(1-jI)/8;
  z = [aC*kC+aI*kI+aBJ*kBJ+aIJ*kIJ]/[aC+aI+aBJ+aIJ].

The denominators are strictly positive and y,z belong to [0,1]. With I-control x, J-control y, K-control z, the LR policy matches the FULL policy's aggregate two-measure J stop/continue mass, J final answer mass, K stop/continue mass and source-independent final K kernel. It therefore matches all four observations. Every LR behavior embeds in FULL, proving equality of the actual real observation sets and hence hull equality.

## Constructive separating functional and uniform residual

Define d1=|b-j|/16, d2=|c-i|/8, d3=|c-b|/12 and d=max(d1,d2,d3). For d>0 choose an edge with maximum defect, and from its displayed FULL witnesses choose the sign giving positive vertical lift +d. Let m be the sum of the two exposing 3D normals, and r,s the LR endpoint vertices. Put

  R = -(TQ(Ls)-TQ(Lr))/(eP(Ls)-eP(Lr));
  N = (1000*m_1+R, 1000*m_2, 1000*m_3, 1).

The three endpoint eP differences are 9/40, 1/4 and 3/16. Hence |R|≤64/3<22, because all expected times belong to [1,5]. At every off-edge LR corner, 1000*m loses at least 1000/20=50, while the R*eP+TQ term can change by at most 22+4=26. Consequently the two LR edge endpoints are the exact LR maximizers of N (tied by the definition of R). The selected FULL witness scores exactly d above their common score, giving h_FULL(N)-h_LR(N)≥d. The norm satisfies ||N||_1≤82023, so its infinity-norm distance to conv(LR) is at least d/82023.

Since |j-i|≤|j-b|+|b-c|+|c-i|≤(16+12+8)d=36d, fixed i=1/4 and j=1/3 imply d≥1/432 and a uniform positive hull-separation distance lower bound of 1/35433936 throughout the strict parameter region. This is a constructive proof for *every* real c,b,t, not a signed-direction finite search.

The edge-discrepancy minimax min over (c,b)∈[0,1]^2 of max(d1,d2,d3) is exactly 1/432. It is attained at the positive rational pair c=29/108, b=8/27, with all three discrepancies equal. This minimax does not assert an exact minimax of full convex-hull distance.

## Exact positive rational rank-four example

For t=1/2, (c,i,b,j)=(1/4,1/4,1/4,1/3), the prior adaptive normal n_old=(-21,-14,-12,12) has equal FULL and LR maxima -41/2. A new signed normal n=(-3169,-2916,0,108) has exact maxima

  h_FULL=-44283/16, h_LR=-11073/4, gap=9/16.

The FULL policy 0100000 attains the larger maximum at W=(51/80,31/80,59/16,85/24), with dist_infinity(W,conv(LR))≥9/99088. The five-vertex LR affine determinant for 000,001,010,100,101 is 3/40960; the FULL interior Jacobian minor on x,jB,jI,kC is -1/163840. Thus the old normal can tie without losing 4D rank, while the new edge witness still separates.

## Verification, provenance and current authority

Executed Python 3 standard-library Fraction program VERIFY.py and captured actual stdout in EXACT_OUTPUT.txt. Verification includes 5 exposed face normals at 3 exact t nodes; all 6 lifted-edge identities for all 16 source-Q hypercube vertices and 3 t nodes, with the parameter degree/multiaffinity argument proving their exact polynomial extensions; real-policy pooling regressions; 128 FULL/8 LR corner supports for the positive rational example; nonzero determinant/minor; and the rational minimax witness. Actual execution: 1567 exact assertions and 7506 source-resolved flow evaluations. Final marker: PASS_EXACT_R5_ALL_Q_SOURCE_EXPOSED_EDGE_FIBER_CLASSIFICATION. The analytical face/fiber and pooling arguments above carry the all-real theorem.

BRC reuse: REUSE_APPLIED, retaining positive source-labelled exact P/Q branch masses C/I/BJ/IJ until observer compression. The three lifted-edge TQ residuals measure information lost by source pooling. No signed-amplitude interpretation, physical calibration or X6 transfer is asserted.

Authenticated GitHub connection: awdawmip, repository push permission. Native Enterprise Math service 0.6.11 reported research_authority_granted=false and executor_binding_configured=false; bounded owner/task query returned CONTROL_QUOTA. No active claimant, formal Result, Driver review or theorem admission is claimed; author-side research only. P000 and ACTIVE worldview were read without mutation.

Next: vary source-conditioned **P** K-delay kernels, rather than tune this already completely classified common-P family. Derive the resulting projected edge geometry, and pursue exact rational LR convex decompositions for all 128 FULL corners or a precise Farkas obstruction, retaining four-dimensional Jacobian rank and the original frozen scientific pins.
