# R762KI — Exact affine four-point obstruction for two upgraded flexible supports

2026-11-23 · Author-side exact finite theorem · NOT_REVIEWED.

## Model, provenance and exact claim

Continue R762KH from immutable project source at commit 09972bfdb89fde5846768a3688017f7387a17311, file research_notes/portable_direct/R762KH_M3_SHARP_THREE_UPGRADE_EULER_THEOREM.md. Frozen science P000 V5: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. Theorem is for the auxiliary **unsigned** six-axis Port–Euler observer. P000 and the ACTIVE worldview are not changed.

The vertices are 15 two-axis Ports; a three-axis support abc permits an edge joining any two active Ports among ab, ac, bc. Ports 01,23,45 are inactive. The twelve active Ports, in the **integer bit-order** used below, are:

02, 03, 04, 05, 12, 13, 14, 15, 24, 25, 34, 35.

Twelve triple supports have a single forced edge, and eight have a three-edge triangle of choices:

024, 025, 034, 035, 124, 125, 134, 135.

Fix any two-element upgraded subset U of these eight flexible supports. Each upgraded support has arbitrary integer event multiplicity at least 2, the other six flexible supports have multiplicity 1, and the twelve forced supports have arbitrary positive integer multiplicities. Each edge event must retain its support label and the full event graph must be connected with strictly positive even degree at each active Port.

Define boundary(e) = 2^u XOR 2^v for a legal edge e=(u,v), where u,v are zero-based positions in the above twelve-Port list. The 12 forced edges span a GF(2) subspace F of rank 9, with 512 forced degree-boundary targets. Each target is induced by exactly eight of the 4096 possible odd/even masks of the forced support multiplicities.

## Theorem KI.1 — Affine obstruction geometry

For every U of size 2, there is an exactly determined four-element set E_U inside F such that the specified positive inventory has a complete Euler realization **if and only if** the XOR forced boundary is outside E_U.

Each E_U is an affine two-dimensional GF(2) plane; explicitly it has the form {a, a XOR x, a XOR y, a XOR x XOR y}, with x and y linearly independent. Consequently exactly 4 of the 512 forced boundary classes, equivalently 32 of the 4096 forced parity masks, are genuinely impossible for each fixed U, regardless of the size of its two upgraded counts.

The 28 planes E_U are all distinct and their union has exactly 47 points, equal to the forbidden forced boundary set with **no** upgraded flexible supports.

### Three canonical exception templates

A flexible support chooses exactly one axis from each missing Port pair, giving the eight vertices of a three-dimensional Boolean cube. The 48-element group of axis permutations preserving the missing perfect matching acts as the full cube automorphism group. Pairs of flexible supports fall into Hamming-distance orbits of sizes 12,12,4.

| Cube distance | Representative U | Complete E_U (decimal bit masks) | Orbit size |
|---|---|---|---:|
| 1 | {024,025} | 3315, 3327, 4083, 4095 | 12 |
| 2 | {024,035} | 1776, 1791, 4083, 4092 | 12 |
| 3 | {024,135} | 1626, 1791, 3963, 4062 | 4 |

For any other pair, permute six axis names while preserving the missing perfect matching, then permute the twelve active-Port bit positions accordingly. This transports the representative missing set to the target pair. The exact checker verifies every transport and every missing set by direct independent DP.

## Proof of the finite lemma and symbolic count extension

1. Because every forced support appears at least once, the forced-edge graph has three connected four-Port components A,B,C. Every flexible legal triangle uses exactly one edge of each of the three component-pair types AB,AC,BC. Thus all Port vertices are connected precisely when flexible chosen events use two or more different component-pair types.

2. Each non-upgraded support has exactly three possible single-edge choices. A support with minimum upgraded count 2 has exactly six unordered two-event multisets: three repeated edges and three pairs of distinct edges. Encode each local choice as (b,t), where b is a twelve-bit XOR degree boundary and t is a three-bit OR mask for component-pair edge types. The update (b,t) -> (b XOR b_s, t OR t_s) is exact, by induction on the eight flexible supports, because total degree parity composes by XOR and component connectivity depends precisely on the union of the three pair types.

3. The complete exact finite program R762KI_TWO_UPGRADE_AFFINE_VERIFY.py constructs every local choice directly from axis incidence, computes the 512 forced targets, and checks all 28 U against the exact connected state set (type mask with at least two bits). Each gives exactly 508 reachable forced boundaries and exactly four unreachable boundaries. It also checks that the parity-only reachable forced set equals the connected reachable forced set, proving the excluded boundaries are genuine parity obstructions. For each U, the four distinct missing integer vectors have XOR zero; in characteristic 2, four distinct points with zero XOR constitute an affine two-plane.

4. Enumerate all 48 axis permutations preserving missing pairs 01,23,45. The checker explicitly verifies that each missing plane is obtained from the appropriate one of the three listed representatives, and counts the three pair orbits. It also verifies all two-upgrade planes lie inside the 47-point no-upgrade exceptional set and that their union has 47 points. This proves both the symmetric classification and the union equality.

5. To extend the minimal 1/2 proof to arbitrary positive support multiplicities, observe that any n>=2 events in a flexible triangle have exactly the same four possible degree boundaries: zero and the three individual edge boundaries. For even n, extend a minimum two-edge choice with duplicate pairs. For odd n>=3, replace a repeated pair by the three triangle edges when its boundary is zero; replace two distinct edges e_i,e_j by (e_k,e_i,e_i), where e_k is the remaining triangle edge, when the original boundary is boundary(e_k); add duplicate pairs as needed. Parity and at least the needed component connectivity persist. A forced support merely repeats its single edge according to its positive prescribed count.

The resulting graph is connected with all twelve vertices of positive even degree, hence has an Euler circuit from any active Port. Conversely a missing forced parity target is unattainable because no upgraded multiplicity adds another local boundary type. The iff conclusion therefore holds for every multiplicity in the stated domain.

## Exact execution and evidence

Run Python standard library command: python R762KI_TWO_UPGRADE_AFFINE_VERIFY.py. Its deterministic JSON output contains all 28 missing sets and the three orbit templates. The source includes assertions for component decomposition, six local multiset choices, 512 targets, 47 no-upgrade holes, 17 holes for each of eight single upgrades, four holes for each of 28 two-upgrade pairs, affine condition, 48 symmetries, and all pair-orbit transports. Executed in this research turn and all assertions passed. Computation uses integer XOR/OR only; neither random sampling nor approximate arithmetic enters the proof.

This extends R762KH's 508/512 cardinality statement to a complete explicit exception classification and sharp arbitrary-count parity criterion. It is author-side checked, with independent mathematical review pending.

## Next question

Find a concise nonenumerative algebraic expression for the three representative missing planes, and a structural description of their 47-point union. Then extend the parity/connection analysis to the remaining one- or two-inactive-Port configurations and compare source-specific 44→42 compression with target realizability. A signed TRIADIC_CLOSURE_E Cell/Link/Port and ordered BRC-provenance lift is a separate unresolved objective.

Attribution of predecessor: Researcher EM-X6-B1684F, historical SID MCP-04016ce373004d3e80f6bff85d689693, Activity RA-6F2C09233DC4F142A2F7795A. Current native authorization is determined by live control, not these historical public identifiers.
