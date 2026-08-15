# RS-R059P — STAGE A NEUTRAL PATH-SPECTRUM ROBUSTNESS

Task-ID: `RS-R059P-STAGE-A-NEUTRAL-PATH-SPECTRUM-ROBUSTNESS`
Generation: `R059P`
Researcher-ID: `EM-R059P-8A2C7D`
Status: `DRIVER_APPROVED_TASKBOOK`
Date: `2026-08-15`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`

## 0. Frozen parent and lane firewall

First round is frozen at owner head:

`f1b8eda8db0e8e069d5caf69f0f7e57bc3ee0ac7`

All first-round R059P artifacts are immutable.

R059P remains independent from R059L. Do not read, consume, modify, or depend on any `R059L_*` artifact, theorem, checkpoint, branch, or result.

Allowed project-level authorities remain:

- `PACKET_PATH_FOUNDATION.md`
- `packet_path_foundation.json`
- `FOUNDATIONAL_LOGIC.md`
- `foundational_logic.json`
- `native_semantics_admissibility.json`

No geometry is introduced.

---

## 1. Frozen first-round results

Retain exactly:

1. For adjacency-preserving relabelings `phi`, finite path spectra satisfy
   `W_n(phi(a),phi(b)) = W_n(a,b)`.
2. On finite state space, symmetric state-only strict scalar descent cannot sustain a nontrivial cycle.
3. Exact elementary neutral cycles can exist when equality moves are permitted.
4. The first-round neutral witness used deliberately chosen weights and therefore proves existence, not robustness or physical naturalness.
5. Intrinsic activity-selection rule remains open.
6. Quantum / zero-point calibration remains open.

---

# 2. Scientific question

Determine whether neutral dynamic steady-state structure is:

- a robust consequence of path-spectrum combinatorics; or
- mainly a fine-tuned artifact of choosing special scalar coupling weights.

The primary target is not merely another equal-`E` cycle. Search for weight-independent or broad-class neutral structure.

---

# 3. Exact spectrum objects

For tagged marker configuration `S=(a_1,...,a_m)` and frozen finite transition-count window `K=[n_min,n_max]`, retain pair spectra

`S_K(a_i,a_j) = (W_n(a_i,a_j))_n`.

Define exact higher-level readout hierarchy:

### R0 — scalar coupling readout
For integer coefficient vector `c=(c_n)`:

`E_c(S)=sum_{i<j} sum_n c_n W_n(a_i,a_j)`

or another explicitly frozen integer pair model from the first-round registry.

### R1 — aggregate path-spectrum vector

`A_K(S) = ( sum_{i<j} W_n(a_i,a_j) )_n`.

If `A_K(S')=A_K(S)`, every shared linear coefficient vector `c` gives `E_c(S')=E_c(S)`.

### R2 — pair-spectrum multiset

`M_K(S) = multiset{ S_K(a_i,a_j) : i<j }`.

Equality preserves every pair-symmetric coupling rule depending only on spectrum class, not only linear weights.

### R3 — labeled-pair spectrum table

`L_K(S) = (S_K(a_i,a_j))_{i<j}`.

Equality is the strongest frozen path-coupling invariance in this stage.

These are N2/higher-level readouts. None changes N0.

---

# 4. Elementary dynamics

Retain the first-round elementary update unless a carrier-specific registry explicitly freezes another local rule:

- exactly one tagged marker makes exactly one declared adjacency transition;
- target packet must satisfy the declared occupancy rule;
- no shortest path, direction, displacement, distance, or geometry.

Build exact transition graphs under the following neutrality notions:

- `G_R0(c)`: elementary edges with `E_c(S')=E_c(S)`;
- `G_R1`: elementary edges with `A_K(S')=A_K(S)`;
- `G_R2`: elementary edges with `M_K(S')=M_K(S)`;
- `G_R3`: elementary edges with `L_K(S')=L_K(S)`.

For each graph determine cycles, SCCs/connected neutral components, and whether they occur at global minima or only excited plateaus.

---

# 5. Fine-tuning theorem for linear scalar neutrality

For a fixed elementary move `S->S'`, define integer vector

`Delta A = A_K(S')-A_K(S)`.

Then

`E_c(S')-E_c(S)=c dot Delta A`.

Mandatory theorem target:

### PA-T01
If `Delta A != 0`, scalar neutrality for that move requires

`c dot Delta A = 0`,

so the neutral coefficient vectors in any finite integer coefficient box lie on an exact proper integer kernel slice.

Do not use continuum measure as a native premise.

For coefficient boxes

`C_B={c in Z_nonnegative^k : 0<=c_n<=B, c!=0}`

and optionally primitive vectors `gcd(c)=1`, compute exact finite fractions of coefficients producing neutrality. If proving asymptotic density `->0`, give a self-contained integer counting bound; do not merely appeal to a real hyperplane having measure zero.

### PA-T02
If `Delta A=0`, the move is neutral for every shared linear coefficient vector `c`; classify it as `WEIGHT_INDEPENDENT_R1_NEUTRAL`.

---

# 6. Strong robustness search

Search bounded relational carriers and marker counts for nontrivial elementary cycles at R1/R2/R3.

Use several non-geometric relational carrier families, for example finite cycles, complete relational carriers, tree-like carriers, and small regular adjacency carriers. Names/labels are implementation only.

At minimum vary:

- carrier size;
- 2, 3, and where tractable 4 tagged markers;
- at least two path-count windows;
- occupancy exclusion on/off only when explicitly typed;
- several bounded integer coefficient boxes for R0 robustness diagnostics.

Do not select one carrier/weight after seeing results and report it as generic.

Freeze the entire bounded registry before expensive enumeration.

---

# 7. Minimum-basin requirement

Persistent microscopic activity intended as a steady-state mechanism is much stronger if neutral cycles occur in the minimum coupling basin.

For every scalar model examined, compute exactly:

`E_min = min_S E(S)`

and classify every neutral cycle/component as:

- `GLOBAL_MINIMUM_NEUTRAL`
- `LOCAL_MINIMUM_NEUTRAL`
- `EXCITED_PLATEAU_ONLY`

A cycle existing only on an excited plateau is not evidence for equilibrium persistent activity without an additional drive/selection mechanism.

For R1/R2/R3, separately report whether the invariant cycle intersects or lies entirely inside scalar minima across broad coefficient classes.

---

# 8. Many-rubber-band cancellation diagnostic

For each one-marker neutral move, decompose total pair change by pairs incident to the moved marker.

Classify:

- `PAIRWISE_INVARIANT`: every affected pair spectrum is unchanged;
- `MULTIPAIR_EXACT_CANCELLATION`: individual pair readouts change but aggregate R1 is unchanged;
- `SCALAR_WEIGHT_CANCELLATION_ONLY`: aggregate spectrum changes but chosen scalar E is unchanged.

The second class is the most direct discrete realization of the user's “many rubber bands bargain against one another” idea.

Quantify how often each class occurs in the frozen registry.

---

# 9. Automorphism versus genuinely local neutrality

Separate:

- collective carrier-automorphism degeneracy;
- elementary local R1/R2/R3-neutral moves;
- cycles generated only after several elementary steps.

Do not claim that automorphism degeneracy itself supplies a dynamics.

---

# 10. Stage-A dispositions

Return exactly one primary disposition:

### `ROBUST_WEIGHT_INDEPENDENT_NEUTRAL_ACTIVITY_FOUND`
Use only if nontrivial elementary neutral cycles are found at R1 or stronger across more than an isolated hand-selected carrier and survive the frozen robustness checks, preferably including minimum-basin examples.

### `NEUTRAL_ACTIVITY_PRIMARILY_FINE_TUNED_OR_EXCITED`
Use if cycles occur mainly through special scalar weights / proper kernel slices or only excited plateaus, with no convincing R1+ minimum-basin cycle family.

### `MIXED_NEUTRAL_ROBUSTNESS_STRUCTURE`
Use if both robust structural and fine-tuned regimes occur and neither dominates the frozen registry.

Also return separate exact status for:

- `INTRINSIC_ACTIVITY_SELECTION_RULE`
- `PATH_HISTORY_MEMORY_NEEDED_OR_NOT_NEEDED`
- `QUANTUM_BRIDGE`

Do not promote any of these unless proved.

---

# 11. If R1+ robust cycles are absent

Do NOT broaden weights indefinitely.

If the exact evidence says weight-independent neutral activity is absent/rare, the next generation should test history-dependent coupling or an enlarged state `(configuration, explicit path-memory)`.

That negative result is scientifically valuable.

---

# 12. If R1+ robust cycles are found

Do NOT immediately call them zero-point motion.

The next question becomes intrinsic transition selection and persistence statistics without external drive.

---

# 13. Hard prohibitions

Forbidden:

- LINE
- STRAIGHTNESS
- DISTANCE
- LENGTH
- SHORTEST PATH
- GEODESIC
- ANGLE
- EDGE / BOUNDARY geometry
- AREA / VOLUME
- Euclidean embedding as premise
- physical atom/energy promoted into N0
- zero-point motion claimed explained
- quantum terminology used as proof
- R059L artifact consumption
- tuning weights after holdout registry results and then calling them generic
- continuum probability measure used to define genericity

---

# 14. Required artifacts

At minimum freeze:

1. `R059P_STAGE_A_ROBUSTNESS_REGISTRY.json`
2. `R059P_NEUTRALITY_HIERARCHY_PROTOCOL.json`
3. `R059P_INTEGER_WEIGHT_KERNEL_THEOREM.json`
4. `R059P_WEIGHT_BOX_ROBUSTNESS_ATLAS.json`
5. `R059P_R1_R2_R3_NEUTRAL_CYCLE_ATLAS.json`
6. `R059P_MINIMUM_BASIN_NEUTRALITY_ATLAS.json`
7. `R059P_MULTIPAIR_CANCELLATION_ATLAS.json`
8. `R059P_AUTOMORPHISM_LOCAL_NEUTRALITY_SEPARATION.json`
9. `R059P_STAGE_A_THEOREM_LEDGER.json`
10. deterministic exact checker output
11. `R059P_STAGE_A_CHECKPOINT.json`

Return SHA256 for all frozen artifacts and stop for Driver review.
