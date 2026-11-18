# EC49AW — exact all-real causal optimum at eta=11/30

Status: AUTHOR_ANALYTIC_PROOF / EXACT_FRACTION_CHECK_PASS / PORTABLE_DRAFT / UNREVIEWED / NOT_ADMITTED. Date: 2026-10-30.

## Frozen model and exact theorem

This is exclusively the auxiliary positive 18+18-leaf probability BRC observer of EC49AU/AV, NOT native signed BRC or X6 dynamics. Hidden w=0,1,2; action c=A0,A1,B0,B1,STOP, costs (1,1,2,2,0); observed u=0,1; purchased label z=0,1,2. At eta=11/30, the probabilities t(w,0)=(4,15,26)/30, t(w,1)=(26,15,4)/30. First-stage x[w,c]>=0 with each row sum 1 and total action cost sum a_c*x=43/16 (expected C1=43/48). For paid actions c<4, q_z(c,u)=x[z,c]*t(z,u)/3, T=sum_z q_z, V=sum_z [43q_z-16T]_+/172. The purchase coin p(c,u) in [0,1] sees only (c,u), not hidden w. Exact purchase cost sum pT=C2=13/16. Optimal terminal acceptance sees only the realized observation and gives H=alpha-(177/172)beta=sum pV. The no-purchase observation never has positive score.

**Theorem:** The maximum H over ALL lawful real causal behavioral strategies is exactly **14401/123840**. It is achieved by the prior explicit W: x rows (0,3/16,1/4,0,9/16), (1,0,0,0,0), (0,1,0,0,0); purchase all positive-mass paid fibers and accept only positive-score purchased labels. This closes the previous exact gap 71/506970 at eta=11/30.

## I. Exhaustive one-dimensional reduction

Reuse EC49AV's proved sparse-optimum lemma: fix a global optimum p, maximize the convex objective in x on three row equations plus action cost plus purchase cost; an extreme point has at most five positive x coordinates. Fix the resulting x, maximize linearly in purchase probabilities subject to one exact cost equality, giving at most one fractional positive-mass fiber. These replacements preserve optimality and never condition purchase on w.

The base x-polytope has four independent equations. On any feasible support its action-cost row cannot lie in the span of the three history row-sums: otherwise each history's supported actions all have a single integer cost, forcing the prescribed sum 43/16 to be integral. Thus its support-restricted rank is four. An x with <=5 positive entries is at a base vertex (support 4) or on a base edge (support 5). Enumerate all C(15,4)=1365 possible bases by exact rational Gaussian elimination: 168 distinct nondegenerate vertices, all with exactly four positive coordinates. Add each unused fifth coordinate to their supports: 924 distinct five-coordinate faces, each with exactly two vertices; rank four proves these faces are exactly all one-dimensional edges. The complete exact enumeration is in VERIFY_EC49AW.py.

The available paid mass P(x)=sum_(w,c<4)x[w,c]/3 is affine. Exact C2 is feasible only when P>=13/16. Intersect each edge with this half-space. Exactly 720 edges have no feasible point, leaving 204 clipped feasible segments. Every base vertex belongs to some enumerated edge, so no admissible sparse optimum is omitted.

## II. Edge-specific dual prices close 196 segments

For lambda>=0 define U_lambda(x)=lambda*C2 + sum_f [V_f(x)-lambda*T_f(x)]_+. As p_f in [0,1] and sum pT=C2, H<=U_lambda(x). Each V_f is convex in x, T_f affine, so U_lambda is convex along every first-stage edge for fixed lambda. Consequently two endpoint bounds U_lambda<=14401/123840 imply the same bound at EVERY real interior point of that edge.

At a rational endpoint x, the feasible price set I(x)={lambda in [0,1]: U_lambda(x)<=14401/123840} is a closed interval: lambda -> U_lambda(x) is convex piecewise-linear, with breakpoints lambda=0,1,V_f/T_f for T_f>0. The exact Fraction verifier computes all intervals from their rational knots (no tolerances). On 196 of 204 feasible clipped edges, endpoint price intervals overlap; choose lambda_E=max(the two exact lower bounds). It checks the two exact endpoint inequalities. The convexity theorem then certifies the entire uncountable real edge. A global single lambda was inadequate in EC49AU; using distinct prices on distinct edges does not assume or grant such a global certificate.

## III. Eight exceptional edges: exact two-piece analytic gap

The remaining eight are *not* improving strategies. Their support sets are recorded in EXACT_REPORT_EC49AW.json. Exact endpoint pairs of each q_z(c,u), up to permuting observed fibers and latent labels within a fiber, have identical affine signatures, so it is sufficient to study one representative.

Let parameter t in [0,1] interpolate the paid-mass-high endpoint whose x rows are (11/16,0,0,0,5/16), (0,1,0,0,0), (1,0,0,0,0), to the sensor-budget boundary whose x rows are (3/16,0,1/4,0,9/16), (0,1,0,0,0), (1,0,0,0,0). Index observed fibers by f=2c+u. Only f=0,...,5 have positive mass. Exact affine scores give

T0=(115-8t)/360; T1=(175-104t)/720; T2=T3=1/6; T4=t/90; T5=13t/180.

V0=(16t+329)/(45*172); V2=V3=9/344; V4+V5=9t/688;
V1=(3349-2808t)/(720*172) for t<=89/104;
V1=(1925-1144t)/(720*172) for t>=89/104.

Of 24 affine observation scores 43q_z-16T, only f=1,z=2 changes sign in (0,1), at exactly 89/104. All other positive-mass fibers f=2,3,4,5 have value per unit purchase mass 27/172. Fiber 0 has density (128t+2632)/(172(115-8t)); fiber 1 has density L(t)/(172(175-104t)), where L(t)=3349-2808t or 1925-1144t on the two intervals. Comparing 27/172 against fiber 1 gives positive cross-product numerators 1376 and 2800-1664t. Comparing fiber 0 against fiber 1 gives positive cross-products 559(27-8t)(8t+5) and (175-104t)(216t+1367). Thus fiber 1 is always the strictly least attractive positive-mass purchase fiber. The exact optimal sensor knapsack buys all other positive-mass fibers and withholds only (P-C2)=(1-t)/12 of fiber 1 (legal because (1-t)/12<=T1).

Substituting that *optimal* purchase rule, target-H(t) is exactly

(4472t^2-8397t+4990)/(7740(175-104t)) for 0<=t<=89/104;

29(1-t)/2580 for 89/104<=t<=1.

The first numerator has positive leading coefficient 4472 and discriminant 8397^2-4*4472*4990=-18751511<0; the denominator stays positive for 0<=t<=1. The second gap is nonnegative and vanishes exactly at t=1. Therefore the eight remaining real segments satisfy the global theorem with equality only at their budget boundary. This is an analytic all-real argument, not a numerical grid.

## Actual verification and exclusions

Run Python 3 standard library: python3 VERIFY_EC49AW.py > EXACT_REPORT_EC49AW.json. The checker was executed, with exactly 168 vertices, 924 edges, 720 infeasible, 196 certified by exact edgewise prices and 8 identical-signature exceptional segments. It verifies the canonical score root and algebraic boundary identities; the discriminant and piecewise proof above are the all-real logical certificate. No sampling is extrapolated.

Author-only evidence and publication do not constitute Source-native activity/CLAIM/Result, mathematical peer review, Foundation admission or empirical physics. The positive probability model does not justify signed BRC amplitude cancellation, native X6 or Heartbeat World correspondence. Protected P000 and ACTIVE worldview are unchanged.