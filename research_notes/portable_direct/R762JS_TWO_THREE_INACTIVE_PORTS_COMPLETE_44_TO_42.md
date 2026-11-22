# R762JS — (6,12,2,0) Port–Euler 44→42, completing two/three inactive Ports

Date 2026-11-23 (Asia/Shanghai). Frozen science predecessor: R762JR, Draft PR #2985 @ `47504c177ac2b318f5419a5fdb1304fafccf21fc`. Evidence class: AUTHOR_PROVED_BY_EXACT_SMALL_FINITE_CHECK_AND_CONSTRUCTION / NOT_REVIEWED. Six-axis **composite Port–Euler observer only**; no signed P000 Cell/path/branch/time/BRC lift.

## Definitions and theorem

Let axes A={0,…,5}; Ports P=C(A,2), |P|=15; supports S=C(A,3), |S|=20. Each event of color s joins two *distinct* Ports belonging to C(s,2); repeated parallel events allowed. N_(p,V)(n)>0 denotes a connected positive-even-degree multigraph with exactly n_s events per color s, exact active Port set V, and an Euler walk starting at p∈V.

**Theorem.** Suppose every support is positive, M=P\V is a matching of size 2 or 3, and n_s∈{1,2,3} for all 20 supports with at most three singleton supports (n_s=1). Then N_(p,V)(n)>0 for every p∈V.

Consequently, if h=(t,d,s,z)=(6,12,2,0) has 44 events and an eligible active set V of this kind, **every** triple support j admits N_(p,V)(h−2e_j)>0 with 42 events. Exact support labels, count parity, active set and starting Port are retained.

All legal inactive sets are matchings: if inactive Ports ab and ac share axis a, the positive support abc has only one active Port available, so none of its positive events could join distinct active Ports. At most three disjoint edges exist on six axes. By S6 axis symmetry it suffices to check representatives M2={01,23} and M3={01,23,45}.

## Forced-edge components and local parity

For each M_i, every support containing a missing Port has precisely two active Port vertices and forces all events onto their single connecting edge; these positive forced edges form a graph with respectively **six** (M2) or **three** (M3) connected components. There are respectively **eight or twelve** forced support colors. The other **twelve or eight** fully active colors each form a triangle meeting three different forced components.

Inside any fully active triangle on a,b,c, write boundary ∂(ab)=e_a+e_b over GF(2). Exact local boundary options:
- count 1: three nonzero side boundaries;
- count 2: all four even options: zero via two parallel copies of one side, or ∂(ab) via the other two edges (length-two path);
- count 3: all four: zero via the three different sides, or ∂(ab) via one ab and two copies of a different side.

For count 2 or 3 and *every* local boundary, the edge realization can preserve connectivity between the endpoints of **any predesignated triangle side**: at count 2 / boundary zero double that designated side; at count 2 / boundary nonzero the length-two path covers all three vertices; and all listed count-3 realizations connect all three.

## Lemma A — exact parity coverage

Let FULL be all fully active support colors, D⊆FULL the colors with count 1 (|D|≤3), and U_D the GF(2)-span of all full-triangle side boundaries from FULL\D. A color outside D offers all four triangle-local even boundaries, and a color in D offers exactly its three nonzero side boundaries. For either canonical matching:

{ sum_(s in D) ∂(chosen side of s) + u : u∈U_D } = {b∈GF(2)^V : sum_(v∈V)b_v=0}.

This is a complete finite lemma on *all* 392 D patterns (not random samples). The attached standard-library verifier uses two independent exact methods: (1) Gaussian elimination and quotient-coset coverage, (2) full reachable-parity-set DP. For M2, |FULL|=12, there are 1+12+66+220=**299** D patterns, each reaching all 2^12=**4096** even masks on 13 vertices. For M3, |FULL|=8, there are 1+8+28+56=**93** patterns, each reaching all 2^11=**2048** even masks on 12 vertices.

GF(2) rank/coset breakdown:
- M2: k=0 rank12×1; k=1 rank12×12; k=2 rank12×62, rank11×4 (2 cosets); k=3 rank12×172, rank11×48 (2 cosets).
- M3: k=0 rank11×1; k=1 rank11×8; k=2 rank11×16, rank10×12 (2 cosets); k=3 rank10×32 (2 cosets), rank9×24 (4 cosets).
Every requisite coset is attained by the singleton choices; no parity target is missing.

The compulsory supports contribute an even global boundary b, and this lemma lets fully active supports cancel b exactly.

## Lemma B — rainbow spanning forest

For every D pattern above, there is a connected tree on the forced-edge components using edges from **distinct** flexible colors in FULL\D, one side per color. The verifier enumerates the complete D domain and performs a memoized finite partition-state search (skip color, or select one of its three Port edges joining two distinct current components). It returns a verified color-distinct tree in every case:
- M2: **299/299**, a five-edge tree connecting six forced components.
- M3: **93/93**, a two-edge tree connecting three forced components.

Each designated color has count 2 or 3, so by the local parity lemma **any** independently selected parity can be realized while retaining a path between its designated pair of endpoints.

## Proof of theorem

Place all forced events on their only legal edges. Choose the flexible full-color boundary assignments that cancel the forced even degree boundary via Lemma A. Choose a color-distinct tree of forced components by Lemma B and designate its selected side for each chosen flexible support. Realize every full color with exactly its given multiplicity and parity; for selected tree colors preserve designated-endpoint connectivity, which is possible for any local boundary at multiplicity 2 or 3. The forced components remain connected internally and are joined by the designated-color tree. All degrees are positive and even, all support counts are exact, inactive Ports have zero degree, and the graph is connected. Euler's theorem gives a closed route from any active Port.

For the terminal (6,12,2,0), removing two events from any one triple changes multiplicities to (5,12,3,0), which has 42 events and at most three singletons. The theorem applies directly, preserving parity label by label. QED.

## Exact verification

File `R762JS_MATCHING_INACTIVE_PORTS_VERIFY.py` contains the complete finite-domain verifiers, a graph constructor and exact graph checker. `R762JS_MATCHING_INACTIVE_EVIDENCE.json` gives counts and SHA256 evidence. **392/392** parity+rainbow patterns passed, both quotient and independent full-DP methods. An additional **2,280/2,280** deterministically selected 42-event inventories (1140 different three-singleton choices for each matching representative) produced and verified full Eulerian graphs: exact support counts, even positive active degrees, no inactive degree and connectivity. These samples crosscheck the constructive implementation; the general quantifiers rely on the finite lemmas and written proof rather than sample coverage.

R762JP/R762JR already cover zero/one inactive Port in this exact terminal histogram. Combined, these author-side results close the entire (6,12,2,0) 44→42 terminal class; their independent Review is still pending. The overall k=0 uniform upper bound remains **44** until the other 44-event histogram classes are resolved.

**Next**: apply the forced-component + GF(2) quotient + rainbow-forest method to remaining 44-event histogram classes, and separately investigate the native signed P000 Cell/Link/Port/time/branch and BRC-faithful lift. This composite graph certificate is not native TRIADIC_CLOSURE_E.

**Control separation:** independent portable research with current Sites client, not a claimed native Researcher/RA or winning shared CLAIM. The file does not assert formal PROGRESS, Result, Review, integration, or task completion. Preserve original contributor provenance and source pins.
