<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-R059C-COUNT-PRESERVING-BRANCHING-COLLAPSE-ALIGNED-SHEET-PATH-CLOUD",
  "title": "R059C Count-Preserving Branching Collapse on an Aligned Sheet",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "FOUNDATIONAL_EXPERIMENT",
  "frontier": "Construct an ideal aligned relational sheet, perturb only a declared remote set one packet at a time, and use count-preserving branching-collapse semantics to measure exact path-cloud and recoalescence integer responses without importing probability, force, energy, distance, angle, or rotation.",
  "next_action": "Freeze count-preserving branching-collapse semantics, validate against explicit raw-history enumeration on tiny carriers, then run deterministic aligned-sheet remote sequential perturbation experiments and expose exact integer response/invariant ledgers.",
  "dependencies": [
    {
      "target": "PACKET_PATH_FOUNDATION",
      "action": "CONSUME_UNIT_PACKET_ADJACENCY_PATH_EVENT_COUNT_SEMANTICS",
      "satisfied": true
    },
    {
      "target": "RS-R021-BRANCHING-COLLAPSE-TOOL-CALCULUS",
      "action": "CONSUME_BRANCHING_VS_SUPPORT_VS_MULTIPLICITY_TYPING_ONLY",
      "satisfied": true
    }
  ],
  "source_refs": [
    "PACKET_PATH_FOUNDATION.md",
    "packet_path_foundation.json",
    "FOUNDATIONAL_LOGIC.md",
    "foundational_logic.json",
    "native_semantics_admissibility.json",
    "research_tasks/R021_BRANCHING_COLLAPSE_TOOL_CALCULUS_20260811.md"
  ],
  "evidence_status": "COUNT_FIRST_PATH_CLOUD_EXPERIMENT",
  "hard_block": null,
  "tags": [
    "R059C",
    "count-preserving-branching-collapse",
    "path-cloud",
    "recoalescence",
    "aligned-sheet",
    "remote-perturbation",
    "integer-count",
    "count-ratio",
    "no-geometry"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "R059C"
}
-->

# R059C — COUNT-PRESERVING BRANCHING COLLAPSE / ALIGNED-SHEET PATH-CLOUD RESPONSE

Status: `READY / DRIVER_APPROVED / INDEPENDENT EXPERIMENT LANE / NOT CANONICAL`

Date: `2026-08-15`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`

---

## 0. Lane isolation and authority

R059C is a new independent lane.

Do **not** read, consume, modify, or depend on any research artifact/checkpoint/result/branch from:

- `R059L_*` / `EM-R059L-5F9D05`;
- `R059P_*` / `EM-R059P-8A2C7D`.

The current taskbook contains all cross-lane motivation needed for this experiment.

Allowed project-level authorities:

- `PACKET_PATH_FOUNDATION.md`
- `packet_path_foundation.json`
- `FOUNDATIONAL_LOGIC.md`
- `foundational_logic.json`
- `native_semantics_admissibility.json`
- `research_tasks/R021_BRANCHING_COLLAPSE_TOOL_CALCULUS_20260811.md` **only for semantic typing of branching/support/multiplicity and recoalescence**.

Do not import R021 arithmetic examples, resource conclusions, or canonical status into this experiment.

The task is explicitly above N0. It must not alter the packet/path foundation.

---

# 1. User hypothesis / experimental question

Construct a sufficiently large ideal stable sheet whose tagged constituents are initially aligned to carrier packets. Keep a declared anchor/reference region fixed. Perturb a declared remote region one tagged constituent at a time by exactly one adjacency transition.

For every intermediate configuration, propagate all admissible finite packet paths for a fixed transition-count horizon and record **how many path histories occupy each packet at each epoch**.

The experiment asks:

1. can a branching-collapse representation preserve exact multiplicity rather than only reachable support?
2. when the remote end is changed one packet at a time, how does the integer path-cloud redistribute?
3. do exact aggregate/recoalescence count invariants or compensations survive even when individual path counts move strongly?
4. can normalized count ratios be defined **after** counting, without assuming that they are physical probabilities?

This task does **not** assume that the result explains attraction, elasticity, rigidity, rotation, quantum mechanics, or zero-point motion.

---

# 2. Foundation firewall

N0 remains exactly the active project foundation:

- CRYSTAL PACKET, each packet quantity `1`;
- declared ADJACENCY;
- TRANSITION EVENT, each event quantity `1`;
- PATH as adjacency walk/history;
- PATH_COUNT / TRANSITION_COUNT;
- occupancy only when explicitly declared.

Implementation labels/coordinates may be used only to construct/check the declared carrier adjacency and deterministic perturbation schedule.

Forbidden as native premises or theorem-critical hidden semantics:

- line / straightness;
- geometric plane or Euclidean surface;
- distance / length;
- shortest path / geodesic;
- edge/boundary geometry;
- angle / rotation angle;
- displacement vector;
- radius;
- area / volume;
- force / energy / strain / attraction;
- stochastic kernel / quantum amplitude;
- physical probability.

The phrase **aligned sheet** is an experiment label for a finite regular relational tagged configuration, not an N0 Euclidean object.

---

# 3. Terminology: branching collapse and multiplicity

R021 explicitly distinguished support exactness from multiplicity/path-count exactness. This task targets multiplicity.

Do not rely on an uncertain historical acronym expansion. Use the explicit task-local term:

`COUNT-PRESERVING BRANCHING COLLAPSE (CPBC)`.

The key rule is:

> branch histories that arrive at the same packet may recoalesce in storage, but their integer multiplicities must add rather than collapse to a Boolean `1`.

A support-only Boolean representation is retained only as a comparison baseline.

---

# 4. Exact path-cloud semantics

Let `X` be a finite declared packet carrier with symmetric adjacency `~` unless a frozen registry case explicitly says otherwise.

For a tagged source at packet `a`, define:

`C_0^a(x) = 1[x=a]`.

For integer epoch `n >= 0`:

`C_{n+1}^a(y) = sum_{x ~ y} C_n^a(x)`.

Interpretation:

`C_n^a(y)` is the exact number of admissible raw adjacency-walk histories starting at `a` that occupy packet `y` after exactly `n` transition events.

This is a natural-number count, not a probability and not a geometric density.

Mandatory theorem/check:

`sum_y C_n^a(y)` equals the total number of length-`n` admissible raw histories from `a` under the frozen path rules.

For a tagged configuration `S=(a_1,...,a_m)`, define multi-source cloud:

`C_n^S(x) = sum_i C_n^{a_i}(x)`.

Also define the window visit count:

`V_[0,T]^a(x) = sum_{n=0}^T C_n^a(x)`

and

`V_[0,T]^S(x) = sum_i V_[0,T]^{a_i}(x)`.

Revisits are counted each time they occur. Do not convert visit count into unique-support count.

---

# 5. Four exact computational representations

Implement and cross-check at least these representations:

### A0 — RAW HISTORY ENUMERATION
For tiny carriers/horizons only, explicitly enumerate every legal raw path history. This is the ground-truth oracle.

### A1 — BOOLEAN BRANCHING SUPPORT
Store only whether a packet is reachable at epoch `n`:

`B_n(x) in {0,1}`.

This intentionally loses multiplicity and must never be reported as a count-preserving result.

### A2 — CPBC NATURAL-NUMBER COUNT
Store `C_n(x) in N` and recoalesce branches by integer addition.

Mandatory exactness target:

for every tiny oracle case,

`CPBC_COUNT == RAW_HISTORY_MULTIPLICITY`

packet-by-packet and epoch-by-epoch.

### A3 — TRUNCATED COUNT-SPECTRUM / GENERATING-CARRIER FORM
For each packet store the vector or polynomial

`G_x(z)=sum_{n=0}^T C_n(x) z^n`.

This is only a compact exact carrier for the whole finite count spectrum. No analytic/continuum meaning is allowed.

A2 and A3 must agree coefficientwise.

Optional matrix powers are permitted only as an independent exact implementation cross-check of walk counts, never as a new ontology.

---

# 6. Pair endpoint spectrum

For tagged markers `i,j` occupying packets `a_i,a_j`, define:

`W_n(i,j) = C_n^{a_i}(a_j)`.

This is the number of `n`-transition paths from marker `i`'s current packet to marker `j`'s current packet.

Freeze finite windows only. Do not call `n` a length.

For each configuration `S_k`, store all labeled-pair tables:

`W_n^(k)(i,j)`.

Also store exact deltas under each remote elementary perturbation:

`Delta W_n^(k)(i,j) = W_n^(k+1)(i,j)-W_n^(k)(i,j)`.

---

# 7. Recoalescence-opportunity counts

For two tagged sources `i,j`, define synchronized endpoint recoalescence count:

`R_n(i,j) = sum_x C_n^{a_i}(x) * C_n^{a_j}(x)`.

This counts ordered pairs of independently enumerated path histories that occupy the same packet after the same number `n` of transition events.

It does **not** yet mean attraction, force, interaction probability, or physical meeting rate.

For a frozen window `K=[n_min,n_max]`, define:

`R_K(i,j) = sum_{n in K} R_n(i,j)`.

Also compute the system-level aggregates:

`R_n^TOTAL(S) = sum_{i<j} R_n(i,j)`

and

`R_K^TOTAL(S) = sum_{i<j} R_K(i,j)`.

Mandatory companion outputs:

- labeled pair table of `R_n(i,j)`;
- multiset of pair `R_n` spectra;
- total aggregate;
- exact signed deltas after each remote perturbation.

If useful, add asynchronous cross-epoch readout

`R_{p,q}(i,j)=sum_x C_p^{a_i}(x) C_q^{a_j}(x)`

but keep it optional in Stage A.

---

# 8. Count ratios: COUNT FIRST, RATIO SECOND

For any count cloud at fixed epoch `n`, define denominator:

`N_n^a = sum_x C_n^a(x)`.

The task may expose the exact normalized rational/count ratio:

`Q_n^a(x) = C_n^a(x) / N_n^a`

or equivalently the reduced integer pair

`C_n^a(x) : N_n^a`.

Semantic label:

`EQUIPATH_COUNT_RATIO`.

Hard rule:

**Do not call `Q_n^a(x)` physical probability.**

The ratio means only:

> among raw admissible histories counted with equal combinatorial weight by this chosen path language, what fraction terminate at packet `x` after epoch `n`?

A future physical theory would still need to justify whether raw histories are equally weighted, unequally weighted, interfered, suppressed, or otherwise reweighted.

The first-round checkpoint must explicitly answer:

`PHYSICAL_PROBABILITY_FROM_COUNTING = NOT_ESTABLISHED`

unless an independent theorem is actually proved, which is not expected in this task.

---

# 9. Primary carrier: ideal aligned regular sheet

Construct a finite regular relational carrier with six local adjacency channels as the primary experiment family, using implementation coordinates only to instantiate/check adjacency.

Call the carrier family:

`IDEAL_C6_RELATIONAL_SHEET_CARRIER`.

The six channels are labels only. No angle, vector, opposite, straight, Euclidean plane, or metric semantics may be used.

Create a finite tagged configuration `S_0` consisting of a regular finite block of occupied/tagged carrier packets.

Required declarations:

- tagged marker identities;
- `ANCHOR_SET`, held fixed throughout the experiment;
- `REMOTE_SET`, the only markers perturbed in Stage A;
- initially occupied aligned packets;
- a surrounding unoccupied padding region;
- a deterministic observation horizon registry.

The word `sheet` denotes this declared regular relational tagged configuration only.

---

# 10. Boundary/padding gate

Artificial carrier boundaries must not be mistaken for a physical effect.

For every sheet size/horizon pair, include enough surrounding carrier packets to contain all packets reachable within `T` transitions from every marker position occurring anywhere in the predeclared perturbation schedule, or verify exact boundary independence by recomputing on a larger padded carrier.

Mandatory gate:

For every retained experiment case and every recorded packet/readout inside the observation domain,

`COUNT_WITH_PADDING_A == COUNT_WITH_LARGER_PADDING_B`.

If this fails, classify the case `BOUNDARY_CONTAMINATED` and do not use it for a stability conclusion.

---

# 11. Frozen size/horizon registry

Before viewing response results, freeze a deterministic registry containing multiple sheet sizes and horizons.

At minimum include:

- one tiny case for raw-history enumeration;
- one medium case;
- one substantially larger case;
- at least three transition horizons;
- at least two remote-set cardinalities or sheet aspect registries where computationally tractable.

Do not choose the final carrier size after seeing a favorable result.

Large means computationally large enough that exact padding independence and cross-size response comparison can be tested; it does not mean continuum limit.

---

# 12. Deterministic remote sequential perturbation

Before computing path-cloud responses, freeze a one-step adjacency target map for the remote markers:

`SHIFT(r_j) = t_j`

with:

- `r_j ~ t_j`;
- all `t_j` initially unoccupied;
- targets pairwise distinct;
- no marker other than the declared remote marker moves;
- no result-dependent target selection.

Freeze a deterministic remote order

`r_1,...,r_M`.

Define:

`S_0` = fully aligned initial configuration;

`S_k` = configuration after markers `r_1,...,r_k` have each made exactly one declared transition to their frozen targets.

Thus each step

`S_k -> S_{k+1}`

contains exactly one tagged-marker transition event.

Also run the reverse perturbation order using the same frozen target map as an order-control experiment. The final occupancy should agree; intermediate count fields may differ because intermediate configurations differ.

Do not call this sequence rotation, shear, stretch, or displacement in the theorem layer. Those are future calibration interpretations only.

---

# 13. Response atlas

For every frozen configuration `S_k`, compute and persist:

1. `C_n^{a_i}(x)` for every tagged source required by the registry;
2. multi-source `C_n^S(x)`;
3. window visits `V_[0,T]`;
4. pair endpoint spectra `W_n(i,j)`;
5. pair recoalescence spectra `R_n(i,j)`;
6. window recoalescence `R_K(i,j)`;
7. total aggregates `R_n^TOTAL`, `R_K^TOTAL`;
8. exact count ratios as optional derived rational fields;
9. support-only A1 baseline;
10. signed deltas from `S_k` to `S_{k+1}`.

Never retain only normalized ratios; raw integer numerators and denominators are primary.

---

# 14. Exact invariant / compensation search

Do **not** invent an energy function in this stage.

Search only exact integer statements.

For each perturbation step and each frozen horizon/window, classify:

### C0 — CELLWISE INVARIANT
`C_n^{S_{k+1}}(x)=C_n^{S_k}(x)` for every observed packet.

### C1 — CELL MULTISET INVARIANT
The multiset of cell counts is unchanged, though packet labels carrying the counts may change.

### C2 — PAIR ENDPOINT-SPECTRUM INVARIANT
All or the multiset of `W_n(i,j)` are unchanged.

### C3 — RECOALESCENCE TABLE INVARIANT
All labeled `R_n(i,j)` are unchanged.

### C4 — RECOALESCENCE MULTISET INVARIANT
Pair identities may exchange values but the multiset is unchanged.

### C5 — TOTAL RECOALESCENCE INVARIANT
`Delta R_n^TOTAL=0` or `Delta R_K^TOTAL=0`.

### C6 — MULTIPAIR EXACT COMPENSATION
Individual pair recoalescence counts change with both positive and negative deltas, but the relevant total aggregate is exactly unchanged.

This is the strongest direct first-stage candidate for the user's “many rubber bands bargain against one another” picture.

Report the full signed decomposition; do not report only the zero sum.

---

# 15. Micro-reconfiguration versus macro-stability diagnostic

For each step quantify exact integer reconfiguration without turning it into an energy:

- number of packets with nonzero `Delta C_n`;
- `sum_x |Delta C_n(x)|` as a count-change magnitude;
- number of labeled pairs with nonzero `Delta W_n`;
- number of labeled pairs with nonzero `Delta R_n`;
- positive-delta total and negative-delta total separately;
- whether any C0-C6 invariant class holds.

A scientifically interesting result is of the form:

`MICRO_COUNT_RECONFIGURATION_NONZERO`

with simultaneously

`MACRO_INTEGER_INVARIANT_EXACT`.

Do not require this result; a negative result is valid.

---

# 16. Raw-history identity versus branch recoalescence

CPBC storage may merge branches that occupy the same packet at the same epoch, but this must never be described as the raw histories becoming identical.

The count `C_n(x)=m` means there are `m` distinct raw histories represented by that branch-count state unless raw enumeration shows otherwise under an explicitly stronger equivalence.

Required firewall:

`RECOALESCED_STORAGE != NATIVE_HISTORY_EQUALITY`.

No path cancellation or quotienting of distinct raw histories is permitted.

---

# 17. Stage 0 — semantic freeze and tiny exact oracle

Before running the large aligned-sheet experiment, freeze:

1. `R059C_CPBC_SEMANTIC_PROTOCOL.json`
2. `R059C_BRANCH_RECOALESCENCE_COUNT_PROTOCOL.json`
3. `R059C_PATH_CLOUD_COUNT_FIELD_PROTOCOL.json`
4. `R059C_RECOALESCENCE_COUNT_PROTOCOL.json`
5. `R059C_COUNT_RATIO_PROTOCOL.json`
6. `R059C_ALIGNED_SHEET_CARRIER_PROTOCOL.json`
7. `R059C_REMOTE_PERTURBATION_PROTOCOL.json`
8. `R059C_SEMANTIC_CLAIM_LEDGER.json`
9. `R059C_COMPUTATION_REGISTRY.json`
10. deterministic Stage-0 checker output.

Tiny oracle requirements:

- explicit raw history enumeration;
- CPBC count equality to raw history multiplicities;
- Boolean support equality after positive-count thresholding;
- A3 count-spectrum coefficient equality;
- revisit / loop / immediate reversal cases;
- recoalescence of multiple distinct raw histories into one packet with multiplicity >1;
- self-consistency of count ratios.

Stage 0 must PASS before Stage A.

---

# 18. Stage A — aligned-sheet experiment

After Stage-0 PASS only:

1. freeze the size/horizon/padding registry;
2. construct all `S_k` configurations under the frozen remote schedule;
3. compute exact CPBC path-cloud fields;
4. compute pair endpoint spectra and recoalescence counts;
5. perform padding independence checks;
6. produce the response atlas;
7. classify every exact invariant/compensation C0-C6;
8. compare forward/reverse perturbation schedules;
9. compare across sheet sizes and horizons without post-selection;
10. stop at a frozen Stage-A checkpoint.

No Stage B or physical interpretation work is authorized.

---

# 19. Required Stage-A artifacts

At minimum return:

1. `R059C_CPBC_EXACTNESS_ATLAS.json`
2. `R059C_ALIGNED_SHEET_REGISTRY.json`
3. `R059C_REMOTE_SEQUENCE_REGISTRY.json`
4. `R059C_PATH_CLOUD_RESPONSE_ATLAS.json`
5. `R059C_PAIR_PATH_SPECTRUM_ATLAS.json`
6. `R059C_RECOALESCENCE_RESPONSE_ATLAS.json`
7. `R059C_COUNT_RATIO_ATLAS.json`
8. `R059C_PADDING_INDEPENDENCE_AUDIT.json`
9. `R059C_INTEGER_INVARIANT_COMPENSATION_LEDGER.json`
10. `R059C_COLLAPSE_ALGEBRA_CROSSCHECK.json`
11. `R059C_STAGE_A_CHECKER_OUTPUT.json`
12. `R059C_STAGE_A_COUNT_BRC_CHECKPOINT.json`
13. concise `R059C_STAGE_A_REPORT.md`.

All outputs must be deterministic from the frozen registry.

---

# 20. Mandatory negative/self-test gates

The checker must deliberately reject at least these mutations:

1. calling `PATH_COUNT` geometric length;
2. restricting paths to shortest paths without authorization;
3. calling Boolean support count-preserving;
4. merging branches and dropping multiplicity;
5. dividing counts and calling the ratio physical probability;
6. using floating probability as primary storage instead of exact integer counts/rationals;
7. interpreting `R_n(i,j)` as force/attraction/energy;
8. introducing Euclidean distance/angle/rotation into the theorem premise;
9. moving more than one remote marker in one elementary perturbation step;
10. choosing perturbation targets/order after seeing results;
11. using boundary-contaminated cases as stability evidence;
12. quotienting distinct raw histories because they recoalesced;
13. reading/consuming R059P research artifacts;
14. reading/consuming R059L research artifacts;
15. claiming quantum or zero-point motion explained.

---

# 21. Return dispositions

Return exactly one primary Stage-A disposition:

### `COUNT_BRC_MACRO_INTEGER_STABILITY_FOUND`
Use only if substantial micro path-cloud reconfiguration coexists with exact, non-post-selected C2-C6 invariant/compensation structure across more than one frozen size/horizon case and survives padding checks.

### `COUNT_BRC_LOCAL_RESPONSE_ONLY_NO_MACRO_INVARIANT`
Use if counts respond deterministically but no convincing exact higher-level invariant/compensation survives.

### `COUNT_BRC_BOUNDARY_OR_FINITE_SIZE_DOMINATED`
Use if retained results cannot be separated from finite carrier/padding effects.

### `MIXED_COUNT_BRC_STABILITY_STRUCTURE`
Use if robust exact invariant regimes and clearly non-invariant regimes coexist in the frozen registry.

Also return separate statuses:

- `COUNT_PRESERVING_BRANCHING_COLLAPSE_EXACTNESS`
- `RECOALESCENCE_COUNT_STABILITY`
- `MULTIPAIR_EXACT_COMPENSATION`
- `EQUIPATH_COUNT_RATIO_DEFINED`
- `PHYSICAL_PROBABILITY_FROM_COUNTING`
- `PHYSICAL_ATTRACTION_BRIDGE`
- `ROTATION_RIGIDITY_BRIDGE`
- `QUANTUM_BRIDGE`

Unless independently proved, the final four physical bridges remain `OPEN / NOT_ESTABLISHED`.

---

# 22. Scientific kill criteria

A negative result is successful if any of these holds:

- CPBC count compression fails to match raw-history multiplicity;
- useful exact invariants disappear once multiplicity rather than Boolean support is retained;
- apparent stability is entirely due to carrier automorphism/relabeling or artificial boundary effects;
- total recoalescence changes monotonically or irregularly with every remote move and no exact compensation survives;
- stable count ratios exist only because a regular carrier gives trivial uniform branching;
- results depend strongly on one hand-picked horizon or sheet size;
- the count-ratio construction has no justification as physical probability beyond equipath combinatorics.

Do not rescue the hypothesis by fitting weights, redefining the perturbation schedule, or introducing geometry after seeing results.

---

# 23. Hard prohibitions

Throughout Stage 0/A, prohibit:

- LINE
- STRAIGHTNESS
- DISTANCE
- LENGTH
- SHORTEST PATH
- GEODESIC
- EDGE/BOUNDARY GEOMETRY
- ANGLE
- ROTATION ANGLE
- DISPLACEMENT VECTOR
- RADIUS
- AREA
- VOLUME
- EUCLIDEAN METRIC PREMISE
- FORCE
- ENERGY
- STRAIN
- ATTRACTION AS ASSUMPTION
- PHYSICAL PROBABILITY AS ASSUMPTION
- QUANTUM AMPLITUDE / WAVEFUNCTION AS EXPLANATION
- ZERO-POINT MOTION CLAIM
- PATH RANKING
- PATH CANCELLATION
- RAW-HISTORY QUOTIENT
- RESULT-DEPENDENT CARRIER / HORIZON / SCHEDULE SELECTION
- R059L artifact consumption
- R059P artifact consumption.

---

# 24. Stop condition

After Stage-A artifacts, deterministic checker, response atlas, and frozen checkpoint are complete:

`STOP_FOR_DRIVER_REVIEW`.

Do not proceed to:

- probability calibration;
- energy/force construction;
- atom model;
- elasticity/rigidity;
- rotation interpretation;
- quantum comparison;
- history-dependent dynamics.

Those require a new Driver task after the integer count experiment is reviewed.
