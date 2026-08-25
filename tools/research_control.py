#!/usr/bin/env python3
"""Cross-layer validator for Enterprise Math Research Control State Machine V1.

This module does not reduce Scheduler events and does not replace any existing
submachine. It validates the composition: semantic/evidence/routing/liveness
state around Scheduler V2 and validates the extra evidence carried by new V2
APPROVE/REVIEW/CLAIM/ADOPT/ORPHAN events.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import sys
from datetime import datetime
from typing import Any

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_SPEC = ROOT / "research_control_state_machine.json"
V2_SCHEMA = "ENTERPRISE_MATH_SCHEDULER_EVENT_V2"


def load_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def nonempty(value: Any) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict, tuple, set)):
        return bool(value)
    return value is not None


def _enum(spec: dict[str, Any], section: str, field: str) -> set[str]:
    value = spec["state_vector"][section][field]
    return set(value) if isinstance(value, list) else set()


def validate_spec(spec: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if spec.get("schema") != "ENTERPRISE_MATH_RESEARCH_CONTROL_STATE_MACHINE_V1":
        return ["unexpected control-state schema"]
    required_sections = {"actor", "object", "runtime", "conversation", "information", "evidence", "routing", "parent"}
    missing = required_sections - set(spec.get("state_vector", {}))
    if missing:
        errors.append("missing state-vector sections: " + ", ".join(sorted(missing)))
    required_profiles = {
        "STANDARD_RESEARCH",
        "FREE_CANDIDATE_AUDIT",
        "INDEPENDENT_AUDIT",
        "AXIOM_ADMISSION_AUDIT",
        "FORMALIZATION",
        "FOUNDATION_DISPOSITION",
        "INTEGRATION",
        "BENCHMARK",
        "MATHEMATICAL_PROMOTION",
        "GOVERNANCE_MAINTENANCE",
    }
    if not required_profiles <= set(spec.get("control_profiles", [])):
        errors.append("control_profiles do not cover all current control classes")
    intake = spec.get("pre_execution_reconciliation_contract", {})
    if intake.get("required_before_new_execution_generation") is not True:
        errors.append("new execution generation must require durable-frontier reconciliation")
    if set(intake.get("classification", [])) != {"VERIFIED_COMPLETE", "IN_PROGRESS_RECOVERABLE", "UNFINISHED", "NEVER_STARTED"}:
        errors.append("pre-execution reconciliation must use the canonical four-way frontier classification")
    recovery = spec.get("conversation_recovery_contract", {})
    if recovery.get("stale_after_minutes_without_verifiable_action") != 10:
        errors.append("conversation recovery must use the canonical 10-minute stale threshold")
    if recovery.get("scheduler_release_event") != "ORPHAN" or recovery.get("scheduler_resume_event") != "ADOPT":
        errors.append("conversation recovery must bridge through Scheduler ORPHAN -> ADOPT")
    if recovery.get("durable_frontier_required_for_recoverable_takeover") is not True:
        errors.append("recoverable conversation takeover must require a durable frontier")
    return errors


def validate_snapshot(snapshot: dict[str, Any], spec: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for section in ("actor", "object", "runtime", "conversation", "information", "evidence", "routing", "parent"):
        if not isinstance(snapshot.get(section), dict):
            errors.append(f"missing section: {section}")
    if errors:
        return errors

    actor = snapshot["actor"]
    obj = snapshot["object"]
    runtime = snapshot["runtime"]
    conv = snapshot["conversation"]
    info = snapshot["information"]
    ev = snapshot["evidence"]
    route = snapshot["routing"]
    parent = snapshot["parent"]

    enum_fields = {
        "actor": (actor, ("role", "mode", "identity_state")),
        "runtime": (runtime, ("scheduler_state", "dispatch_state", "pre_math_gate")),
        "conversation": (conv, ("liveness", "recovery_class")),
        "information": (info, ("firewall", "freeze_state", "source_exposure")),
        "evidence": (
            ev,
            (
                "source_status",
                "independent_status",
                "driver_verdict",
                "axiom_admission_status",
                "formalization_status",
                "foundation_status",
                "integration_status",
                "benchmark_status",
                "promotion_status",
                "canonical_status",
            ),
        ),
        "routing": (route, ("working_truth", "method_harvest", "successor_gate", "route_disposition")),
        "parent": (parent, ("objective", "completion_basis")),
    }
    for section, (payload, fields) in enum_fields.items():
        for field in fields:
            allowed = _enum(spec, section, field)
            if payload.get(field) not in allowed:
                errors.append(f"{section}.{field}: invalid value {payload.get(field)!r}")

    generation = conv.get("generation")
    if not isinstance(generation, int) or generation < 0:
        errors.append("conversation.generation must be a nonnegative integer")
    last_verified = conv.get("last_verified_action_at")
    if nonempty(last_verified):
        try:
            datetime.fromisoformat(str(last_verified).replace("Z", "+00:00"))
        except ValueError:
            errors.append("conversation.last_verified_action_at must be ISO-8601 or null")

    liveness = conv.get("liveness")
    recovery_class = conv.get("recovery_class")
    durable_frontier = conv.get("durable_frontier_ref")
    takeover_ref = conv.get("takeover_ref")
    if liveness == "ACTIVE" and recovery_class != "NONE":
        errors.append("active conversation must not carry a stale recovery classification")
    if liveness == "NOT_APPLICABLE" and recovery_class != "NONE":
        errors.append("conversation recovery_class must be NONE when liveness is NOT_APPLICABLE")
    if liveness in {"STALE", "RECOVERING", "RECOVERED"} and recovery_class == "NONE":
        errors.append("stale/recovering/recovered conversation requires an explicit recovery classification")
    if liveness in {"STALE", "RECOVERING"} and not nonempty(durable_frontier):
        errors.append("stale/recovering conversation requires a durable frontier")
    if recovery_class in {"IN_PROGRESS_RECOVERABLE", "UNFINISHED"} and not nonempty(durable_frontier):
        errors.append("recoverable/unfinished predecessor requires durable_frontier_ref")
    if liveness == "RECOVERING" and not nonempty(takeover_ref):
        errors.append("recovering conversation requires takeover_ref")
    if recovery_class == "VERIFIED_COMPLETE" and runtime.get("dispatch_state") in {"LEASED", "NEEDS_DISPATCH", "ORPHAN_RECOVERY"}:
        errors.append("VERIFIED_COMPLETE recovery forbids duplicate task execution or redispatch")
    if liveness == "RECOVERED" and recovery_class in {"IN_PROGRESS_RECOVERABLE", "UNFINISHED", "NEVER_STARTED"} and not nonempty(takeover_ref):
        errors.append("recovered execution requires takeover_ref")

    profile = obj.get("control_profile")
    if profile not in set(spec.get("control_profiles", [])):
        errors.append(f"object.control_profile: invalid value {profile!r}")

    role_mode = {
        "RESEARCH_DRIVER": {"CONTROL_PLANE"},
        "FOUNDATION_STEWARD": {"VERIFY_OR_MAINTAIN"},
        "RESEARCHER": {"FREE_AXIOM_DISCOVERY", "TASK_RESEARCH"},
    }
    if actor.get("mode") not in role_mode.get(actor.get("role"), set()):
        errors.append("actor role/mode mismatch")
    if actor.get("identity_state") == "UNRESOLVED" and runtime.get("scheduler_state") not in {"NONE", "DRAFT", "REVIEW_PENDING"}:
        errors.append("active work cannot proceed with unresolved role identity")

    if runtime.get("pre_math_gate") == "REQUIRED_UNSATISFIED" and snapshot.get("substantive_math_started") is True:
        errors.append("substantive mathematics cannot start before the task-local pre-math gate is satisfied")

    if ev.get("driver_verdict") in {"ACCEPTED", "NARROWED"}:
        if route.get("method_harvest") == "PENDING":
            errors.append("accepted/narrowed return requires method-harvest classification")
        if route.get("route_disposition") == "PENDING":
            errors.append("accepted/narrowed return requires explicit route disposition")

    if route.get("route_disposition") == "OPEN_CONTINUATION" and route.get("successor_gate") != "SATISFIED":
        errors.append("continuation requires satisfied successor gate")

    if route.get("route_disposition") == "OPEN_INDEPENDENT_REPLICATION_CHILD":
        if runtime.get("scheduler_state") == "HANDOFF_READY":
            errors.append("independent replication cannot be represented as same-task HANDOFF_READY")
        child = route.get("child_task_id")
        if not nonempty(child) or child == obj.get("task_id"):
            errors.append("independent replication requires distinct child_task_id")
        if not nonempty(route.get("child_task_ref")) or not nonempty(route.get("independence_protocol")):
            errors.append("independent replication requires child_task_ref and independence_protocol")

    if profile in {"INDEPENDENT_AUDIT", "FREE_CANDIDATE_AUDIT"}:
        if info.get("firewall") == "NONE":
            errors.append("independent/blind audit requires explicit information firewall classification")
        if ev.get("independent_status") == "CLOSED" and info.get("firewall") in {"FREE_PHASE_A_BLIND", "TASK_BLIND_FORWARD"}:
            if info.get("freeze_state") != "FROZEN" or info.get("source_exposure") != "POST_FREEZE_ONLY":
                errors.append("blind independent closure requires raw freeze before source exposure")
        if snapshot.get("independence_status") == "CLEAN_INDEPENDENT_CONTEXT":
            src_ctx = snapshot.get("source_execution_context")
            exec_ctx = snapshot.get("execution_context")
            if nonempty(src_ctx) and src_ctx == exec_ctx:
                errors.append("clean independent audit requires a distinct execution context")

    if profile == "AXIOM_ADMISSION_AUDIT":
        if info.get("firewall") == "NONE":
            errors.append("axiom-admission audit requires an explicit information firewall/whitelist classification")
        admission = ev.get("axiom_admission_status")
        if admission in {"NOT_APPLICABLE", None}:
            errors.append("axiom-admission audit requires explicit axiom_admission_status")
        if ev.get("canonical_status") != "NONCANONICAL":
            errors.append("axiom-admission research cannot directly canonicalize an axiom")
        if ev.get("foundation_status") in {"ACCEPTED", "NARROWED"}:
            errors.append("axiom-admission research cannot impersonate Foundation Steward disposition")
        if admission in {"ADMIT_RECOMMENDED", "RESTRICTED_ADMISSION_RECOMMENDED"} and ev.get("driver_verdict") in {"ACCEPTED", "NARROWED"}:
            if route.get("route_disposition") != "ROUTE_TO_FOUNDATION":
                errors.append("accepted axiom-admission recommendation must route to Foundation rather than mutate Foundation directly")
            if not nonempty(route.get("route_ref")):
                errors.append("accepted axiom-admission recommendation requires a concrete Foundation route_ref")
            if ev.get("foundation_status") != "PENDING":
                errors.append("accepted axiom-admission recommendation routed to Foundation must remain foundation_status=PENDING until Steward disposition")

    if profile == "FORMALIZATION":
        if ev.get("formalization_status") in {"NOT_APPLICABLE", "NOT_ADMITTED"}:
            errors.append("formalization work cannot start before Driver admission")
        if ev.get("source_status") in {"NONE", "DRAFT", "PROVED_SOURCE", "REPAIR_REQUIRED"}:
            errors.append("formalization requires frozen/corrected accepted source mathematics")
        if ev.get("independent_status") in {"REQUIRED_OPEN", "PARTIAL"}:
            errors.append("formalization cannot start while required independent evidence remains open")
        if snapshot.get("math_change_policy") != "NO_NEW_MATHEMATICS":
            errors.append("formalization profile requires NO_NEW_MATHEMATICS")
        if snapshot.get("statement_mismatch") is True and ev.get("formalization_status") != "RETURN_REQUIRED":
            errors.append("statement/interface mismatch must return to Driver, never silently weaken theorem")

    if ev.get("foundation_status") == "PENDING":
        if ev.get("canonical_status") == "CANONICAL":
            errors.append("pending Foundation disposition blocks canonical mutation")
        if ev.get("formalization_status") in {"ADMITTED", "IN_PROGRESS", "PASS"} and profile == "FOUNDATION_DISPOSITION":
            errors.append("pending Foundation disposition blocks downstream formalization admission")

    if profile == "BENCHMARK" and snapshot.get("performance_claim") == "POSITIVE":
        if ev.get("benchmark_status") != "PASS":
            errors.append("positive performance claim requires benchmark PASS")
        if snapshot.get("fair_baseline") is not True or snapshot.get("cost_accounting") != "COMPLETE":
            errors.append("positive performance claim requires fair baseline and complete cost accounting")
    if profile == "BENCHMARK" and ev.get("benchmark_status") in {"PARTIAL", "NEGATIVE"} and snapshot.get("result_level") == "L4":
        errors.append("partial/negative benchmark cannot carry L4 performance status")

    if profile == "INTEGRATION" and ev.get("integration_status") == "FROZEN":
        if ev.get("source_status") == "REPAIR_REQUIRED":
            errors.append("package cannot freeze while source repair is required")
        if ev.get("independent_status") in {"REQUIRED_OPEN", "PARTIAL"}:
            errors.append("package cannot freeze while required independent evidence remains open")

    if profile == "MATHEMATICAL_PROMOTION":
        if ev.get("promotion_status") in {"IN_ATTEMPT", "MERGED"}:
            for field in ("promotion_attempt_ref", "current_main_snapshot", "conflict_audit_ref", "frozen_head_ref"):
                if not nonempty(snapshot.get(field)):
                    errors.append(f"mathematical promotion requires {field}")
        if ev.get("canonical_status") == "CANONICAL" and ev.get("promotion_status") != "MERGED":
            errors.append("canonical mutation requires completed mathematical promotion gate")

    if parent.get("objective") == "COMPLETE" and parent.get("completion_basis") == "NONE":
        errors.append("parent completion requires an explicit completion basis")
    if parent.get("objective") == "BLOCKED" and parent.get("completion_basis") not in {"UNAVOIDABLE_BLOCK", "PLATFORM_LIMIT"}:
        errors.append("blocked parent requires UNAVOIDABLE_BLOCK or PLATFORM_LIMIT completion basis")
    if parent.get("objective") == "OPEN" and nonempty(parent.get("next_executable_action")) and snapshot.get("terminal_output") is True:
        errors.append("parent objective is open with executable work; final stop would violate active-turn liveness")

    if runtime.get("dispatch_state") in {"BLOCKED", "DORMANT"} and snapshot.get("remote_pending_only") is True and parent.get("objective") == "BLOCKED":
        errors.append("remote/CI pending alone is not a parent HARD_BLOCK")

    return errors


def cross_layer_guard_applies(event: dict[str, Any], spec: dict[str, Any]) -> bool:
    effective = spec.get("cross_layer_effective_at")
    at = event.get("at")
    if not isinstance(effective, str) or not isinstance(at, str):
        return True
    try:
        return datetime.fromisoformat(at) >= datetime.fromisoformat(effective)
    except ValueError:
        return True


def pre_execution_guard_applies(event: dict[str, Any], spec: dict[str, Any]) -> bool:
    effective = spec.get("pre_execution_reconciliation_effective_at") or spec.get("pre_execution_reconciliation_contract", {}).get("effective_at")
    at = event.get("at")
    if not isinstance(effective, str) or not isinstance(at, str):
        return True
    try:
        return datetime.fromisoformat(at) >= datetime.fromisoformat(effective)
    except ValueError:
        return True


def validate_events(events: list[dict[str, Any]], spec: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    contract = spec["review_event_contract"]
    recovery = spec["conversation_recovery_contract"]
    harvest = set(contract["method_harvest_values"])
    evidence_classes = set(contract["evidence_class_values"])
    routes = set(contract["route_disposition_values"])
    for i, event in enumerate(events):
        if event.get("schema") != V2_SCHEMA:
            continue
        kind = event.get("event")
        if not cross_layer_guard_applies(event, spec):
            continue
        if kind == "ORPHAN" and event.get("reason") == recovery.get("scheduler_release_reason"):
            if not nonempty(event.get("evidence_ref")) and not nonempty(event.get("recovery_ref")):
                errors.append(f"event[{i}] stale-conversation ORPHAN requires evidence_ref or recovery_ref")
        if pre_execution_guard_applies(event, spec):
            if kind == "CLAIM":
                if event.get("frontier_class") != "NEVER_STARTED":
                    errors.append(f"event[{i}] CLAIM requires frontier_class=NEVER_STARTED after durable-frontier reconciliation")
                if not nonempty(event.get("frontier_ref")):
                    errors.append(f"event[{i}] CLAIM requires frontier_ref proving pre-execution reconciliation")
            elif kind == "ADOPT":
                if event.get("frontier_class") not in {"IN_PROGRESS_RECOVERABLE", "UNFINISHED"}:
                    errors.append(f"event[{i}] ADOPT requires frontier_class=IN_PROGRESS_RECOVERABLE or UNFINISHED")
                if not nonempty(event.get("recovery_ref")):
                    errors.append(f"event[{i}] ADOPT requires recovery_ref to the durable frontier")
        if kind == "APPROVE":
            if event.get("taskbook_audit") != "PASS":
                errors.append(f"event[{i}] APPROVE requires taskbook_audit=PASS")
            digest = event.get("policy_digest")
            if not isinstance(digest, str) or not digest.startswith("sha256:"):
                errors.append(f"event[{i}] APPROVE requires policy_digest=sha256:...")
            if not nonempty(event.get("taskbook_ref")) or not nonempty(event.get("review_ref")):
                errors.append(f"event[{i}] APPROVE requires taskbook_ref and review_ref")
        if kind == "REVIEW":
            if event.get("verdict") == "REQUEST_INDEPENDENT_REPLICATION":
                errors.append(f"event[{i}] same-task REQUEST_INDEPENDENT_REPLICATION is forbidden; PARK parent and open a distinct child task")
            if event.get("method_harvest") not in harvest:
                errors.append(f"event[{i}] REVIEW requires method_harvest classification")
            if event.get("evidence_class") not in evidence_classes:
                errors.append(f"event[{i}] REVIEW requires evidence_class")
            route = event.get("route_disposition")
            if route not in routes:
                errors.append(f"event[{i}] REVIEW requires route_disposition")
                continue
            verdict = event.get("verdict")
            expected = {
                "RETURN_TO_RESEARCH": {"CONTINUE_SAME_TASK"},
                "ROUTE_TO_FOUNDATION": {"ROUTE_TO_FOUNDATION"},
                "PROMOTION_READY": {"ROUTE_TO_PROMOTION"},
                "REJECT": {"CLOSE"},
            }
            if verdict in expected and route not in expected[verdict]:
                errors.append(f"event[{i}] REVIEW verdict/route_disposition mismatch")
            if route == "OPEN_CONTINUATION" and not nonempty(event.get("successor_gate_ref")):
                errors.append(f"event[{i}] OPEN_CONTINUATION requires successor_gate_ref")
            if route == "OPEN_INDEPENDENT_REPLICATION_CHILD":
                if verdict != "PARK":
                    errors.append(f"event[{i}] independent replication child requires PARK parent review verdict")
                child = event.get("child_task_id")
                if not nonempty(child) or child == event.get("task_id"):
                    errors.append(f"event[{i}] independent replication requires distinct child_task_id")
                for field in ("child_task_ref", "independence_protocol"):
                    if not nonempty(event.get(field)):
                        errors.append(f"event[{i}] independent replication requires {field}")
            if route in {"ROUTE_TO_FOUNDATION", "ROUTE_TO_FORMALIZATION", "ROUTE_TO_PROMOTION", "OPEN_CONTINUATION"} and not nonempty(event.get("route_ref")):
                errors.append(f"event[{i}] {route} requires route_ref")
    return errors


def load_events(path: pathlib.Path) -> list[dict[str, Any]]:
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return []
    if text.startswith("["):
        data = json.loads(text)
        if not isinstance(data, list):
            raise ValueError("events JSON must be an array")
        return data
    return [json.loads(line) for line in text.splitlines() if line.strip()]


def template_snapshot(profile: str, spec: dict[str, Any]) -> dict[str, Any]:
    if profile not in set(spec.get("control_profiles", [])):
        raise ValueError(f"unknown control profile: {profile}")
    snap = {
        "actor": {"role": "RESEARCHER", "mode": "TASK_RESEARCH", "identity_state": "RESOLVED_LOCAL"},
        "object": {"control_profile": profile, "task_id": None, "task_lineage": "NOT_APPLICABLE"},
        "runtime": {"scheduler_state": "NONE", "dispatch_state": "NONE", "pre_math_gate": "NOT_REQUIRED"},
        "conversation": {
            "liveness": "ACTIVE",
            "recovery_class": "NONE",
            "last_verified_action_at": None,
            "durable_frontier_ref": None,
            "takeover_ref": None,
            "generation": 0,
        },
        "information": {"firewall": "NONE", "freeze_state": "NOT_REQUIRED", "source_exposure": "NORMAL"},
        "evidence": {
            "source_status": "NONE",
            "independent_status": "NOT_REQUIRED",
            "driver_verdict": "NONE",
            "axiom_admission_status": "NOT_APPLICABLE",
            "formalization_status": "NOT_APPLICABLE",
            "foundation_status": "NOT_APPLICABLE",
            "integration_status": "NOT_APPLICABLE",
            "benchmark_status": "NOT_APPLICABLE",
            "promotion_status": "NOT_APPLICABLE",
            "canonical_status": "NONCANONICAL",
        },
        "routing": {"working_truth": "INACTIVE", "method_harvest": "PENDING", "successor_gate": "NOT_APPLICABLE", "route_disposition": "PENDING"},
        "parent": {"objective": "OPEN", "completion_basis": "NONE", "next_executable_action": None},
        "terminal_output": False,
    }
    if profile in {"INDEPENDENT_AUDIT", "FREE_CANDIDATE_AUDIT"}:
        snap["information"].update(
            firewall="TASK_BLIND_FORWARD" if profile == "INDEPENDENT_AUDIT" else "FREE_PHASE_A_BLIND",
            freeze_state="REQUIRED_NOT_FROZEN",
            source_exposure="WITHHELD",
        )
        snap["evidence"]["independent_status"] = "REQUIRED_OPEN"
    elif profile == "AXIOM_ADMISSION_AUDIT":
        snap["runtime"]["pre_math_gate"] = "REQUIRED_UNSATISFIED"
        snap["information"].update(
            firewall="STATEMENT_EXPOSED_AUDIT",
            freeze_state="REQUIRED_NOT_FROZEN",
            source_exposure="WITHHELD",
        )
        snap["evidence"]["axiom_admission_status"] = "OPEN"
    elif profile == "FORMALIZATION":
        snap["evidence"]["formalization_status"] = "NOT_ADMITTED"
        snap["math_change_policy"] = "NO_NEW_MATHEMATICS"
    elif profile == "FOUNDATION_DISPOSITION":
        snap["actor"].update(role="FOUNDATION_STEWARD", mode="VERIFY_OR_MAINTAIN")
        snap["evidence"]["foundation_status"] = "PENDING"
    elif profile == "INTEGRATION":
        snap["evidence"]["integration_status"] = "OPEN"
    elif profile == "BENCHMARK":
        snap["evidence"]["benchmark_status"] = "OPEN"
    elif profile == "MATHEMATICAL_PROMOTION":
        snap["actor"].update(role="RESEARCH_DRIVER", mode="CONTROL_PLANE")
        snap["evidence"]["promotion_status"] = "NOT_READY"
    elif profile == "GOVERNANCE_MAINTENANCE":
        snap["actor"].update(role="RESEARCH_DRIVER", mode="CONTROL_PLANE")
    return snap


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Enterprise Math cross-layer research control validator")
    p.add_argument("--spec", type=pathlib.Path, default=DEFAULT_SPEC)
    sp = p.add_subparsers(dest="cmd", required=True)
    sp.add_parser("validate-spec")
    t = sp.add_parser("template")
    t.add_argument("profile")
    s = sp.add_parser("validate-snapshot")
    s.add_argument("path", type=pathlib.Path)
    e = sp.add_parser("validate-events")
    e.add_argument("path", type=pathlib.Path)
    r = sp.add_parser("registry")
    r.add_argument("--events", required=True, type=pathlib.Path)
    args = p.parse_args(argv)
    spec = load_json(args.spec)
    errors = validate_spec(spec)
    if not errors and args.cmd == "template":
        try:
            print(json.dumps(template_snapshot(args.profile, spec), ensure_ascii=False, indent=2))
        except ValueError as exc:
            print("ERROR:", exc)
            return 1
        return 0
    if not errors and args.cmd == "validate-snapshot":
        errors = validate_snapshot(load_json(args.path), spec)
    elif not errors and args.cmd == "validate-events":
        errors = validate_events(load_events(args.path), spec)
    elif not errors and args.cmd == "registry":
        errors = validate_events(load_events(args.events), spec)
        if not errors:
            cmd = [sys.executable, str(ROOT / "tools" / "research_scheduler.py"), "registry", "--events", str(args.events)]
            return subprocess.run(cmd, check=False).returncode
    if errors:
        for error in errors:
            print("ERROR:", error)
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
