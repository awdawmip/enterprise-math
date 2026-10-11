# PCF7 existing correction Result: exact readonly control diagnosis

Captured at 2026-10-11 13:49 UTC. This is Source intake and control diagnosis under Root's bounded delegation. It performs no mathematical correction, checker replay, Task CLAIM/open, repair, Result/review write, or acceptance. The original parent remains OPEN.

## Current native route

Task: `RS-PRIME-COORD-FACTOR-COMPLEXITY-FAILURE-CLASSIFICATION-STATEMENT-CORRECTION`; current publication `TP2-1C146C521C5946742C17`, generation 2.

Own conversation: `codex-agent-pcf7-statement-correction-20261011`; own Researcher `EM-DIRECT-4F2ED1`; Source Session `MCP-8737609598fd45cb8d53e9c3ec640069`; activity `RA-A8DBB23DDCF971CDEFE71474`.

Session request 01 / Issue #3827 succeeded at comment `6109608647`. Source registration at `f44491f37327dd5f0f1d731054afbc843e5c2acf` was independently fetched in full: activity 663 bytes / SHA-256 `e809194f8dac09c0ec6943eb2f2018fb35d400b3535a39246442e04d252eb236` / blob `1a9858a2c2117e47b4d0c7073c911a6f26e05553`; session 1333 bytes / SHA-256 `271ac2e5e5c9011c615dd23d9950e7771f6ec705e6ea593066fbab3a837cd246` / blob `431bc988039b9e861f37436fc565d7bdf1d8f293`. All startup authority fields are false.

Continuation request 02 / Issue #3829 succeeded at comment `6109646808`, observed 2026-10-11 13:42 UTC, Source `d829b7e48451584bf608ad1389261c95324a74d6`, event snapshot SHA-256 `2ef248dd83d6d81eb231052cd93b58057f42e138931f2e7e8c477ead62e225b3`. Its exact native serialization was read by own receipt request 03 / Issue #3836, comment `6109689674`: all 17463 characters, SHA-256 `e1e6bfa2c7b7b4411ffac1392817e97b1e507ce8c718ba5f00fbab8bce47b9d5`, independently recomputed from the actual returned text. No remaining page exists.

Actual state: `BLOCKED / RESULT_CONTROL_AUTHORITY_WITHHELD / terminal=false`; route `RESOLVE_EXACT_RECORDED_CONTROL_BLOCK`, required role `CONTROL_PLANE_MAINTENANCE`, `execution_authorized=false`. `takeover_readiness=NO_LIVE_CLAIM`, operational actor/claim/session/lease null. No permitted fresh mathematical execution route is returned. This differs from the historical READY dossier and is not a declaration that no tasks exist.

## Exact frozen Result fault

Existing historical Result: `RR-F97259D79B7E7EF3F69F`, author `EM-PCF7FIX-B603FA`, frozen 2026-09-17 05:24 UTC, execution `ER-E90FEF513B0AEE96C73E`, claim `CLM-PCF7FIX-0BFF2D2CD73646AD`.

At the same Source, `research_result_authority_quarantines.json` has an exact nonoperational entry bound to Result blob `bba0267ffdc7b685517fec9ac809ab8fc715d408`, current publication blob `520ec677b26a5cd976a7b05406845e1b0f1f053e`, and flat execution blob `a0ca32627668c826ae1f9ea6fd0d26cff9658f1a`. It names precisely four allowed audit errors:

- `unknown execution record`;
- `invalid method_harvest`;
- `invalid independence_status`;
- `invalid source_exposure_status`.

The actual raw metadata values are respectively `BRC_TYPED_ZERO_FLAG_STATEMENT_REPAIR`, `TASK_LOCAL_PROOF_PLUS_DETERMINISTIC_CHECKER_REPLAY_PLUS_EXHAUSTIVE_SMALL_STATEMENT_AUDIT`, and `NONBLIND_DISCLOSED_TASK_RESEARCH`. They are outside the current strict sets in `control_plane/research_result_records_impl.py`. The strict enum sets were read from exact Source code; no normalization or acceptance is performed here.

The execution payload is at `research_execution_records/ER-E90FEF513B0AEE96C73E.json`, state `CLAIM_INTENT`. Exact current `tools/research_execution_records.py:89` indexes `directory.glob("*/*.json")`, so it excludes this flat file. The raw Result and flat execution agree on task, publication, claim, researcher, taskbook blob, and execution branch. Current Task generation/publication/taskbook match their pins. A missing artifact or mismatched current publication is not one of the four recorded faults.

The old activity `research_activity_records/RA-41fbc67e4f414058.json` exists, tied to session `chatgpt-autoA-20260917T045926Z-c8c9f1d5`, with all authority false and checkpoint state `VERIFY_EM_PUBLICATION`. It does not provide a current execution capability. No SourceSession or RA failure is named by the exact Result hold; no inference that an old activity upgrades authority is made.

The raw RR has no `write_authorization` field. That observation alone is not treated as an additional diagnosed fault: the actual native hold and exact quarantine enumerate the four errors above, not a current write-authority hold.

## Mathematical bytes and inherited boundaries

All five raw Result output-manifest rows were fetched in full and independently compared against their SHA-256 and Git-blob pins. Correction return 4747 bytes, statement audit 2058 bytes, checker replay 1025 bytes, execution 3119 bytes, original checker 4135 bytes all match. See `recovery/WITHHELD_RESULT_ALL_OUTPUT_BYTES_VERIFIED.json` for exact immutable URLs and every digest.

The correction return explicitly states in sections 1 and 2 that nonzero support-avoiding probes have gcd 1, zero probes have gcd N, and both fail the proper-factor predicate. It preserves the existing polynomial-prefix obstruction, exact declared worst-case split probability zero, L=N recurrence classification, T1–T5 strengths, sealed PCF2 benchmark, and no-global-lower-bound guard. These are historical author claims being consumed, not a new independent mathematical acceptance.

This is a standalone correction return, as allowed by the Taskbook. It does not physically rewrite the original 23375-byte PCF7 return. That original still contains the false all-gcd-1 statement in section 7 (paragraph starting line 374 / byte 9422) and the repeated checker description at section 14 item 5 (line 633 / byte 19634). The old statement audit quotes a plain-text section-7 before/after statement but contains no distinct exact section-14 span audit. Independent review must decide whether the standalone correction adequately resolves both occurrences under the Taskbook's permitted correction-return route. This report does not assume the answer.

The original checker filters zeros out of `fixed_probe_values()` and guards its unit-gcd assertion with `if v:`. It skips zero checks; it does not directly assert gcd(N,0)=N. The replay document describes that distinction accurately. Its historical replay and 50399-pair statement-audit claims were not rerun by this researcher, because no Task execution was authorized.

## Separate inherited review failure

Historical derived review `DR-027ED0C06D7B6A76E0FF` has raw disposition ACCEPTED and terminal true. Its Result-record SHA-256 pin equals the actual RR digest `a926c55a1aaecac16e4d7e4ca575eb3a3e1dcb5452bf19245de213c4a7e63568`.

However, its review-artifact pins are blob `09632ce122f6acbd8e908d57cb79f3db75392f1b` / SHA-256 `bc3c4716fe2069eef7c007749081da5677bc2906b5a8740a1154695cc191446f`; the current review Markdown is blob `00673bfa87f7f6d5e6a738be87afda83141d4351` / SHA-256 `1eea04a0298e2a26c6b7923e2377f0887167dd6d34f2f756850759543b006642`. Exact `research_result_review_audit_quarantines.json` records `review artifact digest drift`, nonoperational, with history preserved. This is additional to the Result-derived hold. Raw ACCEPTED is therefore not current review authority.

Exact connector GETs for the native packet's old claim comment `5708985481` and last server comment `5709174722` both returned 404. Those failure responses are saved. Their original event bodies were not independently recovered, and no successful server-comment readback or old actor authorization is claimed.

## Existing repair contract boundary

Native recovery asks for a valid Result under the ordinary Result/replacement contract followed by strict gate reevaluation. The exact Source `research_result_control_replacement_contract.json` requires same Task, publication, execution, claim, researcher, return blob and mathematical terminal verdict; immutable old records/reviews stay preserved; common manifest bytes stay identical and the corrected manifest strictly extends the old one; active Source-backed Driver authority is required.

The actual `_CORE_EQUAL_FIELDS` in `research_result_control_replacements.py:42` also includes method_harvest, independence_status and source_exposure_status. Thus directly changing the three invalid enum strings in a same-execution corrected Result violates this current replacement validator's equality rule. Merely copying the flat execution into the canonical index would confer authority not granted by the existing hold. Neither operation is performed or recommended as an already valid repair.

Exact `control_plane/research_result_authority_fault_isolation.py:301` distinguishes a same-execution corrected Result requiring a validated replacement chain from a separately executed clean sibling. The current native route does not grant permission to open that sibling. The independent control auditor and current Root Driver must establish the legitimate route; this report does not invent a replacement Task, claim, alias or exemption.

## Durable local handoff

All material remains in this isolated directory. Original Source records remain unchanged. Root owns legal recovery choice, independent review and Source publication. Author contribution history and shared directed context remain disclosed. No mathematical novelty, generic factoring successor, task completion, parent completion, Working Truth or Foundation promotion is asserted.

The exact response files, full native receipt, input digest index, output verification index, current quarantine entries, code pins, and 404 evidence suffice to recover the diagnostic without hidden chat context. New mathematical execution should start only after a current native packet provides its actual lawful route.
