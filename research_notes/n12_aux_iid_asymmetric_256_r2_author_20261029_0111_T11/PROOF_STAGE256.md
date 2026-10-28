# Stage256 — adjacent all-real Bellman face (author exact proof)

2026-10-29. **AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED**. Parent Stage255 immutable commit 25e42b0aec8a43c826983ce9a31b4a40eb1d5b0e (Draft PR #1571). This is an **external ternary IID auxiliary model**, not native P000 X6 dynamics.

## Statement

Let P=(1/8,1/24,5/6), Q=(1/12,1/12,5/6), maximum observation depth N=12. A full ordered-history randomized stopping/classification policy has errors eP=Pr_P(declare Q), eQ=Pr_Q(declare P) and times tP=E_P[depth], tQ=E_Q[depth]. Let V12(a,b) be the minimum of max(tP,tQ) over policies with eP<=a,eQ<=b, and +infinity if infeasible. The parameters a,b range over all real [0,1], and policy randomization may use arbitrary real probabilities.

The exact one-sided time dual is

    lambdaP=23219011584/292565255,
    lambdaQ=15120288852/292565255,
    thetaP=0, thetaQ=1, H=lambdaQ.

The four complete-observer vectors (eP,eQ,tP,tQ) are

    A   =(0,1,0,0);
    B12 =(1932641711/8707129344,2420922961/4353564672,
          1932641711/362797056,1932641711/362797056);
    C12 =(30348774917/139314069504,9753923645/17414258688,
          31316233733/5804752896,7902199747/1451188224);
    C1  =(1743753479/46438023168,16033302265/17414258688,
          2066239751/1934917632,1622821127/1451188224).

Write R256=conv{error(A),error(B12),error(C12),error(C1)}. Those four points are in cyclic order and are strictly convex, with area

    512352908401406665/606512811305166962688 > 0.

**Theorem (complete real contact region for this dual).** For every real (a,b) in [0,1]^2,

    V12(a,b) = H - lambdaP*a - lambdaQ*b
        IF AND ONLY IF (a,b) lies in R256.

Stage255's C12 contact polygon lies on 2a+b>=1; R256 lies on 2a+b<=1. Their intersection is precisely the FULL common edge A--B12, not merely one endpoint. Their interiors are disjoint. This closes Stage256's slanted-edge adjacent-face problem.

An interior rational example is the equal root mixture of A,B12,C12,C1:

    a=33251151365/278628139008;
    b=26442588221/34828517376;
    V12(a,b)=tQ=8627793859/2902376448;
    tP=34218610181/11609505792 < tQ;
    1-2a-b=292565255/139314069504 > 0.

## Universal dual lower bound

For counts s=(i,j,k) of symbols (0,1,2), 0<=i+j+k<=12, the full ordered-history likelihood quotient is exactly

    L(s) = Q(h)/P(h) = (2/3)^i*2^j.

The P-normalized conditional Bellman value of tQ+lambdaP*eP+lambdaQ*eQ obeys

    H(s) = min{ lambdaQ*L(s) [declare P],
                lambdaP      [declare Q],
                L(s) + sum_z P(z)*H(s+unit_z) [continue] },

with no continuation at depth 12. The likelihood quotient depends on counts because both distributions are IID; this is an observer-specific sufficient statistic, NOT an erasure of ordered history for other observables.

An exhaustive exact-Fraction recursion checks all 455 states and 1,274 available action costs. H(0,0,0)=lambdaQ, 806 candidate action costs have strictly positive gaps, and the **only 13 tie states** are (0,0,k), k=0,...,11 (declare P/continue), and (0,1,0) (declare Q/continue). The neutral terminal (0,0,12) uniquely declares P. Thus the dynamic-programming induction is valid for every randomized complete-history policy and implies

    tQ+lambdaP*eP+lambdaQ*eQ >= lambdaQ.

Both multipliers are strictly positive. Therefore every feasible policy obeys

    max(tP,tQ) >= tQ >= H-lambdaP*a-lambdaQ*b.    (1)

For transparency, the exact dual is determined from the neutral tie and the first-symbol-1 tie by the two rational equations

    -1 - lambdaP/24 + lambdaQ/12=0;
    -171632903/60466176
      +(191164153/1934917632)*lambdaP
      -(70231801/725594112)*lambdaQ=0.

The displayed rational pair solves them. All Bellman inequalities are separately verified, not assumed from these two equations.

## Primal policies, full-face sufficiency and necessity

A declares P immediately.

For every integer k=1,...,12, B_k continues through at most k consecutive neutral symbols 2, declares P upon first 0, Q upon first 1, and P after k neutral symbols. With r_k=(5/6)^k, exact source-mass summation gives

    B_k=((1-r_k)/4,(1+r_k)/2,6*(1-r_k),6*(1-r_k)).

C_k uses the same neutral-depth stopping rule, but after a FIRST observation 1 it chooses continuation (the unique nonneutral Bellman tie) rather than declaring Q, thereafter obeying the unique exact Bellman-minimizing nonneutral actions. The difference C_k-B_k is independent of k because this first-symbol-1 branch is disjoint from every neutral-prefix stop decision:

    Delta=(-191164153/46438023168,
            70231801/17414258688,
            131322119/1934917632,
            171632903/1451188224).

In particular Delta_tQ-Delta_tP=292565255/5804752896>0, while 2*Delta_eP+Delta_eQ=-292565255/69657034752<0.

Every B_k error pair is on the segment A--B12 and every C_k error pair is on the segment C1--C12, with endpoints C_k=B_k+Delta. Because the only Bellman ties are the 13 states above, every Bellman-optimal deterministic complete-history policy coincides, up to unreachable histories, with A, one B_k or one C_k. General randomized full-history policies are convex mixtures of deterministic policies on this finite decision tree. Therefore the entire Bellman equality set's error projection is exactly R256.

All these deterministic equality strategies have tQ>=tP: equality for A and B_k, strict inequality Delta_tQ-Delta_tP>0 for C_k. Thus for ANY real (a,b) in R256, root-randomize among the four displayed vertex policies so that its error pair equals (a,b). This saturates both caps, attains equality in (1), and has tQ>=tP. Hence V12(a,b) equals the affine lower bound, proving sufficiency.

Conversely, if an attainable V12(a,b) equals the affine support, an optimizer exists because the finite-horizon randomized decision-tree policy space is compact and error/time maps are continuous. Positive lambdaP/lambdaQ force both errors to saturate their caps. Equality in (1) forces all positive-source-reach actions to be Bellman-minimizing; hence their error pair lies in R256. This proves necessity, including irrational caps and all boundary cases. Strict convexity and the shoelace area are checked by exact rational cross products.

The old Stage255 C12 polygon has 2a+b>=1 and contains all of A--B12, whereas our R256 has 2a+b<=1 with strict inequality off that side. Their shared edge is precisely A--B12.

## Executed evidence and limits

STAGE256_EXACT_ADJACENT_FACE.py is a Python-standard-library Fraction certificate. It exhausts 455 states and 1,274 actions; separately computes all 24 B_k/C_k policies through count-state recursion and **unmerged complete-ordered-history DFS** tracking both P and Q positive rational masses. It checks both source terminal masses are exactly one, visits 888 ordered-history nodes and 600 terminal branches in aggregate, and checks all four observers, 806 strict gaps, 13 ties, the uniform Delta, convex face and interior point. EXECUTED_EXACT_STDOUT.txt is the observed run output.

The all-real/complete-policy statement follows from the induction, finite deterministic-policy decomposition and compactness, not from interpreting finite testing as an unbounded numerical fit. This is BRC-compatible use of **typed positive source masses/provenance**, not native heartbeat BRC arithmetic. No physical or X6 transfer theorem, independent Driver review or native CLAIM/Result exists for this author artifact.

Frozen reads: GLOBAL_KNOWLEDGE_V1 main@cc98fc94fcd893e8e73223f39ea3adbe5d471645, Enterprise Math main@996de464c253d08520c7c5d0e5c814c676cd9777; canonical P000 projection blob 770e1b157fc10aab7b25d80c2cd52d6fcd07c9dc matched original. Native service v0.6.11 at this run reported research_authority_granted=false, job quota 5/5 and CODE_REVIEW_REQUIRED, so owner and formal CLAIM were not verified. Do not promote this author-side result above AUTHOR_EXACT / UNREVIEWED / NOT_ADMITTED.

Next exact research unit: Stage257, seek the adjacent support beyond translated edge C1--C12 given by 2a+b=1-292565255/69657034752, with exact feasibility, four-observer primal policy and global Bellman certificate.