# PREFIX-405 | Exact NO certificates for six noisy observations and a robust nonconvexity witness

Date: 2026-11-01. Author-side verified, UNREVIEWED, NOT_ADMITTED, NATIVE_REGISTER_PENDING. External auxiliary static five-Port complex model, not a P000-native X6 or typed-BRC dynamical theorem.

Source pins: GLOBAL_KNOWLEDGE_V1 main@eeb6afada377b79c8148e040e1a5b74e00b436be, Enterprise Math main@1fde72896593e8b10c9abb356983a265d2a4600f. Predecessor: research_notes/2026-11-01_prefix404_dual_144_and_all_noisy_two_parameter_fiber.md.

## Model
Original five-row complex matrix:
A = ((4,4,0),(0,-4,4),(-5+3i,0,-3+i),(-2-2i,4+4i,2+2i),(-2,0,5+2i)).
Top 3x3 block A3 has determinant -32+32i. With I1=1 and global common phase removed, W=A3*Y=(1,u,v), and Y=A3^-1*W. All observations are rational closed bands of the six real quantities
I2=|u|^2, Cu=|1+u|^2, I3=|v|^2, Cv=|1+v|^2,
I4=|a4+b4*u+c4*v|^2, I5=|a5+b5*u+c5*v|^2,
(a4,b4,c4)=(5/2+9i/2,3/2+7i/2,4i),
(a5,b5,c5)=(11/4+15i/8,11/4+15i/8,5/4+9i/4).

## Theorem A: exact, replayable all-six-band NO semi-decision; strict-interior YES semi-decision

There is an explicit rational procedure returning (i) a reconstructed rational complex source for any YES, or (ii) a finite box partition with exact rejection inequalities for any NO. It *terminates with NO on every infeasible finite rational closed-band instance*, and terminates with YES if some source places all six observations strictly inside their bands. Boundary-only YES may require an algebraic solver and is reported UNKNOWN if the finite budget runs out.

Proof. I2 and I3 bound four real source coordinates z=(Re u,Im u,Re v,Im v) within the compact rational cube [-R,R]^4, R=1+max(upper(I2),upper(I3)). Negative squared-norm upper bounds immediately imply NO. The identities
Re u=(Cu-1-I2)/2 and Re v=(Cv-1-I3)/2
provide real-part enclosures. The corresponding squared imaginary parts yield rational lower/upper square-root enclosures via integer isqrt, split into up to two signs per amplitude.

For a rational box B with center z0, coordinate radii r_j and an observation F(z)=|a+b*u+c*v|^2, put gamma=(b,i*b,c,i*c),
M=|Re L(z0)|+|Im L(z0)|, D=sum_j (|Re gamma_j|+|Im gamma_j|)*r_j, L=a+b*u+c*v, E=2*M*D+D^2.
Then |F(z)-F(z0)| <= E throughout B. If [max(0,F(z0)-E),F(z0)+E] misses the required band, reject that entire box with the observation label as a replayable NO leaf. If the center satisfies all six observations, return its exact rational source and reconstruct Y=A3^-1(1,u,v). Otherwise split the box along its longest coordinate at the rational midpoint, using fair breadth-first traversal. Independently verifying each exact division and rejected leaf verifies the full NO certificate.

For any NO instance, Phi(z)=max_j dist(F_j(z),J_j) is continuous, positive on the compact bounding cube, and has min delta>0. As the longest-edge dyadic boxes shrink, their interval error E tends uniformly to zero; every sufficiently small box center violates some band by >=delta and is rejected because E<delta. Thus NO terminates on all infeasible cases. For a strict-interior YES, continuity gives a feasible open neighborhood, and dyadic rational centers eventually enter it. This is not a full solver for zero-dimensional irrational algebraic boundary-only YES, and no polynomial bit complexity is claimed.

## Theorem B: observation image is nonconvex; its gap survives six positive band widths

Two distinct complex sources W+=(1,i,0) and W-=(1,-i,0) have six observations
F(W+)=(1,2,0,1,37,709/32),
F(W-)=(1,2,0,1,45,709/32).
Their midpoint m=(1,2,0,1,41,709/32) is not realizable: I3=0 implies v=0; I2=1 and Cu=2 imply u=+i or -i, so I4 must be 37 or 45, not 41. Hence source observations cannot safely be compressed by averaging.

Set eps=1/10000 and give all six measurements nonzero-width rational bands:
J2=[1-eps,1+eps], Ju=[2-eps,2+eps],
J3=[0,eps], Jv=[1-eps,1+eps],
J4=[40,42], J5=[22,23].
The first two bands force |Re u|<=eps and 999/1000<|Im u|<1001/1000. The next two force |Re v|<=eps and |Im v|<=1/100. Write k=sign(Im u) in {+1,-1}. Relative to (u,v)=(k*i,0), the fourth Port amplitude has complex l1 variation at most
D<=5*(11/10000)+4*(101/10000)=459/10000.
At k=+1, its nominal amplitude is -1+6i, norm-square 37, l1 size 7; at k=-1 it is 6+3i, norm-square 45, l1 size 9. Thus:
k=+1: |I4-37|<=64470681/100000000;
k=-1: |I4-45|<=82830681/100000000.
Both intervals are disjoint from [40,42]. The certified minimum exclusion margin is exactly 217169319/100000000 > 0. Replacing J4 by [36,38] or [44,46] makes a + or - source feasible with all six bands of positive width. This proves a robust nonconvex void, not merely an equality-point obstruction.

## Verification, status and continuation

Executed in Python 3.13.5:
- Standard library Fraction/isqrt solver and NO certificate replayer: PASS_PREFIX405_COMPLETE_NO_SEMIDECISION_AND_ROBUST_NONCONVEXITY. The middle-band NO case creates exactly two initial sign-boxes, each rejected by I4.
- Independent SymPy 1.14.0 reconstruction from the original five-Port matrix: PASS_PREFIX405_INDEPENDENT_ORIGINAL_MATRIX_AND_ROBUST_GAP.
Both are author-side mathematical checks. Generic CAD, boundary-only YES completion, independent review and mathematical admission remain to be done.

BRC observer/provenance policy: REUSE_APPLIED for branch-preserving readout; preserve full original complex source, two sign branches, phase and Port labels. No typed BRC operation or native X6 bridge has been executed.

Current native service 0.6.11 reports research_authority_granted=false; Owner/task list query returns CONTROL_QUOTA. This publication is ordinary research evidence, not a CLAIM, Result, review or Foundation admission.

PREFIX-406: implement finite algebraic YES witnesses for boundary-only feasible records, including irrational isolated contacts, tangencies, repeated circles and collapsed bands; compose with exact NO certificates into a complete solver. Separately analyze bit complexity and typed observer preservation.
