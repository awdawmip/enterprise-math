# R058S Stage C — Straight-Edge Cutting-Word Density Isolation

Researcher-ID: `EM-R058S-7C91E4`

Generation: `RS-R058S-EXACT-SQUARE-COLLAPSE-GRAMMAR-DISCOVERY`

Driver: `EM-DVR-R0457K / CONTROL_PLANE`

## 0. Frozen parent

Consume as immutable inputs:

- `R058S_STAGE_A_PACKET_CENSUS_CHECKPOINT_SHA256 = e43da09e347503223cde29de378570e76e79e63f44fe2bd9195b6a7dd6b1a925`
- `R058S_FIRST_SERIOUS_SQUARE_GRAMMAR_CHECKPOINT_SHA256 = 00faf065bb1769f4df7d7e51cec8b8754c414f280666d785adc7ed554acd753b`
- `R058S_STAGE_B2_EDGE_CORNER_CHECKPOINT_SHA256 = eec1e395b8805d8d720648b7a4e1f70dc74a2bd2fdcff91d1d8537c9d052d5c1`
- `R058S_TEACHER_EDGE_CORNER_ROLE_PROTOCOL_SHA256 = 7c9bc4579b1a3002f1567036d914923d2f7a0e7645db021db90a693d173b7ff8`
- Stage-B1 exact head: `81fba01c21a991208daa85bfa109705706534da0`
- Stage-B2 reviewed head: `3c31380b1bba3bc1f2f0c8542ff7b05a30e6f0be`

The Stage-B2 interpretation is also frozen:

- `WHOLE_CHORD_IS_GLOBAL_BASE_BUT_CORNER_SPLIT_NOT_IDENTIFIED`
- `LOCAL_GRAMMAR_ROLE_SEPARATION_PARTIAL`
- `EDGE_DENSITY_BIASED`
- `SQUARE_COLLAPSE_STRUCTURE_OPEN_WITH_EXACT_BOUNDED_EVIDENCE`

This stage exists because B2 did **not** identify a finite corner-split law. The strongest remaining causal signal is straight-edge density bias.

## 1. Scientific question

Remove the four square corners entirely and ask the simpler exact question:

> For an infinite digital straight boundary on the same triangular/Voronoi carrier, what length density is produced by the already-frozen R058S collapse rules?

The desired decomposition is

`digital straight boundary -> periodic/cutting word -> frozen local collapse readout -> exact length per teacher translation period`.

Then return to the finite square only to test whether

`whole square error = straight-edge bulk bias + finite corner/boundary-layer remainder`.

This is a diagnostics / exact-structure stage. It is **not** a new grammar-search stage.

## 2. Hard prohibitions

Do not:

- refit any coefficient or rule;
- run a new optimizer or grammar search;
- modify any B1 composition, predicate, program, or selected candidate;
- add a new local feature/predicate/operator;
- use canonical packet-class ID to invent a new rule;
- expand `K>8`;
- consume the square holdout corpus/predictions;
- consume R057 fitted rules, D1/D2/D3 winners, packet lookups, exception predicates, circle/arc/tangent/radius/circumference/pi targets;
- introduce rectangle or cube teachers;
- optimize segmentation/start offset;
- alter the frozen all-cyclic readout;
- use floating-point coincidence to claim exact density equality;
- interpret a bounded numerical trend as an all-scale theorem.

Allowed:

- exact deterministic construction of infinite/periodic digital straight boundaries on the already-frozen triangular/Voronoi carrier;
- evaluation of **already-frozen** B1 G0/G1/G2 rules on those boundaries;
- exact symbolic/radical arithmetic;
- exact finite-period/cutting-word analysis;
- post-B2 use of the already-frozen teacher edge/corner role semantics for square error decomposition only.

Holdout remains unconsumed.

## 3. Lane C0 — Reproduction gate

Before new analysis, reproduce:

- all Stage-0 frozen hashes;
- Stage-A 20/20 checker;
- Stage-A detail-bundle reconstruction;
- Stage-B1 35/35 checker;
- Stage-B2 34/34 checker;
- Stage-B1 grammar/result hashes;
- Stage-B2 role-protocol/checkpoint hashes.

Verify the frozen corpus facts:

- 384 discovery squares;
- 176,952 total boundary edges;
- D6 class counts `1,2,3,5,8,13,20,32` for `k=1..8`.

Any mismatch => `HARD_STOP_PARENT_DRIFT`.

## 4. Lane C0.5 — Freeze straight-edge protocol before exposure

Before computing any frozen-rule edge density, create and hash:

`R058S_STRAIGHT_EDGE_PERIODIC_PROTOCOL.json`

This file must freeze all semantics below.

### 4.1 Lattice and metric

Use the same triangular axial lattice and exact bilinear form

`beta((a,b),(c,d)) = 2ac + ad + bc + 2bd`

with

`Q(a,b)=a^2+ab+b^2`.

Use the same regular-hexagonal Voronoi carrier; do not rescale the carrier.

### 4.2 Teacher-free straight digital half-plane

For primitive integer normal `n`, define the occupied center set by an exact half-plane inequality

`H(n,h) = { x in Z^2 : beta(x,n) <= h }`

with rational `h` and the frozen closed-membership convention.

For a primitive tangent `t` satisfying

`beta(t,n)=0`,

translation by `t` leaves `H(n,h)` invariant.

The digital exposed Voronoi boundary therefore admits a translational period. This must be verified exactly, not assumed.

### 4.3 Tangent families

For every frozen discovery square orientation `d`, use both square side tangent families:

- tangent `t=d`;
- tangent `t=p`, where `p` is the frozen primitive exact perpendicular from Stage 0.

D6/square-symmetry-equivalent tangent families may be deduplicated only after an exact equivalence audit. Preserve a map back to all discovery orientations.

### 4.4 Offset classes

For each integer normal `n`, compute the exact image subgroup

`beta(Z^2,n) = g_n Z`,

where

`g_n = gcd(2n_a+n_b, n_a+2n_b)`.

Audit whether all rational half-plane thresholds produce, up to lattice translation, one digital-boundary word class or more than one residue/tie class.

Do not assume phase independence. Prove/check it from the exact support subgroup and translation structure.

If multiple inequivalent offset classes exist, enumerate all of them deterministically before any frozen-rule density is read.

### 4.5 Fundamental period

For every tangent/offset class, freeze a canonical fundamental exposed-edge word whose endpoint is translated by the minimal positive lattice tangent period.

Record:

- tangent and normal;
- exact translation vector;
- teacher Euclidean translation length `sqrt(Q(t_period))`;
- exposed-edge count in one period;
- direction word;
- turn word;
- exact start/end Voronoi vertices;
- D6 canonical representation;
- proof/check that concatenating periods reproduces the infinite boundary.

No square corner data may enter this construction.

## 5. Lane C1 — Exact radical arithmetic gate

Every block chord has exact rational squared length on the frozen Voronoi carrier.

Represent every chord length in a canonical exact radical form. At minimum, reduce

`sqrt(a/b)`

to a rational coefficient times `sqrt(q)` with squarefree positive integer `q`, and store finite sums as a sorted radical-coefficient vector.

Teacher period lengths `sqrt(Q(t_period))` use the same exact representation.

Exact zero/equality decisions must use symbolic/radical equality. If any expression falls outside the implemented radical basis, use a certified algebraic-number or interval-separation method and record it explicitly.

Plain binary64/decimal tolerance is forbidden for an `EXACT` classification.

Freeze/check this arithmetic gate before scientific verdicts.

## 6. Lane C2 — Frozen rule straight-edge density atlas

Evaluate only already-frozen B1 rules.

At minimum include:

### G0 universal compositions

For every `k=2..8`, evaluate the frozen G0 winner, which B1 found to be whole chord `(k)` for every k.

### G1 frozen compact programs

Evaluate all frozen B1 G1 balanced programs by k and all frozen B1 minimum-RMSE reference programs by k.

Do not reselect or modify them using the straight-edge teacher.

### G2 frozen high-capacity reference

Evaluate the frozen G2 lookup only as a secondary diagnostic/reference where its frozen packet classes occur on the straight-edge periodic word. Do not repair unseen classes or refit lookup entries.

For each `(tangent class, offset class, k, frozen model)` compute over one fundamental period:

`Lhat_period = (1/k) * sum_i C_g(packet_i)`

with cyclic packet starts on the periodic word.

Compare against exact teacher period length

`L_teacher = sqrt(Q(t_period))`.

Report:

- exact signed radical error;
- exact equality status;
- high-precision decimal only as presentation;
- density ratio `rho = Lhat_period/L_teacher`;
- collapse-count/composition frequencies on the periodic edge;
- whether the model's local branch state is periodic and its period;
- D6 covariance;
- offset-class dependence if any.

Do not choose a new winner from these results. This is transfer diagnosis of frozen rules.

## 7. Lane C3 — Whole-chord density law

Give special treatment to the G0 whole-chord family.

For every `k=2..8` and every tangent class determine whether

`rho_WC(k,t) = 1`

exactly.

Allowed statuses:

- `STRAIGHT_EDGE_WHOLE_CHORD_DENSITY_EXACT`
- `STRAIGHT_EDGE_WHOLE_CHORD_DENSITY_BIASED`
- `ORIENTATION_DEPENDENT_WHOLE_CHORD_DENSITY`
- `OFFSET_DEPENDENT_WHOLE_CHORD_DENSITY`

If a closed formula in the periodic/cutting word is available, derive it exactly.

Do not introduce a fitted correction coefficient.

## 8. Lane C4 — Frozen G1 edge-density exactness

For each already-frozen G1 candidate test whether its straight-edge density is exact across:

- all frozen discovery tangent families;
- all exact offset classes;
- its fixed k.

Classify separately:

- primary balanced G1 candidate;
- B1 minimum-RMSE G1 reference;
- each per-k frozen G1 program.

Allowed statuses include:

- `FROZEN_G1_EDGE_DENSITY_EXACT_ON_DISCOVERY_TANGENTS`
- `FROZEN_G1_EDGE_DENSITY_BIASED`
- `FROZEN_G1_EDGE_DENSITY_ORIENTATION_DEPENDENT`

This does **not** authorize promotion to theorem or holdout transfer.

## 9. Lane C5 — Square bulk-edge / corner-boundary-layer decomposition

Return to the frozen 384 square corpus without changing any predictions.

For each square with side length `s` and frozen axis pair `(d,p)`, use the periodic straight-edge density of the corresponding frozen model to construct the predicted bulk contribution of two `d`-tangent sides and two `p`-tangent sides.

A natural comparison quantity is

`E_bulk(s) = 2s[(rho_d-1) + (rho_p-1)]`

when the chosen period density applies directly in teacher length units. If the exact finite-window convention requires a boundary-layer offset, derive the correct exact formula instead of forcing this expression.

Then define the exact residual

`E_corner_layer = E_square_frozen - E_bulk`.

Stratify by:

- side length;
- orientation;
- phase;
- frozen model.

Ask:

1. Does `E_bulk` explain the linear-in-s component of square error?
2. Is the remaining `E_corner_layer` bounded as s grows on the discovery family?
3. Is it eventually periodic in side length/phase?
4. Does it converge to a finite corner defect, or remain scale-dependent?

No regression slope may be fitted to manufacture the decomposition. Use the exact periodic edge densities computed above.

Allowed verdicts:

- `EDGE_BIAS_EXPLAINS_LINEAR_SQUARE_ERROR`
- `CORNER_REMAINDER_BOUNDED_AFTER_EDGE_REMOVAL`
- `FINITE_CORNER_DEFECT_REMAINS_AFTER_EDGE_REMOVAL`
- `CORNER_REMAINDER_SCALE_DEPENDENT`
- `EDGE_CORNER_DECOMPOSITION_NOT_CLOSED`

## 10. Lane C6 — Local identifiability diagnostic

B2 found material `ROLE_ALIASING_WITHIN_LOCAL_PACKET_CLASS`.

Without adding new features or K, inspect the straight-edge periodic atlas and frozen square role atlas to answer:

- which frozen local packet classes occur on pure infinite straight edges;
- which of those same classes also occur in `CORNER_NEAR` windows;
- whether any `k<=8` class is exclusive to a corner role;
- whether B2's role aliasing can be explained by the finite observation radius rather than by search failure alone.

This is descriptive only. Do not infer that K must be expanded unless the exact evidence supports a finite-radius indistinguishability statement.

Allowed status:

- `FINITE_K_ROLE_ALIASING_STRUCTURAL`
- `FINITE_K_ROLE_ALIASING_NOT_IDENTIFIED`

A theorem-level impossibility claim requires a separate proof generation.

## 11. Lane C7 — Freeze

Create at minimum:

1. `R058S_STRAIGHT_EDGE_PERIODIC_PROTOCOL.json`
2. `R058S_STRAIGHT_EDGE_PERIODIC_WORD_ATLAS.json`
3. `R058S_FROZEN_GRAMMAR_EDGE_DENSITY_ATLAS.json`
4. `R058S_WHOLE_CHORD_EDGE_DENSITY_LEDGER.json`
5. `R058S_SQUARE_EDGE_BULK_CORNER_REMAINDER_DECOMPOSITION.json`
6. `R058S_FINITE_K_ROLE_ALIASING_DIAGNOSTIC.json`
7. `R058S_STAGE_C_CHECK_RESULTS.json`
8. `R058S_STAGE_C_STRAIGHT_EDGE_DENSITY_CHECKPOINT.json`

Return SHA256 for each required artifact and especially:

`R058S_STRAIGHT_EDGE_PERIODIC_PROTOCOL_SHA256`

`R058S_STAGE_C_STRAIGHT_EDGE_DENSITY_CHECKPOINT_SHA256`

Independent checker must cover:

- parent hash reproduction;
- protocol-before-density chronology;
- exact tangent/normal orthogonality;
- period translation reproduction;
- radical arithmetic exactness;
- all frozen-model replays;
- no B1 grammar mutation;
- no holdout/R057/K-expansion/new-search consumption;
- decomposition identity checks.

Then **STOP for Driver review**.

## 12. Interpretation boundary

The purpose of Stage C is not to force a corner generator.

A scientifically strong negative result is acceptable, for example:

`WHOLE_CHORD_GLOBAL_BASE_CONFIRMED / STRAIGHT_EDGE_DENSITY_BIASED / LINEAR_EDGE_BIAS_EXPLAINS_SQUARE_ERROR / CORNER_GENERATOR_NOT_YET_IDENTIFIED`.

If, instead, one already-frozen compact G1 rule is exactly edge-correct across all discovery tangent classes and leaves a bounded corner remainder, that is also important—but it must remain a transfer observation, not a post-hoc refit.

The next decision after Stage C will be made by the Driver. Do not consume square holdout, start rectangles/cubes, expand K, or invent a new grammar in this stage.

`CI_NOT_REQUIRED_FOR_RESEARCH`.
