#!/usr/bin/env python3
"""Create and audit Enterprise Math research taskbooks.

Taskbook policy review and scheduler dispatch review are deliberately separate:
policy PASS makes a taskbook publishable; only scheduler V2 REVIEW/DISPATCH can
make the registered task READY.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "research_taskbook_policy.json"
FRONTMATTER_PREFIX = "<!-- ENTERPRISE_MATH_TASK_V1\n"
FRONTMATTER_SUFFIX = "\n-->"
VALID_LINEAGES = {"NEW_DIRECTION", "CONTINUATION", "REPLAY", "INTEGRATION", "MAINTENANCE"}
VALID_ORIGINS = {
    "DIRECT_USER_DIRECTION", "DRIVER_ROADMAP", "FREE_AXIOM_CANDIDATE",
    "FOUNDATION_QUESTION", "REPLAY_OR_INTEGRATION", "MAINTENANCE",
}
VALID_AUTHOR_ROLES = {"RESEARCHER", "RESEARCH_DRIVER", "STEWARD"}
NEW_TASK_AUTHORITY = "SCHEDULER_REVIEW_REQUIRED"
LEGACY_TASK_AUTHORITY = "DRIVER_APPROVED"


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def policy_manifest(root: Path = ROOT) -> dict[str, Any]:
    return load_json(root / "research_taskbook_policy.json")


def git_blob_identity(data: bytes) -> bytes:
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).digest()


def policy_digest(root: Path = ROOT) -> str:
    policy = policy_manifest(root)
    h = hashlib.sha256()
    paths = ["research_taskbook_policy.json", *policy["policy_inputs"]]
    for rel in paths:
        path = root / rel
        data = path.read_bytes()
        h.update(rel.encode("utf-8"))
        h.update(b"\0")
        h.update(git_blob_identity(data))
        h.update(b"\0")
    return "sha256:" + h.hexdigest()


def split_taskbook(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith(FRONTMATTER_PREFIX):
        raise ValueError("missing ENTERPRISE_MATH_TASK_V1 frontmatter")
    end = text.find(FRONTMATTER_SUFFIX, len(FRONTMATTER_PREFIX))
    if end < 0:
        raise ValueError("unterminated taskbook frontmatter")
    meta = json.loads(text[len(FRONTMATTER_PREFIX):end])
    body = text[end + len(FRONTMATTER_SUFFIX):].lstrip("\n")
    return meta, body


def render_taskbook(meta: dict[str, Any], body: str) -> str:
    return FRONTMATTER_PREFIX + json.dumps(meta, indent=2, ensure_ascii=False) + FRONTMATTER_SUFFIX + "\n\n" + body.rstrip() + "\n"


def taskbook_review(meta: dict[str, Any]) -> dict[str, Any] | None:
    review = meta.get("policy_review")
    return review if isinstance(review, dict) else None


def override_map(meta: dict[str, Any]) -> dict[str, dict[str, Any]]:
    review = taskbook_review(meta) or {}
    out: dict[str, dict[str, Any]] = {}
    overrides = review.get("temporary_overrides", [])
    if isinstance(overrides, list):
        for item in overrides:
            if isinstance(item, dict) and isinstance(item.get("conflict_id"), str):
                out[item["conflict_id"]] = item
    return out


def regex_hits(body: str, patterns: list[str]) -> list[str]:
    return [pat for pat in patterns if re.search(pat, body, flags=re.IGNORECASE | re.MULTILINE)]


def _nonempty(value: Any) -> bool:
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, set, dict)):
        return bool(value)
    return value is not None


def _stage_number(meta: dict[str, Any]) -> int | None:
    text = f"{meta.get('task_id', '')} {meta.get('title', '')}"
    numbers = [int(m.group(1)) for m in re.finditer(r"\bSTAGE[- _]?(\d+)\b", text, flags=re.IGNORECASE)]
    return max(numbers) if numbers else None


def origin_findings(meta: dict[str, Any], *, publish: bool, root: Path = ROOT) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    origin = meta.get("origin_kind")
    if origin is None:
        findings.append({"severity": "ERROR" if publish else "WARN", "code": "TB-ORIGIN-MISSING", "message": "publication requires origin_kind; legacy files may remain historical"})
        return findings
    if origin not in VALID_ORIGINS:
        findings.append({"severity": "ERROR", "code": "TB-ORIGIN-VALUE", "message": f"origin_kind must be one of {sorted(VALID_ORIGINS)}, got {origin!r}"})
        return findings
    contract = load_json(root / "research_taskbook_contract.json")["task_origin_contract"]
    if origin == "FREE_AXIOM_CANDIDATE":
        for field in contract["free_candidate_required_fields"]:
            if not _nonempty(meta.get(field)):
                findings.append({"severity": "ERROR", "code": "TB-ORIGIN-CANDIDATE", "message": f"FREE_AXIOM_CANDIDATE origin requires {field}"})
        state = meta.get("origin_candidate_state")
        if _nonempty(state) and state not in contract["free_candidate_allowed_states"]:
            findings.append({"severity": "ERROR", "code": "TB-ORIGIN-CANDIDATE-STATE", "message": "free candidate origin must already be in an audited intake-eligible state"})
    elif origin == "FOUNDATION_QUESTION":
        field = contract["foundation_question_required_field"]
        if not _nonempty(meta.get(field)):
            findings.append({"severity": "ERROR", "code": "TB-ORIGIN-FOUNDATION", "message": f"FOUNDATION_QUESTION origin requires {field}"})
    return findings


def lineage_findings(meta: dict[str, Any], *, publish: bool, root: Path = ROOT) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    lineage = meta.get("task_lineage")
    if lineage is None:
        findings.append({"severity": "ERROR" if publish else "WARN", "code": "TB-LINEAGE-MISSING", "message": "publication requires task_lineage; legacy files may remain historical"})
        return findings
    if lineage not in VALID_LINEAGES:
        findings.append({"severity": "ERROR", "code": "TB-LINEAGE-VALUE", "message": f"task_lineage must be one of {sorted(VALID_LINEAGES)}, got {lineage!r}"})
        return findings
    stage = _stage_number(meta)
    if stage is not None and stage >= 2 and lineage != "CONTINUATION":
        findings.append({"severity": "ERROR", "code": "TB-STAGE-LINEAGE", "message": f"Stage {stage} task must use task_lineage=CONTINUATION"})
    parent = meta.get("parent_task_id")
    gate = meta.get("successor_gate")
    if lineage == "CONTINUATION":
        if not isinstance(parent, str) or not parent.strip():
            findings.append({"severity": "ERROR", "code": "TB-SUCCESSOR-PARENT", "message": "CONTINUATION requires nonempty parent_task_id"})
        contract = load_json(root / "research_taskbook_contract.json")["task_lineage_contract"]
        required = contract["continuation_required_successor_gate_fields"]
        if not isinstance(gate, dict):
            findings.append({"severity": "ERROR", "code": "TB-SUCCESSOR-GATE", "message": "CONTINUATION requires successor_gate object"})
        else:
            for field in required:
                if not _nonempty(gate.get(field)):
                    findings.append({"severity": "ERROR", "code": "TB-SUCCESSOR-GATE", "message": f"CONTINUATION successor_gate missing/nonempty field: {field}"})
    elif _nonempty(parent) or _nonempty(gate):
        findings.append({"severity": "WARN", "code": "TB-LINEAGE-EXTRA", "message": "parent_task_id/successor_gate present on non-CONTINUATION lineage"})
    return findings


def _required_metadata(contract: dict[str, Any]) -> dict[str, Any]:
    return contract.get("new_taskbook_required_metadata") or contract.get("new_dispatchable_taskbook_required_metadata") or {}


def authorship_findings(meta: dict[str, Any], contract: dict[str, Any], *, publish: bool) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    role = meta.get("created_by_role")
    authority = meta.get("task_authority")
    author_contract = contract.get("author_contract")
    if isinstance(author_contract, dict):
        allowed = set(author_contract.get("allowed_roles", [])) or VALID_AUTHOR_ROLES
        if role not in allowed:
            findings.append({"severity": "ERROR", "code": "TB-AUTHOR-ROLE", "message": f"created_by_role must be one of {sorted(allowed)}, got {role!r}"})
        if authority != NEW_TASK_AUTHORITY:
            if authority == LEGACY_TASK_AUTHORITY:
                findings.append({"severity": "ERROR" if publish else "WARN", "code": "TB-LEGACY-AUTHORITY", "message": "DRIVER_APPROVED is legacy-only; V2 publication requires SCHEDULER_REVIEW_REQUIRED"})
            else:
                findings.append({"severity": "ERROR", "code": "TB-AUTHORITY", "message": f"task_authority must be {NEW_TASK_AUTHORITY}"})
    else:
        # Synthetic/legacy V6 contract compatibility.
        expected = _required_metadata(contract)
        if expected.get("created_by_role") and role != expected["created_by_role"]:
            findings.append({"severity": "ERROR", "code": "TB-META", "message": f"created_by_role must be {expected['created_by_role']!r}"})
        if expected.get("task_authority") and authority != expected["task_authority"]:
            findings.append({"severity": "ERROR", "code": "TB-META", "message": f"task_authority must be {expected['task_authority']!r}"})
    return findings


def audit_taskbook(path: Path, *, root: Path = ROOT, publish: bool = False, dispatch: bool | None = None) -> list[dict[str, str]]:
    # `dispatch` is retained as a compatibility alias for old callers/tests. Under V7
    # it means "strict pre-publication audit"; scheduler V2 owns actual dispatch.
    if dispatch is not None:
        publish = bool(dispatch)
    policy = policy_manifest(root)
    contract = load_json(root / "research_taskbook_contract.json")
    findings: list[dict[str, str]] = []
    try:
        meta, body = split_taskbook(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [{"severity": "ERROR", "code": "TB-PARSE", "message": str(exc)}]

    required = _required_metadata(contract)
    for key, expected in required.items():
        if key in {"created_by_role", "task_authority"}:
            continue
        if key not in meta:
            findings.append({"severity": "ERROR", "code": "TB-META", "message": f"missing metadata: {key}"})
        elif isinstance(expected, str) and expected.startswith("<"):
            pass
        elif isinstance(expected, str) and meta[key] != expected:
            findings.append({"severity": "ERROR", "code": "TB-META", "message": f"{key} must be {expected!r}"})

    findings.extend(authorship_findings(meta, contract, publish=publish))
    findings.extend(origin_findings(meta, publish=publish, root=root))
    findings.extend(lineage_findings(meta, publish=publish, root=root))

    for key in contract.get("forbidden_fixed_runtime_metadata", []):
        if key in meta:
            findings.append({"severity": "ERROR", "code": "TB-RUNTIME-META", "message": f"forbidden fixed runtime metadata: {key}"})

    review = taskbook_review(meta)
    if review is None:
        findings.append({"severity": "ERROR" if publish else "WARN", "code": "TB-POLICY-UNSTAMPED", "message": "taskbook has no current policy_review stamp; publication requires review"})
        overrides: dict[str, dict[str, Any]] = {}
    else:
        overrides = override_map(meta)
        if review.get("policy_set") != "research_taskbook_policy.json":
            findings.append({"severity": "ERROR", "code": "TB-POLICY-SET", "message": "policy_review.policy_set must be research_taskbook_policy.json"})
        current = policy_digest(root)
        if review.get("policy_digest") != current:
            findings.append({"severity": "ERROR" if publish else "WARN", "code": "TB-POLICY-STALE", "message": f"policy digest stale: taskbook={review.get('policy_digest')} current={current}"})
        if publish and review.get("review_state") != "PASS":
            findings.append({"severity": "ERROR", "code": "TB-POLICY-REVIEW", "message": "publication requires policy_review.review_state=PASS"})
        required_override_fields = policy.get("override_required_fields", [])
        for cid, item in overrides.items():
            for field in required_override_fields:
                if not item.get(field):
                    findings.append({"severity": "ERROR", "code": "TB-OVERRIDE-SCHEMA", "message": f"override {cid} missing {field}"})

    for check in policy.get("conflict_checks", []):
        hits = regex_hits(body, check["patterns"])
        if hits and check["id"] not in overrides:
            findings.append({"severity": check.get("severity", "ERROR"), "code": check["id"], "message": "policy-sensitive task-local directive found without explicit temporary override: " + ", ".join(hits)})
    for check in policy.get("restatement_checks", []):
        hits = regex_hits(body, check["patterns"])
        if hits:
            findings.append({"severity": check.get("severity", "ERROR"), "code": check["id"], "message": "generic repository policy is restated in taskbook; remove it and inherit the repository rule: " + ", ".join(hits)})
    return findings


def print_findings(path: Path, findings: list[dict[str, str]]) -> None:
    if not findings:
        print(f"{path}: PASS")
        return
    for item in findings:
        print(f"{path}: {item['severity']} {item['code']}: {item['message']}")


def command_audit(args: argparse.Namespace) -> int:
    paths = sorted((ROOT / "research_tasks").glob("*.md")) if args.all else [Path(p) if Path(p).is_absolute() else ROOT / p for p in args.paths]
    if not paths:
        raise SystemExit("no taskbooks selected")
    errors = 0
    strict = bool(args.publish or args.dispatch)
    for path in paths:
        findings = audit_taskbook(path, publish=strict)
        display = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        print_findings(display, findings)
        errors += sum(item["severity"] == "ERROR" for item in findings)
    return 1 if errors else 0


def base_metadata(args: argparse.Namespace) -> dict[str, Any]:
    if args.origin_kind == "FREE_AXIOM_CANDIDATE" and (not args.origin_candidate_id or not args.origin_candidate_state):
        raise SystemExit("FREE_AXIOM_CANDIDATE requires --origin-candidate-id and --origin-candidate-state")
    if args.origin_kind == "FOUNDATION_QUESTION" and not args.origin_foundation_question_id:
        raise SystemExit("FOUNDATION_QUESTION requires --origin-foundation-question-id")
    successor_gate: dict[str, Any] | None = None
    if args.lineage == "CONTINUATION":
        if not args.parent_task_id:
            raise SystemExit("--parent-task-id is required for --lineage CONTINUATION")
        successor_gate = {
            "new_information_gap": "",
            "why_parent_result_does_not_close_it": "",
            "discriminating_outcomes": [],
            "kill_condition": "",
            "alternative_route_or_free_exploration_considered": "",
            "why_new_stage_or_task_is_better_than_same_task_or_closure": "",
        }
    meta = {
        "task_id": args.task_id,
        "title": args.title,
        "kind": args.kind,
        "owner": "taskbook/unassigned",
        "base_state": "DRAFT",
        "priority": args.priority,
        "leverage": args.leverage,
        "frontier": "",
        "next_action": "",
        "dependencies": [],
        "source_refs": [],
        "evidence_status": "TASKBOOK_DRAFT",
        "last_progress_ref": None,
        "last_progress_at": None,
        "hard_block": None,
        "tags": [],
        "claim_lease_minutes": 1440,
        "created_by_role": args.author_role,
        "task_authority": NEW_TASK_AUTHORITY,
        "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
        "final_response_identity_policy": "INHERIT_GLOBAL",
        "identity_lane": args.lane,
        "origin_kind": args.origin_kind,
        "task_lineage": args.lineage,
        "parent_task_id": args.parent_task_id,
        "successor_gate": successor_gate,
        "policy_review": {
            "policy_set": "research_taskbook_policy.json",
            "policy_digest": policy_digest(ROOT),
            "review_state": "PENDING_POLICY_REVIEW",
            "temporary_overrides": [],
        },
    }
    if args.origin_candidate_id:
        meta["origin_candidate_id"] = args.origin_candidate_id
    if args.origin_candidate_state:
        meta["origin_candidate_state"] = args.origin_candidate_state
    if args.origin_foundation_question_id:
        meta["origin_foundation_question_id"] = args.origin_foundation_question_id
    return meta


def command_new(args: argparse.Namespace) -> int:
    out = Path(args.output)
    if not out.is_absolute():
        out = ROOT / out
    if out.exists():
        raise SystemExit(f"refusing to overwrite {out}")
    meta = base_metadata(args)
    body = f"""# {args.title}

Status: `DRAFT / POLICY_REVIEW_PENDING / NOT PUBLISHED / NOT DISPATCHABLE`

## 0. Task-local mother question

<write only the task-specific question>

## 1. Frozen task-local inputs and scope

<task-specific inputs, assumptions, exclusions, dependencies>

## 2. Required mathematical / executable / formal outputs

<task-specific deliverables>

## 3. Success, kill, and return criteria

<task-specific PASS/KILL conditions. If this is a continuation, the frontmatter successor_gate must independently justify why another stage exists.>
"""
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_taskbook(meta, body), encoding="utf-8")
    print(out.relative_to(ROOT))
    print("created as DRAFT; complete task-local content, then run review --approve. Scheduler publication/review is still required.")
    return 0


def command_review(args: argparse.Namespace) -> int:
    path = Path(args.path)
    if not path.is_absolute():
        path = ROOT / path
    meta, body = split_taskbook(path.read_text(encoding="utf-8"))
    meta["final_response_identity_policy"] = "INHERIT_GLOBAL"
    review = taskbook_review(meta) or {"policy_set": "research_taskbook_policy.json", "temporary_overrides": []}
    review["policy_set"] = "research_taskbook_policy.json"
    review["policy_digest"] = policy_digest(ROOT)
    review["review_state"] = "PENDING_POLICY_REVIEW"
    meta["policy_review"] = review
    path.write_text(render_taskbook(meta, body), encoding="utf-8")
    findings = audit_taskbook(path, publish=False)
    blocking = [f for f in findings if f["severity"] == "ERROR"]
    if blocking:
        print_findings(path.relative_to(ROOT), findings)
        print("policy review not approved")
        return 1
    if args.approve:
        review["review_state"] = "PASS"
        meta["policy_review"] = review
        if meta.get("base_state") == "DRAFT":
            meta["base_state"] = "PUBLISHED"
        if meta.get("evidence_status") == "TASKBOOK_DRAFT":
            meta["evidence_status"] = "TASKBOOK_POLICY_PASS_PENDING_SCHEDULER_REVIEW"
        path.write_text(render_taskbook(meta, body), encoding="utf-8")
        publish_findings = audit_taskbook(path, publish=True)
        if any(f["severity"] == "ERROR" for f in publish_findings):
            print_findings(path.relative_to(ROOT), publish_findings)
            return 1
        print(f"{path.relative_to(ROOT)}: POLICY_REVIEW_PASS / PUBLISHED_READY / SCHEDULER_DISPATCH_REVIEW_REQUIRED")
        return 0
    print(f"{path.relative_to(ROOT)}: policy review refreshed; approval still pending")
    return 0


def command_digest(_: argparse.Namespace) -> int:
    print(policy_digest(ROOT))
    return 0


def main() -> int:
    p = argparse.ArgumentParser()
    sp = p.add_subparsers(dest="cmd", required=True)
    new = sp.add_parser("new")
    new.add_argument("--task-id", required=True)
    new.add_argument("--title", required=True)
    new.add_argument("--kind", default="RESEARCH")
    new.add_argument("--priority", default="P1")
    new.add_argument("--leverage", default="MEDIUM")
    new.add_argument("--lane", default="")
    new.add_argument("--author-role", choices=sorted(VALID_AUTHOR_ROLES), default="RESEARCH_DRIVER")
    new.add_argument("--origin-kind", choices=sorted(VALID_ORIGINS), default="DRIVER_ROADMAP")
    new.add_argument("--origin-candidate-id", default=None)
    new.add_argument("--origin-candidate-state", default=None)
    new.add_argument("--origin-foundation-question-id", default=None)
    new.add_argument("--lineage", choices=sorted(VALID_LINEAGES), default="NEW_DIRECTION")
    new.add_argument("--parent-task-id", default=None)
    new.add_argument("--output", required=True)
    new.set_defaults(func=command_new)
    audit = sp.add_parser("audit")
    audit.add_argument("paths", nargs="*")
    audit.add_argument("--all", action="store_true")
    audit.add_argument("--publish", action="store_true", help="strict pre-PUBLISH gate")
    audit.add_argument("--dispatch", action="store_true", help="legacy alias for --publish; actual dispatch belongs to scheduler V2")
    audit.set_defaults(func=command_audit)
    review = sp.add_parser("review")
    review.add_argument("path")
    review.add_argument("--approve", action="store_true", help="approve taskbook policy only; does not make scheduler READY")
    review.set_defaults(func=command_review)
    digest = sp.add_parser("policy-digest")
    digest.set_defaults(func=command_digest)
    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
