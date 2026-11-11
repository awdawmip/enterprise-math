# R5: a sharp three-atom A→B bridge in the frozen Blackwell fiber

Date: 2026-11-11 (Asia/Shanghai). Status: author-side exact auxiliary-model theorem, awaiting independent mathematical review and formal Source Result.

## Frozen model and dependencies

Scientific inputs are unchanged from R5 PR #2063: account source a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math source 86149263e38c22292c9def1e0f69092efa1be77e. Immediate exact dependency: PR #2072, commit 9708a8b5ba1870bb423577c50144c1acfa7606dd (two-atom A→C and nine one-atom Farkas exclusions). PR #2063 establishes the complete census of exactly three feasible source-3 four-target masks. All numeric inputs are reproduced in VERIFY_BRIDGES.py.

The seven target ratios are R=(2,10,15,20,25,30,38). Nonnegative labeled transfers x(i,j) have source j∈{1,2,3,5}, target i∈{0,...,6}, and satisfy Ax=b where A has fifteen observer rows (seven target marginals, four source marginals, four source R-weighted moments), rank 13. The full 30-arc model has two additional fixed positive singleton arcs (0,0) and (6,6), with full observer rank 15. Source-3 masks are A={1,3,4,6}, C={2,3,4,6}, B={2,3,4,5}. Only these three four-masks are feasible in the frozen fiber (PR #2063).

A signed elementary atom is one six-arc K_(2,3) residual supported on source pair {3,j}, j∈{1,2,5}, and a target triple. Its two source rows are opposite, with zero mass and R-moment sums. Each legal atomic move is a nonnegative line segment in the same observation fiber. Minimize the count of such moves subject to source-3 positive-target support never exceeding five.

## Exact theorem

The minimum number of elementary residual moves from some transfer in the A face to some transfer in the B face, under the source-3 peak-support five bound, is **exactly 3**:

N_atomic(A,B; peak source-3 support ≤5)=3.

More precisely N_atomic(C,B; peak ≤5)=1. The earlier result N_atomic(A,C; peak ≤5)=2 is reused.

### Upper bound: explicit A→C→B

Start from the complete 28-rational vector X_A reproduced from PR #2072 in VERIFY_BRIDGES.py. The first source-pair {3,1} atom H1 has source-3 target coefficients (-23,+28,-5) on (1,2,6); its exact scale is t1=4023851/1367527721. The second source-pair {3,2} atom H2 has the same source-3 coefficients and t2=196521/67951688. The resulting X_C has mask C and source-3 target-6 mass 3930420/195361103.

The new third atom H3 uses source pair {3,5}, targets (2,5,6), source-3 row (-8/15,+23/15,-1), and the opposite source-5 row. Its identities are -8+23-15=0 and 15(-8)+30(23)+38(-15)=0. Set t3=3930420/195361103 and X_B=X_C+t3 H3. This deletes target 6 and creates target 5, with final mask B.

Exact verification checks 15 observer equations, nonnegative masses on all 28 dynamic arcs at the four states X_A, X_A+t1H1, X_C, X_B, unchanged positive singleton arcs, and target masks A, A∪C, C, B. Convexity certifies the entire segments. The four strictly positive source-3 masses at the final B point are: target 2=2592967/16987922; target 3=377644447/2548188300; target 4=1544855/16987922; target 5=262028/8493961.

### Lower bound: exhaustive 144-case exact Farkas obstruction

One elementary atom changes at most three source-3 target labels, whereas A△B={1,2,5,6} has four, so one move is impossible.

For any hypothetical two-atom path with maximum source-3 support five, both atoms must act on source 3. Classification of the first move, using the complete source-3 minimum-four-mask census and the conservation identities, gives precisely three cases:

* OLD (108 labeled cases). First introduce one of the two missing targets, 2 or 5, acting on two of the four old targets in A; the second must introduce the other missing target while eliminating the two old targets 1 and 6. There are 2×C(4,2)×3×3=108 source-labeled possibilities. If the intermediate support falls to four, the only potentially feasible different four-mask is C, but the previous PR #2072 excludes an A→C single atom.
* DOUBLE (18 labeled cases). First introduce both new targets 2 and 5, simultaneously eliminating a shared target u∈{3,4}; the second restores u and eliminates 1 and 6. The old targets 1 and 6 cannot be the eliminated first target since their R ratios 10 and 38 are outside the interval [15,30]. There are 2×3×3=18 choices.
* TRANSIENT (18 labeled cases). First introduce temporary target 0 and one of 2 or 5, eliminating old target 1; the second removes 0 and 6 while introducing the other new target. All other transient-target arrangements either require an infeasible intermediate four-mask or more than three altered target labels in the second move. There are 2×3×3=18 choices.

VERIFY_NO_TWO_ATOMS.py enumerates these 144 possibilities. Each gives a nonnegative feasibility system Bz=d with 83 variables: 25 allowed initial A-arc masses, 2 nonnegative move amplitudes, 28 nonnegative intermediate slacks, and 28 nonnegative final slacks. The 74 equalities are the 15 frozen observation equations, 28 intermediate endpoint equations, 28 final endpoint equations, and final target-0, target-1 and target-6 source-3 zeros.

The file FARKAS_CERTS.b85 is a text-encoded zlib/base85 compressed JSON map from each of the 144 case identifiers to a sparse integer dual vector y∈Z^74. The exact, optimizer-free verifier unpacks it and checks all 83 integer coefficient inequalities Bᵀy≥0 and the strict rational inequality dᵀy<0 separately for every case. If a nonnegative z solved Bz=d, then 0≤zᵀBᵀy=dᵀy<0, a contradiction. All 144 cases fail. Therefore no two-atom path exists under the stated peak-support bound, and the constructive three-atom path is optimal.

The certificates were found through floating-point LP exploration followed by exact rational reconstruction. The published proof objects are the integer dual vectors and the exact Fraction verifier, not the floating-point feasibility flags. The certificate file decompresses to a plain JSON object; no third-party packages or network access are required to check it.

## Verification, provenance, next unit

Run: python3 VERIFY_BRIDGES.py && python3 VERIFY_NO_TWO_ATOMS.py. Both scripts are deterministic standard-library Python. EXACT_OUTPUT.txt records the successful execution including PASS_R5_EXACT_C_TO_B_ONE_ATOM_AND_A_TO_B_THREE_MOVE_WITNESS and PASS_R5_EXACT_144_TWO_ATOM_FARKAS_CERTIFICATES. No native X6 dynamics or P000 promotion is claimed.

Next: test optimality without the source-3 support ceiling, classify alternate three-step itineraries, and derive a concise analytic source-port capacity obstruction replacing the 144-case dual census. The present result remains an author-side exact theorem until independent Source review.