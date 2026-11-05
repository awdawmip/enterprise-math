# S23 lawful-versus-convexified gap: a minimal three-tagged-Bernoulli witness

Date: 2026-11-05. Frozen scientific model: enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34, research_notes/brc_n4_s23_asymmetric_hull_gap_sqrt43_20261101_research1/PROOF.md. Status: AUTHOR_ANALYTIC_PROOF / EXACT_ALGEBRAIC_EXECUTED / UNREVIEWED / NOT_ADMITTED.

## Exact lawful source/observer model

Let Q=[1/2,7/8] x [1/8,1/2] x [1/2,7/8], theta=(a,b,c). The shared second-stage parameter b is one legal control for the A and B branches. The four-stop law is F(u,v,w)=(u,(1-u)v,(1-u)(1-v)w,(1-u)(1-v)(1-w)). Retain all original BRC source labels AU0,AU1,AV,BU0,BU1,BV. Three particular source rows are AU0=F(a,b,1/2), AV=F(a,0,c), BU0=F(1/4,b,1/2).

Apply three deterministic, source-tagged, four-stop-to-Bernoulli kernels:
- K1: AV, indicator of stop 1;
- K2: AU0, indicator of stops 3 or 4;
- K3: BU0, indicator of stop 2.

The three success probabilities are
J(theta)=(a,(1-a)(1-b),3b/4).                        (1)

This is a tagged family of three Bernoulli marginals, not a normalized three-outcome law and not three samples assumed independent. The source labels and common legal parameter b are retained. For nonempty I subset {1,2,3}, define d_I(J(theta),J(z))=max_{i in I}|J_i(theta)-J_i(z)|, the maximum tagged Bernoulli TV. Define lawful radius R_I^L=min_{z in Q}max_{theta in Q}d_I and joint-convexified radius R_I^H=min_{V in conv J(Q)}max_{theta in Q}max_{i in I}|J_i(theta)-V_i|. Convexification means ONE common distribution over whole lawful strategies.

## Theorem (complete proper-subset minimality)

Put r=(sqrt(43)-5)/8. For I={1,2,3}, precisely
R_I^L = r,
R_I^H = 3/16,
R_I^L-R_I^H = (2sqrt(43)-13)/16 > 0.                 (2)

For EVERY nonempty PROPER subset I of the chosen three events,
R_I^L=R_I^H=9/64 if I={3}, and 3/16 otherwise.     (3)

Thus all three chosen source-tagged Bernoulli events are jointly sufficient to retain the full lawful-vs-hull gap of the frozen six-source three-control problem, but any two of these exact designated events lose that gap. This minimality is relative to these three events, not a claim across all possible observers.

## Analytic proof valid on the full real box

The ranges of the three coordinates are exactly:
J1(Q)=[1/2,7/8]; J2(Q)=[1/16,7/16]; J3(Q)=[3/32,3/8]. (4)
All range endpoints are achieved at actual lawful parameter vertices; thus supremum in the max-coordinate event loss is attained at these endpoints for any fixed center. This is a continuum extremum argument, not a grid approximation.

For any lawful center z=(x,y,t) with maximal three-event error u>=0, three legal event comparisons give
u>=7/8-x, u>=7/16-(1-x)(1-y), u>=(3/4)(1/2-y).
Consequently 1-x<=1/8+u, 1-y<=1/2+4u/3, and (1-x)(1-y)>=7/16-u. Nonnegativity of both factors implies
(1/8+u)(1/2+4u/3)>=7/16-u,
i.e. 32u^2+40u-9>=0. The polynomial increases strictly for u>=0 and its positive root is r=(sqrt43-5)/8; hence every lawful center has radius >=r.

Since the polynomial is negative at 3/16 and positive at 1/5, 3/16<r<1/5. The legal center x=7/8-r, y=1/2-4r/3, t=1/2 has
J(x,y,t)=(7/8-r,7/16-r,3/8-r).
The polynomial root relation implies (1-x)(1-y)=7/16-r. Against (4), each coordinate's upper-side error equals r; the other-side errors are 3/8-r, 3/8-r, and 9/32-r, all <=r. This proves R_{123}^L=r.

For one JOINT convex hull center, mix the four complete legal strategies with (a,b)=(1/2,1/8),(1/2,1/2),(7/8,1/8),(7/8,1/2) and common weights (4/9,1/18,2/9,5/18), with any legal c (e.g. 1/2). Their image under J is exactly
V=(11/16,1/4,3/16) in conv J(Q).
Over (4) its maximum coordinate error is 3/16. The J1 range alone forces every hull center to have error >=(7/8-1/2)/2=3/16. Therefore R_{123}^H=3/16. Finally 2sqrt43>13 follows from 172>169, so (2) is a strict positive gap.

For any nonempty I, half the largest included coordinate range is a universal lower bound on BOTH radii. The following legal centers attain that lower bound:
I={1}: (x,y)=(11/16,1/5), radius 3/16;
I={2}: (11/16,1/5), radius 3/16;
I={3}: (11/16,5/16), radius 9/64;
I={1,2}: (11/16,1/5), radius 3/16;
I={1,3}: (11/16,5/16), radius 3/16;
I={2,3}: (7/11,5/16), radius 3/16.
Indeed (11/16,1/5) yields the joint J1 and J2 midpoints (11/16,1/4); (11/16,5/16) yields J1 and J3 midpoints (11/16,15/64); (7/11,5/16) yields J2 and J3 midpoints (1/4,15/64). This proves all six proper-subset equalities (3) exactly over real Q.

## Strict source-to-observer transfer

Let D_full be the frozen maximum of six source-row four-stop TV distances. Each Ki is a deterministic Markov kernel on its named row, and TV contracts under such kernels, so for every lawful theta,z:
d_{123}(J(theta),J(z)) <= D_full(P(theta),P(z)).
The same inequality holds against a COMMON convex combination of complete source strategies. The source theorem at the pinned commit has R_full^L=r and R_full^H=3/16. Our (2) therefore proves that these three tagged Bernoulli readouts exactly preserve BOTH full-source optimum radii in that restricted S23 box.

The earlier K=17 auxiliary T/B Chernoff experiment has distinct two-hypothesis distributions and per-sample costs. This exact observer bridge is a TV/Chebyshev bridge within the restricted lawful source model. Transport to the original unrestricted ten-decoder R_beh(k,10) objective (previous bracket [1/2,2/3] for k=4,6) requires lawful decoder/source composition and an exact map between the relevant risk objectives.

## Verification and typing

VERIFY.py implements Q(sqrt43) order exactly with Fraction and squared-integer comparisons, checks the four-stop event identities at all 8 source vertices, common convex strategy weights, lawful radical witness, and six proper subsets. RUN_EVIDENCE.txt is the actual stdout from a local Python 3 standard-library run. The analytic argument above supplies complete-continuum coverage. BRC interface: REUSE_APPLIED (positive source provenance, deterministic observer push-forward, and nonnegative TV). No native six-axis physical-model claim or independent mathematical review is made.