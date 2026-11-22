# R762IN — Sharp 20-event Port-Euler witness for full-support odd multiplicities

Date: 2026-11-22 (Asia/Shanghai). **AUTHOR_PROVED / EXACT_FINITE_CERTIFICATE_CHECKED / NOT_REVIEWED**.

## Frozen scientific scope

Task: RS-X6-TRIADIC-CLOSURE-DYNAMICS. Frozen P000: a72226e2430ffa4786321ac86e7f0c599d5f0389. Predecessor: [R762IM](https://github.com/awdawmip/enterprise-math/blob/b5e3a6073c54d1bbccd3a5d798887def7243a34c/research_notes/portable_direct/R762IM_K0_EVEN_TAIL_52.md). This is the *composite Port-Euler observer*, not a proof of the native P000 TRIADIC_CLOSURE_E force, time, Cell or rotation laws.

The six axis labels are 0,1,2,3,4,5. There are 15 unordered pair-Ports and 20 unordered triple supports. An event supported on abc chooses an edge of the triangle on pair-Ports ab, ac, bc. The retained observer consists of support positivity, per-support multiplicity parity, exact active Port set, and a specified active starting Port. A legal closed trace is an Euler circuit in a connected even-degree assigned multigraph. Original edge assignment and time ordering are outside this observer.

## Theorem — sharp 20-event core

Let n_S be **positive odd integers for all 20 supports**. For any legal Port-Euler realization with exact active Port set V, and any p in V, there exists a legal 20-event Port-Euler realization with h_S=1 for every support S, exactly the same active set V, and a circuit based at p. Therefore h_S<=n_S and h_S is congruent to n_S modulo 2. All deleted events can be restored by inserting (n_S-1)/2 pairs of parallel edges of the same support S at the edge retained by its 20-event certificate; this preserves support identities, active Ports, even degrees, connectivity and Euler existence. **20 is the minimum** under support-positivity preservation, since all 20 supports require at least one event.

### Classification of possible inactive Port sets

Let M be the inactive pair-Ports. If two inactive Ports intersect in an axis, they have form ab and ac, whose union is an actual support abc. Every allowed edge of its pair-Port triangle touches at least one of ab and ac. Since n_abc>0, that is impossible. Hence M is a *matching* of disjoint edges in K6, of size 0,1,2 or 3.

Conversely, every matching of those four sizes is realized by a connected even-degree 20-event certificate. Four standard matchings are:
M0 = empty; M1 = {01}; M2 = {01,23}; M3 = {01,23,45}. They represent respectively 1, 15, 45 and 15 distinct labeled matchings.

The exact certificate arrays below specify the 20 selected Port edges in lexicographic triple-support order 012,013,...,345. For support abc with Port vertices [ab,ac,bc], digit 0 means edge ab--ac, digit 1 means edge ab--bc, and digit 2 means edge ac--bc.

    M0: [2,1,0,2,2,0,2,0,2,0,0,0,1,0,1,2,2,1,1,0]
    M1: [2,2,2,2,2,2,0,1,0,2,2,2,0,2,2,0,0,0,0,2]
    M2: [2,2,2,2,0,1,1,0,1,2,0,0,1,1,1,2,2,2,2,2]
    M3: [2,2,2,2,0,2,2,0,0,0,0,2,2,0,0,0,2,2,0,0]

For every array, a complete exact graph check verifies: all 20 supports occur exactly once, every chosen edge belongs to its support triangle, all vertex degrees are even, all and only the stated inactive Ports have degree zero, and the active graph is connected. Axis relabeling preserves these properties, and the symmetric group S6 is transitive on matchings of each fixed size. Thus the four finite certificates prove existence for every admissible V; the standard connected-even Euler theorem completes the proof. A separately executed program checks all 720 relabelings of each prototype and all 76 distinct matching cases.

### Counterexample to a load-bearing coverage premise in R762IM

R762IM's finite-check completeness discussion asserts that an inactive Port cannot belong to a support of multiplicity three, hence it counts omitted-Port cases only when all four incident supports have multiplicity below three. **That assertion is false for this observer.** Take the M1 certificate (which omits Port 01), and **triple every selected support edge**. This gives a connected even-degree 60-event realization with n_S=3 for *each* of 20 supports, yet only 14 active Ports; Port 01 is inactive. In the preceding checker, the all-three family T20 was listed as having zero omitted-Port instances. Thus its tally of 3,165 omitted-Port cases is not an exhaustive enumeration of all legal active-Port realizations.

This is a **proof-completeness gap**, not by itself a counterexample to R762IM's 52-event existence theorem. For this particular 60-event witness, an exactly 52-event witness with the same 14 active Ports exists: keep the original 20-event M1 core, triple 16 selected supports and retain one copy in each of the other four. Other histogram families require their own repaired active-set coverage; no further result is inferred without checking them.

## Exact validation and constructive algorithm

The accompanying [R762IN_CHECK.js](R762IN_CHECK.js) requires only exact integer graph operations and four literal arrays. Execute from repo root: node research_notes/portable_direct/R762IN_CHECK.js. It checks 4 prototypes, 2,880 transported witnesses, all 76 distinct matchings (1+15+45+15), and the 60-event omission construction. Its actual local output has status PASS and is retained in [R762IN_EVIDENCE.json](R762IN_EVIDENCE.json). An initial mixed-integer optimization was used only to *discover* these arrays; the final published proof and checker do not depend on an optimizer.

Given V, find its inactive matching M, relabel the appropriate standard 20-event prototype, and insert (n_S-1)/2 same-edge pairs to restore full support multiplicities. For fixed six axes, core generation is constant-size; explicit recovery takes O(sum n_S) operations and preserves the support labels of the original named events.

This is observer-scoped compression, not an equivalence of the full native path, provenance, signed branch, time or Cell state. The previous *universal* 54-event upper bound is unchanged; this result is a sharp proper-subclass theorem. Next: repair all omitted-Port possibilities in the 14 R762IM upper-tail histogram families and verify whether 52 still holds, then address the k>=1 fourfold-bridge extremal families relevant to a universal 53-event bound. Independent review remains NOT_REVIEWED. GitHub publication does not establish a formal Result, CLAIM, PROGRESS, Foundation promotion or P000 revision.
