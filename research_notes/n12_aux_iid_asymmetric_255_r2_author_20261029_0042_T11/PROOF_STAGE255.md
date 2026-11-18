# Stage255 — Exact exterior optimum and full-real coupling contact face

Date: 2026-10-29. Status: AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED.
Parent: Stage254 exact author proof in Draft PR #1571, immutable commit a538e30f5a6e5c2d83bdf88f56a2837aeea17842. This is an EXTERNAL ternary IID auxiliary model, not native P000-X6.

## Model and exact answer

P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), N=12. Arbitrary randomized stopping and classification based on the complete ordered history are allowed. Four observables: eP=Pr_P(declare Q), eQ=Pr_Q(declare P), tP=E_P[stop depth], tQ=E_Q[stop depth]. V_N(a,b)=minimum max(tP,tQ) over both error caps, or infinity when infeasible.

For the exact Stage254 exterior caps
    a=15492478957579/55725627801600
    b=580533802651/1160950579200
the exact value is
    V12(a,b)=12367526316773/2321901158400
             =24(1-a-b) ≈ 5.3264654578558135.

A valid interior-time Bellman dual has thetaP=thetaQ=1/2, lambdaP=lambdaQ=24 and root H=24. Both primal error constraints saturate, and tP=tQ at the constructed optimum.

## A general finite-alphabet exact Bellman calibration lemma

Let P_z,Q_z>0 be any finite-alphabet IID sources, d=TV(P,Q)=sum_z(P_z-Q_z)_+=sum_z(Q_z-P_z)_+>0. Let L=Q(h)/P(h) at an arbitrary ordered history h. For any finite horizon and any 0<theta<1, the P-normalized Bellman equation with terminal costs L/d (declare P), 1/d (declare Q), and continuation cost theta+(1-theta)L+sum_z P_z H(hz) has the exact solution
    H(h)=min(1,L)/d.

Proof: At L<=1, since sum_z LQ_z=L,
    L-sum_z min(P_z,LQ_z)=sum_z(LQ_z-P_z)_+ <= L*d.
At L>=1, since sum_z P_z=1,
    1-sum_z min(P_z,LQ_z)=sum_z(P_z-LQ_z)_+ <= d.
Substituting H= min(1,L)/d, the continuation action exceeds the cheaper stop action by at least theta(1-L) when L<=1 and (1-theta)(L-1) when L>=1. Strict inequality holds for L != 1; at L=1, sum_z min(P_z,Q_z)=1-d makes continuation tie with both stops. Backward induction closes the finite-horizon equation. The same non-strict inequalities hold at theta endpoints.

At the root L=1, H=1/d, proving for EVERY full-history randomized policy:
    theta*tP+(1-theta)*tQ + (eP+eQ)/d >= 1/d.
Hence max(tP,tQ)>=max(0,(1-eP-eQ)/d); taking endpoint theta values separately also bounds each time observer. This exact source-positive-mass calculation retains P/Q branch labels; it does not use signed-amplitude cancellation.

## Exhaustive rational dual certificate for N=12

Here d=1/24, L(s)=(2/3)^i*2^j at count s=(i,j,k) and H(s)=24*min(1,L(s)). The lemma works directly on full ordered histories, with the counts only serving as an exactly sufficient likelihood quotient for these four IID observers.

The actual Fraction checker tested all 455 count states, 1,274 available action costs, and 794 strictly positive action gaps. Exactly 13 tie states occur: (0,0,k), k=0,...,11 has P/Q/continue three-way tie; (0,0,12) has P/Q terminal tie. This follows also from L(s)=1 iff 2^(i+j)=3^i, i.e. i=j=0. Every history containing a nonneutral symbol must immediately stop to attain the supporting line.

## Exact matching primal policy

Put r=(5/6)^12=244140625/2176782336. Root probabilities are
    u=238307216823020789/2243701513771529011200 : immediately declare P;
    v=12137690822080267/2243701513771529011200 : immediately declare Q;
    w=12367526316773/12368906950400 : continue.
Each is positive and u+v+w=1. After continuing, stop at the first nonneutral symbol: 0 implies P, 1 implies Q. If the first 12 symbols are all neutral 2, guess P/Q with 1/2 each.

Exact independent source formulas give
    eP=v+w*((1-r)/4+r/2)=a,
    eQ=u+w*((1-r)/2+r/2)=b,
    tP=tQ=6*w*(1-r)=24*(1-a-b).
The separate nonmemoized, genuinely ordered-history P/Q positive-mass DFS visited 37 nodes and 28 terminal branches, normalized BOTH source masses to one and reproduced all four fractions. It matches the global Bellman lower bound and establishes the exact optimum.

## Complete real contact region and Stage254 adjacency

For EVERY integer N>=1 set rN=(5/6)^N. The affine support equality
    V_N(a,b)=24(1-a-b)
holds for all real caps (a,b) in [0,1]^2 IF AND ONLY IF they belong to the quadrilateral C_N with vertices
    root-P=(0,1), root-Q=(1,0),
    horizon-P=((1-rN)/4,(1+rN)/2),
    horizon-Q=((1+3*rN)/4,(1-rN)/2).
Equivalent inequalities are
    (3+rN)/4 <= a+b <=1,
    2a+b>=1, 2a+3b>=2.

Proof: Equality in the positive-error-multiplier Bellman support forces both caps saturated and every positive-reach action Bellman-minimizing. With theta=1/2, only pure-neutral histories can continue. Any randomized equality policy is a mixture of deterministic first-neutral stopping depths k<=N and P/Q labels. Their error coordinates are affine in (5/6)^k and lie on the two segments joining the root and horizon vertices; their convex hull is exactly C_N. Conversely a root mixture of the four vertex policies realizes every real point of C_N, including irrational mixtures, with tP=tQ=24(1-a-b). Outside the polygon, equality is impossible by the strict Bellman action structure, unsaturated cap condition, nonnegative objective for a+b>1, or infeasibility.

The polygon has exact area (1-rN^2)/8 (integrate horizontal width 4S-3 over S=(a+b) from (3+rN)/4 to 1), increasing to 1/8 as N grows. Thus this is a fully determined all-real contact face, not merely a point estimate.

For Stage254's full parallelogram R254, its x254=0 edge is w254+y*v254, 0<=y<=1. Exact identities are
    w254=horizon-Q, v254=(-r12,+r12),
    w254+v254=horizon-P.
Therefore R254 and C12 share their ENTIRE horizon-Q--horizon-P edge and have disjoint interiors. On that edge H254-K254*(a+b)=24*(1-a-b), where K254=1310563224/20009183>24. The Stage255 exterior target lies strictly inside C12: (a+b)-(3+r12)/4=460211209/18575209267200>0 and both sloping-edge inequalities are strict. Stage254's supporting line is strictly weaker at this target.

## Verification, exposure and next unit

Exact script: STAGE255_EXACT_FACE.py; observed stdout: EXECUTED_EXACT_STDOUT.txt. Python Fraction arithmetic is exact; full-state checking is finite exhaustive; the general theorem is proved algebraically. BRC reuse: typed positive P/Q source likelihood branches and declared observer scope (COMPOSE_APPLIED); native heartbeat/BRC execution was not performed. There is no proved P000 six-dimensional Cell correspondence or physical claim.

Frozen scientific inputs: GLOBAL_KNOWLEDGE_V1 main@7cb24dd235e873a4a13575b5a2206b24679f4682, Enterprise Math main@fa312f0b3a1b798cfde31af9bbb466a39a7ccfea, parent Stage254 commit a538e30f5a6e5c2d83bdf88f56a2837aeea17842. At read, native service v0.6.11 reported research_authority_granted=false and active jobs 5/5; owner query returned CONTROL_QUOTA. This author-side publication is not a native CLAIM, Source Result or independent Driver acceptance.

Stage256: solve a feasible rational point immediately outside C12's sloping side 2a+b=1 or 2a+3b=2 and identify its adjoining nontrivial Bellman support; do not revisit the now-closed Stage254/C12 shared edge.