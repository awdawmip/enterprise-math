# R059D Stage J REISSUE — BRC6 Next-Channel Selection Algebra

Task-ID: `RS-R059D-STAGE-J-BRC6-NEXT-CHANNEL-SELECTION-ALGEBRA`
Generation: `R059D`
Status: `DRIVER_APPROVED_REISSUE_TASKBOOK`
Date: `2026-08-15`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`
Identity policy: `AUTO_RESOLVE_OR_ALLOCATE`
Identity lane: `R059D`

## 0. Supersession and scientific correction

This taskbook supersedes before execution:

`research_tasks/R059D_STAGE_J_GRADED_RELAY_COUPLING_LOCALIZATION_20260815.md`

Superseded source:

`4cf097ff21a9275805fb8ab49cefdd5ff42c4c92`

Supersede note:

`research_tasks/R059D_STAGE_J_GRADED_RELAY_COUPLING_LOCALIZATION_SUPERSEDED_20260815.md`

The Driver correction is fundamental:

> We are not trying to algebraize length / response range. The aligned-step length readout is simply a count of cells and is frozen. The unknown to algebraize is the choice of the NEXT relational channel/direction. Construct a BRC function with six possible results, then test it.

Therefore Stage J is reset around a six-outcome selector.

Do **not** continue the graded-localization search.

All Stage A-I artifacts remain immutable historical results. Stage E-I relay/localization conclusions are side findings and are **not premises** for the BRC6 direction-selector result.

Frozen provenance parent:

`03650b38df5950b86cb2636db9e43094683b1bc8`

## 1. BRC symbol policy

Treat `BRC` as the user-selected symbol.

Do **not** invent or freeze an expansion of the acronym in this stage.

Define only:

`BRC6 = six-outcome next-channel selector`.

Its codomain is the declared six-channel label set:

`C6 = {0,1,2,3,4,5}`.

The labels are relational labels only.

They are **not** native:

- angles;
- directions in Euclidean space;
- left/right/straight/opposite;
- displacement vectors;
- slopes;
- curvature classes.

A result `d in C6` means only:

`SELECT NEXT DECLARED CHANNEL LABEL d`.

## 2. Length / cell-count correction

Freeze a separate readout:

`ALIGNED_SEGMENT_CELL_COUNT = L`.

`L` is the exact number of declared cells/packets in one aligned-to-aligned segment under the frozen carrier convention.

For every six-way decision state used as positive BRC evidence:

`ALIGNED_SEGMENT_CELL_COUNT(d) = L`

for every candidate `d in C6`.

Thus all six candidate next segments have the **same** frozen cell count.

Consequences:

- cell-count length is not a selector variable;
- BRC6 may not choose a channel because one candidate has fewer/more cells;
- no shortest/longest-path objective;
- no attenuation-distance interpretation;
- no search for a length threshold;
- no macro/micro boundary may be inferred from `L` in this stage.

If an implementation accidentally gives different candidate segment cell counts, classify:

`UNEQUAL_LENGTH_CONTAMINATION`

and reject that case from BRC evidence.

Revisit/loop/raw-history transition count may still differ inside a path cloud; that does not redefine the frozen aligned-segment cell-count readout.

## 3. Active native basis

Use only the current packet/path foundation:

- CRYSTAL PACKET with `UNIT_PACKET=1`;
- declared ADJACENCY / channel relations;
- TRANSITION EVENT;
- PATH as adjacency transition history;
- PACKET COUNT;
- PATH / TRANSITION COUNT;
- optional declared C6 ingress/egress relational labels;
- exact natural-number CPBC/path multiplicity semantics already inherited by R059D.

Do not reopen R059C.

Do not consume R059P or R059L.

Do not use Stage E-I relay/localization results as selector premises.

## 4. Core Stage-J object

At a frozen aligned decision state `sigma`, let current ingress channel label be

`i(sigma) in C6`

when an ingress label is declared.

Let the six candidate next-channel labels be

`d in C6`.

Construct for every candidate `d` an exact algebraic/count signature

`Z_d(sigma)`.

Then construct a selector

`BRC6(sigma) in C6`.

The scientific unknown is the algebraic rule producing this one six-valued result.

The output is a **channel choice**, not a length.

## 5. Required channel-signature ladder

Before constructing the final selector, freeze and test progressively richer exact signatures.

### J-S0 — current C6 incidence state

May include only declared current relational state such as:

- `INGRESS_CLASS`;
- exact current channel incidence counts `I[d]`, `O[d]`;
- exact current passage counts `M[a,b]` if declared.

Same-channel ingress/egress remains legal.

### J-S1 — one-step candidate count signature

For each candidate `d`, include exact current counts on the candidate launch packet / declared one-step neighborhood after selecting `d`.

No geometry.

### J-S2 — finite exact continuation count spectrum

For pre-frozen counting horizons `K`, compute candidate-specific exact tuples such as

`(C_0^d, C_1^d, ..., C_K^d)`

or equivalent coefficient/generating-carrier representation.

`K` is a counting horizon only; it is not line length.

### J-S3 — candidate visit / support spectrum

May include exact:

- visit-count tuples;
- support bits derived from positive integer counts;
- count-spectrum multiplicities.

### J-S4 — candidate recoalescence spectrum

May include exact `RECOALESCENCE COUNT` readouts already semantically allowed by R059D, provided the word `recoalescence` is used and no force/energy/probability meaning is assigned.

For every signature family record whether it adds genuine six-way discriminating power.

## 6. Relative C6 representation

Prefer a cyclic-label-covariant representation.

Let

`tau(d)=d+1 mod 6`

be the declared cyclic relabeling action on channel labels.

When ingress `i` is available, the selector may be represented in relative form:

`BRC6(sigma) = i(sigma) + beta(NORM_i(sigma)) mod 6`

with

`beta(...) in Z/6Z`.

This is algebraic label arithmetic only.

Do not call `beta` a turn angle.

Same-channel continuation corresponds simply to relative class `0` and remains legal.

## 7. Mandatory covariance / no-label-bias theorem

A valid BRC6 candidate must satisfy exact cyclic covariance:

`BRC6(tau*sigma) = tau(BRC6(sigma))`.

More generally, for every declared channel-label automorphism `pi` in the frozen carrier registry:

`BRC6(pi*sigma) = pi(BRC6(sigma))`.

Hard reject:

- choose smallest numeric channel label on a tie;
- choose label 0 by default;
- fixed absolute preferred channel;
- hidden label-order priority;
- result-specific target leakage.

Freeze:

`NO_ABSOLUTE_CHANNEL_LABEL_BIAS`.

## 8. Symmetry obstruction gate

A deterministic equivariant six-way selector cannot uniquely choose one label from a state whose full controller-visible algebraic signature is invariant under a nontrivial channel-label automorphism that moves that label.

Therefore distinguish two cases:

1. signature genuinely breaks channel symmetry -> a unique BRC6 result may exist;
2. signature remains exactly symmetric -> do **not** invent a channel choice.

For case 2 classify evaluator verdict:

`BRC6_UNRESOLVED_BY_CURRENT_SIGNATURE`

This verdict is **not** a seventh BRC output. It means the state is outside the proven deterministic selector domain.

Prove the strongest exact symmetry-obstruction statement supported by the frozen grammar.

## 9. BRC6 construction families

Construct and compare exact algebraic selector families. At minimum include:

### F0 — primitive count extremum controls

Shared candidate function applied identically to all six labels, with exact unique-extremum selection where defined.

Test both polarity controls if needed; do not assign physical meaning to larger/smaller count.

### F1 — lexicographic count-spectrum selector

Use the same ordered count-spectrum coordinates for every candidate label.

A candidate may win only by exact lexicographic comparison of its algebraic tuple.

### F2 — shared integer polynomial / expression selector

Freeze a finite expression grammar `P_theta(Z_d)` with integer coefficients/constants.

The same expression must be applied to every `d`.

Search only pre-frozen bounded coefficient/expression registries.

Return a channel only when one candidate is the exact unique extremum under the frozen polarity.

Record coefficient-box robustness; chosen fine-tuning must not be presented as unique naturalness.

### F3 — exact pairwise comparison/tournament selector

Optional if useful. Pairwise comparison must itself be label-covariant and derived from exact integer signatures.

Return a unique channel only when the frozen exact tournament criterion produces one.

Do not use random tie-breaking.

## 10. Six-outcome coverage gate

The final preferred BRC6 construction must demonstrate all six outputs on a frozen registry.

The preferred method is covariance, not six hand-coded cases:

- freeze one asymmetric base witness `sigma_*` with unique output `d_*`;
- apply all six cyclic relabelings;
- prove the six relabeled cases produce all six channel labels exactly.

Freeze:

`BRC6_SIX_OUTCOME_SURJECTIVITY_ON_FROZEN_REGISTRY`.

Reject a rule that only ever outputs a strict subset of C6 unless the result is explicitly reported as partial.

## 11. Tiny exact construction gate

Before large-system testing, use tiny deterministic relational carriers to prove:

- exact six-candidate signature construction;
- exact BRC6 evaluation;
- cyclic covariance;
- six-output coverage;
- symmetry-unresolved hard negative;
- no length leakage;
- same-channel output allowed;
- immediate reversal channel label may be output if the frozen algebra selects it; do not prohibit it geometrically.

No Monte Carlo.

## 12. Large-system test — direction only

After BRC6 construction passes tiny gates, test on large aligned tagged carriers, including a symbolic system-size stress around

`N ~ 10^36`

and frozen nearby integers.

Important:

- `N` is system/tag/packet scale only;
- `N` is not line length;
- aligned segment cell count `L` stays frozen and equal across all six candidate channels inside each test carrier;
- do not search for a length threshold;
- use exact compressed integer/count algebra, never enumerate `10^36` objects.

Test whether the same BRC6 algebra remains exact/covariant at huge N.

## 13. Repeated next-channel dynamics

Once a valid BRC6 exists, iterate aligned decisions:

`d_{k+1} = BRC6(sigma_k)`.

Every aligned segment retains the same frozen cell count `L`.

Record exact sequences:

`d_0,d_1,d_2,...`

and relative C6 label sequence when ingress is declared:

`r_k = d_{k+1}-d_k mod 6`.

These are relational label sequences only.

Classify exact algebraic behavior such as:

- fixed channel-label class under relabeling;
- finite channel cycle;
- longer recurrent word;
- state-dependent nonperiodic behavior within proved finite range;
- unresolved symmetry states.

Do not call these straight/curved/rotating trajectories.

## 14. Direction-selection perturbation tests

After the baseline BRC6 function is frozen, perturb only algebraic/count inputs, not segment cell count.

Examples:

- add/remove one admissible raw-history count token;
- change one local channel-incidence count by an exact legal event;
- single tagged adjacency perturbation before a decision node.

Measure:

`DELTA_BRC6 = selected channel label change / no change`.

Build exact six-way response table.

Do not interpret as force, torque, elasticity, or probability.

## 15. Boundary and padding independence

All positive BRC6 evidence must pass boundary/padding independence.

If a candidate channel signature or selected label changes because finite computation truncation/boundary enters the decision neighborhood, classify:

`BOUNDARY_CONTAMINATED_BRC6`

and do not use it for structural conclusions.

## 16. Probability firewall

Even if candidate count magnitudes differ, do not call

`C_d / sum_e C_e`

physical direction probabilities.

If normalized ratios are diagnostically recorded, call only:

`EQUIPATH_COUNT_RATIO_BY_CHANNEL`.

Freeze:

`PHYSICAL_PROBABILITY_FROM_BRC_COUNTS = NOT_ESTABLISHED`.

BRC6 in this stage is an exact algebraic selector, not a quantum collapse claim.

## 17. Hard rejects

Reject any candidate relying on:

- unequal candidate segment cell counts;
- shortest/longest path;
- Euclidean angle;
- straight/turn/opposite semantics;
- vector displacement;
- absolute channel-number preference;
- random tie-break;
- target map leakage;
- hand-coded six-case lookup keyed by absolute label;
- N-specific or q-specific output table;
- floating equality/tolerance;
- physical probability assumption;
- Stage E-I relay attenuation/localization conclusion as the selector premise.

## 18. Required artifacts

Freeze at minimum:

1. `R059D_STAGE_J_BRC6_SEMANTICS_PROTOCOL.json`
2. `R059D_STAGE_J_FIXED_CELL_COUNT_PROTOCOL.json`
3. `R059D_STAGE_J_CHANNEL_SIGNATURE_PROTOCOL.json`
4. `R059D_STAGE_J_BRC6_FUNCTION_GRAMMAR.json`
5. `R059D_STAGE_J_BRC6_SYMMETRY_OBSTRUCTION.json`
6. `R059D_STAGE_J_BRC6_SIX_OUTCOME_COVERAGE.json`
7. `R059D_STAGE_J_BRC6_TINY_EXACT_REGISTRY.json`
8. `R059D_STAGE_J_BRC6_LARGE_N_REGISTRY.json`
9. `R059D_STAGE_J_BRC6_REPEATED_DIRECTION_DYNAMICS.json`
10. `R059D_STAGE_J_BRC6_PERTURBATION_RESPONSE.json`
11. `R059D_STAGE_J_BRC6_BOUNDARY_PADDING_GATE.json`
12. `R059D_STAGE_J_BRC6_TRIVIALITY_AND_LEAKAGE_LEDGER.json`
13. deterministic checker + output
14. `R059D_STAGE_J_REPORT.md`
15. artifact manifest
16. frozen checkpoint

## 19. Primary dispositions

Use the strongest justified exact disposition:

1. `BRC6_EXACT_EQUIVARIANT_SIX_OUTCOME_SELECTOR_FOUND`
2. `BRC6_PARTIAL_SELECTOR_WITH_EXACT_SYMMETRY_UNRESOLVED_STATES`
3. `BRC6_SELECTOR_FOUND_BUT_FINE_TUNED_TO_EXPRESSION_PARAMETERS`
4. `NO_EQUIVARIANT_BRC6_SELECTOR_FROM_TESTED_COUNT_SIGNATURES`
5. `BRC6_BOUNDARY_OR_LENGTH_CONTAMINATED`

Always preserve symmetry-negative cases and exact tie structures.

## 20. Interpretation firewall

Continue:

`PHYSICAL_DIRECTION_CALIBRATION = NOT_ESTABLISHED`

`PHYSICAL_PROBABILITY_FROM_BRC_COUNTS = NOT_ESTABLISHED`

`PHYSICAL_RIGIDITY_INTERPRETATION = NOT_ESTABLISHED`

`PHYSICAL_ELASTICITY_INTERPRETATION = NOT_ESTABLISHED`

`QUANTUM_BRIDGE = NOT_ESTABLISHED`

The output labels are relational channels only.

## 21. Stop condition

After semantic freeze, BRC6 construction, six-output/covariance/symmetry gates, large-system testing, repeated-direction dynamics, perturbation tests, checker, report, manifest and frozen checkpoint:

`STOP_FOR_DRIVER_REVIEW`.
