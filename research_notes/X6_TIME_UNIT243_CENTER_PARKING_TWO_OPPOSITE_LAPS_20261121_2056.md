# X6 native time — Unit243: one source-defined INNER centre admits opposite OUTER laps under a conditional signed-Port guard

Date: 2026-11-21 (Asia/Hong_Kong). Status: **AUTHOR_PROVED / EXACT_FINITE_EXECUTED / UNREVIEWED / NOT_ADMITTED**.

Parent: PO-X6-UPPER-STRUCTURE-20260906. Task: RS-X6-NATIVE-TIME-DYNAMICS, publication TP2-91D4A7C2F63805BE21A3. Ordinary-control research lane: chatgpt-research-onhour-enterprise-math-20260923, strictly distinct from control maintenance. Historical original author Researcher EM-X6-FB6990, SID MCP-082892eb480e45dea6d4b9fcc0491034. These historical Source identifiers do not establish a new live CLAIM or protected execution.

## Frozen source and precise distinction from Unit242

Reuse awdawmip/enterprise-math@a72226e2430ffa4786321ac86e7f0c599d5f0389:p000_reality_foundation.json, its signed single-axis primitive adjacency in the six-dimensional Cell torsor, and the frozen Viète OUTER C12 construction. Work in a **chosen relative three-axis slice** of the full six-axis space, with chosen Cell anchor P (not an ontic origin). Set

\[
a=(e_1,e_2,e_3,-e_1,-e_2,-e_3),\quad
x_{2r}=P+a_r,\quad x_{2r+1}=P+a_r+a_{r+1}\quad(r\bmod 6).
\]

The twelve x-values are distinct native Cells, and every cyclic neighbour edge is exactly one signed native-axis step. Unit242 proved that if distinct intact labeled triads can travel *only* along those twelve ring Cells, under serial occupied-source/empty-target moves, each labeled full return must have the same integer winding. The opposing pair (-1,+1) is forbidden **under that ring-only graph**.

The independently authored triad relocation proposal dated 2026-11-18 is a conditional candidate: research_artifacts/mcp/RS-X6-NATIVE-TIME-DYNAMICS/MCP-456b8f22a648400585024ffbcc1c2c94/5a04daccb6795e494dbc/X6_TIME_GUARDED_TRIADIC_RESOURCE_CONFLICT_20261118.md at commit f41c2690daba467ecbde99615a1337e67be46ffd. It does not establish an actual physical Port law or a precision sensor.

## Theorem 1 — exact opposite loops with the existing centre Cell

Add precisely the **already source-defined** relative centre Cell P and its six signed-native spokes P ↔ x_{2r}. Retain all OUTER edges. The result has 13 Cells, 18 undirected native edges and 36 directed links (24 ring plus 12 centre spokes). Give each of two distinct triads its own three intact force-token IDs. A conditional serial whole-triad move is enabled only when its directed signed Port is allowed and its target Cell is unoccupied; it retains source/target, token identities, signed axis, STAR/branch and chronological BRC evidence.

Initially put triad A at x0=P+e1, triad B at x2=P+e2, with P empty. A legal explicit schedule is:

1. A: x0 → P, a -e1 primitive spoke.
2. B completes the original **twelve consecutive forward OUTER edges**, from x2 back to x2, recording L_B=+12.
3. A: P → x0 (+e1); then B: x2 → P (-e2), in that order.
4. A completes the original **twelve consecutive reverse OUTER edges**, from x0 back to x0, recording L_A=-12.
5. B: P → x2 (+e2).

Every target is empty at its move. Every link is a **single** signed native axis; the two complete OUTER loops are not approximations or replacement motions. The total ordered BRC ledger has 24 ring steps, four centre-spoke steps and exactly **28 primitive events**, returning both triad labels to their initial native Cells.

The joint history has explicit INNER centre excursions and is **not an OUTER-only physical C12 trajectory**. Ring winding counts only oriented OUTER edges; a spoke changes the triad's occupancy without being silently counted as a ring step. Thus the construction does not contradict Unit242: the ring-only gap invariant ceases to apply while one label is parked at P.

## Theorem 2 — sharp 28-event minimum in this finite conditional graph

Fix the graph above, two labels, the same initial and final Cells (x0,x2), the empty-target serial move guard, and exact signed ring step counts L_A=-12, L_B=+12. Among **all** allowed chronological moves and interleavings, not only the explicit parking protocol, the shortest history is exactly

\[
\boxed{24\text{ ring events}+4\text{ centre spokes}=28\text{ native events}.}
\]

An exact exhaustive breadth-first search has state (position_A,position_B,L_A,L_B). It traverses all source-defined signed edges with the occupancy guard and preserves integer oriented ring increments. The independently executable standard-JavaScript checker reports **shortest distance 28; 24,418 states at depths 0–27; 99 states at depth 28; 24,521 discovered states; zero failed assertions**. It also validates the constructive 28-step witness against all 13 six-axis coordinates.

Completeness of the bounded [-12,12] ring counters for proving the lower bound: any counterexample shorter than 28 would need at least 24 ring events (12 in each target direction). As both tokens begin and end on ring Cells, centre-spoke count must be even. Zero spokes is impossible by Unit242. Thus the only shorter candidate has exactly 2 spokes and 24 ring events: both rings are then forced to move *monotonically* in their target directions, and every prefix ring counter remains inside [-12,12]. The exhaustive BFS includes **every** such candidate. It finds none. The explicit 28-event witness attains the lower bound. The finite certificate proves the claim within this **declared** dynamical graph; it is not a proof of physical Port acceptance.

## Reproduction and independent verification

- Executed JS source: research_checks/X6_TIME_UNIT243_CENTER_PARKING_OPPOSING_WINDING_CHECK_20261121_2056.js, commit 41cfb3fa32cf672069206d68fa11ab3d87889b6f, Git blob 662a1a8ebe8f03e57a910011225a4dad1fae9d7a.
- Exact JSON result: research_checks/X6_TIME_UNIT243_CENTER_PARKING_OPPOSING_WINDING_RESULTS_20261121_2056.json, commit 37a879cdac53d70b91b0a52b219ee41d9a16f259, Git blob 32b5645809b8c80c84b2b30746d11757e30c7fb5.
- Standard-library Python independently reconstructed all 13 native coordinates, 36 directed edges, full 28-event signed chronology and BFS; it likewise found 28 as the shortest with 24,521 discovered states. The committed JS checker is separately executable with Node and returned the stated JSON certificate.
- Unit242 ring-only obstruction remains at research_notes/X6_TIME_UNIT242_MULTITRIAD_C12_EXCLUSION_WINDING_LOCK_20261121_2000.md, commit 26918c8fd8babf3fa106e04ae256419c086ec4c7.

## Physical evidence still missing and next exact discrimination

**Source-defined Cell adjacency is not physical Port admission.** P000 fixes the selected Cell geometry and one-axis primitive step alphabet, not an actual transfer of a complete force triad through a signed centre spoke. The exact acceptance test is to obtain the actual permitted updates for x0 ↔ P and x2 ↔ P, including signed direction, triadic token conservation, target-empty resource guard, environment response and ordered Cell/Port/BRC ledger. If that real law admits all four spoke events, test the exact 28-event schedule; if it denies any of them, record the particular rejecting guard and preserve the original ring-only obstruction. Pair this with independent before/after C12/C24 precision-fibre observation of the *same* Cell. No physical holonomy H=6, Root ±3 time update, Driver approval or Result admission is inferred.

Keep the R063 six-file Native benchmark separate under RS-X6-LEGACY-PLANE-RECONCILIATION. Units233–242 already saved are not recomputed. Protected Native semantic PROGRESS for Units233–243 remains unclaimed without the current winning owner and backend #2903 typed-continuation repair; never replay terminal failed requests.
