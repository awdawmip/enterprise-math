# S23 N=4, K=17: certified full phase 3/4 <= s <= 4/5

2026-11-05; author analytic proof with executed strict rational certificates; INDEPENDENT REVIEW PENDING. Frozen scientific input: awdawmip/enterprise-math@43ec6098b1330ae86d0a7863be336c5d97f6ef34; predecessor result PR #1765 @9e1fb67c7f10b8d588e06d46426b90596167c478.

## Model and theorem

Let a=11/21,b=10/21. Full T observation distributions are (as,1-s,bs) and (bs,1-s,as); typed B projection distributions are (as,1-as) and (bs,1-bs). Write

f_T(t,s)=-log(1-s+s(a^t b^(1-t)+b^t a^(1-t))),
f_B(t,s)=-log((as)^t(bs)^(1-t)+(1-as)^t(1-bs)^(1-t)),
F(m,n;s)=max_{0<=t<=1}[m f_T(t,s)+n f_B(t,s)],
C_T=F(1,0;s), C_B=F(0,1;s), H=f_B(1/2,s).

The shared Chernoff t is optimized once for the entire mixed design, not independently for each observation. Counts m,n are nonnegative integers with cost (2-s)m+n<=17. B is explicitly a projection with different provenance and does not replace full T.

Define four cells, and their special feasible count pair:
(3/4,10/13;12,2); (10/13,7/9;13,1);
(7/9,11/14;9,6); (11/14,4/5;14,0).

For each cell [l,r) and associated (m,n), there is exactly one real s* in (l,l+1/1000) such that F(m,n;s*)=17 C_B(s*). The unique global feasible design is (m,n) on [l,s*), and (0,17) on (s*,r); at s*, exactly these two designs tie. At s=4/5, (10,5) is the unique global optimizer. Hence [3/4,4/5] is completely classified for this auxiliary two-observer model.

## Exact finite integer hull

For s in [3/4,4/5], m<=14. At each m, strictly positive B information forces the largest feasible n=17-2m+floor(ms), if n>=0. Every k/m threshold for m<=14 in [3/4,4/5] is exactly {3/4,10/13,7/9,11/14,4/5}. The entire upper convex hull is:
- [3/4,10/13): [(0,17),(12,2),(13,0)]
- [10/13,7/9): [(0,17),(13,1)]
- [7/9,11/14): [(0,17),(9,6),(13,1)]
- [11/14,4/5): [(0,17),(14,0)]
- {4/5}: [(0,17),(10,5),(14,0)].

VERIFY.py enumerates all m in 0..16 (only nonnegative n survive), every exact rational break, all left-boundary and interior hulls, and the final boundary hull. F is convex in (m,n) as a maximum of linear functions and monotone in both counts, so the maximum over the integer feasible set lies on an upper-hull vertex.

Eliminate the extra vertex (13,0) on the first cell using 17 C_B-13 C_T>0 throughout [3/4,10/13]. Eliminate the extra vertex (13,1) on the third cell by 16 C_B-13 C_T>0 throughout [7/9,11/14], since F(13,1)<=13 C_T+C_B. Both inequalities are proven from 16 exact strict rational value/slope certificates (four subcells each, one value and one slope per subcell). Only the two stated candidates remain on each open cell.

Strict uniqueness at a tie also applies to integer lattice points internal to the candidate edge. Indeed f_T has unique optimal tilt t=1/2, whereas B has an optimal t unequal to 1/2 for all p=as>q=bs>0, p+q=s<1. To see this directly, put d=p-q and phi(r)=log(r)/(sqrt(r)-1/sqrt(r)), r>1. As phi(exp(2u))=u/sinh(u) is strictly decreasing for u>0, p/q>(1-q)/(1-p) yields
Z_B'(1/2)=d[phi(p/q)-phi((1-q)/(1-p))]<0,
and f_B'(1/2)>0. Two nonproportional count vectors cannot share their optimizing tilt unless both component derivatives are zero, which is impossible. Therefore the convexity inequality for F along each candidate edge is strict at internal points. For all other nonvertices, the inferior third vertex (if present) also yields a strict convex-combination inequality. At points where only one vertex wins, uniqueness follows from the strict vertex comparison.

## Strict uniqueness and existence of each continuous crossing

For each fixed tilt t, f_T(t,s) is convex because -log is convex decreasing on a positive affine argument. The Bernoulli coefficient in f_B is the sum of an affine term and a weighted geometric mean of positive affine terms, so it is concave; -log composed with that concave coefficient is convex. Thus F(m,n;s), C_T and C_B are convex in s.

Put G(s)=F(m,n;s)-17 C_B(s). For rational subinterval [x,y] and delta=1/10000 define
L=[C_B(x)-C_B(x-delta)]/delta,
U=[m C_T(y+delta)+n C_B(y+delta)-m C_T(y)-n H(y)]/delta.

The exact shared-tilt bounds
m C_T+n H <= F(m,n) <= m C_T+n C_B
and convex secant inequalities imply for all real x<=u<v<=y
[G(v)-G(u)]/(v-u) <= U-17L.

Each cell is partitioned into 12 rational subintervals; all 48 exact rational checks show 17L-U>0. Thus each G is strictly decreasing over its entire real cell. At each left endpoint l, the exact lower bound m C_T(l)+n H(l)-17 C_B(l)>0 holds; at l+1/1000, the exact upper bound m C_T+n C_B-17 C_B<0 holds. Eight exact sign certificates plus continuity prove exactly one root in (l,l+1/1000) for each cell.

For b C_B-m C_T, each of four rational subintervals [x,y] verifies its positive value at x and the strictly positive slope lower bound
b[C_B(x)-C_B(x-delta)]/delta-m[C_T(y+delta)-C_T(y)]/delta>0.
This proves the surplus-vertex exclusion throughout the whole intervals, with b,m respectively (17,13) and (16,13).

At s=4/5 the exact rational lower bounds
10 C_T+5H-17 C_B>0 and (10 C_T+5H)-14 C_T>0
select (10,5) over the other two hull vertices.

## Exact certificates and scope

The actual executed VERIFY.py uses Fraction and isqrt, outward square-root enclosures at 10^-48, and a 34-term artanh logarithm series with explicit remainder bound 2|v|^(2N+1)/[(2N+1)(1-v^2)], v=(x-1)/(x+1), with |v|<1/3 asserted. Bernoulli C_B is evaluated using the optimal tilted mass rho=J/(H0+J), H0=log(a/b), J=log((1-bs)/(1-as)), C_B=D((rho,1-rho)||(as,1-as)). The code proves positivity by exact rational interval lower bounds, not printed truncated lower values.

Counts: 48 monotonicity checks + 8 crossing sign checks + 16 extra vertex exclusions + 2 right-boundary comparisons = 74 exact strict inequalities; also complete finite rational break/hull assertions. The matching complete executed output is RUN_EVIDENCE.txt. This is author-side mathematically scoped evidence; independent review, native CLAIM and Result admission remain separate. The ten-label S23 minimax mother question retains its previously recorded [1/2,2/3] bracket.