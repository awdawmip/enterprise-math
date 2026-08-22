<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CBRC-F1-NONSIGN-RECOALESCENCE-CARRIER-FORWARD-CLASSIFICATION",
  "title": "Coherent-BRC F1 — Non-Sign Recoalescence Carrier Forward Classification",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "NONSIGN_RECOALESCENCE_MINIMAL_CARRIER_CLASSIFIED",
  "next_action": "Starting from the accepted F0 sign-only layer, classify the minimal conservative coefficient carrier admitting genuinely non-sign finite reversible path transport without importing any downstream phase algebra or readout law.",
  "dependencies": [
    "research/cbrc-f0-native-recoalescence-forward-derivation@501ab10b868f27a8468b1c0863d4435153ba4a2b",
    "driver_reviews/CBRC_F0_NATIVE_RECOALESCENCE_FORWARD_DERIVATION_DRIVER_REVIEW_20260822.md@d4c7dd11287b313360be9e53a5bad5dfd7f1b502"
  ],
  "source_refs": [
    "research/cbrc-f0-native-recoalescence-forward-derivation@501ab10b868f27a8468b1c0863d4435153ba4a2b",
    "driver_reviews/CBRC_F0_NATIVE_RECOALESCENCE_FORWARD_DERIVATION_DRIVER_REVIEW_20260822.md@d4c7dd11287b313360be9e53a5bad5dfd7f1b502"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED",
  "last_progress_ref": null,
  "last_progress_at": null,
  "hard_block": null,
  "tags": [
    "CBRC",
    "F1",
    "blind-forward",
    "recoalescence",
    "coefficient-carrier",
    "non-sign-transport",
    "minimal-extension",
    "foundation-facing"
  ],
  "claim_lease_minutes": 1440,
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "CBRCF1",
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:d5cbe89c8620ca6efa2af5219900424485c85bba1fc042576e17034c10e38299",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# Coherent-BRC F1 — Non-Sign Recoalescence Carrier Forward Classification

Task-ID: `RS-CBRC-F1-NONSIGN-RECOALESCENCE-CARRIER-FORWARD-CLASSIFICATION`

Driver: `EM-DVR-CBRC-F0-7C3A21 / CONTROL_PLANE`

Identity policy: `AUTO_RESOLVE_OR_ALLOCATE`

Identity lane: `CBRCF1`

Intended owner branch:

`research/cbrc-f1-nonsign-recoalescence-carrier-forward-classification`

## 0. Driver routing / why F1 exists

F0 is accepted at owner head:

`501ab10b868f27a8468b1c0863d4435153ba4a2b`

with Driver review:

`driver_reviews/CBRC_F0_NATIVE_RECOALESCENCE_FORWARD_DERIVATION_DRIVER_REVIEW_20260822.md`

at:

`d4c7dd11287b313360be9e53a5bad5dfd7f1b502`.

F0 established, at accepted scope:

1. current Path/N/Boolean BRC cannot produce conservative exact cancellation;
2. the minimal conservative cancellation extension is the free signed additive group on typed Path-formal witnesses;
3. scalar reversible transport on the resulting rank-one coefficient generator has only the sign automorphisms `±1`;
4. sign transport is classified up to gauge by a two-valued native diamond ratio;
5. exact dark cancellation already exists in the sign layer;
6. genuine branch mixing does not exist on that minimal integer-linear two-branch carrier under the declared equivariance/reversibility conditions;
7. the current F0 readout axioms do not select a unique scalar readout.

F1 must **not** try to repair F0 by importing a known coherent/wave algebra.

F1 asks only one next forward question:

> If one operationally requires reversible local transport strictly richer than sign/permutation, what is the minimal conservative coefficient carrier that can support it while preserving the accepted F0 typing, dark cancellation capability, composition, and choice independence?

Readout selection is not part of F1.

## 1. Hard target

`NONSIGN_RECOALESCENCE_MINIMAL_CARRIER_CLASSIFIED`.

The stage must classify whether a minimal carrier beyond the F0 sign-only layer exists, whether it is unique, whether several inequivalent minimal families survive, or whether the requirement is inconsistent with the native constraints.

The task must not optimize for any familiar downstream algebra.

## 2. F1 mathematical source whitelist

Before the F1 raw packet is frozen, read/use only:

1. the accepted F0 owner packet at `501ab10b868f27a8468b1c0863d4435153ba4a2b`:
   - `research_reports/CBRC_F0_NATIVE_RECOALESCENCE_FORWARD_DERIVATION_RETURN_20260822.md`;
   - `research_reports/CBRC_F0_SOURCE_AND_TARGET_LEAK_AUDIT_20260822.md`;
   - `research_reports/CBRC_F0_ABLATION_AND_COUNTERMODEL_PACKET_20260822.md`;
   - `scripts/cbrc_f0_validate_native_recoalescence_forward.py`;
   - `evidence/cbrc_f0_native_recoalescence_forward_manifest.json`;
2. the F0 Driver review at `d4c7dd11287b313360be9e53a5bad5dfd7f1b502`;
3. the four original F0 whitelist definitions, at the blob SHAs frozen in the F0 manifest.

Repository/governance files may be read only for execution/build procedure.

Record exact source SHAs in the return packet.

## 3. Continued blindness / forbidden preload

Until the F1 raw candidate packet is frozen, do **not** read or use:

- R063 Stage 1–4 mathematical results;
- R064/R065 mathematical results;
- any free-research coherent-BRC/wave journal or conversation result;
- Hodge/Shor route results;
- external quantum mechanics, complex amplitudes, quantum walks, Hilbert spaces, Born rules, path integrals, gauge theory, wave equations, or continuum scattering theory.

Also forbidden as starting assumptions or target selectors are any prechosen:

- coefficient ring such as a quadratic integer ring;
- element satisfying a named polynomial relation chosen because of downstream success;
- finite cyclic phase group;
- root of unity;
- complex number system;
- positive quadratic form / inner product;
- transform matrix;
- probability/readout exponent;
- known physical wave law.

Ordinary algebra, finitely generated abelian groups/modules, integer matrices, universal constructions, group actions, and finite classification theorems may be used if derived transparently from the F1 question.

## 4. Frozen F0 semantic boundary

Treat the following as frozen F0 inputs, not as hypotheses to be silently strengthened:

- the minimal same-terminal native multipath witness is the typed `(1,1)` commuting diamond;
- its two concrete path witnesses remain distinct until final aggregation;
- conservative exact cancellation minimally group-completes the nonnegative occurrence coefficient to a signed additive generator;
- the resulting scalar rank-one automorphism group is exactly `±1`;
- sign-only dark cancellation is possible;
- sign-only exact cancellation does not by itself select a scalar readout;
- no Foundation promotion occurred in F0.

Do not reopen F0 unless an exact contradiction is found under the same premises.

## 5. Operational meaning of `non-sign`

F1 may not define `non-sign` by naming a target phase.

Use this target-independent condition:

`NONSIGN_REVERSIBLE_TRANSPORT_EXISTS` iff there is a conservative coefficient extension `C` of the accepted signed generator and an invertible additive local transport `R:C->C` such that:

1. `R` is not `+id` and not `-id` on the generated coefficient carrier;
2. the orbit of an elementary embedded occurrence under `R` is finite and contains more than the two sign states;
3. the embedded additive inverse remains available, so exact dark cancellation has not been lost;
4. `R` is compatible with typed path concatenation/composition;
5. native branch relabeling/orientation reversal, if it acts on the carrier, acts by a derived equivalence rather than by arbitrary naming choice.

If any clause is redundant or inconsistent, prove that and replace it by the weakest exact formulation.

The finite-orbit condition is an F1 operational restriction: the stage is classifying the smallest **finite local transport alphabet** beyond signs. It is not permission to preselect a finite cyclic group.

## 6. F1-Q1 — rank-one no-go replay and extension order

Reprove at the minimum required level that the accepted rank-one signed coefficient carrier cannot satisfy `NONSIGN_REVERSIBLE_TRANSPORT_EXISTS`.

Then define an explicit partial order / complexity order on conservative extensions. It must consider at least:

1. additive rank of the torsion-free part;
2. whether old signed coefficients embed injectively;
3. number of new additive generators/relations;
4. finite orbit size of the new transport;
5. whether multiplication/composition is forced or additionally chosen.

Do not declare one carrier “minimal” without specifying the order.

Deliver:

`RANK_ONE_NONSIGN_NO_GO_AND_EXTENSION_ORDER`.

## 7. F1-Q2 — minimal additive carrier classification

Classify all conservative finitely generated additive extensions at the **smallest additive rank** that can admit a finite-order automorphism `R` satisfying the F1 non-sign conditions.

Required:

- prove the minimal possible additive rank;
- classify finite-order automorphisms at that rank up to integral change of basis compatible with the embedded old signed generator;
- derive the possible orbit sizes/minimal polynomials rather than naming them in advance;
- state whether the embedded sign involution `-id` lies in the subgroup generated by `R` or must be an independent central operation;
- distinguish strict uniqueness from several inequivalent minimal families.

If torsion allows a formally smaller construction, test it against conservative embedding/refinement consistency and either admit or kill it explicitly.

Deliver:

`MINIMAL_ADDITIVE_NONSIGN_CARRIER_FAMILY_CLASSIFIED`.

## 8. F1-Q3 — branch relabeling and conjugate-sheet action

For every minimal carrier surviving Q2, determine what branch-role swap and native orientation reversal can act as without introducing presentation dependence.

At minimum classify:

- whether `R` must be transported to `R^{-1}` under branch reversal;
- whether a conjugate two-sheet structure is forced, optional, or impossible;
- whether the resulting local transport class is independent of serialization of the two paths in the `(1,1)` diamond;
- whether absolute generator names can be eliminated in favor of an invariant orbit/class.

Do not assume a conjugation operation; derive it if required by choice independence.

Deliver:

`NONSIGN_RELABELLING_TRANSPORT_CLASSIFIED`.

## 9. F1-Q4 — composition / diamond extension

Extend each surviving local `R` consistently along native typed paths.

Classify whether a path transport may be represented by:

- vertex/edge data;
- elementary commuting-diamond data;
- a finite orbit-valued cocycle;
- or whether additional provenance is unavoidable.

Required checks:

1. depth-3 associativity;
2. depth-4 commuting-diamond composition;
3. generator swap;
4. cyclic sector copy/covariance at the same weak level allowed in F0;
5. exact preservation of the old sign-dark fiber as a subcase or limit.

No global three-sector coherent process may be claimed.

Deliver:

`NONSIGN_PATH_TRANSPORT_COMPOSITION_CLASSIFIED`.

## 10. F1-Q5 — does path composition force multiplication?

Start only with the minimal additive carrier(s) from Q2.

Ask whether distributive typed concatenation and repeated local transport force an internal multiplication on coefficients.

Possible outcomes include:

- a universal ring structure is forced;
- several inequivalent ring structures exist;
- only a module/action is required and ring multiplication is unnecessary;
- composition is inconsistent with one or more Q2 carriers.

If a ring emerges, prove its universal presentation from the F1 relations. Do not identify/name it by comparison to a known downstream number system before the raw packet freezes.

Deliver:

`COEFFICIENT_MULTIPLICATIVE_STRUCTURE_CLASSIFIED`.

## 11. Explicit non-goals

F1 must not:

- choose or derive a scalar probability/readout law;
- assume or prove a square/Born rule;
- fit double-slit or any continuum interference profile;
- derive a wave/Schrodinger/Dirac equation;
- optimize a quantum algorithm;
- compare the F1 carrier to any R063/R064/downstream coherent-BRC result before freeze;
- promote a carrier to Foundation truth.

The point is to isolate the minimal **carrier/transport** enlargement only.

## 12. Required ablations / countermodels

For every claimed uniqueness/minimality result, rerun after removing one at a time:

1. finite-orbit requirement;
2. conservative embedding of the F0 signed layer;
3. exact dark-cancellation preservation;
4. branch relabeling covariance;
5. orientation-reversal compatibility;
6. composition compatibility;
7. torsion-free requirement, if used;
8. minimal-rank requirement.

Record the smallest countermodel or widened family for each removal.

## 13. Required deterministic checker

Required path:

`scripts/cbrc_f1_validate_nonsign_carrier_forward.py`

Minimum coverage:

- rank-one no-go replay;
- exhaustive finite-order integral automorphism search at every rank actually claimed minimal, within a mathematically complete bound justified in the report;
- canonical-form or characteristic/minimal-polynomial checks for all survivor classes;
- embedded-sign preservation tests;
- branch-swap/reversal transport checks;
- path composition through depth >= 4;
- all mandatory ablation countermodels;
- zero theorem/enumeration mismatches.

Enumeration is evidence, not proof.

## 14. Required artifacts

Return all of:

1. `research_reports/CBRC_F1_NONSIGN_RECOALESCENCE_CARRIER_RETURN_20260822.md`
2. `research_reports/CBRC_F1_SOURCE_AND_TARGET_LEAK_AUDIT_20260822.md`
3. `research_reports/CBRC_F1_ABLATION_AND_COUNTERMODEL_PACKET_20260822.md`
4. `scripts/cbrc_f1_validate_nonsign_carrier_forward.py`
5. `evidence/cbrc_f1_nonsign_carrier_manifest.json`

The main report must include:

- exact frozen inputs and SHAs;
- declared extension/minimality order;
- additive-rank theorem;
- complete survivor family;
- relabeling/reversal classification;
- composition result;
- multiplication/ring verdict;
- ablation table;
- checker digest;
- unresolved assumptions;
- final verdict.

## 15. Verdict taxonomy

Choose exactly one primary verdict:

- `F1_UNIQUE_MINIMAL_NONSIGN_CARRIER`
- `F1_FINITE_MINIMAL_CARRIER_FAMILY`
- `F1_INFINITE_OR_PARAMETERIZED_MINIMAL_FAMILY`
- `F1_MINIMAL_RANK_ONLY_CARRIER_UNDERDETERMINED`
- `F1_NONSIGN_NO_GO_UNDER_CONSTRAINTS`
- `F1_EXISTENCE_WITHOUT_MINIMALITY`
- `F1_TARGET_LEAK_INVALID`

Secondary tags must separately report additive rank, transport orbit, relabeling, composition, and multiplication results.

## 16. Hard acceptance gate

Driver acceptance requires all of:

`RANK_ONE_NONSIGN_NO_GO_AND_EXTENSION_ORDER`

`MINIMAL_ADDITIVE_NONSIGN_CARRIER_FAMILY_CLASSIFIED`

`NONSIGN_RELABELLING_TRANSPORT_CLASSIFIED`

`NONSIGN_PATH_TRANSPORT_COMPOSITION_CLASSIFIED`

`COEFFICIENT_MULTIPLICATIVE_STRUCTURE_CLASSIFIED`

`TARGET_LEAK_AUDIT_PASS`

plus all required ablations and deterministic checker evidence.

Failure of uniqueness is not task failure.

## 17. Freeze / handoff

Freeze the F1 raw packet on the owner branch and report:

- owner head SHA;
- all artifact SHA-256 digests;
- checker deterministic digest;
- clean working-tree status;
- primary verdict.

Only after Driver acceptance may any downstream comparison stage be opened.

---

Driver issue note:

`SIGN_LAYER_ACCEPTED; CLASSIFY THE FIRST NON-SIGN CARRIER WITHOUT NAMING THE DESTINATION.`
