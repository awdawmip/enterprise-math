#!/usr/bin/env python3
"""Immutable execution-linked research-result and Driver-review records."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from tools import research_execution_records
    from tools import research_identity
    from tools import research_task_records
    import research_execution_cohorts
except ModuleNotFoundError:
    import research_execution_records  # type: ignore
    import research_identity  # type: ignore
    import research_task_records  # type: ignore
    import research_execution_cohorts  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
RESULT_ROOT = ROOT / "research_result_records"
REVIEW_ROOT = ROOT / "research_result_reviews"
RESULT_SCHEMA = "ENTERPRISE_MATH_RESEARCH_RESULT_RECORD_V1"
REVIEW_SCHEMA = "ENTERPRISE_MATH_RESEARCH_RESULT_REVIEW_V1"
TERMINAL_DISPOSITIONS = {"ACCEPTED", "REJECTED", "PARKED", "CLOSED", "SUPERSEDED"}
NONTERMINAL_DISPOSITIONS = {"RETURN_TO_OWNER", "REQUEST_REPLICATION", "REQUEST_REVISION"}
ALL_DISPOSITIONS = TERMINAL_DISPOSITIONS | NONTERMINAL_DISPOSITIONS
TERMINAL_VERDICTS = {
    "SUCCESS", "PASS", "KILL", "REFUTED", "NO_GO", "BLOCKED",
    "NEGATIVE_BOUNDARY", "FORMALIZED", "INTEGRATED", "AUDIT_COMPLETE",
}
METHOD_HARVEST = {
    "GLOBAL_TOOL_FAMILY", "GLOBAL_SUBTOOL", "DOMAIN_FACADE", "DOMAIN_OPERATOR",
    "RESULT_ONLY", "CANDIDATE_NOT_TOOL", "DUPLICATE_ALIAS", "NO_TOOL_PAYLOAD",
}
INDEPENDENCE_STATUS = {
    "CLEAN_INDEPENDENT_CONTEXT", "SHARED_AMBIENT_CONTEXT_DISCLOSED",
    "NOT_INDEPENDENT", "NOT_APPLICABLE",
}
SOURCE_EXPOSURE_STATUS = {
    "BLIND_RAW_FROZEN", "SOURCE_EXPOSED_AFTER_RAW_FREEZE",
    "NONBLIND_DISCLOSED", "NOT_APPLICABLE",
}
DESTINATION_CLASSES = {"NONE", "FOUNDATION", "TOOL", "L4", "REPLICATION", "FOLLOWUP_TASK", "ARCHIVE"}
LANE_FIELDS = ("execution_cohort_id", "execution_lane_id")


class ResultRecordError(ValueError):
    pass


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _save_exclusive(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
    try:
        with path.open("x", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError as exc:
        raise ResultRecordError(f"immutable record already exists: {path}") from exc


def _parse_time(value: str) -> datetime:
    dt = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _now(value: str | None) -> str:
    return (_parse_time(value) if value else datetime.now(timezone.utc)).isoformat()


def _blob(path: Path) -> str:
    return research_task_records.git_blob_sha1_bytes(path.read_bytes())


def _normalize_git_blob_identity(value: Any) -> str | None:
    """Normalize historical bare and current ``sha1:`` Git blob identities.

    Stored result/review records are immutable evidence. Early V1 records used a
    bare 40-hex Git blob SHA-1 while current writers prefix the same identity with
    ``sha1:``. Audit compatibility therefore normalizes only for comparison and
    never rewrites historical record bytes.
    """
    if not isinstance(value, str):
        return None
    text = value.strip().lower()
    if text.startswith("sha1:"):
        text = text[5:]
    return text if re.fullmatch(r"[0-9a-f]{40}", text) else None


def _same_git_blob_identity(left: Any, right: Any) -> bool:
    lhs = _normalize_git_blob_identity(left)
    rhs = _normalize_git_blob_identity(right)
    return lhs is not None and rhs is not None and lhs == rhs


def _sha256(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _safe_id(value: str, label: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9._-]+", value):
        raise ResultRecordError(f"{label} contains unsupported characters")
    return value


def _relative(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError as exc:
        raise ResultRecordError(f"output path must be inside repository root: {path}") from exc


def _allowed_output(rel: str, allowed: list[str]) -> bool:
    for raw in allowed:
        rule = raw.strip().replace("\\", "/")
        if rule.endswith("*") and rel.startswith(rule[:-1]):
            return True
        if rule.endswith("/") and rel.startswith(rule):
            return True
        if rel == rule:
            return True
    return False


def execution_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for item in research_execution_records.iter_records(root):
        erid = item.get("execution_record_id")
        if isinstance(erid, str) and erid:
            if erid in out:
                raise ResultRecordError(f"duplicate execution_record_id: {erid}")
            out[erid] = item
    return out


def result_id(task_id: str, execution_record_id: str, return_blob: str, owner_head: str) -> str:
    raw = "\0".join((task_id, execution_record_id, return_blob, owner_head)).encode("utf-8")
    return "RR-" + hashlib.sha256(raw).hexdigest()[:20].upper()


def review_id(result_id_value: str, driver_id: str, review_blob: str, disposition: str) -> str:
    raw = "\0".join((result_id_value, driver_id, review_blob, disposition)).encode("utf-8")
    return "DR-" + hashlib.sha256(raw).hexdigest()[:20].upper()


def iter_results(root: Path = ROOT) -> list[dict[str, Any]]:
    directory = root / "research_result_records"
    if not directory.exists():
        return []
    out = []
    for path in sorted(directory.glob("*/*.json")):
        item = _load_json(path)
        item["_record_path"] = path.relative_to(root).as_posix()
        out.append(item)
    return out


def iter_reviews(root: Path = ROOT) -> list[dict[str, Any]]:
    directory = root / "research_result_reviews"
    if not directory.exists():
        return []
    out = []
    for path in sorted(directory.glob("*/*.json")):
        item = _load_json(path)
        item["_review_path"] = path.relative_to(root).as_posix()
        out.append(item)
    return out


def result_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for item in iter_results(root):
        rid = item.get("result_id")
        if not isinstance(rid, str) or not rid:
            raise ResultRecordError("result record missing result_id")
        if rid in out:
            raise ResultRecordError(f"duplicate result_id: {rid}")
        out[rid] = item
    return out


def latest_review(result_id_value: str, root: Path = ROOT) -> dict[str, Any] | None:
    values = [item for item in iter_reviews(root) if item.get("result_id") == result_id_value]
    if not values:
        return None
    values.sort(key=lambda item: (item.get("reviewed_at", ""), item.get("review_id", "")))
    return values[-1]


def task_result_state(
    task_id: str,
    root: Path = ROOT,
    publication_id: str | None = None,
) -> dict[str, Any] | None:
    """Return result state for one publication generation.

    By default registered tasks resolve their current immutable publication and
    ignore historical-generation results. Callers may pass an explicit historical
    ``publication_id`` for provenance queries. Legacy/test tasks without an
    immutable current publication retain the historical task-id-only behavior.
    """
    if publication_id is None:
        try:
            current = research_task_records.current_records(root).get(task_id)
        except Exception:
            current = None
        if isinstance(current, dict) and isinstance(current.get("publication_id"), str):
            publication_id = current["publication_id"]
    values = [
        item
        for item in iter_results(root)
        if item.get("task_id") == task_id
        and (publication_id is None or item.get("publication_id") == publication_id)
    ]
    if not values:
        return None
    values.sort(key=lambda item: (item.get("frozen_at", ""), item.get("result_id", "")))
    result = values[-1]
    review = latest_review(result["result_id"], root)
    if review is None:
        return {"state": "AWAITING_DRIVER_REVIEW", "result": result, "review": None, "terminal": False}
    disposition = review.get("disposition")
    return {
        "state": "TERMINAL" if disposition in TERMINAL_DISPOSITIONS else "RETURN_TO_EXECUTION",
        "result": result,
        "review": review,
        "terminal": disposition in TERMINAL_DISPOSITIONS,
    }


def build_output_manifest(paths: list[Path], execution: dict[str, Any], root: Path) -> list[dict[str, str]]:
    allowed = execution.get("allowed_outputs")
    if not isinstance(allowed, list) or not allowed:
        raise ResultRecordError("execution record has no allowed output scope")
    manifest: list[dict[str, str]] = []
    seen: set[str] = set()
    for path in paths:
        if not path.exists() or not path.is_file():
            raise ResultRecordError(f"output artifact does not exist: {path}")
        rel = _relative(path, root)
        if rel in seen:
            raise ResultRecordError(f"duplicate output artifact: {rel}")
        seen.add(rel)
        if not _allowed_output(rel, allowed):
            raise ResultRecordError(f"output artifact is outside execution authorization: {rel}")
        manifest.append({"path": rel, "git_blob_sha1": _blob(path), "sha256": _sha256(path)})
    if not manifest:
        raise ResultRecordError("at least one output artifact is required")
    return manifest


def _validate_execution_publication_for_freeze(execution: dict[str, Any], root: Path) -> None:
    task_id = execution["task_id"]
    cohort_id = execution.get("execution_cohort_id")
    lane_id = execution.get("execution_lane_id")
    if (cohort_id is None) != (lane_id is None):
        raise ResultRecordError("execution cohort/lane identity is incomplete")
    if cohort_id is None:
        current = research_task_records.current_records(root).get(task_id)
        if current is None or current.get("publication_id") != execution.get("publication_id"):
            raise ResultRecordError("execution record is not bound to the current operational task publication")
        return
    cohort = research_execution_cohorts.cohort_map(root).get(str(cohort_id))
    if cohort is None or cohort.get("task_id") != task_id:
        raise ResultRecordError("execution record references unknown cohort for task")
    if cohort.get("record_state") != "ACTIVE":
        raise ResultRecordError("lane result cannot freeze after its execution cohort is no longer ACTIVE")
    lanes = [
        row for row in cohort.get("lanes", [])
        if isinstance(row, dict) and row.get("lane_id") == lane_id
    ]
    if len(lanes) != 1:
        raise ResultRecordError("execution record references unknown or ambiguous lane")
    if lanes[0].get("publication_id") != execution.get("publication_id"):
        raise ResultRecordError("execution publication differs from cohort lane publication pin")
    publications = research_execution_records.publication_map(root)
    record = publications.get(str(execution.get("publication_id")))
    if record is None or record.get("task_id") != task_id:
        raise ResultRecordError("lane execution publication generation is unavailable")


def freeze_result(
    *,
    execution_record_id: str,
    return_path: Path,
    output_paths: list[Path],
    owner_head: str,
    terminal_verdict: str,
    hard_target_disposition: str,
    unresolved_residue: str,
    method_harvest: str,
    independence_status: str,
    source_exposure_status: str,
    next_control_plane_recommendation: str,
    frozen_at: str,
    root: Path = ROOT,
) -> dict[str, Any]:
    execution = execution_map(root).get(execution_record_id)
    if execution is None:
        raise ResultRecordError("unknown execution_record_id")
    task_id = execution["task_id"]
    _validate_execution_publication_for_freeze(execution, root)
    if not re.fullmatch(r"[0-9a-fA-F]{40}", owner_head.strip()):
        raise ResultRecordError("owner_head must be a 40-hex frozen commit SHA")
    if terminal_verdict not in TERMINAL_VERDICTS:
        raise ResultRecordError("invalid terminal_verdict")
    if not hard_target_disposition.strip():
        raise ResultRecordError("hard_target_disposition is required")
    if not unresolved_residue.strip():
        raise ResultRecordError("unresolved_residue is required; use NONE when empty")
    if method_harvest not in METHOD_HARVEST:
        raise ResultRecordError("invalid method_harvest")
    if independence_status not in INDEPENDENCE_STATUS:
        raise ResultRecordError("invalid independence_status")
    if source_exposure_status not in SOURCE_EXPOSURE_STATUS:
        raise ResultRecordError("invalid source_exposure_status")
    if not next_control_plane_recommendation.strip():
        raise ResultRecordError("next_control_plane_recommendation is required")
    if not return_path.exists():
        raise ResultRecordError(f"return artifact does not exist: {return_path}")
    return_rel = _relative(return_path, root)
    all_paths = list(output_paths)
    if return_rel not in {_relative(path, root) for path in all_paths}:
        all_paths.append(return_path)
    manifest = build_output_manifest(all_paths, execution, root)
    return_blob = _blob(return_path)
    rid = result_id(task_id, execution_record_id, return_blob, owner_head.lower())
    value: dict[str, Any] = {
        "record_schema": RESULT_SCHEMA,
        "result_id": rid,
        "task_id": task_id,
        "publication_id": execution["publication_id"],
        "execution_record_id": execution_record_id,
        "claim_id": execution["claim_id"],
        "taskbook_path": execution["taskbook_path"],
        "taskbook_blob_sha1": execution["taskbook_blob_sha1"],
        "execution_branch": execution["execution_branch"],
        "execution_branch_base": execution["execution_branch_base"],
        "return_path": return_rel,
        "return_blob_sha1": return_blob,
        "return_sha256": _sha256(return_path),
        "owner_head": owner_head.lower(),
        "researcher_id": execution["researcher_id"],
        "frozen_at": frozen_at,
        "terminal_verdict": terminal_verdict,
        "hard_target_disposition": hard_target_disposition,
        "unresolved_residue": unresolved_residue,
        "output_manifest": manifest,
        "method_harvest": method_harvest,
        "independence_status": independence_status,
        "source_exposure_status": source_exposure_status,
        "next_control_plane_recommendation": next_control_plane_recommendation,
        "driver_review_required": True,
    }
    if execution.get("execution_cohort_id") is not None:
        value.update(
            {
                "execution_cohort_id": execution.get("execution_cohort_id"),
                "execution_lane_id": execution.get("execution_lane_id"),
                "lane_output_prefix": execution.get("lane_output_prefix"),
            }
        )
    return value


def review_result(
    *,
    result: dict[str, Any],
    driver_id: str,
    disposition: str,
    review_path: Path,
    destination_class: str,
    destination_ref_or_none: str,
    reviewed_at: str,
    root: Path = ROOT,
) -> dict[str, Any]:
    if not research_identity.valid_execution_id(driver_id):
        raise ResultRecordError("invalid driver_id")
    if disposition not in ALL_DISPOSITIONS:
        raise ResultRecordError("invalid disposition")
    if destination_class not in DESTINATION_CLASSES:
        raise ResultRecordError("invalid destination_class")
    if destination_class != "NONE" and not destination_ref_or_none.strip():
        raise ResultRecordError("non-NONE destination requires destination_ref_or_none")
    if not review_path.exists():
        raise ResultRecordError(f"Driver review artifact missing: {review_path}")
    result_record_path = result.get("_record_path")
    if not isinstance(result_record_path, str) or not (root / result_record_path).exists():
        raise ResultRecordError("result record path is unavailable for review pinning")
    review_blob = _blob(review_path)
    rid = review_id(result["result_id"], driver_id, review_blob, disposition)
    value: dict[str, Any] = {
        "record_schema": REVIEW_SCHEMA,
        "review_id": rid,
        "result_id": result["result_id"],
        "result_record_path": result_record_path,
        "result_record_sha256": _sha256(root / result_record_path),
        "task_id": result["task_id"],
        "publication_id": result["publication_id"],
        "execution_record_id": result["execution_record_id"],
        "driver_id": driver_id.strip().upper(),
        "review_path": _relative(review_path, root),
        "review_blob_sha1": review_blob,
        "review_sha256": _sha256(review_path),
        "reviewed_at": reviewed_at,
        "disposition": disposition,
        "destination_class": destination_class,
        "destination_ref_or_none": destination_ref_or_none,
        "terminal": disposition in TERMINAL_DISPOSITIONS,
    }
    if result.get("execution_cohort_id") is not None:
        value.update(
            {
                "execution_cohort_id": result.get("execution_cohort_id"),
                "execution_lane_id": result.get("execution_lane_id"),
            }
        )
    return value


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        executions = execution_map(root)
        results = result_map(root)
    except Exception as exc:
        return [str(exc)]
    seen_reviews: set[str] = set()
    for rid, item in results.items():
        prefix = item.get("_record_path", rid)
        if item.get("record_schema") != RESULT_SCHEMA:
            errors.append(f"{prefix}: wrong result schema")
        execution = executions.get(str(item.get("execution_record_id", "")))
        if execution is None:
            errors.append(f"{prefix}: unknown execution record")
            continue
        for field in ("task_id", "publication_id", "claim_id", "researcher_id", "taskbook_blob_sha1", "execution_branch"):
            if item.get(field) != execution.get(field):
                errors.append(f"{prefix}: execution-linked field mismatch: {field}")
        execution_has_lane = execution.get("execution_cohort_id") is not None or execution.get("execution_lane_id") is not None
        result_has_lane = item.get("execution_cohort_id") is not None or item.get("execution_lane_id") is not None
        if execution_has_lane != result_has_lane:
            errors.append(f"{prefix}: lane identity presence differs from execution record")
        if execution_has_lane:
            for field in ("execution_cohort_id", "execution_lane_id", "lane_output_prefix"):
                if item.get(field) != execution.get(field):
                    errors.append(f"{prefix}: execution-linked lane field mismatch: {field}")
        path_value = item.get("return_path")
        if not isinstance(path_value, str) or not (root / path_value).exists():
            errors.append(f"{prefix}: return artifact missing")
        else:
            if not _same_git_blob_identity(_blob(root / path_value), item.get("return_blob_sha1")):
                errors.append(f"{prefix}: return artifact blob drift")
            if _sha256(root / path_value) != item.get("return_sha256"):
                errors.append(f"{prefix}: return artifact SHA-256 drift")
        if item.get("terminal_verdict") not in TERMINAL_VERDICTS:
            errors.append(f"{prefix}: invalid terminal_verdict")
        if item.get("method_harvest") not in METHOD_HARVEST:
            errors.append(f"{prefix}: invalid method_harvest")
        if item.get("independence_status") not in INDEPENDENCE_STATUS:
            errors.append(f"{prefix}: invalid independence_status")
        if item.get("source_exposure_status") not in SOURCE_EXPOSURE_STATUS:
            errors.append(f"{prefix}: invalid source_exposure_status")
        if not isinstance(item.get("hard_target_disposition"), str) or not item["hard_target_disposition"].strip():
            errors.append(f"{prefix}: hard_target_disposition missing")
        if not isinstance(item.get("unresolved_residue"), str) or not item["unresolved_residue"].strip():
            errors.append(f"{prefix}: unresolved_residue missing")
        if not isinstance(item.get("next_control_plane_recommendation"), str) or not item["next_control_plane_recommendation"].strip():
            errors.append(f"{prefix}: next_control_plane_recommendation missing")
        manifest = item.get("output_manifest")
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
                else:
                    if (
                        not _same_git_blob_identity(_blob(path), output.get("git_blob_sha1"))
                        or _sha256(path) != output.get("sha256")
                    ):
                        errors.append(f"{prefix}: output digest drift: {output['path']}")
    for item in iter_reviews(root):
        prefix = item.get("_review_path", "<review>")
        rev_id = item.get("review_id")
        if not isinstance(rev_id, str) or not rev_id:
            errors.append(f"{prefix}: missing review_id")
        elif rev_id in seen_reviews:
            errors.append(f"{prefix}: duplicate review_id")
        seen_reviews.add(str(rev_id))
        if item.get("record_schema") != REVIEW_SCHEMA:
            errors.append(f"{prefix}: wrong review schema")
        rid = item.get("result_id")
        result = results.get(str(rid))
        if result is None:
            errors.append(f"{prefix}: unknown result")
            continue
        for field in ("task_id", "publication_id", "execution_record_id"):
            if item.get(field) != result.get(field):
                errors.append(f"{prefix}: result-linked field mismatch: {field}")
        result_has_lane = result.get("execution_cohort_id") is not None or result.get("execution_lane_id") is not None
        review_has_lane = item.get("execution_cohort_id") is not None or item.get("execution_lane_id") is not None
        if result_has_lane != review_has_lane:
            errors.append(f"{prefix}: lane identity presence differs from result record")
        if result_has_lane:
            for field in LANE_FIELDS:
                if item.get(field) != result.get(field):
                    errors.append(f"{prefix}: result-linked lane field mismatch: {field}")
        result_record_path = item.get("result_record_path")
        if not isinstance(result_record_path, str) or not (root / result_record_path).exists():
            errors.append(f"{prefix}: result record pin missing")
        elif _sha256(root / result_record_path) != item.get("result_record_sha256"):
            errors.append(f"{prefix}: result record digest drift")
        review_path = item.get("review_path")
        if not isinstance(review_path, str) or not (root / review_path).exists():
            errors.append(f"{prefix}: review artifact missing")
        else:
            if (
                not _same_git_blob_identity(_blob(root / review_path), item.get("review_blob_sha1"))
                or _sha256(root / review_path) != item.get("review_sha256")
            ):
                errors.append(f"{prefix}: review artifact digest drift")
        if item.get("disposition") not in ALL_DISPOSITIONS:
            errors.append(f"{prefix}: invalid disposition")
        if item.get("destination_class") not in DESTINATION_CLASSES:
            errors.append(f"{prefix}: invalid destination_class")
        if item.get("terminal") is not (item.get("disposition") in TERMINAL_DISPOSITIONS):
            errors.append(f"{prefix}: terminal flag mismatch")
    return errors


def command_freeze(args: argparse.Namespace) -> int:
    return_path = Path(args.return_path)
    if not return_path.is_absolute():
        return_path = ROOT / return_path
    values = json.loads(args.output_paths_json)
    if not isinstance(values, list):
        raise ResultRecordError("--output-paths-json must decode to an array")
    output_paths = []
    for value in values:
        if not isinstance(value, str):
            raise ResultRecordError("output paths must be strings")
        path = Path(value)
        output_paths.append(path if path.is_absolute() else ROOT / path)
    record = freeze_result(
        execution_record_id=args.execution_record_id,
        return_path=return_path,
        output_paths=output_paths,
        owner_head=args.owner_head,
        terminal_verdict=args.terminal_verdict,
        hard_target_disposition=args.hard_target_disposition,
        unresolved_residue=args.unresolved_residue,
        method_harvest=args.method_harvest,
        independence_status=args.independence_status,
        source_exposure_status=args.source_exposure_status,
        next_control_plane_recommendation=args.next_control_plane_recommendation,
        frozen_at=_now(args.frozen_at),
    )
    out = RESULT_ROOT / _safe_id(record["task_id"], "task_id") / f"{record['result_id']}.json"
    _save_exclusive(out, record)
    errors = audit()
    if errors:
        raise ResultRecordError("result record created but audit failed: " + "; ".join(errors))
    print(json.dumps({**record, "record_path": out.relative_to(ROOT).as_posix()}, ensure_ascii=False, indent=2))
    return 0


def command_review(args: argparse.Namespace) -> int:
    result = result_map().get(args.result_id)
    if result is None:
        raise ResultRecordError(f"unknown result_id: {args.result_id}")
    path = Path(args.review_path)
    if not path.is_absolute():
        path = ROOT / path
    record = review_result(
        result=result,
        driver_id=args.driver_id,
        disposition=args.disposition,
        review_path=path,
        destination_class=args.destination_class,
        destination_ref_or_none=args.destination_ref_or_none,
        reviewed_at=_now(args.reviewed_at),
    )
    out = REVIEW_ROOT / _safe_id(args.result_id, "result_id") / f"{record['review_id']}.json"
    _save_exclusive(out, record)
    errors = audit()
    if errors:
        raise ResultRecordError("review record created but audit failed: " + "; ".join(errors))
    print(json.dumps({**record, "record_path": out.relative_to(ROOT).as_posix()}, ensure_ascii=False, indent=2))
    return 0


def command_audit(args: argparse.Namespace) -> int:
    errors = audit()
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print(f"PASS: result/review records valid ({len(iter_results())} result(s), {len(iter_reviews())} review(s)).")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise Math immutable execution-linked result/review registry")
    sub = parser.add_subparsers(dest="command", required=True)
    freeze = sub.add_parser("freeze")
    freeze.add_argument("--execution-record-id", required=True)
    freeze.add_argument("--return-path", required=True)
    freeze.add_argument("--output-paths-json", required=True)
    freeze.add_argument("--owner-head", required=True)
    freeze.add_argument("--terminal-verdict", choices=sorted(TERMINAL_VERDICTS), required=True)
    freeze.add_argument("--hard-target-disposition", required=True)
    freeze.add_argument("--unresolved-residue", required=True)
    freeze.add_argument("--method-harvest", choices=sorted(METHOD_HARVEST), required=True)
    freeze.add_argument("--independence-status", choices=sorted(INDEPENDENCE_STATUS), required=True)
    freeze.add_argument("--source-exposure-status", choices=sorted(SOURCE_EXPOSURE_STATUS), required=True)
    freeze.add_argument("--next-control-plane-recommendation", required=True)
    freeze.add_argument("--frozen-at")
    freeze.set_defaults(func=command_freeze)
    review = sub.add_parser("review")
    review.add_argument("--result-id", required=True)
    review.add_argument("--driver-id", required=True)
    review.add_argument("--disposition", choices=sorted(ALL_DISPOSITIONS), required=True)
    review.add_argument("--review-path", required=True)
    review.add_argument("--destination-class", choices=sorted(DESTINATION_CLASSES), required=True)
    review.add_argument("--destination-ref-or-none", default="")
    review.add_argument("--reviewed-at")
    review.set_defaults(func=command_review)
    audit_parser = sub.add_parser("audit")
    audit_parser.set_defaults(func=command_audit)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ResultRecordError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
