# R762KX — Sharp ten-event obstruction in cycle coordinates

2026-11-24. AUTHOR_ANALYTIC_PROOF_WITH_EXPLICIT_FINITE_CERTIFICATES / EXACT_PYTHON_CHECKED / NOT_REVIEWED. Independent portable continuation of R762KW, ffa2731618e7bb5cf3bd617b99a14440f5cc9322:research_notes/portable_direct/R762KW_CUBE_CYCLE_RESERVE_STRUCTURE.md (blob 41c768af75c636ab61b84e5416d969de9775598b), and R762KV, 88954b5da3cb001d937f873698a6894ac21d6a15:research_notes/portable_direct/R762KV_SHARP_SINGLETON_SUFFIX_RESERVE.md. Frozen P000 a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json (blob dc84bdae6595b5e237a2ad50d8b21916adb2e447) and joint-relation observer companion read. Original registration r3-20261124-0124-own-research-registration-v1 SUCCEEDED, EM-DIRECT-82A007 / RA-708BCC309CE076D8BB599B91; own metadata recovery r3-20261124-0920-own-recovery-read-v1 has no runs and execution_authorized=false. Prior inventory r3-20261124-0820-owner-read-v1 SUCCEEDED as of 00:23:12 UTC, nonauthorizing. Fresh inventory r3-20261124-0920-owner-read-v1 initially QUEUED. No shared Task adopted.

## KX.1 — Exact domain and F lifting lemma

Reuse the unsigned ordered positive unit branch model of KV/KW: eight supports indexed by vertices (i,j,k) of Q3, twelve Ports indexed by cube edges, each event chooses one of the three nonzero even triples of local incident-edge bits. E is the even-total Port boundary space; F is the subspace even separately in each of the three direction groups. Mixed means at least two event colors appear. Clip each stock at 2 for raw XOR reachability, as in KV: the local sets at 0,1,>=2 events are respectively zero, the three nonzero even triples, and the full even triple space.

Let A be the occupied vertex set. Relax singleton restrictions, allowing all even local triples. The image is the span of pair masks joining incident Ports, hence consists exactly of vectors even on every component of the graph on Ports with a triangle at each occupied support. If F is contained in this image, every direction group must be in one component: otherwise the vector supported on two Ports of that group in different components belongs to F but violates component parity. Any occupied triangle touches all three groups, so all Ports must be connected. The empty A also fails F. Connectedness of this Port graph is equivalent to A being a connected vertex cover of Q3: an edge with both ends empty is an isolated Port; the occupied triangles meet exactly when their support vertices are adjacent.

When A is a connected vertex cover, write any relaxed solution for a boundary b as x0+z with z in the binary cycle space Z(G) of the induced occupied graph G, by KW.1. At each singleton v the forbidden fiber is p_v(z)=x0_v, where p_v is the local incident-edge projection. Assume at least one double. Any assignment of forbidden even triples q_v at singletons can be realized by a relaxed x0 whose boundary belongs to F: set x0_v=q_v at singletons, choose the triple at one double to be the XOR of these singleton triples, and put zero at every other occupied vertex. For each direction the XOR of all local bits is exactly the group parity of b; hence b is in F. Thus whenever forbidden fibers cover Z(G), this construction gives an explicit unreachable F boundary, not merely an unreachable E boundary. Conversely, if no such cover exists, all E boundaries are reachable, as proved in KW.1.

This is an analytical bridge from F-only coverage to E coverage for every clipped stock with a double. No source-history quotient is taken.

## KX.2 — No clipped ten-event stock can saturate F

If A is a connected vertex cover, its complement is independent. With a=|A|, the internal edge count is 12-3(8-a)=3a-12, so connectedness implies 3a-12>=a-1, hence a>=6. For total 10 the singleton count is s=2a-10 and double count 10-a>=2. It suffices to construct a cover of Z(G) by one forbidden fiber per singleton for a=6,7,8.

a=6, s=2. The two missing vertices are nonadjacent; as in KW, G is a six-cycle or a square with two pendant leaves. Its cycle space has dimension one. If either singleton lies off the cycle its zero forbidden fiber covers everything. Otherwise choose the local projection of the zero cycle at the first singleton and of the nonzero cycle at the second: together they cover both cycles.

a=7, s=4. Remove 000 by symmetry. Use KW coordinates a,b,c on the three subdivided outer edges of the K4 carrier. There are three rank-one local maps (one coordinate each), and four rank-two maps (the three pairs of coordinates at outer vertices and the pairwise-XOR map at the center). Let k be the number of rank-one singleton maps.
* k=3: select their forbidden values so that only one point survives; the fourth fiber can contain that point.
* k=2: the two coordinate exclusions leave a two-point line; assign each of the two rank-two fibers to contain one of those points.
* k=1: the coordinate exclusion leaves a four-point square. Among the three selected rank-two maps at least one of the two outer maps containing that coordinate must appear. Its forbidden fiber can cover two points of the square, and the other two fibers can cover one remaining point each.
* k=0: all four rank-two maps occur. Their kernels are the coordinate directions 100,010,001 and 111. The disjoint pairs {000,100}, {001,011}, {110,111}, {010,101} partition the cube and are fibers in precisely these four directions. Choose the corresponding forbidden values.
All four cases provide an exact cover.

a=8, s=6. There are two doubles; cube symmetries reduce their positions to {000,d}, d in {001,011,111}. Write the six face bits as X_i,Y_j,Z_k and fix X_0=0 (global complement gauge). Enumerate the 32 cycle coordinates in lexicographic order (X_1,Y_0,Y_1,Z_0,Z_1). The local triple at vertex (i,j,k), as an integer with the i-direction bit of weight 1, j-direction weight 2, k-direction weight 4, is
p_v=(Y_j XOR Z_k)+2(X_i XOR Z_k)+4(X_i XOR Y_j).
Every even triple has one of the labels 0,3,5,6. The following explicit certificates cover all 32 cycles. Vertex labels are binary ijk encoded as 0..7. Each row gives singleton vertices, forbidden values, then the corresponding 32-bit fiber masks (bit number is the lexicographic cycle index).
* d=1: vertices 2,3,4,5,6,7; q=0,5,0,5,3,6; masks 03030303,50505050,cc000033,00aa5500,30300c0c,0505a0a0.
* d=3: vertices 1,2,4,5,6,7; q=0,0,0,5,3,6; masks 00550055,03030303,cc000033,00aa5500,30300c0c,0505a0a0.
* d=7: vertices 1,2,3,4,5,6; q=0,0,6,0,5,3; masks 00550055,03030303,a0a0a0a0,cc000033,00aa5500,30300c0c.
The bitwise OR of each row is ffffffff. Each mask follows by substitution of the displayed local formula, and the OR is a small exact certificate rather than a search over stocks or boundaries. Thus every six-singleton selection on the full cube admits a forbidden cover.

By KX.1 each cover produces an unreachable boundary in F. The same obstruction holds for all smaller stocks: after clipping, if the occupied set is not a connected vertex cover the span already fails F; otherwise 6<=a<=8 and a stock of total <=10 can be enlarged to total exactly 10 on the same occupied set by replacing singles with doubles. These replacements only enlarge raw reachable sets. The enlarged stock fails F, so the original fails. Clipping preserves raw reach for arbitrary integer stocks, proving the lower bound 11 for all stocks, even before mixed filtering.

For sharpness remove two opposite cube vertices, place one singleton on the surviving six-cycle and doubles at the other five vertices. The local projection at the singleton takes two values, so any single forbidden value leaves a cycle; all E boundaries are attained. If a chosen word is monochromatic, change the two identical events at a double to two of a different color, preserving XOR and making the word mixed (other events remain). Total=11. This gives an analytical lower and upper bound with only three explicit 32-bit certificates for the lower bound, independent of KV's 6561-stock census.

## KX.3 — General four-way saturation equivalence without the stock census

For any clipped stock with a double and connected occupied vertex cover, KX.1 proves raw F saturation iff raw E saturation. For disconnected Port graph F fails by the span argument. If there is no double, total <=8 and KX.2 rules out F saturation. If raw E saturation holds, KX.2 gives total >=11; a double exists and the monochromatic repair in KX.2 works for each target. Consequently raw F, raw E, mixed F and mixed E saturation are equivalent for every clipped stock. For arbitrary stocks, KV's extra-event translation extends mixed E coverage: prescribe colors for extra events, XOR their boundary into the requested target and choose a mixed clipped word. Fixed interleaving does not destroy mixedness. This establishes the full four-way equivalence analytically apart from the three explicit cube certificates.

## KX.4 — Independent executed checks

The following exact Python set propagation (no counting or cycle-cover logic) was actually executed for all 784 ternary stocks of total 10. It asserts each fails raw F coverage and records the maximal raw coverage.
```python
from itertools import product
masks=[]
for i,j,k in product(range(2),repeat=3):
 a=1<<(2*i+j); b=1<<(4+2*i+k); c=1<<(8+2*j+k)
 masks.append((a|b,a|c,b|c))
F={i for i in range(4096) if all(((i>>s)&15).bit_count()%2==0 for s in (0,4,8))}
E={i for i in range(4096) if i.bit_count()%2==0}
counts={}; mxF=mxE=0
for t in product(range(3),repeat=8):
 if sum(t)!=10:continue
 R={0}
 for m,es in zip(t,masks):
  for _ in range(m):R={r^e for r in R for e in es}
 assert not F<=R
 a=sum(m>0 for m in t);counts[a]=counts.get(a,0)+1
 mxF=max(mxF,len(R&F));mxE=max(mxE,len(R&E))
print(counts,sum(counts.values()),mxF,mxE)
```
Observed: {5: 56, 6: 420, 7: 280, 8: 28} 784 508 2032. The three full-cube certificates were separately found by exact enumeration of the 4^6 forbidden assignments, computing masks by the stated face formula; their proof only uses the displayed witnesses, not completeness of that search.

## Next

For a fixed prefix schedule and terminal b, derive the exact required residual subset b XOR P and characterize the smaller reserve by affine fiber avoidance restricted to that subset. The universal 11 threshold does not apply automatically to that smaller observer. Preserve native signs, time, three-dimensional slice common depth, and ordered BRC information; this is a scoped unsigned auxiliary result, not a typed native BRC equivalence or formal task completion.
