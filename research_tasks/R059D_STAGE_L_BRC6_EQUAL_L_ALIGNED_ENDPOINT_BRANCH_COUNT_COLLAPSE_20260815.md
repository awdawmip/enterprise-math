# R059D Stage L — Equal-L Aligned-Endpoint Branch-Count Collapse

Task-ID: `RS-R059D-STAGE-L-BRC6-EQUAL-L-ALIGNED-ENDPOINT-BRANCH-COUNT-COLLAPSE`
Generation: `R059D`
Status: `DRIVER_APPROVED_TASKBOOK`
Date: `2026-08-15`
Driver: `EM-DVR-R0457K / CONTROL_PLANE`
Researcher-ID: `EM-R059D-9C6B2A`
Identity policy: `FIXED_FOR_BRC6_LANE`

## 0. Frozen parent and Driver disposition

Stage K is frozen at owner head:

`fc8abf73f67a5793334905b9863cb5f7d2030d94`

All BRC6 Stage-J and Stage-K artifacts are immutable.

Driver accepts Stage K exactly at the following strength:

- `BRC6_SELECTOR_DEPENDENT_BUT_TRUE_STATE_DYNAMICS_FOUND`;
- `BRC6_SELECTOR_CANONICALITY = NOT_ESTABLISHED`;
- `BRC6_TOTAL_SELECTOR = NOT_ESTABLISHED`;
- `BRC6_SELECTOR_ROBUST_STATE_DOMAIN = ESTABLISHED_NONEMPTY`;
- `BRC6_SELECTOR_DEPENDENT_STATE_DOMAIN = ESTABLISHED`;
- true O/M/I state updates were executed on three pure-relational C6 port carriers;
- Stage-J profile-reuse periods are diagnostic only and are not full-state cycles;
- full exact-state recurrence at distinct resolved epochs is impossible in the frozen accumulating state because `TOTAL_O(e)=TOTAL_O(0)+e`;
- in the Stage-J affine continuation quotient, candidate-discrimination information saturates at `K=1` because `(C0,C1)` determines `(A,I)` and hence all deeper `C_n=A+nI`;
- `N~10^36` remains only a system-scale stress test and does not alter BRC6 comparisons under common-background addition;
- equal aligned-segment cell count remains frozen and is not optimized.

Stage K also reveals the central unresolved issue:

> the same exact state can be sent to different channel labels by different exact, cyclic-label-blind comparators. Therefore continuing to enumerate arbitrary score/comparator families cannot establish a canonical BRC6 law.

Stage L changes the question.

## 1. Scientific correction for Stage L

The user has fixed the semantic target:

- aligned-to-aligned segment cell count is already known and equal across the six candidates;
- the unknown is which of the six next channels is selected;
- the BRC6 selector should therefore be tied to a single exact combinatorial quantity at the **next aligned endpoint**, not to an arbitrary ordering of intermediate count-spectrum coordinates.

Stage L tests a count-mode collapse rule:

> among six equal-L candidate aligned segments, count the exact admissible branch/history multiplicity arriving at each candidate next aligned endpoint; select the unique largest endpoint branch class; exact ties remain unresolved.

This is a mathematical branch-count mode rule only. It is not physical probability.

## 2. Lane firewall

Continue only the BRC6 lane:

`Researcher-ID: EM-R059D-9C6B2A`.

Consume frozen parent only from:

`fc8abf73f67a5793334905b9863cb5f7d2030d94`.

Do not consume or depend on the old graded-relay Stage-J side lane owned by `EM-R059D-4C7E21`.

Do not reopen R059C, R059L or R059P.

No prior frozen artifact may be edited.

## 3. Foundation / geometry firewall

C6 labels remain relational channel labels only.

Do not introduce or infer:

- angle;
- straight / turn / opposite;
- displacement vector;
- Euclidean distance;
- shortest path;
- geometric length optimization;
- curvature;
- area / volume;
- physical force / torque / elasticity;
- physical probability.

`ALIGNED_SEGMENT_CELL_COUNT=L` remains an exact packet/cell count readout only.

## 4. Equal-L contract

For every positive Stage-L evidence state and every candidate `d in C6`:

`ALIGNED_SEGMENT_CELL_COUNT(d)=L`.

For the inherited frozen carriers use the same common value:

`L=4`.

Hard reject any evidence in which candidate segment counts differ.

Important distinction:

- Stage L may use the common aligned endpoint after exactly the frozen L-cell segment as the **evaluation boundary**;
- Stage L may not compare, rank, minimize or maximize L itself;
- L may not appear as a candidate-specific weight or score.

Freeze the semantic statement:

`EQUAL_L_ENDPOINT_EVALUATION_NOT_LENGTH_SELECTION`.

## 5. Exact endpoint branch count

For each decision state `sigma` and candidate channel `d`, define an exact nonnegative integer:

`B_d(sigma)`

with meaning:

> number of admissible declared branch/history instances in the frozen candidate continuation process that arrive at the candidate next aligned endpoint after the common equal-L segment.

No probability normalization is allowed.

### 5.1 Mandatory inherited affine control

First replay the inherited Stage-J affine continuation quotient exactly.

For candidate `d`:

`A_d = O[d] + M[i,d]`

`C_n^d = A_d + n I[d]`.

Under the inherited `L=4` convention, freeze the exact endpoint branch-count readout as the final aligned-boundary coordinate of that frozen segment. The task must state the index convention explicitly and prove it matches the four-cell segment bookkeeping. If the inherited convention implies `B_d=C_3^d`, say so and prove why; do not silently assume an off-by-one convention.

This replay is a control, not permission to alter L or the recurrence after seeing results.

### 5.2 Optional richer exact candidate microgrammar

Only if the inherited affine endpoint count is insufficient for a required theorem may one pre-freeze one additional finite C6-covariant candidate microgrammar whose sole output per channel is still one exact endpoint integer `B_d`.

Any such grammar must be frozen before scoring and must use only declared relational/count transitions. No candidate-specific table, target label leakage or geometry is allowed.

## 6. Stage-L collapse axioms — freeze before scoring

Freeze the following admissibility class before evaluating positive witnesses.

### L-A0 — C6 covariance

Under simultaneous cyclic relabeling `tau(d)=d+1 mod6`:

`B_(tau d)(tau sigma)=B_d(sigma)`.

Any resolved BRC6 output must satisfy:

`BRC6(tau sigma)=tau(BRC6(sigma))`.

### L-A1 — aligned-endpoint sufficiency

The positive Stage-L collapse selector reads only the six endpoint branch counts:

`(B_0,...,B_5)`

plus the current relational label frame required for covariance.

It may not inspect or lexicographically prioritize intermediate `C_0,C_1,...` coordinates once the endpoint counts have been formed.

This explicitly excludes Stage-J F1/reverse-lex/F2 spectrum tradeoff as the Stage-L positive rule.

### L-A2 — common-background invariance

For every exact integer `c>=0`:

`BRC6(B_0+c,...,B_5+c)`

must have the same resolved relative output/unresolved status as the original count vector.

### L-A3 — strictly increasing representation invariance

If the same strictly increasing integer-order embedding `g` is applied to every candidate count, unique winner identity must be unchanged.

This records that only the strict order of endpoint branch multiplicities matters, not an arbitrary numerical scaling.

### L-A4 — exact tie preservation

If the maximal endpoint branch count is attained by more than one channel, deterministic BRC6 must remain unresolved unless an independently pre-frozen endpoint observable breaks the tie.

No smallest-label, absolute-label, random or target-based tie break.

### L-A5 — branch-count monotonicity

If `d` is the unique branch-count winner and only `B_d` is increased, `d` must remain the resolved winner.

A rule where adding an admissible endpoint branch to the current unique winner causes it to lose is rejected from the positive count-mode class.

## 7. Preferred Stage-L BRC6 function

Define the partial count-mode selector:

`BRC6_COUNT_MODE(sigma)=d`

iff

`B_d(sigma) > B_e(sigma)` for every `e != d`.

Otherwise evaluator verdict:

`BRC6_UNRESOLVED_BY_ENDPOINT_BRANCH_COUNT`.

This verdict is not a seventh BRC6 output.

Do not claim this rule is the unique native law of nature. The strongest permitted semantic promotion is:

`CANONICAL_WITHIN_FROZEN_ENDPOINT_BRANCH_COUNT_COLLAPSE_AXIOMS`.

Continue to distinguish that from:

`BRC6_NATIVE_CANONICALITY`,

which remains not established unless a stronger theorem is actually proved.

## 8. Stage-K reconciliation

Re-evaluate at least the following frozen states using endpoint branch count only:

- `W_ASYM_BASE`;
- `W_CONSENSUS_DOMINANT2`;
- `W_FULLY_SYMMETRIC`;
- `W_S1_TIE_S2_RESOLVE`;
- `W_SIGNATURE_INSUFFICIENT_PAIRS`.

For each state record:

- exact vector `(B_0,...,B_5)`;
- Stage-K F1 output;
- Stage-K reverse-lex output;
- Stage-K endpoint-max output;
- Stage-L count-mode output;
- unresolved reason if any.

The fact that Stage-L count-mode may disagree with Stage-J F1 is not an error; it must be recorded as the consequence of the new endpoint-sufficiency semantic freeze.

## 9. Six-outcome coverage

Require exact six-output coverage for the Stage-L count-mode rule.

Preferred proof:

- one asymmetric base endpoint-count witness with unique count-mode winner `d*`;
- six cyclic relabelings produce all six outputs by covariance.

No hand-written six-label cases.

If exact symmetry or endpoint ties prevent total coverage in the frozen registry, report honestly and do not invent a tie break.

## 10. True state dynamics

Use the frozen Stage-K true state update exactly:

after resolving `d` at node `x` with ingress `i`:

`O_x[d] += 1`

`M_x[i,d] += 1`

traverse the declared equal-L segment,

`y=T_NODE(x,d)`

`j=T_INGRESS(x,d)`

`I_y[j] += 1`

then recompute all six endpoint branch counts from the new exact state.

Do this on all three frozen Stage-K relational carriers A/B/C.

Never reuse a normalized profile as the next state.

### Required trajectory outputs

For each carrier record:

- `d_0,d_1,...` under `BRC6_COUNT_MODE`;
- `r_k=d_(k+1)-d_k mod6`;
- first unresolved epoch, if any;
- exact accumulated state digest;
- TOTAL_O growth;
- any repeated channel-label projection word.

Do not call a repeated channel word a full-state cycle when TOTAL_O differs.

## 11. Perturbation tests

Under true Stage-L count-mode dynamics test the frozen perturbation classes:

- one exact launch/count token;
- one exact incidence increment;
- one real tagged adjacency launch-contribution transfer.

For each record:

- first BRC6 divergence epoch;
- whether baseline/perturbed output remains equal despite state delta;
- creation/removal of endpoint-count ties;
- unresolved creation/removal;
- any exact full-state recoalescence within the declared finite window.

No physical force/torque/probability language.

## 12. Large-N stress

Freeze a large-N registry including `N=10^36` and neighboring exact integers before scoring.

N remains only system/tag/packet scale.

If endpoint count vectors receive a common exact N background, prove exact cancellation/invariance symbolically.

No huge object/history enumeration.

No length threshold search.

## 13. Hard negative controls

At minimum include:

1. Stage-J F1 lex spectrum selector as non-authoritative historical control;
2. reverse-lex control;
3. one F2 coefficient selector that disagrees on W_ASYM_BASE;
4. endpoint MIN rule, which must be rejected by the Stage-L branch-count-mode orientation if it violates the declared positive monotonic/dominance semantics;
5. exact endpoint tie witness;
6. full cyclic symmetry witness;
7. boundary contamination inside the aligned endpoint count dependency window.

## 14. Required artifacts

At minimum freeze:

- `R059D_STAGE_L_EQUAL_L_ENDPOINT_PROTOCOL.json`
- `R059D_STAGE_L_ENDPOINT_BRANCH_COUNT_PROTOCOL.json`
- `R059D_STAGE_L_COLLAPSE_AXIOMS.json`
- `R059D_STAGE_L_COUNT_MODE_SELECTOR.json`
- `R059D_STAGE_L_STAGE_K_RECONCILIATION.json`
- `R059D_STAGE_L_SIX_OUTCOME_COVERAGE.json`
- `R059D_STAGE_L_TRUE_DYNAMICS_ATLAS.json`
- `R059D_STAGE_L_PERTURBATION_RESPONSE.json`
- `R059D_STAGE_L_LARGE_N_REGISTRY.json`
- `R059D_STAGE_L_BOUNDARY_AND_TIE_LEDGER.json`
- deterministic checker source/output
- report
- artifact manifest
- frozen checkpoint.

## 15. Permitted dispositions

Strong positive:

`BRC6_EQUAL_L_ENDPOINT_BRANCH_COUNT_COLLAPSE_ESTABLISHED`

and, if true dynamics also works:

`BRC6_ENDPOINT_COUNT_TRUE_STATE_DYNAMICS_ESTABLISHED`.

Qualified positive:

`BRC6_ENDPOINT_COUNT_PARTIAL_WITH_EXACT_TIES`.

Negative/obstruction:

`ENDPOINT_BRANCH_COUNT_INSUFFICIENT_FOR_BRC6`

or

`ENDPOINT_COUNT_SEMANTIC_RULE_DOES_NOT_RESOLVE_SELECTOR_NONIDENTIFIABILITY`.

Never upgrade to physical direction/probability.

## 16. Interpretation firewalls

Continue:

`PHYSICAL_DIRECTION_CALIBRATION = NOT_ESTABLISHED`

`PHYSICAL_PROBABILITY_FROM_BRC_COUNTS = NOT_ESTABLISHED`

`PHYSICAL_RIGIDITY_INTERPRETATION = NOT_ESTABLISHED`

`PHYSICAL_ELASTICITY_INTERPRETATION = NOT_ESTABLISHED`

`QUANTUM_BRIDGE = NOT_ESTABLISHED`.

## 17. Stop

After all required artifacts/checker/report/manifest/frozen checkpoint:

`STOP_FOR_DRIVER_REVIEW`.
