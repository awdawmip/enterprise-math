# R055 Problem Packet — Fixed-N Gravity Relaxation and Self-Centered Shape Formation

Status: `FROZEN PROBLEM PACKET / NEW MOTHER QUESTION / NOT CANONICAL`

## 0. Motivation

R053/R054 start from externally prescribed teacher-circle clusters and then study boundary-collapse readouts. They do **not** test whether a fixed number of triangular-lattice cells, allowed to rearrange on the lattice while preserving cell count, connectivity and topology, will self-organize around its own center of mass into a uniquely selected compact shape.

R055 isolates that missing layer.

The new causal direction is:

`fixed cell count N -> admissible lattice rearrangements -> centroid feedback -> relaxed cluster -> emergent center/shape -> only then external circle/hexagon comparison`.

The key question is not "how well does a teacher circle cut the lattice?" but:

> For equal-mass cells on the triangular lattice, if boundary cells may be relocated through a frozen local relaxation rule and the centroid is recomputed after every accepted move, what terminal shapes are selected? Do they become increasingly isotropic/circle-like, remain hexagonal/Wulff-like, depend on the initial shape, or exhibit multiple metastable attractors?

No classical pi, circle radius, teacher center, circumference target or Euclidean-circle loss may participate in the relaxation objective or move selection.

## 1. Fixed substrate and typing

Use the normalized triangular lattice

`Lambda = {a e1 + b e2 : a,b in Z}`

with

- `e1=(1,0)`;
- `e2=(1/2,sqrt(3)/2)`;
- exact axial squared norm `Q(a,b)=a^2+a*b+b^2`;
- six nearest-neighbor adjacency directions;
- one equal mass per occupied lattice cell.

A cluster `C` is a finite occupied subset of lattice sites.

For this task, the affine/Euclidean lattice realization is an explicitly declared **task-level operational geometry** used to define centroid and quadratic moment. It is not to be promoted into a claim that Euclidean geometry or gravity is N0-native. Native-Semantics Gate V3 still governs any ontology language.

Keep the physical cell scale symbolic as `ell_0`.

## 2. Fixed-N admissible state space

For each frozen `N`, study clusters satisfying:

- `|C|=N` exactly;
- nearest-neighbor connectedness;
- hole-free topology: the complement has no finite connected component fully enclosed by `C` under the declared dual/exterior test;
- clusters are compared modulo translation and D6 where appropriate, with orientation metadata retained when needed.

Do not allow cells to leave lattice sites or continuously slide off-lattice.

## 3. Center of mass and exact gravity-compaction energy

For equal masses define

`g(C) = (1/N) * sum_{x in C} x`.

After **every accepted move**, recompute `g(C)` from the new cluster. Never freeze the initial center.

Primary gravity-compaction objective:

`I2(C) = sum_{x in C} ||x-g(C)||^2`.

Use the exact identity

`I2(C) = (1/N) * sum_{unordered {x,y} subset C} ||x-y||^2`.

Since squared lattice distances are given by `Q`, the scaled energy

`G(C) := N * I2(C)`

is an exact integer pairwise sum. Prefer `G(C)` for exact comparison and checker logic.

Interpretation: this is a quadratic self-centering / compaction potential, not Newtonian inverse-square gravity. Do not claim the Newtonian gravitational field zero coincides with the centroid in arbitrary configurations.

## 4. Boundary and admissible rearrangements

Freeze and compare two dynamics; never conflate them.

### D1 — LOCAL_BOUNDARY_SLIDE

A move replaces one occupied boundary cell `u` by one empty nearest-neighbor lattice site `v` adjacent to `u`, producing

`C'=(C\{u}) union {v}`.

The move is admissible only if:

- `|C'|=N`;
- `C'` is connected;
- `C'` is hole-free;
- `u` is on the occupied boundary;
- `v` is a lattice site and belongs to the exterior frontier after removal;
- the move is not a pure translation of the entire cluster.

### D2 — GLOBAL_BOUNDARY_RELOCATION_REFERENCE

Remove any admissible boundary cell `u` and add any admissible exterior-frontier site `v`, again preserving `N`, connectedness and hole-free topology.

This is a nonlocal reference optimizer used to diagnose whether D1 is trapped in local minima. It is not to be described as a physical local slide.

### Strict-descent rule

For the primary gravity relaxation, accept only moves with

`G(C') < G(C)`.

When several admissible moves have equal best improvement, use one frozen canonical tie-break based on translation/D6-canonical state encoding; also run deterministic alternative tie-breaks as a path-dependence control.

No plateau move is allowed in the primary dynamics. Plateau-enabled exploration, if tested, is a separately labeled diagnostic.

## 5. Separate objective families — do not define "round" by one hidden metric

R055 must keep the following objectives/diagnostics separate before any comparison:

### O1 — Gravity compaction

`G(C)=N I2(C)` as above.

### O2 — Raw lattice boundary size

`P_edge(C)=|delta(C)|`, the number of occupied-to-empty nearest-neighbor cut edges.

This is a control objective. A perimeter minimizer may favor a hexagonal/Wulff shape because the lattice boundary energy is anisotropic. Never call `P_edge` minimization "roundness" by definition.

### O3 — Inertia anisotropy diagnostic

Let `M(C)` be the centered 2x2 second-moment matrix. Record a scale-free anisotropy such as

`A2(C)=((Mxx-Myy)^2+4*Mxy^2)/(trace(M)^2)`

when `trace(M)>0`.

`A2=0` means second-moment isotropy. It is a diagnostic unless separately frozen as an optimization objective in a dedicated arm.

### O4 — Radial-shell dispersion diagnostic

For boundary-cell centers or a separately frozen boundary-anchor convention, define exact squared radii

`q_i = ||b_i-g(C)||^2`

and report normalized variance/spread of the `q_i`. Prefer squared-radius diagnostics so exact algebraic arithmetic can be retained.

### O5 — Directional boundary imbalance

Record occupancy/exposed-edge counts across the six lattice directions and a normalized six-direction imbalance.

Do not combine O1–O5 into one weighted objective after seeing results. If a combined objective is ever desired, it is a later generation with pre-frozen weights.

## 6. Frozen N regimes

Use three regimes.

### Small-N exhaustive regime

Attempt exact enumeration of all connected hole-free clusters modulo translation+D6 for

`N = 1..12`,

and extend to larger `N` only if computationally cheap.

For every enumerated N, identify exact global minimizers/multiplicity for `G(C)` and `P_edge(C)` separately and build the state-transition graph under D1 where feasible.

### Construction / dynamics regime

Use

`N = [19, 31, 37, 53, 61, 79, 91, 113, 127, 151, 169, 199, 217]`.

These deliberately mix centered-hex shell counts and off-shell counts.

### Strict holdout N

Keep unopened until the relaxation rules, tie-breaks, initial-shape generators and diagnostics are frozen:

`N = [43, 67, 103, 139, 181, 241, 301]`.

No objective weight or move rule may be changed after inspecting holdout shapes.

## 7. Multi-start initial shapes

For every construction/holdout N, generate deterministic initial clusters from several structurally different families without using a circle target:

1. `HEX_SHELL_GROWTH`: graph-shell / hex-like compact growth with deterministic truncation;
2. `ELONGATED_STRIP`: long thin connected strip, folded deterministically if needed;
3. `SIX_ARM_STAR`: six-direction arm growth with deterministic fill order;
4. `L_SHAPE_OR_WEDGE`: strongly anisotropic compact connected shape;
5. `EDEN_SEEDED`: deterministic pseudo-random connected growth using pre-frozen integer seeds;
6. `COMPACT_BFS_ALT_TIE`: compact adjacency-first growth with a tie-break distinct from HEX_SHELL_GROWTH.

Freeze the exact generator and seed registry before relaxation.

Do not include a Euclidean disk/circle cut as a privileged starting shape in the primary study. A circle-cut initial condition may appear only later as a nonselective comparison control.

## 8. Primary experimental questions

For each N and initial family under D1 and D2 record:

- exact initial and terminal canonical states;
- move count;
- full `G(C_t)` sequence or compressed exact audit sufficient to verify strict descent;
- centroid path `g(C_t)`;
- total centroid displacement and final centroid class modulo the lattice fundamental cell;
- terminal `P_edge`, `A2`, radial-squared dispersion and directional imbalance;
- whether distinct initial states reach the same D6/translation equivalence class;
- whether different tie-breaks reach different terminal states;
- whether D1 terminal states are improved by D2;
- local-minimum versus exact-global-minimum status where small-N exhaustive truth is available.

Primary terminology:

- `D1_LOCAL_MINIMUM`: no admissible D1 move strictly lowers G;
- `D2_RELOCATION_MINIMUM`: no admissible D2 move strictly lowers G;
- `GLOBAL_G_MINIMUM`: proved only by exhaustive enumeration or theorem;
- `MULTIPLE_ATTRACTORS`: inequivalent terminal states from frozen multi-starts/tie-breaks;
- `UNIQUE_ATTRACTOR_OBSERVED`: bounded empirical observation only unless proved.

## 9. Exact theorem targets

At minimum prove/check the exact pairwise identity for `I2` and a termination theorem for strict-descent dynamics on the finite N-state quotient.

Serious targets include:

- characterization of one-step `Delta G` under a swap `u->v`;
- necessary exchange conditions for a global `G` minimizer;
- uniqueness or multiplicity classification for small N;
- proof/counterexample that every D1 minimum is also D2-minimal;
- proof/counterexample that D1 terminal state is independent of initial shape or tie-break;
- characterization of possible centroid classes of minimizers;
- asymptotic limit-shape theorem for global or D2 `G` minimizers;
- proof that gravity-moment minimizers approach an isotropic disk-like limit, or a counterexample/alternative limit shape;
- separation theorem/counterexample showing `G` minimizers differ from `P_edge` minimizers for infinitely many N or a declared family.

Do not infer an asymptotic theorem from finite images or regression.

## 10. Post-freeze external shape comparison only

Only after the relaxation rule, objective registry, initial families, construction results and strict-holdout terminal clusters are frozen may ordinary Euclidean comparison models be opened.

Then compare the normalized relaxed shapes with at least:

- equal-area Euclidean disk centered at `g(C)`;
- best aligned/rescaled regular hexagon;
- the corresponding raw `P_edge` minimizer/control where available.

Permitted comparison diagnostics include symmetric-difference area, normalized radial deviation, Hausdorff-style boundary discrepancy, second-moment ratio, and circularity/isoperimetric quotients.

Classical `pi` may appear here only as part of the **external comparison metric**. It must not retroactively select a relaxation rule, move, N, initial state, tie-break, or objective.

This stage asks whether "roundness" emerged. It does not define the primary dynamics.

## 11. Mandatory adversarial controls

At minimum attack and record:

- `CELL_COUNT_CHANGED_DURING_RELAXATION`;
- `CELL_LEFT_TRIANGULAR_LATTICE`;
- `CONNECTIVITY_BROKEN_BY_MOVE`;
- `HOLE_CREATED_OR_FILLED_WITHOUT_DECLARATION`;
- `CENTROID_NOT_RECOMPUTED_AFTER_ACCEPTED_MOVE`;
- `INITIAL_CENTER_FROZEN_AS_PRIVILEGED_CENTER`;
- `CLASSICAL_CIRCLE_USED_AS_RELAXATION_TARGET`;
- `PI_USED_IN_MOVE_OR_ENERGY_SELECTION`;
- `PERIMETER_MINIMUM_RELABELED_AS_ROUNDNESS`;
- `GRAVITY_MOMENT_MINIMUM_RELABELED_AS_CIRCLE_BY_DEFINITION`;
- `SINGLE_INITIAL_CONDITION_USED_TO_CLAIM_UNIQUE_ATTRACTOR`;
- `ONE_TIEBREAK_USED_TO_HIDE_PATH_DEPENDENCE`;
- `D1_LOCAL_MINIMUM_CALLED_GLOBAL_MINIMUM`;
- `D2_NONLOCAL_RELOCATION_CALLED_LOCAL_SLIDE`;
- `SMALL_N_EXHAUSTION_EXTRAPOLATED_AS_ALL_N_THEOREM`;
- `FINITE_LARGE_N_IMAGES_PRESENTED_AS_LIMIT_SHAPE_PROOF`;
- `CENTERED_HEX_COUNTS_ONLY_CHERRY_PICKED`;
- `POSTHOC_OBJECTIVE_WEIGHTING`;
- `UNEQUAL_CELL_MASS_INTRODUCED_AFTER_RESULTS`;
- `TRANSLATION_OR_D6_DUPLICATES_COUNTED_AS_DISTINCT_ATTRACTORS`.

## 12. Required artifacts

Return at least:

- `R055_REPORT.md`
- `R055_RELAXATION_PROTOCOL.json`
- `R055_MOVE_ENERGY_REGISTRY.json`
- `R055_INITIAL_STATE_REGISTRY.json`
- `R055_SMALL_N_EXHAUSTIVE_ATLAS.json`
- `R055_RELAXATION_TRAJECTORIES.json`
- `R055_TERMINAL_SHAPE_ATLAS.json`
- `R055_CENTROID_DYNAMICS_ATLAS.json`
- `R055_OBJECTIVE_COMPARISON.json`
- `R055_HOLDOUT_RESULTS.json`
- `R055_EXTERNAL_SHAPE_COMPARISON.json`
- `R055_THEOREM_COUNTEREXAMPLE_LEDGER.json`
- `R055_ADVERSARIAL_TEST_RESULTS.json`
- `R055_EXACT_CHECK_RESULTS.json`
- `R055_ARTIFACT_MANIFEST.json`
- executable checker/tests.

Freeze and return at minimum:

- `R055_RELAXATION_PROTOCOL_SHA256` before any construction relaxation;
- `R055_MOVE_ENERGY_REGISTRY_SHA256` before scoring moves;
- `R055_INITIAL_STATE_REGISTRY_SHA256` before running construction trajectories;
- `R055_THEOREM_COUNTEREXAMPLE_LEDGER_SHA256` before external circle/hexagon comparison;
- `R055_ARTIFACT_MANIFEST_SHA256` at final checkpoint.

## 13. Interpretation discipline

A positive result may say that a declared fixed-N equal-mass triangular-lattice relaxation rule selects compact self-centered shapes with measured isotropy/roundness properties.

Do not automatically claim:

- the universe is a triangular lattice;
- gravity is literally quadratic at the substrate;
- centroid is a native primitive;
- relaxed shapes are mathematically Euclidean circles without proof;
- minimum boundary and minimum moment are the same problem;
- one observed attractor is globally unique;
- a post-freeze match to a circle proves classical pi from the substrate.

The highest-value result is structural: determine whether center and shape can emerge jointly from fixed mass plus local lattice rearrangement, and exactly where locality, lattice anisotropy or metastability prevents uniqueness/circularity.