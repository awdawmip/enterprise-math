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
    "research_inputs/CBRC_F7_BLIND_RANK_TWO_BALANCED_MIXING_EXISTENCE_PACKET_20260825.md@a730d90e64151c32e17f00c643839300898ffbb6",
    "driver_reviews/CBRC_F6_MINIMAL_RANK_TWO_CONSERVATIVE_CARRIER_DRIVER_REVIEW_20260825.md@86b1d5e5ca87e4215d73e5d3c6cbf7d4ec2dd215"
  ],
  "source_refs": [
    "research_inputs/CBRC_F7_BLIND_RANK_TWO_BALANCED_MIXING_EXISTENCE_PACKET_20260825.md@a730d90e64151c32e17f00c643839300898ffbb6"
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
2. verify/create and push owner branch
   `research/cbrc-f7-rank-two-balanced-mixing-existence-selector`;
3. commit/push
   `evidence/cbrc_f7_execution_stamp.json`
   containing at minimum:
   - Researcher-ID;
   - task ID;
   - exact taskbook source commit;
   - owner branch;
   - exact mathematical source ref;
   - `phase=STARTED_BEFORE_MATH`;
   - `mixing_verdict=null`;
   - `math_source_read_before_stamp=false`;
4. verify the remote owner branch resolves exactly to that stamp commit.

If this gate fails, stop without mathematics.

## 3. Mathematical whitelist / firewall

Before raw freeze, read/use only:

`research_inputs/CBRC_F7_BLIND_RANK_TWO_BALANCED_MIXING_EXISTENCE_PACKET_20260825.md@a730d90e64151c32e17f00c643839300898ffbb6`.

The taskbook is specification, not a mathematical premise. Repository/governance files may be read only for execution procedure.

Before raw freeze do **not** read:

- historical F3/F3R/F3R2 mixing reports or their checkers;
- R063/R064/R065/FQ mathematics;
- downstream coherent-BRC/wave research;
- external quantum mechanics, Hilbert spaces, Born rules, quantum walks, path integrals, gauge theory or wave equations;
- complex/Gaussian/Eisenstein/quadratic carrier material;
- rings, fields, arbitrary coefficient multiplication, roots of unity or phase groups;
- norms, inner products, quadratic forms, p-norms, polarization or square laws;
- Hadamard/Fourier/splitter targets;
- any known downstream rank-two mixing answer.

## 4. Frozen F7 universe

Use exactly the carrier, unary maps, scalar axioms, physical-equivalence boundary, and two-slot operational requirements in the blind packet.

Do not strengthen the packet silently.

In particular:

- do not assume `MP=PM`;
- do not assume mixing commutes with every unary map;
- do not assume a 2x2 or 4x4 target matrix shape;
- do not assume the new free direction `f` must be active merely because rank two was forced.

## 5. Q1 — exact existence/no-go

Determine whether there exists an additive automorphism

`M in Aut(C2 ⊕ C2)`

and one fixed marked scalar `q` satisfying all frozen F7 conditions globally on the declared marked pair domain.

For every witness:

- give an exact integral/free-torsion description of `M` and its inverse;
- prove global scalar conservation, not only the elementary split;
- verify elementary balance and A0;
- verify free-projection zero separation;
- verify genuine two-slot mixing under the declared physical equivalence.

If no witness exists, prove the no-go and identify the first incompatible condition.

Deliver:

`F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_CLASSIFIED`.

## 6. Q2 — new free direction participation

Classify whether successful exact mixing can leave `f` dynamically spectator.

Distinguish at least:

1. elementary spectator: the first column of the free block has zero `f_1,f_2` components;
2. invariant spectator sector: the full two-slot `f`-subspace is invariant and unmixed with `e`;
3. globally spectator: the operation is identity/sign/swap only on `f` while all nontrivial mixing occurs elsewhere;
4. genuinely active rank-two mixing: some irreducible free-block coupling between `e` and `f` remains under physical equivalence.

Prove which statuses are possible/impossible. If multiple occur, give exact inequivalent witnesses.

Deliver:

`F7_NEW_FREE_DIRECTION_PARTICIPATION_CLASSIFIED`.

## 7. Q3 — free-block structural constraints

Write the free quotient block in ordered basis `(e1,f1,e2,f2)` as `A in GL_4(Z)`.

Derive the strongest theorem-level constraints forced by:

- integral invertibility;
- elementary A0;
- elementary balance;
- global marked conservation;
- unary invariance of `q`;
- free-projection zero separation;
- physical equivalence.

At minimum classify:

- primitive first-column restrictions;
- any determinant/parity/congruence restrictions actually forced;
- invariant-sublattice obstructions;
- exact sufficient infinite or finite families if they exist;
- whether a bounded canonical normal form is provable.

A bounded `GL_4(Z)` census is regression evidence only and may not be used as an exhaustiveness proof.

Deliver:

`F7_RANK_TWO_FREE_BLOCK_CONSTRAINTS_CLASSIFIED`.

## 8. Q4 — scalar feasibility and selector status

Determine exactly what scalar information is forced.

Required:

- classify scalar laws for every explicit witness family as far as theoremically possible;
- decide uniqueness/nonuniqueness of `q`;
- search actively for exact countermodels to uniqueness;
- if strict underdetermination is claimed, exhibit at least two physically inequivalent exact `(M,q)` models satisfying the same frozen axioms;
- state whether periodic/support/pathological readouts remain possible under free-projection positivity;
- identify every extra regularity used by any narrower selector and keep it explicitly counterfactual unless admitted by a separate task.

Do not define a preferred scalar by resemblance to a norm or square law.

Deliver:

`F7_SCALAR_AND_MIXING_SELECTOR_STATUS_CLASSIFIED`.

## 9. Q5 — physical equivalence and minimum status

Physical equivalence may use only:

- marker relabeling;
- operation orientation `M <-> M^-1`;
- typed carrier automorphisms preserving the accepted F6 unary class and old projection.

Classify all returned witnesses under this equivalence.

If a complexity order is used to identify a smallest representative, declare it before use and prove whether it is only a bookkeeping minimizer or is actually selected by frozen axioms.

Deliver:

`F7_MIXING_PHYSICAL_EQUIVALENCE_AND_MINIMUM_STATUS_CLASSIFIED`.

## 10. Mandatory ablations

Ablate one at a time:

1. A0 elementary branch projection nondegeneracy;
2. free-projection zero separation;
3. unary invariance of `q`;
4. exact global marked conservation;
5. elementary balance;
6. additive invertibility of `M`;
7. marker relabeling equivalence;
8. inverse-orientation equivalence;
9. torsion `tau` preservation;
10. permission for the new free direction `f` to participate.

For each, record whether existence, scalar feasibility, physical classification, or selector status changes.

## 11. Deterministic checker

Required path:

`scripts/cbrc_f7_validate_rank_two_balanced_mixing_existence.py`

Minimum coverage:

- exact determinant/inverse checks for every witness matrix;
- torsion action consistency for every witness;
- elementary A0 and balance;
- exact finite-quotient or symbolic conservation checks used in proofs;
- unary-invariance checks for the scalar witnesses;
- physical-equivalence canonicalization for returned witness classes;
- bounded `GL_4(Z)` regression/counterexample search;
- all mandatory ablations;
- zero theorem/model mismatches.

If a scalar proof is genuinely infinite, the checker may test exact finite reductions only; the theorem proof must justify the reduction and completeness.

## 12. Required artifacts / checkpoints

### Checkpoint A — raw theorem freeze

Push drafts of:

1. `research_reports/CBRC_F7_RANK_TWO_BALANCED_MIXING_EXISTENCE_RETURN_20260825.md`;
2. `research_reports/CBRC_F7_MIXING_COUNTERMODEL_AND_ABLATION_PACKET_20260825.md`.

### Checkpoint B — audit/checker

Push:

3. `research_reports/CBRC_F7_SOURCE_AND_TARGET_LEAK_AUDIT_20260825.md`;
4. `scripts/cbrc_f7_validate_rank_two_balanced_mixing_existence.py`.

Run the exact pushed checker and record byte identity, result and deterministic digest.

### Checkpoint C — manifest

Push:

5. `evidence/cbrc_f7_rank_two_balanced_mixing_existence_manifest.json`.

Together with the initial execution stamp, all six artifacts are mandatory.

After every checkpoint verify the remote owner head before continuing.

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

Stop after freeze.

Do not proceed to a full arbitrary torsion-lift membership completion, ring/norm/square-law classification, or downstream wave comparison without Driver review.

---

Driver issue note:

`F6 FIXES THE MINIMAL RANK-TWO ADDITIVE/UNARY CARRIER. F7 NOW TESTS WHETHER BALANCED TWO-SLOT MIXING REALLY EXISTS AND WHETHER RANK TWO IS DYNAMICALLY USED, WITHOUT PRELOADING A KNOWN SPLITTER.`
