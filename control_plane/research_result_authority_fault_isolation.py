#!/usr/bin/env python3
"""Withhold control authority from exact invalid frozen Results, retaining evidence.

This registry does not correct Results, interpret Driver dispositions, resolve
replacement edges, or grant an execution identity. Its raw audit error set and
bound historical execution diagnostics are deliberately separate.
"""
from __future__ import annotations

import hashlib
import json
from contextlib import contextmanager
from contextvars import ContextVar
from pathlib import Path, PurePosixPath
from typing import Any, Iterator

ROOT = Path(__file__).resolve().parents[1]
QUARANTINE_FILE = "research_result_authority_quarantines.json"
SCHEMA = "ENTERPRISE_MATH_RESULT_CONTROL_AUTHORITY_QUARANTINE_V1"
BASIS = "EXACT_INVALID_FROZEN_RESULT_CONTROL_AUTHORITY_WITHHELD"
STATE = "RESULT_CONTROL_AUTHORITY_WITHHELD"
LEGACY_BASIS = "BOUND_FROZEN_RESULT_EXACT_LEGACY_RECORD"
_ACTIVE: ContextVar[tuple[Path, dict[str, dict[str, Any]]] | None] = ContextVar(
    "exact_result_authority_snapshot", default=None,
)


class ResultAuthorityIsolationError(ValueError):
    pass


def _fail(message: str) -> None:
    raise ResultAuthorityIsolationError(f"{QUARANTINE_FILE}: {message}")


def _path(root: Path, relative: Any) -> Path:
    if not isinstance(relative, str) or not relative or "\\" in relative or ":" in relative:
        _fail("noncanonical repository-local path")
    value = PurePosixPath(relative)
    if value.is_absolute() or value.as_posix() != relative or any(x in {".", ".."} for x in value.parts):
        _fail(f"noncanonical repository-local path: {relative}")
    target = root / relative
    if not target.resolve().is_relative_to(root.resolve()):
        _fail(f"path escapes repository: {relative}")
    return target


def _object(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        _fail(f"JSON root must be object: {path}")
    return value


def _digests(data: bytes) -> tuple[str, str]:
    return (
        "sha1:" + hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest(),
        "sha256:" + hashlib.sha256(data).hexdigest(),
    )


def _strings(value: Any, label: str, *, empty: bool = False) -> list[str]:
    if (not isinstance(value, list) or (not empty and not value)
            or any(not isinstance(x, str) or not x for x in value)
            or len(value) != len(set(value))):
        _fail(f"{label}: invalid exact string set")
    return value


def quarantine_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    path = root / QUARANTINE_FILE
    if not path.exists():
        return {}
    payload = _object(path)
    if payload.get("schema") != SCHEMA or payload.get("status") != "ACTIVE":
        _fail("wrong schema/status")
    entries = payload.get("entries")
    if not isinstance(entries, list):
        _fail("entries must be list")
    rows = {}
    for row in entries:
        if not isinstance(row, dict):
            _fail("entry must be object")
        rid = row.get("result_id")
        if not isinstance(rid, str) or not rid or rid in rows:
            _fail(f"invalid/duplicate result_id: {rid!r}")
        for field in ("task_id", "publication_id", "record_path", "record_blob_sha1",
                      "publication_record_path", "publication_record_blob_sha1",
                      "execution_record_id", "execution_record_path", "execution_record_blob_sha1", "reason"):
            if not isinstance(row.get(field), str) or not row[field].strip():
                _fail(f"{rid}: missing {field}")
        if (row.get("basis") != BASIS or row.get("state") != STATE
                or row.get("operational") is not False or row.get("history_preserved") is not True):
            _fail(f"{rid}: wrong control isolation basis/state")
        for flag in ("terminality_granted", "working_truth_granted", "foundation_authority_granted",
                     "canonical_promotion_granted", "successor_triggered"):
            if row.get(flag) is not False:
                _fail(f"{rid}: cannot grant {flag}")
        _strings(row.get("allowed_result_audit_errors"), f"{rid}: raw errors")
        _strings(row.get("bound_legacy_diagnostic_errors"), f"{rid}: legacy diagnostics", empty=True)
        if row.get("execution_identity_basis") not in {"CANONICAL_EXECUTION_RECORD_ID", LEGACY_BASIS}:
            _fail(f"{rid}: invalid execution identity basis")
        if not isinstance(row.get("dependency_pins"), list) or not row["dependency_pins"]:
            _fail(f"{rid}: dependency pins required")
        if not isinstance(row.get("derived_reviews"), list):
            _fail(f"{rid}: derived review set required")
        rows[rid] = row
    return rows


def _validated_rows(root: Path) -> dict[str, dict[str, Any]]:
    from control_plane import research_result_records_impl as impl

    rows = quarantine_rows(root)
    if not rows:
        return rows
    # This is the existing canonical map: no record_id alias is introduced.
    executions = impl.execution_map(root)
    result_sources = {rid: [] for rid in rows}
    for path in sorted((root / "research_result_records").glob("*/*.json")):
        result = _object(path)
        rid = result.get("result_id")
        if rid in rows:
            result_sources[rid].append(path.relative_to(root).as_posix())
    raw_reviews = []
    for path in sorted((root / "research_result_reviews").glob("*/*.json")):
        review = _object(path)
        if review.get("result_id") in rows:
            raw_reviews.append((path.relative_to(root).as_posix(), review))
    legacy_rows = None
    for rid, row in rows.items():
        if result_sources[rid] != [row["record_path"]]:
            _fail(f"{rid}: complete raw Result source path set drift")
        task, pub, eid = row["task_id"], row["publication_id"], row["execution_record_id"]
        for field, expected in (
            ("record_path", f"research_result_records/{task}/{rid}.json"),
            ("publication_record_path", f"research_task_records/{task}/{pub}.json"),
            ("execution_record_path", f"research_execution_records/{task}/{eid}.json"),
        ):
            if row[field] != expected:
                _fail(f"{rid}: {field} identity mismatch")
        pins = {}
        for pin in row["dependency_pins"]:
            if not isinstance(pin, dict):
                _fail(f"{rid}: dependency pin must be object")
            relative = pin.get("path")
            path = _path(root, relative)
            if relative in pins or not path.is_file():
                _fail(f"{rid}: duplicate/missing dependency: {relative}")
            if _digests(path.read_bytes()) != (pin.get("git_blob_sha1"), pin.get("sha256")):
                _fail(f"{rid}: exact dependency byte drift: {relative}")
            pins[relative] = pin
        for field, blob_field in (("record_path", "record_blob_sha1"),
                                 ("publication_record_path", "publication_record_blob_sha1"),
                                 ("execution_record_path", "execution_record_blob_sha1")):
            if pins.get(row[field], {}).get("git_blob_sha1") != row[blob_field]:
                _fail(f"{rid}: primary pin differs from dependency pin: {field}")
        result = _object(_path(root, row["record_path"]))
        publication = _object(_path(root, row["publication_record_path"]))
        execution = _object(_path(root, row["execution_record_path"]))
        if any(result.get(k) != row[k] for k in ("result_id", "task_id", "publication_id", "execution_record_id")):
            _fail(f"{rid}: raw Result identity mismatch")
        if publication.get("task_id") != task or publication.get("publication_id") != pub:
            _fail(f"{rid}: publication identity mismatch")
        if any(execution.get(k) != result.get(k) for k in ("task_id", "publication_id", "claim_id", "researcher_id", "execution_branch", "execution_branch_base")):
            _fail(f"{rid}: pinned execution relation mismatch")
        if not isinstance(result.get("frozen_at"), str) or not result["frozen_at"].strip():
            _fail(f"{rid}: Result is not frozen")
        required = {row["record_path"], row["publication_record_path"], row["execution_record_path"],
                    result.get("return_path"), result.get("taskbook_path"), publication.get("taskbook_path")}
        if execution.get("taskbook_path"):
            required.add(execution["taskbook_path"])
        manifest = result.get("output_manifest")
        if not isinstance(manifest, list) or any(not isinstance(x, dict) or not isinstance(x.get("path"), str) for x in manifest):
            _fail(f"{rid}: exact manifest invalid")
        required.update(x["path"] for x in manifest)
        expected_reviews = {}
        for review_row in row["derived_reviews"]:
            if not isinstance(review_row, dict):
                _fail(f"{rid}: review pin must be object")
            review_id = review_row.get("review_id")
            if not isinstance(review_id, str) or not review_id or review_id in expected_reviews:
                _fail(f"{rid}: invalid/duplicate derived review")
            review_path = f"research_result_reviews/{rid}/{review_id}.json"
            if review_row.get("result_id") != rid or review_row.get("review_record_path") != review_path:
                _fail(f"{rid}: derived review path/identity mismatch")
            if pins.get(review_path, {}).get("git_blob_sha1") != review_row.get("review_record_blob_sha1"):
                _fail(f"{rid}: derived review blob mismatch")
            review = _object(_path(root, review_path))
            if any(review.get(k) != v for k, v in {"review_id": review_id, "result_id": rid, "task_id": task, "publication_id": pub, "execution_record_id": eid}.items()):
                _fail(f"{rid}: derived review linked identity mismatch")
            if review.get("review_path") != review_row.get("review_artifact_path"):
                _fail(f"{rid}: review artifact path mismatch")
            required.update([review_path, review_row["review_artifact_path"]])
            expected_reviews[review_id] = review_path
        actual = [(v.get("review_id"), p) for p, v in raw_reviews if v.get("result_id") == rid]
        if len(actual) != len(expected_reviews) or dict(actual) != expected_reviews:
            _fail(f"{rid}: complete derived review source set drift")
        if set(pins) != required:
            _fail(f"{rid}: dependency set incomplete or stale")
        result["_record_path"] = row["record_path"]
        prefix = row["record_path"] + ": "
        canonical = executions.get(eid)
        if row["execution_identity_basis"] == LEGACY_BASIS:
            if canonical is not None or "execution_record_id" in execution:
                _fail(f"{rid}: legacy execution must remain absent from canonical map")
            if legacy_rows is None:
                from control_plane import research_execution_record_audit_fault_isolation as legacy
                legacy_rows = legacy.validated_rows(root)
            matching = [x for x in legacy_rows if x.get("execution_record_id") == eid
                        and x.get("nonlive_basis") == LEGACY_BASIS]
            if len(matching) != 1:
                _fail(f"{rid}: exact historical execution bridge missing")
            bridge = matching[0]
            if bridge.get("result_record_path") != row["record_path"] or bridge.get("result_record_blob_sha1") != row["record_blob_sha1"]:
                _fail(f"{rid}: historical execution bridge Result pin mismatch")
            diagnostic = [x.removeprefix(prefix) for x in impl.audit_result_record(result, execution, root)]
        else:
            if execution.get("execution_record_id") != eid or canonical is None:
                _fail(f"{rid}: canonical execution identity missing")
            if {k: v for k, v in canonical.items() if not k.startswith("_")} != execution:
                _fail(f"{rid}: canonical execution differs from exact pinned record")
            diagnostic = []
        actual_errors = [x.removeprefix(prefix) for x in impl.audit_result_record(result, canonical, root)]
        if actual_errors != row["allowed_result_audit_errors"]:
            _fail(f"{rid}: complete raw strict error set drift: {actual_errors!r}")
        if diagnostic != row["bound_legacy_diagnostic_errors"]:
            _fail(f"{rid}: complete bound legacy diagnostic set drift: {diagnostic!r}")
    return rows


def validated_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    active = _ACTIVE.get()
    if active is not None and active[0] == root.resolve():
        return active[1]
    return _validated_rows(root)


def _snapshot_stamp(root: Path, rows: dict[str, dict[str, Any]]) -> dict[str, str]:
    paths = {QUARANTINE_FILE, "research_execution_record_audit_quarantines.json"}
    paths.update(pin["path"] for row in rows.values() for pin in row["dependency_pins"])
    for directory in ("research_execution_records", "research_result_records", "research_result_reviews"):
        paths.update(p.relative_to(root).as_posix() for p in (root / directory).glob("*/*.json"))
    return {p: hashlib.sha256(_path(root, p).read_bytes()).hexdigest()
            for p in sorted(paths) if _path(root, p).is_file()}


@contextmanager
def authority_snapshot(root: Path = ROOT) -> Iterator[dict[str, dict[str, Any]]]:
    """Share one validation only within a reduction; reject changed bytes on exit."""
    active = _ACTIVE.get()
    if active is not None and active[0] == root.resolve():
        yield active[1]
        return
    before = _snapshot_stamp(root, quarantine_rows(root))
    rows = _validated_rows(root)
    token = _ACTIVE.set((root.resolve(), rows))
    try:
        yield rows
    finally:
        _ACTIVE.reset(token)
        if _snapshot_stamp(root, rows) != before:
            _fail("authority snapshot inputs changed during reduction")


def validated_review_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    return {review["review_id"]: {
        **review, "task_id": row["task_id"], "publication_id": row["publication_id"],
        "basis": "RESULT_CONTROL_AUTHORITY", "control_only": True, "operational": False,
    } for row in validated_rows(root).values() for review in row["derived_reviews"]}


def operational_results(
    results: list[dict[str, Any]], root: Path = ROOT, *,
    replacement_edges: dict[str, dict[str, Any]] | None = None,
) -> list[dict[str, Any]]:
    """The caller must finish ordinary replacement validation/sink selection first."""
    rows = validated_rows(root)
    surviving = [item for item in results if item.get("result_id") not in rows]
    for item in surviving:
        for rid, row in rows.items():
            if any(item.get(k) != row[k] for k in ("task_id", "publication_id", "execution_record_id")):
                continue
            # A same-execution corrected Result needs the ordinary authenticated
            # replacement chain. A separately executed clean sibling is distinct.
            cursor, visited = rid, set()
            while cursor in (replacement_edges or {}) and cursor not in visited:
                visited.add(cursor)
                cursor = replacement_edges[cursor]["corrected_result_id"]
            if cursor != item.get("result_id"):
                _fail(f"{rid}: same-execution recovery lacks validated replacement authority")
    return surviving


def operational_reviews(reviews: list[dict[str, Any]], root: Path = ROOT) -> list[dict[str, Any]]:
    rows = validated_rows(root)
    return [item for item in reviews if item.get("result_id") not in rows]


def withheld_state(task_id: str, publication_id: str, root: Path = ROOT) -> dict[str, Any] | None:
    rows = [row for row in validated_rows(root).values()
            if row["task_id"] == task_id and row["publication_id"] == publication_id]
    if not rows:
        return None
    records = [_object(_path(root, row["record_path"])) for row in rows]
    return {
        "state": STATE, "terminal": False, "result": None, "review": None,
        "task_id": task_id, "publication_id": publication_id,
        "withheld_result_ids": sorted(row["result_id"] for row in rows),
        "withheld_frozen_at": min(item["frozen_at"] for item in records),
        "historical_execution_claims": [{
            key: item.get(key) for key in
            ("result_id", "claim_id", "researcher_id", "execution_record_id", "frozen_at")
        } for item in records],
        "control_recovery_required": True,
    }


def audit_against(errors: list[str], root: Path = ROOT) -> list[str]:
    rows = validated_rows(root)
    suppressions = {f"{row['record_path']}: {suffix}" for row in rows.values()
                    for suffix in row["allowed_result_audit_errors"]}
    stale = sorted(suppressions - set(errors))
    return ([f"{QUARANTINE_FILE}: stale or unused suppression: {x}" for x in stale]
            + [x for x in errors if x not in suppressions])


def install(root: Path = ROOT) -> None:
    """Filter final public review consumers after earlier independent isolations."""
    from tools import research_result_records as public

    validated_rows(root)
    if getattr(public.iter_reviews, "_exact_result_authority_filter", False):
        return
    prior = public.iter_reviews

    def reviews(local_root: Path = ROOT) -> list[dict[str, Any]]:
        return operational_reviews(prior(local_root), local_root)

    reviews._exact_result_authority_filter = True
    public.iter_reviews = reviews
    public._result_authority_review_isolation_installed = True
