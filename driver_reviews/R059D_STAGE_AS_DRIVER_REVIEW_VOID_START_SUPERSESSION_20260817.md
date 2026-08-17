# R059D Stage AS — Driver Review under Void-Start Segment Supersession

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`
Date: `2026-08-17`
Researcher: `EM-R059D-AS-6E2A91`
Owner head: `974474eaf63958d9a46ccc44b505ce4ee5cf5983`
Original taskbook source: `75d2e38cf20bc7c6c64e0100c6d78ea151b5cbd6`

## Driver disposition

`DIAGNOSTIC_ACCEPTED__WEAKER_AXIOMS_UNDERDETERMINED__SUPERSEDED_BY_VOID_START_ALL_SHORTEST_PATH_FOUNDATION`

Stage AS is **not** accepted as the current foundational segment model. It is accepted as a correct diagnosis of the weaker pre-foundation problem.

AS proved that, before a canonical segment ontology was frozen, multiple inequivalent longer-segment carriers and multiple native-looking length observables survived. In particular, `L_chain` and endpoint graph-distance `L_disp` agreed on axis anchors but disagreed on a triangular detour.

The user/Driver has now supplied the missing foundational selection:

`VOID_E = ∅`

`VOID_E -> O_E=±1` is the first step,

`SEG_E(P) = all shortest paths VOID_E -> P`,

`ELL_E(P)=d_(G~_E)(VOID_E,P)=1+d_E(O_E,P)`.

Therefore the old AS underdetermination is resolved by explicit supersession, not by fitting to AK/AL.

## What survives from AS

Preserve as diagnostic/combinatorial facts:

1. Single-chain, terminal-side, and edgewise-strip carriers are not foundationally forced by incidence alone.
2. A local triangle `1->2` move changes raw chain cardinality by `+1` and `2->1` by `-1`.
3. Free-endpoint shell and newly-entered-cell shell can produce different escape choices; a cell-level escape score was therefore underdetermined in the old carrier models.
4. AL support without A8 did not remove the first old-carrier `1->2` drift witness.

## What is superseded

Do not retain as current foundation:

- `L_chain` as segment length;
- any single ordered chain as the segment itself;
- terminal-side or edgewise-strip carrier selection;
- old AS escape/circle nonclosure statements as the theorem about the newly defined segment.

Under the new foundation, a fixed-endpoint path belongs to the segment iff it is geodesic. Hence a `1->2` replacement with unchanged subpath endpoints is automatically excluded if it increases shortest-path length.

## New hard consequence

The current research problem is no longer "which longer-segment carrier should be chosen?" It is:

1. characterize all shortest `VOID_E -> P` paths;
2. derive their spatial geodesic tail from `O_E`;
3. classify equal-length/geodesic-preserving local replacements;
4. determine the endpoint set at fixed total existence length;
5. re-audit the canonical circle and circumference under that indexing.

Historical AK/AL/AI interpretations are not protected.
