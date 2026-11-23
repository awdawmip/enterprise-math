# R762JY — Joint double/triple parity repair: complete four-slice 42-event theorem

2026-11-23 · Author-side **finite exhaustive constructive proof** · **NOT_REVIEWED**.
Parent scientific lineage: R762JX, `b5ebd79873bb2f0e732c1b1b5d3578bcfd458108`, Draft PR #2999. P000 frozen science unchanged.
This is the *unsigned composite six-axis Port–Euler observer*; no signed primitive P000 / BRC history preservation is asserted.

## Exact object and theorem

Let A={0,1,2,3,4,5}; the 15 composite Ports are P=choose(A,2), and the 20 event colors are S=choose(A,3). Color abc permits an unoriented edge joining any pair among its three Ports ab,ac,bc. Let M be a matching of 0–3 inactive Ports and V=P\M. Every color retains at least two active Ports. An inventory n has a 42-event Euler realization if a connected multigraph on V has exactly n_s legal edges of color s, strictly positive even degree at each v∈V, and degree zero on M.

Fix five singleton colors D⊂S and seven triple colors T⊂S\D. Set n_s=1 on D, n_s=3 on T, and n_s=2 otherwise; total 5+21+16=42. Index Ports and colors in lexicographic order. The four fixed (M,D) representative slices are:

| | M (Port indices) | D (color indices) |
|---|---|---|
| 0 | () | (0,1,2,3,4) |
| 1 | (0) | (4,5,6,7,8) |
| 2 | (0,9) | (5,6,7,8,9) |
| 3 | (0,9,14) | (5,6,7,8,11) |

**Theorem JY.2.** For each of these four fixed representatives, *every* T of size seven chosen from the other 15 colors admits a connected 42-event Euler realization starting at **any** active Port. The 25,740 cases are exhausted exactly. The first three slices each have 6,435 directly constructed witnesses; the fourth has 6,171 direct witnesses plus 264 additional witnesses using double-edge repetition. All 25,740 witness graphs were independently property-checked with exact integer assertions.

## Structural theorem JY.1: joint parity correction

Form G_F on V from all three candidate sides of every three-active, non-singleton color. Contract its components to obtain C. Form H_T from the candidate sides of all three-active colors in T, with component partition Q; Q may refine C. For an event edge uv set ∂_Q(uv)=e_{Q(u)}+e_{Q(v)} over GF(2).

Assume we can (i) pick one legal edge e_s for each singleton s∈D so that all fixed two-active non-singleton edges and these five choices connect the G_F component quotient; and (ii) for each three-active *double* color select one of its three sides h_s such that

`Σ_{s∈T, two-active} ∂_Q(fixed_edge_s) + Σ_{s∈D} ∂_Q(e_s) + Σ_{s double, three-active} ∂_Q(h_s) = 0`.

**Then the inventory is Euler-realizable with every active degree positive even.**

**Proof.** Give each forced two-active color its unique side repeated n_s times. Give each singleton its selected side. For each flexible double color take the *other two* sides of its triangle: their parity boundary equals ∂h_s and they span all three Ports. For each flexible triple color take all three sides once, initially parity zero and spanning all three Ports. Thus every flexible non-singleton color spans its three active vertices. Their union connects each G_F component internally; condition (i) connects those components externally. The resulting multigraph is connected and every active Port has positive degree.

By condition (ii) its parity has zero image on Q; hence each Q component carries even parity. The full triple-color side boundaries span the even GF(2) parity space on each Q component because their candidate graph H_T is connected there. Distribute the required parity correction among the full triple colors. In a triangle, any sum of candidate side boundaries is either zero or a single side boundary. For zero use its three distinct sides; for ∂(uv) use one uv edge plus two copies of a *different* side. Both use exactly three events, have the specified parity, and keep the triangle connected. Therefore all odd degrees can be cancelled without changing multiplicities, positive degrees or connectivity. Euler's criterion proves the claim. □

The condition is strictly more permissive than R762JX's requirement that full triple colors alone span each G_F component: flexible double colors can carry parity across distinct H_T components.

## Exact finite proof of the four slices

The self-contained source/extraction bundle `R762JY_EXACT_REPRO.py` generates the original readable `R762JY_COMPLETE_EXACT_VERIFY.py`; its SHA-256 is `93750fd254b07919fe1bdcf6fd13a7768e4d5bdf7b7f7c627cf96a81e0925eb4`. Run the extractor with `--extract-source`, then run the decoded script using Python 3.10+ standard library.

For each representative (M,D), the program enumerates all C(15,7)=6,435 T choices. For the first construction it enumerates all five singleton legal-side choices connecting the G_F quotient, computes the GF(2) parity boundary on Q, and uses exact XOR dynamic programming to choose sides for all flexible double colors. When the target boundary is reachable, theorem JY.1 constructs and checks a full witness. The counts are 6,435; 6,435; 6,435; 6,171 respectively, totaling 25,476.

Only 264 targets, all in slice 3, require another construction. For slice 3 the only three fully active non-singleton triangle colors are 12, 13, 14. For each of the 264 targets, the second algorithm enumerates all five singleton side choices and all locally legal 2-edge or 3-edge multisets for those three colors, including double-color repetition on one side (which gives zero parity but does not necessarily span the third Port). It finds a full valid Euler graph in **every** case. The actual graph, not a spanning proxy, is checked.

A separately written checker in the same source reconstructs all 15 Ports, all 20 allowed color edge sets, the exact 42 events and per-color multiplicities, zero inactive degree, positive-even active degrees, and full connectedness by DFS, then approves *each of the 25,740 graphs*. No floating approximations or solver dependencies enter. The archive is reproducibly generated with `--archive`. Length-framed canonical serialized witness-stream SHA-256:
`62a2af0f72be9b20a1e4279977d3a0012b5156f8845b849201f0a26edb82f0d9`.

| Inactive Ports | Joint double/triple | Double-repeat repair | Verified total |
|---|---:|---:|---:|
| 0 | 6,435 | 0 | 6,435 |
| 1 | 6,435 | 0 | 6,435 |
| 2 | 6,435 | 0 | 6,435 |
| 3 | 6,171 | 264 | 6,435 |
| Total | **25,476** | **264** | **25,740** |

## S6 transfer and 44→42 source reinflation

Every six-axis *label permutation* preserves this composite incidence model, degree parity, connectivity and Euler property. An exact 720-permutation calculation yields orbit sizes of the four (M,D) representatives equal to **180, 180, 180, 360**. The orbits are disjoint by the number of inactive Ports. Every T in each orbit is transported from one of the 6,435 representative configurations by the inverse axis permutation. Thus at least
`(180+180+180+360) × 6435 = 5,791,500`
**distinct labeled 42-event target inventories** are realized. This extension uses a proved symmetry, not 5.8 million separate program executions.

Choose any of a target's five singleton colors j and add two copies of its chosen event edge. Degrees increase by 2 at each endpoint, all Euler requirements persist, and the inventory becomes a valid 44-event source with (8 triple, 8 double, 4 singleton) colors. Removing precisely those two j-events recovers the target. Therefore the covered orbits yield **28,957,500 labeled, *marked* 44→42 compression instances** (M,D,T,j). This does not assert that the *unmarked* 44 sources are all distinct.

## Scope, provenance, and next question

These are author-side proofs and exact finite checks; independent Driver review is **NOT_REVIEWED**. P000 native six-space dimensions, three-dimensional slices, signed primitive three-force balance, ordered BRC provenance and allowed native transports are unchanged. The model uses a separate 15-Port composite graph; graph-edge parity is not a physical primitive two-force balance.

The next task is to enumerate new, non-equivalent (M,D) orbits for the remaining (8,8,4,0) 44-event class, distinguishing the existence of *some* removable triple from removability of *every* marked triple. Eventually construct a separate signed X6 Cell/Link/Port/BRC source-faithful lift under its actual permitted operations.
