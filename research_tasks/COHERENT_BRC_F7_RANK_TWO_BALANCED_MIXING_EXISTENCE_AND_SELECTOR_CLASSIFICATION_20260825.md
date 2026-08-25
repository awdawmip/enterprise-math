<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION",
  "title": "Coherent-BRC F7 — Rank-Two Balanced Mixing Existence and Selector Classification",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_STATUS_CLASSIFIED",
  "next_action": "On the unique least F6 additive/unary rank-two object, independently classify whether exact balanced reversible two-slot mixing exists, whether the new free direction must participate, and whether the frozen axioms select a unique mixing/scalar class or remain strictly underdetermined.",
  "dependencies": [
    "research_inputs/CBRC_F7_BLIND_RANK_TWO_BALANCED_MIXING_EXISTENCE_PACKET_20260825.md@bc046c8d77910ddb1f42b572a736d9d938ecbb9c",
    "driver_reviews/CBRC_F6_MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_DRIVER_REVIEW_20260825.md@a36bfc4cbeab82704c3ebb17b8e93af0b7e2e4b7"
  ],
  "source_refs": [
    "research_inputs/CBRC_F7_BLIND_RANK_TWO_BALANCED_MIXING_EXISTENCE_PACKET_20260825.md@bc046c8d77910ddb1f42b572a736d9d938ecbb9c"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED_FIRST_RANK_TWO_MIXING_GATE",
  "tags": ["CBRC","F7","rank-two","two-slot-mixing","balanced","scalar-conservation","selector-status","blind-forward"],
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "CBRCF7"
}
-->

# Coherent-BRC F7 — Rank-Two Balanced Mixing Existence and Selector Classification

Task-ID:

`RS-CBRC-F7-RANK-TWO-BALANCED-MIXING-EXISTENCE-AND-SELECTOR-CLASSIFICATION`

Driver:

`EM-DVR-CBRC-F0-7C3A21 / CONTROL_PLANE`

Intended owner branch:

`research/cbrc-f7-rank-two-balanced-mixing-existence-selector`

## 0. Driver routing

F6 is Driver-accepted at working-extension scope. The unique least additive/unary rank-two class is frozen, but F6 intentionally did not classify any two-slot operation or scalar selector.

F7 is the first authorized two-slot stage. Its purpose is deliberately narrower than a complete arbitrary-lift classification: establish exact existence/no-go, structural free-block constraints, participation of the newly forced free direction, and uniqueness versus strict underdetermination.

Do not optimize for a familiar transform. A no-go or exact underdetermination theorem is a valid completion.

## 1. Hard target

`RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_STATUS_CLASSIFIED`.

Choose exactly one primary verdict:

- `F7_NO_BALANCED_RANK_TWO_MIXING_EXISTS`;
- `F7_BALANCED_RANK_TWO_MIXING_EXISTS_UNIQUE_CLASS`;
- `F7_BALANCED_RANK_TWO_MIXING_EXISTS_FINITE_CLASSES`;
- `F7_BALANCED_RANK_TWO_MIXING_EXISTS_STRICTLY_UNDERDETERMINED`;
- `F7_EXISTENCE_PROVED_BUT_STRUCTURAL_SELECTOR_STATUS_INCOMPLETE`;
- `F7_TARGET_LEAK_INVALID`.

## 2. Publication-liveness gate — before mathematics

Before reading any mathematical source:

1. allocate a fresh Researcher-ID;
2. verify/create and push owner branch `research/cbrc-f7-rank-two-balanced-mixing-existence-selector`;
3. commit/push `evidence/cbrc_f7_execution_stamp.json` containing Researcher-ID, task ID, exact taskbook source, owner branch, exact mathematical source ref, `phase=STARTED_BEFORE_MATH`, `mixing_verdict=null`, and `math_source_read_before_stamp=false`;
4. verify the remote owner branch resolves exactly to that stamp commit.

If this gate fails, stop without mathematics.

## 3. Mathematical whitelist / firewall

Before raw freeze, read/use only:

`research_inputs/CBRC_F7_BLIND_RANK_TWO_BALANCED_MIXING_EXISTENCE_PACKET_20260825.md@bc046c8d77910ddb1f42b572a736d9d938ecbb9c`.

The taskbook is specification, not a mathematical premise. Repository/governance files may be read only for execution procedure.

Before raw freeze do **not** read historical F3/F3R/F3R2 mixing reports/checkers; R063/R064/R065/FQ; downstream coherent-BRC/wave; external quantum mechanics; complex/Gaussian/Eisenstein/quadratic carrier material; rings/fields/multiplication; roots of unity or phase groups; norms/inner products/quadratic forms/p-norms/polarization/square laws; Hadamard/Fourier/splitter targets; or any known downstream rank-two answer.

## 4. Frozen F7 universe

Use exactly the carrier, unary maps, scalar axioms, physical-equivalence boundary, and two-slot operational requirements in the blind packet. Do not strengthen the packet silently.

In particular, do not assume `MP=PM`, mixing-unary commutation, a target matrix shape, or participation of `f` merely because rank two was forced.

## 5. Q1 — exact existence/no-go

Determine whether there exists an additive automorphism `M in Aut(C2 ⊕ C2)` and one fixed marked scalar `q` satisfying all frozen F7 conditions globally on the declared marked-pair domain.

For every witness, give an exact integral/free-torsion description of `M` and its inverse, prove global scalar conservation, verify elementary balance/A0/free-projection zero separation, and verify genuine mixing under the declared equivalence.

If none exists, prove the no-go and identify the first incompatible condition.

Deliver: `F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_CLASSIFIED`.

## 6. Q2 — new free direction participation

Classify whether successful exact mixing can leave `f` dynamically spectator. Distinguish elementary spectator, invariant spectator sector, globally spectator, and genuinely active rank-two coupling. Prove which statuses are possible/impossible and give inequivalent witnesses when multiple survive.

Deliver: `F7_NEW_FREE_DIRECTION_PARTICIPATION_CLASSIFIED`.

## 7. Q3 — free-block structural constraints

Write the free quotient block in basis `(e1,f1,e2,f2)` as `A in GL_4(Z)`.

Derive the strongest theorem-level restrictions forced by integral invertibility, A0, balance, global marked conservation, unary invariance, free-projection positivity and physical equivalence. At minimum classify primitive first-column restrictions, any forced congruence/parity/invariant-sublattice conditions, and exact sufficient families where possible.

A bounded `GL_4(Z)` census is regression evidence only, never an exhaustiveness proof.

Deliver: `F7_RANK_TWO_FREE_BLOCK_CONSTRAINTS_CLASSIFIED`.

## 8. Q4 — scalar feasibility and selector status

Classify scalar feasibility for every explicit witness family as far as theoremically possible. Decide uniqueness/nonuniqueness of `q`, search actively for exact countermodels to uniqueness, and determine whether multiple physically inequivalent exact `(M,q)` models survive.

If strict underdetermination is claimed, prove it by explicit inequivalent models, not parameter counting. Keep every additional selector regularity explicitly counterfactual unless separately admitted.

Deliver: `F7_SCALAR_AND_MIXING_SELECTOR_STATUS_CLASSIFIED`.

## 9. Q5 — physical equivalence and minimum status

Use only marker relabeling, orientation `M<->M^-1`, and typed carrier automorphisms preserving the accepted F6 unary class and old projection.

Classify all returned witness families under this equivalence. If a complexity order is introduced, declare it before use and distinguish bookkeeping minimization from axiom-selected physical uniqueness.

Deliver: `F7_MIXING_PHYSICAL_EQUIVALENCE_AND_MINIMUM_STATUS_CLASSIFIED`.

## 10. Mandatory ablations

Ablate one at a time:

1. A0;
2. free-projection zero separation;
3. unary invariance of `q`;
4. exact global marked conservation;
5. elementary balance;
6. additive invertibility of `M`;
7. marker relabeling equivalence;
8. inverse-orientation equivalence;
9. torsion `tau` preservation;
10. permission for `f` to participate.

Record the effect on existence, scalar feasibility, physical classification and selector status.

## 11. Deterministic checker

Required path:

`scripts/cbrc_f7_validate_rank_two_balanced_mixing_existence.py`

Minimum coverage:

- exact determinant/inverse checks for every witness matrix;
- torsion action consistency;
- elementary A0 and balance;
- exact finite quotient/symbolic conservation reductions used in proofs;
- unary-invariance checks for scalar witnesses;
- physical-equivalence canonicalization;
- bounded `GL_4(Z)` regression/counterexample search;
- all mandatory ablations;
- zero theorem/model mismatches.

If a scalar proof is infinite, the checker may test only the exact finite reduction; the report must prove the reduction.

## 12. Required artifacts / checkpoints

Initial mandatory artifact:

1. `evidence/cbrc_f7_execution_stamp.json`.

Checkpoint A — push:

2. `research_reports/CBRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_RETURN_20260825.md`;
3. `research_reports/CBRC_F7_MIXING_COUNTERMODEL_AND_ABLATION_PACKET_20260825.md`.

Checkpoint B — push:

4. `research_reports/CBRC_F7_SOURCE_AND_TARGET_LEAK_AUDIT_20260825.md`;
5. `scripts/cbrc_f7_validate_rank_two_balanced_mixing_existence.py`.

Run the exact pushed checker and record byte identity/result/digest.

Checkpoint C — push:

6. `evidence/cbrc_f7_rank_two_balanced_mixing_existence_manifest.json`.

Verify remote owner head after every checkpoint.

## 13. Hard acceptance gate

Driver acceptance requires:

`F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_CLASSIFIED`;
`F7_NEW_FREE_DIRECTION_PARTICIPATION_CLASSIFIED`;
`F7_RANK_TWO_FREE_BLOCK_CONSTRAINTS_CLASSIFIED`;
`F7_SCALAR_AND_MIXING_SELECTOR_STATUS_CLASSIFIED`;
`F7_MIXING_PHYSICAL_EQUIVALENCE_AND_MINIMUM_STATUS_CLASSIFIED`;
`RANK_TWO_BALANCED_MIXING_EXISTENCE_AND_SELECTOR_STATUS_CLASSIFIED`;
`TARGET_LEAK_AUDIT_PASS`;
publication-liveness checkpoints and deterministic checker evidence.

## 14. Freeze / stop

Freeze on the owner branch and report owner head, artifact SHA-256s, checker digest/result, clean-tree status and primary verdict.

Stop after freeze. Do not proceed to full arbitrary torsion-lift membership, ring/norm/square-law classification, or downstream wave comparison without Driver review.

---

Driver issue note:

`F6 FIXES THE MINIMAL RANK-TWO ADDITIVE/UNARY CARRIER. F7 NOW TESTS WHETHER BALANCED TWO-SLOT MIXING REALLY EXISTS AND WHETHER RANK TWO IS DYNAMICALLY USED, WITHOUT PRELOADING A KNOWN SPLITTER.`
