<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-CBRC-F5R-INDEPENDENT-FORGETFUL-BRANCH-SEMANTIC-REPLICATION",
  "title": "Coherent-BRC F5R — Independent Forgetful-Branch Semantic Replication",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P1",
  "leverage": "HIGH",
  "frontier": "FORGETFUL_BRANCH_NONDEGENERACY_SEMANTIC_STATUS_INDEPENDENTLY_CLASSIFIED",
  "next_action": "Independently re-execute the lost F5 semantic gate from the original frozen whitelist, determine whether per-branch nonzero projection is derived or additional, and materialize the complete evidence surface with publication-liveness guards.",
  "dependencies": [
    "research_inputs/CBRC_F5_BLIND_FORGETFUL_BRANCH_SEMANTICS_PACKET_20260823.md@a107c133e11597623bbe79ef37397fc8ba5c13f7",
    "driver_reviews/CBRC_F5_RETURN_MATERIALIZATION_RECOVERY_DRIVER_REVIEW_20260825.md@ec7888269ab8d45acf61d047a4945dfff6287289"
  ],
  "source_refs": [
    "research_inputs/CBRC_F5_BLIND_FORGETFUL_BRANCH_SEMANTICS_PACKET_20260823.md@a107c133e11597623bbe79ef37397fc8ba5c13f7",
    "definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md@6ec0d73a19e28ec586c59a97d24f5798c9119771",
    "definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md@b631242db84c5bd3640e6dc554b19a1d04d464f3"
  ],
  "evidence_status": "TASKBOOK_DRIVER_APPROVED_REEXECUTION",
  "tags": ["CBRC","F5R","independent-replication","semantic-gate","forgetful-map","branch-nondegeneracy","publication-liveness"],
  "created_by_role": "RESEARCH_DRIVER",
  "task_authority": "DRIVER_APPROVED",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "identity_lane": "CBRCF5R"
}
-->

# Coherent-BRC F5R — Independent Forgetful-Branch Semantic Replication

Task-ID:

`RS-CBRC-F5R-INDEPENDENT-FORGETFUL-BRANCH-SEMANTIC-REPLICATION`

Driver:

`EM-DVR-CBRC-F0-7C3A21 / CONTROL_PLANE`

Intended owner branch:

`research/cbrc-f5r-independent-forgetful-branch-semantics`

## 0. Why this task exists

The original F5 execution was reported complete, but its mathematical return, checker, manifest, owner branch and handoff evidence were never materialized remotely. A recovery-only task correctly searched for the original artifacts, found none, and stopped without reconstructing mathematics.

Therefore F5R is a **fresh independent mathematical re-execution**, not a recovery and not a continuation from a remembered verdict.

Do not try to infer what the lost F5 conclusion probably was.

The purpose is to answer the same semantic gate independently and leave a durable evidence surface.

## 1. Hard target

`FORGETFUL_BRANCH_NONDEGENERACY_SEMANTIC_STATUS_INDEPENDENTLY_CLASSIFIED`.

Choose exactly one primary verdict:

- `F5R_DERIVED_FROM_EXISTING_NATIVE_REFINEMENT`;
- `F5R_NEW_AXIOM_REQUIRED`;
- `F5R_WEAKER_DERIVED_CONDITION_ONLY`;
- `F5R_INCONSISTENT_WITH_NATIVE_REFINEMENT`;
- `F5R_UNDERDETERMINED_BY_CURRENT_SEMANTICS`;
- `F5R_TARGET_LEAK_INVALID`.

Failure to derive the candidate is a valid success condition.

## 2. Publication-liveness gate — BEFORE mathematics

This section is mandatory and must be completed before any mathematical derivation.

1. Allocate a fresh Researcher-ID distinct from all prior F5 identities.
2. Create/push the owner branch:
   `research/cbrc-f5r-independent-forgetful-branch-semantics`.
3. On that branch, create and commit:
   `evidence/cbrc_f5r_execution_stamp.json`
   containing at minimum:
   - Researcher-ID;
   - this task ID;
   - exact taskbook source commit;
   - owner branch;
   - the three mathematical source refs below;
   - `phase = STARTED_BEFORE_MATH`;
   - `mathematical_verdict = null`.
4. Verify the remote owner branch resolves to that stamp commit.

If this publication-liveness gate cannot be completed, stop and report an execution failure. Do not do mathematics in an unmaterialized local-only state.

## 3. Mathematical whitelist / firewall

Before raw mathematical freeze, read/use only:

1. `research_inputs/CBRC_F5_BLIND_FORGETFUL_BRANCH_SEMANTICS_PACKET_20260823.md@a107c133e11597623bbe79ef37397fc8ba5c13f7`;
2. `definitions/ENTERPRISE_BRC_MULTIPATH_ENRICHMENT_BRIDGE_20260821.md` at blob `6ec0d73a19e28ec586c59a97d24f5798c9119771`;
3. `definitions/ENTERPRISE_NATIVE_LINE_TRACE_FORMULA_20260821.md` at blob `b631242db84c5bd3640e6dc554b19a1d04d464f3`.

The recovery Driver review may be read only to understand why F5R is a re-execution; it supplies **no mathematical premise**.

Do not read/use before raw freeze:

- any missing/later reconstruction claim about the original F5 verdict;
- full F0–F4 reports beyond facts already frozen into the F5 blind packet;
- R063/R064/R065/FQ mathematics;
- downstream coherent-BRC/wave free research;
- external quantum mechanics, quantum walks, Hilbert spaces, Born rules, path integrals, gauge theory or wave equations;
- any preselected rank-two/complex/quadratic carrier, phase group, norm, inner product, square law, Hadamard/Fourier/splitter target.

## 4. Candidate — do not assume

Let

`pi : C -> Z e`

be the conservative forgetful retraction from an enriched coefficient carrier to the old signed occurrence coordinate.

For an elementary two-branch refinement/mixing

`M(e,0)=(x,y)`, define

`FORGETFUL_BRANCH_NONDEGENERACY`

iff

`pi(x) != 0` and `pi(y) != 0`.

This is the object to classify, not a premise.

## 5. Q1 — exact type audit

Separate rigorously:

1. concrete Path-formal witness `[p]`;
2. formal coefficient multiplying `[p]`;
3. marked slot retaining a distinguishable alternative;
4. enriched coefficient state in `C`;
5. forgetful projection `pi`;
6. marker erasure / same-terminal recoalescence.

Determine which notions are canonical in the allowed sources and which belong only to later coefficient bookkeeping.

Deliver:

`F5R_PATH_WITNESS_VS_MARKED_SLOT_SEMANTIC_BOUNDARY_CLASSIFIED`.

## 6. Q2 — derivability / independence

Classify whether a retained marked alternative must project nontrivially under `pi`.

At minimum distinguish these exact semantic models:

### S-A — basis-refinement semantics
Every retained marked branch refines at least one concrete Path-formal basis witness with nonzero old coefficient.

### S-B — carrier-state semantics
A retained marked branch is merely a nonzero enriched carrier state in a typed slot; its old projection may be zero.

### S-C — total-only semantics
Only the total marked family is required to recover the old occurrence/multiplicity after forgetting; individual branches may have zero projection.

Determine which, if any, is logically forced by the canonical sources. If multiple models satisfy the source semantics, prove independence with explicit countermodels rather than declaring ambiguity informally.

Deliver:

`F5R_FORGETFUL_BRANCH_NONDEGENERACY_DERIVABILITY_CLASSIFIED`.

## 7. Q3 — load-bearing implication audit

Test individually whether any of the following already imply per-branch nonzero projection:

- Path-formal provenance retention;
- conservative embedding/retraction;
- no-resurrection;
- marker refinement consistency;
- reversibility before marker erasure;
- typed locality;
- preservation of total old signed coefficient;
- preservation of old Boolean support.

For each implication claim give a proof. For each failure give the smallest exact semantic countermodel.

In particular test whether a nonzero enriched branch with `pi=0` can coexist with all of:

- exact nonzero enriched state;
- correct total old projection;
- invertible pre-collapse refinement;
- unchanged old Boolean support after forgetting;
- preserved Path-formal provenance on the genuinely old-supported branch(es).

Deliver:

`F5R_BRANCH_SURVIVAL_LOAD_BEARING_AXIOMS_CLASSIFIED`.

## 8. Q4 — strongest genuinely derived substitute

If full per-branch nondegeneracy is not derived, identify the strongest theorem that *is* forced. Candidates may include, but must not be assumed:

- total projected coefficient remains nonzero;
- total projected Boolean support is preserved;
- at least one marked branch has nonzero projection;
- each branch family associated to an original basis witness has nonzero total projection;
- no new old-support basis witness can be resurrected after forgetting.

State the strongest derivable condition and prove maximality by countermodel to every stronger natural formulation you reject.

Deliver:

`F5R_MAXIMAL_DERIVED_FORGETFUL_BRANCH_CONDITION_CLASSIFIED`.

## 9. Q5 — rank consequence, strictly conditional

Use only the F4 boundary already included in the blind packet:

- under `GLOBAL_ZERO_SEPARATION`, every successful torsion-free-rank-one model has a signed-permutation free quotient block;
- a signed-permutation first column cannot have two nonzero old-coordinate projections.

Therefore:

- if F5R genuinely derives `pi(x)!=0` and `pi(y)!=0`, freeze only
  `torsion_free_rank(C) >= 2`;
- if that condition requires a new axiom, report the lower bound only as
  `CONDITIONAL_ON_NEW_AXIOM`;
- if only a weaker condition is derived, state exactly whether it kills or fails to kill the F4 torsion loophole.

Do not construct, name, classify or preselect any rank-two carrier.

Deliver:

`F5R_CONDITIONAL_RANK_CONSEQUENCE_CLASSIFIED`.

## 10. Mandatory ablations

At minimum ablate one at a time:

1. branch-to-concrete-witness correspondence;
2. conservative retraction `pi`;
3. no-resurrection;
4. reversibility;
5. total old-coefficient preservation;
6. old Boolean support preservation;
7. marker identity/provenance retention.

Record whether the candidate condition becomes derived, independent, weaker, stronger, meaningless or unchanged.

## 11. Deterministic checker

Required path:

`scripts/cbrc_f5r_validate_forgetful_branch_semantics.py`

Minimum coverage:

- minimal `(1,1)` two-witness Path-formal fiber;
- finite formal-sum and signed-coefficient semantic toy models;
- exact embedding/retraction and projection tests;
- S-A / S-B / S-C model witnesses;
- total projection/support preservation;
- all mandatory ablations;
- zero theorem/model mismatch on every finite semantic model used.

The checker is evidence only; semantic implication/independence claims require proofs in the return.

## 12. Mandatory materialization checkpoints

To prevent another lost-return event:

### Checkpoint A — after theorem statements are stable
Commit/push drafts of:

- `research_reports/CBRC_F5R_INDEPENDENT_FORGETFUL_BRANCH_SEMANTICS_RETURN_20260825.md`
- `research_reports/CBRC_F5R_SEMANTIC_COUNTERMODEL_AND_ABLATION_PACKET_20260825.md`

before final polish.

### Checkpoint B — before final verdict
Commit/push:

- `research_reports/CBRC_F5R_SOURCE_AND_TARGET_LEAK_AUDIT_20260825.md`
- `scripts/cbrc_f5r_validate_forgetful_branch_semantics.py`

Run the exact checker from the pushed owner branch and record its result.

### Checkpoint C — final freeze
Commit/push:

- `evidence/cbrc_f5r_forgetful_branch_semantics_manifest.json`

containing source refs, artifact SHA-256s, checker digest/result, owner branch, primary verdict and final materialization status.

After each checkpoint, verify the remote branch resolves to the new commit before continuing.

## 13. Required artifacts

All are mandatory:

1. `research_reports/CBRC_F5R_INDEPENDENT_FORGETFUL_BRANCH_SEMANTICS_RETURN_20260825.md`
2. `research_reports/CBRC_F5R_SOURCE_AND_TARGET_LEAK_AUDIT_20260825.md`
3. `research_reports/CBRC_F5R_SEMANTIC_COUNTERMODEL_AND_ABLATION_PACKET_20260825.md`
4. `scripts/cbrc_f5r_validate_forgetful_branch_semantics.py`
5. `evidence/cbrc_f5r_forgetful_branch_semantics_manifest.json`
6. the initial `evidence/cbrc_f5r_execution_stamp.json`.

## 14. Hard acceptance gate

Driver acceptance requires all of:

`F5R_PATH_WITNESS_VS_MARKED_SLOT_SEMANTIC_BOUNDARY_CLASSIFIED`

`F5R_FORGETFUL_BRANCH_NONDEGENERACY_DERIVABILITY_CLASSIFIED`

`F5R_BRANCH_SURVIVAL_LOAD_BEARING_AXIOMS_CLASSIFIED`

`F5R_MAXIMAL_DERIVED_FORGETFUL_BRANCH_CONDITION_CLASSIFIED`

`F5R_CONDITIONAL_RANK_CONSEQUENCE_CLASSIFIED`

`TARGET_LEAK_AUDIT_PASS`

plus deterministic checker evidence and the publication-liveness checkpoints.

## 15. Freeze / stop

Freeze on:

`research/cbrc-f5r-independent-forgetful-branch-semantics`

and report:

- Researcher-ID;
- taskbook source commit;
- owner head SHA;
- artifact SHA-256s;
- checker deterministic digest/result;
- clean-tree status;
- primary verdict.

After freeze, stop.

No F6, rank-two construction, downstream wave comparison or Foundation promotion is authorized by F5R.

---

Driver issue note:

`ORIGINAL F5 RETURN LOST; RE-EXECUTE THE SEMANTIC GATE INDEPENDENTLY, PRESERVE BLINDNESS, AND MATERIALIZE EVIDENCE BEFORE CLAIMING COMPLETION.`
