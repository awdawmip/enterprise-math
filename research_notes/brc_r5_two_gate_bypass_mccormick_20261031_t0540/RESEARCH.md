# R5: rank-four McCormick obstruction for two shared STOP gates and a bypass

**2026-10-31 author-side portable research; independent mathematical review pending.**

## Scope and frozen input

The mother problem seeks a finite strictly positive two-law P/Q, genuine STOP/CONTINUE experiment with likelihood-ratio (LR) collisions whose FULL and *seedless* LR four-observer convex hulls agree, but their actual real behavioral images differ, at full four-dimensional affine rank. Predecessor: enterprise-math commit ed0d456470e39a114114c76734787cc4e8eddecd, research_notes/brc_r5_fourclass_time_hull_20261031_t0440. Normative inputs are GLOBAL_KNOWLEDGE_V1 main@5fc65ed14778a7980b29edc600982ef7f0e70853 and Enterprise Math main@f53d9c10a841f1e09d27b4219127c517cbe9cbfb. P000 and protected ACTIVE worldview remain unchanged. This is an auxiliary probability/observer model, not a native X6 physical theorem; the two stopping-time coordinates are an auxiliary observation, not a P000 native plane.

New result: exact equality of FULL and LR **actual two-time images**, plus a rank-four and **nonconvex** seedless LR four-observer image with an explicit FULL behavioral point inside the LR convex hull but outside the LR actual image. However, a complete McCormick facet argument proves that the **four-observer FULL and LR hulls remain strictly unequal**, excluding this full-rank bypass-template family from the mother target.

## Strictly positive P/Q experiment

Chance at time 0 selects origin A0, A1, B, C0, C1 with Q masses respectively 1/8, 1/8, 1/4, 1/4, 1/4 and initial likelihood ratios 2, 2, 1, 1/2, 1/2. Multiplication yields P masses 1/4, 1/4, 1/4, 1/8, 1/8. Both measures total one.

At time 1, A0/A1 visit the shared LR=2 CONTINUE gate x; C0/C1 visit the shared LR=1/2 CONTINUE gate z. STOP immediately terminates at time 1. A_i CONTINUE triggers the following fixed *strictly positive* natural chance kernel on terminal likelihood-ratio classes (Y,L,M,H), with R=(1,3/2,2,3):

| Q conditional | Y | L | M | H |
| --- | ---: | ---: | ---: | ---: |
| A0 | 1/4 | 1/12 | 3/8 | 7/24 |
| A1 | 1/4 | 1/6 | 1/4 | 1/3 |

For each A_i, its P conditional mass is Q conditional mass multiplied by R/2. All eight conditional masses are positive; each P and Q row sums to one and the Q moment of R is two. Outcomes L/M/H terminate at time 3. Outcome Y reaches a second **shared LR=1 STOP gate at time 2**: STOP immediately terminates at time 2, CONTINUE terminates at time 3. B bypasses the first x gate, entering Y directly at time 2 with Q=P=1/4. From each A_i, the unconditional Q and P mass reaching Y if it continues at x is 1/32. C_i CONTINUE forces termination at time 3.

Every terminal error probability is strictly inside (0,1): baseline delta=1/8 on every stopping path, with an additional 1/2 if B STOPs at Y or if C_i STOPs at time 1 (giving 5/8 on those paths). Four observables are (e_P,e_Q,T_P,T_Q): two error probabilities and two expected stopping times.

**BRC labelled residual:** K_A0-K_A1=(0,-1/12,1/8,-1/24), total variation 1/8. This is a difference of positive Q kernels, not a signed probability distribution. The forced time-3 class contrast is invisible to the chosen four-coordinate observer but remains a real source-labelled predictive residual for a terminal-class observer.

## Exact all-real behavior laws

FULL may choose distinct source-history parameters x0,x1, u0,u1,uB, z0,z1 independently in [0,1]. x_i,z_i are CONTINUE probabilities at time 1; u_i,uB are STOP probabilities at Y. Define x=(x0+x1)/2, z=(z0+z1)/2, w=(x0*u0+x1*u1)/2 and s=uB/4+w/16. Direct chance-weight summation gives

    e_P = 1/8 + uB/8 + (1-z)/8
    e_Q = 1/8 + uB/8 + (1-z)/4
    T_P = 3/2 + x + z/2 - s
    T_Q = 3/2 + x/2 + z - s.

A seedless LR policy must use x0=x1=x, u0=u1=uB=u and z0=z1=z at identical (time,LR) states; therefore w=xu and s=(1/4+x/16)u. No persistent random seed or offline convex-mixture surrogate is allowed in the LR actual image.

Let Phi(x,u,w,z) denote the affine map above, using u=uB. Its coefficient columns in observable order are

    X=(0,0,1,1/2), U=(1/8,1/8,-1/4,-1/4),
    W=(0,0,-1/16,-1/16), Z=(-1/8,-1/4,1/2,1).

The constant vector is (1/4,3/8,3/2,3/2). Exact rational elimination proves det[X,U,Z,W]=1/2048, so Phi is injective with full four-dimensional affine rank.

FULL realizes **all** feature quadruples in the convex polytope D_FULL={0<=x,u,z<=1, 0<=w<=x}. One inclusion follows from 0<=u_i<=1. For the reverse, choose x0=x1=x, z0=z1=z, uB=u and u0=u1=w/x when x>0, arbitrary when x=0. Consequently the FULL actual image Phi(D_FULL) is convex in this **particular** model.

## Theorem 1: exact equality of real two-time images

Both times depend only on (x,z,s), with x,z in [0,1] and 0<=s<=1/4+x/16. Every FULL choice respects those bounds, and for any such triple a seedless LR policy takes u=s/(1/4+x/16). The denominator stays strictly positive. Thus

    {(T_P,T_Q): FULL actual real} = {(T_P,T_Q): LR actual real}.

This is not only convex-hull equality: it is equality of the actual two-coordinate images. The exact rational verifier independently checks all 128 FULL and eight LR deterministic time outputs have the same six-vertex hull.

## Theorem 2: full-rank LR nonconvexity and a real FULL witness

Take seedless LR points V0=Phi(0,0,0,0)=(1/4,3/8,3/2,3/2) and V1=Phi(1,1,1,0)=(3/8,1/2,35/16,27/16). Their midpoint is

    M=(5/16,7/16,59/32,51/32).

M is actually realized by a FULL behavioral policy x0=1,x1=0,u0=1,u1=0,uB=1/2,z0=z1=0, using only a local Bernoulli choice at B's Y gate; no persistent seed.

For an arbitrary observer v=(eP,eQ,TP,TQ), set EP=eP-1/8, EQ=eQ-1/8. Invert Phi:

    u=16 EP-8 EQ; z=1-8(EQ-EP);
    x=z+2(TP-TQ);
    w=16(3/2+x+z/2-u/4-TP).

For M these four recovered coordinates are (x,u,w,z)=(1/2,1/2,1/2,0), violating the **necessary identity w=xu** for all real seedless LR behavior (which demands 1/4). Therefore M is in FULL_actual intersect conv(LR_actual) but not in LR_actual; the LR actual image is nonconvex even though its hull has full affine dimension four.

Quantitatively let G(v)=w(v)-x(v)u(v). G(M)=1/4, G=0 throughout LR. For any LR point v, set rho=||v-M||_infinity. The inverse formulas give |delta w|<=336 rho, |delta x|<=20 rho and |delta u|<=24 rho. Since both endpoints have decoded x,u in [0,1], |delta(xu)|<=44 rho. Therefore distance_infinity(M,LR_actual)>= (1/4)/380 = **1/1520**, for all real LR policies.

## Theorem 3: an exact rank-four McCormick no-go

The convex hull of the graph {w=xu; x,u in [0,1]} is exactly the four-facet McCormick envelope

    w>=0, w<=x, w<=u, w>=x+u-1.

The inclusion one way follows from the products. Conversely, for any feasible (x,u,w), weights w, x-w, u-w, 1-x-u+w on four Boolean corners (1,1),(1,0),(0,1),(0,0) are nonnegative and sum to one; split z independently between zero and one. Hence conv(LR_actual)=Phi(D_McCormick). FULL's feasible (x,u,w,z)=(1,0,1,0) violates w<=u. Since Phi is injective,

    conv(LR_actual) is a STRICT subset of conv(FULL_actual)=FULL_actual.

The explicit signed observable direction

    H=14e_P-19e_Q+2T_P-4T_Q

obeys **8H+53=w-uB** under every real FULL policy, and w=xuB under LR. Exact extreme values follow by choosing FULL (x,uB,w)=(1,0,1) and LR w<=u:

    sup_FULL H = -13/2, sup_LR H = -53/8, gap=1/8>0.

This excludes the entire **four-feature bypass template** at four-dimensional rank under the precise hypotheses: FULL's feasible feature region includes D_FULL, LR is the product graph, and the four-coordinate affine observation map is injective. If the coefficient rank falls below four, the full-dimension mother requirement fails. The argument does NOT classify arbitrary two-gate STOP trees containing other path products, flow constraints, repeated decision keys or additional mergers.

## Evidence, existing mathematics and next problem

The sibling VERIFY.py was actually executed with the Python standard-library Fraction type; EXACT_OUTPUT.txt records the run ending PASS_EXACT_R5_TWO_GATE_BYPASS_MCCORMICK_RANK4. Checks include all P/Q chances, likelihood ratios, positive natural transitions, strictly interior error probabilities, origin residual TV, two-time hull by exact rational monotone-chain, 128 FULL/8 LR deterministic policies, rank determinant, actual FULL midpoint witness, four-observer exact separator and distance constant. Finite enumeration confirms the concrete rational instance; *all-real* statements are analytical consequences of the exact parameterizations, inverse and corner convex-decomposition proof.

McCormick bilinear-envelope inequalities are classical, not a project novelty claim. Related verified literature: Khademnia & Davarnia, Convexification of bilinear terms over network polytopes (2023), https://arxiv.org/abs/2302.14151; Oh & Yang, On the convexification of a bilinearly constrained set with a common variable (posted 2026-10-12), https://arxiv.org/abs/2610.16116. These do not prove the present stopped P/Q experiment. BRC reuse is typed labelled-positive-branch flow and prospective observer factorization; this is not a heartbeat/BRC-Shor native computation.

Next exact task: add another interacting merger/product and physical cross-flow coupling, so FULL cannot choose McCormick-forbidden w>u independently at rank four. First prove two-time equality, then **all-signed four-observer convex-hull equality** by exact rational convex certificates/Farkas separation and rank, only then real-image nonmembership. Do not rescan error coefficients in the already excluded four-feature bypass template. Full continuation in NEXT_TASK.md.

**Status observed 2026-10-31:** AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING. Native Sites gateway reported research_authority_granted=false and write_relay_enabled=false; active Owner query returned CONTROL_QUOTA. No Source session, current owner, CLAIM, Result, mathematical acceptance or independent Driver review is asserted. Exposed historical context remains disclosed. Neutral GitHub author-side publication is not native research admission.
