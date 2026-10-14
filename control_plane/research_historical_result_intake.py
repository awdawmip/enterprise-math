"""Prospective review of immutable historical science; no retrospective execution.

HRI and HIRR are distinct record kinds, never ordinary RR/ER/DR aliases. A
Source-approved, exact pinned target can be admitted by a *current* winning GOV
Driver execution. Its old scientific record is copied as provenance without
normalizing old enums or inferring missing authentication. Fresh independent
Driver review plus explicit task-scoped continuation is the only terminal gate.
Remote publication still needs current Source CAS and execution reauthorization.
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

from control_plane import immutable_write_transaction as tx

CONTRACT = "control_plane/historical_result_intake_contract.json"
SCHEMA = "ENTERPRISE_MATH_HISTORICAL_RESULT_INTAKE_V1"
REVIEW_SCHEMA = "ENTERPRISE_MATH_HISTORICAL_RESULT_REVIEW_V1"
INTAKE_ROOT = "research_historical_result_intakes"
REVIEW_ROOT = "research_historical_result_reviews"
SPEC_KEYS = frozenset(("run_request_id", "target_task_id", "publication_id", "historical_result_id",
    "expected_result_sha256", "expected_result_blob_sha1", "expected_execution_sha256",
    "expected_execution_blob_sha1", "expected_publication_blob_sha1", "expected_taskbook_blob_sha1", "reason"))
REVIEW_KEYS = frozenset(("target_task_id", "publication_id", "intake_id", "expected_intake_sha256",
    "expected_intake_blob_sha1", "review_path", "expected_review_sha256", "expected_review_blob_sha1",
    "disposition", "reviewer_contribution_ids", "reason", "portfolio_continuation", "supersedes_review_ids", "expected_previous_review_set_sha256"))
BASE_CONTEXT_KEYS = frozenset(("source_commit", "authorized_at", "principal", "authority_observed_through_comment_id"))
INTAKE_CONTEXT_KEYS = BASE_CONTEXT_KEYS | {"server_comments", "task_definition", "taskbook_content_base64"}
GOV_PRINCIPAL_KEYS = frozenset(("driver_id", "session_id", "authority_record_id", "governance_task_id",
    "governance_publication_id", "claim_id", "ownership_epoch", "execution_record_id", "run_request_id"))
REVIEW_PRINCIPAL_KEYS = frozenset(("driver_id", "session_id", "authority_record_id"))
INTAKE_RECORD_KEYS = frozenset(("record_schema", "intake_id", "task_id", "publication_id", "historical_result_id",
    "target_pins", "scientific_record", "scientific_manifest", "historical_authentication_status", "effect",
    "historical_review_inherited", "terminal", "created_at", "request_binding", "reason", "authorization"))
REVIEW_RECORD_KEYS = frozenset(("record_schema", "review_id", "intake_id", "task_id", "publication_id", "intake_pin",
    "review_artifact_pin", "driver_id", "reviewer_contribution_ids", "disposition", "task_scope_followup", "terminal_scope",
    "parent_completion_granted", "working_truth_granted", "canonical_promotion_granted", "created_at", "reason", "authorization"))
REVIEW_RECORD_KEYS |= {"previous_review_set", "previous_review_set_sha256"}


class HistoricalIntakeError(ValueError):
    pass


def _require(value: bool, message: str) -> None:
    if not value:
        raise HistoricalIntakeError(message)


def _text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _keys(value: Any, expected: frozenset[str], label: str) -> None:
    _require(isinstance(value, dict) and set(value) == expected, f"{label} has missing or unknown fields")


def _digest(record: Mapping[str, Any]) -> str:
    value = {k: v for k, v in record.items() if k != "authorization" and not k.startswith("_")}
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def _path(root: Path, value: str) -> Path:
    _require(_text(value), "missing path")
    path = (root / value).resolve()
    _require(not Path(value).is_absolute() and path.is_relative_to(root.resolve()), "unsafe artifact path")
    return path


def pin(root: Path, value: str) -> dict[str, Any]:
    raw = _path(root, value).read_bytes()
    return {"path": value, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(),
            "git_blob_sha1": hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()}


def _hex(value: Any, n: int) -> bool:
    return isinstance(value, str) and re.fullmatch(f"[0-9a-f]{{{n}}}", value) is not None


def _check_pin(root: Path, row: Mapping[str, Any]) -> dict[str, Any]:
    actual = pin(root, str(row["path"]))
    _require(all(actual[k] == str(row[k]).removeprefix("sha1:").removeprefix("sha256:")
                 for k in ("sha256", "git_blob_sha1")), "immutable evidence byte drift: " + actual["path"])
    return actual


def _target(root: Path, task: str, publication: str, result: str) -> dict[str, Any]:
    contract = json.loads((root / CONTRACT).read_text(encoding="utf-8"))
    _require(contract.get("schema") == "ENTERPRISE_MATH_HISTORICAL_RESULT_INTAKE_CONTRACT_V1", "invalid intake contract")
    found = [row for row in contract["targets"] if (row["task_id"], row["publication_id"], row["historical_result_id"]) == (task, publication, result)]
    _require(len(found) == 1, "historical target has no exact Source-approved intake scope")
    return found[0]


def _science(root: Path, target: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    if "historical_source_custody" in target:
        from control_plane import research_historical_source_custody as custody
        return custody.science(root, target)
    for field in ("result_pin", "execution_pin", "publication_pin", "taskbook_pin"):
        _check_pin(root, target[field])
    old = json.loads(_path(root, target["result_pin"]["path"]).read_text(encoding="utf-8"))
    er = json.loads(_path(root, target["execution_pin"]["path"]).read_text(encoding="utf-8"))
    publication = json.loads(_path(root, target["publication_pin"]["path"]).read_text(encoding="utf-8"))
    for key in ("task_id", "publication_id"):
        _require(old[key] == target[key] == publication[key] == er[key], "historical publication scope mismatch")
    _require(old["result_id"] == target["historical_result_id"], "historical Result identity mismatch")
    audit_execution = _execution_evidence(root, target, old, er, publication)
    for key in ("claim_id", "researcher_id", "execution_branch"):
        _require(old[key] == er[key], "historical execution-linked field mismatch: " + key)
    _require(publication["taskbook_blob_sha1"] == old["taskbook_blob_sha1"], "historical taskbook mismatch")
    _require(old.get("output_manifest") and isinstance(old["output_manifest"], list), "missing historical outputs")
    outputs = [_check_pin(root, row) for row in old["output_manifest"]]
    _require(len({row["path"] for row in outputs}) == len(outputs), "duplicate historical output")
    _require(any(row["path"] == old["return_path"] and row["sha256"] == old["return_sha256"].removeprefix("sha256:")
                 and row["git_blob_sha1"] == old["return_blob_sha1"].removeprefix("sha1:") for row in outputs), "return outside historical manifest")
    from control_plane import research_result_records_impl as impl
    executions = impl.execution_map(root)
    if audit_execution is None:
        _require(old["execution_record_id"] not in executions, "historical flat ER cannot be imported or aliased")
    else:
        # Bind a preexisting canonical row to its exact original bytes; do not
        # create an alias or infer authenticated execution from its presence.
        canonical = executions.get(old["execution_record_id"])
        _require(isinstance(canonical, dict), "pinned canonical execution evidence is absent from execution map")
        _require(canonical.get("_record_path") == target["execution_pin"]["path"],
                 "pinned canonical execution map path mismatch")
        _require(canonical == {**audit_execution, "_record_path": target["execution_pin"]["path"]},
                 "pinned canonical execution map content mismatch")
    failures = impl.audit_result_record(old, audit_execution, root)
    errors = {error.split(": ", 1)[-1] for error in failures}
    _require(errors == set(target["allowed_ordinary_audit_errors"]), "historical audit has an unapproved failure or changed diagnosis")
    return old, outputs


def _execution_evidence(root: Path, target: dict[str, Any], old: dict[str, Any],
                        er: dict[str, Any], publication: dict[str, Any]) -> dict[str, Any] | None:
    """Validate pinned historical provenance; never normalize an ER or authorize it."""
    if "historical_execution_evidence" not in target:
        _require(old["execution_record_id"] == er.get("execution_record_id"), "historical execution identity mismatch")
        _require(old["taskbook_blob_sha1"] == er.get("taskbook_blob_sha1"), "historical execution-linked field mismatch: taskbook_blob_sha1")
        return
    profile = target["historical_execution_evidence"]
    if isinstance(profile, dict) and profile.get("schema") == "ENTERPRISE_MATH_EXACT_EXISTING_CANONICAL_EXECUTION_EVIDENCE_V1":
        expected = {
            "schema": "ENTERPRISE_MATH_EXACT_EXISTING_CANONICAL_EXECUTION_EVIDENCE_V1",
            "historical_identifier_field": "execution_record_id",
            "required_fields": ["execution_record_id", "taskbook_blob_sha1"],
            "execution_map_binding": "EXACT_PREEXISTING_RECORD_PATH_AND_BYTES",
            "taskbook_binding_basis": "EXACT_RESULT_PUBLICATION_AND_TASKBOOK_PINS",
            "execution_authentication_restored": False,
            "canonical_execution_alias_created": False,
        }
        _keys(profile, frozenset(expected), "existing canonical execution evidence profile")
        _require(profile == expected and profile["execution_authentication_restored"] is False
                 and profile["canonical_execution_alias_created"] is False,
                 "unsupported existing canonical execution evidence profile")
        _require(target.get("historical_authentication_status") == "UNKNOWN_NO_RECOVERED_AUTHENTICATED_SERVER_ENVELOPES",
                 "existing canonical evidence cannot restore historical authentication")
        _require(target.get("allowed_ordinary_audit_errors") == ["invalid method_harvest", "invalid independence_status", "invalid source_exposure_status"],
                 "existing canonical evidence permits only the three exact legacy enum errors")
        _require(er.get("record_schema") == "ENTERPRISE_MATH_RESEARCH_EXECUTION_RECORD_V1"
                 and "_record_path" not in er and all(_text(er.get(key)) for key in expected["required_fields"]),
                 "existing canonical evidence requires original canonical execution fields")
        _require(er["execution_record_id"] == old["execution_record_id"]
                 and Path(target["execution_pin"]["path"]).name == old["execution_record_id"] + ".json",
                 "existing canonical execution evidence identity mismatch")
        _require(er.get("execution_branch_base") == old["execution_branch_base"],
                 "historical execution-linked field mismatch: execution_branch_base")
        _require(old["taskbook_path"] == er.get("taskbook_path") == publication.get("taskbook_path") == target["taskbook_pin"]["path"],
                 "existing canonical evidence requires exact Result/execution/publication/Taskbook path binding")
        actual = pin(root, target["taskbook_pin"]["path"])
        _require(all(item["taskbook_blob_sha1"].removeprefix("sha1:") == actual["git_blob_sha1"]
                     for item in (old, er, publication)),
                 "existing canonical evidence requires exact Result/execution/publication/Taskbook byte binding")
        return er
    expected = {
        "schema": "ENTERPRISE_MATH_EXACT_LEGACY_EXECUTION_EVIDENCE_V1",
        "historical_identifier_field": "record_id",
        "absent_fields": ["execution_record_id", "taskbook_blob_sha1"],
        "taskbook_binding_basis": "EXACT_RESULT_PUBLICATION_AND_TASKBOOK_PINS",
        "execution_authentication_restored": False,
        "canonical_execution_alias_created": False,
    }
    _keys(profile, frozenset(expected), "historical execution evidence profile")
    _require(profile == expected and profile["execution_authentication_restored"] is False
             and profile["canonical_execution_alias_created"] is False,
             "unsupported historical execution evidence profile")
    _require(target.get("historical_authentication_status") == "UNKNOWN_NO_RECOVERED_AUTHENTICATED_SERVER_ENVELOPES",
             "legacy evidence profile cannot restore historical authentication")
    _require(all(key not in er for key in expected["absent_fields"]),
             "legacy evidence profile requires exact missing execution fields")
    _require(er.get("record_id") == old["execution_record_id"]
             and Path(target["execution_pin"]["path"]).name == old["execution_record_id"] + ".json",
             "legacy execution evidence identity mismatch")
    _require(er.get("execution_branch_base") == old["execution_branch_base"],
             "historical execution-linked field mismatch: execution_branch_base")
    _require(old["taskbook_path"] == publication.get("taskbook_path") == target["taskbook_pin"]["path"],
             "legacy evidence requires exact Result/publication/Taskbook path binding")
    actual = pin(root, target["taskbook_pin"]["path"])
    _require(old["taskbook_blob_sha1"].removeprefix("sha1:") == actual["git_blob_sha1"]
             and publication["taskbook_blob_sha1"].removeprefix("sha1:") == actual["git_blob_sha1"],
             "legacy evidence requires exact Result/publication/Taskbook byte binding")


def _authority(context: dict[str, Any], root: Path, *, governance: str | None = None, fresh: bool = False) -> None:
    _keys(context, INTAKE_CONTEXT_KEYS if governance else BASE_CONTEXT_KEYS, "authority context")
    principal = context["principal"]
    _keys(principal, GOV_PRINCIPAL_KEYS if governance else REVIEW_PRINCIPAL_KEYS, "current principal")
    _require(_hex(context["source_commit"], 40), "current authority has no immutable Source commit")
    from tools import research_runtime_reducer as reducer
    at = reducer.parse_time(context["authorized_at"])
    if fresh:
        delta = (datetime.now(timezone.utc) - at).total_seconds()
        _require(-5 <= delta <= 90, "writer requires fresh current authorization")
        from control_plane import research_continuation
        research_continuation.verify_source_snapshot(root, context["source_commit"])
    boundary = context["authority_observed_through_comment_id"]
    _require(type(boundary) is int and boundary > 0, "missing actual Driver event boundary")
    import research_driver_authority as driver
    authority = driver.require_active_driver(principal["driver_id"], at.isoformat(), root, through_comment_id=boundary)
    _require(authority is not None and authority["authority_record_id"] == principal["authority_record_id"], "inactive or different current Driver authority")
    body = json.loads(authority["source_body"])
    session = body.get("session_id") or (body.get("succession") or {}).get("session_id")
    _require(_text(session) and session == principal["session_id"], "current Driver session mismatch")
    if governance:
        _require(principal["governance_task_id"] == governance, "GOV task does not authorize this historical target")
        from tools import research_dispatch
        from control_plane import research_continuation_write_authority as writes
        publication = json.loads((root / "research_task_records" / governance / (principal["governance_publication_id"] + ".json")).read_text())
        if fresh:
            from tools import research_task_records
            current = research_task_records.current_records(root).get(governance)
            _require(isinstance(current, dict) and current.get("publication_id") == principal["governance_publication_id"]
                     and current.get("claimable") is True, "intake GOV publication is no longer current and claimable")
        definition = writes._canonical_frozen_definition(publication, context)
        _require(definition == context["task_definition"] and definition.get("kind") == "GOVERNANCE", "not the immutable GOV task definition")
        events = research_dispatch.events_from_github_comments(context["server_comments"], root=root)
        accepted, _ = research_dispatch._event_authentication_filter(definition, events)
        filtered, _ = research_dispatch._filter_registered_events(definition, accepted, root, result_state=None)
        state = reducer.reduce_task(definition, filtered, default_lease_minutes=int(definition.get("claim_lease_minutes") or 120), now=at)
        _require(state.get("dispatch_state") == "LEASED", "intake requires winning live GOV CLAIM")
        for key, expected in (("claim_id", principal["claim_id"]), ("researcher_id", principal["driver_id"]),
                              ("ownership_epoch", principal["ownership_epoch"]), ("session_id", principal["session_id"])):
            _require(state.get(key) == expected, "GOV ownership mismatch: " + key)
        er = json.loads((root / "research_execution_records" / governance / (principal["execution_record_id"] + ".json")).read_text())
        for key, expected in (("task_id", governance), ("publication_id", principal["governance_publication_id"]),
                              ("claim_id", principal["claim_id"]), ("researcher_id", principal["driver_id"])):
            _require(er.get(key) == expected, "current GOV ER mismatch: " + key)
        _require(_text(principal["run_request_id"]), "missing authenticated current GOV run binding")


def _receipt(record: dict[str, Any], context: dict[str, Any]) -> dict[str, Any]:
    return {"schema": "ENTERPRISE_MATH_PROSPECTIVE_HISTORICAL_WRITE_AUTHORIZATION_V1",
            "payload_sha256": _digest(record), "context": copy.deepcopy(context)}


def _validate_receipt(record: dict[str, Any], root: Path, governance: str | None = None) -> None:
    auth = record.get("authorization")
    _require(isinstance(auth, dict) and set(auth) == {"schema", "payload_sha256", "context"}, "missing typed historical authorization")
    _require(auth["schema"] == "ENTERPRISE_MATH_PROSPECTIVE_HISTORICAL_WRITE_AUTHORIZATION_V1" and auth["payload_sha256"] == _digest(record), "historical authorization payload mismatch")
    _authority(auth["context"], root, governance=governance)


def _target_pins(target: dict[str, Any]) -> dict[str, Any]:
    pins = {k: copy.deepcopy(target[k]) for k in ("result_pin", "execution_pin", "publication_pin", "taskbook_pin")}
    if "historical_source_custody" in target:
        from control_plane import research_historical_source_custody as custody
        pins["custody_map_pin"] = custody.map_pin(target)
    return pins


def validate_intake(record: dict[str, Any], *, root: Path) -> None:
    _keys(record, INTAKE_RECORD_KEYS, "historical intake record")
    _require(record.get("record_schema") == SCHEMA, "wrong historical intake schema")
    target = _target(root, record["task_id"], record["publication_id"], record["historical_result_id"])
    old, outputs = _science(root, target)
    _require(record["scientific_record"] == old and record["scientific_manifest"] == outputs, "historical science or author provenance changed")
    _require(record["target_pins"] == _target_pins(target), "intake target pins changed")
    expected_id = "HRI-" + hashlib.sha256((target["task_id"] + "|" + target["publication_id"] + "|" + target["result_pin"]["sha256"]).encode()).hexdigest()[:24].upper()
    _require(record["intake_id"] == expected_id, "wrong historical intake ID")
    _require(record["historical_authentication_status"] == target["historical_authentication_status"], "historical authentication cannot be restored")
    _require(record["effect"] == "PROSPECTIVE_SCIENTIFIC_REVIEW_ONLY" and record["terminal"] is False and record["historical_review_inherited"] is False, "intake cannot grant acceptance or completion")
    _require(_text(record["reason"]) and record["created_at"] == record["authorization"]["context"]["authorized_at"]
             and record["request_binding"] == record["authorization"]["context"]["principal"]["run_request_id"], "intake write-time or request binding differs from current principal")
    _validate_receipt(record, root, target["authorizing_governance_task_id"])


def _persist(record: dict[str, Any], relative: str, validator: Any, root: Path) -> dict[str, Any]:
    validator(record, root=root)
    path = _path(root, relative)
    if path.exists():
        actual = json.loads(path.read_text())
        validator(actual, root=root)
        # A deterministic identity is an immutable semantic slot. A repeated
        # plan may use a later auth time/source, but cannot replace its old bytes.
        semantic = lambda row: {k: v for k, v in row.items() if k not in {"authorization", "created_at", "request_binding", "reason"}}
        _require(semantic(actual) == semantic(record), "historical immutable slot already has different semantics")
        return {"record_path": relative, "record": actual, "created": False}
    tx.commit([tx.PlannedFile(path, tx.json_bytes(record))], postcheck=lambda: _postcheck(validator, record, root))
    return {"record_path": relative, "record": record, "created": True}


def _postcheck(validator: Any, record: dict[str, Any], root: Path) -> list[str]:
    try:
        validator(record, root=root)
        return []
    except Exception as exc:
        return [str(exc)]


def freeze_intake(spec: dict[str, Any], authority_context: dict[str, Any], *, root: Path) -> dict[str, Any]:
    _keys(spec, SPEC_KEYS, "intake spec")
    _require(_text(spec["reason"]), "intake reason missing")
    target = _target(root, spec["target_task_id"], spec["publication_id"], spec["historical_result_id"])
    from tools import research_task_records
    from control_plane.research_result_authority_fault_isolation import ResultAuthorityIsolationError
    try:
        current_records = research_task_records.current_records(root)
    except ResultAuthorityIsolationError as exc:
        # Canonical views can reject pinned evidence before _science runs.
        # Preserve that strict rejection through the intake error surface.
        raise HistoricalIntakeError(str(exc)) from exc
    current = current_records.get(target["task_id"])
    _require(isinstance(current, dict) and current.get("publication_id") == target["publication_id"], "historical target publication is no longer current")
    fields = (("expected_result_sha256", "result_pin", "sha256"), ("expected_result_blob_sha1", "result_pin", "git_blob_sha1"),
        ("expected_execution_sha256", "execution_pin", "sha256"), ("expected_execution_blob_sha1", "execution_pin", "git_blob_sha1"),
        ("expected_publication_blob_sha1", "publication_pin", "git_blob_sha1"), ("expected_taskbook_blob_sha1", "taskbook_pin", "git_blob_sha1"))
    for key, row, field in fields:
        _require(spec[key] == target[row][field], "intake expected CAS pin differs from Source contract: " + key)
    _authority(authority_context, root, governance=target["authorizing_governance_task_id"], fresh=True)
    _require(spec["run_request_id"] == authority_context["principal"]["run_request_id"], "intake run binding mismatch")
    old, outputs = _science(root, target)
    identifier = "HRI-" + hashlib.sha256((target["task_id"] + "|" + target["publication_id"] + "|" + target["result_pin"]["sha256"]).encode()).hexdigest()[:24].upper()
    record = {"record_schema": SCHEMA, "intake_id": identifier, "task_id": target["task_id"], "publication_id": target["publication_id"],
        "historical_result_id": target["historical_result_id"], "target_pins": _target_pins(target),
        "scientific_record": old, "scientific_manifest": outputs, "historical_authentication_status": target["historical_authentication_status"],
        "effect": "PROSPECTIVE_SCIENTIFIC_REVIEW_ONLY", "historical_review_inherited": False, "terminal": False,
        "created_at": authority_context["authorized_at"], "request_binding": spec["run_request_id"], "reason": spec["reason"]}
    record["authorization"] = _receipt(record, authority_context)
    return _persist(record, f"{INTAKE_ROOT}/{record['task_id']}/{identifier}.json", validate_intake, root)


def validate_review(record: dict[str, Any], *, root: Path) -> None:
    _keys(record, REVIEW_RECORD_KEYS, "historical review record")
    _require(record.get("record_schema") == REVIEW_SCHEMA, "wrong historical review schema")
    intake_path = f"{INTAKE_ROOT}/{record['task_id']}/{record['intake_id']}.json"
    intake = json.loads(_path(root, intake_path).read_text())
    validate_intake(intake, root=root)
    _check_pin(root, record["intake_pin"])
    _require(record["intake_pin"]["path"] == intake_path and record["publication_id"] == intake["publication_id"], "review intake scope mismatch")
    _check_pin(root, record["review_artifact_pin"])
    _validate_receipt(record, root)
    principal = record["authorization"]["context"]["principal"]
    _require(record["driver_id"] == principal["driver_id"], "review author principal mismatch")
    _require(_text(record["reason"]) and record["created_at"] == record["authorization"]["context"]["authorized_at"], "review write-time differs from authenticated principal")
    declared = record["reviewer_contribution_ids"]
    _require(isinstance(declared, list) and declared and all(_text(v) for v in declared) and len(set(declared)) == len(declared), "reviewer must preserve explicit contribution identities")
    science = intake["scientific_record"]
    authors = set(science.get("contributor_ids", [])) | {science["researcher_id"]}
    _require(not authors.intersection(set(declared) | {record["driver_id"]}), "reviewer contributed to historical science")
    _require(record["disposition"] in {"ACCEPTED", "REQUEST_REVISION", "REJECTED"}, "invalid fresh review disposition")
    followup = record["task_scope_followup"]
    _keys(followup, frozenset(("parent_objective_status", "next_action", "next_task_id")), "task-scoped continuation")
    _require(followup["parent_objective_status"] == "OPEN" and _text(followup["next_action"]) and
             (followup["next_task_id"] is None or _text(followup["next_task_id"])), "fresh review requires an explicit open parent continuation")
    _require(record["terminal_scope"] == "TASK" and record["parent_completion_granted"] is False and record["working_truth_granted"] is False and record["canonical_promotion_granted"] is False, "fresh historical review exceeds task scope")
    previous = record["previous_review_set"]
    _require(isinstance(previous, list) and len({row["review_id"] for row in previous}) == len(previous), "invalid previous exact review set")
    _require(record["previous_review_set_sha256"] == review_set_digest(previous), "previous review set digest changed")
    from tools import research_runtime_reducer as reducer
    at = reducer.parse_time(record["created_at"])
    for row in previous:
        _keys(row, frozenset(("review_id", "path", "bytes", "sha256", "git_blob_sha1")), "previous review pin")
        _check_pin(root, row)
        _require(row["path"] == f"{REVIEW_ROOT}/{record['intake_id']}/{row['review_id']}.json" and row["review_id"] != record["review_id"], "invalid review successor linkage")
        parent = json.loads(_path(root, row["path"]).read_text())
        _require(parent["intake_id"] == record["intake_id"] and reducer.parse_time(parent["created_at"]) < at, "review successor must follow exact immutable parents")
    identifier = "HIRR-" + hashlib.sha256((record["intake_id"] + "|" + record["driver_id"] + "|" + record["review_artifact_pin"]["sha256"] + "|" + record["disposition"] + "|" + record["previous_review_set_sha256"]).encode()).hexdigest()[:24].upper()
    _require(record["review_id"] == identifier, "wrong historical review ID")


def review_set_digest(rows: list[dict[str, Any]]) -> str:
    values = sorted(({key: row[key] for key in ("review_id", "sha256", "git_blob_sha1")} for row in rows), key=lambda row: row["review_id"])
    return hashlib.sha256(json.dumps(values, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def review_heads(intake_id: str, *, root: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Return exact immutable history and DAG heads, with no latest-wins rule."""
    rows = []
    ids = set()
    replaced = set()
    for path in (root / REVIEW_ROOT / intake_id).glob("*.json"):
        row = json.loads(path.read_text())
        validate_review(row, root=root)
        _require(row["intake_id"] == intake_id and path.name == row["review_id"] + ".json" and row["review_id"] not in ids, "historical review path/identity set mismatch")
        ids.add(row["review_id"])
        replaced.update(value["review_id"] for value in row["previous_review_set"])
        rows.append(row)
    _require(replaced.issubset(ids), "missing review successor parent")
    return rows, [row for row in rows if row["review_id"] not in replaced]


def freeze_review(spec: dict[str, Any], authority_context: dict[str, Any], *, root: Path) -> dict[str, Any]:
    _keys(spec, REVIEW_KEYS, "historical review spec")
    _require(_text(spec["reason"]), "review reason missing")
    from tools import research_task_records
    current = research_task_records.current_records(root).get(spec["target_task_id"])
    _require(isinstance(current, dict) and current.get("publication_id") == spec["publication_id"], "review target publication is no longer current")
    _authority(authority_context, root, fresh=True)
    intake_path = f"{INTAKE_ROOT}/{spec['target_task_id']}/{spec['intake_id']}.json"
    intake_pin = _check_pin(root, {"path": intake_path, "sha256": spec["expected_intake_sha256"], "git_blob_sha1": spec["expected_intake_blob_sha1"]})
    artifact_pin = _check_pin(root, {"path": spec["review_path"], "sha256": spec["expected_review_sha256"], "git_blob_sha1": spec["expected_review_blob_sha1"]})
    driver = authority_context["principal"]["driver_id"]
    identifier = "HIRR-" + hashlib.sha256((spec["intake_id"] + "|" + driver + "|" + artifact_pin["sha256"] + "|" + spec["disposition"] + "|" + spec["expected_previous_review_set_sha256"]).encode()).hexdigest()[:24].upper()
    relative = f"{REVIEW_ROOT}/{spec['intake_id']}/{identifier}.json"
    existing = _path(root, relative)
    if existing.exists():
        # Lost-response recovery resolves the deterministic *original* record;
        # its publication already moved the head set, so do not CAS it again.
        prior = json.loads(existing.read_text())
        validate_review(prior, root=root)
        expected = {"task_id": spec["target_task_id"], "publication_id": spec["publication_id"],
            "intake_pin": intake_pin, "review_artifact_pin": artifact_pin, "driver_id": driver,
            "reviewer_contribution_ids": spec["reviewer_contribution_ids"], "disposition": spec["disposition"],
            "task_scope_followup": spec["portfolio_continuation"], "previous_review_set_sha256": spec["expected_previous_review_set_sha256"]}
        _require(all(prior[key] == value for key, value in expected.items()) and
            sorted(row["review_id"] for row in prior["previous_review_set"]) == sorted(spec["supersedes_review_ids"]),
            "review retry differs from original immutable operation")
        _require(prior["authorization"]["context"]["principal"]["session_id"] == authority_context["principal"]["session_id"], "review retry belongs to a different original session")
        return {"record_path": relative, "record": prior, "created": False}
    _, heads = review_heads(spec["intake_id"], root=root)
    previous = [{"review_id": row["review_id"], **pin(root, f"{REVIEW_ROOT}/{spec['intake_id']}/{row['review_id']}.json")} for row in heads]
    supplied = spec["supersedes_review_ids"]
    _require(isinstance(supplied, list) and len(set(supplied)) == len(supplied) and set(supplied) == {row["review_id"] for row in heads}, "review successor CAS must consume the complete current head set")
    _require(spec["expected_previous_review_set_sha256"] == review_set_digest(previous), "review exact-set CAS changed")
    record = {"record_schema": REVIEW_SCHEMA, "review_id": identifier, "intake_id": spec["intake_id"], "task_id": spec["target_task_id"],
        "publication_id": spec["publication_id"], "intake_pin": intake_pin, "review_artifact_pin": artifact_pin, "driver_id": driver,
        "reviewer_contribution_ids": copy.deepcopy(spec["reviewer_contribution_ids"]), "disposition": spec["disposition"],
        "previous_review_set": previous, "previous_review_set_sha256": spec["expected_previous_review_set_sha256"],
        "task_scope_followup": copy.deepcopy(spec["portfolio_continuation"]), "terminal_scope": "TASK", "parent_completion_granted": False,
        "working_truth_granted": False, "canonical_promotion_granted": False, "created_at": authority_context["authorized_at"], "reason": spec["reason"]}
    record["authorization"] = _receipt(record, authority_context)
    return _persist(record, relative, validate_review, root)


def task_state(task_id: str, publication_id: str, *, root: Path) -> dict[str, Any] | None:
    """New handle is reviewable; old records/DRs stay isolated as history.

    Multiple fresh decisive reviews require explicit synthesis: never latest-wins.
    This reducer grants no execution or followup publication authority.
    """
    rows = []
    for path in (root / INTAKE_ROOT / task_id).glob("*.json"):
        row = json.loads(path.read_text())
        if row.get("publication_id") == publication_id:
            validate_intake(row, root=root)
            rows.append(row)
    if not rows:
        return None
    _require(len(rows) == 1, "historical intake set requires explicit synthesis")
    intake = rows[0]
    history, reviews = review_heads(intake["intake_id"], root=root)
    head_pins = [{"review_id": row["review_id"], **pin(root, f"{REVIEW_ROOT}/{intake['intake_id']}/{row['review_id']}.json")} for row in reviews]
    value = {"task_id": task_id, "publication_id": publication_id, "state": "AWAITING_DRIVER_REVIEW", "result": {
        **copy.deepcopy(intake["scientific_record"]), "result_id": intake["intake_id"], "record_schema": SCHEMA,
        "_record_path": f"{INTAKE_ROOT}/{task_id}/{intake['intake_id']}.json",
        # This is a new prospective lifecycle boundary, not a restoration of
        # the unknown old execution. Retain the original time as provenance.
        "frozen_at": intake["created_at"], "historical_frozen_at": intake["scientific_record"]["frozen_at"],
        "historical_result_id": intake["historical_result_id"], "historical_intake": intake}, "review": None, "terminal": False,
        "historical_intake_id": intake["intake_id"], "historical_authentication_status": intake["historical_authentication_status"],
        "execution_authorized": False, "parent_completion_granted": False, "historical_review_inherited": False,
        "review_write_operation": "historical_result_review", "historical_review_ids": sorted(row["review_id"] for row in reviews),
        "historical_review_history_ids": sorted(row["review_id"] for row in history), "historical_review_set_sha256": review_set_digest(head_pins)}
    if len(reviews) > 1:
        value["historical_review_state"] = "AWAITING_EXACT_SET_REVIEW_SYNTHESIS"
    elif reviews:
        row = {**reviews[0], "reviewed_at": reviews[0]["created_at"]}
        value.update(review=row, terminal=row["disposition"] in {"ACCEPTED", "REJECTED"}, terminal_scope="TASK",
            portfolio_continuation=row["task_scope_followup"], state="TERMINAL" if row["disposition"] in {"ACCEPTED", "REJECTED"} else "RETURN_TO_EXECUTION")
    return value


def audit(root: Path) -> list[str]:
    errors = []
    for directory, validator in ((INTAKE_ROOT, validate_intake), (REVIEW_ROOT, validate_review)):
        for path in (root / directory).glob("*/*.json"):
            try:
                validator(json.loads(path.read_text()), root=root)
            except Exception as exc:
                errors.append(f"{path.relative_to(root)}: {exc}")
    return errors
