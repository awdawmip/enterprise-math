# R762IQ — Exhaustive parity census and complete obstruction orbits

Date: 2026-11-22 Asia/Shanghai. Status: AUTHOR_DERIVED / EXACT_FINITE_ENUMERATION / NOT_REVIEWED.
Frozen six-axis composite Port-Euler scientific source: a72226e2430ffa4786321ac86e7f0c599d5f0389.
Predecessors: R762IO and R762IP at 449ecf17d3407c86a18323288fa5972c742d6ab6 (Draft PR #2941); R762IM at b5e3a6073c54d1bbccd3a5d798887def7243a34c (prior exhaustive-coverage gap remains recorded).

## Exact domain and statement

Let A={0,...,5}. The 15 Ports are unordered pairs of axes, and the 20 support types S are unordered triples. A support S supplies a triangle on its three contained pair-Ports. One event chooses one triangle edge. Consider every labeled multiplicity n_S in {0,1,2,3} with sum_S n_S in {54,56,58,60}. For each inactive-Port set M, require local incidence admissibility: every support of positive multiplicity has at least two Ports outside M. This is equivalent to F(M) being a subset of Z={S:n_S=0}, as in R762IO.

The exact R762IP GF(2) component criterion distinguishes all-even Port-degree realizability from its failure. Over the COMPLETE domain of 14,260,096 labeled (n,M) incidence-admissible pairs, exactly 14,259,376 are degree-parity feasible; exactly 720 are parity-infeasible.

All 720 obstructions have the following exact classification:
- sum_S n_S=54; exactly two support types are missing and all other 18 supports have multiplicity three.
- The two missing supports intersect in exactly one axis.
- Among the 90 labeled pairs of missing supports of intersection size one, each has exactly four parity-infeasible M with |M|=3 and exactly four with |M|=4. Thus 90*(4+4)=720.
- In each of the 720 cases the graph of adjustable full-three-Port supports has exactly two components: one singleton Port and one component containing all other active Ports (11 or 10 respectively). The singleton has odd forced boundary charge. The latter is a direct, independently checkable obstruction.
- Under the natural S6 permutation action there are exactly TWO obstruction orbits of size 360 each, distinguished by |M|=3 versus |M|=4.

The two orbit representatives can use zero-support pair {012,034}. Inactive M for the |M|=3 orbit: {03,04,15}. Inactive M for the |M|=4 orbit: {03,04,15,34}. For the former, Port 01 is an isolated adjustable component with odd forced degree; it remains so after additionally inactivating 34.

## Exhaustive exact census

| Number m of absent supports | Labeled multiplicities | Locally admissible (n,M) | Parity feasible | Parity impossible |
|---|---:|---:|---:|---:|
| 0 | 155,156 | 11,791,856 | 11,791,856 | 0 |
| 1 | 26,600 | 2,447,200 | 2,447,200 | 0 |
| 2 | 190 | 21,040 | 20,320 | 720 |
| TOTAL | 181,946 | 14,260,096 | 14,259,376 | 720 |

| Total events | Parity feasible | Parity impossible |
|---|---:|---:|
| 60 | 76 | 0 |
| 58 | 15,960 | 0 |
| 56 | 677,540 | 0 |
| 54 | 13,565,800 | 720 |

## Proof and computational certificate

Write deficits d_S=3-n_S. Then d_S ranges from 0 to 3 and sum d_S=60-sum n_S belongs to {0,2,4,6}. A full recursive enumeration of the 20 deficits with the exact sum covers every labeled multiplicity once. Each n_S=0 consumes three deficit units, so m<=2, and each singleton n_S=1 consumes two deficit units, so at most three singleton choices occur. Enumerate precisely all 2^15 Port masks M and retain those for which every positive support has at least two active Ports, preindexing allowed M for the 211 possible zero-support sets of size at most two. This gives R762IO's complete local population of 14,260,096 pairs.

For each retained pair construct G_free by uniting all three active Ports of every support with n_S>=2 and all three active. A support with exactly two active Ports contributes its forced odd-parity boundary iff n_S is odd. A support with all three active Ports and n_S=1 supplies one of its three edge boundaries. Enumerate those choices (at most 3^3=27), quotient each boundary to components of G_free, and accept iff a total zero component signature exists. R762IP proved this test equivalent to existence of an assignment with all Port degrees even, at arbitrary finite n.

The attached C++17 checker performs this entire enumeration with integer bit masks and exact GF(2), independently checks the population and all aggregate counts by deficits and absent-support intersection. A second Python checker independently enumerates all 190 two-zero-support cases and all 2^15 masks, checks component charges by a separately written algorithm, confirms the size-3/size-4 distribution, checks every odd singleton component, and computes both S6 orbits. On the local execution in this run both completed with PASS. Finite exhaustive counts are exact for the declared domain; scripts are supplied as replay evidence.

## Scientific interpretation and continuation

The parity quotient eliminates precisely 720 of the 14,260,096 R762IO local candidates. For every other pair it proves even-degree realizability but still does not require each intended active Port to have positive degree or require the realized graph to be connected. Thus the R762IM global 52-event high-tail compression statement remains OPEN pending exact connectivity and same-active-set witness validation; this census repairs its parity-search scope, not its full proof.

Next research unit: use the parity-pass candidates to check exact positive activation, connectivity and preservation of the active Port set under 52-event removal (or produce a genuine counterexample). Retain frozen P000 and observer scopes; this Port graph theorem makes no native heartbeat/time-dynamics claim.

Role/control: independent portable science on the existing R762IP line; no native CLAIM, PROGRESS, Result, Review, or historical identity adoption is implied.
