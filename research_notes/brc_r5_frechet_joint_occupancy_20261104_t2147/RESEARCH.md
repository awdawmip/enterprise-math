# R5: Fréchet-consistent competing occupancies — equal hulls with a nonconvex seedless image

Date: 2026-11-04. Status: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY. Mother R5 remains open.

## Context and exact scope

Predecessor: enterprise-math@d341c7bde87276ec94277eede1d5c019024e7d7a, research_notes/brc_r5_competing_capacity_certificates_20261104_t2055/RESEARCH.md. It used independent simplex occupancy variables y in Delta_k and z in x Delta_k and found a generic strict support gap. We now impose exact joint-marginal conservation. Frozen scientific pins: Global a01383f825ef9d43b4b754254303298c64041568; EM 86149263e38c22292c9def1e0f69092efa1be77e. Current normative context read separately. The model has auxiliary nonabsorbing controls and a declared affine observer; it is not yet an R5 stop/continue/declare O4 model.

## Joint occupation model

Let X in {0,1} be a first nonabsorbing action and J in {0,1,...,k}, k>=1, a later nonabsorbing categorical action. FULL remembers X in the later decision. A seedless LR controller, at a shared time and likelihood-ratio key, does not remember X and chooses J using one unconditional distribution.

Write p_{a,i}=Pr(X=a,J=i), x=Pr(X=1), y_i=Pr(J=i), z_i=Pr(X=1,J=i) for i=1,...,k. FULL's exact all-real feasible joint-marginal polytope K_k is

    y_i>=0, z_i>=0, z_i<=y_i, sum_i y_i<=1,
    sum_i z_i <= x <= 1 - sum_i y_i + sum_i z_i.

Necessity is immediate. Sufficiency follows by constructing the atoms:

    p_{1,i}=z_i,           p_{0,i}=y_i-z_i    (i>=1),
    p_{1,0}=x-sum_i z_i,   p_{0,0}=1-x-sum_i y_i+sum_i z_i.

They are nonnegative and sum to 1; draw X with marginal x and draw J conditional on X with the indicated row probabilities (arbitrary conditional on a zero-mass row). Hence every feasible vector is causally attainable by FULL. For seedless LR, independence of the two action distributions is exact: z_i=x*y_i. When k=1 the FULL constraint is the Fréchet bound max(0,x+y-1)<=z<=min(x,y).

## Theorem (universal affine hull equality)

For any real vector space V and arbitrary A,B_i,C_i in V, define

    Phi(x,y,z)=x A + sum_i (y_i B_i + z_i C_i).
    F=Phi(K_k);
    L={Phi(x,y,xy): 0<=x<=1, y_i>=0, sum_i y_i<=1}.

Then for every finite k>=1 and every choice of coefficients,

    F = conv(L) = conv({0,A} union {B_i,A+B_i+C_i:1<=i<=k}).

Proof. Every FULL joint distribution is a convex combination of the 2(k+1) deterministic Dirac laws on (X,J)=(0,0),(1,0),(0,i),(1,i). Their Phi images are respectively 0,A,B_i,A+B_i+C_i. Each deterministic Dirac law is also a seedless independent product policy, so these endpoints are in L. The FULL joint-distribution simplex is their convex hull and Phi is affine in the atom probabilities. L is contained in F. Both convex-hull inclusions follow, establishing the identity for arbitrary real parameters. QED.

Unlike the earlier independent z-in-x-Delta_k model, every cross-occupancy is constrained by both its own branch marginal and the complementary unused probability mass. The resulting full hull and seedless hull agree identically, yet nonlinear seedless image differences may survive.

## Exact four-coordinate nonmembership witness

Take k=1 and V=R^4 with A=(1,0,0,0), B_1=(0,1,0,0), C_1=(0,0,1,0). Then Phi(x,y,z)=(x,y,z,0).

The FULL set is the tetrahedron with vertices

    (0,0,0,0), (0,1,0,0), (1,0,0,0), (1,1,1,0).

The seedless LR set is the bilinear graph L={(x,y,xy,0):x,y in [0,1]}. The midpoint

    W=(1/2,1/2,1/2,0)
      = [Phi(0,0,0)+Phi(1,1,1)]/2

belongs to FULL and conv(L). It is outside L because x=y=1/2 forces xy=1/4 rather than 1/2. Therefore L is nonconvex although its convex hull equals FULL exactly.

The exact infinity-distance to the seedless image is

    dist_infty(W,L) = sqrt(5)/2 - 1 > 0.

Proof. If a seedless point is within distance d then x,y<=1/2+d and xy>=1/2-d. Thus (1/2+d)^2>=1/2-d, implying d^2+2d-1/4>=0 and d>=sqrt(5)/2-1. At d equal to the positive root choose x=y=1/2+d; their product is 1/2-d, giving equality. QED. This is nonlinear nonmembership, not a hyperplane separator: the convex hulls are equal.

## Explicit positive P/Q experimental realization, with model boundary

A finite two-measure process with nonabsorbing controls realizes the joint occupancy. Before actions, each of two chance source outcomes has Q and P probability 1/2, strictly positive. The binary action X does not stop the process. At the second decision all histories have the same time and likelihood ratio 1, though FULL can remember X; choose categorical J without stopping. At the final independent terminal chance signal H, use Q(H=0,1)=(1/2,1/2), P(H=0,1)=(1/3,2/3), all positive. Terminal likelihood ratios are 2/3 and 4/3. The auxiliary Phi uses action-indicator expectations under Q (or P before terminal H), so this process realizes the stated equal-hull/nonconvex mechanism.

Original R5 instead demands stop/continue/free P/Q terminal declarations and O4=(eP,eQ,TP,TQ). The nonabsorbing actions and auxiliary readout are an explicit changed-model ingredient. An admissible R5 realization, or a precise obstacle to it, remains open. No claim of a mother-question solution or project admission is made.

## Exact verification and continuation

Standard-library Python Fraction verifier checks the exact K_k atom reconstruction for all 84 binary-by-binary joint laws with denominator 6, all 462 binary-by-three-category joint laws with denominator 6, and 49/196 seedless product policies. It verifies the tetrahedron midpoint and all 625 signed integer four-coordinate support directions, plus exact root isolation 0.118<sqrt(5)/2-1<0.119. Actual output ends PASS_EXACT_R5_FRECHET_COUPLING_LIFT. These exhaustive rational grids are sanity checks; the continuous theorem and distance are established analytically above.

Next: construct a legitimate positive P/Q BRC with historical information collisions and exclusively stop/continue/declare actions; derive its joint occupancy conservation and full O4 deterministic vertices. First check hull equality with at most five-vertex rational mixtures or a rational strict separation; then prove or refute nonlinear membership. Retain source/path residuals, current owner state and separate scientific pins.