# R5 — Seedless-F targets escape the zero-row face: exact lawful positive-mu1 witness and full rank-15 Blackwell carrier

Date: 2026-11-10 (Asia/Shanghai).
Status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / INDEPENDENT_REVIEW_PENDING.
Research mode: auxiliary seven-node likelihood-ratio Blackwell/P-Q-BRC statistical observer; seven statistical labels are not native P000 space axes. P000 remains six-dimensional native X6 space plus separately typed time.

## Frozen provenance and specific open question

Frozen science remains GLOBAL a01383f825ef9d43b4b754254303298c64041568 and Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Relevant immutable predecessors: PR #1859 (mass map and physical constraints), commit f63a0250714f2445e8b406754b85f26d983ec3a6; PR #1873 (transverse physical chart), commit 2cd0988e8461607db04312b05304dcb1c4630340; and PR #1889 (exact universal 14-edge theorem when mu_1=nu_4=0), commit b269751faa1996a1e1a6c8342817e1d00571d560.

The unresolved prerequisite proposed by PR #1889 is whether ALL lawful seedless-F targets obey mu_1=0. This research answers NO and exactly classifies the rank/support genericity of the larger statistical face nu_4=0, then supplies one fully feasible physical matched-time Blackwell pair in the omitted region.

Set the ordered likelihood ratios r=(1/10,1/2,3/4,1,5/4,3/2,19/10). A nonnegative transport E from source index j to target index i must satisfy the 21 exact equations:

    sum_j E_ij = mu_i,                    i=0,...,6
    sum_i E_ij = nu_j,                    j=0,...,6
    sum_i r_i E_ij = r_j nu_j,            j=0,...,6.

All arithmetic used in the certificate is exact rational arithmetic. The generic real-convex-geometric theorem is proved separately below.

## Theorem 1: lawful seedless F with mu_1>0 and 30 positive admissible transport edges

Let physical-flow coordinates be (g,a,b,u,v,w,z). Use exactly these rational tuples:

    X0=(999/1000,1/6,999/1000,1/20,29/240,11/160,1/120)
    Y0=(1,2002911/10904720,26095487/40892700,
        442758619/6542832000,11037627/68154500,
        394502727/2180944000,2002911/109047200)
    H=17774559/17507527960
    X=X0+(H/2)*(0,0,0,0,0,0,1)
    Y=Y0+(1/100000)*(0,1,0,-1/4,-1/4,0,1/10).

Claim: X is a lawful FULL_HIST source with g=b. Y is a lawful seedless-F target with g=1 and z=a/10. All 13 explicit capacity inequalities hold; both stopping-time coordinates are exactly (17609/6000,33857/12000), and normalized marginals nu=M(X), mu=M(Y) obey

    nu_4=0,                 mu_1=23/4000000>0.

There is an exact nonnegative Blackwell coupling E with all THIRTY admissible entries strictly positive; min E_ij=1/10000000.

Proof: the companion VERIFY.py contains the complete rational mass map M, stopping-time formulas, and all 13 physical-capacity slacks. Direct exact evaluation verifies the above facts, including the only zero source slack g-b and the two tight target slack constraints 1-g and a/10-z. In the frozen model, extremal LR columns 0 and 6 have only their diagonal admissible edge. Because nu_4=0, column 4 vanishes. The full fixed 30-edge carrier is

    D={(0,0),(6,6)} union
      {(i,j): 0<=i<=6, j in {1,2,3,5}}.

Let A_e denote the 21-vector of transport column e=(i,j) with coefficients 1 at row i, 1 at row 7+j, r_i at row 14+j, and zero elsewhere. Let h=(mu,nu,(r_j nu_j)_{j=0}^6).

Take the following ordered 15 columns:

    B=((0,0),(0,1),(2,1),(0,2),(2,2),(4,2),
       (0,3),(1,3),(3,3),(4,3),(5,3),
       (4,5),(5,5),(6,5),(6,6)).

Take row indices

    I=(0,1,2,3,4,5,6,7,8,9,10,12,15,16,17).

The rational minor has det A[I,B] = -299/1600, so it is invertible. Define tau=1/10000000, d=h-tau*sum_{e in D}A_e and w=(A[I,B])^{-1}d[I], using exact Gaussian elimination. The computed vector satisfies min(w)=107/20000000>0. Assign E_e=tau+w_k to the 15 basis edges e=B_k, and E_e=tau to the remaining 15 edges.

The verifier checks all 21 Blackwell equalities individually, not just the selected 15 pivot equations; it also checks both physical strategies, both stopping times, all capacity slacks, normalized margins, and positive transport weights. Every assertion succeeds with standard-library Fraction. Thus the explicit E is a rigorous rational feasibility witness, with 30 strictly positive edges. QED.

Consequence: seedless-F does not imply mu_1=0. Hence PR #1889's uniform 14-edge result for the smaller face mu_1=nu_4=0 cannot alone prove the desired bound over the whole seedless g=b physical family. Importantly the positive-mu_1 point is also physically lawful and Blackwell-feasible with matched stopping times.

## Theorem 2: rank 15, universal 15-edge upper bound, and ambient generic sharpness

For EVERY normalized pair of nonnegative 7-node marginals with nu_4=0 and at least one nonnegative Blackwell coupling, some coupling has at most 15 positive entries. For GENERIC such feasible marginal pairs in the complete nu_4=0 face, every coupling requires at least 15 positive entries. Therefore 15 is the exact generic minimum for that full feasible normalized marginal face.

Proof: nu_4=0 forces the entire j=4 source column zero. As r_0<r_i<r_6 for every internal i, the moment equations and nonnegativity make source column j=0 supported only on (0,0), and column j=6 only on (6,6). Thus D is a complete allowed support of 30 edges.

Let A_D have the 21 equality rows and 30 columns. Rank(A_D)<=15: the nontrivial rows are the seven target mass sums, six source mass sums on columns 0,1,2,3,5,6, and four internal source moment rows j=1,2,3,5. Among these 17 rows there are exactly at least two global dependencies: equality of total target/source mass and equality of target/source likelihood-ratio weighted mass. Hence rank<=7+6+4-2=15. The exact minor det A[I,B]=-299/1600 is nonzero, so rank(A_D)=15.

For any feasible margins h, the normalized nonnegative fiber {E>=0:A_D E=h} is a nonempty bounded polytope, because the total edge mass equals 1. Any vertex E has linearly independent columns indexed by its strictly positive entries: a dependent positive-support perturbation permits two distinct feasible nonnegative matrices with midpoint E, contradicting extremality. Hence a vertex has at most rank(A_D)=15 positive edges.

For generic sharpness consider the 15-dimensional image cone K=A_D(R^30_{>=0}). Theorem 1 constructed a strictly positive E in all 30 coordinates, so K has nonempty relative interior in the 15-dimensional column span. The normalized section total mu=1 therefore has dimension 14 and nonempty relative interior. A fixed support of at most 14 edges maps, after normalization, to an affine set of dimension at most 13. There are only finitely many such supports. Their union has zero relative 14-dimensional Lebesgue measure and empty relative interior. Thus generic normalized feasible marginal pairs in this face require at least 15, while the vertex theorem yields at most 15. QED.

Quantifier scope: generic sharpness is proved for the COMPLETE normalized statistical marginal face nu_4=0. The legal g=b source / seedless F target / equal-stopping-times subfamily is a lower-dimensional constrained subset. Theorem 1 places a legal physical point with mu_1>0 into the full-rank feasible region, but does not certify that this particular point needs 15 rather than 14 edges.

## Reproduction and scientific next action

The checked source is VERIFY.py (no nonstandard libraries, floats, external solver, symbolic assumptions, or hidden data). EXACT_OUTPUT.txt is its actual complete terminal stdout. The theorem's generic statement follows from the rank proof and a finite union of proper subspaces, not from a finite sample. BRC statistical branch labels and positive masses are preserved. This is static auxiliary Blackwell theory, not native heartbeat evolution or physical calibration.

The next discriminating unit is to decide whether the SPECIFIC legal physical point above admits some nonnegative coupling on <=14 edges. An exact 14-edge witness would extend the constructive atlas; a valid <=14 obstruction must cover all eligible support sets or give an equivalent exact dual/matroid certificate. Efficient investigation can classify which 14-column spans intersect the physical marginal affine hull before applying exact nonnegativity checks. A generic 15-edge requirement for the 14-dimensional ambient face is a rigorous theorem already; a 15-edge physical necessity witness remains open.

## Research identity and governance boundary

Source activity: Researcher-ID EM-DIRECT-C84CB5 / TASK_RESEARCH; Activity-ID RA-FC145E5B612E0CAE9C04B7FE, readback-verified in canonical Source main c63928b8aab541f0736e79ffbf2eb5edcf27b90b. Current native dispatch returned an unrelated X6 rotation task; this R5 artifact is independent author-side evidence, with no R5 CLAIM, formal Result or independent review/acceptance. This draft was locally checked with exact Fraction arithmetic and is submitted on its research branch for review.
