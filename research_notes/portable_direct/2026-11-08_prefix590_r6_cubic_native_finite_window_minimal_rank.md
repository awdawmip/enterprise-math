# PREFIX-590-R6 — Sharp finite-window rank of the native cubic BRC observer

Date: 2026-11-08 (Asia/Shanghai).  
Status: AUTHOR_PROVED / EXACT_FINITE_NATIVE_CERTIFICATE / UNREVIEWED / NOT_ADMITTED.  
Frozen scientific pin: \`f42f2906d77f24085c123f3ccfe9667d41caa96d\`.  
Native implementation: \`research_notes/portable_direct/PREFIX565_positive_marginal_certificate.py\`, Git blob \`7d4ffaaa5f2e804bff01196f2c2c5cc8bcb79f41\`.  
Related exact sources: PREFIX-588-R6 at \`755fca13477494e324d4484b38066648eb68f176\`, PREFIX-589-R6 at \`d9556df528a3b665b911fb93da98d4ee7e09a0ad\`.  
Source-native identity, active owner and CLAIM not established: \`BACKEND_IDENTITY_CHECK_UNAVAILABLE\`, \`operation_sent=false\`.

## Exact question

Which **minimal number of variable linear statistics of the arbitrary initial-port probability law** suffices to recover all cubic-and-below mixed native BRC path moments at every horizon \(n=0,1,\ldots,8\)?

Use precisely the frozen zero-root four-STAR original native X6-BRC kernel with 96 ports, six labeled actions, each independently and uniformly chosen. For each start port \(i\), let \((R_1,\ldots,R_6,K)\) be the cumulative original native rewards of a path of length \(n\). Define
\[
P_0=R_1+R_2,\quad P_1=R_3+R_4,\quad
Y=K-\frac{5R_1-R_2+5R_3-R_4-4R_5-4R_6}{192},\quad T=192Y.
\]
For each depth \(n\), the observer is the vector of all 20 moments
\[
\left(E_\pi[T_n^aP_{0,n}^bP_{1,n}^c]\right)_{a+b+c\le3}.
\]
\(P_2=R_5+R_6=n-P_0-P_1\) is exactly recoverable at each declared length.

## Finite-window theorem

Let \(M_n\in\mathbb Z^{96\times20}\) be the original labeled-path **integer** matrix, each row the 20 sums of the corresponding mixed monomials over the \(6^n\) original native paths from one given start port, with no division by \(6^n\). Thus the conditional expectation matrix is \(6^{-n}M_n\), which has the same column rank.

For \(d=0,\ldots,8\) define the concatenated matrix
\[
\mathcal M_d=[M_0\mid M_1\mid\cdots\mid M_d]\in \mathbb Z^{96\times 20(d+1)}.
\]
Exact rational row reduction of all original native paths gives
\[
\boxed{(\operatorname{rank}\mathcal M_d)_{d=0}^8
=(1,6,14,22,30,33,33,33,33)}.
\]
Individual depths have ranks
\[
\boxed{(\operatorname{rank}M_d)_{d=0}^8
=(1,6,9,16,14,16,16,16,16)}.
\]
Consequently the **entire declared finite window** \(0\le n\le8\) admits **exactly 32 variable rational linear sufficient coordinates** of the start law \(\pi\) (plus the known constant \(1\)); 32 is minimal in the class of linear statistics preserving all 180 requested pooled moments for **every** probability vector \(\pi\) on the 96 native ports.

In particular, the 8-variable rank-optimal depth-two summary from PREFIX-588 requires **12 additional independent variable linear coordinates** to recover the entire depth-three cubic observer (rank of \([M_2|M_3]\) is 21 vs rank \(M_2=9\)). PREFIX-589 supplied one explicit positive-law future-step witness; this computation determines the full exact linear information gap.

## Proof and independent minor certificate

The published standard-library Python certificate enumerates all original native paths at each depth via exact nonnegative integer dynamic path aggregation over native tuples \((\mathrm{endpoint},T,P_0,P_1)\), preserving all multiplicities, including the original six BRC edge labels. It then performs exact \(\mathbb Q\) elimination of all \(96\times180\) entries. The 33 independent columns of \(\mathcal M_8\) have zero-based indices
\[
(0,21,22,23,27,29,41,42,43,47,48,49,57,59,63,67,68,69,
71,74,75,76,83,87,88,89,94,97,98,99,103,107,108).
\]
Thus exact elimination directly certifies that **every** one of the 180 moment columns belongs to a 33-dimensional rational span. For an independently checkable nonzero 33×33 minor, use zero-based native port rows
\[
(0,2,4,6,7,8,10,12,14,16,18,20,22,24,28,32,34,36,38,42,46,
48,50,52,54,56,60,64,68,72,76,80,84)
\]
and the 33 columns displayed above. Their determinant obeys
\[
\boxed{\det(\text{minor})\equiv325742\pmod{1000003}\ne0}.
\]
The nonzero modular determinant provides a separate exact rank-lower-bound certificate. Because the constant \(6^n\) is present in the degree-zero column at every depth, the image of the normalized initial-port probability simplex has affine dimension \(\operatorname{rank}\mathcal M_8-1=32\). Any linear sufficient carrier for these 180 observables must therefore have at least 32 variable coordinates, and an independent 33-column basis provides a matching construction.

## Scope and interpretation

This is an **exact theorem on the stated finite native horizon** \(n\le8\) and declared degree-three observation family. The rank has stabilized at 33 for the computed depths \(5,6,7,8\); an all-length closure theorem remains open until an invariant-subspace or certified recurrence argument establishes it. This is an information-preserving observation calculation; the original native six-dimensional carrier, branch labels and endpoint provenance remain in the underlying dynamics.

## Verification and next question

Local execution of \`PREFIX590_R6_eight_depth_joint_moment_rank_certificate.py\` with original \`PREFIX565_positive_marginal_certificate.py\` returned \`ALL_CHECKS_PASS\`. The script uses exact integers and Python \`Fraction\`, computes all per-depth and cumulative ranks, checks the explicit 33-column basis, 33-port minor and its nonzero modular determinant. Structured exact results are in \`PREFIX590_R6_RESULTS.json\`.

Next: construct the explicit smallest **weighted native transition-invariant** subspace containing these moment observables, to prove or refute that rank 33 persists for all horizons. Track the multi-grade BRC moment operators, keeping horizon and observer typing; first test their action on the certified 33-column finite basis. A longer finite numerical-looking rank plateau is not an all-length certificate.
