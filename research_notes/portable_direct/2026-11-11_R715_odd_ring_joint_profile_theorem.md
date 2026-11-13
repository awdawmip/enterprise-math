# R715 — Exact four-boundary residual fibers and joint optimal schedules on odd BRC rings

Date: 2026-11-11, Asia/Shanghai.
Parent Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS, publication TP2-8B7E13C5904A2D6F1142, parent PO-X6-UPPER-STRUCTURE-20260906.
Frozen scientific source (unchanged): awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389.
Predecessors: R711/R711b @8fe4c9ce43183e9394d1e4047585ba51c336c483, R712 @e74bb4deb28b07bbfb12c147a282a336d72dd4e5, R713 @70ba12fd8d11b71209cfbc4e8d8506d299554f0d.
Mode: author-side exact mathematical derivation in the declared R709b–R713 candidate five-stage X6 event model. Independent review pending.

## Defined input, BRC carrier and observer
An odd labelled ring has m>=5 physical Cell edges, phases 1,...,5, and two individually source-labelled positive TRANSFER events of opposite types on each physical edge. Every Cell joins at most one elementary event per phase. On edge i choose p_i<q_i, the stages used by its two events, with adjacent cyclic edge stage sets disjoint. The two event types may be ordered either way independently on every edge. The old triadic state gate is frozen over five phases and committed at their end.

For phase boundaries t=1,...,4, define D_t=# {i:p_i<=t<q_i}, with area A=sum D_t=sum_i(q_i-p_i) and peak H=max D_t. The positive BRC event population retains its provenance; unsigned residual D and derived signed physical currents are typed observer readouts. R712 proved min A=m+3 and min H=ceil((m+3)/4). R713 counted area-optimal histories.

## Theorem A: profile-resolved exact counting formula
For odd m>=5, let N_m(D1,D2,D3,D4) be the number of rooted (fixed labelled edge zero) cyclic phase-pair histories with A=m+3 and the given entire four-boundary residual vector. Put k=(m-5)/2. The count is zero unless there are unique integers r,s,t>=0, r+s+t=k, such that

(D1,D2,D3,D4)=(2+r+s, 2+t, 2+s, 2+r+t).

For such a triple:

N_m(D)=8m * binom(r+s,s) * binom(r+t,t).

Consequently, for every area-optimal word:
D1+D2=D3+D4=(m+3)/2 and D1-D3=D4-D2=r>=0.

### Proof of Theorem A
Represent every stage pair (p,q) by a vertex of the Petersen graph K(5,2), with adjacency when the stage sets are disjoint. An admissible rooted phase-pair word is exactly a closed walk of length m. Define vertex excess w(p,q)=q-p-1>=0. The total excess is A-m=3.

Let x1,...,x4 mark the four boundary currents, and let M(y,x) be the 10-by-10 weighted adjacency matrix with
M_(u,v) = 1_{u adjacent v} y^(q(v)-p(v)-1) product_{j=p(v)}^{q(v)-1} x_j.
Write F(z,y,x)=det(I-z M(y,x)). The trace-determinant identity in the formal power-series ring gives:
sum_{m>=1} tr(M(y,x)^m) z^m = -z (d/dz) log F(z,y,x).

The zero-weight vertices are the four consecutive pairs 34,12,45,23, whose induced subgraph is the path 34--12--45--23. Define a=x1*x3, b=x1*x4, c=x2*x4. The y^0 determinant is
d0(z,x)=1-z^2(a+b+c)+z^4*a*c=(1-z^2*a)(1-z^2*c)-z^2*b.

An odd determinant term of total excess <=3 must contain an odd simple graph cycle. There are no Petersen 7-cycles. Any 9-cycle contains at least five positive-weight vertices because only four vertices have zero weight; hence its excess is >=5. The twelve undirected 5-cycles include exactly four with excess 3 and none with smaller excess. All four have boundary profile (2,2,2,2). Their unused zero-weight vertices do not include a disjoint adjacent pair, so no additional zero-weight transposition can accompany them. Thus the entire odd-z part of the y^3 determinant coefficient is
[y^3]F |_{z odd} = -8*z^5*(x1*x2*x3*x4)^2.
The factor -8 comes from the four undirected cycles in two orientations. Lower excess coefficients are even in z, so the corresponding odd-z part of [y^3]log F is the preceding term divided by d0.

We obtain the complete multivariate generating function:

sum_{odd m>=5} sum_D N_m(D) z^m product_j(x_j^D_j)
= 8*(x1*x2*x3*x4)^2 * z (d/dz) [ z^5 / (1-z^2*(a+b+c)+z^4*a*c) ].

Since the denominator equals (1-z^2*a)(1-z^2*c)-z^2*b, expand its reciprocal exactly as
sum_{r,s,t>=0} binom(r+s,s) binom(r+t,t) z^{2(r+s+t)} a^s b^r c^t.
The additional x-exponents are (r+s,t,s,r+t). Differentiating multiplies the coefficient of z^m by m. This is the desired formula for all odd m>=5.

Four explicit undirected minimum-excess Petersen 5-cycles (two-character phase labels):
12-34-15-23-45; 12-34-25-13-45; 12-35-14-23-45; 12-35-24-13-45.
The attached checker exhaustively confirms the graph claims, with independent full closed-walk DP for small sizes.

## Theorem B: simultaneous minimum area and minimum peak
Let V_m count the rooted phase-pair histories reaching both A=m+3 and H=ceil((m+3)/4). Then for every odd m>=5:

V_m = 8m                        if m mod 4 = 1,
V_m = 8m*(2+((m-3)/4)^2)       if m mod 4 = 3.

Proof. If m=4n+1, the area is 4(n+1), so the optimal peak forces all four D_j=n+1. This is only r=0,s=t=n-1, giving 8m. If m=4n+3, the invariant D1+D2=D3+D4=2n+3 and peak n+2 force each pair to be a permutation of (n+2,n+1). Exactly three of four pairings satisfy r=D1-D3>=0; their coefficients are 8m, 8m*n^2 and 8m. Every such coefficient is positive and achieves both sharp bounds. QED.

The exact number of fully typed histories is 2^m*V_m because every edge chooses independently which positive event type is performed first. The minimum fixed-length reversible memory from their common completed event-count ledger is
B_m=m+ceil(log2 V_m).
Along m=4n+1 it is m+log2(m)+O(1); along m=4n+3 it is m+3log2(m)+O(1). This counts raw histories, not future V39-equivalence classes.

## Examples and evidence
m | Area-optimal U_m | Joint-optimal V_m
5 | 40 | 40
7 | 168 | 168
9 | 576 | 72
11 | 1848 | 528
13 | 5720 | 104
15 | 17280 | 1320
17 | 51272 | 136
19 | 150024 | 2736
21 | 434112 | 168

In particular the joint-optimal histories collapse from an exponential area-optimal population to two polynomial subfamilies of degrees 1 and 3 in m.

Run the attached Python standard-library exact checker and redirect stdout to the companion JSON. It checks all 5-,7-,9-vertex simple Petersen cycles; independent rooted closed-walk DP with full residual profile for m=5,7,...,17; and all 49 odd sizes m=5,...,101 against the R713 recurrence and this theorem. Return flag: R714_ODD_RING_JOINT_OPTIMAL_PROFILE_PASS. Filename/flag R714 originated as local experiment before the distinct R714 PR #2067 was found; this theorem is designated R715.

BRC resolution: COMPOSE_APPLIED. The N_m(D) formula certifies the exact fiber for the declared area-optimal phase-pair observer. P000 V5, signed X6 native Cell identity, the six-axis and triadic constraints are preserved. The candidate event scheduler still requires direct native Link/Port time-admission comparison.

Next unresolved scientific unit: refine the profile fibers by S3 holonomy for the two source-labelled BRC loop generators, under a documented future V39 (j,h) observer and frozen Link/Port/triadic update semantics. Prove a scoped safe quotient only after testing that future observation. Formal CLAIM, native Result, and independent mathematical review are separate from this author-side publication.
