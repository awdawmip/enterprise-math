# Exact historical ER/RR provenance in the execution audit

Auxiliary package `/root/stability_research`, authorized by owner after the actual reference-chain failure. Base `16cc5663c191a73e997e3a973f589197d0694c89`, worktree `D:/em/integration-owner-control-20260907`. This package changes only the audit wrapper, its audit-only registry, one regression module and this note. It creates no research claim, formal Result, execution intent, publication, mathematical adoption or remote action.

## Actual failure and immutable source checks

After the separately frozen taskbook-provenance repair, workflow steps 19, 20 and 21 passed. Step 22, `python control_plane/research_execution_record_audit_fault_isolation.py`, returned 12 errors, four for each of three existing ER payloads. The chain stopped before steps 23–34. Original and continuation logs remain in `TEMP/owner-control-reference-chain-20260907/`.

For each source the strict errors are retained explicitly: `missing execution_record_id`; `taskbook path differs from referenced publication generation`; `taskbook blob differs from referenced publication generation`; `allowed_outputs invalid`. These payloads contain literal `record_id` values and post-execution evidence, but omit canonical execution-intent ID, taskbook path/pin and allowed-output fields. No missing field is reconstructed from filenames, publication data or output manifests.

All three ERs, referenced publications, bound RRs, their taskbooks, the original strict audit implementation and the original audit registry were read and compared with baseline Git bytes. Source evidence is unchanged. The three exact pairs are:

| ER / RR | ER Git blob | RR Git blob |
|---|---|---|
| `ER-907FEC0874745310610E` / `RR-1337737608BDE3D7E620` | `sha1:af15aadec9a883aedf75ac0b68fde87da6dc4a56` | `sha1:c618fd689127b6b532ba47416c20fb61d28000ff` |
| `ER-020EE42FBD97E1978ADD` / `RR-65F19B398F4D33FEAE9C` | `sha1:e7e364226af86810b58c94eb98442fa25c568f0e` | `sha1:6a2405630b87d97ad7aeb0508e41ffcf12e94e75` |
| `ER-36B4FE8C61A135DD3AAE` / `RR-4B7576B2FDCA2CCBAB37` | `sha1:4534e1b172c1ec40edba5db11f54a1a54de894b5` | `sha1:f1aabc914bd1aa1381464c6a5a451de68b2207b1` |

Their referenced generation-1 taskbooks are respectively `research_tasks/N_COUPLED_PUBLIC_N_DISTRIBUTIONAL_NONEXTERNALIZABILITY_20260903.md` (`sha1:7be6bca90aeb7b1e8222090ea6e22797f9e96f8c`), `research_tasks/N_COUPLED_PUBLIC_N_NONREFLECTIVE_CAPABILITY_ASYMMETRY_20260901.md` (`sha1:21346d14f5ed3069cee2a26cc985b234379fdbbb`) and `research_tasks/N_COUPLED_PUBLIC_N_REALIZED_EFFECT_TRACE_NONCOMPILABILITY_20260902.md` (`sha1:243efaef4fb6e0b9f2faad08a6c8397ee5be844b`). Actual book bytes match publication pins. These reference paths do not retroactively supply missing intent fields or an allowed-output scope.

In every pair the ER's literal `record_id` equals the RR's `execution_record_id`; task, publication, claim, researcher, execution branch and branch-base identities all match. Each RR has a nonempty `frozen_at`, `terminal_verdict: NEGATIVE_BOUNDARY`, and exactly one manifest entry for the exact ER path/Git blob; the optional ER SHA256 also matches. The full paths and fixed IDs are recorded in the three new registry rows.

## Narrow audit-only contract

The added basis is `BOUND_FROZEN_RESULT_EXACT_LEGACY_RECORD`. It locates a source only through the explicitly registered record path and Git blob. The canonical `execution_record_id` key must actually be absent (present null also fails), while the existing literal payload `record_id` must equal the registered ID. The source keeps its original execution-record schema.

The row also fixes an RR path, Git blob and result ID. Validation checks the RR schema, execution reference, all six execution identity fields, frozen timestamp and matching terminal verdict. Its manifest must have unique valid paths and exactly one ER entry with the registered ER path/Git blob; a supplied SHA256 must also match. Safe repository-local source paths are required. Duplicate or mismatched ER manifest entries, changed source bytes, identity drift, missing terminal evidence and enabled authority flags fail.

This branch does not add an ID alias to `intent_for_claim` or the canonical execution record index. The two existing nonlive bases remain unchanged; using the ordinary frozen-result basis for a record missing canonical ID still fails. The registry's original seven row objects and all surrounding metadata retain their original bytes. Three rows are appended, each listing exactly its four observed errors and all four authority flags false. The existing stale/unused-suppression and extra-error checks remain active.

## Runtime boundary

Missing canonical ID alone is not a runtime-rejection proof: `tools/research_execution_records.py:118` indexes by task/claim and can return all three original payloads. At the inspected snapshot the distributional task has no canonical current publication; the other two still select the referenced generation. No live Issue history was fetched and no empty-live-history claim is made.

The unchanged `canonical_live_claim_binding` rejects an intent whose absent taskbook pin differs from the current publication's nonempty pin (`control_plane/research_runtime_guard_core.py:244`). Its later output-scope check also requires a nonempty `allowed_outputs` list. The audit registry is not read by intent lookup, dispatch, runtime ownership, Result authority or review authority. Historical evidence is preserved without making these malformed payloads executable or adopting their mathematical contents.

## Tests and validation

With the existing bundled Python 3.12.14 on Windows, the actual step-22 command returned exit 0 and reported ten pinned historical/terminal sources. The standalone `tests.test_exact_legacy_execution_audit` module passed 11 tests; the same 11 also passed in a process that first installed the full canonical bootstrap. This second invocation specifically checks the global-bootstrap interaction exposed by the separate taskbook fixture work.

Tests use actual temporary copies of ER/RR/publication/book bytes and the real audit validators. They cover exact four-error suppression, no filename-derived ID, no ID alias under old bases, present-null or present canonical ID, ER/RR byte drift, every RR identity field, absent frozen/terminal evidence, manifest path/blob/duplicate/SHA256 defects, flags/path escape, stale or missing suppressions and a real additional strict branch-base error. A guarded hypothetical winning-claim prefix exercises the unchanged runtime guard's missing-pin rejection; no real event is asserted or emitted. Lookup objects remain unchanged before and after audit.

Scoped baseline diffs confirm no changes under `research_execution_records`, `research_result_records`, `research_task_records`, `research_tasks`, or in `tools/research_execution_records.py`, `tools/research_dispatch.py` and `control_plane/research_runtime_guard_core.py`. The taskbook-provenance package remains separate; its independently owned fixture correction does not alter this audit's source boundary.

## Frozen author paths

| Path | SHA256 |
|---|---|
| `control_plane/research_execution_record_audit_fault_isolation.py` | `6f4c5fb2da19d9034093c77dd7fff023282e67396396b7fe0f102fcea4ffe41c` |
| `research_execution_record_audit_quarantines.json` | `f940db85e37ba38ad4ea9049901a2824cf7af9eb16b2d331ee872f414efaddcb` |
| `tests/test_exact_legacy_execution_audit.py` | `bb066d9c09e2a99460d5facf9f2ee4f7f7fbecf3cf5852e21ee0bbd50b664fab` |
| `research_notes/OWNER_EXACT_LEGACY_EXECUTION_AUDIT_20260907.md` | own hash supplied separately |

Global-Knowledge-Sync: main@ad231516 / GLOBAL_KNOWLEDGE_V1
