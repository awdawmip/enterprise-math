# R704 — X6 signed triadic-path Port incidence and exact BRC observer compression

Date: 2026-11-11 (Asia/Shanghai). Task: `RS-X6-TRIADIC-CLOSURE-DYNAMICS`, immutable publication `TP2-8B7E13C5904A2D6F1142`. Scientific input frozen at `awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389`; P000 V5, `definitions/P000_DISCRETE_DIRECTION_TRIADIC_BALANCE_20260905.md` and `definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md`. Authors' R703 prior result: `ab68d798d7c7564d03d9baa2025a979930632719`. This is an author-side candidate computation, not a reviewed native dynamics law.

## Carrier, observer and operation

The native spatial X6 is a `Z^6` affine Cell torsor. A signed primitive spatial step is `T_i^σ(z)=z+σ e_i`, `i=0,...,5`, `σ∈{−1,+1}`. Fix an arbitrary Cell `c`, and form every ordered three-step path using **three distinct axes**, each bearing one fixed sign. Its label is the entire ordered word, not just endpoint. This is a potential transport carrier for a three-action event; it is not itself a definition of `TRIADIC_CLOSURE_E`.

For this local test only, introduce independent static directed Boolean Port gates `D(z,i,σ)∈{0,1}`; each step queries the gate at the Cell immediately before that step. This extra gate independence is a **candidate model assumption**, not a native Link/Port occupancy or V29/V39 conservation claim. BRC gives each permitted ordered source unit positive mass. Two declared observers are (i) full labeled source support and (ii) 160 native endpoints' **unnormalized** source-count histogram. Future operations covered are static gate filtering and queries of those observables. No force-cancellation interpretation is attached to positive mass.

## Theorem A — signed triadic source count and nonreturn

The 20 choices of three axes, eight sign patterns and six permutations produce exactly

`20·8·6 = 960` labeled sources and `20·8=160` distinct Cell endpoints, each reached by six paths. Every endpoint displacement has exactly three coordinates `±1`, hence `||Δz||_1=3`, `L_E(Δz)^2=3` and `Δz≠0`. Therefore **none of the 960 three-step distinct-axis paths is a native spatial return**. A triadic stable-force relation in P000 must have its own typed closure/event semantics; identifying it with this particular native spatial-return condition would leave this candidate family empty. It is a sharp representation obstruction, not a challenge to the P000 triadic axiom.

For `d≥3` dimensions, the same count is `8d(d−1)(d−2)` ordered paths and `8·binom(d,3)` endpoints, six paths per endpoint.

## Theorem B — exact local Port influence

Each path checks three directed ports. Partition by the Manhattan distance from its starting Cell at the check:

| Step | Directed Port sites | Sources using each |
|---|---:|---:|
| 1 at `c` | 12 | 80 |
| 2 at `c±e_i` | 120 | 8 |
| 3 at `c±e_i±e_j, i≠j` | 480 | 2 |
| **Total** | **612** | 960 three-port paths |

Proof for general `d`: first layer has `2d` ports and `4(d−1)(d−2)` suffixes each; middle layer has `4d(d−1)` ports with `2(d−2)` suffixes; last layer has `4d(d−1)(d−2)` ports, each used by the two permutations of its first two steps. With `d=6` these give 12+120+480=612, and total incidences `12·80+120·8+480·2=2880=960·3`.

The radius-two bound is sharp. From all open gates close only `D(c+e_0+e_1,2,+)=0`. All gates at distance ≤1 are unchanged; exactly `(0+,1+,2+)` and `(1+,0+,2+)` lose permission. The other 958 sources remain permitted.

## Theorem C — distinguishability of single-Port faults

From the all-open gate field, the complete labeled source-loss set from closing a single gate is the set of paths traversing it. Distinct gates in a single step layer control disjoint source sets (classified by the first step, ordered first-two prefix, or last step at its final pre-Cell). Across layers, their loss cardinalities 80,8,2 differ. Thus **all 612 single-gate closures have different labeled BRC source-loss signatures**.

For the coarser endpoint-count observer, closing a last-layer gate removes two out of six sources at precisely one endpoint. For each endpoint there are three possible last-axis ports, so **480 distinct terminal gate faults collapse to exactly 160 endpoint-count signatures**, each with three possible original gates. For example endpoint `c+e_0+e_1+e_2` has three final-axis choices, each deleting a different two-source pair. After one terminal-gate closure, uniformly drawing from remaining paths gives probability `4/958=2/479` at the affected endpoint and `6/958=3/479` at each other endpoint.

## Theorem D — sharp 480-bit versus 320-bit state spaces

Hold **all first- and second-layer gates open** and vary only the 480 independent last-layer gate bits. Their source blocks are disjoint two-source pairs partitioning all 960 paths; hence there are precisely `2^480` distinct permitted labeled-source masks. Any fixed-length exact code for their full source-support observer needs 480 bits; storing these 480 gates achieves the bound.

The three last-layer gates belonging to one endpoint are exclusive to it. Its unnormalized permitted source count is twice its number of open last-layer gates, one of `{0,2,4,6}`. Across 160 endpoints all these four counts vary independently: there are exactly `4^160=2^320` endpoint-count histograms. Their optimal exact fixed-length code takes **320 bits** (two bits per endpoint, encoding 0..3 open terminal gates). This quotient is future-sufficient only for endpoint-symmetric observation/operation, and loses addressed last-axis Port information. The claim is about **unnormalized counts**; normalized probability kernels can have additional identifications.

## Validation and continuation

`experiments/R704_X6_TRIADIC_GATE_VERIFY_20261111.py` exhaustively constructs 960 ordered signed native three-distinct-axis paths, 160 six-source endpoints, 612 directed ports with usage multiplicities, 612 unique single-fault source signatures and 480 disjoint terminal source-pairs, and checks exactly three terminal pairs per endpoint. The executable evidence marker is `R704_X6_SIGNED_TRIADIC_PORT_INCIDENCE_EXACT_PASS`; see JSON evidence adjacent to the script. All counts are integer-exact; the exponentially large state-space cardinalities follow from the proved independent block partition, not infeasible enumeration.

Next: read an actual source-pinned Cell/Link/Port occupancy/update contract (and V29 PASS/TRANSFER, V39 `j`), then construct two decorated packets with the same endpoint count histogram but distinct terminal gates and test whether one genuine permitted event distinguishes them. Establish a separate typed `TRIADIC_CLOSURE_E` event and rotation covariance before claiming native triadic dynamics or a formal Result. The frozen scientific pin remains unchanged.