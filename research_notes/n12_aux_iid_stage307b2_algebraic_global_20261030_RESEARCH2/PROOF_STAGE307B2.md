# Stage307-B.2 — exact algebraic global public minimax

Status: PORTABLE_AUTHOR_PROOF / EXACT_RATIONAL_CERTIFICATE_EXECUTED / UNREVIEWED / NOT_ADMITTED. This is an external finite positive-rational BRC observer model, not a native P000 X6 theorem.

Inputs fixed: GLOBAL_KNOWLEDGE_V1 main@51309f36bdcd96b26f08d9a10153cfca1142ecda; enterprise-math main@dcde68d8979770a9aa5d29ef7a0591a98b9913de; original P000 V5 blob bcc2590d3168a28f72e8b9f0f9b1f76faadcd488; Stage306-B commit e6801c19582e0a91be182fb49561f685b08cc403; Stage307-B.1 commit 505192696012143fbbbc8a4cbd690bd59112568d. The actual owner was not confirmed (CONTROL_QUOTA); research_authority_granted=false. No native session, CLAIM, Result, independent review or admission is inferred.

## Theorem: unique exact algebraic minimizer, all real rates and all public-history H/F policies

Let b_k(z)=z^k(1-z)^(3-k), p=(61,21,9,9)/160,
r_k(x,y)=4b_k(x)/5+b_k(y)/5-p_k, and
d(x,y)=(1/2) sum_{k=0}^3 binom(3,k)|r_k(x,y)|.
Stage306 proved that the exact full eight-rate public minimax (three future visits, arbitrary public-history adaptive H/F policies) is R3*=(5/8) min_{[0,1]^2}d, because all-F maximizes TV by data processing and the outer G fibers are mirrors. Each private history locks one deterministic real Bernoulli rate; no within-label rate randomization or reset is allowed.

Let a* be the unique root of
F(a)=(41/16-4a^2)^3-(61/32-4a^3)^2
on the rational interval (7689/10000,769/1000).
Set x*=1-a*, y*=1-sqrt(41/16-4a*^2).
Then (x*,y*) is the UNIQUE GLOBAL minimizer of d on the entire real square, and

R3*=9/256-(4x*^3+y*^3)/8
approximately 0.0075582672377169382906614428725878773953.

Equivalently x* is the unique root in (231/1000,2311/10000) of
327680x^6-1966080x^5+4411392x^4-4475904x^3+2027712x^2-408960x+30123=0.
No complete Pareto-frontier claim is made.

## Analytic root existence and strict minimum in a rational box

Take B=[23/100,24/100] x [55/100,56/100]. Equations r0=r1=0 are exactly
4(1-x)^2+(1-y)^2=41/16 and
4(1-x)^3+(1-y)^3=61/32.
Put a=1-x in [.76,.77], b=1-y in [.44,.45].
Along the first equation,
G(a)=4a^3+(41/16-4a^2)^(3/2)-61/32
satisfies G'(a)=12a(a-b)>0.
At a0=7689/10000 and a1=769/1000, direct rational arithmetic gives F(a0)<0<F(a1); both 41/16-4a_i^2 are between (.44)^2 and (.45)^2, and 61/32-4a_i^3>0. Thus F and G have the same signs, and there exists a unique zero within the rational interval. It supplies the unique point in B at which r0=r1=0.

Rational Bernstein extrema show r2>0 and r3<0 throughout B, and r0+3r1+3r2+r3=0. Therefore
d=3r2+max(0,r0)+3max(0,r1).
Put L=3r2+(3/5)r0+(2/3)r1. For dx=x-x*,dy=y-y*,
d-d* >= L-L*+(2/5)|r0|+(2/3)|r1|.
By scalar mean-value identities, r0=-A dx-B' dy and r1=C dx-D dy for some positive coefficients satisfying throughout B:
69/50<A<3/2, 11/100<B'<3/20,
17/100<C<1/5, 57/1000<D<7/100.
Hence AD+B'C>9/100, and inversion gives
|dx|+|dy|<=3|r0|+(55/3)|r1|.
Consequently (2/5)|r0|+(2/3)|r1| >= (1/30)(|dx|+|dy|).
Direct differentiation gives
L_x=-(4/75)(132x^2-104x+17),
L_y=-(1/75)(132y^2-104y+17),
both absolutely <1/40 on B (exact endpoint checks; the quadratic vertex 104/264 lies between x- and y-intervals).
Integration along a straight segment in convex B yields
d(x,y)-d(x*,y*) >= (1/120)(|x-x*|+|y-y*|).
This proves strict uniqueness throughout B without approximations.

## Exact GLOBAL exclusion outside B

The complement of the interior of B is covered by four rational rectangles:
[0,23/100]x[0,1]; [24/100,1]x[0,1];
[23/100,24/100]x[0,55/100];
[23/100,24/100]x[56/100,1].

At rational witness (xw,yw)=(231083940855/10^12,555508857277/10^12),
direct exact evaluation gives
U=d(xw,yw)=15116534475889766921898005231381567/1250000000000000000000000000000000000.

For each I x J, the exact min/max of b_k on an interval are attained at endpoints and (for k=1,2) at k/3 when contained in the interval. These rational extrema bound each residual r_k between l_k,u_k and yield the valid continuum bound
d(x,y) >= LB(I,J)=(1/2) sum binom(3,k) max(0,l_k,-u_k).

Recursively bisect the longer physical side (ties x), accepting a leaf only when LB>U STRICTLY. The executed exact Fraction computation exhausts the four rectangles in (nodes, leaves) counts:
(329,165), (55,28), (27,14), (133,67):
544 nodes, 274 leaves, maximal dyadic depth 18.
The independent checker verified each persisted path's exact strict rational bound, prefix-freeness, and dyadic Kraft sum 1 per region. Therefore every REAL point outside B satisfies d>U.
The unique algebraic minimizer inside B has d*<=U (since the rational witness is in B), so is also the unique global minimizer. At it r0=r1=0 and r3=-3r2<0, whence d*=-r3=9/160-(4x*^3+y*^3)/5. Multiplication by 5/8 proves the announced exact value.

## Reproducibility and scope

Reproducer: REPRO_STAGE307B2.py (pure Python Fraction) tests all rational signs/ranges and constructs all 274 leaves; its executed stdout is included. The independent verifier in the full local handoff also checked the leaf path cover and strict bounds. The continuum inference additionally uses the written endpoint-extremum, IVT, monotonicity, and mean-value arguments; neither floating approximations nor finite grid points establish the continuum claim.

BRC method reuse: finite explicit positive-rational branch carrier with S,J,W,Y provenance and declared public quotient, definitions/ENTERPRISE_BRC_WEIGHTED_GLOBAL_SUBSTRATE_20260902.json, source blob f375a059fa4af8c6eefaddb4d4a8689a0c063674. This auxiliary result does not assert a P000 native X6 path/triadic closure/time/final-Cell embedding, or novel Foundation acceptance.

Next: Stage308-B — sharp Pareto frontier F(p)=inf{T3(t):P3(t)<=p} between the algebraic public optimum and unique joint-audit optimum 77/1024; prove a parametric exact-semi-algebraic branch/breakpoint or exact counterexample. Preserve both observer scopes and the separate native transfer obligation.
