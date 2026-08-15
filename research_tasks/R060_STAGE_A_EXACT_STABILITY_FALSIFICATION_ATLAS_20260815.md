# RS-R060 — STAGE A EXACT STABILITY FALSIFICATION / TERMINAL-ORBIT ATLAS

Task-ID: `RS-R060-STAGE-A-EXACT-STABILITY-FALSIFICATION-ATLAS`
Generation: `R060`
Stage: `A`
Status: `DRIVER_APPROVED_TASKBOOK`
Identity-policy: `AUTO_RESOLVE_OR_ALLOCATE`
Identity-lane: `R060`
Date: `2026-08-15`
Driver: `EM-DVR-9GP3M7 / CONTROL_PLANE`

## 0. Driver disposition and frozen parent

R060 Stage 0 is **ACCEPTED**.

Frozen Stage-0 owner head:

`1abc43a78c87b4adcb535d2964afe274e78f9337`

Frozen Stage-0 checkpoint SHA256:

`7e87358a0e328ec41674a8ffce26d1eed21b5dbc5f5bdba93458a660d698f185`

Stage-0 artifacts are immutable.

R059L remains parked and is not a parent of R060.

Stage A must use exactly the frozen Stage-0 carrier, dynamics, automorphism equivalence, and stability definitions. Do not repair or enlarge the model during this stage.

---

# 1. Scientific question

Stage 0 proved only S0 termination for:

`C3_RELATIONAL_RANK3_CHANNEL_CARRIER`

with dynamics:

`D3_L1_LOCAL_CONTACT_CUT_DESCENT`.

Stage A asks the first actual stability question:

> Does the frozen rank-3 candidate exhibit S1 single-initial confluence and S2 local-perturbation robustness, or can either property be falsified by an exact finite counterexample?

The priority is **falsification at the smallest N**, not large-N performance.

A failure of S1/S2 is a failure of this frozen carrier+dynamics pair. It is not a proof that relational rank 3 is impossible and not a proof about the physical dimension of the world.

---

# 2. Frozen objects — DO NOT MODIFY

Use exactly:

- `R060_RELATIONAL_RANK3_CARRIER.json`
- `R060_RANK3_AUTOMORPHISM_PROTOCOL.json`
- `R060_CONTACT_CUT_PROTOCOL.json`
- `R060_D3_L1_LOCAL_COLLAPSE_PROTOCOL.json`
- `R060_STABLE_COLLAPSE_HIERARCHY.json`
- `R060_DIMENSION_AS_OUTPUT_INFERENCE_GUARD.json`

In particular:

- `UNIT_PACKET(x)=1`;
- carrier adjacency is the frozen rank-3 six-incidence relational adjacency;
- `B(C)=CONTACT_CUT_COUNT`;
- one move relocates one occupied packet to an adjacent empty packet;
- fixed N and connectivity are preserved;
- only strict `B` decrease is accepted;
- every accepted move is a valid nondeterministic branch;
- equivalence is the full frozen carrier-automorphism orbit;
- no tie-breaker is permitted.

Do not add cooperative moves, equal-B moves, temporary uphill moves, centroid rules, distance, or another energy in Stage A.

---

# 3. Exact descent DAG

For each finite connected state-orbit representative `C`, construct the complete directed descent graph:

`C -> C'`

for every legal frozen D3_L1 move.

Because Stage 0 proved strict integer descent of `B`, the graph is acyclic.

Define exactly:

`T(C) = set of carrier-automorphism orbits of all terminal endpoints reachable from C`.

Compute `T(C)` by complete finite recursion / dynamic programming on the descent DAG, never by one greedy trajectory.

Mandatory checks:

- every outgoing accepted move is included;
- all terminal endpoints are included;
- automorphism-equivalent duplicates are merged only under the frozen exact orbit procedure;
- no branch-order preference is introduced.

---

# 4. S1 exact test

Frozen definition:

`S1(C) <=> |T(C)| = 1`.

Search connected state orbits in increasing N.

Primary target:

`N_S1_FAIL = min { N : exists connected C, |C|=N, |T(C)|>1 }`

if such an N is found in the exact searched range.

For the first S1 failure, freeze an explicit certificate containing:

1. one canonical initial state `C0`;
2. at least two complete legal D3_L1 descent histories from `C0`;
3. their exact `B` sequences;
4. two terminal endpoints `F1,F2`;
5. canonical orbit representatives / orbit IDs proving `F1` and `F2` are inequivalent under full carrier automorphism;
6. proof that both trajectories are maximal/terminal;
7. proof that no smaller N contains an S1 failure, by exhaustive lower-N coverage.

Return disposition:

- `RANK3_D3_L1_S1_NONCONFLUENCE_FOUND`, or
- `RANK3_D3_L1_S1_HOLDS_THROUGH_BOUND` if no failure is found in the declared exact range.

A bounded positive result is not a theorem for all N.

---

# 5. S2 exact test

Frozen perturbation neighborhood:

`P1_ADJACENT_RELOCATION(C)`

contains every connected fixed-N state obtained by relocating one occupied packet to an adjacent empty packet, **without requiring B descent**.

Frozen definition:

`S2(C) <=> S1(C) and for every C1 in P1_ADJACENT_RELOCATION(C), T(C1)=T(C)`.

Search in increasing N.

Primary target:

`N_S2_FAIL = min { N : exists connected C, |C|=N, not S2(C) }`.

Separate two failure modes:

- `S2_FAIL_BY_S1`: the base state itself is nonconfluent;
- `S2_FAIL_BY_PERTURBATION`: the base state is S1 but an allowed one-packet perturbation has a different terminal-orbit set.

For the earliest perturbative failure, freeze:

1. canonical `C0`;
2. canonical one-relocation neighbor `C1`;
3. exact relocation `u -> v`;
4. `T(C0)` and `T(C1)`;
5. exact automorphism-inequivalence evidence for the differing terminal orbit(s);
6. proof no smaller N has an S2 failure under the frozen definition.

Return disposition:

- `RANK3_D3_L1_S2_PERTURBATION_FAILURE_FOUND`, or
- `RANK3_D3_L1_S2_HOLDS_THROUGH_BOUND` if no failure is found in the declared exact range.

---

# 6. Search order and computational budget

Stage 0 already exhaustively enumerated connected carrier-automorphism orbits for `N<=6`.

Therefore Stage A must begin with the existing exact `N<=6` state-orbit registry and add **reachability**, not regenerate a larger universe first.

Required order:

1. replay/verify the frozen `N<=6` orbit registry;
2. construct complete D3_L1 descent DAGs for those orbits;
3. compute every `T(C)` for `N<=6`;
4. determine exact S1/S2 status and minimal failure N within this range;
5. if both S1 and S2 already have exact failures, **stop expansion** and characterize those failures;
6. only if a target failure is still absent may the researcher expand one N at a time, with a default hard ceiling `N<=8` for this stage.

Do not perform open-ended enumeration.

The point of Stage A is to learn whether the simplest rank-3 model is stable, not to maximize N.

---

# 7. S3 diagnostic — secondary only

For each completely enumerated N, report the exact union:

`U_N = union_C T(C)`

over all connected N-packet state orbits in the registry.

Classify:

- `S3_UNIQUE_ORBIT` if `|U_N|=1`;
- otherwise `S3_EXACT_FINITE_BASIN_ATLAS` with exact terminal-orbit family and initial-orbit -> reachable-terminal-orbit incidence.

Do not call multiple terminal orbits a defect by itself unless the declared S3 criterion requires uniqueness.

Do not let S3 work delay the primary S1/S2 falsification targets.

---

# 8. Instability mechanism ledger

If S1 or S2 fails, classify the exact relational mechanism without inventing new physics.

Allowed descriptive classes include:

- `BRANCH_ORDER_SENSITIVITY`
- `MULTIPLE_STRICT_LOCAL_MINIMA`
- `PERTURBATION_CHANGES_BASIN`
- `CONNECTIVITY_CONSTRAINT_SPLITS_DESCENT`
- `CONTACT_CUT_DEGENERACY`
- `OTHER_EXACT_RELATIONAL_MECHANISM`

Any mechanism claim must be backed by explicit finite state/move data.

Do not interpret it as gravity, energy barrier, curvature, geometric roughness, or physical metastability in Stage A.

---

# 9. Semantic firewall

All Stage-0 prohibitions remain active.

Strictly forbidden:

- Euclidean distance/norm;
- center/centroid/radius;
- line/straightness;
- angle/curvature;
- area/volume/surface-area interpretation;
- graph distance as collapse score;
- shortest path optimization;
- convex hull;
- imported gravity;
- probability/entropy reinterpretation unless separately typed and authorized;
- path ranking imported from R059L;
- changing UNIT_PACKET=1;
- changing carrier adjacency;
- changing the D3_L1 move set;
- adding deterministic tie-breakers to manufacture confluence;
- treating S0 termination as S1/S2 stability;
- treating one carrier failure as `3D_IMPOSSIBLE`;
- treating one carrier success as `WORLD_IS_3D`.

Coordinate triples remain I0 implementation encoding only.

---

# 10. Required artifacts

Freeze at least:

1. `R060_STAGE_A_DESCENT_DAG_REGISTRY.json`
2. `R060_STAGE_A_TERMINAL_ORBIT_MAP.json`
3. `R060_STAGE_A_S1_CONFLUENCE_ATLAS.json`
4. `R060_STAGE_A_S2_PERTURBATION_ATLAS.json`
5. `R060_STAGE_A_MINIMAL_S1_COUNTEREXAMPLE.json` if found
6. `R060_STAGE_A_MINIMAL_S2_COUNTEREXAMPLE.json` if found
7. `R060_STAGE_A_S3_FINITE_BASIN_ATLAS.json`
8. `R060_STAGE_A_INSTABILITY_MECHANISM_LEDGER.json`
9. `R060_STAGE_A_COVERAGE_CERTIFICATE.json`
10. `R060_STAGE_A_SEMANTIC_CLAIM_LEDGER.json`
11. deterministic Stage-A checker output
12. `R060_STAGE_A_STABILITY_CHECKPOINT.json`

---

# 11. Checker hard negatives

The deterministic checker must reject at least:

- `GREEDY_SINGLE_PATH_USED_AS_T_OF_C`
- `UNEXPLORED_LEGAL_BRANCH_DROPPED`
- `COORDINATE_EQUALITY_USED_INSTEAD_OF_AUTOMORPHISM_ORBIT`
- `S0_PROMOTED_TO_S1`
- `S1_PROMOTED_TO_S2`
- `S2_PERTURBATION_REQUIRES_B_DESCENT`
- `TIE_BREAKER_ADDED_TO_FORCE_CONFLUENCE`
- `DYNAMICS_CHANGED_AFTER_COUNTEREXAMPLE`
- `BOUNDED_S1_PASS_PROMOTED_TO_ALL_N_THEOREM`
- `BOUNDED_S2_PASS_PROMOTED_TO_ALL_N_THEOREM`
- `RANK3_FAILURE_PROMOTED_TO_3D_IMPOSSIBLE`
- `RANK3_SUCCESS_PROMOTED_TO_WORLD_IS_3D`
- any Stage-0 geometry leakage fixture.

---

# 12. Required return

Return:

- Researcher-ID;
- Stage-0 frozen parent head and checkpoint SHA256;
- exact searched N range;
- state-orbit counts replayed/added;
- exact descent-DAG coverage;
- `N_S1_FAIL` or bounded S1-pass statement;
- `N_S2_FAIL` or bounded S2-pass statement;
- explicit earliest counterexample certificates if found;
- S3 exact finite basin summary for fully covered N;
- instability mechanism ledger;
- checker result;
- artifact SHA256s;
- Stage-A checkpoint SHA256;
- owner head / Draft PR if published;
- one overall scientific disposition:
  - `RANK3_D3_L1_STRONG_STABILITY_FAILS_EXACTLY`
  - `RANK3_D3_L1_STRONG_STABILITY_SURVIVES_BOUND`
  - `STAGE_A_INCOMPLETE_WITH_EXACT_PARTIAL_ATLAS`
  - `SEMANTIC_HARD_STOP` with exact violated gate.

Then stop for Driver review.

Do not alter the collapse rule in response to a counterexample. Any repair is a later Driver decision.
