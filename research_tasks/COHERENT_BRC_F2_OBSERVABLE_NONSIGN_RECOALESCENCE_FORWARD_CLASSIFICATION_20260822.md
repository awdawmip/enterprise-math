<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CBRC-F2-OBSERVABLE-NONSIGN-RECOALESCENCE-FORWARD-CLASSIFICATION",
  "title": "Coherent-BRC F2 — Observable Non-Sign Recoalescence Forward Classification",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "OBSERVABLE_NONSIGN_RECOALESCENCE_MINIMAL_EXTENSION_CLASSIFIED",
  "next_action": "Using only the blind accepted F0/F1 input packet, classify whether the accepted hidden non-sign transport can change the scalar outcome of the minimal native recoalescence under target-independent invariance/refinement conditions, and if not classify the least enlargement that can.",
  "dependencies": [
    "research_inputs/CBRC_F2_BLIND_OBSERVABILITY_PACKET_20260822.md@155297ab859e4207634dae75566c89ca1a430000",
    "driver_reviews/CBRC_F1_NONSIGN_RECOALESCENCE_CARRIER_DRIVER_REVIEW_20260822.md@282c8d30f204780804070aba49c1386e6a909df2"
  ],
  "source_refs": [
    "research_inputs/CBRC_F2_BLIND_OBSERVABILITY_PACKET_20260822.md@155297ab859e4207634dae75566c89ca1a430000"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "CBRC",
    "F2",
    "blind-forward",
    "relative-observability",
    "recoalescence",
    "readout-classification",
    "foundation-facing"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "CBRCF2",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d5cbe89c8620ca6efa2af5219900424485c85bba1fc042576e17034c10e38299",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Coherent-BRC F2 — Observable Non-Sign Recoalescence Forward Classification

Task-ID: `RS-CBRC-F2-OBSERVABLE-NONSIGN-RECOALESCENCE-FORWARD-CLASSIFICATION`

Driver: `EM-DVR-CBRC-F0-7C3A21 / CONTROL_PLANE`

Identity lane: `CBRCF2`

Intended owner branch:

`research/cbrc-f2-observable-nonsign-recoalescence-forward-classification`

## 0. Driver routing / why F2 exists

F0 classified the minimal conservative cancellation layer.

F1 classified the least finite reversible transport strictly richer than the sign orbit under its declared extension order.

The accepted F1 object is deliberately narrower than a wave/coherence claim: its new orbit is erased by the accepted F0 forgetful map, and F1 selected no scalar readout.

Therefore the next load-bearing question is not downstream algebra matching.

It is:

> Can the accepted non-sign enrichment become visible **only through relative same-terminal recoalescence**, while each individual alternative keeps the same local scalar status and all common transport / relabeling choices remain unobservable?

If yes, classify the allowed readout family and its exact degree of underdetermination.

If no, classify the least carrier enlargement required for such relative observability.

## 1. Hard target

`OBSERVABLE_NONSIGN_RECOALESCENCE_MINIMAL_EXTENSION_CLASSIFIED`.

The result must choose among:

- accepted F1 carrier is already relatively observable;
- accepted F1 carrier is observationally silent under the declared invariances;
- it is observable but the scalar law is nonunique;
- a strictly larger carrier is required and can be minimally classified;
- the requirements are inconsistent or underdetermined before carrier selection.

Do not optimize for any familiar wave/quantum result.

## 2. Phase-A mathematical source whitelist

Before the raw F2 packet is frozen, read/use only:

`research_inputs/CBRC_F2_BLIND_OBSERVABILITY_PACKET_20260822.md`

at source commit:

`155297ab859e4207634dae75566c89ca1a430000`.

The packet already contains the exact upstream facts authorized for F2.

Repository/governance files may be read only for build/test/branch procedure and may not contribute mathematical candidates.

Do **not** open the full F1 reports, F1 counterfactual higher-rank section, downstream journals, or external theory before F2 raw freeze.

## 3. Continued blindness / forbidden preload

Until F2 raw freeze, do not read or use:

- R063/R064/R065 mathematical results;
- any downstream/free-research coherent-BRC or wave result;
- Hodge/Shor mathematics;
- external quantum mechanics;
- complex-amplitude or Hilbert-space formalism;
- Born/probability-amplitude laws;
- quantum walks;
- path integrals;
- gauge-field theory;
- continuum wave/scattering equations.

Also forbidden as premises/target selectors are prechosen:

- square or other power readout;
- norm or inner product;
- coefficient ring/field beyond the accepted packet;
- additional finite phase group;
- root of unity;
- transform matrix;
- trigonometric interference law;
- continuum intensity formula.

Ordinary algebra, group actions, ordered/nonnegative scalar functions, finite combinatorics, universal constructions, and exact countermodels are allowed if introduced transparently from this task.

## 4. Frozen accepted input boundary

Use only the facts stated in the blind input packet.

In particular, the minimal typed native recoalescence witness contains two distinct paths `p,q` with one common terminal.

The accepted signed coefficient generator is `e`, with sign involution `J=-id`.

The accepted F1 enrichment is

`C1 = Z e ⊕ <tau | 3 tau = 0>`

with

`R(e)=e+tau`,
`R(tau)=tau`,
`R^3=id`,

and reversal

`S(e)=e`,
`S(tau)=-tau`,
`SRS^-1=R^-1`.

No scalar readout is inherited.

Do not import any omitted F1 counterfactual carrier family.

## 5. Operational definition of relative observability

F2 must not define observability by naming a known amplitude model.

Start with a scalar functional on **unmarked same-terminal aggregate coefficients**:

`rho : C -> R_nonnegative`

or a rigorously justified smaller exact nonnegative codomain that embeds in an ordered scalar system.

If you choose a different codomain, prove it is sufficient for every comparison below.

For individually distinguishable/marked alternatives, use a separate tagged scalar bookkeeping rule; do not silently identify distinguishable addition with unmarked recoalescence.

At minimum impose/test the following target-independent conditions.

### O1. `NULL_ZERO`

`rho(0)=0`.

Do not assume the converse unless derived.

### O2. `ELEMENTARY_NORMALIZATION`

Every single embedded elementary occurrence has one common positive scalar value, normalized to `1`:

`rho(e)=1`.

### O3. `ABSOLUTE_NONSIGN_INVISIBILITY`

A non-sign label on a **single** alternative is not by itself observable:

`rho(R^k e)=rho(e)`

for every allowed `k`.

Likewise the sign of one isolated alternative is not an absolute scalar label:

`rho(J R^k e)=rho(R^k e)`.

This is an operational condition, not an assumed norm law.

### O4. `DISTINGUISHABLE_ALTERNATIVE_ADDITIVITY`

If `p,q` remain explicitly distinguishable markers, their scalar total is the sum of their individual elementary scalar values.

Thus two tagged elementary alternatives have tagged total `2` regardless of their relative transport labels.

This tagged rule is **not** a statement about the unmarked same-terminal aggregate.

### O5. `COMMON_TRANSPORT_INVARIANCE`

Applying the same reversible transport to every coefficient in an unmarked same-terminal aggregate cannot change the scalar:

`rho(R^k z)=rho(z)`

for every aggregate state `z` in the declared domain.

### O6. `GLOBAL_SIGN_INVARIANCE`

`rho(J z)=rho(z)`.

### O7. `REVERSAL / SERIALIZATION INVARIANCE`

`rho(S z)=rho(z)` where the accepted reversal acts, and swapping the serialization of the two native paths cannot change the scalar class.

### O8. `AGGREGATE_PRESENTATION_INDEPENDENCE`

Once path markers are deliberately erased at the declared recoalescence boundary, the scalar depends on the resulting coefficient aggregate and declared typed terminal, not on an arbitrary list order, temporary marker name, or parenthesization.

### O9. `COMPOSITION_COMPATIBILITY`

The same `rho` must work for coefficients produced by finite path-transport composition, not only for one hand-picked diamond table.

### O10. `NONSIGN_RELATIVE_SENSITIVITY`

The enrichment is operationally non-sign-observable only if there exists a nontrivial relative transport class, beyond the old sign-only class, such that on the same native `(1,1)` terminal fiber

`rho(e + J^s R^k e) != rho(e + J^s e)`

for some `s in {0,1}` and some nonidentity `R^k`.

This requires a **relative** effect while O3 forbids an absolute single-branch effect.

Do not assume the changed value must be a particular number or lie between constructive/dark values; report that separately if derivable.

## 6. F2-Q1 — invariant orbit space on the accepted F1 carrier

Using only `C1,J,R,S`, classify the orbits relevant to scalar readout under the common actions required by O5–O7.

Required:

1. classify all `R/J/S` invariant classes of aggregate coefficients needed for one and two elementary alternatives;
2. identify whether the old constructive aggregate `e+e`, old sign-dark aggregate `e+Je=0`, and every non-sign relative aggregate lie in the same or different invariant classes;
3. prove whether O10 is possible or impossible on `C1`;
4. separate theorem-level orbit classification from any chosen scalar assignment to those orbits.

Deliver:

`F1_CARRIER_RELATIVE_OBSERVABILITY_ORBIT_SPACE_CLASSIFIED`.

## 7. F2-Q2 — scalar readout existence and nonuniqueness

If the accepted F1 carrier admits O10, classify the scalar readouts satisfying O1–O9 on the smallest domain sufficient for the minimal diamond and then extend/classify them on the full finitely generated coefficient domain.

Required:

- construct at least one exact readout if existence is claimed;
- prove nonnegativity and all invariances;
- exhibit at least two inequivalent readouts if uniqueness is not forced;
- identify the exact free parameters/invariant-orbit data;
- do not name a preferred exponent or norm unless it is forced;
- state whether any readout is faithful, partially blind, or necessarily blind on nonzero torsion states.

If no readout exists, prove the obstruction.

Deliver:

`NONSIGN_RECOALESCENCE_READOUT_EXISTENCE_CLASSIFIED`.

## 8. F2-Q3 — observable-minimal carrier classification

Define an explicit complexity order for **observable** non-sign extensions.

It must preserve the old signed layer and consider at least:

1. torsion-free additive rank;
2. new generators/relations;
3. finite-kernel size, if any;
4. transport orbit size;
5. number of scalar orbit classes on the minimal two-path recoalescence actually distinguished under O1–O10;
6. whether additional multiplication/bilinear structure is required.

If `C1` is observable, prove it is or is not minimal under this stronger order.

If `C1` is silent, search/classify the least larger carrier without importing any omitted F1 counterfactual family as a target.

Deliver:

`OBSERVABLE_NONSIGN_MINIMAL_CARRIER_FAMILY_CLASSIFIED`.

## 9. F2-Q4 — finite-path/refinement extension

The minimal-diamond result must extend coherently to larger Path-formal fibers.

Required checks:

1. depth-3 path composition;
2. depth-4 commuting-diamond composition;
3. finite same-terminal fibers with at least three alternatives;
4. marker refinement followed by deliberate marker erasure;
5. branch swap and accepted reversal;
6. common transport of the entire fiber;
7. recovery of the original F0 sign-only constructive/dark examples when non-sign labels are trivialized.

Classify whether new scalar behavior appears first at two-path or only at higher-path recoalescence.

Deliver:

`OBSERVABLE_NONSIGN_FINITE_FIBER_EXTENSION_CLASSIFIED`.

## 10. F2-Q5 — what additional principle, if any, selects a scalar law?

Do not assume F2 will produce a unique readout.

If multiple scalar laws survive, identify the weakest additional operational principles that could reduce the family.

Test candidate principles one at a time and by ablation. Examples of admissible **questions**, not premises, include:

- a bound comparing unmarked recoalescence to the tagged total;
- multiplicative scaling under independent replication;
- continuity/monotonicity on an emergent integer parameter, if such a parameter is derived;
- finite-copy consistency beyond mere marker refinement;
- conservation under an additional nontrivial local mixing operation, only if such an operation has already been derived independently.

For every proposed selector:

- state it without target-law language;
- give at least one countermodel when it is removed;
- state exactly what it selects and what remains free.

Do not promote a selector to Foundation truth in F2.

Deliver:

`READOUT_SELECTOR_DEPENDENCY_CLASSIFIED`.

## 11. Mandatory ablations

At minimum rerun the relevant classification after removing one at a time:

1. absolute non-sign invisibility O3;
2. distinguishable additivity O4;
3. common transport invariance O5;
4. global sign invariance O6;
5. reversal/serialization invariance O7;
6. aggregate presentation independence O8;
7. composition compatibility O9;
8. non-sign sensitivity O10;
9. minimal-carrier requirement.

Record the smallest countermodel/widened family for every ablation.

## 12. Deterministic checker

Required path:

`scripts/cbrc_f2_validate_observable_nonsign_forward.py`

Minimum coverage:

- exact arithmetic representation of the accepted blind-input carrier;
- orbit classification for all one- and two-element aggregate states generated by `J,R,S`;
- exhaustive relative transport table on the minimal `(1,1)` fiber;
- every claimed scalar readout on a declared exact finite test window;
- composition through depth `>=4`;
- at least one three-alternative same-terminal test;
- every mandatory ablation countermodel;
- zero theorem/enumeration mismatches.

Enumeration is regression evidence only; infinite-domain claims require proof.

## 13. Target-leak kill conditions

Immediate `F2_TARGET_LEAK_INVALID` if the researcher:

- reads the full F1 counterfactual carrier section before raw freeze;
- imports downstream coherent-BRC/wave results;
- chooses a scalar law because it matches a known interference formula;
- assumes a square/norm/inner product/Born law;
- assumes a familiar phase group or coefficient ring beyond the blind packet;
- uses external quantum/wave theory as a premise;
- silently treats the F1 torsion orbit as already observable;
- silently kills the F1 torsion carrier because it does not resemble a familiar target.

## 14. Explicit non-goals

F2 must not:

- fit double-slit data;
- derive a continuum wave equation;
- derive or name a physical probability law;
- compare against R063/R064/R065 or downstream free-research carriers;
- optimize Shor or any quantum algorithm;
- promote any readout/carrier to Foundation truth.

## 15. Required artifacts

Return all of:

1. `research_reports/CBRC_F2_OBSERVABLE_NONSIGN_RECOALESCENCE_RETURN_20260822.md`
2. `research_reports/CBRC_F2_SOURCE_AND_TARGET_LEAK_AUDIT_20260822.md`
3. `research_reports/CBRC_F2_ABLATION_AND_COUNTERMODEL_PACKET_20260822.md`
4. `scripts/cbrc_f2_validate_observable_nonsign_forward.py`
5. `evidence/cbrc_f2_observable_nonsign_manifest.json`

The main return must contain:

- exact blind-input source SHA;
- orbit-space theorem;
- O1–O10 status table;
- readout existence/nonexistence proof;
- observable-minimal carrier result;
- finite-fiber extension;
- selector-dependency classification;
- ablation table;
- checker digest;
- unresolved assumptions;
- primary verdict.

## 16. Verdict taxonomy

Choose exactly one primary verdict:

- `F2_F1_CARRIER_OBSERVABLE_READOUT_FAMILY`
- `F2_F1_CARRIER_OBSERVABLE_UNIQUE_READOUT`
- `F2_F1_CARRIER_OBSERVATIONALLY_SILENT`
- `F2_LARGER_UNIQUE_MINIMAL_OBSERVABLE_CARRIER`
- `F2_FINITE_MINIMAL_OBSERVABLE_CARRIER_FAMILY`
- `F2_OBSERVABLE_CARRIER_UNDERDETERMINED`
- `F2_OBSERVABILITY_NO_GO_UNDER_CONSTRAINTS`
- `F2_TARGET_LEAK_INVALID`

## 17. Hard acceptance gate

Driver acceptance requires all of:

`F1_CARRIER_RELATIVE_OBSERVABILITY_ORBIT_SPACE_CLASSIFIED`

`NONSIGN_RECOALESCENCE_READOUT_EXISTENCE_CLASSIFIED`

`OBSERVABLE_NONSIGN_MINIMAL_CARRIER_FAMILY_CLASSIFIED`

`OBSERVABLE_NONSIGN_FINITE_FIBER_EXTENSION_CLASSIFIED`

`READOUT_SELECTOR_DEPENDENCY_CLASSIFIED`

`TARGET_LEAK_AUDIT_PASS`

plus all required ablations and deterministic checker evidence.

Failure of uniqueness is not task failure.

## 18. Freeze / handoff

Freeze the raw F2 packet on the owner branch and report:

- owner head SHA;
- artifact SHA-256 digests;
- checker deterministic digest;
- clean working-tree status;
- primary verdict.

Only after Driver acceptance may a separate downstream comparison or physical-model stage be opened.

---

Driver issue note:

`FIRST PROVE WHETHER THE NONSIGN SHEET CAN BE SEEN RELATIONALLY; DO NOT PRENAME THE READOUT.`
