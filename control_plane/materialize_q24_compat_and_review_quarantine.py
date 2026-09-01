#!/usr/bin/env python3
"""One-shot branch materializer for exact immutable Q22-Q24 control metadata.

This script is deleted in the same commit that materializes its output. It does
not rewrite Result or Driver-review records. It only appends exact Git-blob-pinned
compatibility/quarantine rows to existing control registries.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMPAT = ROOT / "research_result_record_compatibility.json"
REVIEW_Q = ROOT / "research_result_review_audit_quarantines.json"


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


def main() -> int:
    compat = json.loads(COMPAT.read_text(encoding="utf-8"))
    require(
        compat.get("schema") == "ENTERPRISE_MATH_RESEARCH_RESULT_COMPATIBILITY_V1"
        and compat.get("status") == "ACTIVE",
        "unexpected compatibility registry schema/status",
    )
    result_rows = compat.get("result_normalizations")
    require(isinstance(result_rows, list), "result_normalizations must be a list")
    append_unique(
        result_rows,
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
    COMPAT.write_text(
        json.dumps(compat, ensure_ascii=False, separators=(",", ":")) + "\n",
        encoding="utf-8",
    )

    review_q = json.loads(REVIEW_Q.read_text(encoding="utf-8"))
    require(
        review_q.get("schema") == "ENTERPRISE_MATH_RESULT_REVIEW_AUDIT_QUARANTINE_V1"
        and review_q.get("status") == "ACTIVE",
        "unexpected review quarantine schema/status",
    )
    review_rows = review_q.get("entries")
    require(isinstance(review_rows, list), "review quarantine entries must be a list")

    common = {
        "state": "INVALID_IMMUTABLE_REVIEW_RECORD",
        "operational": False,
        "history_preserved": True,
        "allowed_review_audit_errors": [
            "result record digest drift",
            "review artifact digest drift",
        ],
        "reason": "Exact immutable Q22-Q24 review bytes fail the current V1 secondary-digest audit while their primary review/result Git blobs remain exactly pinned. CONTROL_PLANE_MAINTENANCE preserves each Driver review as nonoperational history and removes only its review/follow-up authority; it does not infer, repair or rewrite the Driver disposition.",
        "working_truth_granted": False,
        "foundation_authority_granted": False,
        "canonical_promotion_granted": False,
        "successor_triggered": False,
    }
    rows = [
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
    ]
    for row in rows:
        append_unique(review_rows, row, "review_id")
    REVIEW_Q.write_text(
        json.dumps(review_q, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    print(
        "MATERIALIZED Q24 result enum compatibility and three exact invalid-review quarantines"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
