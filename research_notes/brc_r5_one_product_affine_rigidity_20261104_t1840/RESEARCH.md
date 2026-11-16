# R5 / BRC — One-product affine-observer rigidity theorem

Date: 2026-11-04. Status: AUTHOR_PROVED / EXACT_INTEGER_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.

## Mother target and scope

The R5 objective asks for a positive source/route-sensitive P/Q BRC with equal **complete four-observer convex hulls** for FULL and seedless LR, but different **actual real-policy observation images**. The bypass predecessor produced the reduced occupancy graph z=xy (LR) versus 0<=z<=x and independent 0<=y<=1 (FULL). We analyze **every affine observation of this exact reduced occupancy geometry**, in any real vector space, not the full unrestricted-declaration BRC itself.

Frozen scientific pins: Global `a01383f825ef9d43b4b754254303298c64041568`, EM `86149263e38c22292c9def1e0f69092efa1be77e`. Previous model: `enterprise-math@3e64db6c9d12627a18a3d134a0bdab554391cdf7:research_notes/brc_r5_bypass_information_order_threshold_20261104_t1740/RESEARCH.md`. Current normative rules were independently re-read. P000/ACTIVE worldview unchanged; no native X6 embedding is claimed.

## Theorem, arbitrary real vectors

For any real vector space V and A,B,C in V, define

    F = {x A + y B + z C : 0<=x<=1, 0<=y<=1, 0<=z<=x}
    L = {x A + y B + xy C : 0<=x<=1, 0<=y<=1}.

The following conditions are **equivalent**:
(i) conv(F)=conv(L);
(ii) F=L as actual real-policy images;
(iii) B=0, or B!=0 and C=lambda B for some real lambda>=0.

This includes all boundary cases and all observation dimensions. Adding a common affine translation leaves the conclusion invariant. Thus **an affine readout alone cannot turn this single bilinear coupling into equal hulls with unequal actual images**.

## Complete proof

F is convex: its defining domain is a polytope with six vertices, whose images are

    0, B, A, A+B, A+C, A+B+C.

The LR map is multi-affine and obeys the exact barycentric identity

    x A+y B+xy C = (1-x)(1-y)*0 + x(1-y)*A
                   + (1-x)y*B + xy*(A+B+C).

Therefore conv(L)=conv{0,A,B,A+B+C}. Because L subset F, hull equality is equivalent to BOTH additional FULL vertices P=A+B and Q=A+C lying in the latter four-point hull.

**Necessity 1.** If B,C are linearly independent, take a linear functional ell on their span with ell(B)=1, ell(C)=-1 and extend it linearly to span(A,B,C). Set a=ell(A). LR hull vertex values are {0,a,1,a}, while ell(P)=a+1 and ell(Q)=a-1. If a>0 then ell(P)>max(0,a,1); if a<=0 then ell(Q)<min(0,a,1). Either case is a strict separating certificate. Thus B,C must be dependent.

**Necessity 2.** If B!=0, write C=lambda B. Assume lambda<0. Choose a linear functional ell(B)=1 and set a=ell(A). LR vertex values are {0,a,1,a+1+lambda}. If a>0, ell(P)=a+1 exceeds each of these. If a<=0, ell(Q)=a+lambda lies below each of these. Contradiction. Hence lambda>=0.

**Sufficiency, with a real strategy reconstruction.** For B=0 and any FULL (x,y,z), set LR y'=z/x when x>0, otherwise y'=0. Then xy'=z and observers match. For B!=0, C=lambda B, lambda>=0, take

    y'=(y+lambda*z)/(1+lambda*x).

The bound 0<=z<=x ensures 0<=y'<=1, and the LR output equals
xA+y'(1+lambda*x)B=xA+(y+lambda*z)B, exactly the FULL output. Reverse inclusion L subset F is automatic, so F=L. This proves (iii)=>(ii)=>(i)=>(iii).

The common image is an affine triangle {xA+zC:0<=z<=x<=1} if B=0, or an affine trapezoid {xA+tB:0<=x<=1,0<=t<=1+lambda*x} for nonzero B with lambda>=0. Degenerate affine images are included.

## Exact examples and executed verification

The standard-library integer/Fraction program `VERIFY.py` was actually executed. For each of 15,625 triples A,B,C in {-2,-1,0,1,2}^2, it computes COMPLETE finite convex-hull membership for the two extra FULL vertices using exact singleton, nondegenerate segment and barycentric triangle tests (2D Caratheodory). The conjectured linear-algebraic criterion agrees in every case: 2,225 equal-hull triples, 13,400 strict-hull triples. This covers only that finite integer box; the all-real result comes from the proof above.

Rational strategy reconstruction: A=(1,1),B=(1,0),C=(2,0), y'=(y+2z)/(1+2x), checked for 75 rational FULL triples. B=0 with A=(1,0),C=(0,1) gives y'=z/x and 75 more exact checks.

Two independent strict certificates, both using FULL x=1,y=0,z=1 and normal n=(1,-1):
- A=(1,1),B=(1,0),C=(0,1): W=(1,2), min_LR<n,.>=0, <n,W>=-1; gap 1.
- A=(1,1),B=(1,0),C=(-1,0): W=(0,1), min_LR<n,.>=0, <n,W>=-1; gap 1.

All program assertions passed: `PASS_EXACT_R5_ONE_PRODUCT_AFFINE_RIGIDITY`. See `EXACT_OUTPUT.txt`. No floats, Monte Carlo, or external oracle. All-real proof, finite checks and project admission are separate evidence levels.

## Boundary and next scientific question

This theorem applies to a **single product** with affine readout. The unrestricted free-declaration BRC has additional error fibers and can have different feasibility geometry. It does not prove anything new about complete four-coordinate O4 equality in all BRCs and does not settle R5. The result eliminates a concrete proposed route: merely changing the affine observer dimension, weights or compression of (x,y,z) cannot meet the R5 mother target. The next test should introduce two genuinely independent occupancy products or a changed positive-flow topology, derive the full O4 observer map with free P/Q declarations, then certify complete hull membership before nonlinear real-image nonmembership.

No native CLAIM, Result, Driver review, mathematical acceptance, external novelty, or P000 promotion is claimed.
