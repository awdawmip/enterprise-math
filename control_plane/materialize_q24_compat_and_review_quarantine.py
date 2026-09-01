#!/usr/bin/env python3
"""One-shot branch materializer for exact immutable current control metadata.

This script is deleted in the same commit that materializes its output. It never
rewrites Result, Driver-review, execution, task, or authority records. It only
appends exact Git-blob-pinned compatibility/quarantine rows to existing control
registries so invalid immutable generations leave the operational view without
manufacturing replacement authority or changing mathematical dispositions.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULT_COMPAT = ROOT / "research_result_record_compatibility.json"
RESULT_QUARANTINE = ROOT / "research_result_record_quarantines.json"
REVIEW_QUARANTINE = ROOT / "research_result_review_audit_quarantines.json"
DRIVER_COMPAT = ROOT / "research_driver_authority_compatibility.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def append_unique(rows: list[dict], row: dict, id_field: str) -> None:
    value = row[id_field]
    existing = [item for item in rows if item.get(id_field) == value]
    if existing:
        require(existing == [row], f"{id_field} {value} already exists with different bytes")
        return
    rows.append(row)


def write_json(path: Path, value: dict, *, compact: bool = False) -> None:
    text = (
        json.dumps(value, ensure_ascii=False, separators=(",", ":"))
        if compact
        else json.dumps(value, ensure_ascii=False, indent=2)
    )
    path.write_text(text + "\n", encoding="utf-8")


def materialize_result_compatibility() -> None:
    compat = json.loads(RESULT_COMPAT.read_text(encoding="utf-8"))
    require(
        compat.get("schema") == "ENTERPRISE_MATH_RESEARCH_RESULT_COMPATIBILITY_V1"
        and compat.get("status") == "ACTIVE",
        "unexpected result compatibility registry schema/status",
    )
    rows = compat.get("result_normalizations")
    require(isinstance(rows, list), "result_normalizations must be a list")
    append_unique(
        rows,
        {
            "normalization_id": "RRC-CURRENT-RR-1DE3F3213271AED2625C-ENUMS",
            "result_id": "RR-1DE3F3213271AED2625C",
            "record_path": "research_result_records/RS-P000-PHILOSOPHY-FIRST-NATIVE-MODEL-CHANGE-ARROW-AUDIT/RR-1DE3F3213271AED2625C.json",
            "record_blob_sha1": "sha1:10debd66fe28265a45203a42723603428e21ccbc",
            "field_aliases": [
                {
                    "field": "method_harvest",
                    "from": "RESULT_ONLY / NO_NEW_TOOL_PAYLOAD",
                    "to": "RESULT_ONLY",
                },
                {
                    "field": "independence_status",
                    "from": "NONBLIND_TASK; current P000 worldview/foundation plus Q10, Q11, Q18 and Q21 accepted internal semantics were intentionally consumed.",
                    "to": "SHARED_AMBIENT_CONTEXT_DISCLOSED",
                },
                {
                    "field": "source_exposure_status",
                    "from": "PROJECT_INTERNAL_ACCEPTED_RESULTS_PLUS_ACCOUNT_P000_WORLDVIEW; NO_EXTERNAL_NOVELTY_CLAIM",
                    "to": "NONBLIND_DISCLOSED",
                },
            ],
            "artifact_sha256_repairs": [],
            "reason": "Current control compatibility only: exact immutable Q24 Result bytes remain unchanged; the three free-form metadata values are conservatively normalized to current V1 enum classes under the exact Result Git-blob pin. No mathematical, Driver, Working Truth, Foundation, promotion or successor authority changes.",
        },
        "result_id",
    )
    write_json(RESULT_COMPAT, compat, compact=True)


def materialize_result_quarantine() -> None:
    payload = json.loads(RESULT_QUARANTINE.read_text(encoding="utf-8"))
    require(
        payload.get("schema") == "ENTERPRISE_MATH_RESEARCH_RESULT_QUARANTINE_V1"
        and payload.get("status") == "ACTIVE",
        "unexpected result quarantine schema/status",
    )
    rows = payload.get("entries")
    require(isinstance(rows, list), "result quarantine entries must be a list")
    append_unique(
        rows,
        {
            "resolution_id": "RQ-NCASOT-B923-20260901",
            "result_id": "RR-B9234FB62194F252F751",
            "record_path": "research_result_records/RS-N-COUPLED-OPAQUE-LAZY-TYPED-SUPPORT-SCALARIZATION-DELAY/RR-B9234FB62194F252F751.json",
            "record_blob_sha1": "sha1:70d2bddb863835a67b47d256e94a783437c4a858",
            "corrected_result_id": "RR-00F7FFAA06553D90B4AC",
            "task_id": "RS-N-COUPLED-OPAQUE-LAZY-TYPED-SUPPORT-SCALARIZATION-DELAY",
            "publication_id": "TP2-6C1A4E92B7D3058F2A41",
            "resolution": "QUARANTINE_INVALID_RECORD",
            "operational": False,
            "history_preserved": True,
            "reason": [
                "Two independently frozen executions used the same task-level return/checker paths with different primary Git blobs; repository integration can retain only one byte sequence at each shared path.",
                "RR-B9234FB62194F252F751 therefore fails the primary return/checker Git-blob pins and cannot be repaired by a secondary SHA-256 compatibility alias.",
                "RR-00F7FFAA06553D90B4AC is a strict-audit-valid Result for the same task/publication and remains the operational Result without ranking the two mathematical conclusions or claiming same-execution control replacement.",
                "The invalid immutable RR-B9234FB62194F252F751 record remains referenceable history; a future authorized unique-path re-freeze may replace this quarantine through the ordinary Result contract.",
            ],
            "working_truth_granted": False,
            "foundation_authority_granted": False,
            "canonical_promotion_granted": False,
            "successor_triggered": False,
        },
        "result_id",
    )
    write_json(RESULT_QUARANTINE, payload)


def materialize_review_quarantines() -> None:
    payload = json.loads(REVIEW_QUARANTINE.read_text(encoding="utf-8"))
    require(
        payload.get("schema") == "ENTERPRISE_MATH_RESULT_REVIEW_AUDIT_QUARANTINE_V1"
        and payload.get("status") == "ACTIVE",
        "unexpected review quarantine schema/status",
    )
    rows = payload.get("entries")
    require(isinstance(rows, list), "review quarantine entries must be a list")

    common = {
        "state": "INVALID_IMMUTABLE_REVIEW_RECORD",
        "operational": False,
        "history_preserved": True,
        "allowed_review_audit_errors": [
            "result record digest drift",
            "review artifact digest drift",
        ],
        "reason": "Exact immutable review bytes fail the current V1 secondary-digest audit while the primary review/result Git blobs remain exactly pinned. CONTROL_PLANE_MAINTENANCE preserves the Driver review as nonoperational history and removes only its review/follow-up authority; it does not infer, repair or rewrite the Driver disposition.",
        "working_truth_granted": False,
        "foundation_authority_granted": False,
        "canonical_promotion_granted": False,
        "successor_triggered": False,
    }
    additions = [
        {
            "review_id": "DR-C20A9201B684ECE69AF8",
            "result_id": "RR-14766C42C430C5DD36C4",
            "task_id": "RS-P000-PHILOSOPHY-FIRST-FORWARD-XOR-ALL-N-INDEPENDENCE",
            "review_record_path": "research_result_reviews/RR-14766C42C430C5DD36C4/DR-C20A9201B684ECE69AF8.json",
            "review_record_blob_sha1": "sha1:5188b4d3500fc1551481c443f9a57590b3b53787",
            "result_record_path": "research_result_records/RS-P000-PHILOSOPHY-FIRST-FORWARD-XOR-ALL-N-INDEPENDENCE/RR-14766C42C430C5DD36C4.json",
            "result_record_blob_sha1": "sha1:2c92407333afcc2b137b4a79ca601c0e16d1e825",
            **common,
        },
        {
            "review_id": "DR-19B757A8E5D817B5E495",
            "result_id": "RR-1DE3F3213271AED2625C",
            "task_id": "RS-P000-PHILOSOPHY-FIRST-NATIVE-MODEL-CHANGE-ARROW-AUDIT",
            "review_record_path": "research_result_reviews/RR-1DE3F3213271AED2625C/DR-19B757A8E5D817B5E495.json",
            "review_record_blob_sha1": "sha1:688fe7ac4c6714fe558e80785333e14861cbfca6",
            "result_record_path": "research_result_records/RS-P000-PHILOSOPHY-FIRST-NATIVE-MODEL-CHANGE-ARROW-AUDIT/RR-1DE3F3213271AED2625C.json",
            "result_record_blob_sha1": "sha1:10debd66fe28265a45203a42723603428e21ccbc",
            **common,
        },
        {
            "review_id": "DR-B66959082DC75F6225C0",
            "result_id": "RR-8A1951FD6A09D5D232CD",
            "task_id": "RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-ITERATED-REFINEMENT-FRONTIER",
            "review_record_path": "research_result_reviews/RR-8A1951FD6A09D5D232CD/DR-B66959082DC75F6225C0.json",
            "review_record_blob_sha1": "sha1:e331a6e5a8c715b55ef878a8cfbfbb15ba74a580",
            "result_record_path": "research_result_records/RS-P000-PHILOSOPHY-FIRST-RETURN-PROFILE-ITERATED-REFINEMENT-FRONTIER/RR-8A1951FD6A09D5D232CD.json",
            "result_record_blob_sha1": "sha1:ccbfce4198c31a743813965a06b7bd65ba757099",
            **common,
        },
        {
            "review_id": "DR-007256B8119682DF8EFA",
            "result_id": "RR-0A26702D3A361799ADE0",
            "task_id": "RS-GEO6-OBJECTIVE-SEMANTIC-SELECTOR-SYNTHESIS",
            "review_record_path": "research_result_reviews/RR-0A26702D3A361799ADE0/DR-007256B8119682DF8EFA.json",
            "review_record_blob_sha1": "sha1:1bf79b7b03a400a9bd6910540eefdb39b9af6db5",
            "result_record_path": "research_result_records/RS-GEO6-OBJECTIVE-SEMANTIC-SELECTOR-SYNTHESIS/RR-0A26702D3A361799ADE0.json",
            "result_record_blob_sha1": "sha1:2774c81c9c170828de935b34e5ad4f718194fcf4",
            **common,
        },
    ]
    for row in additions:
        append_unique(rows, row, "review_id")
    write_json(REVIEW_QUARANTINE, payload)


def materialize_driver_authority_alias() -> None:
    payload = json.loads(DRIVER_COMPAT.read_text(encoding="utf-8"))
    require(
        payload.get("schema") == "ENTERPRISE_MATH_DRIVER_AUTHORITY_COMPATIBILITY_V1"
        and payload.get("status") == "ACTIVE",
        "unexpected Driver authority compatibility schema/status",
    )
    rows = payload.get("id_aliases")
    require(isinstance(rows, list), "Driver authority id_aliases must be a list")
    append_unique(
        rows,
        {
            "record_path": "research_driver_authority_records/EM-DVR-WLE3X6/DA-E6099309952F17671DEC.json",
            "record_blob_sha1": "sha1:645d19460bf3c70739b108cf97d060cf345cd89c",
            "raw_authority_record_id": "DA-E6099309952F17671DEC",
            "normalized_authority_record_id": "DA-C31E3425800272BAEC24",
        },
        "record_path",
    )
    write_json(DRIVER_COMPAT, payload)


def main() -> int:
    materialize_result_compatibility()
    materialize_result_quarantine()
    materialize_review_quarantines()
    materialize_driver_authority_alias()
    print(
        "MATERIALIZED exact Q24 enum compatibility, one invalid Result quarantine, "
        "four invalid-review quarantines, and one Driver authority ID alias"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
