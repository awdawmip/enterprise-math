# R5 — exact image-convexity filter for a serial two-decision BRC model

Date: 2026-11-04, Asia/Shanghai. AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. This is a narrowly scoped auxiliary theorem; the full R5 mother problem remains open.

## Source and boundary

Continue immutable R5 K3 certificate b436e925727896e23f1a341425e4c8a30e1c33f7 (research_notes/brc_r5_k3_global_certificate_20261104_t1140/RESEARCH.md and NEXT_TASK.md). Frozen scientific input pins: Global Knowledge a01383f825ef9d43b4b754254303298c64041568, Enterprise Math 86149263e38c22292c9def1e0f69092efa1be77e. P000 and ACTIVE worldview unmodified. Current normative rules loaded separately.

The question: can two *serial*, source-blind continuation choices with no intermediate route split have equal FULL/LR four-dimensional convex hulls and unequal actual real behavioral image sets? This is a positive-mass, origin-labeled abstract BRC observer problem, not yet an embedded X6, physical, or fully specified binary likelihood-ratio experiment. In particular, two serial decisions are NOT a genuine two-route/two-reconvergence diamond.

## Definition

Let m origins have w_i>0, sum w_i=1. At successive opportunities 1 and 2, the policy can stop, otherwise it stops at 3. Conditioned on source i and stopping stage j, its four readouts are a FIXED vector V_ij in R^4 (eP,eQ,TP,TQ). The source label is retained through the readout but concealed from the seedless LR controller. The four coordinates may include source-conditional P/Q ratios in V_ij. No route-dependent actions, additional declaration decisions, correlated persistent seed, or fresh source observation are available. FULL may choose first and second stopping hazards a_i,b_i separately for each source; seedless LR must use common a,b, with fresh independent coins.

Stage law for hazards (a,b) is pi=(a,(1-a)b,(1-a)(1-b)). This parametrizes the COMPLETE probability simplex in three coordinates: for any pi, a=pi_1 and b=pi_2/(1-pi_1) if pi_1<1, else b=0.

## Theorem 1 — all-real convexity and exact signed support

Under these hypotheses:

    O4(FULL) = sum_i w_i conv{V_i1,V_i2,V_i3}   (Minkowski sum);
    O4(LR)   = conv{sum_i w_i V_i1, sum_i w_i V_i2, sum_i w_i V_i3}.

Both are already convex actual real images. Thus equality of four-observer convex hulls is equivalent to equality of actual real observer images. In particular this fixed-emission/no-rebranch serial-hazard family CANNOT realize the target "equal hulls / unequal images".

For ANY signed n in R^4:

    Delta(n) = h_FULL(n)-h_LR(n)
             = sum_i w_i max_j(n·V_ij) - max_j sum_i w_i(n·V_ij) >= 0.

At a given n equality holds if and only if all origin-specific maximizing-stage sets have nonempty intersection. Therefore hull equality is equivalent to this intersection condition for EVERY n in R^4, not just finitely sampled directions.

Proof. The displayed inverse for pi shows that every probability distribution over the three stages can be implemented by two hazards. FULL chooses independent simplexes, and its linear four-readout image is the Minkowski sum of their triangular images, hence convex. LR chooses one common simplex, giving the triangle of aggregated stage vertices. Maximizing a linear n independently at each origin gives the first support expression; maximizing the common stage gives the second. If one stage maximizes for all origins the two values agree. Conversely choose a maximizing LR stage j*: the sum of positive w_i times nonnegative source deficits [max_j n·V_ij - n·V_i,j*] equals zero only if each deficit is zero, so j* maximizes every origin. QED.

The same argument works for k serial source-blind hazards and k+1 fixed stopping stages: their hazards parametrize the complete (k+1)-simplex. It does NOT establish any result for intermediate splitting/reconvergence, shared route-conditioned actions, additional declaration controls, or a general R5 likelihood-ratio graph.

## Corollary 2 — heterogeneity can remain observationally irrelevant

If V_ij=b_i+lambda_i d_j for source-specific vectors b_i, nonnegative scalars lambda_i and common d_j in R^4, put B=sum_i w_i b_i and L=sum_i w_i lambda_i. Then BOTH actual images are B+L conv{d_1,d_2,d_3}. For any FULL stage distributions pi_i, if L>0, choose LR common pi_j=(sum_i w_i lambda_i pi_ij)/L and recover valid common hazards by the simplex inverse; if L=0 both images are the point B. This proves actual-image equivalence even for unequal b_i and lambda_i. It also shows why source heterogeneity alone does not imply action-relevant BRC residual. In the illustrated numerical homothetic case, clock coordinates may depend on source; it is a four-vector geometry example rather than a proof of common-clock physical realizability.

## Exact rational separating example

Take two source weights w=(1/3,2/3) and stage vectors:

    A1=(0,1,1,1),   A2=(1/2,1/2,2,2), A3=(1,0,3,3);
    B1=(1,0,1,1),   B2=(1/2,1/2,2,2), B3=(0,1,3,3).

For n=(1,0,0,0), FULL chooses (A3,B1) giving W=(1,0,5/3,5/3), while the largest LR first coordinate is max(2/3,1/2,1/3)=2/3. Exact gap 1/3, and dist_infinity(W,O4(LR))>=1/3. For n=(0,1,0,0) the gap is also 1/3. For n=(0,0,1,0) it is zero.

## Exact rational homogeneous-direction example

Use common d_1=(1/10,1/5,1,1), d_2=(1/5,1/10,2,2), d_3=(3/10,1/5,3,3); b_A=(1/20,0,0,0), b_B=(0,1/30,0,0), lambda_A=1/2, lambda_B=3/2 with the same w. Then L=7/6, distinct source profiles, and images equal. For each of the 9 deterministic FULL stage pairs the executable verifier constructs exact nonnegative LR mixing coefficients. For the interior stage laws pi_A=(1/5,3/10,1/2), pi_B=(1/3,1/6,1/2), it produces common LR pi=(11/35,13/70,1/2), hazards (a,b)=(11/35,13/48), and the exactly equal four-vector.

## Actual verification and next question

VERIFY.py is standalone Python stdlib Fraction code. EXACT_OUTPUT.txt is actual local stdout from exact rational computation. It enumerates 9 FULL and 3 LR deterministic stage configurations in each example, checks four signed support directions per example, the exact strict separating witness, all 9 rational LR convex certificates for the homothetic example, and one nonvertex real-behavioral rational instance. Finite arithmetic validates those examples; universal-real statements follow from the proof's explicit simplex parametrization and linearity. No floating point, claim of independent mathematics review, or P000/native X6 theorem is made.

BRC implementation: w_i>0, origin labels and ordered stage identities are retained until source-specific readout; only afterward can the declared four-observer aggregation be performed. This observation restriction is crucial. The next scientific unit must introduce *genuine* intermediate origin-mixed branching between two reconvergences, preserve path labels, enumerate the appropriate FULL/LR deterministic policy classes, and test all-signed hull equality by exact rational convex membership/Farkas certificates before a real-image nonmembership search. The mother problem is still OPEN. Native owner read currently returns CONTROL_QUOTA; the native Site has read-only research scopes, so no native CLAIM/Result/Driver admission is asserted.
