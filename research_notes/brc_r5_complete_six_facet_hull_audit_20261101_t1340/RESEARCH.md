# R5 — Complete six-facet FULL/LR hull audit for a coupled time–likelihood-ratio stopping model

Date: 2026-11-01 (Asia/Shanghai).
Classification: AUTHOR_PROVED / EXACT_FRACTION_CHECKED / UNREVIEWED / NOT_ADMITTED / PORTABLE_ONLY / REGISTER_PENDING.
The original four-observer mother question remains open.

## Frozen provenance and boundaries

GLOBAL_KNOWLEDGE_V1: canonical main@390e9c2d78163e7c7453131d145e817224828693, with 00_BOOTSTRAP.md, OPERATING_MANUAL.md and triggered math/BRC/code/research and ACTIVE worldview routes. Enterprise Math: main@738596c45bf5942e05bf68f7f5a5452343185b31, including AGENTS.md, P000, ACTIVE Heartbeat World, the mandatory joint-relation observer contract, current control authority, autonomous and portable research protocols. Scientific predecessor: immutable d772eca66778503f0ca8248dca831a59a9f39d80, research_notes/brc_r5_two_coupled_keys_perfect_recall_20261101_t1242, draft PR #1663.

BRC carrier: 13 separately source-labelled terminal events with strictly positive exogenous P and Q nature likelihoods. The four terminal statistics eP=P(answer Q), eQ=Q(answer P), TP=E_P[T], TQ=E_Q[T] are calculated only after retaining the labelled paths. Signed separating functionals are post-observer linear forms, never negative probabilities. This is an auxiliary finite decision model and no four-observer chart coordinate is a native X6 spatial axis. The P000 premise, native six-dimensional spatial world and protected worldview were not modified.

Hidden sources A1,A2,B,C have P masses (1/8,1/8,1/4,1/2) and Q masses (1/8,1/8,1/8,5/8). At I=(time1,LR1), A1/A2 choose STOP Q at time1 or CONTINUE. The latter has independent low-edge probabilities (P,Q)=(1/2,1/4) for A1, (3/4,3/8) for A2, with high answering P at time2; low edges meet bypass B at J=(time2,LR2). STOP at J answers Q at time2. A1 continuing from J splits X/Y with (P(X),Q(X))=(3/5,1/2): X answers P and Y Q at time3; A2 and B continuing from J answer Q at time3. C has independent time1 LR4/5 key: STOP answers P at time1, CONTINUE answers Q at time3. Each terminal answer is a single function of terminal (time, exogenous P/Q likelihood ratio). FULL uses independent (p1,p2,q1,q2,qB,r); LR uses (p,q,r) with p1=p2=p and q1=q2=qB=q. Same behavioral randomization applies under both laws. Each decision key is visited at most once per path.

## Theorem A — exact H-description of LR convex hull

The predecessor observation polynomial is exactly, for all real p,q,r in [0,1],

O_LR=O0+p B+q C+(pq)D+r E

with
O0=(139/160,3/16,93/32,181/64)
B=(21/160,-3/16,-13/32,-21/64)
C=(3/80,-1/64,-13/32,-13/64)
D=(-3/80,1/64,5/32,5/64)
E=(-1/2,5/8,-1,-5/4).

For A=[B C D E], det(A)=233/163840 and

A^{-1}=(1/233)*
[[-480,-1152,320,-640],
 [-5140,-3016,-2010,2156],
 [-14100,-9608,-2250,2636],
 [80,192,102,-204]].

For an arbitrary real O write (u,v,s,w)=A^{-1}(O-O0); this is an *affine diagnostic coordinate*, not necessarily a physically available policy. Then O lies in the entire LR four-observer convex hull IF AND ONLY IF all SIX inequalities hold:

F0=s>=0,
F1=1-u-v+s>=0,
F2=u-s>=0,
F3=v-s>=0,
F4=w>=0,
F5=1-w>=0.

Proof: (p,q,pq) is in the tetrahedron with corners (0,0,0),(1,0,0),(0,1,0),(1,1,1). A point (u,v,s) lies in that tetrahedron precisely when its four barycentric weights (1-u-v+s,u-s,v-s,s) are nonnegative. They sum to 1 and are its unique corner weights. The independent w=r interval contributes weights (1-w,w) to each of the four corners. Thus the six inequalities give explicit nonnegative weights for all eight LR deterministic observations and reconstruct O exactly. Conversely each actual (p,q,pq,r) yields such a corner mixture, and linearity preserves the inequalities. A is invertible, so this is an exact equivalence in observed 4-space. The hull is a full-dimensional tetrahedral prism with six irredundant facets. This is the classical unit-square McCormick convex envelope, used here in a labelled dual-law model. For an included O, eight rational LR corner weights are immediately available; Carathéodory ensures a representation with at most five of them when needed. This is convex-hull membership, not actual behavioral image membership. QED.

Prior art: G. P. McCormick, 'Computability of global solutions to factorable nonconvex programs: Part I — Convex underestimating problems', Mathematical Programming 10 (1976), 147–175, DOI 10.1007/BF01580665. No claim of novelty for the general bilinear envelope.

## Theorem B — exact all-signed six-facet FULL separation

The FULL observation is multi-affine in its six independent real behavioral parameters. Therefore the minimum of each linear Fi over *every real* FULL policy occurs at a deterministic vertex. The standalone checker rebuilds all 13 labelled P/Q terminal flows and exhaustively calculates 64 such corners. The exact results:

Facet | min_FULL Fi | Number of violating FULL corners | extremal policy (p1,p2,q1,q2,qB,r) | L-infinity distance lower bound
F0=s | -2793/1864 | 22 | (1,0,0,0,0,0) | 2793/228752
F1=1-u-v+s | -90/233 | 16 | (1,0,0,0,0,0) | 3/520
F2=u-s | -3737/1864 | 18 | (0,1,0,0,1,0) | 3737/223376
F3=v-s | -205/233 | 8 | (0,1,0,0,0,0) | 205/16272
F4=w | -1/932 | 8 | (1,0,0,0,0,0) | 1/2312
F5=1-w | -1/932 | 8 | (0,1,0,0,0,1) | 1/2312.

Every LR point obeys Fi>=0, and min_LR Fi=0 because Fi is a facet. For each FULL minimizing point with Fi=-g<0, this produces a strict separator and exact signed support gap g. To express Fi(O)=alpha_i+n_i·(O-O0), the six observer-space dual normals, with common denominator 233, are:

n0=(-14100,-9608,-2250,2636)/233
n1=(-8480,-5440,-560,1120)/233
n2=(13620,8456,2570,-3276)/233
n3=(8960,6592,240,-480)/233
n4=(80,192,102,-204)/233
n5=(-80,-192,-102,204)/233.

Hölder gives dist_infty(O,conv(LR)) >= g/||n_i||_1, yielding the exact final column. In particular FULL policy (0,1,0,0,1,0) produces O=(9/10,7/64,39/16,81/32) and F2=-3737/1864, proving dist_infty>=3737/223376. This improves the *quantitative bound for a newly selected witness* over the previous model's one-direction 1/320 bound; the witness is different. No FULL/LR hull equality is possible at these fixed kernels. QED.

## Corollary — complete 64-vertex inclusion audit

All six exact inequalities hold for 22 of the 64 FULL deterministic observation vectors. For each of these 22, the checker gives an explicit eight-corner LR convex reconstruction with weights (1-u-v+s,v-s,u-s,s) assigned in (00,01,10,11) order and split over private r corners by (1-w,w). The remaining 42 FULL corner vectors violate at least one facet. The six violation counts overlap; they must not be summed to count excluded vertices. Hence conv(FULL) strictly contains conv(LR), and six simultaneous facet corrections are needed to have hull equality in a perturbed model retaining the invertible affine bilinear form.

The previous midpoint proof of nonconvex actual LR behavior still applies unchanged: the LR chart is injective and the midpoint of (p,q,r)=(0,0,0) and (1,1,0) requires (u,v,s,w)=(1/2,1/2,1/2,0), contradicting s=uv=1/4 in the real LR behavioral image. Neither this nonconvexity nor full affine rank supplies hull equality.

## Exact verification and authority

Run python3 VERIFY.py. Its arithmetic uses only Python standard-library Fraction; no floats. It checks 13 labelled terminal flows, P/Q normalization, terminal answer consistency at repeated (time,LR) keys, 125 rational LR parameter triples against the polynomial and invertible diagnostic chart, exact determinant and inverse, all eight LR corners and 64 FULL corners, six facet extrema/counts/norms, and 22 primal rational LR mixtures. EXACT_OUTPUT.txt contains the executed output. Analytic bilinear tetrahedron and multi-affine extremum arguments—not finite sampling—justify the universal real-parameter statements.

At this run the native gateway reported version 0.6.11, research_authority_granted=false, executor_binding_configured=false, and active subject quota 5/5; no current role-bound CLAIM or Result was obtained. Persistence of this portable artifact does not imply task admission, review, Foundation or native X6 theorem status. See NEXT_TASK.md for the smallest successor unit.
