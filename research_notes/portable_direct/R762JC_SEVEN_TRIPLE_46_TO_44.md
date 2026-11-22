# R762JC — Complete seven-triple 46→44 Port–Euler compression

Date: 2026-11-22 (Asia/Shanghai).
Frozen scientific pin retained: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389; Source P000 V5 unchanged.
Predecessors: R762JA (uniform 46 bound), R762JB (six-triple 46→44), R762IR (GF(2) nonessential-triangle repair).
Status: AUTHOR_PROVED / FINITE_INTEGER_WITNESSES_CHECKED / NOT_REVIEWED.
**Scope:** composite 15-Port/20-support Euler observer, not signed native P000/X6 path, phase, time, order or residuals.

## Statement

Let A={0,...,5}, the 15 Ports P be the unordered two-subsets of A, and the 20 three-axis supports S the unordered three-subsets. An event of support {a,b,c} chooses one of the three edges between Ports ab, ac, bc; parallel repetitions are permitted. An admissible closed history is a connected positive-even-degree multigraph on precisely the active Ports V, admitting a specified Euler-circuit starting Port p. Let N_{p,V}(n)>0 denote existence with support multiplicity vector n.

**Theorem R762JC:** For every n in {1,2,3}^20 with histogram (t,d,s,z)=(7,12,1,0) and N_{p,V}(n)>0, some support j with n_j=3 satisfies

    N_{p,V}(n - 2e_j)>0.

The event number changes from 7*3+12*2+1=46 to 44. The reduced witness retains the exact active Port set, specified circuit start, every positive support, and support-count parity.

## Proof by disjoint cases

**1. Inactive Port restriction.** Every support is positive. If two inactive Ports represented K6 edges sharing an axis, the support triangle on those three axes would have only one active vertex, and therefore no allowed edge. Hence M=P\V is a K6 matching (76 possibilities, including empty).

**2. A triple support contains an inactive Port.** Precisely two vertices of that triangle remain active, so all its three events are copies of their unique allowed edge. Delete two copies. Connectivity and support positivity remain; endpoint degrees decrease by two. As the original degrees are even and at least four, exact positive-even degree and the active set persist.

**3. Seven fully active triple triangles, one nonessential.** Let G(T) be the union of the complete three-edge triangles for the seven triple supports T. If some j is nonessential, the three vertices of triangle j remain mutually connected in G(T\{j}). Replace its three edges by one. The change of GF(2) degree boundary has zero or two odd endpoints, joined by a path in G(T\{j}). Assign each path segment to its unique triangle and realize each triangle's local even boundary by three connecting edges: a three-cycle for zero boundary, otherwise one edge between the prescribed odd pair and two parallel edges to the third vertex. Reassign retained triple supports, leaving double/singleton allocations unchanged. This fixes parity. Every original retained triple edge's endpoints remain connected within its replacement triangle, while the removed triangle's vertices remain connected through the other triples. Original graph connectivity and the precise active set therefore persist.

**4. Fully active, all-essential seven-triangle families.** Enumerate all C(20,7)=77,520 seven-support families. Exactly 23,700 have every triangle essential for the component count of G(T). Under S6 axis permutations they form 55 orbits. For each orbit representative enumerate every inactive matching disjoint from the triple triangle vertices and each of 13 choices for the singleton support outside T. This produces 1,755 representative configurations (715 with zero inactive Ports, 962 with one, 78 with two). Their S6 transports exhaust 741,780 labelled (T,M,singleton) configurations.

For each representative reduce the least-indexed triple j to one event, keep the other six triples at three events, twelve doubles at two events, and the singleton at one event. The companion Python/HiGHS program constructs a 60-entry candidate integer allocation among the three edges of each support. It then verifies with independent **exact integer checks** all 20 support sums, the 44-event total, inactive-Port zero degree, active-Port positive-even degree, and graph connectivity. A disconnected candidate receives an explicit crossing cut and is solved again. The observed execution returned 1,755/1,755 passing allocations; 1,679 required no connectivity cuts and 76 required one. The optimizer is a proposal mechanism, not the proof validator. Each checked integer allocation transports through S6. Any active p is a valid Euler-circuit start.

Together cases 1–4 establish the theorem for all originally legal configurations of this histogram.

## Worked exact two-inactive-Port witness

Order supports and Ports lexicographically and the three possible edges lexicographically within each support. Take T={0,1,2,3,4,6,7}; inactive Port indices M={10,13} (axis pairs {2,4} and {3,5}); singleton support index 5; reduce j=0. The following 60 integer edge counts, three per support, give an explicit 44-event connected Eulerian witness:

    0,0,1, 2,1,0, 0,0,3, 3,0,0, 3,0,0,
    1,0,0, 0,3,0, 0,1,2, 2,0,0, 1,1,0,
    0,0,2, 2,0,0, 1,0,1, 1,0,1, 2,0,0,
    1,0,1, 0,2,0, 2,0,0, 0,0,2, 0,2,0

## Reproducibility

Companion file: research_notes/portable_direct/R762JC_SEVEN_TRIPLE_46_44.py (Python, NumPy, SciPy/HiGHS). Executed locally on 2026-11-22 with the complete finite domain. It printed:

    PASS R762JC: 77,520 subsets, 23,700 all-essential, 55 S6 orbits
    1755/1755 exact integer witnesses; labelled cases: 741780
    inactive cases: {0: 715, 1: 962, 2: 78}
    connectivity cut rounds: {0: 1679, 1: 76}

All integer candidates were checked for the same exact proposition after solver generation. The full individual allocation table is **not included in this note**; the supplied generator reproduces valid witnesses and exact checks. A separate local run also packed the 1,755 allocations into 26,325 two-bit bytes, SHA-256 be9e437311c8f901499973ccaecae2caf3237fd61f21781b139fef3a9eb15519. This is an evidence fingerprint of a local run, not a published independent certificate or acceptance signature.

## Consequence and next question

This establishes another complete 46→44 terminal histogram after R762JB. The overall author-side k=0 upper bound **remains 46**. Open terminal histograms include (8,10,2,0), (9,8,3,0), (10,6,4,0), (8,11,0,1), (9,9,1,1), (10,7,2,1), (10,8,0,2) and high-triple reductions; independently audit the prior uniform-46 lemma and orbit predicates as necessary. The model-internal observer statement does not establish a native signed-P000 history compression or residual-safe lifting.

Portable science publication does not confer shared CLAIM, PROGRESS, Result, or Review authority.