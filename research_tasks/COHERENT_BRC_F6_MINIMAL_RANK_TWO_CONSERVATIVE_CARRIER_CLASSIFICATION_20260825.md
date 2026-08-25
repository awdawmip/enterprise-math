<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CBRC-F6-MINIMAL-RANK-TWO-CONSERVATIVE-CARRIER-CLASSIFICATION",
  "title": "Coherent-BRC F6 — Minimal Rank-Two Conservative Carrier Classification",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_AND_UNARY_TRANSPORT_CLASSIFIED",
  "next_action": "Classify the least torsion-free-rank-two additive carrier that conservatively retains the accepted signed/order-three relative layer and classify all inherited unary R/J/S lifts, without opening two-slot mixing or preselecting a known rank-two number system.",
  "dependencies": [
    "research_inputs/CBRC_F6_BLIND_MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_PACKET_20260825.md@d80209037f114d14bc67b529f9f779409bc104f0",
    "driver_reviews/CBRC_F5B_POSITIVE_SEPARATION_REGULARITY_ADMISSION_DRIVER_REVIEW_20260825.md@c64ec362797f98de111040ad8925c70c67260ddc"
  ],
  "source_refs": [
    "research_inputs/CBRC_F6_BLIND_MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_PACKET_20260825.md@d80209037f114d14bc67b529f9f779409bc104f0"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED_FIRST_RANK_TWO_STAGE",
  "tags": ["CBRC","F6","rank-two","carrier","additive-classification","unary-transport","blind-forward"],
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "CBRCF6"
}
-->

# Coherent-BRC F6 — Minimal Rank-Two Conservative Carrier Classification

Task-ID:

`RS-CBRC-F6-MINIMAL-RANK-TWO-CONSERVATIVE-CARRIER-CLASSIFICATION`

Driver:

`EM-DVR-CBRC-F0-7C3A21 / CONTROL_PLANE`

Intended owner branch:

`research/cbrc-f6-minimal-rank-two-conservative-carrier`

## 0. Driver routing

F5B closes the last known rank-one gate at **working-extension** scope:

`A0 + FREE_PROJECTION_ZERO_SEPARATION + BALANCED_REVERSIBLE_CONSERVATION => torsion_free_rank(C) >= 2`.

This does not select any rank-two number system. F6 is deliberately narrower than the old F3 mixing stage: it classifies only the minimal additive rank-two carrier and inherited unary transport structure. Two-slot mixing and scalar-law classification remain frozen for a later stage.

## 1. Hard target

`MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_AND_UNARY_TRANSPORT_CLASSIFIED`.

Choose exactly one primary verdict:

- `F6_UNIQUE_MINIMAL_RANK_TWO_CARRIER_AND_UNARY_CLASS`;
- `F6_FINITE_INEQUIVALENT_MINIMAL_RANK_TWO_UNARY_CLASSES`;
- `F6_PARAMETERIZED_OR_INFINITE_MINIMAL_RANK_TWO_UNARY_FAMILY`;
- `F6_NO_RANK_TWO_CONSERVATIVE_CARRIER_PRESERVES_UPSTREAM_LAYER`;
- `F6_CONSERVATIVITY_NOT_STRONG_ENOUGH_TO_CLASSIFY`;
- `F6_TARGET_LEAK_INVALID`.

## 2. Publication-liveness gate — before mathematics

Before reading any mathematical source:

1. allocate a fresh Researcher-ID;
2. create/push owner branch
   `research/cbrc-f6-minimal-rank-two-conservative-carrier`;
3. commit/push
   `evidence/cbrc_f6_execution_stamp.json`
   with:
   - Researcher-ID;
   - task ID;
   - exact taskbook source commit;
   - owner branch;
   - exact mathematical source ref;
   - `phase = STARTED_BEFORE_MATH`;
   - `carrier_verdict = null`;
   - `math_source_read_before_stamp = false`;
4. verify the remote branch resolves to the stamp commit.

If this gate fails, stop without mathematics.

## 3. Mathematical whitelist / firewall

Before raw freeze, read/use only:

`research_inputs/CBRC_F6_BLIND_MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_PACKET_20260825.md@d80209037f114d14bc67b529f9f779409bc104f0`.

The taskbook is specification, not an extra mathematical premise. Repository/governance files may be read only for execution procedure.

Do **not** open the full historical F1 review before raw freeze: it contains a torsion-free counterfactual that is intentionally withheld from F6 discovery.

Forbidden before raw freeze:

- R063/R064/R065/FQ mathematics;
- downstream coherent-BRC/wave free research;
- external quantum mechanics, Hilbert spaces, Born rules, path integrals, quantum walks, gauge theory, wave equations;
- complex numbers or a complex plane as target carrier;
- Gaussian/Eisenstein/quadratic integers;
- roots of unity / finite phase groups as a selector;
- rings, fields or multiplication on arbitrary coefficient states;
- norms, inner products, quadratic forms, p-norms, square laws;
- Hadamard/Fourier/splitter matrices;
- any rank-two downstream answer.

## 4. Frozen upstream structure to preserve

Use only the structure stated in the blind packet:

`C1 = Z e ⊕ <tau | 3 tau=0>`

with accepted unary `R,J,S`, old retraction `pi1`, and relative witness

`e+J e=0`,
`e+J R e=-tau!=0`.

Any F6 carrier must preserve these relations exactly on the embedded upstream layer. Do not weaken them to make a rank-two model fit.

## 5. Q1 — rank-two additive carrier normal form

Let `C` be a finitely generated abelian additive carrier of torsion-free rank exactly `2` containing an embedded copy `j:C1->C`, with primitive old generator and an additive retraction `pi:C->Z e` extending `pi1`.

Classify all such carriers up to isomorphism preserving the typed upstream embedding/retraction data.

Required:

1. exact structure theorem normal form;
2. classification of the torsion subgroup and the image of `tau`;
3. whether additional torsion beyond the accepted `Z/3` is ever forced;
4. whether minimality forces torsion exactly `Z/3`;
5. whether the new free direction can be chosen canonically or only up to complement/gauge choice;
6. exact automorphism/equivalence group preserving `e`, `tau`, and `pi` as appropriate.

Deliver:

`F6_RANK_TWO_ADDITIVE_CARRIER_NORMAL_FORM_CLASSIFIED`.

## 6. Q2 — conservativity strength / retraction to C1

The blind packet does not assume a retraction `r:C->C1`.

Classify exactly:

- embedding-only conservativity;
- old-signed retraction `pi` conservativity;
- full upstream retract conservativity `r j=id_C1`;
- whether the least carrier under the F6 order automatically admits such an `r`;
- whether different choices of `r` are equivalent or carry real new data.

If imposing a full retract changes the least carrier class, report both boundaries. Do not silently assume splitting.

Deliver:

`F6_CONSERVATIVE_EXTENSION_NOTIONS_CLASSIFIED`.

## 7. Q3 — extension of unary R/J/S

Classify all additive automorphism triples

`R~, J~, S~ in Aut(C)`

that restrict on `j(C1)` to the accepted `R,J,S` and satisfy the inherited relations:

`R~^3=id`,
`J~^2=id`,
`S~^2=id`,
`J~R~=R~J~`,
`S~R~S~^-1=R~^-1`.

Also impose the natural old-projection covariance inherited from the upstream maps:

`pi R~=pi`,
`pi S~=pi`,
`pi J~=-pi`.

Required:

1. exact normal form for every lift;
2. necessary and sufficient arithmetic constraints;
3. equivalence under additive automorphisms preserving the upstream typed layer and `pi`;
4. distinction between raw presentation parameters and genuine inequivalent unary classes;
5. whether the new free direction can carry nontrivial finite unary orbit information under these inherited relations or is necessarily fixed/sign-only at free-quotient level.

Deliver:

`F6_INHERITED_UNARY_TRANSPORT_LIFTS_CLASSIFIED`.

## 8. Q4 — minimality and extra torsion

At fixed free rank `2`, apply the target-independent order from the blind packet.

Prove the least carrier/unary classes exactly. In particular test:

- no-extra-torsion models;
- one additional finite cyclic kernel factor;
- noncyclic finite torsion additions;
- whether extra torsion creates a genuinely smaller unary-data burden or only enlarges the carrier;
- whether any apparently smaller presentation is merely an isomorphic/gauge presentation of the same additive carrier.

Do not use familiar algebraic-number names as classifications or tie-breakers.

Deliver:

`F6_MINIMAL_RANK_TWO_CARRIER_UNARY_CLASSIFIED`.

## 9. Q5 — upstream relative witness / composition preservation

For every minimal survivor verify:

- embedded `e+Je=0`;
- embedded `e+JRe=-tau!=0`;
- exact `R/J/S` relations;
- typed composition through depth at least `4` in the checker;
- translation/marker-independent interpretation where relevant;
- no new relation collapses `e` or `tau`;
- no implicit multiplication is needed.

Deliver:

`F6_UPSTREAM_RELATIVE_STRUCTURE_PRESERVED`.

## 10. Q6 — final carrier verdict

State exactly:

- the least additive rank-two carrier class(es);
- all least unary lift equivalence classes;
- which freedom is presentation/gauge and which is genuine;
- whether additional data are still needed before two-slot mixing can be classified.

Do not perform the next mixing classification.

Deliver:

`MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_AND_UNARY_TRANSPORT_CLASSIFIED`.

## 11. Mandatory ablations

At minimum ablate one at a time:

1. primitive-old-generator requirement;
2. preservation of order-three `tau`;
3. old retraction `pi`;
4. full upstream retract if used;
5. `R^3=id`;
6. central sign relation `JR=RJ`;
7. reversal relation `SRS^-1=R^-1`;
8. old-projection covariance;
9. no-extra-torsion minimality preference.

For each, state whether carrier uniqueness, unary classification, upstream witness preservation, or minimality changes.

## 12. Deterministic checker

Required path:

`scripts/cbrc_f6_validate_minimal_rank_two_conservative_carrier.py`

Minimum coverage:

- Smith-normal-form / finitely-generated-abelian-group finite presentations used in the proof;
- bounded primitive embeddings for regression only;
- all finite parameter cases arising in unary lift normal forms;
- exact relation checks for `R~,J~,S~`;
- equivalence-class canonicalization under allowed basis/complement changes;
- upstream relative-witness checks;
- composition depth at least `4`;
- mandatory ablations;
- zero theorem/model mismatches.

Bounded enumeration is evidence only; group/unary completeness requires theorem proof.

## 13. Materialization checkpoints

### Checkpoint A
After additive normal form and conservativity theorems stabilize, push drafts of:

- `research_reports/CBRC_F6_MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_RETURN_20260825.md`;
- `research_reports/CBRC_F6_CARRIER_COUNTERMODEL_AND_ABLATION_PACKET_20260825.md`.

### Checkpoint B
Before final verdict, push:

- `research_reports/CBRC_F6_SOURCE_AND_TARGET_LEAK_AUDIT_20260825.md`;
- `scripts/cbrc_f6_validate_minimal_rank_two_conservative_carrier.py`.

Run the exact pushed checker and record byte identity/result/digest.

### Checkpoint C
Push final manifest:

`evidence/cbrc_f6_minimal_rank_two_conservative_carrier_manifest.json`.

Verify the remote owner branch after every checkpoint.

## 14. Required artifacts

1. `evidence/cbrc_f6_execution_stamp.json`;
2. `research_reports/CBRC_F6_MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_RETURN_20260825.md`;
3. `research_reports/CBRC_F6_SOURCE_AND_TARGET_LEAK_AUDIT_20260825.md`;
4. `research_reports/CBRC_F6_CARRIER_COUNTERMODEL_AND_ABLATION_PACKET_20260825.md`;
5. `scripts/cbrc_f6_validate_minimal_rank_two_conservative_carrier.py`;
6. `evidence/cbrc_f6_minimal_rank_two_conservative_carrier_manifest.json`.

## 15. Hard acceptance gate

Driver acceptance requires:

`F6_RANK_TWO_ADDITIVE_CARRIER_NORMAL_FORM_CLASSIFIED`;

`F6_CONSERVATIVE_EXTENSION_NOTIONS_CLASSIFIED`;

`F6_INHERITED_UNARY_TRANSPORT_LIFTS_CLASSIFIED`;

`F6_MINIMAL_RANK_TWO_CARRIER_UNARY_CLASSIFIED`;

`F6_UPSTREAM_RELATIVE_STRUCTURE_PRESERVED`;

`MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_AND_UNARY_TRANSPORT_CLASSIFIED`;

`TARGET_LEAK_AUDIT_PASS`;

plus publication-liveness checkpoints and deterministic checker evidence.

## 16. Freeze / stop

Freeze on the owner branch and report owner head, artifact SHA-256s, checker digest/result, clean-tree status and primary verdict.

Stop after freeze. Do not classify two-slot mixing, scalar laws, rings/norms, or downstream wave structures. Driver review is required before any next stage.

---

Driver issue note:

`RANK ONE IS CLOSED ONLY IN THE EXPLICIT WORKING EXTENSION. CLASSIFY THE LEAST RANK-TWO ADDITIVE CARRIER FIRST; DO NOT NAME THE NUMBER SYSTEM YOU EXPECT.`
