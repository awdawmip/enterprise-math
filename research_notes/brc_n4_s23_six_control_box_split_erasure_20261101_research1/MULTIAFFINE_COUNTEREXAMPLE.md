# Addendum: sharp two-control MULTIAFFINE counterexample to midpoint centers

Research date: 2026-11-01. Author analytic proof, exact integer validation; UNREVIEWED / NOT_ADMITTED. This is an additional theorem in the frozen BRC N=4 S23 finite source/observer model, not a native P000 theorem.

## Legal two-control rectangular policy face

Use the same eleven-parameter S23 source law and six-by-six M as PROOF.md in this directory. Freeze b_U=b_AV=0, the AU0 and AU1 third-stage controls to 1/2, and all B-side controls to a_B=1/4, b_BV=1/3, c_BU0=c_BU1=c_BV=1/2. The b_U control is SHARED across A and B groups as in the original S23 schema; since a_B and B-side c are fixed, its chosen value introduces no B variation. Let just two legal controls vary independently over the FULL real square:

a_A = a in [0,1], c_AV = c in [0,1].

The two AU prepared rows (both mixtures of identical AU0/AU1 source laws) are

p_AU(a,c) = (a,0,(1-a)/2,(1-a)/2),

while the AV singleton row is

p_AV(a,c) = (a,0,(1-a)c,(1-a)(1-c)).

The three B prepared rows are CONSTANT throughout this two-control square: BU=(1/4,0,3/8,3/8) twice, and BV=(1/4,1/4,1/4,1/4) once. This lists ALL six actual prepared distributions, rather than merely an isolated invented simplex.

## Exact theorem

For a legal anchor z=(alpha,gamma), let

R(z) = sup_{(a,c) in [0,1]^2} max_{i=0..5} TV(p_i(a,c),p_i(alpha,gamma)).

Then

(1) min_z R(z) = 2/3, attained at a UNIQUE parameter anchor (alpha,gamma)=(1/3,1/2).

(2) The ordinary parameter midpoint z_mid=(1/2,1/2) has exact R(z_mid)=3/4.

(3) The exact full two-control prepared-law diameter is D=1. Thus min R=2/3 > D/2=1/2.

These are statements for all REAL a,c, not grid extrapolations.

Proof, lower bound and uniqueness. The lawful policies (a,c)=(1,0),(0,1),(0,0) make the AV prepared law the three pairwise disjoint atoms e_1,e_3,e_4, respectively. At any anchor, AV has q=(alpha,0,(1-alpha)gamma,(1-alpha)(1-gamma)). Their max TV to q equals 1-min(q_1,q_3,q_4), which is at least 2/3 because the three nonnegative q entries sum to one. Equality requires all three entries exactly 1/3, forcing alpha=1/3 and gamma=1/2, so any optimal anchor must be this one.

Proof, matching upper bound. At z*=(1/3,1/2), both AU and AV anchor rows are exactly (1/3,0,1/3,1/3). For EVERY legal (a,c), their output laws lie in the triangle conv{e_1,e_3,e_4}; total variation from the equal-three-coordinate law is at most 2/3 by convexity and the atom values. The B rows do not change and have distance zero. Thus R(z*)<=2/3, closing the bound and uniqueness.

Proof, midpoint radius. At z_mid, both AU and AV anchor rows equal (1/2,0,1/4,1/4). The AV policies e_3 and e_4 have TV=3/4 from that law, and every point in their three-atom simplex has TV<=3/4 by convexity. The AU rows lie in the same simplex, B rows remain unchanged, so R(z_mid)=3/4.

Proof, diameter. AV outputs include both e_3 and e_4, whose TV distance is exactly 1; all pairs of probability measures have TV<=1. Therefore D=1. QED.

## Why it matters

The previous affine six-third-stage rectangle theorem has midpoint-optimal anchors and exact radius equal to half the diameter because the first two causal survivals are frozen. Allowing one first-stage variable a_A to vary jointly with a third-stage variable c_AV creates a genuine MULTIAFFINE product (1-a)c. Its lawful two-dimensional prepared-law image is a three-atom simplex rather than a centrally symmetric interval/zonotope. The exact Chebyshev radius 2/3 does NOT equal D/2, and the parameter midpoint has strictly suboptimal radius 3/4.

This explicitly discharges the first proposed two-control counterexample question in NEXT_TASK.md. It is a warning for any purported 11D 'half the box diameter' or simple parameter-midpoint certificate. It is not a lower bound for the unrestricted optimizable ten-label bank. Independent mathematical review and a native P000 six-axis/independent-time bridge are still outstanding.

Verification: VERIFY_MULTIAFFINE.js reconstructs the six prepared rows and checks the four exact corner policies, the three AV atom witnesses, the anchor values, the 2/3 and 3/4 radii and diameter one using integer numerators with denominator 24. The all-real proof is analytic; the finite check tests only arithmetic and vertices.
