# R058S Stage D — Primitive-Period Straight-Edge Collapse Theorem

Researcher-ID: `EM-R058S-7C91E4`

Generation: `RS-R058S-EXACT-SQUARE-COLLAPSE-GRAMMAR-DISCOVERY`

Driver-ID: `EM-DVR-R0457K / CONTROL_PLANE`

Status: `AUTHORIZED AFTER DRIVER ACCEPTANCE OF STAGE C`

## 0. Frozen parent checkpoints

Treat all prior bytes as immutable.

Stage A:

`R058S_STAGE_A_PACKET_CENSUS_CHECKPOINT_SHA256 = e43da09e347503223cde29de378570e76e79e63f44fe2bd9195b6a7dd6b1a925`

Stage B1:

`R058S_FIRST_SERIOUS_SQUARE_GRAMMAR_CHECKPOINT_SHA256 = 00faf065bb1769f4df7d7e51cec8b8754c414f280666d785adc7ed554acd753b`

Stage B2:

`R058S_STAGE_B2_EDGE_CORNER_CHECKPOINT_SHA256 = eec1e395b8805d8d720648b7a4e1f70dc74a2bd2fdcff91d1d8537c9d052d5c1`

Stage C:

`R058S_STAGE_C_STRAIGHT_EDGE_DENSITY_CHECKPOINT_SHA256 = 22f285cc876ce9624200a1ff4d58b910a7d698c1d0fbb0ec455409396fd809bb`

`R058S_STRAIGHT_EDGE_PERIODIC_PROTOCOL_SHA256 = acf22b9d2f256b0dccfa210abce69e2e994205a39d19bc3bed945026d75e78b9`

Stage-C reviewed head:

`4cde24e1e8e9a0a78822a6b3e01dc54a452eb0de`

Stage C checker:

`6451 / 6451 PASS`.

## 1. Why Stage D exists

Stage C established exact periodic straight-edge carrier words for eight discovery tangent classes. Their exposed-edge fundamental period lengths are:

`m = (2,4,8,14,6,10,10,16)`.

Within the already frozen empirical range `k=2..8`, Stage C found exactly eight whole-chord pairs with exact density `rho=1`:

`(k,tangent) =`

- `(2,T1)`
- `(4,T1)`
- `(4,T2)`
- `(6,T1)`
- `(6,T5)`
- `(8,T1)`
- `(8,T2)`
- `(8,T3)`.

Driver post-Stage-C observation:

> These eight and only these eight observed exact pairs satisfy `m(tangent) | k`.

This divisibility observation was **not** frozen as a theorem in Stage C. Stage D must determine whether it follows from an exact general identity.

The candidate theorem is simple:

Let an oriented periodic polygonal boundary have vertices `v_i` and primitive period length `m` edges with translation vector `t`, so that

`v_{i+m} = v_i + t` for every integer `i`.

For whole-chord packet length `k=q m`, every `k`-edge packet chord is

`v_{i+k}-v_i = q t`.

Under the frozen all-cyclic readout over one fundamental period,

`Lhat = (1/k) sum_{i=0}^{m-1} |v_{i+k}-v_i|`

would therefore satisfy

`Lhat = |t|`.

If valid, this is the first exact collapse law in the R058 line:

`one complete primitive digital straight-edge period -> its endpoint chord`.

## 2. Epistemic firewall

Stage D is **proof / exact structural analysis only**.

Forbidden:

- any coefficient fit or refit;
- any optimizer or candidate ranking;
- any new learned grammar;
- any new predicate/operator selected from square loss;
- any change to B1 G0/G1/G2 grammar bytes;
- any change to Stage-C periodic carrier words;
- any holdout consumption;
- any R057 fitted prior consumption;
- rectangle, cube, circle, disk, arc, tangent-circle, radius, circumference, pi target;
- any empirical expansion of the frozen packet-search range `K>8`;
- any claim that symbolic theorem variable `k=q m` constitutes a new searched packet grammar.

Important distinction:

Stage D may reason symbolically about arbitrary integer `q,m` and may prove an identity for `k=q m`. It must **not** generate a new empirical packet-search corpus at `K=10,14,16,...`, must not score such packets on square teacher data, and must not call symbolic theorem blocks a new fitted grammar.

If a later generation wants to deploy primitive-period blocks with lengths above 8, that must be separately authorized after Stage D.

## 3. Lane D0 — Reproduction gate

Before proof work, reproduce:

- Stage A checkpoint/hash ledger;
- Stage B1 checkpoint/hash ledger and 35/35 checker;
- Stage B2 checkpoint/hash ledger and 34/34 checker;
- Stage C checkpoint/hash ledger and 6451/6451 checker;
- the eight Stage-C tangent classes;
- exact fundamental edge-period lengths `2,4,8,14,6,10,10,16`;
- Stage-C exact whole-chord pair list above.

If any mismatch:

`HARD_STOP_PARENT_DRIFT`.

## 4. Lane D1 — Abstract primitive-period theorem

State and prove an exact theorem for an arbitrary periodic polygonal path.

At minimum define:

- ordered vertices `v_i` in a normed Euclidean vector space;
- integer fundamental edge period `m>=1`;
- nonzero translation `t` satisfying `v_{i+m}=v_i+t`;
- whole-chord packet map `C_k(i)=||v_{i+k}-v_i||`;
- all-period cyclic estimator
  
  `Lhat_{m,k}=(1/k) sum_{i=0}^{m-1} C_k(i)`.

Prove:

### Theorem D1.A — Period-multiple exactness

For every integer `q>=1`, if `k=q m`, then

`C_k(i)=q||t||` for all `i`, hence

`Lhat_{m,qm}=||t||` exactly.

The proof must not use the square teacher, triangular lattice specifics, floating point, or asymptotics.

Clarify that this is a sufficient condition for exactness. Do **not** claim the converse `rho=1 => m|k` in general unless separately proved.

## 5. Lane D2 — Carrier specialization theorem

Specialize D1 to the frozen triangular-lattice Voronoi straight-boundary carrier.

Use the exact Stage-C half-plane construction:

- primitive tangent lattice vector `t`;
- primitive exposed-edge cycle of `m` Voronoi edges;
- lifted boundary satisfies period translation by `t`;
- teacher straight-line translation length is exactly `sqrt(Q(t))` in the frozen physical units.

Prove:

### Theorem D2.A — Exact primitive-period edge collapse

For a digital half-plane boundary with primitive exposed-edge period `m` and primitive tangent translation `t`, whole-chord collapse over any complete integer number of periods returns exactly the Euclidean teacher translation length:

`Lhat_{m,qm}=sqrt(Q(t))`.

Use the same exact radical conventions as Stage C.

## 6. Lane D3 — Frozen Stage-C evidence as theorem consistency check

Do not perform new teacher search.

Using only existing Stage-C records, verify that every already observed exact pair `rho=1` satisfies `m|k` and that every observed pair with `m|k` is in the exact list.

For the eight discovery tangent classes and frozen `k=2..8`, record a 56-row Boolean audit:

- tangent id;
- `m`;
- frozen `k`;
- `m|k`;
- Stage-C exact `rho=1` flag;
- agreement.

Required observed-discovery status if all 56 rows agree:

`STAGE_C_EXACTNESS_MATCHES_PERIOD_DIVISIBILITY_ON_FROZEN_56_PAIRS`.

This is a finite consistency result, not the converse theorem.

## 7. Lane D4 — Finite straight-segment period/tail decomposition

Now prove a structural decomposition, still without creating a new deployed grammar.

For any finite digital straight segment whose interior follows a primitive period word of edge length `m`, write its edge sequence as:

`prefix_tail + q complete primitive periods + suffix_tail`,

where the two tails together are bounded independently of the macroscopic segment length once the alignment convention is fixed.

At minimum prove the purely combinatorial statement that after choosing a period alignment, a word interval contains `q` complete periods and a residual of fewer than `2m` edges total.

Then prove that collapsing each complete period to its endpoint chord would make the entire bulk contribution exact, leaving only the finite tails as unresolved length contribution.

This lane is a theorem/proposal only.

Label the not-yet-deployed operator:

`POST_STAGE_C_PRIMITIVE_PERIOD_COLLAPSE_OPERATOR_PROPOSAL`.

Do not apply it as a new square predictor in Stage D.

## 8. Lane D5 — Square implication without refit

Using Stage B2/C exact geometry, establish the strongest justified implication for a square side:

- far enough from a corner, the digitized square side is locally identical to the corresponding digital half-plane boundary;
- hence the straight-side interior consists of repetitions of the primitive cutting word;
- an exact primitive-period collapse would remove straight-edge bulk density bias;
- any remaining discrepancy must be localized to finite side tails / corner boundary layers rather than accumulate linearly with side length.

Distinguish carefully:

1. **proved word/period statement**;
2. **proved exact bulk-collapse identity**;
3. **finite-square localization statement** if proved;
4. anything still only conjectural about a universal corner grammar.

Do not claim a finite corner generator has been found.

Allowed statuses include:

- `PRIMITIVE_PERIOD_WHOLE_CHORD_THEOREM_PROVED`
- `STRAIGHT_EDGE_BULK_EXACT_AFTER_PERIOD_COLLAPSE`
- `FINITE_SIDE_TAIL_LOCALIZATION_PROVED`
- `SQUARE_ERROR_REDUCED_TO_FINITE_PERIOD_TAILS_AND_CORNER_LAYERS`
- `CORNER_GENERATOR_STILL_OPEN`

## 9. Lane D6 — Minimality / converse audit

Investigate, without expanding empirical K, whether any stronger abstract statement can be proved.

Questions:

- Is `m` minimal among positive edge periods by Stage-C primitive-cycle construction?
- For a generic periodic path, can `rho=1` occur at `k` not divisible by `m`?
- If yes, provide a counterexample and explicitly reject the converse theorem.
- If no only under additional hypotheses, state those hypotheses exactly.

This lane is mathematical reasoning, not square fitting.

A counterexample is scientifically useful.

## 10. Required artifacts

At minimum create:

1. `R058S_PRIMITIVE_PERIOD_COLLAPSE_THEOREM.md`
2. `R058S_PERIOD_DIVISIBILITY_CONSISTENCY_AUDIT.json`
3. `R058S_FINITE_STRAIGHT_SEGMENT_PERIOD_TAIL_THEOREM.md`
4. `R058S_SQUARE_PERIOD_TAIL_IMPLICATION_LEDGER.json`
5. `R058S_STAGE_D_CHECK_RESULTS.json`
6. `R058S_STAGE_D_PRIMITIVE_PERIOD_THEOREM_CHECKPOINT.json`

The theorem markdown must separate:

- abstract theorem;
- carrier specialization;
- finite frozen evidence;
- unproved conjectures/proposals.

## 11. Checker requirements

Independent checker must verify at least:

- parent hashes unchanged;
- Stage-C 6451/6451 reproduction summary;
- exact period lengths;
- exact observed pair list;
- all 56 `m|k` vs Stage-C exactness flags;
- theorem algebra on symbolic/random integer test instances as implementation sanity only;
- no empirical `K>8` square search;
- no new square predictions;
- no holdout;
- no R057 fitted prior;
- no B1 grammar mutation;
- no optimizer/refit.

Symbolic/random test instances support checker implementation only and are not the proof.

## 12. Publication

Use compact theorem/checkpoint artifacts.

Do not create gzip/base64 chunk pipelines.

`CI_NOT_REQUIRED_FOR_RESEARCH`.

## 13. Return values and stop condition

Return at least:

`R058S_PRIMITIVE_PERIOD_COLLAPSE_THEOREM_SHA256`

`R058S_PERIOD_DIVISIBILITY_CONSISTENCY_AUDIT_SHA256`

`R058S_FINITE_STRAIGHT_SEGMENT_PERIOD_TAIL_THEOREM_SHA256`

`R058S_SQUARE_PERIOD_TAIL_IMPLICATION_LEDGER_SHA256`

`R058S_STAGE_D_CHECK_RESULTS_SHA256`

`R058S_STAGE_D_PRIMITIVE_PERIOD_THEOREM_CHECKPOINT_SHA256`

Then immediately STOP for Driver review.

Do not implement the proposed period-collapse operator on square corpus yet.

Do not consume holdout.

Do not start rectangle or cube.
