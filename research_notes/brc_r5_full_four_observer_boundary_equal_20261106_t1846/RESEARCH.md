# R5 — FULL_HIST and seedless LR have identical entire four-observer fibers at every timing-octagon boundary point

Date: 2026-11-06 (Asia/Shanghai).
Scientific status: AUTHOR_PROVED / EXACT_FRACTION_EXECUTED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY.
Frozen scientific pins: GLOBAL a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e.
Source predecessor: EM 9f8e53d0a5bb6094e650f7c165c28b44da70648d, exact 28-facet FULL_HIST (TQ,TP,D) projection; structural predecessor: EM 57f7d654e5dd002567e0b0d333937e6e38f3b4cb (single quadratic gate), and EM 02e1b1263649e6bef8c2acf16212a54ffb9dd851 (J-width formula).
This is an auxiliary exact positive finite P/Q likelihood-ratio/BRC observer. It does not assert native X6 dynamics. Applicable behavioral rules were separately read from current canonical-main; scientific sources remain frozen.

## Exact theorem and practical consequence

Let O4(FULL_HIST), O4(seedless LR) be the actual all-real four-observer images for the fixed strictly-positive four-stage P/Q tree at delta=1/4, with observations W=(eP,eQ,TP,TQ), eQ=Q(declare P), eP=P(declare Q). The stopping-time image H_T in coordinates (TQ,TP) is the proven rational octagon with eight facets (a,b,h) meaning a*TQ+b*TP<=h:

 (-323,282,-41), (-188,216,139), (-160,160,41), (-1,2,4),
 (3,-2,4), (80,-80,23), (123,-146,-23), (274,-236,179).

**Theorem (complete boundary-fiber equivalence, all real strategies).** For every t=(TQ,TP) on the *entire closed boundary* of H_T,

 { (eP,eQ) : (eP,eQ,TP,TQ) in O4(FULL_HIST) }
 =
 { (eP,eQ) : (eP,eQ,TP,TQ) in O4(seedless LR) }.

In fact, the aggregate six-flow (g,u0,u1,X0,X1,X2) is uniquely determined by each boundary time t. Its seven stopped likelihood-ratio Q masses M_r(t), r in R={1/10,1/2,3/4,1,5/4,3/2,19/10}, are also unique. The *entire exact* four-observer error fiber is the two-dimensional zonotope

 { (1-sum_r r*M_r(t)*z_r, sum_r M_r(t)*z_r) : z_r in [0,1] for all r in R }.

Equivalently, for each rho in R, its necessary and sufficient fourteen rational/affine-in-error inequalities are

 1 + sum_{r>rho}(rho-r)*M_r(t) <= eP+rho*eQ
 <= 1 + sum_{r<rho}(rho-r)*M_r(t).

For rational boundary t all masses and coefficients are rational. All-real, irrational and endpoint declarations are included. Therefore an R5 actual-image separation for this particular tree, if found, has stopping times strictly inside H_T.

## Proof (finite complete stop-flow certificate plus real-valued reconstruction)

Write q3[0]=(13/20,1/5,3/20), q3[1]=(1/40,9/20,21/40), b_ij=u_i*q3[i,j]/2, V_j=b_0j+b_1j. Let g be time-1 continuation, u_i time-2 continuation Q flow parameters, x_ij arbitrary full-history time-3 continuation, and X_j=x_0j+x_1j. Thus 0<=u_i<=g<=1 and 0<=x_ij<=b_ij. The exact times are

 TQ=1+g+(u0+u1)/2+X0+X1+X2,
 TP=1+g+(3u0+5u1)/8+X0/2+X1+3X2/2.

Pre-sampling all nine local stop/continue Bernoulli decisions gives a mixture of 2^9=512 deterministic stop assignments, hence the full feasible six-flow polytope is their convex hull. Exact enumeration collapses these to 82 distinct six-flows. On each of the eight known timing facets, every deterministic six-flow lying on the facet lies on the same six-dimensional segment between the two unique timing endpoints. This is a complete finite equality test (not a sampling heuristic) in VERIFY.py. Any randomized flow with boundary time must be a convex combination of deterministic flows *on that facet*, because all facet slacks are nonnegative and their mixture has zero slack. Consequently, for any point t on that edge the six-flow is the unique interpolation x(t) of the edge endpoints.

For all eight edges, at least one of the following nonnegative affine factors vanishes at *both* endpoints, hence throughout the face: A=u0/10, B=9u1/40, X1, A+B-X1. The exact facet certificates are:

 facet (a,b,h)                  deterministic face profiles   common zero factor
 (-323,282,-41)                 2                             A and X1
 (-188,216,139)                 2                             A+B-X1
 (-160,160,41)                  2                             A
 (-1,2,4)                      4                             A+B-X1
 (3,-2,4)                      4                             A+B-X1
 (80,-80,23)                   2                             B
 (123,-146,-23)                2                             B and X1
 (274,-236,179)                2                             A+B-X1.

Let alpha=47/180, beta=67/162, d=beta-alpha=247/1620. For arbitrary full-history central continuation, J=alpha*x_01+beta*x_11 lies in the exact interval

 max(alpha*X1, beta*X1-d*A) <= J <= min(beta*X1,alpha*X1+d*B),

whose length is d*min(A,B,X1,A+B-X1). The common zero factor therefore makes this interval a singleton on all eight edges. It must equal the seedless LR central value J_LR=X1*(alpha*A+beta*B)/(A+B), with value 0 when A+B=0.

Construct a seedless LR stopping policy at that same six-flow: continue from time 1 with probability g; continue from time-2 branch i with conditional probability u_i/g (take zero on a null branch); at the time-3 LR key j, use shared continuation probability z_j=X_j/V_j (zero if V_j=0). For j=0,2, the time-4 conditional Q kernels do not depend on history i; for j=1, the exact equality J=J_LR makes the pooled terminal distribution identical to FULL_HIST. All seven stopped-ratio Q masses are consequently unchanged.

For any original full-history labels, let ell_r be the total stopped Q mass declaring P across *all* histories with ratio r. Set the seedless LR declaration probability p_r=ell_r/M_r for M_r>0 and 0 otherwise. Since 0<=ell_r<=M_r, these shared probabilities are legal, and both error observers match exactly:

 eQ=sum_r ell_r,  eP=1-sum_r r*ell_r.

The stop times also match. This converts every real FULL_HIST behavior at boundary t into a real seedless LR behavior without changing any of the four observations. The reverse inclusion follows because LR is a FULL_HIST subclass. The zonotope expression follows from independent p_r in [0,1]. Its fourteen inequalities follow by minimizing and maximizing 1+sum_r(rho-r)M_r*p_r separately; these directions are the complete planar zonotope edge normals. QED.

## Exact verification and coverage

The executed standard-library Python Fraction checker enumerates all 512 deterministic local stopping assignments, obtains 82 different six-flow profiles, verifies all eight timing inequalities, the complete facet-collinearity and unique endpoint conditions, and their common nonnegative zero factors. It checks the singleton J condition and 80 exact FULL_HIST-to-LR stopped-mass/declaration reconstructions on five rational interpolation parameters per facet and two history splits. All checks pass:

 PASS_EXACT_R5_BOUNDARY_FOUR_OBSERVER_FULL_LR_EQUALITY

See VERIFY.py and actual stdout EXACT_OUTPUT.txt. The finite enumeration is exhaustive for deterministic stopping encodings. The convex-mixture/conditioning and label-pooling arguments extend the conclusion from those finite certificates to every real-valued randomized strategy, including all edge interiors and vertices.

## BRC information/observer application and next problem

Carrier: seven stopped likelihood-ratio masses plus seven declaration masses, retaining the central hidden-history split until its actual vanishing-defect identity is established. Observer: (eP,eQ,TP,TQ). Allowed future operation: only this four-observer readout; richer history-sensitive observers are not asserted invariant under pooling. Result: boundary-time pooling is exact because the unique scalar information defect d*AB/(A+B)*(z_11-z_01) is forced to vanish by the timing face.

The R5 mother question of actual-image separation/equality within the model remains open only for strictly interior stop times. Select interior rational t with nonzero exact J-width, construct FULL_HIST four-W using nonzero central defect, and decide LR membership by the complete seven-variable polytope K(W) and the one quadratic condition F=(A+B)J-X1*(alpha*A+beta*B). A strict global one-sided F certificate gives genuine separation; a real root yields an LR witness. Owner/CLAIM and independent review are separate from this author-side Source artifact.