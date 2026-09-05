<!-- ENTERPRISE_MATH_TASK_V1
{
  "task_id": "RS-X6-LEGACY-PLANE-RECONCILIATION",
  "title": "Legacy plane research reconciliation under centered signed X6",
  "kind": "RESEARCH",
  "owner": "taskbook/unassigned",
  "base_state": "READY",
  "priority": "P0",
  "leverage": "HIGH",
  "frontier": "The centered signed X6 slice Foundation is current, but pre-rebase plane research may still survive in definitions, research notes, experiments, tests, theorem-facing prose, and downstream references with triple-intersection origin, positive/min-zero point identity, observer-gauge reversal asymmetry, or positive-sector counts typed as native facts.",
  "next_action": "Compare the complete pre-rebase plane corpus at fd2bcff10ca6e147348b6c1236027fc0d2877df3 against the centered-slice baseline at 59538f585d037d09ef687b28715c4bc1a3f9fe03, build a claim-level correction ledger, and begin exact recomputation of the highest-impact surviving native claims.",
  "dependencies": [
    {
      "target": "P000 V5 + signed X6 Cell-center Foundation at 59538f585d037d09ef687b28715c4bc1a3f9fe03",
      "action": "CONSUME",
      "satisfied": true
    },
    {
      "target": "centered three-axis slice rebase and exact recomputation packet at 59538f585d037d09ef687b28715c4bc1a3f9fe03",
      "action": "CONSUME",
      "satisfied": true
    },
    {
      "target": "pre-rebase plane generation at fd2bcff10ca6e147348b6c1236027fc0d2877df3",
      "action": "COMPARE",
      "satisfied": true
    }
  ],
  "source_refs": [
    "awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:p000_reality_foundation.json",
    "awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:definitions/ENTERPRISE_X6_NATIVE_SPATIAL_CELL_TORSOR_20260905.md",
    "awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:definitions/ENTERPRISE_X6_CENTERED_THREE_AXIS_SLICE_REBASE_20260905.md",
    "awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:definitions/ENTERPRISE_JOINT_RELATION_OBSERVER_PRESERVATION_20260905.json",
    "awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:experiments/x6_centered_three_axis_slice_v19_20260905/check_centered_slice_rebase.py",
    "awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03:experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py",
    "awdawmip/enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3:definitions/",
    "awdawmip/enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3:research_notes/"
  ],
  "evidence_status": "CENTERED_SLICE_FOUNDATION_MERGED_HISTORICAL_RECONCILIATION_OPEN",
  "last_progress_ref": "awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03",
  "last_progress_at": "2026-09-05T09:50:49+00:00",
  "hard_block": null,
  "tags": [
    "X6",
    "plane",
    "three-axis-slice",
    "historical-reconciliation",
    "observer-typing",
    "BRC",
    "foundation-maintenance"
  ],
  "claim_lease_minutes": 120,
  "created_by_role": "FOUNDATION_STEWARD",
  "task_authority": "PUBLISHED_REGISTERED",
  "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
  "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
  "registry_key": "RS-X6-LEGACY-PLANE-RECONCILIATION",
  "parent_objective_id": "PO-X6-SPATIAL-FOUNDATION-CONSISTENCY-20260905",
  "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
  "final_response_identity_policy": "INHERIT_GLOBAL",
  "identity_lane": "X6P",
  "origin_kind": "DIRECT_USER_DIRECTION",
  "task_lineage": "MAINTENANCE",
  "parent_task_id": null,
  "successor_gate": null,
  "policy_review": {
    "policy_set": "research_taskbook_policy.json",
    "policy_digest": "sha256:fbe51ab884e1267b7bb6de0de598ad5504fd0d67d1570475115a9a16a6ec4ca0",
    "review_state": "PASS",
    "temporary_overrides": []
  }
}
-->

# RS-X6-LEGACY-PLANE-RECONCILIATION — centered-X6 historical plane repair

Status: `PUBLISHED_REGISTERED / CLAIMABLE / DIRECT_USER_DIRECTION`

## Mother question

Which mathematical claims from the pre-centered three-axis Enterprise-plane program remain valid after the native plane is unified with the signed Cell-centered X6 geometry, which survive only as carrier/observer/path-combinatoric statements, and which must be recomputed or superseded?

The task is not to reopen the current X6 mother geometry. It is to repair the historical plane research so that every surviving result is typed at the strongest level actually supported by the current Foundation.

## Frozen inputs and scope

Mathematical baseline: `awdawmip/enterprise-math@59538f585d037d09ef687b28715c4bc1a3f9fe03`.

Historical comparison baseline: `awdawmip/enterprise-math@fd2bcff10ca6e147348b6c1236027fc0d2877df3`, immediately before the centered-slice rebase.

The following are frozen inputs for this task: P000 V5; `X6_NATIVE_SPATIAL = AFFINE_TORSOR(Z^6)`; signed primitive axis directions; the centered native three-axis slice as a signed `Z^3` affine subtorsor with a real Cell at coordinate zero; the X6 sum-of-squares component metric; and the observer-preservation requirement before any information-reducing quotient.

Audit the old plane program broadly enough to cover active definitions, research notes, experiments, scripts, tests, theorem-facing documentation, and downstream references whose semantics depend on the earlier plane ontology. Use historical generations to recover the exact old claims, but do not rewrite provenance merely to make history look current.

At minimum search and semantically inspect claims involving `O_E`, triple-boundary origin, `ORIGIN_IS_NOT_CELL_CENTER`, positive-only axes, `NO_NATIVE_NEGATIVE_AXES_REQUIRED`, `min(a,b,c)=0`, `A_E`, diagonal-shift decoding, directed line gauge, reversal asymmetry, `(1,0,4)`, `3-4-5`, the old `N=25` total `72`, `e_1+e_2+e_3=0`, carrier triangle return, circle Cell identity, and any later theorem or tool that consumed those claims.

Keep native Cell identity, carrier geometry, relative/min-zero observation, path identity, and BRC multiplicity/provenance as separate typed layers. For path claims, use the current signed endpoint/path interfaces rather than inferring path structure from the carrier endpoint alone.

Do not expand this task into complete native rotation dynamics, triadic-force dynamics, physical calibration, or unrelated number-theory programs. If a later higher-authority Foundation revision conflicts with the pinned mathematical baseline, preserve the conflict as an explicit return rather than blending generations.

## Hard target and required outputs

1. Produce a claim-level reconciliation ledger covering the pre-rebase plane corpus. Each material claim must record: source artifact and location; old statement; old semantic type; current status; corrected statement or strongest surviving restriction; exact evidence; downstream dependents; and required repository action. Use a finite status vocabulary such as `PRESERVE_NATIVE`, `PRESERVE_CARRIER`, `PRESERVE_OBSERVER`, `PRESERVE_PATH_BRC`, `RECOMPUTE`, `SUPERSEDE`, `NO_CHANGE`, and `UNRESOLVED_PROVENANCE`.

2. Recompute the old plane calculations from raw signed native coordinates before applying any relative observer. The regression set must include, at minimum:
   - legal zero Cell and signed unit neighbors;
   - reversal-symmetric native distance `sum d_i^2`;
   - exact min-zero residual plus common-depth reconstruction;
   - `(3,4,0)` and `(-3,-4,0)` both with squared native length `25`;
   - shortest-path BRC multiplicity `35` in both directions;
   - `(1,0,4)` retained only at the correct relative-observer strength;
   - `(1,1,1)` as a carrier return but native nonreturn, with squared native length `3` and six shortest signed words;
   - the full signed three-axis `N=25` shell with `30` endpoints and total shortest-path multiplicity `846`, while retaining `72` only as the historical positive-sector subtotal;
   - center spacing `1`, carrier radius `1/sqrt(3)`, pair overlap, triple carrier incidence, and gap-free cover at carrier-readout strength.

3. Re-audit every old formula discovered beyond the mandatory regression set. Do not assume that a formula is wrong merely because its historical interpretation was wrong; salvage exact algebra and combinatorics whenever they descend to a correctly typed native, carrier, observer, or path statement.

4. Trace downstream consumption. In particular inspect the historical R061 line-trace family, arbitrary-point directed gauge, bidirectional segment spectrum, derived diagonal displacement quotient, R062 BRC bridge, FCC slice/carrier material, path-valued operators, and any later result that imports their old plane semantics.

5. Correct current active surfaces that still expose a superseded plane claim as native truth. Historical evidence may remain historical, but current routing, theorem-facing statements, executable checks, and reusable interfaces must not require the reader to know an obsolete ontology to interpret them safely.

6. Add or extend exact checks so the corrected layer fails if any of the following are silently reintroduced as native facts: a non-Cell coordinate zero; positive-only native axis ontology; min-zero triple as complete Cell identity; reversal-asymmetric native distance caused only by canonicalization; carrier return as native return; or observer-only path counts as the full signed shell.

7. Return a compact residual list. Genuine unresolved mathematics exposed by the audit must be separated from mechanical historical repair and identified with the smallest exact unanswered question.

## Research value to preserve

The earlier plane program contains substantial valid material: triangular/FCC carrier geometry, circle-cover calculations, component traces, discrete path fibers, BRC multiplicities, and observer constructions. A coarse purge would destroy useful mathematics; leaving the old ontology uncorrected would allow false origin, sign, distance, and return semantics to leak back into later research.

This task therefore preserves the old work at its strongest valid typed level while making the centered signed X6 slice the single native spatial reference. The key value is a durable before/after map showing exactly what survived, what changed type, what changed value, and what genuinely failed.

## Success, kill, and return criteria

Success requires a reproducible ledger and recomputation packet such that every material pre-rebase plane claim located in the declared corpus has an explicit current disposition, every active/current consumer in scope is consistent with the centered signed X6 slice, and the mandatory numerical/algebraic witnesses agree with the current Foundation and signed BRC path semantics.

Do not guess through missing provenance. If an old result cannot be reconstructed from durable evidence, mark `UNRESOLVED_PROVENANCE` and identify the missing datum.

If repairing an old claim would require changing P000 V5 or the current centered signed X6 Foundation, stop that subclaim and return the exact contradiction witness. This maintenance task has no authority to mutate those frozen inputs.

If an apparent discrepancy is only a carrier/observer/native type mismatch and the old calculation remains exact at a lower layer, preserve it there instead of declaring it false.

The task is complete when no located active/current plane-era statement in scope still depends on a superseded native-origin, unsigned/min-zero identity, false reversal asymmetry, or carrier-return interpretation, and all remaining unresolved items are isolated as explicit research residues.
