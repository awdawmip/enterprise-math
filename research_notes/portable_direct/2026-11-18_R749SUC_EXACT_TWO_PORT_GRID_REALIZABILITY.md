# R749SUC — Exact feasible two-port rank-one stability-grid signatures

Date: 2026-11-18 (Asia/Shanghai). Evidence grade: **AUTHOR_EXACT_NOT_REVIEWED**. Scope: positive-rational recurrent BRC visible ports with WBRC-T30..T32 at the unchanged scientific pin `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`. Independent portable continuation of R749SUA / R749SUB (Draft PR #2679). No shared-task CLAIM or native X6 triadic event permission asserted.

## Main theorem: complete characterization of rational two-port stars

Let W be a 2x2 nonnegative rational matrix with spectral radius <1 and named visible ports 1,2; define S=(I-W)^(-1)=[[A,B],[C,D]] and Δ=AD-BC.

**Theorem 1 (feasible-star characterization).** A finite rational quadruple (A,B,C,D) arises this way if and only if

    A>=1, D>=1, B>=0, C>=0, Δ>=max(A,D)>0.

**Proof.** For a baseline-stable nonnegative W=[[a,b],[c,d]], the inverse is S=(1/det(I-W))*[[1-d,b],[c,1-a]]. Thus A,D>=1 by the Neumann series, B,C>=0, Δ=1/det(I-W)>0 and
W=I-S^(-1)=[[1-D/Δ,B/Δ],[C/Δ,1-A/Δ]]. W>=0 gives Δ>=max(A,D).
Conversely assume all listed inequalities. Then W=I-S^(-1) has nonnegative rational entries and its (I-W)^(-1) is the declared entrywise-nonnegative S. Taking v=S*(1,1)^T>0 yields Wv=v-(1,1)^T<v, so by the positive-vector Perron comparison rho(W)<1. QED.

Equivalently, the offdiagonal guard entries obey

    B*C <= A*D-max(A,D).

In particular, the four threshold guards in R749SUB are constrained by joint realizability: the formally possible (M+1)^4 grid vectors need not all arise from genuine nonnegative stable two-port modules.

## Sharp finite-grid realizability theorem

Fix integers K>=2, 1<=M<K. Each ordered pair is tested with resettable rank-one edge weights t=j/K for j=1,...,M, and the bit is 1 exactly if t*S[j,i]<1. The observed number of unstable tests is h(s)=#{1<=j<=M: j*s>=K}. A four-entry signature can be indexed as (h(A),h(D),h(B),h(C)).

Define lower bounds for offdiagonal bins

    L_0=0; L_h=K/(M-h+1), 1<=h<=M.

For each *diagonal* bin h, its exact rational interval is:
    h=0:  [1,K/M)
    1<=h<M: [K/(M-h+1),K/(M-h))
    h=M: [K,+infinity).

Write U_h=K/(M-h) for h<M and U_M=+infinity. Offdiagonal bins have the same lower limits L_h, but h=0 starts at 0 rather than 1.

**Theorem 2 (exact realizability and class count).** A vector (i,j,x,y) in {0,...,M}^4 is the observation signature of some rational baseline-stable nonnegative two-port W if and only if either U_i or U_j is infinite, or

    L_x*L_y < U_i*U_j-max(U_i,U_j).

Consequently, with the bracket denoting 0 or 1,

    N(2,K,M) = sum_{i,j,x,y=0}^{M}
                   [ U_i=infinity OR U_j=infinity
                     OR L_x*L_y < U_i*U_j-max(U_i,U_j) ].

This is an exact finite integer-sum formula valid for every K>=2, 1<=M<K. The optimal fixed-width storage cost for the complete resettable finite-grid observer is ceil(log2 N(2,K,M)) bits.

**Proof of necessity.** From Theorem 1, BC<=F(A,D)=AD-max(A,D). The cross entries are at least their bin lower bounds. With both upper diagonal bounds finite, A<U_i and D<U_j. Since A,D>=1 and F is nondecreasing in both arguments (indeed strictly increasing on (1,infinity)^2), F(A,D)<F(U_i,U_j). Therefore L_xL_y< F(U_i,U_j).

**Proof of sufficiency.** For finite upper diagonal bounds, each upper endpoint U is >1. Choose rational A and D within their permitted half-open bins sufficiently close to their respective upper endpoints that F(A,D)>L_xL_y; set rational B=L_x,C=L_y. Then Δ=AD-BC>max(A,D) and Theorem 1 supplies the stable rational W=I-S^(-1). When one diagonal bin is unbounded, choose its diagonal entry sufficiently large and the finite other entry strictly above 1; the resulting F grows without bound. When both are unbounded, increase both. Thus all grid signatures satisfying the criterion are realized, proving the exact count. Finally, different signatures have some distinguishing guard bit, while an adaptive sequence of resettable probes sees only this signature. Injectivity on the realized classes and pigeonhole prove the bit bound. QED.

A boundary subtlety matters: the diagonal upper bins are open, so the inequality is **strict** even though Theorem 1 permits the matrix inequality BC<=F(A,D). Replacing < by <= overcounts impossible signatures.

## Exact evaluation for K=4, M=3

The 16 counts of realizable cross-pair (x,y) combinations, indexed by the diagonal labels (i,j), are

    [ [ 7,  7,  7, 16],
      [ 7,  8, 10, 16],
      [ 7, 10, 15, 16],
      [16, 16, 16, 16] ].

Summing yields

    N(2,4,3)=190; 256-190=66 formally possible signatures are impossible.

The exact minimal fixed-width complete observer memory is

    ceil(log2(190))=8 bits.

This sharpens R749SUB's general lower/upper bound 16<=N(2,4,3)<=256. A 4-bit signature is insufficient; 8 bits is necessary and sufficient under this precise observer.

The same exact integer-sum formula yields:
    K=2,M=1: N=15, bit cost 4;
    K=3,M=2: N=68, bit cost 7;
    K=5,M=2: N=70, bit cost 7;
    K=5,M=4: N=426, bit cost 9;
    K=7,M=3: N=204, bit cost 8.

## Validation and reproducibility

Companion `R749SUC_TWO_PORT_GRID_REALIZABILITY_CERT.py` uses only Python standard-library Fraction. It enumerates every candidate grid signature for all six (K,M) examples above. For *every* predicted feasible signature, it explicitly constructs rational A,B,C,D satisfying the correct bins and positive-rational baseline matrix W, then rechecks the exact rank-one guard signatures and strict stability using the 2x2 determinant. Each predicted excluded signature is counted separately. The code ran locally and returned PASS; the captured exact JSON is `R749SUC_TWO_PORT_GRID_REALIZABILITY_RESULTS.json`. The infinite family over integer K,M follows from the preceding proof, not finite enumeration.

This is an observer-relative WBRC positive-mass signature theorem; P000's native six-dimensional Cell addresses, source/branch provenance, independent time and triadic closure remain unchanged. Full X6 event-license and causal/resource observations remain a separate scientific research frontier. No independent review, Result/Review promotion or deployment occurred.

## Next research direction

Analyze asymptotics of N(2,K,M) when K,M grow with M/K fixed and derive an efficient exact lattice-count formula. For a physical X6 claim, identify a genuinely licensed time-ordered triadic Cell/Link/Port operation with preserved sources and resource guards and compare its observable quotient to the abstract WBRC Port guard.