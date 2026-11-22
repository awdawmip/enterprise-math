# R762IO — corrected inactive-Port census and a 14-Port T20 witness

Date: 2026-11-22 (Asia/Shanghai). Status: AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED.
Scope: frozen six-axis composite Port-Euler observer only. Scientific input pin: a72226e2430ffa4786321ac86e7f0c599d5f0389.
Predecessors: R762IM@b5e3a6073c54d1bbccd3a5d798887def7243a34c and R762IN@1ce925dcd2168c6cb890128e8cdb864bf4a3158d.
Control: independent portable result; no CLAIM, PROGRESS, Review or native P000-dynamics promotion is asserted.

## Definitions and exact local criterion

Let A={0,1,2,3,4,5}. Ports are the 15 unordered axis-pairs, identified with the edges of K6. Supports are the 20 unordered triples S. Each positive support event chooses an edge joining two of the three pair-Ports contained in S. Fix Z, the set of zero-multiplicity supports, and M, the proposed set of inactive Ports. For the graph H=(A,M), let

F(M)={S: |C(S,2) intersect M| >= 2}.

There exists a supportwise allocation of every positive event to an edge wholly outside M (without imposing even degrees or connectedness) if and only if F(M) is a subset of Z. For a positive support S, two active pair-Ports are necessary and sufficient for at least one allowed edge. This is an exact equivalence for the LOCAL incidence condition; it is only a necessary condition for a connected Euler realization with exactly the proposed active set.

Writing d_H(v) for the degree of axis v in H and t(H) for the number of triangles of H, the number of forced-zero supports satisfies the integer identity

|F(M)| = sum_{v in A} binom(d_H(v),2) - 2 t(H).

Proof: every two edges of H sharing an axis form a wedge in a unique triple support. A support with exactly two missing pair-Ports contributes one wedge; a support with three contributes three wedges and is counted once after subtraction of two. All other supports contribute zero.

## Complete finite census for at most two absent supports

Classify Z by its size, and for size two by the intersection size of its two triple supports. The entries below give the exact number of labeled inactive-Port masks M of size j that satisfy F(M) subset Z, for one FIXED Z of that class (not yet Euler feasibility):

| Z type | count of Z | j=0 | j=1 | j=2 | j=3 | j=4 | j=5 | j=6 | total M per Z |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| none | 1 | 1 | 15 | 45 | 15 | 0 | 0 | 0 | 76 |
| one absent support | 20 | 1 | 15 | 48 | 25 | 3 | 0 | 0 | 92 |
| two disjoint/complementary supports | 10 | 1 | 15 | 51 | 35 | 15 | 6 | 1 | 124 |
| two supports meeting in one axis | 90 | 1 | 15 | 51 | 35 | 6 | 0 | 0 | 108 |
| two supports meeting in two axes | 90 | 1 | 15 | 51 | 37 | 8 | 0 | 0 | 112 |

Independently, the potential-edge graph on V=C(A,2)\M, formed by all legal edges available to positive support types, is connected for EVERY pair (Z,M) in this table. The exact exhaustive check covers 76 + 20*92 + 10*124 + 90*108 + 90*112 = 22,956 such labeled pairs. This graph is a superset of edges that an actual fixed-multiplicity realization may select. Connectivity of the potential graph does not prove Euler realizability.

### Corrected input domain for R762IM's high-tail families

For terminal multiplicities n_S in {0,1,2,3} and even totals 54,56,58,60, let m,u,e count supports with multiplicities 0,1,2, with the remaining 20-m-u-e supports at multiplicity 3. Necessarily D=60-sum n_S = 3m+2u+e in {0,2,4,6}. Thus m <= 2. Independent exact multinomial enumeration yields:

| zero support count m | labeled histograms | locally admissible inactive masks per histogram / aggregate | labeled (n,M) pairs |
|---|---:|---|---:|
| 0 | 155,156 | 76 each | 11,791,856 |
| 1 | 26,600 | 92 each | 2,447,200 |
| 2 | 190 | 10*124 + 90*108 + 90*112 over all two-zero choices | 21,040 |
| total | 181,946 | full local incidence domain | 14,260,096 |

These are LOCAL incidence candidates, not a count of Euler histories or of distinct realizable active sets. They give a complete replacement search domain for the previous over-restrictive inactive-Port filter, before exact parity/activeness/connectedness testing. In particular the earlier R762IM checker checked only 3,165 special 14-Port cases and incorrectly excluded many locally admissible 14-Port and smaller active sets; its claimed exhaustive proof cannot be reused without rechecking the omitted cases. The existential 52-event statement remains open at this dependency until repaired, not refuted by these counts.

## Explicit new 60-event, 14-active-Port Euler witness

For each support S in lexicographic order below, choose the displayed pair-Port edge and repeat that same edge THREE times:

012: 02-12; 013: 03-13; 014: 04-14; 015: 05-15;
023: 02-03; 024: 02-04; 025: 02-05; 034: 03-04;
035: 03-35; 045: 04-45; 123: 12-13; 124: 12-14;
125: 12-25; 134: 14-34; 135: 15-35; 145: 14-45;
234: 23-24; 235: 23-25; 245: 24-45; 345: 34-45.

This 60-edge multigraph is connected, has even positive degree at each of its 14 active Ports and degree zero at Port 01. Each of the four supports 012,013,014,015 contains the inactive Port 01 and nevertheless has multiplicity 3, directly falsifying R762IM's statement that an inactive Port cannot belong to a three-event support.

Delete two of the three parallel events for each of the first four supports above: a 52-event connected even-degree witness remains, with exactly the same 14 active Ports, all 20 supports positive and each support multiplicity odd. Any active Port can be selected as the start of an Euler tour. Six-axis permutation transports the construction to any designated single inactive Port.

The attached Python checker verifies all 20 legal edge labels, support counts, vertex degrees, connectedness and this explicit 52-event recovery. This example does not decide the full 14-family 52-event claim.

## Exact verification, evidence and next step

Run: python3 research_notes/portable_direct/R762IO_CORRECTED_ACTIVE_PORT_CENSUS_CHECK.py.
Arithmetic: exact Python integers and finite bitmasks; enumerates 2^15 inactive masks and every Z of size 0, 1 or 2; independent combinatorial wedge identity crosscheck; exact potential-graph BFS and multinomial histogram count; explicit 60/52-edge witness assertions.
Observed local result: PASS R762IO_CORRECTED_INACTIVE_CENSUS.
Independent mathematical review: NOT_REVIEWED. No native P000 triadic time/force/Cell lifting is inferred.

Next: replace the old R762IM 14-Port-only filter using this complete (n,M) domain. Use exact per-support parity and connectedness with precise support identities to classify realizable (n,M), and construct a 52-event witness or counterexample for each newly admitted class. Preserve older artifacts and correct proof dependencies instead of silently promoting the old completeness claim.
