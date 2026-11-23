# R762KK — Projection-pair obstruction formula and adaptive upgrade minimum

Date: 2026-11-23. Status: AUTHOR_PROVED_FROM_PREDECESSOR_FINITE_THEOREMS / EXACT_CHECKED / NOT_REVIEWED.
Researcher: EM-X6-B1684F; activity: RA-6F2C09233DC4F142A2F7795A; source session: MCP-04016ce373004d3e80f6bff85d689693.

## Scope and immutable scientific input

Unsigned auxiliary six-axis Port–Euler graph, not the native signed P000 dynamics. Inactive Ports: 01,23,45. The twelve active Ports are 02,03,04,05,12,13,14,15,24,25,34,35 (in that bit order). The eight flexible three-axis supports are the Boolean cube (i,j,k) in {0,1}^3, representing supports (i,2+j,4+k). The other twelve supports carry arbitrary positive integer multiplicity and have one forced legal edge each.

A flexible support has one event unless upgraded, in which case its event multiplicity is any integer at least two. A realization retains all support multiplicities, connects all twelve active Ports and gives every active Port strictly positive even degree. Let F be the nine-dimensional GF(2) boundary space of the twelve forced edges, so |F|=512. Let W be the all-one twelve-Port boundary, decimal 4095.

Frozen P000 source: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json. Prior mathematical sources:
- R762KH, exact 17 one-upgrade holes: awdawmip/enterprise-math@09972bfdb89fde5846768a3688017f7387a17311:research_notes/portable_direct/R762KH_M3_SHARP_THREE_UPGRADE_EULER_THEOREM.md.
- R762KI, four-hole affine plane E_U for each two-support upgrade, with three exact orbit templates: awdawmip/enterprise-math@211070ca0d144092298fe3883fd1a16712a1a021:research_notes/portable_direct/R762KI_M3_TWO_UPGRADE_AFFINE_OBSTRUCTION_THEOREM.md.
- R762KJ, 47 no-upgrade holes and equality with the union of 28 two-upgrade planes: awdawmip/enterprise-math@7111f9c409ca09dac3bf51ac329f1479624fd79c:research_notes/portable_direct/R762KJ_GEOMETRIC_47_HOLE_THEOREM.md.

The prior claims are author-side exact finite checked, not independently reviewed. R762KK explicitly takes their proved finite statements as dependencies, and independently checks its formulas against exact construction/parity enumeration.

## Theorem KK.1 — Closed projection-pair formula (zero DP lookup per query)

For cube support u=(i,j,k) define three projections
A(u)=(i,2+j), B(u)=(i,4+k), C(u)=(2+j,4+k), each a Port.
For an unordered pair U={u,v}, define the three twelve-bit masks
P_G(U) = bit(G(u)) XOR bit(G(v)), G in {A,B,C}.
Here bit(Port) is the power of two in the active-Port bit order; a coincident projection makes P_G=0.

Let d be the Hamming distance between the two cube vertices. The exact set E_U of forced boundaries that **cannot** be repaired by upgrading precisely U is:

- d=1: exactly one of P_A,P_B,P_C is zero. Write the two nonzero masks as X,Y. Then
  E_U = { W, W XOR X, W XOR Y, W XOR X XOR Y }.
- d=2 or 3: all three masks X=P_A, Y=P_B, Z=P_C are nonzero. Then
  E_U = { W XOR X, W XOR Y, W XOR Z, W XOR X XOR Y XOR Z }.

The four masks are distinct and form an affine GF(2) two-plane. Consequently the direct formula evaluates E_U using only the two cube vertices, their three projections and XOR operations, without an eight-support parity DP.

**Proof.** The group preserving inactive matching 01|23|45 is the 48-element automorphism group of the three-cube and has precisely the three pair orbits d=1,2,3. The expression is equivariant under flipping/permuting the cube coordinates because projections and bit permutation commute. For the three representatives U={024,025}, {024,035}, {024,135}, direct substitution yields respectively the exact prior R762KI exception sets (decimal):
d=1: {3315,3327,4083,4095}; d=2: {1776,1791,4083,4092}; d=3: {1626,1791,3963,4062}. R762KI establishes those exact sets by exhaustive connected parity-state calculation with its local integer-count extension. Equivariance completes all 28 pairs. The independent R762KK checker separately reconstructs connected edge-event states and verifies all 28 outcomes.

## Theorem KK.2 — Geometric union with direct combinatorial enumeration

The union of all 28 E_U equals the following disjoint four families:
1. W itself: 1 vector.
2. W XOR Q, where Q is any two-distinct-Port mask confined to one of the three four-Port grids: 3*binom(4,2)=18 vectors.
3. W XOR P_G(U) XOR P_H(U), where d(U)=1, G,H are the two projections with nonzero masks: 12 vectors.
4. W XOR P_A(U) XOR P_B(U) XOR P_C(U), where d(U) is 2 or 3: 12+4=16 vectors.

Hence the union contains exactly 1+18+12+16=47 forced boundaries. By the prior KJ exact union theorem, these are precisely the no-upgrade holes.

**Combinatorial justification.** The three sets have distinct numbers of non-full grids, so the families are disjoint. Any two distinct cells of a given two-coordinate grid admit precisely four pairs of cube lifts; thus every two-cell mask Q is represented. The distance-one pairs are in bijection with their 12 two-grid masks because the full grid reveals the changed coordinate and the other two projected lines recover the fixed coordinate values. For d>=2 the three unordered two-coordinate projections determine the two cube vertices up to exchanging u and v, hence the corresponding 16 three-grid masks are distinct.

The incidence multiplicities for a hole b across two-upgrade planes are immediate: W appears in all 12 distance-one planes; each of the 18 one-grid-complement holes appears in four planes (four choices of paired cube lifts); each remaining two- or three-grid hole appears in exactly one plane. Total 12+18*4+28=112=28*4.

## Theorem KK.3 — Adaptive upgrade threshold is exactly 0,1,2

For a fixed flexible support u, let E_u denote the forced boundaries impossible after upgrading *only* u. Then

  E_u = union_{v != u} E_{ {u,v} },  |E_u|=17.

The 17 points consist of W, nine single-grid-complement points, three two-grid points coming from the Hamming-one neighbors of u, and four three-grid points coming from its Hamming-two/three neighbors.

**Proof.** The local parity boundary choices of multiplicity >=2 are {0,AB,AC,BC}, while a singleton has {AB,AC,BC}. A 1-event edge can be replaced by two distinct triangle edges with the same XOR boundary and at least as much intercomponent connectivity. Thus E_{u,v} is contained in E_u for each v. By KK.1 the union over v has exactly 1+9+3+4=17 distinct members. R762KH established |E_u|=17 for all eight u by exact connected state calculation. Inclusion and equal cardinality yield equality. The R762KK checker verifies the connected states directly for all eight one-upgrade inventories.

For any forced boundary b in F, if the upgraded support set may be selected *after* knowing b, the minimum number of upgrades needed is:
- 0 for exactly 465 boundaries outside the 47-hole set;
- 1 for exactly 46 boundaries in the 47-hole set other than W;
- 2 for the unique boundary W=4095.

Indeed W belongs to E_u for every u because every u has a distance-one neighbor, whereas W is absent from every E_{u,v} of Hamming distance >=2. For the other holes, the number of one-upgrade choices which **fail** equals 4 for the 18 one-grid-complement holes and 2 for the remaining 28. So there is always a successful single-upgrade support.

This distinguishes **adaptive choice conditioned on the forced boundary** (worst case two upgrades) from R762KH's **fixed upgrade set working uniformly for all boundaries** (sharp threshold three).

## Exact computation and reproduction

Execute: python R762KK_PROJECTION_PLANES_VERIFY.py (Python standard library only).

The checker independently computes the forced space (512), all 28 two-upgrade parity DP reachable sets, and connected event-state sets tracking boundary XOR and component-edge-type OR; verifies each against KK.1, independently enumerates all 3^8 singleton configurations, checks the 47-hole union, all 8 one-upgrade connected and parity states against KK.3, and checks the incidence distributions and adaptive minima. Every assertion passed in the local run on 2026-11-23; exact integer arithmetic, no sampling.

## Evidence level and continuation

AUTHOR_PROVED_FROM_PREDECESSOR_FINITE_THEOREMS / EXACT_CHECKED / NOT_REVIEWED. The closed obstruction formula, incidence and adaptive minimality are new corollaries conditional on previously saved KI/KJ/KH finite results, plus this run's independent exact calculation. No native signed Cell/Link/Port or ordered BRC provenance lift is claimed.

**Next scientific question:** Give a standalone algebraic proof of the three representative pair-hole templates from local cube-color parity constraints, avoiding even their finite DP. Study whether a similar projection-pair formula survives one or two inactive Ports or additional structured forbidden-Port patterns. Independently prove that a native signed BRC-observer projection preserves the ordered/path/branch information needed to transport any Euler result.
