#!/usr/bin/env python3
"""Pre-write validation for immutable result and review candidates.

These helpers mirror the candidate-local checks in the canonical result/review
audit but run before the record exists on disk.  They do not decide terminal
verdicts or Driver dispositions; they only verify that the supplied values and
digest bindings are structurally admissible under the existing enums and linked
execution/result records.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from control_plane import research_result_records_impl as impl

ROOT = impl.ROOT


class ImmutableCandidateValidationError(ValueError):
    pass


def _result_prefix(record: dict[str, Any]) -> str:
    return str(record.get("result_id") or "<candidate-result>")


def _review_prefix(record: dict[str, Any]) -> str:
    return str(record.get("review_id") or "<candidate-review>")


def validate_result_candidate(
    record: dict[str, Any],
    *,
    root: Path = ROOT,
) -> list[str]:
    errors: list[str] = []
    prefix = _result_prefix(record)
    try:
        executions = impl.execution_map(root)
        existing = impl.result_map(root)
    except Exception as exc:
        return [str(exc)]

    rid = record.get("result_id")
    if not isinstance(rid, str) or not rid:
        errors.append(f"{prefix}: missing result_id")
    elif rid in existing:
        errors.append(f"{prefix}: duplicate result_id")
    if record.get("record_schema") != impl.RESULT_SCHEMA:
        errors.append(f"{prefix}: wrong result schema")

    execution = executions.get(str(record.get("execution_record_id", "")))
    if execution is None:
        errors.append(f"{prefix}: unknown execution record")
        return errors
    for field in (
        "task_id",
        "publication_id",
        "claim_id",
        "researcher_id",
        "taskbook_blob_sha1",
        "execution_branch",
    ):
        if record.get(field) != execution.get(field):
            errors.append(f"{prefix}: execution-linked field mismatch: {field}")

    execution_has_lane = (
        execution.get("execution_cohort_id") is not None
        or execution.get("execution_lane_id") is not None
    )
    result_has_lane = (
        record.get("execution_cohort_id") is not None
        or record.get("execution_lane_id") is not None
    )
    if execution_has_lane != result_has_lane:
        errors.append(f"{prefix}: lane identity presence differs from execution record")
    if execution_has_lane:
        for field in ("execution_cohort_id", "execution_lane_id", "lane_output_prefix"):
            if record.get(field) != execution.get(field):
                errors.append(f"{prefix}: execution-linked lane field mismatch: {field}")

    path_value = record.get("return_path")
    if not isinstance(path_value, str) or not (root / path_value).exists():
        errors.append(f"{prefix}: return artifact missing")
    else:
        path = root / path_value
        if not impl._same_git_blob_identity(impl._blob(path), record.get("return_blob_sha1")):
            errors.append(f"{prefix}: return artifact blob drift")
        if impl._sha256(path) != record.get("return_sha256"):
            errors.append(f"{prefix}: return artifact SHA-256 drift")

    if record.get("terminal_verdict") not in impl.TERMINAL_VERDICTS:
        errors.append(f"{prefix}: invalid terminal_verdict")
    if record.get("method_harvest") not in impl.METHOD_HARVEST:
        errors.append(f"{prefix}: invalid method_harvest")
    if record.get("independence_status") not in impl.INDEPENDENCE_STATUS:
        errors.append(f"{prefix}: invalid independence_status")
    if record.get("source_exposure_status") not in impl.SOURCE_EXPOSURE_STATUS:
        errors.append(f"{prefix}: invalid source_exposure_status")
    if not isinstance(record.get("hard_target_disposition"), str) or not record["hard_target_disposition"].strip():
        errors.append(f"{prefix}: hard_target_disposition missing")
    if not isinstance(record.get("unresolved_residue"), str) or not record["unresolved_residue"].strip():
        errors.append(f"{prefix}: unresolved_residue missing")
    if not isinstance(record.get("next_control_plane_recommendation"), str) or not record["next_control_plane_recommendation"].strip():
        errors.append(f"{prefix}: next_control_plane_recommendation missing")

    manifest = record.get("output_manifest")
    if not isinstance(manifest, list) or not manifest:
        errors.append(f"{prefix}: output_manifest missing")
    else:
        for output in manifest:
            if not isinstance(output, dict) or not isinstance(output.get("path"), str):
                errors.append(f"{prefix}: invalid output manifest row")
                continue
            path = root / output["path"]
            if not path.exists():
                errors.append(f"{prefix}: output missing: {output['path']}")
            elif (
                not impl._same_git_blob_identity(impl._blob(path), output.get("git_blob_sha1"))
                or impl._sha256(path) != output.get("sha256")
            ):
                errors.append(f"{prefix}: output digest drift: {output['path']}")
    return errors


def validate_review_candidate(
    record: dict[str, Any],
    *,
    root: Path = ROOT,
) -> list[str]:
    errors: list[str] = []
    prefix = _review_prefix(record)
    try:
        results = impl.result_map(root)
        existing_reviews = impl.iter_reviews(root)
    except Exception as exc:
        return [str(exc)]

    rev_id = record.get("review_id")
    if not isinstance(rev_id, str) or not rev_id:
        errors.append(f"{prefix}: missing review_id")
    elif rev_id in {
        item.get("review_id") for item in existing_reviews if isinstance(item, dict)
    }:
        errors.append(f"{prefix}: duplicate review_id")
    if record.get("record_schema") != impl.REVIEW_SCHEMA:
        errors.append(f"{prefix}: wrong review schema")

    rid = record.get("result_id")
    result = results.get(str(rid))
    if result is None:
        errors.append(f"{prefix}: unknown result")
        return errors
    for field in ("task_id", "publication_id", "execution_record_id"):
        if record.get(field) != result.get(field):
            errors.append(f"{prefix}: result-linked field mismatch: {field}")

    result_has_lane = (
        result.get("execution_cohort_id") is not None
        or result.get("execution_lane_id") is not None
    )
    review_has_lane = (
        record.get("execution_cohort_id") is not None
        or record.get("execution_lane_id") is not None
    )
    if result_has_lane != review_has_lane:
        errors.append(f"{prefix}: lane identity presence differs from result record")
    if result_has_lane:
        for field in impl.LANE_FIELDS:
            if record.get(field) != result.get(field):
                errors.append(f"{prefix}: result-linked lane field mismatch: {field}")

    result_record_path = record.get("result_record_path")
    if not isinstance(result_record_path, str) or not (root / result_record_path).exists():
        errors.append(f"{prefix}: result record pin missing")
    elif impl._sha256(root / result_record_path) != record.get("result_record_sha256"):
        errors.append(f"{prefix}: result record digest drift")

    review_path = record.get("review_path")
    if not isinstance(review_path, str) or not (root / review_path).exists():
        errors.append(f"{prefix}: review artifact missing")
    else:
        path = root / review_path
        if (
            not impl._same_git_blob_identity(impl._blob(path), record.get("review_blob_sha1"))
            or impl._sha256(path) != record.get("review_sha256")
        ):
            errors.append(f"{prefix}: review artifact digest drift")

    if record.get("disposition") not in impl.ALL_DISPOSITIONS:
        errors.append(f"{prefix}: invalid disposition")
    if record.get("destination_class") not in impl.DESTINATION_CLASSES:
        errors.append(f"{prefix}: invalid destination_class")
    if record.get("terminal") is not (
        record.get("disposition") in impl.TERMINAL_DISPOSITIONS
    ):
        errors.append(f"{prefix}: terminal flag mismatch")
    return errors


def require_valid_result_candidate(record: dict[str, Any], *, root: Path = ROOT) -> None:
    errors = validate_result_candidate(record, root=root)
    if errors:
        raise ImmutableCandidateValidationError("; ".join(errors))


def require_valid_review_candidate(record: dict[str, Any], *, root: Path = ROOT) -> None:
    errors = validate_review_candidate(record, root=root)
    if errors:
        raise ImmutableCandidateValidationError("; ".join(errors))
