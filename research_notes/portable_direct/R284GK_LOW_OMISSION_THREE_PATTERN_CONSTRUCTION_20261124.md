# R284GK — Low-omission three-pattern construction and exact transition

Date 2026-11-24. Informed portable research on the frozen auxiliary four-phase binary fixed-tag model. Author proof, NOT_REVIEWED; no shared CLAIM. P000 and ACTIVE worldview unchanged. Source provenance: R284GJ 5df644efe9d0fc36c0b317688c284543c8e0c585; R284GE a112519ea319ef0e0bdf10ee01d817e10fd3dcd5; R284GF 85801535d3b34cca713f28703b4984baf80975f3; R284FM 1d1c5dd412719c7aaf016187b6493b77253cd9f9. All paths as in GE/GJ. The actual prior session recovered read-only as MCP-8cd6c4fa26b9459d923ff73ba0082220, EM-DIRECT-0C386E, RA-B82240E8488EF5A1DA5186C4. No shared authority asserted.

## Result
The repeated Gray upper bound 4q+8u+2 is not universally sharp. For integer u>=1, 0<=q<=2u-1, a symmetric three-pattern histogram (x1,...,x7)=(0,0,A,0,B,A,0) with A=2q+u+1 and B=max(q+3u,2q+2u) admits a safe fixed-order four-phase protocol. Width
N= max(5q+5u+2,6q+4u+2)
is strictly smaller than Gray in this region. This is an infinite constructive family, not an extrapolation of finite enumeration. For q<=u, the improvement is 3u-q; for u<=q<=2u-1, it is 4u-2q. In fact this N is optimal within the symmetric three-pattern class in the stated region. For q>=2u this class cannot improve Gray (not a global lower bound).

## Exact two-threshold proof
Use normalized bit patterns p=3:(0,1,1,0), 5:(0,1,0,1), 6:(0,0,1,1), retaining individual last-changing-edge capacity q. Let A=2q+d, d>=0, and B>=0. Adjacent stable/no-rollback condition from GE is (A-q)_+ + (B-q)_+ >= q+4u+1 on every edge. Opposite pair distance is 2d, since the two differing types have distinct source and comparison vertices; stable separation requires d>=u+1. (If A<2q the opposite distance is zero, so this excludes that case.) Rotation permutes 3 and 6 and preserves 5, with phase-0 XOR normalization; thus one edge suffices in the symmetric class.

Consider edge 0->1, attempted counts a on type 3 and b on type 5, successful counts s,t. Type 6 is unchanged. To compare with phase 2, the remaining A-s mismatches of type 3 have their own two last-change endpoints (each capacity q). The C=A type-6 mismatches have source endpoint 3 and comparison endpoint 1. The t successful type-5 writes differ from phase 2 and have only comparison endpoint 1, shared with type 6. Because A>=2q, exact residual distance is (A-s-2q)_+ + A+t-2q. To compare with phase 3, the B-t unwritten type-5 mismatches have endpoints S3,T2, A unchanged type-6 mismatches have endpoints S3,T1, and s successful type-3 mismatches have endpoint T2 only. The maximum contained-demand cut is max(A-2q,B-t+A+s-3q): all other cuts are dominated, since A>=2q and B-t>=0. Thus the minimum over current omission vectors of each third-phase distance is exactly
 D2(a,b)=d+(d-a)_++(b-q)_+,
 D3(a,b)=max(d,B-b+d+(a-q)_+-q).
For D2 omit only type 5 up to q, for D3 omit only type 3 up to q. These are realizable, not merely cut bounds. This keeps the joint source incidence rather than replacing two groups by total residual.

For u+1<=d<=2u put L=2u+1-d>=1. At each integer a, safe b values form [lower(a),upper(a)] intersect [0,B], with
 lower(a)=0 if (d-a)_+>=L, otherwise q+L-(d-a)_+;
 upper(a)=min(B,B-q-L+(a-q)_+).
The endpoints are safe exactly when d>=L and B>=q+L. Both bounds nondecreasing. There is a monotone unit-step path iff lower(a+1)<=upper(a) for every 0<=a<A: necessity follows from the edge advancing a; sufficiency follows by moving b to max(current b,lower(a+1)) before advancing a, and finishing b at a=A. The maximum of lower(a+1)-(a-q)_+ on the positive-lower segment occurs at a=d-1 (possibly tied): before d-1 the expression is nondecreasing, afterwards nonincreasing. It equals q+L-max(0,d-1-q). Consequently the exact path condition is B>=2q+2L-max(0,d-1-q), plus the endpoint conditions. For d>=2u+1, both third-phase distances exceed 2u at every prefix, so only adjacent GE remains. With GE and opposite separation, the GE full-cycle sufficiency theorem gives a stateless minimal forced decoder, stable correctness, no rollback, no third-phase recognition, with these fixed orders on all four edges.

In the claimed construction d=u+1, L=u, B=max(q+3u,2q+2u). This meets GE (B>=q), the endpoint conditions and the exact path inequality. No solver is needed for arbitrary q,u.

Symmetric-class optimality: for u+1<=d<=2u, GE forces B>=q (B<q would force d>=4u+1). Therefore n=4q+2d+B >= max(5q+4u+1+d,6q+4u+2-max(0,d-1-q)). First term >=5q+5u+2. If d<=q+1, second term is 6q+4u+2; if d>q+1, first term >=6q+4u+3. Hence n>=N. For d>=2u+1 and B>=q, GE gives n>=5q+4u+1+d>=5q+6u+2, which is >=N when q<=2u-1 and >=Gray when q>=2u. If B<q, GE forces d>=4u+1, hence n>=4q+8u+2. For q>=2u the preceding low-d lower bound 6q+4u+2 is >=Gray. The optimality assertion is limited to x3=x6 and support {3,5,6}.

## Exact finite global scan (all seven patterns)
Adapted GJ's finite histogram and prefix checker to arbitrary q,u and n<=4q+8u+1. Prune partial nonnegative histogram assignments with remaining budget r: for each GE edge, let current group masses z_e; maximum attainable overflow <= sum_e(z_e-q)_+ + max over groups containing an unassigned type of [(z_e+r-q)_+-(z_e-q)_+], including zero. Proof: convexity of the positive part; all allocations of <=r form a simplex whose maximum convex value is attained at a vertex. Pruning is sound even when maxima on different edges cannot be jointly attained. Every retained full histogram passes all four GE constraints, six stable cuts, and complete memoized prefix path tests with all omissions <=q on each edge. Constants may be removed because fixed constant columns provide no separating distance for physical stable/prefix sets; necessity/sufficiency uses GE. Actual runs (q,u,limit | GE pass | stable pass | nonheavy | full survivors | minimum survivor length):
5,2,37 | 656212 | 315 | 3 | 0 | none (GJ regression)
4,2,33 | 349062 | 343 | 28 | 0 | none
3,2,29 | 178750 | 487 | 128 | 66 | 28
2,2,25 | 89086 | 1015 | 417 | 743 | 22
1,2,21 | 45098 | 3421 | 1914 | 3421 | 17
0,2,17 | 27323 | 13555 | 8535 | 13555 | 12
8,3,57 | 9361989 | 2247 | 3 | 0 | none
7,3,53 | 6078699 | 2275 | 31 | 0 | none
The Gray construction supplies the matching upper bound when there are zero survivors. Thus n_min(q,2)=12,17,22,28,34 for q=0,1,2,3,4 respectively, and 4q+18 for q>=5 by GJ. Also n_min(7,3)=54 and n_min(8,3)=58. For (q,u)=(3,2) the two minimum histograms are (0,0,9,0,10,9,0) and (0,0,10,0,8,10,0). An explicit successful attempted order for the first on edge 0 is 3555535333333355555 (digits are pattern indices); edge 1 is 5555566665656565656; edges 2 and 3 repeat edge 0 and 1. Prefix paths verified with exact cuts and all current omissions. Additional independent Python verification of the two closed distance formulas performed 8588 exact cut minimum comparisons (q<=2,u<=2), and interval path formula tested on q=0..3,u=1..4,d=u+1..2u,B=2q..2q+4u+2. C++ executable actual results above; source companion follows. No independent mathematical Review claimed.

## Next
The global capacity may undergo its transition near q=2u, not 4u. The two-heavy obstruction alone cannot settle it. Establish global lower bounds matching the three-pattern upper construction for q<2u, and test q=2u..4u-4, especially u>=3. For low q and u>=3 the symmetric result is a construction, not a global minimum assertion. Keep exact source-group residuals, not a native geometric/BRC computation.

## Additional completed u=3 scan in the same run
Same exact C++ checker, immutable code commit 501e7fce66cecd84af712be7dc79cf249c265590, git blob 03cf7b6a2924223b43bc0486cac494a811618228 equals locally executed code. Compile with g++ -O3 -std=c++17, run executable q u. Each output survivor is a seven-integer histogram; stderr gives the complete pruning and search counts. The code uses int counts/keys, safe at all tested parameter sizes (not asserted overflow-safe for unlimited inputs).
q,u,limit | GE pass | stable pass | nonheavy | full survivors | min survivor length:
6,3,49 | 3864457 | 2415 | 168 | 0 | none
5,3,45 | 2408134 | 2919 | 624 | 90 | 44
4,3,41 | 1475091 | 4372 | 1794 | 1747 | 38
3,3,37 | 893835 | 8076 | 4489 | 6464 | 32
2,3,33 | 545153 | 18973 | 12437 | 18955 | 27
1,3,29 | 350977 | 56893 | 41971 | 56893 | 22
0,3,25 | 264340 | 146098 | 108266 | 146098 | 17
Hence the full u=3 row is n_min=17,22,27,32,38,44,50,54,58 at q=0..8 respectively; q>=9 follows GJ. For u=2 and u=3, finite global exact results and earlier high-q theorem together match min(4q+8u+2,max(5q+5u+2,6q+4u+2)) for every nonnegative integer q. This piecewise formula is now a concrete global conjecture for arbitrary u, rather than Gray universal optimality. The proved constructive upper bound applies to every integer u>=1 and q>=0 by selecting the better of the two available constructions. Next pursue matching global lower bound; for q<2u, consider deriving it from GE and opposite cuts plus the two competing thresholds, retaining non-symmetric and mixed pattern cases.
