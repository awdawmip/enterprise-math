#!/usr/bin/env python3
"""Claim-scoped blind/independent source-firewall lifecycle.

This module is deliberately not a toolbox tool.  It is a validator used by the
canonical runtime guard.  Ordinary tasks that omit ``source_firewall`` are
untouched.  A BLIND_INDEPENDENT task gets three append-only local evidence
boundaries:

PRE_MATH -> RAW_FREEZE -> SOURCE_EXPOSED.

All mathematical source identities are repository-relative path + exact commit
+ Git blob SHA-1.  The records bind the current immutable publication and the
current authorized winning CLAIM (and cohort/lane when present).
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

try:
    from tools import research_task_records
    from tools import research_taskbook
except ModuleNotFoundError:
    import research_task_records  # type: ignore
    import research_taskbook  # type: ignore

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_FILE = "research_source_firewall_contract.json"
PRE_MATH_SCHEMA = "ENTERPRISE_MATH_BLIND_EXECUTION_STAMP_V2"
RAW_FREEZE_SCHEMA = "ENTERPRISE_MATH_BLIND_RAW_FREEZE_V1"
SOURCE_EXPOSURE_SCHEMA = "ENTERPRISE_MATH_BLIND_SOURCE_EXPOSURE_V1"
HEX40 = re.compile(r"^[0-9a-fA-F]{40}$")
_SAFE = re.compile(r"[^A-Za-z0-9._-]+")


class SourceFirewallError(ValueError):
    pass


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _parse_time(value: str | None) -> str:
    if value:
        dt = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
    else:
        dt = datetime.now(timezone.utc)
    return dt.astimezone(timezone.utc).isoformat()


def _git(root: Path, *args: str) -> str:
    try:
        proc = subprocess.run(
            ["git", *args],
            cwd=root,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
    except OSError as exc:
        raise SourceFirewallError(f"git is unavailable for source-firewall validation: {exc}") from exc
    if proc.returncode != 0:
        detail = proc.stderr.strip() or proc.stdout.strip() or "git command failed"
        raise SourceFirewallError(detail)
    return proc.stdout.strip()


def git_blob_sha1_bytes(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("ascii")
    return "sha1:" + hashlib.sha1(header + data).hexdigest()


def sha256_bytes(data: bytes) -> str:
    return "sha256:" + hashlib.sha256(data).hexdigest()


def _normalize_blob(value: Any) -> str:
    if not isinstance(value, str):
        raise SourceFirewallError("source pin blob_sha1 must be a string")
    text = value.strip().lower()
    if text.startswith("sha1:"):
        text = text[5:]
    if not HEX40.fullmatch(text):
        raise SourceFirewallError("source pin blob_sha1 must be a 40-hex Git blob SHA-1")
    return text


def _safe_repo_path(value: Any, *, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise SourceFirewallError(f"{field} must be a nonempty repository-relative path")
    text = value.strip().replace("\\", "/")
    path = Path(text)
    if path.is_absolute() or ".." in path.parts:
        raise SourceFirewallError(f"{field} must be a safe repository-relative path")
    return path.as_posix()


def _normalize_pins(value: Any, *, field: str, allow_empty: bool) -> list[dict[str, str]]:
    if not isinstance(value, list) or (not allow_empty and not value):
        qualifier = "a list" if allow_empty else "a nonempty list"
        raise SourceFirewallError(f"{field} must be {qualifier}")
    out: list[dict[str, str]] = []
    seen: set[tuple[str, str]] = set()
    for index, pin in enumerate(value):
        if not isinstance(pin, Mapping):
            raise SourceFirewallError(f"{field}[{index}] must be an object")
        path = _safe_repo_path(pin.get("path"), field=f"{field}[{index}].path")
        commit = pin.get("commit")
        if not isinstance(commit, str) or not HEX40.fullmatch(commit.strip()):
            raise SourceFirewallError(f"{field}[{index}].commit must be a 40-hex commit SHA")
        commit = commit.strip().lower()
        blob = _normalize_blob(pin.get("blob_sha1"))
        key = (commit, path)
        if key in seen:
            raise SourceFirewallError(f"{field} contains duplicate commit/path pin")
        seen.add(key)
        out.append({"path": path, "commit": commit, "blob_sha1": blob})
    return out


def validate_config(value: Any) -> dict[str, Any] | None:
    """Validate the optional taskbook ``source_firewall`` object."""
    if value in (None, {}, "NONE"):
        return None
    if not isinstance(value, Mapping):
        raise SourceFirewallError("source_firewall must be an object")
    mode = value.get("mode")
    if mode == "NONE":
        return None
    if mode != "BLIND_INDEPENDENT":
        raise SourceFirewallError("source_firewall.mode must be NONE or BLIND_INDEPENDENT")
    if value.get("pre_math_stamp_required") is not True:
        raise SourceFirewallError("BLIND_INDEPENDENT requires pre_math_stamp_required=true")
    remote = value.get("remote_stamp_before_math_required")
    if type(remote) is not bool:
        raise SourceFirewallError("source_firewall.remote_stamp_before_math_required must be boolean")
    allowed = _normalize_pins(
        value.get("allowed_source_pins"), field="allowed_source_pins", allow_empty=False
    )
    withheld = _normalize_pins(
        value.get("withheld_source_pins"), field="withheld_source_pins", allow_empty=True
    )
    allowed_keys = {(item["commit"], item["path"]) for item in allowed}
    withheld_keys = {(item["commit"], item["path"]) for item in withheld}
    overlap = allowed_keys & withheld_keys
    if overlap:
        raise SourceFirewallError(
            "allowed_source_pins and withheld_source_pins must be disjoint before RAW_FREEZE"
        )
    raw_path = _safe_repo_path(value.get("raw_freeze_path"), field="raw_freeze_path")
    return {
        "mode": "BLIND_INDEPENDENT",
        "pre_math_stamp_required": True,
        "remote_stamp_before_math_required": remote,
        "allowed_source_pins": allowed,
        "withheld_source_pins": withheld,
        "raw_freeze_path": raw_path,
    }


def current_task_record(task_id: str, root: Path = ROOT) -> dict[str, Any]:
    try:
        record = research_task_records.current_records(root).get(task_id)
    except Exception as exc:
        raise SourceFirewallError(f"cannot resolve current task publication: {exc}") from exc
    if record is None:
        raise SourceFirewallError("source firewall requires an immutable registered task")
    return record


def source_firewall_for_task(
    task_id: str, root: Path = ROOT
) -> tuple[dict[str, Any] | None, dict[str, Any]]:
    record = current_task_record(task_id, root)
    taskbook = root / str(record.get("taskbook_path") or "")
    try:
        meta, _ = research_taskbook.split_taskbook(taskbook.read_text(encoding="utf-8"))
    except Exception as exc:
        raise SourceFirewallError(f"cannot parse taskbook source_firewall: {exc}") from exc
    return validate_config(meta.get("source_firewall")), record


def validate_source_pins(
    pins: list[dict[str, str]], root: Path = ROOT
) -> list[dict[str, str]]:
    """Validate exact pins using only the local Git object database."""
    results: list[dict[str, str]] = []
    for pin in pins:
        commit = pin["commit"]
        path = pin["path"]
        declared_blob = pin["blob_sha1"]
        resolved_commit = _git(root, "rev-parse", "--verify", f"{commit}^{{commit}}")
        if resolved_commit.lower() != commit:
            raise SourceFirewallError(f"source pin commit did not resolve exactly: {commit}")
        actual_blob = _git(root, "rev-parse", f"{commit}:{path}").lower()
        if not HEX40.fullmatch(actual_blob):
            raise SourceFirewallError(f"source pin did not resolve to a Git blob: {path}@{commit}")
        if actual_blob != declared_blob:
            raise SourceFirewallError(
                f"source pin blob mismatch for {path}@{commit}: declared {declared_blob}, actual {actual_blob}"
            )
        results.append(
            {
                "path": path,
                "commit": commit,
                "declared_blob_sha1": declared_blob,
                "actual_blob_sha1": actual_blob,
                "status": "PASS",
            }
        )
    return results


def _binding_scope(binding: Mapping[str, Any]) -> dict[str, Any]:
    claim_id = binding.get("claim_id")
    researcher_id = binding.get("researcher_id")
    publication_id = binding.get("publication_id")
    if not isinstance(claim_id, str) or not claim_id.strip():
        raise SourceFirewallError("winning execution binding has no claim_id")
    if not isinstance(researcher_id, str) or not researcher_id.strip():
        raise SourceFirewallError("winning execution binding has no researcher_id")
    if not isinstance(publication_id, str) or not publication_id.strip():
        raise SourceFirewallError("winning execution binding has no publication_id")
    scope: dict[str, Any] = {
        "claim_id": claim_id.strip(),
        "researcher_id": researcher_id.strip().upper(),
        "publication_id": publication_id.strip(),
    }
    cohort = binding.get("execution_cohort_id")
    lane = binding.get("execution_lane_id")
    if cohort is not None or lane is not None:
        if not isinstance(cohort, str) or not cohort.strip() or not isinstance(lane, str) or not lane.strip():
            raise SourceFirewallError("blind lane provenance requires both cohort and lane ids")
        scope["execution_cohort_id"] = cohort.strip()
        scope["execution_lane_id"] = lane.strip()
    return scope


def _scope_fields(scope: Mapping[str, Any]) -> dict[str, Any]:
    out = {
        "claim_id": scope["claim_id"],
        "researcher_id": scope["researcher_id"],
    }
    if "execution_cohort_id" in scope:
        out["execution_cohort_id"] = scope["execution_cohort_id"]
        out["execution_lane_id"] = scope["execution_lane_id"]
    return out


def _safe_component(value: str) -> str:
    return _SAFE.sub("_", value).strip("_") or "scope"


def default_evidence_dir(task_id: str, binding: Mapping[str, Any], root: Path = ROOT) -> Path:
    scope = _binding_scope(binding)
    return (
        root
        / "evidence"
        / _safe_component(task_id)
        / "source_firewall"
        / _safe_component(str(scope["claim_id"]))
    )


def default_pre_math_path(task_id: str, binding: Mapping[str, Any], root: Path = ROOT) -> Path:
    return default_evidence_dir(task_id, binding, root) / "pre_math_stamp.json"


def default_raw_record_path(task_id: str, binding: Mapping[str, Any], root: Path = ROOT) -> Path:
    return default_evidence_dir(task_id, binding, root) / "raw_freeze_record.json"


def default_exposure_path(task_id: str, binding: Mapping[str, Any], root: Path = ROOT) -> Path:
    return default_evidence_dir(task_id, binding, root) / "source_exposure.json"


def _inside_root(path: Path, root: Path) -> Path:
    resolved = path if path.is_absolute() else root / path
    try:
        resolved.resolve().relative_to(root.resolve())
    except ValueError as exc:
        raise SourceFirewallError("source-firewall evidence path must stay inside repository root") from exc
    return resolved


def _relative(path: Path, root: Path) -> str:
    return path.resolve().relative_to(root.resolve()).as_posix()


def _write_exclusive(path: Path, payload: Mapping[str, Any], root: Path) -> None:
    path = _inside_root(path, root)
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(dict(payload), ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    try:
        with path.open("x", encoding="utf-8") as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError as exc:
        raise SourceFirewallError(f"refusing to overwrite source-firewall record: {path}") from exc


def build_pre_math_stamp(
    *,
    task_id: str,
    binding: Mapping[str, Any],
    created_at: str | None = None,
    root: Path = ROOT,
) -> dict[str, Any]:
    firewall, record = source_firewall_for_task(task_id, root)
    if firewall is None:
        raise SourceFirewallError("task does not declare BLIND_INDEPENDENT source_firewall")
    scope = _binding_scope(binding)
    if scope["publication_id"] != record.get("publication_id"):
        raise SourceFirewallError("winning CLAIM publication is not current source-firewall publication")
    validation = validate_source_pins(firewall["allowed_source_pins"], root)
    return {
        "schema": PRE_MATH_SCHEMA,
        "phase": "PRE_MATH",
        "task_id": task_id,
        "publication_id": record["publication_id"],
        "taskbook_path": record["taskbook_path"],
        "taskbook_blob_sha1": record["taskbook_blob_sha1"],
        **_scope_fields(scope),
        "created_at": _parse_time(created_at),
        "math_source_read_before_stamp": False,
        "source_validation": validation,
        "allowed_source_pins": firewall["allowed_source_pins"],
        "withheld_source_pins": firewall["withheld_source_pins"],
        "raw_freeze_path": firewall["raw_freeze_path"],
        "remote_stamp_before_math_required": firewall["remote_stamp_before_math_required"],
        "remote_stamp_verification": (
            "TASK_SPECIFIC_EXTERNAL_ORCHESTRATOR_REQUIRED"
            if firewall["remote_stamp_before_math_required"]
            else "NOT_REQUIRED_BEFORE_MATH"
        ),
    }


def write_pre_math_stamp(
    *,
    task_id: str,
    binding: Mapping[str, Any],
    output: Path | None = None,
    created_at: str | None = None,
    root: Path = ROOT,
) -> tuple[dict[str, Any], Path]:
    stamp = build_pre_math_stamp(task_id=task_id, binding=binding, created_at=created_at, root=root)
    path = output or default_pre_math_path(task_id, binding, root)
    path = _inside_root(path, root)
    _write_exclusive(path, stamp, root)
    return stamp, path


def verify_pre_math_stamp(
    *,
    task_id: str,
    binding: Mapping[str, Any],
    stamp_path: Path,
    root: Path = ROOT,
) -> dict[str, Any]:
    firewall, record = source_firewall_for_task(task_id, root)
    if firewall is None:
        raise SourceFirewallError("task does not declare BLIND_INDEPENDENT source_firewall")
    scope = _binding_scope(binding)
    path = _inside_root(stamp_path, root)
    if not path.exists():
        raise SourceFirewallError(f"PRE_MATH stamp does not exist: {path}")
    stamp = _load_json(path)
    if stamp.get("schema") != PRE_MATH_SCHEMA or stamp.get("phase") != "PRE_MATH":
        raise SourceFirewallError("invalid PRE_MATH stamp schema/phase")
    expected_identity = {
        "task_id": task_id,
        "publication_id": record.get("publication_id"),
        "taskbook_path": record.get("taskbook_path"),
        "taskbook_blob_sha1": record.get("taskbook_blob_sha1"),
        **_scope_fields(scope),
    }
    for field, expected in expected_identity.items():
        if stamp.get(field) != expected:
            raise SourceFirewallError(f"PRE_MATH stamp {field} mismatch")
    if stamp.get("math_source_read_before_stamp") is not False:
        raise SourceFirewallError("PRE_MATH stamp must freeze math_source_read_before_stamp=false")
    if stamp.get("allowed_source_pins") != firewall["allowed_source_pins"]:
        raise SourceFirewallError("PRE_MATH allowed-source pins differ from current taskbook")
    if stamp.get("withheld_source_pins") != firewall["withheld_source_pins"]:
        raise SourceFirewallError("PRE_MATH withheld-source pins differ from current taskbook")
    if stamp.get("raw_freeze_path") != firewall["raw_freeze_path"]:
        raise SourceFirewallError("PRE_MATH raw_freeze_path differs from current taskbook")
    if stamp.get("source_validation") != validate_source_pins(firewall["allowed_source_pins"], root):
        raise SourceFirewallError("PRE_MATH source validation is stale or inconsistent")
    return stamp


def build_raw_freeze_record(
    *,
    task_id: str,
    binding: Mapping[str, Any],
    pre_math_stamp_path: Path,
    created_at: str | None = None,
    root: Path = ROOT,
) -> dict[str, Any]:
    firewall, record = source_firewall_for_task(task_id, root)
    if firewall is None:
        raise SourceFirewallError("task does not declare BLIND_INDEPENDENT source_firewall")
    stamp = verify_pre_math_stamp(
        task_id=task_id, binding=binding, stamp_path=pre_math_stamp_path, root=root
    )
    raw_path = _inside_root(Path(firewall["raw_freeze_path"]), root)
    if not raw_path.is_file():
        raise SourceFirewallError(f"RAW_FREEZE artifact does not exist: {raw_path}")
    data = raw_path.read_bytes()
    stamp_bytes = _inside_root(pre_math_stamp_path, root).read_bytes()
    scope = _binding_scope(binding)
    return {
        "schema": RAW_FREEZE_SCHEMA,
        "phase": "RAW_FREEZE",
        "task_id": task_id,
        "publication_id": record["publication_id"],
        "taskbook_path": record["taskbook_path"],
        "taskbook_blob_sha1": record["taskbook_blob_sha1"],
        **_scope_fields(scope),
        "created_at": _parse_time(created_at),
        "pre_math_stamp_path": _relative(_inside_root(pre_math_stamp_path, root), root),
        "pre_math_stamp_sha256": sha256_bytes(stamp_bytes),
        "raw_freeze_path": firewall["raw_freeze_path"],
        "raw_freeze_blob_sha1": git_blob_sha1_bytes(data),
        "raw_freeze_sha256": sha256_bytes(data),
        "raw_freeze_bytes": len(data),
        "withheld_source_pins": stamp["withheld_source_pins"],
        "source_exposure_permitted": True,
    }


def write_raw_freeze_record(
    *,
    task_id: str,
    binding: Mapping[str, Any],
    pre_math_stamp_path: Path,
    output: Path | None = None,
    created_at: str | None = None,
    root: Path = ROOT,
) -> tuple[dict[str, Any], Path]:
    record = build_raw_freeze_record(
        task_id=task_id,
        binding=binding,
        pre_math_stamp_path=pre_math_stamp_path,
        created_at=created_at,
        root=root,
    )
    path = output or default_raw_record_path(task_id, binding, root)
    path = _inside_root(path, root)
    _write_exclusive(path, record, root)
    return record, path


def verify_raw_freeze_record(
    *,
    task_id: str,
    binding: Mapping[str, Any],
    raw_record_path: Path,
    root: Path = ROOT,
) -> dict[str, Any]:
    firewall, record = source_firewall_for_task(task_id, root)
    if firewall is None:
        raise SourceFirewallError("task does not declare BLIND_INDEPENDENT source_firewall")
    scope = _binding_scope(binding)
    path = _inside_root(raw_record_path, root)
    if not path.exists():
        raise SourceFirewallError(f"RAW_FREEZE record does not exist: {path}")
    raw_record = _load_json(path)
    if raw_record.get("schema") != RAW_FREEZE_SCHEMA or raw_record.get("phase") != "RAW_FREEZE":
        raise SourceFirewallError("invalid RAW_FREEZE record schema/phase")
    expected_identity = {
        "task_id": task_id,
        "publication_id": record.get("publication_id"),
        "taskbook_path": record.get("taskbook_path"),
        "taskbook_blob_sha1": record.get("taskbook_blob_sha1"),
        **_scope_fields(scope),
    }
    for field, expected in expected_identity.items():
        if raw_record.get(field) != expected:
            raise SourceFirewallError(f"RAW_FREEZE record {field} mismatch")
    if raw_record.get("raw_freeze_path") != firewall["raw_freeze_path"]:
        raise SourceFirewallError("RAW_FREEZE path differs from current taskbook")
    raw_path = _inside_root(Path(firewall["raw_freeze_path"]), root)
    if not raw_path.is_file():
        raise SourceFirewallError("frozen raw artifact is missing")
    data = raw_path.read_bytes()
    if raw_record.get("raw_freeze_blob_sha1") != git_blob_sha1_bytes(data):
        raise SourceFirewallError("RAW_FREEZE artifact Git blob identity drift")
    if raw_record.get("raw_freeze_sha256") != sha256_bytes(data):
        raise SourceFirewallError("RAW_FREEZE artifact SHA-256 drift")
    if raw_record.get("raw_freeze_bytes") != len(data):
        raise SourceFirewallError("RAW_FREEZE artifact byte-length drift")
    pre_ref = raw_record.get("pre_math_stamp_path")
    if not isinstance(pre_ref, str):
        raise SourceFirewallError("RAW_FREEZE record missing PRE_MATH stamp reference")
    stamp_path = _inside_root(Path(pre_ref), root)
    if not stamp_path.exists() or raw_record.get("pre_math_stamp_sha256") != sha256_bytes(stamp_path.read_bytes()):
        raise SourceFirewallError("RAW_FREEZE PRE_MATH stamp identity drift")
    verify_pre_math_stamp(task_id=task_id, binding=binding, stamp_path=stamp_path, root=root)
    return raw_record


def build_source_exposure_record(
    *,
    task_id: str,
    binding: Mapping[str, Any],
    raw_record_path: Path,
    created_at: str | None = None,
    root: Path = ROOT,
) -> dict[str, Any]:
    firewall, record = source_firewall_for_task(task_id, root)
    if firewall is None:
        raise SourceFirewallError("task does not declare BLIND_INDEPENDENT source_firewall")
    raw_record = verify_raw_freeze_record(
        task_id=task_id, binding=binding, raw_record_path=raw_record_path, root=root
    )
    exposure = validate_source_pins(firewall["withheld_source_pins"], root)
    scope = _binding_scope(binding)
    raw_path = _inside_root(raw_record_path, root)
    return {
        "schema": SOURCE_EXPOSURE_SCHEMA,
        "phase": "SOURCE_EXPOSED",
        "task_id": task_id,
        "publication_id": record["publication_id"],
        "taskbook_path": record["taskbook_path"],
        "taskbook_blob_sha1": record["taskbook_blob_sha1"],
        **_scope_fields(scope),
        "created_at": _parse_time(created_at),
        "raw_freeze_record_path": _relative(raw_path, root),
        "raw_freeze_record_sha256": sha256_bytes(raw_path.read_bytes()),
        "raw_freeze_blob_sha1": raw_record["raw_freeze_blob_sha1"],
        "withheld_source_validation": exposure,
        "source_exposure_authority": "RAW_FREEZE_VERIFIED_THEN_EXACT_WITHHELD_PINS_VALIDATED",
    }


def write_source_exposure_record(
    *,
    task_id: str,
    binding: Mapping[str, Any],
    raw_record_path: Path,
    output: Path | None = None,
    created_at: str | None = None,
    root: Path = ROOT,
) -> tuple[dict[str, Any], Path]:
    record = build_source_exposure_record(
        task_id=task_id,
        binding=binding,
        raw_record_path=raw_record_path,
        created_at=created_at,
        root=root,
    )
    path = output or default_exposure_path(task_id, binding, root)
    path = _inside_root(path, root)
    _write_exclusive(path, record, root)
    return record, path


def execution_gate(
    *,
    task_id: str,
    binding: Mapping[str, Any],
    state: Mapping[str, Any],
    root: Path = ROOT,
) -> dict[str, Any] | None:
    """Require a valid PRE_MATH stamp for an opt-in blind task."""
    firewall, _ = source_firewall_for_task(task_id, root)
    if firewall is None:
        return None
    frontier = state.get("durable_frontier")
    stamp_ref: Path
    if isinstance(frontier, Mapping) and isinstance(frontier.get("source_firewall_pre_math_stamp"), str):
        stamp_ref = Path(str(frontier["source_firewall_pre_math_stamp"]))
    else:
        stamp_ref = default_pre_math_path(task_id, binding, root)
    verify_pre_math_stamp(task_id=task_id, binding=binding, stamp_path=stamp_ref, root=root)
    if firewall["remote_stamp_before_math_required"]:
        raise SourceFirewallError(
            "task requires remote PRE_MATH stamp verification by an external orchestrator; caller state cannot satisfy it"
        )
    return {
        "mode": "BLIND_INDEPENDENT",
        "phase": "PRE_MATH_VERIFIED",
        "pre_math_stamp_path": _relative(_inside_root(stamp_ref, root), root),
        "allowed_source_count": len(firewall["allowed_source_pins"]),
        "withheld_source_count": len(firewall["withheld_source_pins"]),
        "raw_freeze_path": firewall["raw_freeze_path"],
        "remote_stamp_before_math_required": False,
    }
