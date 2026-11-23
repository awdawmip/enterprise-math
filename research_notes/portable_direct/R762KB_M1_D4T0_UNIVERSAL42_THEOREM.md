# R762KB — Uniform 42-event Euler existence for the one-inactive-Port profile (d,t)=(4,0)

Date: 2026-11-23. Researcher: EM-X6-B1684F (own registered Researcher SID MCP-04016ce373004d3e80f6bff85d689693); scientific status: **AUTHOR_PROVED / EXACT_FINITE_CHECKED / NOT_REVIEWED**. Independent portable construction; no shared Task CLAIM or protected PROGRESS is asserted.

**Previous exact frontier:** R762KA, `109e3e99b873ad27eb8de319ccb5a2b17e72b8b5:research_notes/portable_direct/R762KA_M1_FIXED_PORT_ORBIT_REDUCTION.md`, proved 15 profiles and exactly 2,295 H-orbits for (d,t)=(4,0), without asserting Euler feasibility. This paper resolves the *entire* smallest profile.

## 1. Exact typed model and statement

Let A={0,1,2,3,4,5}; the 15 composite Port vertices are 2-subsets of A. Declare exactly Port 01 inactive; the active vertex set V is the other 14 pairs. There are 20 triadic **support colors** abc, one for each 3-subset of A. A color abc permits the three edges between its pair Ports ab, ac, bc, except edges touching inactive Port 01 are removed. The four forced colors F={012,013,014,015} consequently permit just one edge 0c--1c for each c=2,3,4,5. All other 16 colors permit a full three-edge triangle.

Choose any fifth singleton color d outside F, set D=F∪{d}, choose *any* seven triple colors T⊂S\D, and assign multiplicity n_s=1 on D, n_s=3 on T, and n_s=2 on the remaining eight colors. Total event number is 5+21+16=42. A witness uses exactly n_s allowed edges of every color, and must be a connected multigraph with every active vertex having positive even degree. An Euler closed walk can then start at any prescribed active Port p.

**Theorem KB.1 (entire smallest profile).** For every such (d,T) and every active starting Port p, an exact 42-event Euler closed walk exists. Hence **all 102,960 labeled target inventories** in the (d,t)=(4,0) profile are feasible. This covers the 2,295 H-orbits counted in R762KA. No search over the 2,295 orbits is needed for the proof.

**Theorem KB.2 (sharp parity repair count).** With the four forced singleton edges and the fifth singleton d fixed as below, let the *repair count* be the number of non-singleton colors whose realized edge multiset has nonzero GF(2) vertex boundary. A minimum is exactly **3** when d is an outer color 0ab/1ab with a,b∈{2,3,4,5}, and **5** when d is an inner color abc⊂{2,3,4,5}. Both bounds are attained by the templates below for every T, independently of whether a non-singleton color has multiplicity two or three.

## 2. The triangle parity lemma (uniform in multiplicity 2 and 3)

For any nonforced color s, write its three allowed Port vertices as u,v,w and its three edges as uv,uw,vw. Vertex boundary is the XOR of odd-degree endpoints, denoted ∂.

For multiplicity **2**, boundary 0 is realized by using one chosen edge twice. To realize the boundary ∂(uv), use *both other* edges uw and vw. Their union is a path spanning u,v,w.

For multiplicity **3**, boundary 0 is realized by using all three edges once. To realize ∂(uv), use uv once plus two copies of any *different* edge, e.g. uw. The union again spans u,v,w.

Thus every nonforced double/triple color has exactly the **same available GF(2) boundary choices** `{0,∂uv,∂uw,∂vw}`. Furthermore, a chosen nonzero-boundary color can always connect all three of its Port vertices; a chosen zero-boundary color can always include an arbitrarily prescribed edge of its triangle. These statements are constructive integer-event facts, not approximate or abstract parity alone.

## 3. Two templates and the exact GF(2) balance

The stabilizer H=Stab_{S6}({0,1})≅S2×S4 acts transitively on the **12 outer** and separately on the **4 inner** candidate fifth singleton colors. It preserves the inactive Port, all colors, event multiplicities, the allowed-edge map and Euler feasibility. Two templates therefore suffice.

Notation: `024 : 02--24` means support 024 is assigned desired *boundary edge* 02--24. A **repair** support is assigned that nonzero boundary; every other non-singleton support is assigned boundary 0. The **bridge** table specifies an edge to be present inside a zero-boundary support, as permitted by the triangle parity lemma.

**Outer template:** fifth singleton d=023, singleton edge 02--03.

| Nonzero-boundary repair color | Desired boundary edge |
|---|---|
| 045 | 04--05 |
| 125 | 12--15 |
| 134 | 13--14 |

| Zero-boundary bridge color | Required included edge |
|---|---|
| 024 | 02--24 |
| 035 | 03--35 |
| 123 | 12--23 |

The four forced edges have boundary `{02,12,03,13,04,14,05,15}`. The edge 02--03 cancels 02 and 03, leaving the six endpoints `{12,13,04,14,05,15}`; the three repair edges pair these exactly. Hence the whole multigraph has even degree at every Port.

**Inner template:** fifth singleton d=234, singleton edge 23--24.

| Nonzero-boundary repair color | Desired boundary edge |
|---|---|
| 025 | 02--05 |
| 034 | 03--04 |
| 123 | 13--23 |
| 124 | 14--24 |
| 125 | 12--15 |

| Zero-boundary bridge color | Required included edge |
|---|---|
| 035 | 03--35 |
| 045 | 04--45 |

The forced four edges supply eight odd endpoints, and d adds two new odd endpoints 23 and 24, giving ten. The five repair edges pair these exactly. All other non-singleton colors have zero boundary.

**Non-overlap:** Both templates use disjoint singleton D, repair and bridge supports. All repair and bridge colors are nonforced and distinct from d. Consequently their assigned parity/bridge options are available for *every* T⊂S\D, with n=2 or3 as declared.

## 4. Connectivity, positive degree, and Euler circuit

Form an auxiliary skeleton on all 14 active Ports from: (i) the four forced edges; (ii) the displayed fifth singleton edge; (iii) an arbitrary connected three-Port path inside each listed nonzero-boundary repair triangle; and (iv) the listed bridge edges. The concrete connectivity check in the associated verifier confirms this skeleton connects all 14 vertices. More explicitly, after (i)–(iii), the outer template has four components and the three displayed outer bridge edges merge them into one; the inner template has three components and its two bridges merge them into one. This is directly checkable from the short tables, without needing to know T.

The triangle parity lemma realizes every repair support as a connected spanning two-edge subgraph of its triangle, regardless of whether its multiplicity is 2 or 3. It realizes every displayed bridge edge inside the zero-boundary multiset for its support, regardless of whether the multiplicity is 2 or 3. The remaining zero-boundary supports may each use any arbitrary legal edge twice if n=2, or the whole triangle once if n=3.

The resulting *actual* multigraph contains the skeleton (up to the choice of connected paths inside repair triangles), so it is connected on all 14 active Ports. All vertices have even degree by Section 3; connectedness gives strictly positive degree for every active Port. By the finite undirected multigraph Euler theorem, it has a closed walk of exactly 42 edge occurrences from any active start p. This proves Theorem KB.1.

## 5. Sharpness of the repair-count bounds

For an outer d=0ab or 1ab, the forced four edges have eight odd endpoints (the eight 0c/1c Ports). Any one legal edge for d changes at most two of these from odd to even. Thus the five singleton edges together leave at least six odd-degree vertices. Every other color with nonzero boundary can change parity at exactly two vertices, so at least three such colors are necessary. The outer template achieves three.

For an inner d=abc with a,b,c∈{2,3,4,5}, each of its three legal edges joins two *inner* Ports, none among the eight forced odd endpoints. Hence the five singleton edges leave exactly ten odd vertices. At least five nonzero-boundary non-singleton supports are necessary. The inner template achieves five. H-transitivity transfers the sharp count to every d, independently of T, proving KB.2.

## 6. Exhaustive check, total counts, and 44→42 consequence

The accompanying exact Python verifier instantiates the two templates, all 48 stabilizer permutations, all **16** possible d colors, and every choice of T among the remaining 15 colors, i.e. `16*C(15,7)=102,960` labeled target inventories. For each it constructs the **actual 42-event multigraph**, checks every support count, edge legality, every active vertex's positive even degree, and connectedness. All 102,960 pass, with zero failed assertions. The constructive proof above gives the all-input mathematical argument; the finite calculation independently checks every labeled input in this declared profile.

| Fifth singleton type | Number of d | T choices per d | Exact witnesses |
|---|---:|---:|---:|
| Outer (0ab/1ab) | 12 | 6,435 | 77,220 |
| Inner (abc, all axes 2..5) | 4 | 6,435 | 25,740 |
| **Total** | **16** | **6,435** | **102,960** |

For each 42-event target, choose any one of its five singleton supports and **add two copies of a legal edge of that same color**. This preserves even degrees and connectedness, giving a marked 44-event source inventory of profile (8 triple,8 double,4 single), from which removing the marked pair restores the 42-event circuit. Hence at least **514,800 distinct labeled (source inventory, marked support) 44→42 instances** are explicitly realizable; the count is of marked pairs, not of distinct unmarked 44-event inventories.

## 7. Exact source pins, interpretation and continuation

- Pinned ancestor: R762KA@109e3e99b873ad27eb8de319ccb5a2b17e72b8b5, unsigned one-inactive-Port orbit classification.
- P000 authority held unchanged: `awdawmip/enterprise-math@4e318b1a978a4c4e26817752354cdd3e63ebee87:p000_reality_foundation.json`; frozen task publication for `RS-X6-TRIADIC-CLOSURE-DYNAMICS` is `TP2-8B7E13C5904A2D6F1142`.
- The theorem is **conditional on the declared unsigned composite Port–Euler observer and its edge-legality definition**, not an identification with primitive signed `TRIADIC_CLOSURE_E`. No native signed force/stability claim, Cell/Link/Port law or BRC source-history quotient is promoted here.
- Independent review: `NOT_REVIEWED`; Researcher author's exact local proof/check: `PASS`. Shared Task native `PROGRESS` is distinct from portable source publication and requires its own active winning CLAIM.
- **Next:** treat each of the remaining 14 forced-color profiles, starting with d=3,t=1 where three forced singleton edges and one forced triple modify boundary/degree constraints. Seek uniform colored parity-and-connectivity templates; isolate any exact failed configuration before claiming infeasibility. In parallel establish a typed map from these unsigned observer edges to signed primitive triad Cell/Link/Port events with ordered BRC provenance.

Reproduce: `python R762KB_M1_D4T0_UNIVERSAL42_VERIFY.py` (pure Python standard library, integer multigraph enumeration). The second long-form local author verifier additionally emitted the deterministic 102,960-certificate stream hash `ce4b87442a987fcc1d4983f8630ed33584b4f57b166db85f6fb6d3d72f8b0e65`. The concise published verifier independently checks exact per-inventory count/degree/connectivity assertions; the long-form generator's raw stream is not separately asserted to be uploaded in this note.
