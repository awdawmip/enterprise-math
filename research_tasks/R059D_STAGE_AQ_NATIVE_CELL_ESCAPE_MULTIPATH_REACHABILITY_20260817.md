# R059D Stage AQ — Native Cell Escape Multipath Reachability

Task-ID: `RS-R059D-STAGE-AQ-NATIVE-CELL-ESCAPE-MULTIPATH-REACHABILITY`

Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

Identity policy: `AUTO_RESOLVE_OR_ALLOCATE`

Owner branch after taskbook freeze:

`research/r059d-stage-aq-native-cell-escape-multipath-reachability`

## 0. Why this stage exists

Stage AP-REISSUE proved that the visible one-step endpoint orbit can be simple while the hidden competition/collapse mechanism is not. The user now proposes a more primitive rule that does **not** choose UP versus DOWN and does **not** assume any circle arc.

The new idea is an **escape process**:

> We do not know how the circle arc runs. At a current native cell, expose the three edge-adjacent candidate cells. Let the line segment route itself by escaping as far from the signed origin as the local rule permits. Impose a jump-count budget. Every path satisfying the same local escape rule is accepted; no tie-breaking path is privileged. Whatever cells/endpoints are reachable under the budget are the result.

This stage tests that idea exactly. It is not allowed to tune the escape rule to reproduce the old R059D circle.

## 1. Frozen coordinate foundation

Read first:

- `definitions/ENTERPRISE_SIGNED_ORIGIN_ONE_COORDINATE_20260817.md`
- `definitions/ENTERPRISE_SQUARE_AND_ROOT_SIGNED_ORIGIN_ONE_20260817.md`
- `definitions/ENTERPRISE_COORDINATE_SYSTEM_AND_BRC_BRIDGE_20260816.md`
- `driver_reviews/R059D_STAGE_AP_REISSUE_DRIVER_REVIEW_20260817.md` if present; otherwise use the accepted AP-REISSUE report/checkpoint as frozen input.

Freeze:

`+1 ≡ -1 ≡ O_E`

`0` is not a native Enterprise coordinate.

Negative native states `-2,-3,...` are legal.

Old zero-centered coordinates may be used only as an explicitly typed auxiliary computation chart through the already-defined signed-origin encoding/decoding.

## 2. Output type change: single resolver -> path family

Do **not** define a function

`orientation -> one chosen target state`.

The primary object is now set-valued / nondeterministic:

`ESCAPE_J(seed) = set of all admissible native cell paths with at most/exactly J jumps`

and its endpoint set

`END_J(seed) = { terminal cell of gamma : gamma in ESCAPE_J(seed) }`.

Ties are not broken. If two or three next cells are equally admissible under the same local escape score, all branches survive.

Freeze:

`ALL_ADMISSIBLE_REACHABLE_PATHS_ARE_VALID`.

Path multiplicity may be recorded but may not be used to delete a reachable endpoint.

## 3. Stage A — define the native triangular cell carrier

Construct the exact native elementary-cell complex used by the escape rule.

Required:

1. a native cell type consistent with the accepted Enterprise triangular/half-square incidence structure;
2. an edge-adjacency relation;
3. proof that each elementary triangular cell has exactly three edge-adjacent cells in the local carrier used here;
4. the signed-origin action/D6 transport on cells;
5. a precise origin-star `STAR(O_E)` consisting of native cells incident to the glued origin state.

Do not import source Euclidean area or source angular distance to define adjacency.

If the native carrier does not actually support a canonical three-neighbor relation, stop and report the exact obstruction rather than inventing one.

Required output:

`R059D_STAGE_AQ_NATIVE_CELL_CARRIER.json`.

## 4. Stage B — native outward shell / escape score

Formalize “尽量远离原点” without using the classical circle.

Preferred canonical score:

`SHELL(C) = graph distance in the native cell dual graph from STAR(O_E) to C`.

Equivalent native incidence formulations are allowed if proved equal.

Mandatory properties to prove/check:

- source-free;
- D6 invariant;
- translation semantics explicitly typed if used;
- adjacent cells change shell by a controlled amount;
- every nonterminal escape state has at least one locally maximal neighbor.

For a current cell `C`, let its three edge-neighbors be `N3(C)` and define the local farthest set

`FAR(C) = argmax_{D in N3(C)} SHELL(D)`.

No arbitrary tie breaker is allowed.

Also test the stricter variant

`FAR_PLUS(C) = {D in FAR(C): SHELL(D) > SHELL(C)}`

and determine whether `FAR` and `FAR_PLUS` coincide on all relevant escape states. Freeze the true relation.

Required output:

`R059D_STAGE_AQ_NATIVE_ESCAPE_SCORE.json`.

## 5. Stage C — jump-budgeted multipath escape law

For integer jump budget `J>=0`, define path families recursively.

Preferred exact-J form:

- `ESCAPE_0(C) = {(C)}`;
- if `gamma=(C_0,...,C_j)` is admissible and `j<J`, every `D in FAR(C_j)` extends a branch `(C_0,...,C_j,D)`;
- if a strict-outward rule is adopted, replace `FAR` by the proved correct `FAR_PLUS`;
- no branch is pruned merely because another branch reaches farther by a different route.

Record both:

- exact-J endpoints `END_J`;
- up-to-J reachable set `REACH_LE_J`.

Because the user explicitly said “跳数限制，看能逃到哪就是哪”, `J` is an independent control parameter. Do **not** assume `J = radius`, `J = coordinate magnitude`, or `J = source precision`.

Required output:

`R059D_STAGE_AQ_ESCAPE_REACHABILITY_DEFINITION.json`.

## 6. Stage D — seed semantics for a rotating line segment

We do not know the circle arc, so the seed must not encode the desired answer.

For a fixed signed-origin segment class, construct the local set of native cells touched/eligible at the free endpoint before escape.

At minimum analyze:

- the one-step segment class from AP-REISSUE;
- all six D6 axis orientations;
- every canonical local seed cell incident to the free endpoint/endpoint frontier;
- whether the three-neighbor escape rule depends on triangle orientation.

If there are multiple legitimate seeds for the same endpoint/orientation, retain all of them as branches.

Required output:

`R059D_STAGE_AQ_SEGMENT_ESCAPE_SEEDS.json`.

## 7. Stage E — exhaustive reachability census

Compute/prove the multipath escape family before comparing to any old circle.

Minimum budgets:

`J=0..32` for one-step seeds,

and larger checkpoints where growth remains computationally manageable.

For every J record:

- number of admissible paths;
- number of distinct reachable cells;
- number of distinct exact-J endpoints;
- shell distribution;
- D6 orbit decomposition;
- path multiplicity per endpoint;
- whether branches merge after diverging;
- whether endpoint set is a simple cycle, several cycles, an annulus/ring, a filled sector, or something else.

The theorem target here is descriptive, not predetermined.

Required output:

`R059D_STAGE_AQ_ESCAPE_CENSUS.json`.

## 8. Stage F — all-path acceptance theorem

Prove the strongest structural statement supported by the native escape graph.

Questions:

1. Does local farthest escape generate a directed acyclic graph because shell strictly increases?
2. Are exact-J endpoints exactly one native shell?
3. Are all shell-J cells reachable, or only a proper subset?
4. Is the path family equivalent to all native geodesic rays from the origin-star?
5. Does retaining all tied branches force a canonical set-valued object even though no canonical single path exists?

Preferred disposition if true:

`CANONICAL_SET_VALUED_ESCAPE_RESOLVER_PROVED__NO_SINGLE_PATH_SELECTION_NEEDED`.

But exact countertheorems are fully acceptable.

Required output:

`R059D_STAGE_AQ_MULTIPATH_STRUCTURE_THEOREM.json`.

## 9. Stage G — circle emergence test, only after escape law is frozen

Only after Stages A–F are frozen may the result be compared with previous circle objects.

For each line/coordinate magnitude `r` and jump budget `J`, compare the signed-origin escape endpoint family to:

- the accepted one-step visible six-axis orbit;
- the signed-origin conjugate of legacy R059D radius-r endpoint cycles where available;
- any native boundary/frontier object that is independent of the source classical circle.

Determine whether there exists a **natural, non-retuned** relation `J=J(r)` arising from native combinatorics such that the escape endpoint set/path envelope reproduces or refines the circle.

Forbidden:

- choosing J separately at each radius just because it matches the old answer;
- using source pi/circle arc to choose J;
- discarding valid escape paths to improve the match.

Possible valid outcomes include:

1. exact circle recovery;
2. circle contained in a larger escape envelope;
3. escape boundary differs but converges asymptotically;
4. escape rule produces a different native object;
5. rule is too permissive and cannot define a useful circle.

Required output:

`R059D_STAGE_AQ_CIRCLE_EMERGENCE_AUDIT.json`.

## 10. Stage H — relation to AP coherent collapse

Compare the new escape family with AP-REISSUE without forcing equivalence.

In particular ask:

- does AP coherent DOWN+axis completion correspond to one distinguished path in the larger escape family?
- does the broader `DIRECT_FORWARD_AXIS` counterpolicy appear naturally as another admissible escape path?
- does all-path acceptance explain why AP did not justify a unique collapse direction?
- can `COHERENT_COUPLED_COLLAPSE_DIRECTION` be demoted from a needed uniqueness axiom because the new theory accepts all branches instead?

This stage may show that the correct object is not “choose the right collapse direction” at all, but the whole reachable path family.

Required output:

`R059D_STAGE_AQ_AP_RELATION.json`.

## 11. No intrinsic probability unless separately defined

The user accepts all reachable paths. Therefore do not introduce path probabilities by default.

You may record:

- raw path multiplicity;
- endpoint multiplicity;
- uniform-random tie-choice diagnostics;

only as optional measures on top of the set-valued object.

Never use a chosen probability law to delete or privilege native reachable paths.

## 12. Deterministic validation

After theorem statements are frozen, validate at minimum:

- every local three-neighbor list;
- shell invariance under D6;
- all branches for J=0..32 from all one-step D6 seeds;
- independent BFS/DFS replay giving identical reachable sets;
- branch-merger accounting;
- reverse/provenance reconstruction from each endpoint;
- signed-origin / no-native-zero firewall;
- no source geometry in escape score;
- comparison to AP and legacy circle only after the escape object itself is frozen.

Finite replay supports implementation; structural reachability claims require graph-theoretic proof or finite-exhaustive proof on the declared bounded carrier.

## 13. Mandatory firewalls

- `0` is never a native Enterprise coordinate.
- `+1 ≡ -1` is one glued origin state.
- Source Euclidean radius, source angle, source pi and classical circle may not define the escape score, candidate cell set, or path pruning.
- No unique path may be selected just to recover an old circle.
- All locally admissible tied branches survive.
- Jump budget J is independent until a native theorem relates it to line magnitude/radius.
- Do not identify path count with probability without an explicit measure.
- Do not modify prior-stage result files.

## 14. Terminal dispositions

Use the strongest justified status:

1. `CANONICAL_SET_VALUED_ESCAPE_RESOLVER_PROVED__CIRCLE_EMERGES_WITH_NATIVE_JUMP_LAW`
2. `CANONICAL_SET_VALUED_ESCAPE_RESOLVER_PROVED__CIRCLE_CONTAINED_IN_ESCAPE_ENVELOPE`
3. `CANONICAL_SET_VALUED_ESCAPE_RESOLVER_PROVED__ESCAPE_OBJECT_DISTINCT_FROM_CIRCLE`
4. `MULTIPATH_ESCAPE_GRAPH_PROVED__NATIVE_JUMP_TO_CIRCLE_RELATION_OPEN`
5. `LOCAL_FARTHEST_RULE_TOO_PERMISSIVE__EXACT_COUNTERTHEOREM`
6. `THREE_NEIGHBOR_NATIVE_CELL_PREMISE_FALSE__CARRIER_REPAIR_REQUIRED`

Stop for Driver review. Do not consume a later stage automatically.
