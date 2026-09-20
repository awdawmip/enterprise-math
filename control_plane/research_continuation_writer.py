"""Restricted native writer adapter for an isolated writable Source snapshot.

No network or Git publication occurs here. The service owns snapshot creation,
allowed artifact uploads, fresh raw server evidence and the final Source CAS.
Only the fixed, admitted native result/review CLI is executable by this adapter.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Mapping

from control_plane.research_continuation import ContinuationError, _path, _source

MARKER = "EM_CONTINUATION_WRITE_SANDBOX.json"
GENERATED_ROOTS = {"research_result_records", "research_result_reviews", "research_driver_followups",
                   "research_tasks", "research_task_records", "research_objective_records",
                   "research_objective_heads", "research_task_objective_bindings"}
FREEZE_FIELDS = {"execution_record_id", "return_path", "output_paths", "owner_head", "terminal_verdict",
                 "hard_target_disposition", "unresolved_residue", "method_harvest", "independence_status",
                 "source_exposure_status", "next_control_plane_recommendation"}
REVIEW_REQUIRED = {"result_id", "driver_id", "reviewer_session_id", "reviewer_contribution_ids",
                   "disposition", "review_path", "destination_class", "expected_result_sha256"}
REVIEW_OPTIONAL = {"destination_ref_or_none", "followup_spec"}


def _sandbox(root: Path, source_commit: str) -> None:
    _source(source_commit)
    marker = json.loads((root / MARKER).read_text(encoding="utf-8"))
    if marker != {"schema": "ENTERPRISE_MATH_ISOLATED_WRITE_SANDBOX_V1", "source_commit": source_commit, "isolated": True}:
        raise ContinuationError("native writer requires the service's exact isolated Source sandbox marker")
    _path(root, "tools/research_result_records.py")


def _capture(root: Path) -> dict[str, str]:
    captured = {}
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if path.is_file() and not set(relative.parts) & {".git", "__pycache__"} and relative.as_posix() != MARKER:
            _path(root, relative.as_posix())
            captured[relative.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return captured


def _changes(root: Path, before: Mapping[str, str]) -> list[dict[str, str]]:
    after = _capture(root)
    deleted = set(before) - set(after)
    if deleted:
        raise ContinuationError(f"native transaction unexpectedly deleted protected records: {sorted(deleted)}")
    files = []
    for path, digest in sorted(after.items()):
        if before.get(path) == digest:
            continue
        if path.split("/", 1)[0] not in GENERATED_ROOTS:
            raise ContinuationError(f"native writer changed a path outside its fixed output classes: {path}")
        if path in before and path.split("/", 1)[0] not in {"research_tasks", "research_objective_heads"}:
            raise ContinuationError(f"native transaction unexpectedly rewrote immutable history: {path}")
        files.append({"path": path, "content": (root / path).read_text(encoding="utf-8"), "sha256": digest})
    if not files:
        raise ContinuationError("native writer produced no publishable record")
    return files


def _invoke(root: Path, command: str, arguments: list[str]) -> dict[str, Any]:
    if command not in {"freeze", "review"}:
        raise ContinuationError("unsupported native writer command")
    result = subprocess.run([sys.executable, "-I", str(root / "tools/research_result_records.py"), command, *arguments],
                            cwd=root, capture_output=True, text=True, encoding="utf-8", timeout=300, check=False)
    if result.returncode:
        raise ContinuationError(f"native {command} failed ({result.returncode}): {(result.stderr or result.stdout)[-12000:]}")
    try:
        value = json.loads(result.stdout)
    except ValueError as exc:
        raise ContinuationError(f"native {command} did not return its canonical JSON receipt") from exc
    if not isinstance(value, dict):
        raise ContinuationError("native writer returned a non-object receipt")
    return value


def prepare_freeze(*, root: Path, source_commit: str, runtime_state: Mapping[str, Any],
                   raw_comments: list[dict[str, Any]], payload: Mapping[str, Any]) -> dict[str, Any]:
    """Create a real RR locally; return exact bytes plus an unsubmitted HANDOFF."""
    _sandbox(root, source_commit)
    if set(payload) != FREEZE_FIELDS:
        raise ContinuationError("freeze payload must contain exactly the native freeze fields")
    if not isinstance(payload["output_paths"], list) or not payload["output_paths"]:
        raise ContinuationError("freeze requires explicit output_paths")
    for path in [payload["return_path"], *payload["output_paths"]]:
        _path(root, path)
    before = _capture(root)
    with tempfile.TemporaryDirectory(prefix="em-freeze-input-") as temp:
        state_path, event_path = Path(temp) / "state.json", Path(temp) / "events.json"
        state_path.write_text(json.dumps(runtime_state, ensure_ascii=False), encoding="utf-8")
        event_path.write_text(json.dumps(raw_comments, ensure_ascii=False), encoding="utf-8")
        arguments = ["--source-commit", source_commit, "--runtime-state-file", str(state_path), "--events", str(event_path)]
        for key, value in payload.items():
            flag = "--output-paths-json" if key == "output_paths" else "--" + key.replace("_", "-")
            arguments.extend([flag, json.dumps(value, ensure_ascii=False) if key == "output_paths" else str(value)])
        record = _invoke(root, "freeze", arguments)
    files = _changes(root, before)
    expected_path = f"research_result_records/{record['task_id']}/{record['result_id']}.json"
    if len(files) != 1 or files[0]["path"] != expected_path:
        raise ContinuationError("native freeze produced an unexpected write scope")
    template = {"schema": "ENTERPRISE_MATH_SCHEDULER_EVENT_V1", "event": "HANDOFF",
                "task_id": record["task_id"], "publication_id": record["publication_id"],
                "claim_id": record["claim_id"], "researcher_id": record["researcher_id"],
                "result_id": record["result_id"], "handoff_scope": "FROZEN_RETURN_AWAITING_DRIVER_REVIEW",
                "terminal_scope": "RESEARCH_RETURN_FROZEN_AWAITING_DRIVER_REVIEW",
                "next_action": record["next_control_plane_recommendation"]}
    return {"files": files, "record": record, "result_record_path": expected_path,
            "handoff_event_template": template, "requires_publication_before_handoff": True,
            "handoff_progress_ref_rule": "Fill exact immutable Source commit/result-record URL only after CAS and full-byte readback.",
            "execution_authorized": False, "mathematical_acceptance_granted": False}


def prepare_review(*, root: Path, source_commit: str, payload: Mapping[str, Any]) -> dict[str, Any]:
    """Run only the explicitly requested Driver disposition and follow-up spec."""
    _sandbox(root, source_commit)
    if not REVIEW_REQUIRED <= set(payload) or set(payload) - REVIEW_REQUIRED - REVIEW_OPTIONAL:
        raise ContinuationError("review payload must contain the native review fields and no unknown controls")
    _path(root, payload["review_path"])
    matches = list((root / "research_result_records").glob(f"*/{payload['result_id']}.json"))
    if len(matches) != 1 or hashlib.sha256(matches[0].read_bytes()).hexdigest() != payload["expected_result_sha256"]:
        raise ContinuationError("review Result bytes changed; refresh exact Result before review write")
    before = _capture(root)
    arguments = ["--source-commit", source_commit]
    for key in REVIEW_REQUIRED - {"expected_result_sha256", "reviewer_contribution_ids"}:
        arguments.extend(["--" + key.replace("_", "-"), str(payload[key])])
    arguments.extend(["--reviewer-contribution-ids-json", json.dumps(payload["reviewer_contribution_ids"], ensure_ascii=False)])
    if "destination_ref_or_none" in payload:
        arguments.extend(["--destination-ref-or-none", str(payload["destination_ref_or_none"])])
    with tempfile.TemporaryDirectory(prefix="em-review-input-") as temp:
        if "followup_spec" in payload:
            spec_path = Path(temp) / "followup.json"
            spec_path.write_text(json.dumps(payload["followup_spec"], ensure_ascii=False), encoding="utf-8")
            arguments.extend(["--followup-spec", str(spec_path)])
        result = _invoke(root, "review", arguments)
    return {"files": _changes(root, before), "review": result["review"], "followup": result["followup"],
            "requires_source_cas_and_readback": True, "disposition_was_explicitly_supplied": True,
            "default_successor_generated": False}
