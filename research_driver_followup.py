#!/usr/bin/env python3
"""Driver-review -> automatic follow-up taskset barrier.

A Driver review is a semantic checkpoint, not a place where the control loop may
silently stop.  Reviews created after the policy cutover must be followed by one
immutable follow-up packet.  The packet either:

* pins one or more post-review immutable task publications (the normal case); or
* proves that the canonical parent Objective is already CLOSED.

The packet explicitly evaluates formalization, external prior-art/duplication,
independent replication, integration/tool harvest, adversarial audit, and
mathematical-continuation gates.  A terminal review cannot become terminal
runtime authority while its required follow-up packet is missing or invalid.

Historical reviews before the cutover remain immutable compatibility evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from control_plane import research_result_records_impl as result_impl
import research_objective_records
from tools import research_task_records, research_taskbook

ROOT = Path(__file__).resolve().parent
PACKET_ROOT = ROOT / "research_driver_followups"

SCHEMA = "ENTERPRISE_MATH_DRIVER_REVIEW_FOLLOWUP_V1"
POLICY = "AUTO_PUBLISH_TASKSET_OR_PARENT_CLOSE_V1"
# User-directed cutover: reviews at/after 2026-08-27 17:19 Asia/Taipei.
CUTOVER_REVIEWED_AT = "2026-08-27T09:19:00+00:00"

DECISIONS = {"TASK_SET_PUBLISHED", "PARENT_OBJECTIVE_CLOSURE"}
GATE_DECISIONS = {"REQUIRED", "SATISFIED_BY_REVIEWED_RESULT", "NOT_REQUIRED"}
GATES = (
    "MATHEMATICAL_CONTINUATION",
    "LEAN_FORMALIZATION",
    "EXTERNAL_PRIOR_ART_DUPLICATION",
    "INDEPENDENT_REPLICATION",
    "INTEGRATION_OR_TOOL_HARVEST",
    "ADVERSARIAL_AUDIT",
)
TASK_ROLES = {
    "MATHEMATICAL_CONTINUATION",
    "LEAN_FORMALIZATION",
    "EXTERNAL_PRIOR_ART_DUPLICATION",
    "INDEPENDENT_REPLICATION",
    "INTEGRATION_OR_TOOL_HARVEST",
    "ADVERSARIAL_AUDIT",
    "REVISION",
    "PARALLEL_REFERENCE_OR_SYNTHESIS",
    "OTHER",
}
GATE_TO_ROLE = {gate: gate for gate in GATES}
ID_RE = re.compile(r"^[A-Za-z0-9._-]+$")


class DriverFollowupError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise DriverFollowupError(f"{path}: JSON root must be an object")
    return value


def _save_exclusive(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    try:
        with path.open("x", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError as exc:
        raise DriverFollowupError(f"immutable follow-up packet already exists: {path}") from exc


def _parse_time(value: Any, label: str) -> datetime:
    if not isinstance(value, str) or not value.strip():
        raise DriverFollowupError(f"{label} is required")
    try:
        dt = datetime.fromisoformat(value.strip().replace("Z", "+00:00"))
    except ValueError as exc:
        raise DriverFollowupError(f"{label} is not ISO-8601") from exc
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def _now(value: str | None = None) -> str:
    if value:
        return _parse_time(value, "created_at").isoformat()
    return datetime.now(timezone.utc).isoformat()


def _safe(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip() or not ID_RE.fullmatch(value.strip()):
        raise DriverFollowupError(f"{label} is invalid")
    return value.strip()


def packet_id(review_id: str, decision: str, task_publication_ids: list[str]) -> str:
    payload = {
        "review_id": review_id,
        "decision": decision,
        "task_publication_ids": sorted(task_publication_ids),
    }
    return "DFU-" + hashlib.sha256(
        json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")
    ).hexdigest()[:20].upper()


def iter_packets(root: Path = ROOT) -> list[dict[str, Any]]:
    directory = root / "research_driver_followups"
    if not directory.exists():
        return []
    out: list[dict[str, Any]] = []
    for path in sorted(directory.glob("*/*.json")):
        value = _load(path)
        value["_path"] = path.relative_to(root).as_posix()
        out.append(value)
    return out


def packet_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for item in iter_packets(root):
        rid = item.get("review_id")
        if not isinstance(rid, str) or not rid:
            raise DriverFollowupError(f"{item.get('_path', '<packet>')}: missing review_id")
        if rid in out:
            raise DriverFollowupError(f"multiple follow-up packets for review {rid}")
        out[rid] = item
    return out


def review_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for item in result_impl.iter_reviews(root):
        rid = item.get("review_id")
        if isinstance(rid, str) and rid:
            if rid in out:
                raise DriverFollowupError(f"duplicate review_id: {rid}")
            out[rid] = item
    return out


def result_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    return result_impl.result_map(root)


def publication_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for item in research_task_records.iter_records(root):
        pid = item.get("publication_id")
        if isinstance(pid, str) and pid:
            if pid in out:
                raise DriverFollowupError(f"duplicate publication_id: {pid}")
            out[pid] = item
    return out


def review_requires_followup(review: dict[str, Any]) -> bool:
    reviewed = _parse_time(review.get("reviewed_at"), "reviewed_at")
    cutover = _parse_time(CUTOVER_REVIEWED_AT, "cutover")
    return reviewed >= cutover


def _source_parent_objective(
    review: dict[str, Any], result: dict[str, Any], root: Path
) -> str:
    pid = review.get("publication_id")
    for publication in research_task_records.iter_records(root):
        if publication.get("publication_id") == pid:
            if publication.get("task_id") != result.get("task_id"):
                raise DriverFollowupError("source publication task differs from reviewed result")
            parent = publication.get("parent_objective_id")
            if not isinstance(parent, str) or not parent.strip():
                raise DriverFollowupError("source publication has no parent_objective_id")
            return parent.strip()
    raise DriverFollowupError(f"review source publication is unavailable: {pid}")


def _objective_head(parent_objective_id: str, root: Path) -> dict[str, Any] | None:
    return research_objective_records.current_head(parent_objective_id, root)


def _gate_map(value: Any) -> dict[str, dict[str, Any]]:
    if not isinstance(value, list) or len(value) != len(GATES):
        raise DriverFollowupError(
            f"gate_decisions must contain exactly {len(GATES)} canonical gate rows"
        )
    out: dict[str, dict[str, Any]] = {}
    for row in value:
        if not isinstance(row, dict):
            raise DriverFollowupError("gate_decisions rows must be objects")
        gate = row.get("gate")
        if gate not in GATES:
            raise DriverFollowupError(f"unknown follow-up gate: {gate}")
        if gate in out:
            raise DriverFollowupError(f"duplicate follow-up gate: {gate}")
        decision = row.get("decision")
        if decision not in GATE_DECISIONS:
            raise DriverFollowupError(f"{gate}: invalid gate decision")
        reason = row.get("reason")
        if not isinstance(reason, str) or not reason.strip():
            raise DriverFollowupError(f"{gate}: nonempty reason is required")
        evidence = row.get("evidence_refs", [])
        if (
            not isinstance(evidence, list)
            or any(not isinstance(item, str) or not item.strip() for item in evidence)
            or len(evidence) != len(set(evidence))
        ):
            raise DriverFollowupError(f"{gate}: evidence_refs must be a unique string list")
        if decision == "SATISFIED_BY_REVIEWED_RESULT" and not evidence:
            raise DriverFollowupError(
                f"{gate}: SATISFIED_BY_REVIEWED_RESULT requires evidence_refs"
            )
        out[gate] = {
            "gate": gate,
            "decision": decision,
            "reason": reason.strip(),
            "evidence_refs": evidence,
        }
    if set(out) != set(GATES):
        raise DriverFollowupError("gate_decisions do not cover the exact canonical gate set")
    return out


def _forced_gate_rules(
    review: dict[str, Any], result: dict[str, Any], gates: dict[str, dict[str, Any]]
) -> None:
    disposition = review.get("disposition")
    destination = review.get("destination_class")

    if disposition == "ACCEPTED":
        if gates["EXTERNAL_PRIOR_ART_DUPLICATION"]["decision"] == "NOT_REQUIRED":
            raise DriverFollowupError(
                "ACCEPTED review requires EXTERNAL_PRIOR_ART_DUPLICATION to be "
                "REQUIRED or SATISFIED_BY_REVIEWED_RESULT"
            )

    if disposition == "ACCEPTED" and destination == "L4":
        if gates["LEAN_FORMALIZATION"]["decision"] == "NOT_REQUIRED":
            raise DriverFollowupError(
                "ACCEPTED L4 review requires LEAN_FORMALIZATION to be REQUIRED "
                "or SATISFIED_BY_REVIEWED_RESULT"
            )

    if disposition == "ACCEPTED" and destination == "FOUNDATION":
        if gates["EXTERNAL_PRIOR_ART_DUPLICATION"]["decision"] == "NOT_REQUIRED":
            raise DriverFollowupError(
                "Foundation-directed acceptance cannot skip external prior-art/duplication review"
            )

    if disposition == "ACCEPTED" and destination == "TOOL":
        if gates["INTEGRATION_OR_TOOL_HARVEST"]["decision"] == "NOT_REQUIRED":
            raise DriverFollowupError(
                "TOOL destination requires integration/tool-harvest gate"
            )

    if disposition == "REQUEST_REPLICATION":
        if gates["INDEPENDENT_REPLICATION"]["decision"] != "REQUIRED":
            raise DriverFollowupError(
                "REQUEST_REPLICATION disposition requires an INDEPENDENT_REPLICATION task"
            )

    method = result.get("method_harvest")
    if method in {"GLOBAL_TOOL_FAMILY", "GLOBAL_SUBTOOL", "DOMAIN_FACADE", "DOMAIN_OPERATOR"}:
        if gates["INTEGRATION_OR_TOOL_HARVEST"]["decision"] == "NOT_REQUIRED":
            raise DriverFollowupError(
                "tool-bearing result cannot skip INTEGRATION_OR_TOOL_HARVEST gate"
            )


def _task_rows(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        raise DriverFollowupError("task_publications must be a list")
    out: list[dict[str, Any]] = []
    seen: set[str] = set()
    for row in value:
        if not isinstance(row, dict):
            raise DriverFollowupError("task_publications rows must be objects")
        pid = _safe(row.get("publication_id"), "task publication_id")
        if pid in seen:
            raise DriverFollowupError(f"duplicate task publication in follow-up packet: {pid}")
        seen.add(pid)
        role = row.get("task_role")
        if role not in TASK_ROLES:
            raise DriverFollowupError(f"{pid}: invalid task_role")
        task_id = _safe(row.get("task_id"), "task_id")
        out.append({"task_id": task_id, "publication_id": pid, "task_role": role})
    return out


def build_packet(
    *,
    review_id: str,
    decision: str,
    gate_decisions: list[dict[str, Any]],
    task_publications: list[dict[str, Any]],
    driver_id: str,
    created_at: str,
    root: Path = ROOT,
) -> dict[str, Any]:
    reviews = review_map(root)
    results = result_map(root)
    review = reviews.get(review_id)
    if review is None:
        raise DriverFollowupError(f"unknown review_id: {review_id}")
    if not review_requires_followup(review):
        raise DriverFollowupError("historical pre-cutover review does not require a follow-up packet")
    result = results.get(str(review.get("result_id")))
    if result is None:
        raise DriverFollowupError("review references unknown result")
    if driver_id.strip().upper() != str(review.get("driver_id", "")).strip().upper():
        raise DriverFollowupError("follow-up driver_id must equal the reviewed Driver")
    if decision not in DECISIONS:
        raise DriverFollowupError("invalid follow-up decision")

    gates = _gate_map(gate_decisions)
    _forced_gate_rules(review, result, gates)
    rows = _task_rows(task_publications)
    parent = _source_parent_objective(review, result, root)
    recommendation = result.get("next_control_plane_recommendation")
    if not isinstance(recommendation, str) or not recommendation.strip():
        raise DriverFollowupError("reviewed result lacks next_control_plane_recommendation")

    pids = [row["publication_id"] for row in rows]
    value = {
        "schema": SCHEMA,
        "policy": POLICY,
        "packet_id": packet_id(review_id, decision, pids),
        "review_id": review_id,
        "result_id": result["result_id"],
        "task_id": result["task_id"],
        "source_publication_id": result["publication_id"],
        "driver_id": str(review["driver_id"]).strip().upper(),
        "review_disposition": review.get("disposition"),
        "review_destination_class": review.get("destination_class"),
        "parent_objective_id": parent,
        "source_next_control_plane_recommendation": recommendation,
        "decision": decision,
        "gate_decisions": [gates[name] for name in GATES],
        "task_publications": rows,
        "created_at": created_at,
        "working_truth_granted": False,
        "foundation_authority_granted": False,
        "canonical_promotion_granted": False,
    }
    return value


def validate_packet(packet: dict[str, Any], root: Path = ROOT) -> None:
    if packet.get("schema") != SCHEMA:
        raise DriverFollowupError("wrong follow-up packet schema")
    if packet.get("policy") != POLICY:
        raise DriverFollowupError("wrong follow-up policy")

    review_id = _safe(packet.get("review_id"), "review_id")
    reviews = review_map(root)
    results = result_map(root)
    publications = publication_map(root)
    review = reviews.get(review_id)
    if review is None:
        raise DriverFollowupError("follow-up packet references unknown review")
    if not review_requires_followup(review):
        raise DriverFollowupError("follow-up packet may not retroactively govern a legacy review")

    result = results.get(str(review.get("result_id")))
    if result is None:
        raise DriverFollowupError("reviewed result is unavailable")
    if packet.get("result_id") != result.get("result_id"):
        raise DriverFollowupError("packet result_id mismatch")
    if packet.get("task_id") != result.get("task_id"):
        raise DriverFollowupError("packet task_id mismatch")
    if packet.get("source_publication_id") != result.get("publication_id"):
        raise DriverFollowupError("packet source publication mismatch")
    if str(packet.get("driver_id", "")).strip().upper() != str(review.get("driver_id", "")).strip().upper():
        raise DriverFollowupError("packet Driver differs from review Driver")
    if packet.get("review_disposition") != review.get("disposition"):
        raise DriverFollowupError("packet review disposition drift")
    if packet.get("review_destination_class") != review.get("destination_class"):
        raise DriverFollowupError("packet review destination drift")

    parent = _source_parent_objective(review, result, root)
    if packet.get("parent_objective_id") != parent:
        raise DriverFollowupError("packet parent Objective differs from source task")

    recommendation = result.get("next_control_plane_recommendation")
    if packet.get("source_next_control_plane_recommendation") != recommendation:
        raise DriverFollowupError(
            "Driver follow-up packet must consume the exact result next_control_plane_recommendation"
        )

    gates = _gate_map(packet.get("gate_decisions"))
    _forced_gate_rules(review, result, gates)
    rows = _task_rows(packet.get("task_publications"))
    decision = packet.get("decision")
    if decision not in DECISIONS:
        raise DriverFollowupError("invalid follow-up decision")

    created = _parse_time(packet.get("created_at"), "packet created_at")
    reviewed = _parse_time(review.get("reviewed_at"), "reviewed_at")
    if created < reviewed:
        raise DriverFollowupError("follow-up packet predates its Driver review")

    required_roles = {
        GATE_TO_ROLE[gate]
        for gate, row in gates.items()
        if row["decision"] == "REQUIRED"
    }
    actual_roles = {row["task_role"] for row in rows}

    if decision == "TASK_SET_PUBLISHED":
        if not rows:
            raise DriverFollowupError("TASK_SET_PUBLISHED requires at least one task publication")
        missing = sorted(required_roles - actual_roles)
        if missing:
            raise DriverFollowupError(
                f"required follow-up gates have no matching published task role: {missing}"
            )
    else:
        if rows:
            raise DriverFollowupError("PARENT_OBJECTIVE_CLOSURE cannot carry task publications")
        if required_roles:
            raise DriverFollowupError(
                "PARENT_OBJECTIVE_CLOSURE cannot leave REQUIRED follow-up gates"
            )
        head = _objective_head(parent, root)
        if head is None or head.get("objective_status") != "CLOSED":
            raise DriverFollowupError(
                "no-task exception is valid only after canonical parent Objective head is CLOSED"
            )

    for row in rows:
        publication = publications.get(row["publication_id"])
        if publication is None:
            raise DriverFollowupError(
                f"follow-up publication does not exist: {row['publication_id']}"
            )
        if publication.get("task_id") != row["task_id"]:
            raise DriverFollowupError(
                f"{row['publication_id']}: packet task_id differs from publication"
            )
        if publication.get("parent_objective_id") != parent:
            raise DriverFollowupError(
                f"{row['publication_id']}: follow-up task left the reviewed parent Objective"
            )
        if publication.get("publisher_role") != "RESEARCH_DRIVER":
            raise DriverFollowupError(
                f"{row['publication_id']}: automatic review follow-up must be Driver-published"
            )
        if str(publication.get("publisher_id", "")).strip().upper() != str(review.get("driver_id", "")).strip().upper():
            raise DriverFollowupError(
                f"{row['publication_id']}: follow-up task publisher is not the reviewing Driver"
            )
        published = _parse_time(publication.get("published_at"), "published_at")
        if published < reviewed:
            raise DriverFollowupError(
                f"{row['publication_id']}: follow-up task was published before the review"
            )
        taskbook_path = publication.get("taskbook_path")
        if not isinstance(taskbook_path, str) or not (root / taskbook_path).exists():
            raise DriverFollowupError(
                f"{row['publication_id']}: follow-up taskbook missing"
            )
        if research_task_records.taskbook_blob(root / taskbook_path) != publication.get("taskbook_blob_sha1"):
            raise DriverFollowupError(
                f"{row['publication_id']}: follow-up taskbook blob drift"
            )

    expected_id = packet_id(review_id, str(decision), [row["publication_id"] for row in rows])
    if packet.get("packet_id") != expected_id:
        raise DriverFollowupError("follow-up packet_id mismatch")
    if packet.get("working_truth_granted") is not False:
        raise DriverFollowupError("follow-up packet cannot grant Working Truth")
    if packet.get("foundation_authority_granted") is not False:
        raise DriverFollowupError("follow-up packet cannot grant Foundation authority")
    if packet.get("canonical_promotion_granted") is not False:
        raise DriverFollowupError("follow-up packet cannot grant canonical promotion")


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        packets = packet_map(root)
        reviews = review_map(root)
    except Exception as exc:
        return [str(exc)]

    for rid, review in reviews.items():
        try:
            required = review_requires_followup(review)
        except Exception as exc:
            errors.append(f"{rid}: cannot evaluate follow-up cutover: {exc}")
            continue
        packet = packets.get(rid)
        if required and packet is None:
            errors.append(
                f"{rid}: post-cutover Driver review has no automatic follow-up taskset/closure packet"
            )
        if not required and packet is not None:
            errors.append(
                f"{rid}: legacy pre-cutover review must not be retroactively governed by a packet"
            )

    for rid, packet in packets.items():
        prefix = packet.get("_path", rid)
        if rid not in reviews:
            errors.append(f"{prefix}: packet references unknown review")
            continue
        try:
            validate_packet(packet, root)
        except Exception as exc:
            errors.append(f"{prefix}: {exc}")
    return errors


def state_for_review(review_id: str, root: Path = ROOT) -> dict[str, Any]:
    review = review_map(root).get(review_id)
    if review is None:
        return {
            "review_id": review_id,
            "required": True,
            "ready": False,
            "state": "UNKNOWN_REVIEW",
            "packet": None,
        }
    try:
        required = review_requires_followup(review)
    except Exception as exc:
        return {
            "review_id": review_id,
            "required": True,
            "ready": False,
            "state": "FOLLOWUP_POLICY_ERROR",
            "error": str(exc),
            "packet": None,
        }
    if not required:
        return {
            "review_id": review_id,
            "required": False,
            "ready": True,
            "state": "LEGACY_PRE_CUTOVER",
            "packet": None,
        }
    packet = packet_map(root).get(review_id)
    if packet is None:
        return {
            "review_id": review_id,
            "required": True,
            "ready": False,
            "state": "AWAITING_FOLLOWUP_TASKSET_PUBLICATION",
            "packet": None,
        }
    try:
        validate_packet(packet, root)
    except Exception as exc:
        return {
            "review_id": review_id,
            "required": True,
            "ready": False,
            "state": "FOLLOWUP_PACKET_INVALID",
            "error": str(exc),
            "packet": packet,
        }
    return {
        "review_id": review_id,
        "required": True,
        "ready": True,
        "state": (
            "FOLLOWUP_TASKSET_READY"
            if packet.get("decision") == "TASK_SET_PUBLISHED"
            else "PARENT_OBJECTIVE_CLOSED"
        ),
        "packet": packet,
    }


def _taskbook_text(spec: dict[str, Any], parent: str) -> str:
    required = (
        "task_id",
        "title",
        "task_role",
        "frontier",
        "next_action",
        "research_value",
        "mother_question",
        "frozen_inputs_and_scope",
        "hard_target_and_required_outputs",
        "research_value_to_preserve",
        "success_kill_and_return_criteria",
    )
    for field in required:
        if not isinstance(spec.get(field), str) or not str(spec[field]).strip():
            raise DriverFollowupError(f"task spec {field} is required")
    role = spec["task_role"]
    if role not in TASK_ROLES:
        raise DriverFollowupError(f"task spec has invalid task_role: {role}")
    lineage = str(spec.get("task_lineage") or "CONTINUATION").upper()
    if lineage not in {"NEW_DIRECTION", "CONTINUATION", "REPLAY", "INTEGRATION", "MAINTENANCE"}:
        raise DriverFollowupError("task spec has invalid task_lineage")
    parent_task_id = spec.get("parent_task_id")
    successor_gate = spec.get("successor_gate")
    if lineage == "CONTINUATION":
        if not isinstance(parent_task_id, str) or not parent_task_id.strip():
            raise DriverFollowupError("CONTINUATION follow-up requires parent_task_id")
        if not isinstance(successor_gate, dict):
            raise DriverFollowupError("CONTINUATION follow-up requires successor_gate")
    else:
        successor_gate = None

    meta = {
        "task_id": spec["task_id"].strip(),
        "title": spec["title"].strip(),
        "kind": str(spec.get("kind") or "RESEARCH").upper(),
        "owner": str(spec.get("owner") or "taskbook/unassigned"),
        "base_state": "READY",
        "priority": str(spec.get("priority") or "P1").upper(),
        "leverage": str(spec.get("leverage") or "HIGH").upper(),
        "frontier": spec["frontier"].strip(),
        "next_action": spec["next_action"].strip(),
        "dependencies": spec.get("dependencies", []),
        "source_refs": spec.get("source_refs", []),
        "evidence_status": "DRIVER_REVIEW_FOLLOWUP_V1",
        "last_progress_ref": None,
        "last_progress_at": None,
        "hard_block": spec.get("hard_block"),
        "tags": list(dict.fromkeys([role, "DRIVER_AUTO_FOLLOWUP"] + list(spec.get("tags", [])))),
        "claim_lease_minutes": int(spec.get("claim_lease_minutes", 120)),
        "created_by_role": "RESEARCH_DRIVER",
        "task_authority": "PENDING_PUBLICATION",
        "publication_contract": research_task_records.TASKBOOK_PUBLICATION_CONTRACT,
        "publication_template": research_task_records.TASKBOOK_TEMPLATE,
        "registry_key": spec["task_id"].strip(),
        "parent_objective_id": parent,
        "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
        "final_response_identity_policy": "INHERIT_GLOBAL",
        "identity_lane": str(spec.get("identity_lane") or role),
        "origin_kind": str(spec.get("origin_kind") or "DRIVER_ROADMAP"),
        "task_lineage": lineage,
        "parent_task_id": parent_task_id,
        "successor_gate": successor_gate,
        "policy_review": {
            "policy_set": "research_taskbook_policy.json",
            "policy_digest": research_taskbook.policy_digest(ROOT),
            "review_state": "PENDING_POLICY_REVIEW",
            "temporary_overrides": [],
        },
    }
    body = f"""# {spec['title'].strip()}

Status: `READY / DRIVER REVIEW FOLLOW-UP / PENDING IMMUTABLE PUBLICATION`

## 0. Mother question

{spec['mother_question'].strip()}

## 1. Frozen inputs and scope

{spec['frozen_inputs_and_scope'].strip()}

## 2. Hard target and required outputs

{spec['hard_target_and_required_outputs'].strip()}

## 3. Research value to preserve

{spec['research_value_to_preserve'].strip()}

## 4. Success, kill, and return criteria

{spec['success_kill_and_return_criteria'].strip()}
"""
    return research_taskbook.render_taskbook(meta, body)


def _preflight_taskbook(text: str, root: Path) -> None:
    with tempfile.TemporaryDirectory() as td:
        path = Path(td) / "task.md"
        path.write_text(text, encoding="utf-8")
        meta, body = research_taskbook.split_taskbook(text)
        body_errors = research_task_records.validate_body(body)
        if body_errors:
            raise DriverFollowupError("; ".join(body_errors))
        research_task_records.prepare_taskbook(
            path,
            publisher_role="RESEARCH_DRIVER",
            parent_objective_id=meta["parent_objective_id"],
            root=root,
        )


def materialize(
    *,
    review_id: str,
    spec: dict[str, Any],
    created_at: str | None = None,
    root: Path = ROOT,
) -> dict[str, Any]:
    review = review_map(root).get(review_id)
    if review is None:
        raise DriverFollowupError(f"unknown review_id: {review_id}")
    if not review_requires_followup(review):
        raise DriverFollowupError("review predates automatic follow-up policy cutover")
    result = result_map(root).get(str(review.get("result_id")))
    if result is None:
        raise DriverFollowupError("reviewed result is unavailable")
    parent = _source_parent_objective(review, result, root)
    decision = spec.get("decision")
    gates = spec.get("gate_decisions")
    task_specs = spec.get("tasks", [])
    if decision not in DECISIONS:
        raise DriverFollowupError("spec decision is invalid")
    if not isinstance(task_specs, list):
        raise DriverFollowupError("spec tasks must be a list")

    normalized_gates = _gate_map(gates)
    _forced_gate_rules(review, result, normalized_gates)

    if decision == "PARENT_OBJECTIVE_CLOSURE":
        if task_specs:
            raise DriverFollowupError("parent closure spec cannot include tasks")
        head = _objective_head(parent, root)
        if head is None or head.get("objective_status") != "CLOSED":
            raise DriverFollowupError(
                "parent Objective must already be canonically CLOSED before no-task exception"
            )
        if any(row["decision"] == "REQUIRED" for row in normalized_gates.values()):
            raise DriverFollowupError("parent closure cannot leave REQUIRED gates")
        packet = build_packet(
            review_id=review_id,
            decision=decision,
            gate_decisions=[normalized_gates[name] for name in GATES],
            task_publications=[],
            driver_id=str(review["driver_id"]),
            created_at=_now(created_at),
            root=root,
        )
        out = root / "research_driver_followups" / review_id / f"{packet['packet_id']}.json"
        _save_exclusive(out, packet)
        errors = audit(root)
        if errors:
            raise DriverFollowupError(
                "follow-up packet created but audit failed: " + "; ".join(errors)
            )
        return {**packet, "record_path": out.relative_to(root).as_posix()}

    if not task_specs:
        raise DriverFollowupError("TASK_SET_PUBLISHED requires one or more task specs")

    existing_paths: set[Path] = set()
    prepared: list[tuple[dict[str, Any], str, Path]] = []
    suffix = review_id.replace("DR-", "").lower()[:8]
    for task_spec in task_specs:
        if not isinstance(task_spec, dict):
            raise DriverFollowupError("each task spec must be an object")
        text = _taskbook_text(task_spec, parent)
        _preflight_taskbook(text, root)
        task_id = _safe(task_spec.get("task_id"), "task_id")
        filename = str(task_spec.get("taskbook_filename") or f"{task_id}_{suffix}.md")
        if "/" in filename or "\\" in filename or not filename.endswith(".md"):
            raise DriverFollowupError("taskbook_filename must be one repository-local .md filename")
        path = root / "research_tasks" / filename
        if path in existing_paths or path.exists():
            raise DriverFollowupError(f"follow-up taskbook path already exists: {path}")
        existing_paths.add(path)
        prepared.append((task_spec, text, path))

    published_rows: list[dict[str, Any]] = []
    for task_spec, text, path in prepared:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        meta = research_task_records.prepare_taskbook(
            path,
            publisher_role="RESEARCH_DRIVER",
            parent_objective_id=parent,
            root=root,
        )
        supersedes = task_spec.get("supersedes_publication_id")
        record = research_task_records.build_record(
            meta,
            path=path,
            publisher_role="RESEARCH_DRIVER",
            publisher_id=str(review["driver_id"]),
            research_value=str(task_spec["research_value"]).strip(),
            published_at=_now(created_at),
            supersedes_publication_id=supersedes,
            root=root,
        )
        record_path = research_task_records.record_path(
            root, record["task_id"], record["publication_id"]
        )
        research_task_records._save_json_exclusive(record_path, record)
        published_rows.append(
            {
                "task_id": record["task_id"],
                "publication_id": record["publication_id"],
                "task_role": task_spec["task_role"],
            }
        )

    publication_errors = research_task_records.audit(root)
    if publication_errors:
        raise DriverFollowupError(
            "follow-up task publication(s) created but task audit failed: "
            + "; ".join(publication_errors)
        )

    packet = build_packet(
        review_id=review_id,
        decision="TASK_SET_PUBLISHED",
        gate_decisions=[normalized_gates[name] for name in GATES],
        task_publications=published_rows,
        driver_id=str(review["driver_id"]),
        created_at=_now(created_at),
        root=root,
    )
    out = root / "research_driver_followups" / review_id / f"{packet['packet_id']}.json"
    _save_exclusive(out, packet)
    errors = audit(root)
    if errors:
        raise DriverFollowupError(
            "follow-up packet created but audit failed: " + "; ".join(errors)
        )
    return {**packet, "record_path": out.relative_to(root).as_posix()}


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Enterprise Math Driver-review automatic follow-up taskset barrier"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("audit")

    state = sub.add_parser("state")
    state.add_argument("--review-id", required=True)

    materialize_parser = sub.add_parser("materialize")
    materialize_parser.add_argument("--review-id", required=True)
    materialize_parser.add_argument("--spec", required=True)
    materialize_parser.add_argument("--created-at")

    args = parser.parse_args()
    if args.command == "audit":
        errors = audit()
        if errors:
            for error in errors:
                print("ERROR:", error)
            return 1
        governed = sum(
            1 for review in review_map().values() if review_requires_followup(review)
        )
        print(
            f"PASS: Driver review follow-up barrier valid "
            f"({governed} post-cutover review(s), {len(iter_packets())} packet(s))."
        )
        return 0
    if args.command == "state":
        print(
            json.dumps(
                state_for_review(args.review_id),
                ensure_ascii=False,
                indent=2,
                sort_keys=True,
            )
        )
        return 0

    spec_path = Path(args.spec)
    if not spec_path.is_absolute():
        spec_path = ROOT / spec_path
    if not spec_path.exists():
        raise DriverFollowupError(f"follow-up spec not found: {spec_path}")
    spec = _load(spec_path)
    result = materialize(
        review_id=args.review_id,
        spec=spec,
        created_at=args.created_at,
        root=ROOT,
    )
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except DriverFollowupError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
