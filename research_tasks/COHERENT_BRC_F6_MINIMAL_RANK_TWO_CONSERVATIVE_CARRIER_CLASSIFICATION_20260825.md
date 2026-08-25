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
    "research_inputs/CBRC_F6_BLIND_MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_PACKET_20260825.md@d0991001455a0a40a50f66ac6c14595448d29f21",
    "driver_reviews/CBRC_F5B_POSITIVE_SEPARATION_REGULARITY_ADMISSION_DRIVER_REVIEW_20260825.md@010a1b09f0f79e2484ea56b94bdc7d414b8e0f11"
  ],
  "source_refs": [
    "research_inputs/CBRC_F6_BLIND_MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_PACKET_20260825.md@d0991001455a0a40a50f66ac6c14595448d29f21"
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

This does not select any rank-two number system. F6 classifies only the minimal additive rank-two carrier and inherited unary transport structure. Two-slot mixing and scalar-law classification remain frozen.

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
2. create/push owner branch `research/cbrc-f6-minimal-rank-two-conservative-carrier`;
3. commit/push `evidence/cbrc_f6_execution_stamp.json` with Researcher-ID, task ID, exact taskbook source, owner branch, exact mathematical source ref, `phase=STARTED_BEFORE_MATH`, `carrier_verdict=null`, `math_source_read_before_stamp=false`;
4. verify the remote branch resolves to that stamp commit.

If this gate fails, stop without mathematics.

## 3. Mathematical whitelist / firewall

Before raw freeze, read/use only:

`research_inputs/CBRC_F6_BLIND_MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_PACKET_20260825.md@d0991001455a0a40a50f66ac6c14595448d29f21`.

The taskbook is specification, not an extra mathematical premise. Repository/governance files may be read only for execution procedure.

Do not open the full historical F1 review before raw freeze; its torsion-free counterfactual is intentionally withheld from F6 discovery.

Forbidden before raw freeze: R063/R064/R065/FQ; downstream coherent-BRC/wave; external quantum mechanics; complex/Gaussian/Eisenstein/quadratic carriers; roots of unity/phase groups; rings/fields/multiplication; norms/inner products/quadratic or square laws; Hadamard/Fourier/splitter targets; any known downstream rank-two answer.

## 4. Frozen upstream structure

Use exactly the F6 blind packet's `C1`, `R,J,S`, `pi1`, and relative witness. Preserve those relations exactly on the embedded upstream layer.

## 5. Q1 — rank-two additive carrier normal form

Let `C` be a finitely generated abelian additive carrier of torsion-free rank exactly `2` containing an embedded `j:C1->C`, with primitive old generator and additive retraction `pi:C->Z e` extending `pi1`.

Classify all such carriers up to isomorphism preserving the typed upstream embedding/retraction data. Determine torsion normal form, whether extra torsion beyond the accepted `Z/3` is forced, whether minimality forces exactly the inherited torsion, complement/gauge freedom, and the relevant automorphism group.

Deliver:

`F6_RANK_TWO_ADDITIVE_CARRIER_NORMAL_FORM_CLASSIFIED`.

## 6. Q2 — conservativity strength / retraction to C1

The blind packet does not assume `r:C->C1`.

Classify embedding-only, old-signed-retraction, and full-upstream-retract notions. Determine whether the least carrier automatically admits `r j=id_C1`, whether imposing it changes the least class, and whether choices of `r` are equivalent or real data.

Deliver:

`F6_CONSERVATIVE_EXTENSION_NOTIONS_CLASSIFIED`.

## 7. Q3 — inherited unary R/J/S lifts

Classify all additive automorphism triples `R~,J~,S~ in Aut(C)` restricting to accepted `R,J,S` on `j(C1)` and satisfying

`R~^3=id`, `J~^2=id`, `S~^2=id`, `J~R~=R~J~`, `S~R~S~^-1=R~^-1`,

plus old-projection covariance

`pi R~=pi`, `pi S~=pi`, `pi J~=-pi`.

Give exact normal forms, arithmetic constraints, equivalence classes under allowed basis/complement changes, and determine whether the new free direction can carry genuine finite unary-orbit information or is forced to be fixed/sign-only at free-quotient level.

Deliver:

`F6_INHERITED_UNARY_TRANSPORT_LIFTS_CLASSIFIED`.

## 8. Q4 — minimality / extra torsion

At fixed free rank `2`, apply the blind packet's target-independent order. Test no-extra-torsion, extra cyclic and noncyclic finite torsion, and prove the least carrier/unary classes. Do not use familiar algebraic-number names as classifications or tie-breakers.

Deliver:

`F6_MINIMAL_RANK_TWO_CARRIER_UNARY_CLASSIFIED`.

## 9. Q5 — preserve upstream relative structure

For every minimal survivor verify embedded `e+Je=0`, embedded `e+JRe=-tau!=0`, all unary relations, typed composition through checker depth at least `4`, no new relation collapsing `e` or `tau`, and no implicit multiplication.

Deliver:

`F6_UPSTREAM_RELATIVE_STRUCTURE_PRESERVED`.

## 10. Q6 — final verdict

State the least additive rank-two carrier class(es), all least unary-lift equivalence classes, genuine versus presentation freedom, and exactly what remains unresolved before two-slot mixing.

Do not perform the mixing classification.

Deliver:

`MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_AND_UNARY_TRANSPORT_CLASSIFIED`.

## 11. Mandatory ablations

Ablate one at a time: primitive old generator; preservation of order-three `tau`; old retraction `pi`; full upstream retract if used; `R^3=id`; `JR=RJ`; `SRS^-1=R^-1`; old-projection covariance; no-extra-torsion minimality preference.

## 12. Deterministic checker

Required path:

`scripts/cbrc_f6_validate_minimal_rank_two_conservative_carrier.py`

Minimum coverage: finite-presentation/SNF examples used in proofs; bounded primitive embeddings for regression only; all finite unary-lift parameter cases; exact `R~,J~,S~` relations; equivalence canonicalization; upstream relative witness; composition depth at least `4`; all ablations; zero theorem/model mismatches.

Bounded enumeration is evidence only; completeness requires theorem proof.

## 13. Materialization checkpoints

Checkpoint A: push draft return and countermodel/ablation packet after additive normal form and conservativity stabilize.

Checkpoint B: push source/target-leak audit and checker; run exact pushed checker and record byte identity/result/digest.

Checkpoint C: push final manifest `evidence/cbrc_f6_minimal_rank_two_conservative_carrier_manifest.json` and verify remote head.

## 14. Required artifacts

1. `evidence/cbrc_f6_execution_stamp.json`;
2. `research_reports/CBRC_F6_MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_RETURN_20260825.md`;
3. `research_reports/CBRC_F6_SOURCE_AND_TARGET_LEAK_AUDIT_20260825.md`;
4. `research_reports/CBRC_F6_CARRIER_COUNTERMODEL_AND_ABLATION_PACKET_20260825.md`;
5. `scripts/cbrc_f6_validate_minimal_rank_two_conservative_carrier.py`;
6. `evidence/cbrc_f6_minimal_rank_two_conservative_carrier_manifest.json`.

## 15. Hard acceptance gate

Driver acceptance requires all five named classification labels, the hard target, `TARGET_LEAK_AUDIT_PASS`, publication-liveness checkpoints and deterministic checker evidence.

## 16. Freeze / stop

Freeze on owner branch and report owner head, artifact SHA-256s, checker digest/result, clean-tree status and primary verdict.

Stop after freeze. Do not classify two-slot mixing, scalar laws, rings/norms, or downstream wave structures. Driver review is required before any next stage.

---

Driver issue note:

`RANK ONE IS CLOSED ONLY IN THE EXPLICIT WORKING EXTENSION. CLASSIFY THE LEAST RANK-TWO ADDITIVE CARRIER FIRST; DO NOT NAME THE NUMBER SYSTEM YOU EXPECT.`
