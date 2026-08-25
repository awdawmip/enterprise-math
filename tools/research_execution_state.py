#!/usr/bin/env python3
"""Validate and query the Enterprise Math TASK_RESEARCH execution state machine."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MACHINE_PATH = ROOT / "research_execution_state_machine.json"
FRONTMATTER_PREFIX = "<!-- ENTERPRISE_MATH_TASK_V1\n"
FRONTMATTER_SUFFIX = "\n-->"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def load_machine(root: Path = ROOT) -> dict[str, Any]:
    return load_json(root / "research_execution_state_machine.json")


def split_taskbook(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith(FRONTMATTER_PREFIX):
        raise ValueError("missing ENTERPRISE_MATH_TASK_V1 frontmatter")
    end = text.find(FRONTMATTER_SUFFIX, len(FRONTMATTER_PREFIX))
    if end < 0:
        raise ValueError("unterminated taskbook frontmatter")
    raw = text[len(FRONTMATTER_PREFIX):end]
    return json.loads(raw), text[end + len(FRONTMATTER_SUFFIX):].lstrip("\n")


def _nonempty(value: Any) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, set, dict)):
        return bool(value)
    return value is not None


def _action_guard_set(machine: dict[str, Any], action: str) -> set[str]:
    """Return action plus all parent action classes whose guards also apply."""
    classes = set(machine.get("action_classes", {}))
    if action not in classes:
        raise ValueError(f"unknown action class: {action}")
    implies = machine.get("action_class_implies", {})
    out: set[str] = set()
    visiting: set[str] = set()

    def visit(current: str) -> None:
        if current in out:
            return
        if current in visiting:
            raise ValueError(f"cyclic action_class_implies at {current}")
        visiting.add(current)
        out.add(current)
        parents = implies.get(current, [])
        if not isinstance(parents, list):
            raise ValueError(f"action_class_implies[{current}] must be a list")
        for parent in parents:
            if parent not in classes:
                raise ValueError(f"action_class_implies[{current}] references unknown {parent}")
            visit(parent)
        visiting.remove(current)

    visit(action)
    return out


def validate_machine(machine: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    states = machine.get("states")
    if not isinstance(states, dict) or not states:
        return ["states must be a nonempty object"]

    initial = machine.get("initial_state")
    if initial not in states:
        errors.append(f"initial_state {initial!r} is not declared")

    authority = machine.get("task_authority_contract", {})
    required_authorities = {
        "OFFICIAL_TASKBOOK",
        "DIRECT_USER_TASK",
        "SCHEDULER_TASK",
        "DRIVER_DISPATCH_ENVELOPE",
    }
    authority_kinds = set(authority.get("allowed_authority_kinds", []))
    if not required_authorities.issubset(authority_kinds):
        errors.append("task authority contract must cover official/direct/scheduler/Driver-envelope task authority")

    allowed = machine.get("allowed_action_classes_by_state")
    if not isinstance(allowed, dict):
        errors.append("allowed_action_classes_by_state must be an object")
        allowed = {}
    elif set(allowed) != set(states):
        errors.append("allowed_action_classes_by_state keys must exactly match states")

    action_classes = machine.get("action_classes", {})
    action_names = set(action_classes)
    for state, actions in allowed.items():
        if not isinstance(actions, list):
            errors.append(f"{state}: allowed actions must be a list")
            continue
        unknown = sorted(set(actions) - action_names)
        if unknown:
            errors.append(f"{state}: unknown action classes {unknown}")

    for child, parents in machine.get("action_class_implies", {}).items():
        if child not in action_names:
            errors.append(f"action_class_implies unknown child {child!r}")
            continue
        if not isinstance(parents, list):
            errors.append(f"action_class_implies[{child}] must be a list")
            continue
        unknown = sorted(set(parents) - action_names)
        if unknown:
            errors.append(f"action_class_implies[{child}] unknown parents {unknown}")
        try:
            _action_guard_set(machine, child)
        except ValueError as exc:
            errors.append(str(exc))

    for state in ("UNBOUND", "DISPATCH_READY", "CLAIMED", "IDENTITY_READY", "PRE_MATH_GATES_PENDING"):
        if state in states:
            if states[state].get("substantive_math_allowed") is not False:
                errors.append(f"{state}: substantive_math_allowed must be false")
            for forbidden in ("MATHEMATICAL_SOURCE_READ", "POST_FREEZE_SOURCE_READ", "MATHEMATICAL_DERIVATION"):
                if forbidden in allowed.get(state, []):
                    errors.append(f"{state}: {forbidden} must be forbidden")

    for state in ("EXECUTION_READY", "IN_PROGRESS"):
        if state in states and states[state].get("substantive_math_allowed") is not True:
            errors.append(f"{state}: substantive_math_allowed must be true")

    gate_contract = machine.get("execution_gate_contract", {})
    if gate_contract.get("initial_gate_status") != "PENDING":
        errors.append("execution gates must initialize PENDING")
    required_statuses = {"PENDING", "SATISFIED", "FAILED"}
    if not required_statuses.issubset(set(gate_contract.get("gate_status_values", []))):
        errors.append("gate_status_values must include PENDING/SATISFIED/FAILED")
    if not _nonempty(gate_contract.get("action_guard_rule")):
        errors.append("execution gate contract must define action_guard_rule")

    transition_keys: set[tuple[str, str]] = set()
    for item in machine.get("transitions", []):
        if not isinstance(item, dict):
            errors.append("every transition must be an object")
            continue
        src, event, dst = item.get("from"), item.get("event"), item.get("to")
        if src not in states:
            errors.append(f"transition source {src!r} is not a state")
        if dst not in states:
            errors.append(f"transition target {dst!r} is not a state")
        if not _nonempty(event):
            errors.append(f"transition from {src!r} has no event")
        key = (str(src), str(event))
        if key in transition_keys:
            errors.append(f"duplicate transition key {key}")
        transition_keys.add(key)
        req = item.get("requires", [])
        if not isinstance(req, list):
            errors.append(f"{key}: requires must be a list")
        allowed_kinds = item.get("allowed_authority_kinds")
        if allowed_kinds is not None:
            if not isinstance(allowed_kinds, list) or not allowed_kinds:
                errors.append(f"{key}: allowed_authority_kinds must be a nonempty list")
            else:
                unknown = sorted(set(allowed_kinds) - authority_kinds)
                if unknown:
                    errors.append(f"{key}: unknown authority kinds {unknown}")

    required_regressions = {
        ("UNBOUND", "DISPATCH_AUDIT_PASS", "DISPATCH_READY"),
        ("UNBOUND", "DIRECT_USER_TASK_AUTHORITY_ACCEPTED", "DISPATCH_READY"),
        ("UNBOUND", "SCHEDULER_TASK_AUTHORITY_ACCEPTED", "DISPATCH_READY"),
        ("CLAIMED", "IDENTITY_RESOLVED", "IDENTITY_READY"),
        ("IDENTITY_READY", "STARTUP_CLASSIFIED_WITH_PRE_MATH_GATES", "PRE_MATH_GATES_PENDING"),
        ("PRE_MATH_GATES_PENDING", "PRE_MATH_GATES_SATISFIED", "EXECUTION_READY"),
        ("PRE_MATH_GATES_PENDING", "PRE_MATH_GATE_FAILED", "NONSTART_TERMINAL"),
        ("HANDOFF_READY", "SAME_CONVERSATION_EXECUTION_RESUMED", "IN_PROGRESS"),
        ("RETURNED", "RETURN_DELIVERED_WITHOUT_DRIVER_REVIEW", "DELIVERED_UNREVIEWED"),
    }
    actual = {
        (item.get("from"), item.get("event"), item.get("to"))
        for item in machine.get("transitions", [])
        if isinstance(item, dict)
    }
    for regression in sorted(required_regressions - actual):
        errors.append(f"missing required regression transition {regression}")

    recovery = machine.get("recovery_transitions", {})
    if recovery.get("to") != "RECOVERY_REQUIRED":
        errors.append("liveness recovery must enter RECOVERY_REQUIRED")
    if recovery.get("redispatch_to") != "REDISPATCH_REQUIRED":
        errors.append("non-resumable recovery must end REDISPATCH_REQUIRED")

    guard = machine.get("f5a_regression_guard", {})
    forbidden = set(guard.get("forbidden_classifications", []))
    required_forbidden = {"EXECUTION_READY", "IN_PROGRESS", "RETURN_ACCEPTED", "DELIVERED_UNREVIEWED", "CLOSED"}
    if not required_forbidden.issubset(forbidden):
        errors.append("F5A regression guard does not forbid all false-success states")
    return errors


def _declared_gates(meta: dict[str, Any], machine: dict[str, Any]) -> list[dict[str, Any]]:
    field = machine["execution_gate_contract"]["taskbook_gate_field"]
    gates = meta.get(field, [])
    return [gate for gate in gates if isinstance(gate, dict)] if isinstance(gates, list) else []


def audit_taskbook_execution(
    meta: dict[str, Any], machine: dict[str, Any], *, body: str = ""
) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    gate_contract = machine["execution_gate_contract"]

    policy_field = gate_contract["taskbook_policy_field"]
    policy_value = gate_contract["taskbook_policy_value"]
    if meta.get(policy_field) != policy_value:
        findings.append({
            "severity": "ERROR",
            "code": "EX-STATE-POLICY",
            "message": f"{policy_field} must be {policy_value!r}",
        })

    gates = meta.get(gate_contract["taskbook_gate_field"])
    if not isinstance(gates, list):
        findings.append({
            "severity": "ERROR",
            "code": "EX-GATES",
            "message": f"{gate_contract['taskbook_gate_field']} must be a list (use [] when none)",
        })
        return findings

    seen: set[str] = set()
    allowed_phases = set(gate_contract["allowed_gate_phases"])
    pre_math_gate_count = 0
    for idx, gate in enumerate(gates):
        if not isinstance(gate, dict):
            findings.append({
                "severity": "ERROR",
                "code": "EX-GATE-SCHEMA",
                "message": f"execution_gates[{idx}] must be an object",
            })
            continue
        for field in gate_contract["required_gate_fields"]:
            if not _nonempty(gate.get(field)):
                findings.append({
                    "severity": "ERROR",
                    "code": "EX-GATE-SCHEMA",
                    "message": f"execution_gates[{idx}] missing/nonempty field {field}",
                })
        gate_id = gate.get("gate_id")
        if isinstance(gate_id, str):
            if gate_id in seen:
                findings.append({
                    "severity": "ERROR",
                    "code": "EX-GATE-DUPLICATE",
                    "message": f"duplicate gate_id {gate_id!r}",
                })
            seen.add(gate_id)

        phase = gate.get("phase")
        if phase not in allowed_phases:
            findings.append({
                "severity": "ERROR",
                "code": "EX-GATE-PHASE",
                "message": f"gate {gate_id!r} phase must be one of {sorted(allowed_phases)}",
            })
        if phase == "PRE_MATH":
            pre_math_gate_count += 1

        must_precede = gate.get("must_precede")
        if not isinstance(must_precede, list) or not must_precede:
            findings.append({
                "severity": "ERROR",
                "code": "EX-GATE-ACTIONS",
                "message": f"gate {gate_id!r} must_precede must be a nonempty list",
            })
        else:
            unknown = sorted(set(must_precede) - set(machine["action_classes"]))
            if unknown:
                findings.append({
                    "severity": "ERROR",
                    "code": "EX-GATE-ACTIONS",
                    "message": f"gate {gate_id!r} names unknown action classes {unknown}",
                })
            if phase == "PRE_MATH":
                required_math = {"MATHEMATICAL_SOURCE_READ", "MATHEMATICAL_DERIVATION"}
                missing = sorted(required_math - set(must_precede))
                if missing:
                    findings.append({
                        "severity": "ERROR",
                        "code": "EX-PREMATH-COVERAGE",
                        "message": f"PRE_MATH gate {gate_id!r} must precede both generic source reads and math derivation; missing {missing}",
                    })
            if phase == "PRE_RETURN" and "RETURN_WRITE" not in must_precede:
                findings.append({
                    "severity": "ERROR",
                    "code": "EX-PRERETURN-COVERAGE",
                    "message": f"PRE_RETURN gate {gate_id!r} must precede RETURN_WRITE",
                })

        evidence = gate.get("evidence")
        if not isinstance(evidence, dict):
            findings.append({
                "severity": "ERROR",
                "code": "EX-GATE-EVIDENCE",
                "message": f"gate {gate_id!r} evidence must be an object",
            })
        else:
            for field in gate_contract["required_evidence_fields"]:
                if not _nonempty(evidence.get(field)):
                    findings.append({
                        "severity": "ERROR",
                        "code": "EX-GATE-EVIDENCE",
                        "message": f"gate {gate_id!r} evidence missing/nonempty field {field}",
                    })

    detector = machine.get("premath_directive_detection", {})
    hits = [
        pattern
        for pattern in detector.get("patterns", [])
        if re.search(pattern, body, flags=re.IGNORECASE | re.MULTILINE)
    ]
    if hits and pre_math_gate_count == 0:
        findings.append({
            "severity": "ERROR",
            "code": "EX-PREMATH-UNDECLARED",
            "message": "task authority contains an obvious pre-math directive but declares no PRE_MATH execution gate: " + ", ".join(hits),
        })
    return findings


def audit_execution_spec(
    spec: dict[str, Any], machine: dict[str, Any], *, authority_body: str = ""
) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    contract = machine["task_authority_contract"]
    for field in contract["normalized_execution_spec_fields"]:
        value = spec.get(field)
        if field == "execution_gates":
            if not isinstance(value, list):
                findings.append({
                    "severity": "ERROR",
                    "code": "EX-SPEC",
                    "message": "normalized execution spec requires execution_gates list",
                })
        elif not _nonempty(value):
            findings.append({
                "severity": "ERROR",
                "code": "EX-SPEC",
                "message": f"normalized execution spec missing/nonempty field {field}",
            })
    authority_kind = spec.get("authority_kind")
    if _nonempty(authority_kind) and authority_kind not in contract["allowed_authority_kinds"]:
        findings.append({
            "severity": "ERROR",
            "code": "EX-AUTHORITY-KIND",
            "message": f"authority_kind must be one of {contract['allowed_authority_kinds']}",
        })
    fake_meta = {
        machine["execution_gate_contract"]["taskbook_policy_field"]: machine["execution_gate_contract"]["taskbook_policy_value"],
        machine["execution_gate_contract"]["taskbook_gate_field"]: spec.get("execution_gates"),
    }
    findings.extend(audit_taskbook_execution(fake_meta, machine, body=authority_body))
    return findings


def audit_taskbook_path(path: Path, root: Path = ROOT) -> list[dict[str, str]]:
    try:
        meta, body = split_taskbook(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [{"severity": "ERROR", "code": "EX-TASKBOOK-PARSE", "message": str(exc)}]
    return audit_taskbook_execution(meta, load_machine(root), body=body)


def allowed_action(machine: dict[str, Any], state: str, action: str) -> bool:
    if state not in machine["states"]:
        raise ValueError(f"unknown state: {state}")
    if action not in machine["action_classes"]:
        raise ValueError(f"unknown action class: {action}")
    return action in machine["allowed_action_classes_by_state"][state]


def gate_blockers(
    meta: dict[str, Any], machine: dict[str, Any], action: str, satisfied_gate_ids: set[str]
) -> list[str]:
    guard_classes = _action_guard_set(machine, action)
    blockers: list[str] = []
    for gate in _declared_gates(meta, machine):
        gate_id = gate.get("gate_id")
        if not isinstance(gate_id, str) or not gate_id:
            continue
        must_precede = gate.get("must_precede")
        if isinstance(must_precede, list) and guard_classes.intersection(must_precede) and gate_id not in satisfied_gate_ids:
            blockers.append(gate_id)
    return sorted(blockers)


def allowed_task_action(
    meta: dict[str, Any],
    machine: dict[str, Any],
    state: str,
    action: str,
    satisfied_gate_ids: set[str] | None = None,
) -> tuple[bool, list[str]]:
    satisfied = satisfied_gate_ids or set()
    if not allowed_action(machine, state, action):
        return False, [f"STATE:{state}"]
    blockers = gate_blockers(meta, machine, action, satisfied)
    return not blockers, blockers


def _transition_authority_audit(
    machine: dict[str, Any], event: str, evidence: dict[str, Any]
) -> None:
    authority_events = {
        "DISPATCH_AUDIT_PASS": ("OFFICIAL_TASKBOOK", "taskbook_authority_body"),
        "DIRECT_USER_TASK_AUTHORITY_ACCEPTED": ("DIRECT_USER_TASK", "authority_body"),
        "SCHEDULER_TASK_AUTHORITY_ACCEPTED": ("SCHEDULER_TASK", "authority_body"),
        "DRIVER_DISPATCH_ENVELOPE_ACCEPTED": ("DRIVER_DISPATCH_ENVELOPE", "authority_body"),
    }
    if event not in authority_events:
        return
    expected_kind, body_field = authority_events[event]
    spec = evidence.get("normalized_execution_spec")
    if not isinstance(spec, dict):
        raise ValueError("authority transition requires normalized_execution_spec object")
    if spec.get("authority_kind") != expected_kind:
        raise ValueError(f"{event} requires normalized authority_kind={expected_kind}")
    body = evidence.get(body_field, "")
    findings = audit_execution_spec(spec, machine, authority_body=body if isinstance(body, str) else "")
    errors = [item for item in findings if item["severity"] == "ERROR"]
    if errors:
        detail = "; ".join(f"{item['code']}:{item['message']}" for item in errors)
        raise ValueError(f"normalized execution spec audit failed: {detail}")


def next_state(machine: dict[str, Any], state: str, event: str, evidence: dict[str, Any]) -> str:
    if state == "RECOVERY_REQUIRED":
        recovery = machine["recovery_transitions"]
        if event == recovery["resume_event"]:
            target = evidence.get("resume_state")
            if target not in recovery["resume_targets"]:
                raise ValueError(f"resume_state must be one of {recovery['resume_targets']}")
            if not _nonempty(evidence.get("durable_frontier_ref")):
                raise ValueError("DURABLE_FRONTIER_RECONCILED requires durable_frontier_ref")
            if evidence.get("execution_gate_ledger_reconciled") is not True:
                raise ValueError("DURABLE_FRONTIER_RECONCILED requires execution_gate_ledger_reconciled=true")
            return target
        if event == recovery["redispatch_event"]:
            if not _nonempty(evidence.get("reason")):
                raise ValueError("DURABLE_FRONTIER_NOT_RESUMABLE requires reason")
            return recovery["redispatch_to"]

    recovery = machine["recovery_transitions"]
    if event == recovery["trigger_event"]:
        if state not in recovery["triggerable_from"]:
            raise ValueError(f"{event} is not legal from {state}")
        if not _nonempty(evidence.get("reason")):
            raise ValueError(f"{event} requires reason")
        return recovery["to"]

    _transition_authority_audit(machine, event, evidence)

    matches = [
        item for item in machine["transitions"]
        if item["from"] == state and item["event"] == event
    ]
    if len(matches) != 1:
        raise ValueError(f"no unique transition from {state} on {event}")
    transition = matches[0]
    missing = [field for field in transition.get("requires", []) if not _nonempty(evidence.get(field))]
    if missing:
        raise ValueError(f"missing transition evidence: {missing}")

    allowed_kinds = transition.get("allowed_authority_kinds")
    if allowed_kinds is not None and evidence.get("authority_kind") not in allowed_kinds:
        raise ValueError(f"transition {event} allowed only for authority kinds {allowed_kinds}")

    strict_true = {
        "dispatch_audit_pass",
        "execution_gates_checked_empty_of_pre_math",
        "action_within_task_scope",
        "return_write_action_guard_pass",
        "execution_gate_ledger_complete",
        "execution_gate_ledger_reconciled",
        "parent_objective_or_successor_gate_evaluated",
    }
    false_fields = [
        field for field in transition.get("requires", [])
        if field in strict_true and evidence.get(field) is not True
    ]
    if false_fields:
        raise ValueError(f"transition requires exact true evidence: {false_fields}")
    return transition["to"]


def _print_findings(findings: list[dict[str, str]]) -> int:
    if not findings:
        print("PASS")
        return 0
    for item in findings:
        print(f"{item['severity']} {item['code']}: {item['message']}")
    return 1 if any(item["severity"] == "ERROR" for item in findings) else 0


def command_validate_machine(_: argparse.Namespace) -> int:
    errors = validate_machine(load_machine())
    if not errors:
        print("research_execution_state_machine.json: PASS")
        return 0
    for item in errors:
        print(f"ERROR EX-MACHINE: {item}")
    return 1


def command_audit_taskbook(args: argparse.Namespace) -> int:
    path = Path(args.path)
    if not path.is_absolute():
        path = ROOT / path
    return _print_findings(audit_taskbook_path(path))


def command_audit_spec(args: argparse.Namespace) -> int:
    try:
        spec = json.loads(args.spec_json)
        if not isinstance(spec, dict):
            raise ValueError("--spec-json must decode to an object")
        return _print_findings(audit_execution_spec(spec, load_machine(), authority_body=args.authority_body))
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 2


def command_check_action(args: argparse.Namespace) -> int:
    machine = load_machine()
    try:
        ok = allowed_action(machine, args.state, args.action)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2
    print("ALLOWED_BY_STATE" if ok else "BLOCKED_BY_STATE")
    return 0 if ok else 1


def command_check_task_action(args: argparse.Namespace) -> int:
    machine = load_machine()
    path = Path(args.taskbook)
    if not path.is_absolute():
        path = ROOT / path
    try:
        meta, _ = split_taskbook(path.read_text(encoding="utf-8"))
        satisfied = {item for item in args.satisfied_gates.split(",") if item}
        ok, blockers = allowed_task_action(meta, machine, args.state, args.action, satisfied)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 2
    if ok:
        print("ALLOWED")
        return 0
    print("BLOCKED: " + ",".join(blockers))
    return 1


def command_next_state(args: argparse.Namespace) -> int:
    machine = load_machine()
    try:
        evidence = json.loads(args.evidence_json)
        if not isinstance(evidence, dict):
            raise ValueError("--evidence-json must decode to an object")
        print(next_state(machine, args.state, args.event, evidence))
        return 0
    except (ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}")
        return 2


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    vm = sub.add_parser("validate-machine")
    vm.set_defaults(func=command_validate_machine)

    at = sub.add_parser("audit-taskbook")
    at.add_argument("path")
    at.set_defaults(func=command_audit_taskbook)

    asp = sub.add_parser("audit-spec")
    asp.add_argument("--spec-json", required=True)
    asp.add_argument("--authority-body", default="")
    asp.set_defaults(func=command_audit_spec)

    ca = sub.add_parser("check-action")
    ca.add_argument("--state", required=True)
    ca.add_argument("--action", required=True)
    ca.set_defaults(func=command_check_action)

    cta = sub.add_parser("check-task-action")
    cta.add_argument("--taskbook", required=True)
    cta.add_argument("--state", required=True)
    cta.add_argument("--action", required=True)
    cta.add_argument("--satisfied-gates", default="")
    cta.set_defaults(func=command_check_task_action)

    ns = sub.add_parser("next-state")
    ns.add_argument("--state", required=True)
    ns.add_argument("--event", required=True)
    ns.add_argument("--evidence-json", default="{}")
    ns.set_defaults(func=command_next_state)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
