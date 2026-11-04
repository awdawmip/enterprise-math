# Stage434-B — Parameterized native-X6 future quotient with exact codebook

2026-11-04 · Research2 · AUTHOR_SIDE_PROOF / EXACT_INTEGER_EXECUTED / UNREVIEWED / NOT_ADMITTED.

Frozen scientific inputs: GLOBAL main@bf84bd7c61a2444b59b1da96be57df0e9ae47e53; EM main@2af3fc484eb11060b69e0afc1b562bcaf5ad1419; original P000 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488. Parent Stage433-B commit c092446161ebce5d844c8429078d0535992b6e2a. Chart-relative displacements remain native X6 quantities. The observer below records full directed J and the absolute-index match K.

## Population and observation

Fix A=+E1, B=-E1, C=+E2 in the twelve signed-native-X6 direction alphabet. Let integers m,n,p,r satisfy n>=2, 0<=p<=n-1, r>=1, m>=n+r+2. For every b in {2,...,m-1} form P^(b)=A^(b-1) B A^(m-b) and Q=C^n. The observer is (m,n,xP,xQ,JP,JQ,K), where x is the six-component endpoint displacement, J lists all directed adjacent label counts, and K is the number of matching labels at identical absolute positions up to min(m,n). P remains fixed. Each legal future operation word has at most p terminal POPs of Q and at most r APPENDs by an arbitrary native direction. Every intermediate complete observation and operation legality is compared.

## Theorem 434.1 — Complete common observer fiber

The entire native-X6 fiber determined by this current observer comprises exactly the m-2 pairs (P^(b),C^n), with b=2,...,m-1. The common observer values are xP=(m-2)E1, xQ=nE2; JP(AA)=m-3 and JP(AB)=JP(BA)=1, all other JP zero; JQ(CC)=n-1 and others zero; K=0.

Proof. For a nonempty directed-label word w,
x(w)-sum_{u,v}J_w(u,v)vec(v)=vec(w_1).
This identity recovers the first label using twelve distinct signed-axis vectors. Thus the first P label is A and the first Q label is C. Directed Euler traversal must use the unique A->B->A excursion, all other P edges being AA; B is at one internal position. Q follows only CC edges. The current K is zero because Q is all C while P uses A and B. This enumerates the whole fiber and certifies unit integral BRC mass per original history.

## Theorem 434.2 — Exact future-equivalence quotient

Put a=n-p+1, z=n+r and I={a,...,z}, of size p+r. Then the exact future-observation equivalence classes on the above complete fiber are

F_0={b: b not in I} and F_j={j} for each j in I.

Hence q_F(p,r)=p+r+1, with positive integer populations mass(F_0)=m-2-p-r and mass(F_j)=1 for every j in I.

Proof of sufficiency. In every legal future, Q's original positions i<a remain C: at most p POPs can remove original suffix labels. Positions i>z are never reached because there are at most r APPENDs. Original C labels cannot match either A or B. On accessible positions i in I, each history has P_i=A except for its single B if b lies in I. Thus the class exactly determines K for every operation prefix. Endpoint and JP of P are common, and the Q endpoint, JQ, length and legality are determined by initial Q and the shared operation word. All complete observer traces descend through these classes.

Proof of necessity. For each j in I choose a legal future word making its final K equal [b=j]. If j<=n, perform n-j+1 POPs followed by APPEND(B); if j>n, append C exactly j-n-1 times and then B. All other Q labels are C and cannot match A/B. The budgets follow from a<=j<=z. Thus every singleton is distinguishable from each other singleton and from F_0. By m>=n+r+2, b=z+1 is a valid outside representative, so F_0 is nonempty. These two directions establish the exact quotient.

## Corollary — Repeated budget-dependent splitting

At the same fiber, provided p+1<=n-1, q_F(p+1,r)=q_F(p,r)+1. Provided m>=n+r+3, q_F(p,r+1)=q_F(p,r)+1. This gives arbitrary finite runs of strict splits by choosing n,m sufficiently large.

## Exact codebook and resources

Encode a history with defect at b as k=0 when b is outside I, otherwise k=b-a+1. Decode k=0 to canonical representative b=z+1; k>0 to b=a+k-1. The fixed-length minimal class label costs ceil(log2(p+r+1)) bits; storing exact b in the same known fiber costs ceil(log2(m-2)) bits. The analytic codebook is a closed-form map, so construction uses O(1) arithmetic description and O(p+r) enumeration if explicit entries are wanted.

On ordinary raw word input, identifying and checking the one-defect fiber, endpoint and J takes O(m+n) word operations, with O(log(m+n)) bit counters. With b already indexed, class assignment is O(1) word operations. For an operation at Q absolute position i, the class reader updates K by one comparison with the expected P letter: 0 for i<a (protected C), A for i in I except the distinguished k>0 position, and B at that distinguished position. It updates Q endpoint/J and the terminal stack by local operations; six spatial components are fixed-size and integers have O(log(m+n+p+r)) bits. Recovering a canonical full P word takes O(m); recovering the exact original when k=0 requires separately retaining b. The full input-to-class and class-to-observer costs are therefore explicit. This is a future-observer compression, with exact BRC integer class populations.

## Verification

Run Node.js 22: node REPRO_STAGE434B.js. Exact integer checker covers all twelve primitive signed directions and all legal operation words for five cases (m,n,p,r)=(8,3,0,1),(9,3,1,1),(10,3,1,2),(11,4,2,2),(13,5,3,2). It exhaustively compares full intermediate observer traces of the complete fiber and tests a separate O(1)-per-step quotient reader, individual distinction witnesses, complete class masses and bijective class representatives. Results: 41 original histories, 5,184 enumerated legal operation words, 155 history-pair comparisons, 135 exact witness evaluations and 28,195 quotient-reader/full-trace comparisons. The original code executed under Node.js 22 locally and the identical source string was executed in the GitHub connector's JS runtime; both passed, matching REPRO_STAGE434B_EXECUTED.json. Infinite-parameter statements follow from the proof.

## Next

Stage435-B: multiple nonadjacent B defects (k>=2), exact transfer-matrix enumeration of J-fixed fibers and class populations, distinguishing future tests, and input-to-class costs compared with full Euler enumeration.
