# Exact rational Chebyshev certificate for a non-simplex S23 two-control box

Research date: 2026-11-01. Author-side exact analytic proof with independently executed V8 integer sanity checks. Status: **UNREVIEWED / NOT_ADMITTED**. This extends the already preserved S23 two-control full-square counterexample at PR #1765, immutable predecessor 52b75934716d469de77ec5bd43c1eee936101741; it neither reproves nor revises P000.

## 1. Frozen, lawful positive-source BRC model

Use the six labelled sources (AU0, AU1, AV, BU0, BU1, BV), the four stopping outcomes and the matrix

20 M = [[10,10,0,0,0,0],[9,11,0,0,0,0],[0,0,20,0,0,0],[0,0,0,10,10,0],[0,0,0,2,18,0],[0,0,0,0,0,20]].

Every source follows the legitimate three-stage stopping distribution F(a,b,c)=(a,(1-a)b,(1-a)(1-b)c,(1-a)(1-b)(1-c)). Freeze b_U=b_AV=0, c_AU0=c_AU1=1/2, and all B controls at a_B=1/4,b_BV=1/3,c_BU0=c_BU1=c_BV=1/2. All six prepared laws are then

p_AU0=p_AU1=(a,0,(1-a)/2,(1-a)/2),
p_AV=(a,0,(1-a)c,(1-a)(1-c)),
p_BU0=p_BU1=(1/4,0,3/8,3/8),
p_BV=(1/4,1/4,1/4,1/4).

The shared first-stage A control a=a_A and the AV-only third-stage control c=c_AV vary independently in the rational box Q=[A,B]×[C,D]. All unmentioned controls remain frozen, including the shared b_U used by both A and B source groups. The representation retains all six source identities and prepared observations; AU equalities in this face follow from explicitly frozen identical AU kernels, not a declaration of global observer redundancy.

## 2. General rational-box finite LP theorem

For arbitrary 0≤A≤B≤1 and 0≤C≤D≤1, set alpha in [A,B], gamma in [C,D] for a lawful anchor; put beta=(1-alpha)gamma. Its AV law is q=(alpha,0,beta,1-alpha-beta). Since a three-atom zero-sum signed difference has TV equal to the maximum absolute coordinate difference, exactly

TV(p_AV(a,c),q)=max(|a-alpha|, |(1-a)c-beta|, |a+(1-a)c-alpha-beta|).

Also TV(p_AU(a),p_AU(alpha))=|a-alpha|, which is pointwise dominated by the AV expression. The B prepared laws are constant. Thus the full six-input anchor risk is precisely the supremum of the AV expression.

The parameter image in (a,y=(1-a)c) is the convex polygon

P={ (a,y): A≤a≤B, C(1-a)≤y≤D(1-a) }.

Its vertices are images of the four box corners (with degeneracies allowed). The exact coordinate ranges are

a ∈ [A,B],
y ∈ [(1-B)C,(1-A)D],
a+y ∈ [A+(1-A)C, B+(1-B)D].

Consequently for every lawful anchor (alpha,beta)∈P, the maximum over ALL REAL parameter values is the following finite maximum of affine forms:

R(alpha,beta)=max{
alpha-A, B-alpha,
beta-(1-B)C, (1-A)D-beta,
alpha+beta-[A+(1-A)C],
[B+(1-B)D]-(alpha+beta)
}.

The exact best lawful anchor is therefore obtained by the three-variable LP: minimize r subject to (alpha,beta)∈P and all six displayed expressions ≤r. This is a necessary AND sufficient continuum certificate, not a grid approximation. For rational bounds the LP has a rational minimizing (alpha,beta,r); recover gamma=beta/(1-alpha) if alpha<1, and any permitted gamma if alpha=1 (then beta=0). A rational primal feasible anchor together with a rational nonnegative combination of risk inequalities reaching the same r proves the exact optimum. No arbitrary independent prepared-law center is substituted for a lawful common-parameter anchor.

## 3. Exact non-simplex rational example: strict diameter/2 gap

Take A=C=1/4, B=D=3/4. The four AV corner laws, written as (p1,p3,p4) with the identically zero p2 suppressed only for exposition, are

(A,C)=(1/4,3/16,9/16),
(A,D)=(1/4,9/16,3/16),
(B,C)=(3/4,1/16,3/16),
(B,D)=(3/4,3/16,1/16).

They form a proper quadrilateral within the three-atom simplex (not the full simplex of the preceding [0,1]^2 result). Their coordinate extrema are
alpha-direction [1/4,3/4], beta-direction [1/16,9/16] and alpha+beta [7/16,15/16]. Thus the exact six-row risk for any (alpha,beta)∈P is

R=max{alpha-1/4,3/4-alpha,beta-1/16,9/16-beta,
alpha+beta-7/16,15/16-alpha-beta}.

**Exact dual lower bound:** Three of these inequalities give

3R ≥ (3/4-alpha)+(9/16-beta)+(alpha+beta-7/16)
   = 7/8,

hence R≥7/24 for ANY lawful anchor. This is an explicit finite LP dual certificate with positive unit multipliers (a valid bound even without using P).

**Exact primal and uniqueness:** Set alpha=11/24, beta=13/48. It is lawful since gamma=beta/(1-alpha)=1/2 belongs to [1/4,3/4]. Substitution in the six affine constraints yields respectively (5/24,7/24,5/24,7/24,7/24,5/24), so R=7/24. At equality in the three-term lower-bound sum all three inequalities must be tight, forcing alpha=11/24 and beta=13/48, hence the original anchor (a,c)=(11/24,1/2) is UNIQUE.

The ordinary parameter midpoint (1/2,1/2) produces (alpha,beta)=(1/2,1/4), and its radius is exactly 5/16 >7/24. The full face diameter is 1/2: every one of the three relevant coordinate ranges has width 1/2, so TV between any two laws is ≤1/2, attained for example at the AV corners (A,D) and (B,C). Consequently

min-lawful-anchor R = 7/24 > diam(Q)/2 = 1/4,

with exact positive gap 1/24. The LP optimum corrects the midpoint first control by -1/24 while keeping c=1/2.

The three independently ideal coordinate midranges (alpha,beta,alpha+beta)=(1/2,5/16,11/16) cannot hold jointly because 1/2+5/16=13/16≠11/16. The failure of 'half the diameter' is a joint-relation consistency obstruction, not rounding or an arbitrary loss of source provenance.

## 4. Finite exact verification and limits

VERIFY.js was executed under a V8 JavaScript isolate with ordinary exact safe-integer arithmetic and scale 2400. It checks the actual six-source M mixture, all 121 lattice policies in this rational box, all 726 prepared row comparisons, every AV/AU domination check, all four sharp corner risks, the exact full-face diameter, the midpoint, and the three tight dual inequalities. Saved output: RUN_EVIDENCE.json. The all-real statements follow from the analytic coordinate-extrema proof, not from the 121-point lattice.

BRC reuse: REUSE_APPLIED (labelled positive sources, observer rows, total-variation metric, and S23 lawful causal controls from the existing PR). The LP parametrization (alpha,beta) is a coordinate change of **the same six-law observation**, not a reduction in native six-dimensional Cell dimensions. This result only covers this frozen two-control S23 face; no global eleven-parameter or free ten-label minimax improvement is asserted. Earlier unrestricted 1/2≤R_beh(k,10)≤2/3, k=4,6, remains unchanged. Formal Owner/CLAIM/Result and independent review are separate; P000 X6/independent-time bridge and the S2 information-set extension remain unproved here.
