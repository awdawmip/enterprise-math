# X6 R58 — Diagonal Port-equality BRC tomography

Date: 2026-11-20 (Asia/Shanghai). Task: RS-X6-NATIVE-TIME-DYNAMICS. Status: CONDITIONAL_AUTHOR_PROOF / EXACT_FINITE_BRC_CHECK_PASS / NOT_INDEPENDENTLY_REVIEWED.

## Inputs and declared model

Frozen scientific input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389 (P000 V5). Source: R57, research_notes/portable_direct/2026-11-20_x6_r57_collision_orbit_future_language.md@51456406362177f25323f8512179c0d3bcdcfbe5.

Retain R57's conditional ordered collision geometry g=(a,b) in J², J={0,...,p-1}, p>=1. A and B are individually named sources; each fires an indivisible three-force carrier through one of p Ports, once only. Exactly A_a and B_b share target Cell c, with other target Cells distinct. A_i B_j without release succeeds iff (i,j)!=(a,b). Current task asks which joint source-Port incidence survives erasure of absolute Port names. Observe source letters, the predicate "the two used Port indices are equal", and positive BRC branch masses; no signed cancellation. Assign arbitrary positive per-event, source-specific Port-independent weights u and v.

## Theorem R58.1: exact four-mass reconstruction

Let U=Z(A), V=Z(B), T=Z(AB), and W=Z(AB with equal underlying Port indices), where AB refers to consecutive source transfers without R or T between them. Put delta=1 if a=b, else 0. Then for every p>=1 and positive u,v:

\[
\boxed{U=pu,\quad V=pv,\quad T=(p^2-1)uv,\quad W=(p-\delta)uv.}
\]

Proof: of p² ordered Port pairs (i,j), the sole forbidden one is (a,b), because A occupies the sole shared Cell iff i=a and B would then require that occupied Cell iff j=b. Among the p diagonal pairs (i,i), the forbidden pair is diagonal exactly when a=b. Multiply successful branch counts by uv. For p=1, T=W=0 as required. QED.

Because UV-T=uv>0, the unknown Port count and collision equality bit are reconstructed exactly by

\[
\boxed{p=\sqrt{\frac{UV}{UV-T}},\qquad
\delta=p-\frac{p^2W}{UV}.}
\]

Thus the four exact positive observations identify p and whether a=b without knowing the absolute Port labels, u or v. Necessary model-consistency checks: UV-T>0; UV/(UV-T) is a positive perfect integer square; recovered delta is in {0,1}, with delta=1 for p=1. These formulas are invariant under unknown *per-source event gains* already absorbed into u,v; arbitrary unrelated gains on U,V,T,W are outside their claim.

## Theorem R58.2: exact simultaneous-renaming orbit classification

Let S_p act on both sources by the same Port permutation pi, carrying (a,b) to (pi(a),pi(b)). For p>=2 its orbits are exactly the diagonal a=b (p elements) and off-diagonal a!=b (p(p-1) elements); for p=1 there is one orbit. U,V,T,W are constant on each orbit, and W differs across the two orbits by uv>0. Hence the four-mass observer identifies exactly the two simultaneous-renaming geometry classes. One bit is a sharp fixed-length code for this **orbit type** when p>=2, compared with the ceil(log2(p²)) bits needed for the full absolute labelled geometry from R57.

If A and B Port labels may instead be renamed independently, S_p×S_p is transitive on all g. Those independent relabellings transport every R57 typed event (including its conditional R/T) and every positive source-only path mass, so complete future observations that discard cross-source equality cannot distinguish diagonal from off-diagonal g. The equality bit is therefore a genuine joint provenance coordinate, not an extra spatial axis or force. No claim is made that the native X6 rotation group equals either relabelling group.

## Corollary R58.3: sharp ratio-observation resolution

For p>=2, H=W/T=(p-delta)/(p²-1). The two possible H values differ by exactly 1/(p²-1). Under a sole absolute error budget epsilon on this already-formed scalar H, the two closed compatibility intervals are disjoint exactly when epsilon < 1/[2(p²-1)]. At equality their midpoint is compatible with both classes, proving sharpness. This does not certify independent error budgets on raw U,V,T,W.

For p>=2, a Boolean observer asking only whether some equal-Port AB transfer exists sees yes in either case, as p-delta>=1. Positive BRC multiplicity supplies strictly more joint incidence information in this observer.

## Scope and falsifier for larger incidence networks

For an arbitrary bipartite set C of blocked Port pairs rather than the single collision pair, the two aggregate masses become T=(p²-|C|)uv and W=(p-|C intersect diagonal|)uv. They are not a complete graph-isomorphism invariant. At p=3, C1={(0,1),(1,0)} and C2={(0,1),(0,2)} have the same edge count 2 and zero diagonal edges, but their A-side degree multisets are (1,1,0) and (2,0,0). They cannot be related by a simultaneous Port permutation. The single-pair theorem is thus not silently extended to multi-Cell collision networks.

## Exact computation and remaining question

The companion executable Python Fraction verifier explicitly enumerates every geometry for p=1..20 with three exact positive source-weight pairs: 2,870 geometries and 8,610 weighted instances. It checks the four masses and reconstruction formulas. A separate exhaustive Port permutation test for p=1..5 checks 3,447 geometry-renaming cases. A graph-degree counterexample is checked. All assertions pass. The symbolic counting argument establishes the all-integer-p, all-positive-real-weight theorem; finite computation is supporting exact evidence.

Next: find an admitted frozen-P000 Cell/Link/Port event signature realizing the shared-Cell collision guard, and check whether synchronous source Port-index equality descends under an *actual* native X6 rotation. Multi-Cell incidence and correlated raw-measurement errors are separate open extensions. No R/T admission, physical heartbeat law, independent review, formal Result or native PROGRESS is asserted by this conditional note.
