# Independent audit of the exact historical execution-record bridge

Internal control assistant `/root/execution_gate_review`; no research identity, formal Driver review, claim, theorem disposition or promotion authority. This review made no edits to the four author paths below. It evaluated their actual worktree bytes against main baseline `16cc5663c191a73e997e3a973f589197d0694c89`.

## Decision and preserved boundary

**PASS for this four-path audit-only bridge.** The independent run verifies the three explicitly registered ER/RR pairs and the original seven quarantine rows. This decision is not a passing decision for the complete reference workflow: its next newly executed gate, step 24, fails on separate Result/Review integrity defects described below.

The new `BOUND_FROZEN_RESULT_EXACT_LEGACY_RECORD` branch is confined to the execution audit wrapper. It requires an explicit repository-local ER path and Git blob, an actually absent canonical `execution_record_id` key, the original literal `record_id`, and a fixed RR path, Git blob and result identity. It compares task, publication, claim, researcher, execution branch and branch-base identity; requires frozen terminal evidence with matching verdict; and requires exactly one manifest entry for the exact ER path/blob, including a matching SHA256 when supplied. It grants no execution, result, review, theorem or followup authority.

The existing `BOUND_FROZEN_RESULT_EXISTS` and `TERMINAL_EXECUTION_STATE` branches retain their old conditions. No general-purpose ID alias was added. Exact strict error strings remain the suppression unit; unused/stale suppressions and additional errors remain failures. The bridge does not replace the full Result schema, artifact or review audit.

The original seven row objects, all text before the end of their seventh object, and all metadata/trailing text after the registry array were compared by exact spans with baseline Git bytes. They are unchanged; only the three registered rows were appended. All twelve ER/RR/publication/taskbook source files for these pairs match baseline Git bytes exactly. Every book still matches its referenced publication pin. The strict execution tool, dispatch and runtime guard have no content change from the baseline; their worktree byte hashes also remained fixed throughout this run.

`intent_for_claim` can still return the unchanged legacy payloads by task/claim. Missing canonical ID alone is not a runtime rejection proof. The existing `canonical_live_claim_binding` rejects a missing taskbook pin against a real publication pin, and subsequently requires a nonempty allowed-output scope. The test uses a hypothetical winning-claim prefix only to reach that unchanged guard. It emits no Issue event and makes no statement about actual live claims.

## Actual independent execution

Interpreter: bundled Python **3.12.14**, Windows. These are local command results, not an Ubuntu/GitHub CI claim.

| Invocation | Actual result |
|---|---|
| `python -m unittest tests.test_exact_legacy_execution_audit -v` | 11 tests PASS; test runner 1.217 s; process 2.578 s |
| The same module after canonical `research_control_bootstrap.install()` | 11 tests PASS; test runner 1.541 s; process 6.141 s |
| Step 22: `python control_plane/research_execution_record_audit_fault_isolation.py` | PASS, exit 0; 1.766 s |
| Step 23: `python control_plane/check_legacy_control_isolation.py` | PASS, exit 0; 7.391 s |
| Step 24: `python control_plane/check_result_review_binding_fault_isolated.py` | FAIL, exit 1; 20.390 s |

Steps 25–34 were not executed. Earlier steps 1–21 retain their earlier evidence and are not claimed rerun. The composite executed frontier is therefore 23 passing workflow steps, followed by the step-24 failure. The workflow and all four author files, twelve source files and three protected runtime files remained byte-identical before/after this independent run.

The regression module exercises actual temporary source copies and real validators: exact four-error suppression; no filename-derived identity; no alias under old bases; absent versus null/present canonical ID; ER/RR byte drift; every execution identity field; frozen/terminal evidence; manifest path/blob/duplicate/SHA256 defects; authority flags and external source path rejection; stale/missing suppression; a real additional strict branch-base error; and unchanged lookup/runtime rejection.

## First newly failing gate: bounded diagnosis

Step 24 returned **53 errors**. A source-driven comparison recomputed every reported digest against baseline Git bytes. Every error-owning Result/Review record is byte-identical to the baseline. None of these 53 errors is attributable solely to Windows checkout line endings.

| Canonical cause | Error count |
|---|---:|
| Invalid enumerated values: eight Results with three free-text fields, plus three review destination classes | 27 |
| Existing declared pins mismatch the canonical target bytes | 13 |
| Required SHA256 pins are absent | 10 |
| Three Result references encounter the legacy ER identity shape | 3 |

The strict Result auditor immediately continues to the next Result after `unknown execution record`. Therefore suppressing only those three error strings would not prove that the rest of those Results had been checked. A later repair must explicitly preserve all remaining Result checks without installing a generic live `record_id` alias. Existing Result/Review records, frozen artifacts and Driver dispositions must remain intact; the present bridge does not repair or accept them.

Detailed local evidence is in `TEMP/owner-control-reference-chain-20260907/execution-independent-review/`:

- `summary.json`, SHA256 `55a9789d920ffe4924358747eec6ead7ec232687df38cfe683bea47b2d00402d`;
- `step24-first-failure-diagnosis.json`, SHA256 `e030e48bf7b44f08d1c4b3ed02c327d113ced09e16763615d13b9ae5b8b96d91`;
- separate stdout/stderr files for both test entrypoints and workflow steps 22, 23 and 24.

## Reviewed author snapshot

| Path | SHA256 |
|---|---|
| `control_plane/research_execution_record_audit_fault_isolation.py` | `6f4c5fb2da19d9034093c77dd7fff023282e67396396b7fe0f102fcea4ffe41c` |
| `research_execution_record_audit_quarantines.json` | `f940db85e37ba38ad4ea9049901a2824cf7af9eb16b2d331ee872f414efaddcb` |
| `tests/test_exact_legacy_execution_audit.py` | `bb066d9c09e2a99460d5facf9f2ee4f7f7fbecf3cf5852e21ee0bbd50b664fab` |
| `research_notes/OWNER_EXACT_LEGACY_EXECUTION_AUDIT_20260907.md` | `65ba90eb97487117b4843cc9f8308fce1d2fc5fbc9bdbaee7ee1f5a6b37a43de` |

No commit, push, record rewrite, official review or remote event was performed by this assistant.

Global-Knowledge-Sync: main@ad231516 / GLOBAL_KNOWLEDGE_V1
