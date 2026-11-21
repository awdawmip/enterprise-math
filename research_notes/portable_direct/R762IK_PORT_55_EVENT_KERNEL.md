# R762IK — 55-event witness kernel for the six-axis composite Port Euler observer

Date: 2026-11-22, Asia/Shanghai. **AUTHOR_PROVED / EXHAUSTIVE_EXACT_CHECKED / NOT_REVIEWED**.

Frozen science: RS-X6-TRIADIC-CLOSURE-DYNAMICS at a72226e2430ffa4786321ac86e7f0c599d5f0389. Earlier immutable sources: R762IH@5f39e2e5faac0b3e8fb358d810eb8d0477e5d612, R762II@5ca203b040c2d42b201be366c5cec21ffa84f59a, R762IJ@cada89a4571801206a4d25fb42f6f8db8526f330. This proves a composite observer graph statement, not the native P000 TRIADIC_CLOSURE_E dynamics.

## Theorem

There are 15 Port vertices, the unordered pairs of the six native axes, and 20 event support types, the three-axis subsets. A support abc permits one event on any one of the three edges of the triangle with Port vertices ab, ac, bc. A valid closed named-event history at specified active Port p is a connected even-degree assigned Port multigraph with an Euler tour starting at p.

For **every** nonzero support histogram n and **every** legal Euler realization of n, there exists a histogram h with h_S <= n_S for all supports and an Euler realization of h such that:

- Support presence and parity are preserved: (h_S > 0 iff n_S > 0), h_S ≡ n_S (mod 2). Thus n-h is a collection of support-identical event pairs.
- The original realization's **active Port set** and its chosen starting Port p remain the same.
- Each h_S ≤ 4 and **Σ_S h_S ≤ 55**.

Conversely, deleted support-identical pairs can be reinserted as two parallel copies of an occupied permitted Port edge for the same support. Thus Port Euler existence is preserved in both directions under this witness-dependent reduction. The bound is not a fixed coordinatewise cap, and does not preserve Euler multiplicities, order or Cell signed displacement.

## Proof I: exact structural reduction

Use R762IH's supportwise pair deletion: remove two copies from an edge containing at least three copies, keeping one; remove a doubled triangle side if the remaining two sides connect its endpoints; and remove either doubled side of a four-event (2,2,0) support when the side is not a bridge in the underlying simple graph. At termination all supports have count ≤4, and each surviving four-count *critical* support has occupancy (2,2,0) on two distinct simple-graph bridges.

One can additionally reduce a three-event support: (3,0,0) loses two copies, and (2,1,0) loses two copies on the doubled edge whenever that edge is not a bridge. Continue all permissible reductions. Every remaining three-count support now occupies at least two sides of its triangle, hence all three Port vertices lie in one connected component after removal of critical four-support bridge edges. All deletions preserve support presence, count parity, even vertex degrees, connectedness and active vertices.

Let k be the number of critical four-event supports and T the number of three-event supports in the terminal graph. Each Port edge uniquely determines its support, so the 2k critical bridges are distinct. Therefore k≤7, and removing them from the simple connected Port graph yields exactly 2k+1 components on the active vertices.

For an arbitrary subset of T three-axis supports, join all three sides of their Port triangles and count connected components on **all fifteen** Port vertices, leaving unused vertices isolated. Let M(T) be the maximum such component count across every T-subset of the 20 types. Our original active graph has 2k+1 components after bridge removal, and inclusion of unused Port vertices only adds possible isolated components. Thus **M(T) ≥ 2k+1**.

The accompanying C++17 integer DSU checker exhaustively examines all 2^20=1,048,576 support subsets and establishes:

| T | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17–20 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| M(T) | 15 | 13 | 11 | 10 | 10 | 8 | 7 | 7 | 6 | 6 | 6 | 4 | 3 | 3 | 2 | 2 | 2 | 1 |

For k=1,2,3,4,5,6,7, respectively, T≤13,10,7,4,2,1,0. At most 20 supports are positive; the k critical supports contribute four each, the T three-supports contribute three each, and the others contribute at most two. Therefore

  Σh_S ≤ 3T+4k+2(20−T−k) = 40+T+2k.

The seven upper bounds are respectively **55,54,53,52,52,53,54**. All k≥1 cases are proved.

## Proof II: k=0 complete high-count constructive cover

When k=0, each positive support has count 1, 2 or 3, with Σh_S≤60. Histograms already ≤55 require no change. Every case of size 56–60 falls in exactly the following 11 families, using U for count one, E for count two, M for missing, and all remaining supports of count three:

| Family | #U | #E | #M | Histogram placements | S6 orbits | Original count | Result count |
|---|---:|---:|---:|---:|---:|---:|---:|
| T20 | 0 | 0 | 0 | 1 | 1 | 60 | 54 |
| E1 | 0 | 1 | 0 | 20 | 1 | 59 | 55 |
| E2 | 0 | 2 | 0 | 190 | 3 | 58 | 54 |
| E3 | 0 | 3 | 0 | 1140 | 7 | 57 | 55 |
| E4 | 0 | 4 | 0 | 4845 | 21 | 56 | 54 |
| U1 | 1 | 0 | 0 | 20 | 1 | 58 | 54 |
| U2 | 2 | 0 | 0 | 190 | 3 | 56 | 54 |
| U1E1 | 1 | 1 | 0 | 380 | 3 | 57 | 55 |
| U1E2 | 1 | 2 | 0 | 3420 | 12 | 56 | 54 |
| M1 | 0 | 0 | 1 | 20 | 1 | 57 | 55 |
| M1E1 | 0 | 1 | 1 | 380 | 3 | 56 | 54 |
| **Total** | | | | **10,606** | **56** | | |

The companion Python standard-library checker constructs the 56 orbits by explicitly applying all 720 permutations of six axes. For each representative it searches for a **specific Euler multigraph**, then verifies every support count, parity of all 15 vertex degrees, connectedness, and presence of all intended supports. Every histogram in the orbit is the image of the representative under an axis permutation, so the 56 positive exact checks cover all 10,606 high-count histograms.

**Reproducible construction.** Initially assign each count-three support a full triangle, giving degree two to each vertex, and each count-two support a double edge, again giving even degrees. Replace enough selected count-three targets by one edge each to reduce the event total to ≤55. Treat each chosen target and each existing count-one support edge as a two-vertex mod-2 boundary. For each boundary, search a two-edge Port path from its first to second endpoint using edges of two still-full, different-support triangles. Combine path-edge boundaries assigned to each helper support by XOR in GF(2)^15. On a helper triangle this XOR is either zero or the boundary of one of its three sides. For zero use (1,1,1); otherwise replace that full triangle with its three-edge (1,2,0) arrangement whose odd side gives exactly the needed boundary. The checker's constructed edge multiset then passes all exact Euler and support-count checks, so this is a concrete finite certificate rather than a heuristic.

**Preserving the original active Port set.** All these high-count histograms have at least 16 count-three support types. Each Port belongs to exactly four support types. With at least 17 full triangles, all 15 Ports must be active in every original realization (each full three-event triangle occupies at least two sides after our reduction). With exactly 16, the only possible missing Port occurs in E4, when the four even support types are the four triangles incident to a single pair-Port. That Port may be inactive. The checker **additionally constructs and verifies** a 54-event connected even-degree realization on the corresponding **14** Ports, excluding that one vertex, for this exceptional orbit; when it was originally active, the all-15-Port witness applies. Thus the original active set and arbitrary designated active start p are preserved.

## Exact verification and scope

Execution performed on 2026-11-22 using Python 3 standard-library integer operations and C++17 integer DSU. The C++ checker exhausts 1,048,576 triangle masks, calculates the displayed exact M(T), and returns PASS with k≥1 maximum 55. The Python checker exhausts the 10,606 high-count histograms via 56 complete S6 orbits, constructs and validates an Euler witness for each representative, and validates the 14-active-Port exception: PASS R762IK. These are executable, reproducible finite certificates; the unbounded-length theorem is the preceding graph proof plus this exhaustive finite cover.

Run from the repository root:
    python3 research_notes/portable_direct/R762IK_CHECK.py
    g++ -O2 -std=c++17 research_notes/portable_direct/R762IK_COMPONENT_SCAN.cpp -o /tmp/r762ik_scan
    /tmp/r762ik_scan

Port Euler existence, support parity/presence, the same active Port set and starting p are retained. This lossy observer does **not** retain event order, all named-history counts, six-axis signed Cell displacement, positive BRC masses, path provenance, native force, time or rotation. The latter require separate observer/future-operation preservation bridges to native P000; no such promotion is asserted. Formalization and independent proof review have not been completed: **NOT_REVIEWED**.

Open research: exclude or construct the k=1,T=13 extremum to test a 54-event bound; search whether all k=0 56-event families also reduce further; build a histogram-only algorithm outputting a Port Euler circuit or exact infeasibility certificate; seek type-faithful P000 native TRIADIC_CLOSURE_E lift.

## Control and provenance

Historical author: EM-X6-A681A5, SID MCP-773502d89b7a4bd58a37e97a2dd52ba5, whose own managed session was confirmed open by read-only recovery in this turn. Exact native continuation request r3-20261122-0628-x6-cont-read-v1 returned **FAILED / SOURCE_TREE_TRUNCATED** at current Source 41e8bb8df2b398b75c937084070b302dc0b23147; active Task owner/CLAIM is unconfirmed and execution_authorized=false. This independent non-overwriting GitHub research file is neither protected PROGRESS nor formal Result/Review/Foundation admission.
