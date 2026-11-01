# R5 — Complete time-marginal polygon obstruction, independent of terminal answers

Date: 2026-11-01 Asia/Shanghai. STATUS: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.
Parent: original four-observer FULL/LR hull-equality + actual-image-inequality question remains OPEN.
Frozen inputs: GLOBAL_KNOWLEDGE_V1 canonical main a79db1aa492e6e05d95da61481bce3e3292109d8; Enterprise Math canonical main 1cce3e5a5246da8660e995cc5ea67182785504ef. Predecessor (full six-facet 4D analysis): da5f5835bc20e2059bc7de82e99d28274c10f623, research_notes/brc_r5_complete_six_facet_hull_audit_20261101_t1340/RESEARCH.md and VERIFY.py. P000 and ACTIVE worldview unchanged. This is an auxiliary finite two-law stopping model, not a native X6 theorem.

## Exact model and probability flow

Hidden sources A1,A2,B,C have masses P=(1/8,1/8,1/4,1/2), Q=(1/8,1/8,1/8,5/8). At actual (time,likelihood ratio) key I=(1,1), A1/A2 stop at t=1 with probabilities p1,p2 or continue. Continuing low-edge P/Q chances are (1/2,1/4) for A1 and (3/4,3/8) for A2. High edges terminate at time 2; low edges join bypass B at J=(2,2). At J, A1,A2,B stop at time 2 with probabilities q1,q2,qB or continue to time 3. C stops at time 1 with probability r or continues to time 3. Each key is visited at most once per path. FULL uses independent (p1,p2,q1,q2,qB,r) in [0,1]^6. Legal LR requires p1=p2=p and q1=q2=qB=q; r is independent. All behavior probabilities are shared under the two measures. Paths retain their source labels; signed scores are applied after probability projection.

For a source with low-edge chance l under a given measure, its expected stopping time is tau(p,q;l)=p+(1-p)(2+l(1-q)). Consequently

TP = tau(p1,q1;1/2)/8 + tau(p2,q2;3/4)/8 + (3-qB)/4 +(3-2r)/2;
TQ = tau(p1,q1;1/4)/8 + tau(p2,q2;3/8)/8 + (3-qB)/8 +5(3-2r)/8.

These are exact source-labelled conservation identities. Both are multi-affine in the six independent behavioral parameters. The X/Y terminal signal and terminal P/Q answer after A1/J continuation occur at the *same time 3*, hence do not alter TP or TQ.

## Theorem A: universal time-only strict support separation

Set H = 21 TP - 26 TQ (the eP,eQ coefficients are zero). Algebraic expansion for every real FULL policy gives

H_FULL = -25/2 + p1/8 - p2/8 -(1-p1)q1/2 - 3(1-p2)q2/4 -2qB +23r/2 <= -7/8.

Equality occurs at (p1,p2,q1,q2,qB,r)=(1,0,0,0,0,1) (q1 can be anything when p1=1). Under LR it simplifies for all real p,q,r in [0,1] to

H_LR = -25/2 +23r/2 -[2+5(1-p)/4]q <= -1,

equality at r=1,q=0 for every p. Therefore max_FULL H - max_LR H = 1/8, a strict **all-real** support gap in the two time coordinates alone. The full four-observer convex hulls are strictly different regardless of any change in terminal answers or final signals that does not alter reachability, stopping times, or the LR decision partition. Terminal-only repair of the previous six four-dimensional facet violations is impossible. No assertion is made for altered upstream kernels, decisions, or time costs.

## Theorem B: complete two-dimensional convex hull classification

Multi-affinity means the time-marginal convex hulls of all real behavioral policies equal hulls of the finite deterministic image sets (8 LR and 64 FULL corners). A standalone Python Fraction enumerator, using the flow formulas above, computes exact oriented cross-products and primitive integer edge inequalities. The exact CCW LR polygon has six vertices:

(5/4,9/8), (3/2,5/4), (61/32,101/64), (93/32,181/64), (5/2,21/8), (9/4,19/8).

The FULL polygon has *exactly these six vertices plus one new vertex* W=(55/32,91/64), inserted between the second and third above. The exact LR polygon facets a TP+b TQ+c >=0 (ordered CCW) have integer triples

(-1,2,-1), (-21,26,-1), (-160,128,103), (4,-8,11), (8,-8,1), (20,-16,-7).

The number of FULL deterministic corners violating these six facets is (0,2,0,0,0,0). Both violating strategies, (1,0,0,0,0,1) and (1,0,1,0,0,1), project to W. Its unique violated facet is -21 TP+26 TQ-1=-1/8. Thus the entire FULL time hull is conv(LR time hull union {W}), not merely known to be larger in one direction.

The time-space L-infinity distance from W to the LR time polygon is **exactly 1/376**. Lower bound: the separating normal has L1 norm 21+26=47, giving (1/8)/47. Attaining mixture:
Y=(22/47)*(3/2,5/4)+(25/47)*(61/32,101/64)=(2581/1504,4285/3008),
with ||W-Y||_infty=1/376. Every FULL 4D witness projecting to W has distance to the 4D LR convex hull at least 1/376, but exact equality in 4D is not asserted.

## Theorem C: an explicit positive two-kernel open no-go rectangle

Keep the same timing and origin/low kernels. After A1 continues at J, X answers P at t=3 and Y Q at t=3. Perturb their independent positive P/Q X probabilities from (3/5,1/2) to (3/5+alpha,1/2+beta); complementary Y probabilities change correspondingly. Let |alpha|,|beta|<=1/100. X/Y terminal (time,LR) signatures remain distinct from the other signatures and each other; all exogenous branch probabilities stay strictly positive. In this whole rectangle, with k=(1-p1)(1-q1), the full four-statistic observation perturbation is the **exact identity**

O(alpha,beta)-O(0,0) = k*(-alpha/16,beta/32,0,0).

Hence the time-only separation remains identically 1/8, not merely robust to small parameters. The previous LR four-dimensional chart O0+pB+qC+pqD+rE changes, with U=(-alpha/16,beta/32,0,0), to O0+U+p(B-U)+q(C-U)+pq(D+U)+rE. The rank-one matrix determinant lemma and the preceding exact inverse give

det[B-U,C-U,D+U,E] = (233+530alpha-170beta)/163840 >=113/81920>0.

Thus LR four-observer rank stays 4 and, since the chart is injective and its actual real image imposes s=pq, that image remains nonconvex. Further, the six prior fixed-model signed support separations persist uniformly under this perturbation: with old facet normal ni=(ai,bi,ci,di), each score changes by <=|ai|/1600+|bi|/3200, so its FULL-vs-LR gap stays at least gi-2(|ai|/1600+|bi|/3200). Exact positive bounds in predecessor facet order:

65099/46600, 76/233, 88963/46600, 4742/5825, 3/23300, 3/23300.

These are bounds for the original six *signed directions*, not a claim that the perturbed hull has the identical six facet equations. The stronger time-only strict support gap holds even beyond this small rectangle whenever the unchanged timing/reach assumptions hold.

## Validation, permission and next question

VERIFY.py uses only Python stdlib Fraction. It exhausts the 8 LR and 64 FULL deterministic time policies, checks six exact planar facets and the 7-vs-6 hull classification, verifies the analytical support identity on all corners and 125 interior LR triples, checks the exact nearest LR mixture, the two-parameter corner tests, rank certificate, and all six old-direction perturbation margins. Universal real assertions follow from the displayed identities, multi-affinity, and finite-vertex hull reduction, **not** from finite interior sampling. Exact executed output is in EXACT_OUTPUT.txt. Full 4D source model and earlier exact six facets are cited to the immutable predecessor commit; this new checker focuses on the time-marginal and perturbation derivations.

The private gateway reported research_authority_granted=false and did not verify backend connectivity; bounded native owner listing returned CONTROL_QUOTA; own session request was denied STATIC_READONLY_SCOPE_DENIED before backend dispatch. GitHub artifacts are author-side portable, not a native CLAIM, Result, independent review, Foundation promotion or P000 modification. Original four-observer mother question OPEN.

**Next:** Vary *upstream* low kernels while preserving genuine LR time–likelihood ratio collisions; classify the exact parameter locus where even the (TP,TQ) hulls coincide before attempting the four-observer all-signed primal/Farkas test and real-image nonmembership.
