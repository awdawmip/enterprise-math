# Preserve the R005 named success through the current Result view

Classification: `CONTROL_PLANE_METADATA_COMPATIBILITY / NO_NEW_MATHEMATICS`.

## The actual boundary

The original published taskbook declares both its hard target and its exact success outcome as `R005_DEFICIT_SHADOW_EXECUTABLE_BINDING_CORRECTED_AND_BYTE_REVALIDATED`. Original Result `RR-566554389F6F36576DE2` reports `PASS` with that exact named disposition. Its immutable record blob is `aea04ecd76c5f6effe92726ae08d64c512f73131`, SHA-256 `5dc2a43840b2878013281cc49f4956c893754b4feab50148dbea2c75d8f5fc62`. The R005 Driver recovered the completed correction from PR1201, revalidated its final bytes and positive/negative paths, and admitted the original evidence and lawful two-head synthesis through PR1453 at main `d8dc1d37ca1ef7fc910d084eee36e5ab177cd03c`.

The current `research_driver_followup._task_scope_continuation` separately requires an ACCEPTED review, PASS/SUCCESS Result and the literal hard-target spelling `SATISFIED`. A read-only preflight with the actual R005 Result and the Driver's complete six-gate specification passed gate-shape/forced-gate checks but stopped at that literal comparison. Rewriting the Result would destroy its original evidence binding; control-result replacement also deliberately preserves the original hard-target spelling. Neither is the repair used here.

## Reuse the existing compatibility mechanism

Extend the existing `research_result_record_compatibility.json` / `control_plane/research_result_records_compat_runtime.py` mechanism with one constrained alias for `hard_target_disposition`. The runtime view may expose `SATISFIED` only for an explicitly registered, named historical success with all of these witnesses:

- the exact immutable Result path, ID and Git blob, retaining its original PASS/SUCCESS and raw named disposition;
- its exact V2 publication ID, canonical record path and Git blob;
- that publication's exact taskbook path and Git blob;
- the matching task identity in the taskbook header;
- an exact `Hard target` line and the exact full `Success is exactly` declaration in the frozen taskbook body.

The additional `hard_target_success_witness` object has exactly seven fields: `task_id`, `publication_id`, `publication_record_path`, `publication_record_blob_sha1`, `taskbook_path`, `taskbook_blob_sha1`, and `declared_success_line`. Generic outcomes such as PASS, PARTIAL, INCOMPLETE, NO_GO and NOT_SATISFIED cannot use this route. A positive-looking string without the frozen declaration cannot use it either. An unused witness, duplicate alias, altered input view or drift in any pinned object fails closed.

Append only `RRC-R005-DECLARED-SUCCESS-SPELLING-20260909` to the existing registry. All 57 prior Result normalizations and both review normalizations are preserved. The original R005 Result, outputs, publication, taskbook and mathematical claims are not rewritten. The seven witness fields do not themselves prove the task's mathematics; they identify the author's declared spelling. Review and execution authority remain separate.

## Authority boundaries and validation

The follow-up implementation and contract are unchanged. Current operational publication, accepted Driver authority, the six canonical gates, TASK-only terminal scope, absence of new tasks in portfolio continuation, exact raw Result SHA binding and the original parent scope remain required. No parent completion, Working Truth, Foundation, promotion or successor authority is added. Raw-source control-replacement checks continue to consume the original record and its original spelling.

Local validation used an explicitly bounded snapshot: local base4caf plus the 33 exact R005 source/intake paths and the three current compatibility code/registry/test pins from main d8dc. It is not described as a complete checkout of later main. The 11 new boundary tests, five existing compatibility tests and 12 existing public first-review/portfolio transaction tests passed together: 28 tests in 84.416 seconds. They include nonaccepted review, parent-scope, required-gate and immutable-byte rejection paths; the first draft used a nonexistent test constant and was corrected to read the shipped contract before this passing run.

The actual R005 six-gate read-only preflight then passed through the canonical compatibility view. The Result file still hashes to the original `5dc2a438...`; only the returned view uses `SATISFIED`. No formal review or follow-up was written by this preflight. The Driver remains responsible for the fresh exact-byte first-review transaction and main/GK persistence after this compatibility source is available.

Local receipts: `D:/em/TEMP/r005-result-success-alias-20260909/prepared-snapshot-receipt.json` and `actual-preflight-receipt.json`. Remote source and final-main readbacks are recorded separately when performed. No new mathematical computation, theorem acceptance or global CI success is asserted here.

Global-Knowledge-Sync: main@5f14819 / GLOBAL_KNOWLEDGE_V1
