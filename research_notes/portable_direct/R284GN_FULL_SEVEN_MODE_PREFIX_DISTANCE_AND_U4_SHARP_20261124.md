# R284GN — Exact full seven-mode attempted-prefix distances and sharp capacity for u=4

2026-11-24. Informed portable continuation of the auxiliary four-phase binary fixed-tag model. Author analytic derivation and exact finite computation, NOT_REVIEWED. P000 and ACTIVE worldview unchanged; no native X6 or BRC physical interpretation asserted. Own original registration r1-20261124-0256-r284gd-session-v1 read back SUCCEEDED, Researcher EM-DIRECT-0C386E, Activity RA-B82240E8488EF5A1DA5186C4. Owner inventory r1-20261124-1100-owner SUCCEEDED, snapshot INV-be0143ca3e446484b45bbef80113febb at 2026-11-24T03:03:57.275958Z, source 01e1ae8e6118e439b0da0481c692ff1fdb55ac21, no LEASED tasks returned. Snapshot not live write authority. No shared CLAIM.

Frozen scientific inputs:
- R284GM @a06ff527a1494a6a61b6964f9a753bcb35ab7433:research_notes/portable_direct/R284GM_GLOBAL_LOW_OMISSION_SHARP_CAPACITY_AND_RIGIDITY_20261124.md (global low-omission theorem, GE group and opposite cut table).
- R284GL @5f74ba8a545788cc3fdb080f9953bbe5a0926531:research_notes/portable_direct/R284GL_ASYMMETRIC_THREE_PATTERN_SHARP_CAPACITY_20261124.md (three-mode exact distances and capacity).
- R284GE @a112519ea319ef0e0bdf10ee01d817e10fd3dcd5:research_notes/portable_direct/R284GE_EXACT_ADJACENT_ROLLBACK_CAPACITY_20261124.md (source-incidence cut theorem, GE1 and full-cycle criterion).
- R284GK @9c56aa402a9f36352c11ea721fe5b1bba580fdf1:research_notes/portable_direct/R284GK_LOW_OMISSION_THREE_PATTERN_CONSTRUCTION_20261124.md (global upper bound).
- R284GJ @5df644efe9d0fc36c0b317688c284543c8e0c585:research_notes/portable_direct/R284GJ_SHARP_BOUNDARY_Q4U_MINUS3_20261124.md (high-omission theorem).

## GN1. Exact formulas on the complete seven-pattern carrier

For each p=1,...,7, normalize phase 0 bit to 0 and take phase i bit (p>>(i-1))&1 for i=1,2,3. Let x_p>=0 be its integer multiplicity. Edge 0->1 attempts a_p coordinates in types p=1,3,5,7 (0<=a_p<=x_p). At most q>=0 integer current attempts may be omitted, with independent historical last-change group budgets of q as in GE/FM. Let [z]+ = max(0,z). D_j is the minimum physical Hamming distance to the stable set of phase j over all allowed source histories and current omissions, j=2,3. These two distances are separately minimized; their witnesses need not be the same physical word.

Put U=x3-a3, V=x7-a7, W=[a1+a5-q]+. Then

    D2 = max(0,
             [U-q]+ + [V-q]+ - q,
             W + [x2-q]+ + [x6-q]+ - q,
             W + [U+x2-q]+ + [V+x6-q]+ - 2q).             (GN2)

For the other phase put

    s=[a1+a3-q]+, l=max(0,s-a3), h=min(s,a1),
    p0=x7-a7, p1=x6, p2=x4+x5-a5,
    M(t1,t2)=max(0,s-t1-t2,l-t1,s-h-t2).

Then

    D3 = max(M(q,q), [p0-q]+ + M(q-p1,q-p2) - q).        (GN3)

All variables are integers in the specified domain; t1,t2 can be negative. Both formulas hold for all x, a, q, including zero and small multiplicities, with no symmetry or heavy-mode assumptions. A cyclic shift followed by XOR normalization relabels the patterns and applies the same formulas to every edge. Combined with GE1 and the two GM opposite cuts, safety of a histogram is exactly existence of a monotone path on each edge keeping D2,D3>=2u+1. Each evaluation uses a constant number of integer operations, independent of q and width (arithmetic bit complexity still depends on operand size). This replaces per-prefix enumeration of omission allocations and eight-vertex cuts, not the monotone path search itself.

### Proof of GN2

In a distance minimization to phase 2, a successful write of types 3,7 removes a differing bit, so all their attempts may be taken successful. A successful write of types 1,5 adds a differing bit; these share comparison budget T1. It is optimal to minimize their combined successes to W, attainable by using as many current omissions as useful on these two types. Monotonicity follows directly from the contained-demand cut expression. In the residual incidence graph the paired demands are S2--T0: U; S3--T0: V; S2--T1: x2; S3--T1: x6. The extra W demand is incident only to T1. Every budget vertex has capacity q; the minimum unassigned demand equals maximum contained-demand minus q times selected vertex count (GE/FM). For fixed selected comparison vertices J, maximizing over source vertices can be done independently: choose each S precisely when its total demand to J exceeds q (ties harmless). The four choices J=empty,{T0},{T1},{T0,T1} give exactly GN2.

### Proof of GN3

For phase 3, it is optimal to make all attempts of types 5,7 successful (they remove mismatches); minimize combined successes of the other types 1,3 to s. Every integer allocation z=s1 in [l,h], s3=s-z, is attainable using at most q current omissions. For fixed z the paired demands are all incident to S3: p0 to T0, p1 to T1, p2 to T2; the single-endpoint demands at T1,T2 are z,s-z. Set b0=0,b1=z,b2=s-z. The exact residual distance for this star is

    max(sum_i [b_i-q]+, sum_i [b_i+p_i-q]+ - q).

Indeed if S3 is excluded from the cut, each T is selected independently only for positive b_i-q; if included, independently for positive b_i+p_i-q and subtract q once for S3. This exhausts all relevant cuts.

For real thresholds t1,t2, the sum f(z)=[z-t1]+ + [s-z-t2]+ has minimum on [l,h] equal to M(t1,t2): its unconstrained minimizing interval is between t1 and s-t2, and projection onto [l,h] gives the formula, also immediate by expanding f=max(0,s-t1-t2,z-t1,s-z-t2). Here thresholds are integer, so projected minimizing points can be integer. The two functions in the star maximum have threshold pairs (q,q) and (q-p1,q-p2), respectively, up to constants. Their unconstrained minimizing intervals intersect: if s<=2q the first interval is [s-q,q], while the second has one endpoint <=q and the other >=s-q; if s>=2q the second contains [q,s-q]. Projection onto [l,h] preserves a common minimizer. Consequently the minimum over the feasible integer allocation of the maximum equals the maximum of the two separate minima. Substituting gives GN3. This common-minimizer property is the new elimination of the current omission allocation. It depends on the source incidence, not just the total residual.

## GN4. Reduction of possible sub-conjecture histograms

Write F=min(4q+8u+2,max(5q+5u+2,6q+4u+2)), u>=1. From GM's lower-bound proof, every qualifying opposite row/column cut gives n>=5q+6u+2>=F (compare separately q<=u, u<=q<=2u, q>=2u). Thus a sub-F histogram can use only single-cell or whole-matrix opposite cuts. If both whole matrices qualify, GM's small-count cases A<q or C<q yield n>=6q+6u+2>=F, and B<q yields n>=4q+8u+2+B>=F. Hence such a histogram has A,B,C>=q and the singleton cost bound of GM. In particular for u<q<2u and n<=F-1, S+sum_{p in {1,2,4,7}}min(q,x_p)<=4(q-u)-2. For 2u<=q, n<=F-1 gives S+sum min<=12u-4q-2, so this both-full-cut case is impossible already for q>=3u. This leaves a single-cell-cut family to treat in that region. This reduction does not assume every singleton is removable.

## GN5. Exact finite capacity for u=4, all q>=0

The companion exact integer JS program at 421722208d733b7c1a639ef44eefd2cb818b16d7:research_notes/portable_direct/R284GN_full_seven_mode_prefix_checker.js is byte-identical to the executed local file (Git blob a0510cdebc5d70b77f8f1fcb34b79c599e4d3628, SHA256 de3ddd59c5cd9125a4ae4cdf30d6de7dc84648a52a7a78ea3ecf11e5488ab29c).

Regression: node checker.js regression enumerated all x1..x7 in 0..2, every attempted prefix, q=0..3, all current omission allocations. Independently regenerated eight-vertex cuts from bit and last nominal change incidence. Actual output: prefixes=139968, comparisons=279936, allocations=554040, cutCounts=[11,11], zero failures. GN2/GN3 are analytically proved, this calculation checks their implementation.

Finite scan: node checker.js 5 12 4 (the initial combined run reached q=9 before a local execution timeout; q=10,11,12 were each run to completion separately). At each q test width n=F(q,4)-1. Constant columns can be deleted; any smaller safe code can be enlarged to n by adding nonconstant columns with decoder ignoring them, preserving the original projected trajectory and omission budget. Thus excluding all histograms at n excludes every smaller width. Enumerate all seven-mode compositions using exact adjacent GE pruning: with r unassigned coordinates, the sum of group overflows is convex in allocations of r across the groups, so its maximum is at a simplex vertex (all r to one eligible group, or none if no eligible group); current allocated counts are kept, future counts zero. This is a valid upper bound for each GE test; prune only when that bound fails. At leaves require exact GE, both opposite cuts, then exact memoized monotone paths on all four rotated edges using GN2/GN3. A node is safe iff both distances >=2u+1; adjacent rollback is already settled by GE1. All arithmetic is exact integer within JS safe-integer bounds here.

Actual results:
q | tested width | GE survivors | stable survivors | visited path nodes | first failed edge 0,1,2,3 | all-cycle survivors
5 | 47 | 362529 | 19 | 810 | 10,9,0,0 | 0
6 | 53 | 947258 | 252 | 16877 | 134,118,0,0 | 0
7 | 59 | 2166773 | 1484 | 152208 | 783,701,0,0 | 0
8 | 65 | 4482088 | 5776 | 872571 | 3039,2737,0,0 | 0
9 | 69 | 6027019 | 5420 | 837755 | 2774,2646,0,0 | 0
10 | 73 | 8027689 | 5308 | 835622 | 2668,2640,0,0 | 0
11 | 77 | 10588776 | 5283 | 839919 | 2643,2640,0,0 | 0
12 | 81 | 13831479 | 5280 | 845130 | 2640,2640,0,0 | 0

Totals 46433611 exact GE survivors, 28822 stable survivors, 4400892 memoized path visits, 456648138 pruned subtrees. All eight widths excluded. The lower q<=4 is covered by GM; q>=13 covered by GJ; GK supplies upper constructions. Therefore n_min(q,4)=F(q,4) for every integer q>=0, within the stated frozen model and dependencies. No extrapolation to u>=5.

## Next

Use GN2/GN3 as the exact full-carrier residual coordinates to derive symbolic prefix barriers, rather than iterating general omission allocations. In particular study single-cell-cut families above q=3u and both-full-cut families for u<q<3u, including the quantified singleton cost from GN4. Seek an analytic separator at crossing steps in four attempted coordinates. The general F lower bound for remaining u>=5 ranges is open; do not repeat completed u<=4 scans. All results author-checked, independent Review pending.
