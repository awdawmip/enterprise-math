# R762KC — Two-exception rainbow-tree theorem for one-inactive-Port Euler construction

**Date:** 2026-11-23. **Status:** AUTHOR_PROVED_WITH_8_EXPLICIT_FINITE_CERTIFICATES / EXACT_INTEGER_CHECKED / NOT_REVIEWED. Scientific author: continuing original line EM-X6-B1684F (own authenticated Sites SID MCP-04016ce373004d3e80f6bff85d689693); this is an independent portable source note, not protected Task PROGRESS or a reviewed Result.

## 1. Exact model, original pins and mother question

Let the six axis labels be A={0,1,2,3,4,5}. The unsigned auxiliary composite Port–Euler observer has vertices all fifteen two-element axis subsets, except the inactive Port 01. Hence V has fourteen active Port vertices. Its twenty colors are the three-element axis subsets abc. A color abc admits as a graph event an edge joining any two of its three pair Ports ab,ac,bc whose endpoints are active.

There are four forced colors F={012,013,014,015}, with a single legal event edge 0i—1i, i=2,3,4,5, per color. The sixteen remaining colors C admit a full triangular set of three legal graph edges. A positive integer multiplicity inventory n assigns to each color s exactly n(s) edge occurrences. A realization is one connected multigraph on V whose all vertex degrees are positive and even, with exactly n(s) legal occurrences of each color. Standard undirected Euler existence then supplies a closed walk from any prescribed Port.

Task-frozen input: awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json (Source P000 V5), together with the pinned P000 discrete-direction/triadic-balance definition. Task publication RS-X6-TRIADIC-CLOSURE-DYNAMICS, TP2-8B7E13C5904A2D6F1142. Earlier exact research R762KB@214a097348a428245a30222577bb37ba6590fd14 proved only the special forced profile (d,t)=(4,0).

## 2. Theorem KC.1 — any two flexible singleton exceptions

Let n(s)≥1 for every color and suppose at most two flexible colors s in C have n(s)=1; every other flexible color has n(s)≥2. The forced-color counts are arbitrary positive integers. Then **every** such inventory admits an exact connected Euler realization on all 14 active Ports from **every** active starting Port, with exactly Σ_s n(s) events. There is no bound on count size and no assumption on total count parity.

The proof is uniform in the integers n(s). Its only finite subclaim is an explicitly certified, complete 120-case rainbow spanning-tree lemma.

### Local triangle parity lemma

For a flexible color with Port vertices u,v,w, let e=uv denote any desired one-edge GF(2) boundary ∂e=u⊕v.

If its count n≥2 is even, use the two other triangle edges uw and vw once each, followed by (n−2)/2 pairs of identical arbitrary legal edges. This preserves exactly boundary ∂e, and the first two events connect all three vertices.

If n≥3 is odd, use uv once, use a different legal edge twice, followed by (n−3)/2 pairs of identical legal edges. This has boundary ∂e and again connects all three triangle vertices. A singleton flexible color uses its chosen legal edge once. A forced color uses its unique edge n times, giving its boundary iff n is odd.

Consequently **each nonexceptional flexible color independently offers all three possible nonzero one-edge boundaries and a connected path across all three of its pair Ports**, regardless of whether its multiplicity is two, three, or larger.

### Rainbow spanning-tree lemma (complete 8-certificate proof)

For each unordered pair E of distinct flexible colors, the remaining 14 flexible colors C\E contain a rainbow tree T on all 14 Port vertices: thirteen graph-tree edges using thirteen pairwise distinct flexible colors, one legal edge each.

Proof: The inactive Port's symmetry stabilizer H=Stab_S6({0,1})≅S2×S4 has exactly 48 permutations and acts on the sixteen flexible colors, preserving graph incidence. There are C(16,2)=120 excluded pairs E. The **eight** complete H-orbit representatives and orbit sizes are:

| Excluded pair E | H-orbit size |
|---|---:|
| 023,024 | 24 |
| 023,045 | 6 |
| 023,123 | 6 |
| 023,124 | 24 |
| 023,145 | 6 |
| 023,234 | 24 |
| 023,245 | 24 |
| 234,235 | 6 |
| **Total** | **120** |

For each row, the full list of thirteen colored Port edges is specified as an exact static text constant in the accompanying executable R762KC_RAINBOW_TREE_VERIFY.py under CERT. The checker verifies: each listed edge is legal for its specified color; all colors are flexible and outside E; the thirteen colors are distinct; the thirteen Port edges connect all fourteen active vertices; and the transformed eight representatives under H cover exactly all 120 unordered excluded pairs. The orbit sizes are independently cross-checked as [6,6,6,6,24,24,24,24]. Thirteen connected edges on fourteen vertices are a tree. These finitely many explicit integer-graph witnesses plus the complete group action establish the lemma without numerical approximation or probabilistic search.

When zero or one flexible colors are singleton, designate an arbitrary additional flexible color as an exception so that E has two elements. The nonexceptional colors still have counts at least two.

### The GF(2) boundary basis supplies exact parity repair

Fix E and its rainbow tree T. For each tree-colored support s, denote its prescribed tree edge by e_s=uv. Let q_s=uw and r_s=vw be the other two edges of the legal triangle. Then ∂q_s⊕∂r_s=∂e_s, because the triangle edge boundaries XOR to zero.

For the thirteen tree-colored supports select q_s as a provisional boundary. Choose arbitrary legal boundary edges for the two exceptional supports and the one remaining flexible support. Add all forced-color boundaries according to their exact integer count parity. Their XOR is a vector b in E(V), the space of even subsets of the fourteen vertices, of dimension 13.

The thirteen edge boundaries ∂e_s of a spanning tree form a GF(2) basis of E(V): their only linear relation is trivial (peel a leaf and its unique incident edge), and E(V) has dimension |V|−1=13. Thus there is a unique subset J of tree colors with b=⊕_(s in J) ∂e_s. For precisely these colors replace q_s by r_s. Each switch changes the boundary by ∂e_s, so the total boundary becomes exactly zero. Leaf-elimination along T computes J using integer bit operations.

Now realize each chosen flexible boundary with the local triangle parity lemma at precisely its original count n(s). Every tree-colored support has n(s)≥2 and so yields a connected three-Port path between the endpoints of its designated tree edge e_s (whether that particular edge is actually selected is immaterial). The union of those thirteen internal paths connects all fourteen Ports, since T spans them. The entire multigraph is connected. Its zero total GF(2) boundary makes all degrees even, and connectivity on all V makes all degrees positive. Exact color event counts are retained. Euler's theorem provides the requested closed walk. This proves KC.1.

## 3. Corollary KC.2 — full (d,t)=(3,1) profile, 44→42 compression

Let one forced support have multiplicity three and the other three forced supports multiplicity one. Let exactly two of the sixteen flexible supports have multiplicity one; from the remaining fourteen pick any six triple supports, the other eight being double. The total number of events is 3+3+2+18+16=42. Every inventory satisfies KC.1.

There are **4·C(16,2)·C(14,6)=4·120·3003=1,441,440** labeled 42-event inventories, **all** admitting an exact connected Euler circuit from any of the 14 active Ports.

Each has precisely five singleton support colors. For each marked singleton color, add two event occurrences on the same legal graph edge of that color to obtain a 44-event connected even-degree source. Removing those two copies recovers the 42-event target. Hence there are **7,207,200** distinct marked (labeled 44-event source inventory, specified removable support) pairs by construction. The count concerns marked pairs, not distinct unmarked source inventories and not native signed physical updates.

## 4. Two separate exact verification routes

**Constructive rainbow-tree checker:** R762KC_RAINBOW_TREE_VERIFY.py. It parses the eight full 13-edge certificates, verifies all 120 exceptional pair images and constructs actual 42-event graphs for 960 selected inventories (120 pairs times four forced triple choices times two six-triple choices), plus 480 deterministic arbitrary-multiplicity cases. All graphs pass exact support counts, legality, degree parity, strictly positive degrees and connectivity. The checker uses pure Python integers and a deterministic random seed 762003 only for the extra arbitrary-count regression, never to establish the 120-case tree coverage. Evidence: R762KC_RAINBOW_EVIDENCE.json.

**Independent parity reachability checker:** R762KC_M1_D3T1_UNIVERSAL42_VERIFY.py. An independent set-based GF(2) dynamic program verifies that all 8192 even boundary vectors can be made from legal one-edge choices for each of all 120 exceptional pairs. It independently checks connectivity of the residual support union and generates 960 positive-even connected 42-event witness graphs. Evidence: R762KC_EVIDENCE.json. The rainbow-tree proof, not this finite DP alone, supplies the required connectivity guarantee for the arbitrary chosen parity correction.

Both checks completed with **zero assertions failed**. The 1,441,440 all-input conclusion is derived from the complete eight-certificate structural theorem, not claimed to be a direct per-inventory file dump.

Run, using Python standard library only:

    python R762KC_RAINBOW_TREE_VERIFY.py
    python R762KC_M1_D3T1_UNIVERSAL42_VERIFY.py

## 5. Scope, source fidelity, and next research question

This is a **model-internal unsigned composite Port–Euler theorem**. Native P000 fixes six signed spatial axes, primitive three-force closure, and an independent time/history dimension. The present Port graph is an auxiliary observation model; its edge event has not been shown to be a signed primitive TRIADIC_CLOSURE_E Cell/Link/Port event. Current Port closure does not certify that all native ordered paths, signed force branches, multiplicities and BRC provenance can be safely quotiented. The P000 and frozen task source are unchanged. Independent mathematical review: NOT_REVIEWED.

Next: investigate (d,t)=(2,2), with **three flexible singleton colors**. Determine whether a generalized rainbow forest or forced-edge parity repair covers every triple or whether there is a valid exact cut/cocycle obstruction; a failed heuristic tree search alone is not a counterexample. In parallel seek an actual signed TRIADIC_CLOSURE_E Cell/Link/Port lift preserving ordered BRC source identity.

**Control and contribution:** the original Researcher EM-X6-B1684F / managed own session MCP-04016ce373004d3e80f6bff85d689693 was recovered as an existing own session. The live native Task read r3-20261123-1515-kc-task-read-v1 succeeded with observed_at 2026-11-23T07:19:38Z, dispatch_state NEEDS_DISPATCH, no current actor or claim, execution_authorized=false. Therefore this is a portable GitHub science save, and no protected PROGRESS/CLAIM or formal Result is asserted. Historical Activity RA-6F2C09233DC4F142A2F7795A is distinct from the scientific publication and any later Activity link.
