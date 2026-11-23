# R762JU — Repair of four-singleton pencil exceptions (Port–Euler)

2026-11-23 Asia/Shanghai | New independent constructive pencil lemma: exact arithmetic, locally checked. Strengthened R762JT corollary: AUTHOR_PROVED / NOT_REVIEWED (relies on archived non-pencil finite lemmas). This concerns only the **composite unsigned Port–Euler observation model**, not a P000 signed Cell/path/branch/time or BRC lift.

**Fixed science/provenance:** R762JT, draft PR #2990 at \`6fda34681d94d915894ec5f1c32d1e3654102865\`, \`research_notes/portable_direct/R762JT_PORT44_T7D10S3_UNIFORM42.md\`. No rebasing or editing that scientific input.

## Model and theorem

Let A={0,1,2,3,4,5}, P=C(A,2) be the 15 Ports, S=C(A,3) the 20 colors. A color abc contributes one edge between two different Ports in {ab,ac,bc}; parallel edges are allowed. N_(p,V)(n)>0 means a connected undirected colored multigraph with precisely n_s edges of each color, positive even degree at precisely the vertices V, and a prescribed Euler circuit starting at p in V.

A four-color **pencil** about Port ab is D_ab={abc:c in A\{a,b}}. Let M be any matching of inactive Ports on axes disjoint from ab, so |M|<=2, and V=P\M.

**JU.1, unconditional pencil repair.** If n_s=1 for s in D_ab and n_s>=2 for every other color, then N_(p,V)(n)>0 for **every** p in V. The statement applies to all finite integer n_s>=2, not just the 42-event section.

### Proof

All (ab,M) with these properties reduce under S6 to: (ab=01,M=empty), (ab=01,M={23}), (ab=01,M={23,45}), denoted m=0,1,2. A color with exactly two active endpoints is forced to use their joining edge; its positive events create 15,10,6 forced components respectively. Port 01 is an isolated forced component, because all colors containing it are the four singleton pencil colors. Let W=V\{01}.

The **non-pencil flexible colors** (three active endpoints, not in D_01) have a triangle-side graph connected on W. The spanning-tree certificates below prove this directly: 13,12,11 edges for m=0,1,2. Hence their available local pair-boundaries span the full even GF(2) space E(W).

The same colors admit a rainbow tree after contracting the forced components **within W**. There are 14,9,5 such contracted vertices, connected by respectively 13,8,4 certificate edges with pairwise distinct colors. The explicit labeled trees appear below and have been independently checked for legal sides, distinct colors and spanning.

Choose exactly two of the four pencil singletons to touch 01 (choose the edge 01--0c), and the remaining two to use the opposite side (0c--1c). Thus deg(01)=2 and 01 attaches to W. Add all forced edges with their prescribed multiplicities; their total degree-boundary on W, together with the four singleton boundaries, is even, i.e. b in E(W).

Express b as a sum of pair-boundaries from the non-pencil flexible-color spanning tree; group terms by color. On a triangle (u,v,w), a flexible color with multiplicity >=2 realizes any of four parity vectors 0,uv,uw,vw while preserving a selected rainbow-side endpoint connection. With designated side uv:
- multiplicity 2, parity 0: uv+uv; parity uv: uw+wv; parity uw: uv+vw; parity vw: uv+uw.
- multiplicity 3, parity 0: all three triangle sides; parity xy: xy plus two copies of uv.
- any higher multiplicity: add pairs of uv copies, preserving parity and endpoint connectivity.

Choose each flexible-color multiset according to its assigned parity. Every vertex of W has even total degree, the color-distinct rainbow connections keep W connected through forced components, and the two pencil incident edges attach vertex 01, now with even positive degree. Inactive Ports receive no edge. Exact event multiplicities are preserved. Euler's theorem supplies a circuit with any p in V. QED.

## Explicit exact finite certificates

Notation \`abc:uv-vw\` means use color abc's side joining Ports uv and vw. Every listed edge is a legal triangle side; certificates are only for the three canonical cases, and S6 transports them to all allowed (ab,M).

**Rainbow quotient trees (all colors distinct):**

- m=0 (13 edges): 034:04-34, 135:13-35, 234:23-34, 235:23-35, 023:03-23, 035:03-05, 134:13-14, 245:25-45, 025:05-25, 124:12-24, 145:15-45, 123:12-23, 024:02-04.
- m=1 (8 edges): 035:03-35, 025:05-25, 135:13-35, 034:03-04, 045:04-45, 145:15-45, 345:34-35, 124:12-14.
- m=2 (4 edges): 124:12-14, 024:02-04, 034:04-34, 135:15-35.

**Parity-spanning trees on W (colors may repeat):**

- m=0 (13 edges): 023:02-03, 024:02-04, 025:02-05, 023:02-23, 024:02-24, 025:02-25, 034:03-34, 035:03-35, 045:04-45, 123:23-12, 123:23-13, 124:24-14, 125:25-15.
- m=1 (12 edges): 024:02-04, 025:02-05, 024:02-24, 025:02-25, 034:04-03, 034:04-34, 045:04-45, 035:05-35, 124:24-12, 124:24-14, 125:25-15, 134:34-13.
- m=2 (11 edges): 024:02-04, 025:02-05, 024:02-24, 025:02-25, 034:04-03, 034:04-34, 035:05-35, 124:24-12, 124:24-14, 125:25-15, 134:34-13.

**Construction/check:** For any chosen six triple colors outside D_01, set those counts to 3 and the other ten to 2. Prescribe the four singleton edges as above and every forced edge repeated according to its color. Compute the remaining even parity b on W. Root the listed parity tree, peel leaves: for each vertex with odd residual parity, toggle the tree edge to its parent, grouping chosen boundaries by flexible color. Realize each flexible color by the multiplicity-2/3 recipes, using its fixed rainbow side when listed. Check every color count, exactly 42 total events, positive even degrees on V, zero degrees on M, and BFS connectedness.

A locally executed pure-Python standard-library checker independently rebuilt the geometry and the two fixed trees, then constructed and validated **every C(16,6)=8008 inventory for each of m=0,1,2: 24024/24024 PASS**. The numeric coverage validates that 42-event regime; the universal >=2 theorem is by the written construction argument. Results were recorded in local \`R762JU_PENCIL_EVIDENCE.json\` and \`R762JU_PENCIL_PARITY_REPAIR_VERIFY.py\`; GitHub publication of this note alone does **not** claim those two local files were uploaded.

## Corollary and scope

In R762JT, an inventory of histogram (7 triple,10 double,3 singleton,0 absent) has 44 events. Reducing **any** one of its seven triple colors by two leaves exactly four singleton colors and 42 events. If those colors make an *R762JT exceptional pencil*—its common Port is active and disjoint from inactive Ports—the new JU.1 theorem supplies a direct connected Euler construction. Otherwise, including a combinatorial pencil centered on an inactive Port, the previously documented R762JT finite GF(2)-parity and rainbow-tree nonexceptional lemmas cover it. **Conditional on the validity of those prior finite lemmas, all seven triple reductions succeed**, strengthening the earlier lower bound of six.

The same synthesis applies to all-positive inventories with <=4 singleton supports and all other supports of multiplicity >=2, with an inactive-Port matching. It consolidates the 44-event histograms (4,16,0,0), (5,14,1,0), (6,12,2,0), (7,10,3,0), subject to the R762JT finite lemmas. It does **not** establish the overall 44→43 global reduction, since other histogram types remain open.

**Next:** independently audit R762JT's non-pencil finite lemmas; then test five-singleton support inventories, particularly the (8,8,4,0) 44-event class after a reduction, and determine if the quotient-tree/parity principle extends or admits an exact obstruction. Separately retain the typed P000 signed-path/BRC residual-faithfulness lift as an open research question.

**Review:** AUTHOR_PROVED / LOCAL_EXACT_FINITE_VERIFICATION / NOT_REVIEWED. No Source Result/Review or formal mathematical admission asserted.
