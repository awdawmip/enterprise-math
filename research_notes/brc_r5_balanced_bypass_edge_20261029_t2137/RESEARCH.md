# R5 — Balanced-bypass normal-cone certificate (unbounded face size)

Date: 2026-10-29 Asia/Shanghai. Author-side portable theorem.
Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED.
No native Source CLAIM, Result, mathematical acceptance or independent Driver review.

## Frozen sources and scope

GLOBAL_KNOWLEDGE_V1 canonical main@43426477421af85d5b1cab601c39d682d5f41b13, Enterprise Math canonical main@e3148a75734182faea1e2822c84bd782b43005bb. Read global bootstrap/manual, project router and P000, ACTIVE worldview, TASK research router, portable research protocol and BRC priority. Previous theorem: five-vertex exposed-facet veto on PR #1663 at 183521836359dfc07dc70153cc7c560aa61bd7b3.

Scope: external finite strictly absorbing two-law P/Q stopping trees. FULL retains history, LR uses seedless real behavioral decisions keyed by (time, exact likelihood ratio); each key occurs no more than once per path. Four observers O=(eP,eQ,TP,TQ). BRC use: exact positive P/Q origin-and-branch masses are maintained before observer projection. Signed affine differences are never negative path probabilities. No native X6 or Heartbeat physical inference.

The native owner inventory attempt returned CONTROL_QUOTA, and own native session start returned STATIC_READONLY_SCOPE_DENIED with operation_sent=false. The actual active task owner and formal claim are not certified; this is an author-side portable research note, not a task-state write.

## New theorem: shared-face normal detects FULL bypass residual

Fix ordered LR binary decision keys k<l (actions 0=absorbing stop, 1=continue), with other deterministic actions fixed. Perfect recall allows FULL at l to distinguish histories that visited k from histories that bypassed k. Let four deterministic LR observation corners be A=V00, B=V01, C=V10, D=V11.

By explicitly setting k=continue and using different decisions at l for via-k and bypass-k histories, FULL has the two legal deterministic observations

H_via = A + D - B,  H_bypass = C + B - A.

The identity H_via + H_bypass = C + D is exact; it follows by decomposing observer contributions over disjoint path origins, not by signed cancellation of path masses. Put delta=A-B, so H_via=D+delta and H_bypass=C-delta.

Let K=conv(O_LR), the convex hull of all deterministic LR observer outputs. For any supporting linear functional w and h such that w·v >= h for all v in K and w·C=w·D=h, we obtain

w·H_via-h = w·delta,  w·H_bypass-h = -w·delta.

Therefore the all-real policy support gap satisfies

min_LR(w·O) - min_FULL(w·O) >= |w·delta|.

If w·delta != 0, choose the negative split witness: it is outside the entire LR convex hull. Its L-infinity distance from every real LR observation is at least |w·delta| / ||w||_1. This is a single rational separating inequality if all vertices and w are rational. No facet-size bound and no rank-three rectangle condition are required.

### Exact normalized local LP

For the complete finite rational list V of deterministic LR observer vertices, solve both rational linear feasibility systems indexed by sigma=+1 and -1:

w·(D-C)=0;
w·(v-C)>=0 for every v in V;
sigma*w·(A-B)>=1.

A feasible solution is an exact signed all-real separator with gap at least 1 and a lawful FULL witness. By positive rescaling, the two systems detect exactly the shared-supporting-face normals with nonzero bypass contrast. Infeasibility of both is ONLY failure of this local certificate, not proof of convex-hull equality or real-image equality.

### Minimal-face tangency and arbitrary-vertex edge veto

Let F be the smallest face of K containing m=(C+D)/2. If both FULL split observations were in K, the midpoint identity and face property would force H_via,H_bypass,C,D all to lie in F. Hence necessarily delta=A-B is in lin(F-F). If C,D are endpoints of an exposed EDGE of K, but delta is not parallel to D-C, they cannot both belong to K. Every finite-polytope edge is exposed; for rational vertices a rational edge-normal w can be perturbed within the open relative normal cone so w·delta !=0 while keeping all other LR vertices strictly above the edge. Thus a rational certificate always exists. Crucially this rejects rectangles on facets with SIX, SEVEN, or arbitrarily many vertices whenever C-D remains an edge; the prior five-vertex facet veto could not do so.

## Exact strictly positive two-law stopping example

At the beginning there are two observable origins i=via-k,bypass-k, each having P and Q probability 1/2. Via visits k at time 1 and may stop (zero error,T=1) or continue. Bypass reaches time 2 directly. Both surviving origins reach LR key l=(2,1): the P/Q mass of EACH origin is 1/2, so exact likelihood ratio equals 1. At l stop emits zero error at time 2; continue produces a terminal Bernoulli error at time 3. Conditional probabilities (P(error),Q(error)) are (1/4,3/4) for via and (3/4,1/4) for bypass; all errors and complementary outcomes are strictly positive under both laws, and all physical kernels normalize. The sample space and observations are common to P,Q. Deterministic stop absorption is a chosen action, not an assertion of a strictly positive random transition.

With FULL continue-probabilities x at k, v at l after via-k, b at l after bypass-k, all real in [0,1], exact positive flow gives

eP=x*v/8 + 3*b/8;
eQ=3*x*v/8 + b/8;
TP=TQ=(3+x+x*v+b)/2.

LR requires one shared decision y=v=b. The four LR deterministic observer corners are
A=(0,0,3/2,3/2), B=(3/8,1/8,2,2),
C=(0,0,2,2), D=(1/2,1/2,3,3).

Two FULL split observations:
H_via=(1/8,3/8,5/2,5/2);
H_bypass=(3/8,1/8,5/2,5/2).

For w=(1,3,-1,-1) and h=-4, Phi(O)=4+eP+3eQ-TP-TQ.
An exact identity valid for ALL real LR x,y is
Phi_LR(x,y)=(1-x)*(1-y/4)>=0.

For ALL real FULL x,v,b:
Phi_FULL(x,v,b)=1-x+x*v/4-b/4 >= -1/4.

The FULL minimum -1/4 is attained at (x,v,b)=(1,0,1), the LR minimum 0 is attained at x=1. Thus the exact all-real support gap is 1/4, not a finite-grid estimate. The explicit LR-valid inequality Phi>=0 is violated by H_bypass at -1/4, giving L-infinity distance >= (1/4)/(1+3+1+1)=1/24. This genuine model has ONE LR merger; it illustrates the new lemma but is NOT a double-merger equal-hull counterexample.

## Seven vertices with a six-vertex facet, yet the edge test works

Abstract rational 4D vertices (x,y,z,t):
A=(0,0,0,0); B=(1,0,0,0);
C=(0,1,0,0); D=(0,0,1,0);
E=(-2,-2,1,0); F=(-2,-2,2,0); Q=(0,0,0,1).

All seven are extreme. Unique exposing maxima on the first six, after subtracting t, are respectively -x-y-5z, x, y, x+y+3z, -x-y-z, z; Q is uniquely exposed by t. Hence t=0 exposes a 3D facet with SIX extreme vertices. The inequality

4+x-4y-4z >= 0

holds at all seven vertices and vanishes precisely at C,D, exposing an edge. The abstract formal split H_via=A+D-B=(-1,0,1,0) has value -1, while H_bypass=C+B-A=(1,1,0,0) has value +1. The abstract L-infinity bound is 1/9. This is intentionally NOT claimed as a two-law stopping realization; it demonstrates why the new obstruction adds pruning power beyond the <=5-vertex criterion.

## Exact computation, evidentiary boundary and successor

Actually executed standard-library Python Fraction code, verifying all positive P/Q probabilities and exact r=1 collision, six deterministic model observations and bypass identity, both polynomial formulae on 729 FULL and 81 LR rational behavior grids, exact extrema at pure corners, the seven unique rational vertex exposing functionals and the six-vertex facet with exposed C-D edge. The completed execution printed PASS_EXACT_R5_BALANCED_BYPASS_NORMAL_CONE; the attached EXACT_OUTPUT.txt is actual stdout. All-real results rely on the algebraic factorizations and face proof, not these finite samples.

No independent mathematical review or formal Source registration was obtained, and this work does not prove the equal-hull/different-real-image mother problem. Novelty priority against existing general convex geometry literature is NOT claimed.

Next unit: for a genuine positive rational source-sensitive interacting DOUBLE merger with exact LR cross-product collisions, enumerate every deterministic LR observer vector and ordered action rectangle. Run both normalized rational normal-cone LPs first; publish separating w and actual FULL policy for any feasible case. For survivors, apply the <=5-facet veto, then complete all-signed convex-hull containment via exact facets/Farkas. Only after that attempt all-real LR image nonmembership with polynomial equations and zero-flow boundary cases. Preserve P/Q positive history provenance throughout.
