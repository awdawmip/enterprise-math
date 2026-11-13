# R5: exact source-3 support filtration and optimal branch-support bridge

Date: 2026-11-11 (Asia/Shanghai). Researcher-ID: EM-DIRECT-2CB28A / TASK_RESEARCH. Research-Activity-ID: RA-8A53F787F030D7F32FF5EAA5.

Source registration: enterprise-math main at a34388855bee7ed2873033f15b679aa69874caea. Formal R5 CLAIM, Source Result and independent review: pending. The R5 frozen scientific inputs remain unchanged from PR #2063: global a01383f825ef9d43b4b754254303298c64041568; Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. Earlier witness: R5 PR #2017. Immediate proof dependency: R5 PR #2063, commit 9001105df972b214e8a52571aa4b175fc34cfcca. Its original exact verifier was copied verbatim as r5_prior_four.py (identical Git blob c316620c817b1abff6658b7f2d673f146141b28b).

## The fixed mathematical object

This theorem concerns the one frozen **auxiliary seven-ratio P/Q–BRC Blackwell observation fiber**. The integer ratio vector is

\[
R=(2,10,15,20,25,30,38).
\]

Thirty labeled nonnegative transmission arcs consist of 28 dynamic arcs \((i,j)\), with \(i=0,\ldots,6\) and \(j\in\{1,2,3,5\}\), and the two fixed strictly positive singleton arcs \((0,0)\) and \((6,6)\). Let \(E^0\) be the exact positive rational reference transfer whose full 30 entries are embedded in r5_prior_four.py. Let \(C\) be the 21-row observation operator recording seven target marginals, seven source marginals and seven source first moments.

\[
F=\{E\in\mathbb{R}^{30}_{\ge0}:CE=CE^0\}, \qquad \operatorname{rank} C=15,\quad \dim F=15.
\]

After fixing the two singleton masses, the 28 dynamic variables satisfy \(Ax=b\), with \(A\in\mathbb{Z}^{15\times28}\) and \(\operatorname{rank} A=13\). The exact right-hand side comes from the same \(E^0\) throughout.

For any target mask \(K\subseteq\{0,\ldots,6\}\), define the exposed face

\[
F_K=\{E\in F:E_{i,3}=0\text{ for all }i\notin K\}.
\]

A mask is *strictly realizable* if some \(E\in F_K\) has every arc allowed by \(K\) strictly positive. Let

\[
S_m=\{E\in F:|\{i:E_{i,3}>0\}|\le m\}.
\]

The property counted is positive **source-3 labeled target support**, not total nonzero transmission support. All other labeled arcs and their joint provenance remain part of the model.

## Main theorem — complete support filtration for this fixed fiber

For \(m=1,\ldots,7\), the exact strict mask census, corresponding exposed-face dimension and number of connected components of \(S_m\) are:

| Source-3 support size m | Strict masks of size m | Affine dimension of each strict face | Components of S_m |
| --- | ---: | ---: | ---: |
| 1, 2 or 3 | 0 | none | empty |
| 4 | 3 | 12 | 3 |
| 5 | 9 | 13 | 3 |
| 6 | 6 | 14 | 1 |
| 7 | 1 | 15 | 1 |

The three realizable four-masks, exactly those from PR #2063, are

\[
J_A=\{1,3,4,6\}, \quad J_B=\{2,3,4,5\}, \quad J_C=\{2,3,4,6\}.
\]

All **nine** strictly realizable five-masks are:

| Mask | Contains a feasible four-mask? |
| --- | --- |
| 01346 | yes |
| 02345 | yes |
| 02346 | yes |
| 02356 | **no** |
| 12345 | yes |
| 12346 | yes |
| 12356 | **no** |
| 13456 | yes |
| 23456 | yes |

The twelve excluded five-masks, each with an exact rational Farkas certificate, are:

01234, 01235, 01236, 01245, 01246, 01256, 01345, 01356, 01456, 02456, 03456, 12456.

Of the seven six-masks, precisely the six containing target 3 are strictly realizable. The seventh, 012456, is excluded by a rational Farkas certificate.

**Connectivity.** The nine five-faces split into exactly three connected components of \(S_5\): one union of seven faces and two isolated **13-dimensional** faces \(F_{02356}\), \(F_{12356}\). These two faces each have no four-support subface. The six six-faces form a connected 14-dimensional face complex, and \(S_6\) is connected.

**Sharp minimax bridge.** For any two different components of the four-support locus \(S_4\), the minimum possible maximum number of positive source-3 arcs along a continuous path in \(F\) is **exactly five**. To attain it, interpolate along the rational full-transmission witnesses \(J_A\to J_C\to J_B\). Both \(J_A\cup J_C\) and \(J_C\cup J_B\) have five targets. A direct \(J_A\to J_B\) segment has six-target support, so inserting \(J_C\) genuinely lowers the peak.

## Proof with exact finite certificates

### 1. The inherited four-mask classification

The exact predecessor checker, reproduced as r5_prior_four.py, verifies that no one-, two-, or three-support mask satisfies the source-3 mass/capacity/first-moment constraints. Of the 35 four-masks, exactly seven satisfy the local moment test; the original full-fiber checker constructs strictly positive rational transfers for \(J_A,J_B,J_C\) and exact Farkas separators for the remaining four candidates. Each successful four-face has 25 positive dynamic arcs plus two fixed singletons, i.e. 27 positive original arcs, and rank 13 in the dynamic constraints, hence dimension 25−13=12.

### 2. Exact primal certificates for all nine five-masks

Seven five-masks contain a successful four-mask. Fix its strictly positive rational witness and 13-column pivot basis of full rank. Add the unique fifth source-3 target with small positive rational mass \(t\) and adjust the same 13 pivot-column masses so that all 15 rational equalities \(Ax=b\) are preserved. Because the unperturbed pivot masses are strictly positive, a small enough positive \(t\) preserves strict positivity. VERIFY_SUPPORT_FILTRATION.py takes the rational sequence \(t=1/10000,1/20000,\ldots\), solves the overdetermined system by exact Fraction Gauss–Jordan elimination, and checks positivity and every original equality.

The remaining two five-masks, 02356 and 12356, do not contain any feasible four-mask. They are nevertheless **strictly realizable**, shown by the following explicit construction. Use all 26 allowed dynamic columns, place \(1/1000\) on each of 13 nonpivot columns, and solve \(Ax=b\) on these respective 13 pivot columns (indices follow dynamic source order 1,2,3,5 and target order 0,…,6):

| Mask | Thirteen pivot-column indices |
| --- | --- |
| 02356 | (1,16,17,19,0,8,25,27,20,4,11,14,2) |
| 12356 | (16,1,17,0,19,8,27,25,4,20,15,11,2) |

The exact program verifies all 26 allowed coordinates are strictly positive and every one of the 15 equalities holds as rational equality. In all nine cases the 15×26 restricted system has rank 13, so the nonempty exposed face has dimension 26−13=13.

### 3. Exact Farkas separators for all twelve excluded five-masks

VERIFY_SUPPORT_FILTRATION.py contains the **complete explicit 15-component rational vectors** for the twelve masks listed above. For each excluded mask \(K\), it checks separately:

\[
\forall k\in\operatorname{allowed}(K),\quad y_K^{\mathsf T}a_k\ge0;
\qquad y_K^{\mathsf T}b<0.
\]

If there were a nonnegative solution \(x\) supported on allowed columns, then \(y_K^{\mathsf T}Ax\ge0\) but \(y_K^{\mathsf T}b<0\), a contradiction. These twelve infeasibility results and the nine explicit positive transfers cover all \(\binom75=21\) size-five masks.

### 4. Exact classification of the six-masks

For each size-six mask containing target 3, choose one of the nine strictly feasible five-masks that it contains. The previous step supplies a strictly positive rational transfer and a 13-column full-rank pivot basis. Enable the sixth source-3 target with sufficiently small positive rational mass and correct the pivot coordinates, exactly as above. This yields 27 strictly positive dynamic masses and a 14-dimensional exposed face (27−13=14).

The only remaining six-mask is 012456 (which omits target 3). Apply the Farkas vector of the excluded five-mask 12456. The extra allowed target 0 has dual column pairing

\[
\frac45-\frac5{14}+\frac2{28}=\frac{18}{35}>0.
\]

Hence the same vector still pairs nonnegatively with all allowed columns but negatively with \(b\). Thus 012456 is infeasible, completing all \(\binom76=7\) cases.

### 5. Connectivity of the support filtration

For any masks \(K,L\),

\[
F_K\cap F_L=F_{K\cap L}.
\]

Each nonempty \(F_K\) is compact and convex. The union of all realized faces at support threshold \(m\) is exactly \(S_m\): every transfer of smaller support belongs to at least one realized \(m\)-face.

Two distinct size-five faces intersect only if their (at most four-target) intersection mask is feasible, so the known exact three four-masks determine the complete five-face intersection graph. It has three components with cardinalities **7,1,1**. Because disjoint finite unions of compact faces are separated, the graph components equal the connected components of \(S_5\).

Two distinct size-six faces intersect on a five-target mask. Exact five-mask feasibility determines the six-face intersection graph, which is connected. Every realized five-face lies inside one of the six six-faces. This proves \(S_6\) is connected. \(S_7=F\) is convex.

For the minimax claim, lower bound five follows from the three distinct connected components of \(S_4\); upper bound five follows from convex interpolation between the verified rational four-mask witnesses along \(J_A\to J_C\to J_B\), since the two unions have cardinality five. Both endpoints and every intermediate point satisfy the original full 30-arc observation equations.

## Verification and research status

All scientific equalities, positivity inequalities, rank tests, Farkas certificates and finite mask enumerations use exact rational arithmetic. The new local derivation/checker logic was actually run with Python Fraction (the local predecessor helper used an equivalent SymPy exact linear solve). Its actual output is preserved in EXACT_OUTPUT.txt. The GitHub-hosted new verifier includes the verbatim original prior checker and uses **Python standard library Fraction only**; its immutable bytes have been read back, but independent execution of those exact remote bytes is left for replication. Reproduction command from this folder:

    python3 VERIFY_SUPPORT_FILTRATION.py

Expected final line: PASS_EXACT_R5_SUPPORT_FILTRATION_4_TO_7_AND_NINE_FIVE_MASKS.

This is a model-internal exact mathematical result about the auxiliary Blackwell transmission observation fiber; no native X6 physical dynamics is inferred. GitHub persistence is author-side evidence and is not a formal scientific Result, independent review or Foundation admission.

## Next executable research units

1. Construct the exact signed six-edge K_{2,3} residual-atom decomposition and minimum circuit word-length for an explicit optimal five-support path \(J_A\to J_C\to J_B\). Preserve every labeled source-target mass and nonnegativity at all interpolation stages.
2. Determine which non-four-residual adjacent extreme edges connect the nine tree components inside the previously established 11-dimensional common face of 49 sharp edges.
3. Classify first feasible 14-dimensional incidences and residual directions from the two exceptional five-faces 02356 and 12356; independently re-execute the hosted exact verifier as part of review.
