#!/usr/bin/env python3
"""Create and audit Enterprise Math research taskbooks against current repository policy."""
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
    "DIRECT_USER_DIRECTION",
    "DRIVER_ROADMAP",
    "FREE_AXIOM_CANDIDATE",
    "FOUNDATION_QUESTION",
    "REPLAY_OR_INTEGRATION",
    "MAINTENANCE",
}
DIGEST_EXCLUDE_BEGIN_RE = re.compile(
    r"^<!-- TASKBOOK_POLICY_DIGEST_EXCLUDE_BEGIN: ([A-Z0-9_.-]+) -->$"
)
DIGEST_EXCLUDE_END_RE = re.compile(
    r"^<!-- TASKBOOK_POLICY_DIGEST_EXCLUDE_END: ([A-Z0-9_.-]+) -->$"
)
DIGEST_EXCLUDED_OPERATIONAL_BLOCKS = {
    "CONTEXT_READ_BUDGET": {
        "AGENTS.md",
        "docs/GITHUB_INTERACTION_BUDGET.md",
    },
}


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def policy_manifest(root: Path = ROOT) -> dict[str, Any]:
    return load_json(root / "research_taskbook_policy.json")


def git_blob_identity(data: bytes) -> bytes:
    """Return the raw SHA-1 identity Git assigns to this exact file content."""
    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).digest()


def taskbook_policy_digest_payload(rel: str, data: bytes) -> bytes:
    """Remove explicitly allowed runtime-only addenda from taskbook policy coupling.

    Taskbook policy digests freeze mathematical/task-authoring semantics. Pure
    conversational read-budget changes must be visible to every agent without
    invalidating every already-published taskbook. Only named addenda on an exact
    path allowlist are excluded; malformed, nested, unknown, or mismatched markers
    fail closed.
    """
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError(f"{rel}: taskbook policy input must be UTF-8") from exc
    lines = text.splitlines(keepends=True)
    out: list[str] = []
    active: str | None = None
    for line in lines:
        marker = line.rstrip("\r\n")
        begin = DIGEST_EXCLUDE_BEGIN_RE.fullmatch(marker)
        end = DIGEST_EXCLUDE_END_RE.fullmatch(marker)
        if begin:
            label = begin.group(1)
            allowed_paths = DIGEST_EXCLUDED_OPERATIONAL_BLOCKS.get(label)
            if allowed_paths is None or rel not in allowed_paths:
                raise ValueError(f"{rel}: unauthorized taskbook policy digest exclusion {label}")
            if active is not None:
                raise ValueError(f"{rel}: nested taskbook policy digest exclusions are forbidden")
            active = label
            continue
        if end:
            label = end.group(1)
            if active is None:
                raise ValueError(f"{rel}: unmatched taskbook policy digest exclusion end {label}")
            if label != active:
                raise ValueError(
                    f"{rel}: taskbook policy digest exclusion end {label} does not match {active}"
                )
            active = None
            continue
        if active is None:
            out.append(line)
    if active is not None:
        raise ValueError(f"{rel}: unterminated taskbook policy digest exclusion {active}")
    return "".join(out).encode("utf-8")


def policy_digest(root: Path = ROOT) -> str:
    policy = policy_manifest(root)
    h = hashlib.sha256()
    paths = ["research_taskbook_policy.json", *policy["policy_inputs"]]
    for rel in paths:
        path = root / rel
        data = taskbook_policy_digest_payload(rel, path.read_bytes())
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
    raw = text[len(FRONTMATTER_PREFIX):end]
    meta = json.loads(raw)
    body = text[end + len(FRONTMATTER_SUFFIX):].lstrip("\n")
    return meta, body


def render_taskbook(meta: dict[str, Any], body: str) -> str:
    return (
        FRONTMATTER_PREFIX
        + json.dumps(meta, indent=2, ensure_ascii=False)
        + FRONTMATTER_SUFFIX
        + "\n\n"
        + body.rstrip()
        + "\n"
    )


def taskbook_review(meta: dict[str, Any]) -> dict[str, Any] | None:
    review = meta.get("policy_review")
    return review if isinstance(review, dict) else None


def override_map(meta: dict[str, Any]) -> dict[str, dict[str, Any]]:
    review = taskbook_review(meta) or {}
    overrides = review.get("temporary_overrides", [])
    out: dict[str, dict[str, Any]] = {}
    if isinstance(overrides, list):
        for item in overrides:
            if isinstance(item, dict) and isinstance(item.get("conflict_id"), str):
                out[item["conflict_id"]] = item
    return out


def regex_hits(body: str, patterns: list[str]) -> list[str]:
    hits: list[str] = []
    for pat in patterns:
        if re.search(pat, body, flags=re.IGNORECASE | re.MULTILINE):
            hits.append(pat)
    return hits


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


def origin_findings(
    meta: dict[str, Any], *, dispatch: bool, root: Path = ROOT
) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    origin = meta.get("origin_kind")
    if origin is None:
        findings.append({
            "severity": "ERROR" if dispatch else "WARN",
            "code": "TB-ORIGIN-MISSING",
            "message": "new dispatch requires origin_kind; legacy files may remain historical until redispatch",
        })
        return findings
    if origin not in VALID_ORIGINS:
        findings.append({
            "severity": "ERROR",
            "code": "TB-ORIGIN-VALUE",
            "message": f"origin_kind must be one of {sorted(VALID_ORIGINS)}, got {origin!r}",
        })
        return findings

    contract = load_json(root / "research_taskbook_contract.json")["task_origin_contract"]
    if origin == "FREE_AXIOM_CANDIDATE":
        for field in contract["free_candidate_required_fields"]:
            if not _nonempty(meta.get(field)):
                findings.append({
                    "severity": "ERROR",
                    "code": "TB-ORIGIN-CANDIDATE",
                    "message": f"FREE_AXIOM_CANDIDATE origin requires {field}",
                })
        state = meta.get("origin_candidate_state")
        if _nonempty(state) and state not in contract["free_candidate_allowed_states"]:
            findings.append({
                "severity": "ERROR",
                "code": "TB-ORIGIN-CANDIDATE-STATE",
                "message": "free candidate origin must already be in an audited intake-eligible state",
            })
    elif origin == "FOUNDATION_QUESTION":
        field = contract["foundation_question_required_field"]
        if not _nonempty(meta.get(field)):
            findings.append({
                "severity": "ERROR",
                "code": "TB-ORIGIN-FOUNDATION",
                "message": f"FOUNDATION_QUESTION origin requires {field}",
            })
    return findings


def lineage_findings(
    meta: dict[str, Any], *, dispatch: bool, root: Path = ROOT
) -> list[dict[str, str]]:
    findings: list[dict[str, str]] = []
    lineage = meta.get("task_lineage")
    if lineage is None:
        findings.append({
            "severity": "ERROR" if dispatch else "WARN",
            "code": "TB-LINEAGE-MISSING",
            "message": "new dispatch requires task_lineage; legacy files may remain historical until redispatch",
        })
        return findings
    if lineage not in VALID_LINEAGES:
        findings.append({
            "severity": "ERROR",
            "code": "TB-LINEAGE-VALUE",
            "message": f"task_lineage must be one of {sorted(VALID_LINEAGES)}, got {lineage!r}",
        })
        return findings

    stage = _stage_number(meta)
    if stage is not None and stage >= 2 and lineage != "CONTINUATION":
        findings.append({
            "severity": "ERROR",
            "code": "TB-STAGE-LINEAGE",
            "message": f"Stage {stage} task is explicit continuation semantics and must use task_lineage=CONTINUATION",
        })

    parent = meta.get("parent_task_id")
    gate = meta.get("successor_gate")
    if lineage == "CONTINUATION":
        if not isinstance(parent, str) or not parent.strip():
            findings.append({
                "severity": "ERROR",
                "code": "TB-SUCCESSOR-PARENT",
                "message": "CONTINUATION requires nonempty parent_task_id",
            })
        contract = load_json(root / "research_taskbook_contract.json")["task_lineage_contract"]
        required = contract["continuation_required_successor_gate_fields"]
        if not isinstance(gate, dict):
            findings.append({
                "severity": "ERROR",
                "code": "TB-SUCCESSOR-GATE",
                "message": "CONTINUATION requires successor_gate object",
            })
        else:
            for field in required:
                if not _nonempty(gate.get(field)):
                    findings.append({
                        "severity": "ERROR",
                        "code": "TB-SUCCESSOR-GATE",
                        "message": f"CONTINUATION successor_gate missing/nonempty field: {field}",
                    })
    elif _nonempty(parent) or _nonempty(gate):
        findings.append({
            "severity": "WARN",
            "code": "TB-LINEAGE-EXTRA",
            "message": "parent_task_id/successor_gate present on non-CONTINUATION lineage; verify that the lineage classification is intentional",
        })
    return findings


def audit_taskbook(path: Path, *, root: Path = ROOT, dispatch: bool = False) -> list[dict[str, str]]:
    policy = policy_manifest(root)
    contract = load_json(root / "research_taskbook_contract.json")
    findings: list[dict[str, str]] = []
    try:
        meta, body = split_taskbook(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [{"severity": "ERROR", "code": "TB-PARSE", "message": str(exc)}]

    required = contract["new_dispatchable_taskbook_required_metadata"]
    for key, expected in required.items():
        if key not in meta:
            findings.append({"severity": "ERROR", "code": "TB-META", "message": f"missing metadata: {key}"})
        elif isinstance(expected, str) and expected.startswith("<"):
            pass
        elif isinstance(expected, str) and meta[key] != expected:
            findings.append({"severity": "ERROR", "code": "TB-META", "message": f"{key} must be {expected!r}"})

    findings.extend(origin_findings(meta, dispatch=dispatch, root=root))
    findings.extend(lineage_findings(meta, dispatch=dispatch, root=root))

    for key in contract.get("forbidden_fixed_runtime_metadata", []):
        if key in meta:
            findings.append({"severity": "ERROR", "code": "TB-RUNTIME-META", "message": f"forbidden fixed runtime metadata: {key}"})

    review = taskbook_review(meta)
    if review is None:
        sev = "ERROR" if dispatch else "WARN"
        findings.append({
            "severity": sev,
            "code": "TB-POLICY-UNSTAMPED",
            "message": "taskbook has no policy_review stamp; legacy files may remain archived, but dispatch requires review",
        })
        overrides: dict[str, dict[str, Any]] = {}
    else:
        overrides = override_map(meta)
        if review.get("policy_set") != "research_taskbook_policy.json":
            findings.append({"severity": "ERROR", "code": "TB-POLICY-SET", "message": "policy_review.policy_set must be research_taskbook_policy.json"})
        current = policy_digest(root)
        if review.get("policy_digest") != current:
            findings.append({
                "severity": "ERROR" if dispatch else "WARN",
                "code": "TB-POLICY-STALE",
                "message": f"policy digest stale: taskbook={review.get('policy_digest')} current={current}",
            })
        if dispatch and review.get("review_state") != "PASS":
            findings.append({"severity": "ERROR", "code": "TB-POLICY-REVIEW", "message": "dispatch requires policy_review.review_state=PASS"})

        required_override_fields = policy.get("override_required_fields", [])
        for cid, item in overrides.items():
            for field in required_override_fields:
                if not item.get(field):
                    findings.append({"severity": "ERROR", "code": "TB-OVERRIDE-SCHEMA", "message": f"override {cid} missing {field}"})

    for check in policy.get("conflict_checks", []):
        hits = regex_hits(body, check["patterns"])
        if hits and check["id"] not in overrides:
            findings.append({
                "severity": check.get("severity", "ERROR"),
                "code": check["id"],
                "message": "policy-sensitive task-local directive found without explicit temporary override: " + ", ".join(hits),
            })

    for check in policy.get("restatement_checks", []):
        hits = regex_hits(body, check["patterns"])
        if hits:
            findings.append({
                "severity": check.get("severity", "ERROR"),
                "code": check["id"],
                "message": "generic repository policy is restated in taskbook; remove it and inherit the repository rule: " + ", ".join(hits),
            })

    return findings


def print_findings(path: Path, findings: list[dict[str, str]]) -> None:
    if not findings:
        print(f"{path}: PASS")
        return
    for item in findings:
        print(f"{path}: {item['severity']} {item['code']}: {item['message']}")


def command_audit(args: argparse.Namespace) -> int:
    if args.all:
        paths = sorted((ROOT / "research_tasks").glob("*.md"))
    else:
        paths = [Path(p) if Path(p).is_absolute() else ROOT / p for p in args.paths]
    if not paths:
        raise SystemExit("no taskbooks selected")
    errors = 0
    for path in paths:
        findings = audit_taskbook(path, dispatch=args.dispatch)
        display = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        print_findings(display, findings)
        errors += sum(item["severity"] == "ERROR" for item in findings)
    return 1 if errors else 0


def base_metadata(args: argparse.Namespace) -> dict[str, Any]:
    if args.origin_kind == "FREE_AXIOM_CANDIDATE":
        if not args.origin_candidate_id or not args.origin_candidate_state:
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
        "created_by_role": "RESEARCH_DRIVER",
        "task_authority": "DRIVER_APPROVED",
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
            "review_state": "PENDING_DRIVER_REVIEW",
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

Status: `DRAFT / POLICY_REVIEW_PENDING / NOT DISPATCHABLE`

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
    print("created with PENDING_DRIVER_REVIEW; edit task-local content, complete any successor gate, then run review --approve")
    return 0


def command_review(args: argparse.Namespace) -> int:
    path = Path(args.path)
    if not path.is_absolute():
        path = ROOT / path
    text = path.read_text(encoding="utf-8")
    meta, body = split_taskbook(text)
    meta["final_response_identity_policy"] = "INHERIT_GLOBAL"
    review = taskbook_review(meta) or {"policy_set": "research_taskbook_policy.json", "temporary_overrides": []}
    review["policy_set"] = "research_taskbook_policy.json"
    review["policy_digest"] = policy_digest(ROOT)
    review["review_state"] = "PENDING_DRIVER_REVIEW"
    meta["policy_review"] = review
    path.write_text(render_taskbook(meta, body), encoding="utf-8")

    findings = audit_taskbook(path, dispatch=False)
    blocking = [f for f in findings if f["severity"] == "ERROR"]
    if blocking:
        print_findings(path.relative_to(ROOT), findings)
        print("review not approved")
        return 1

    if args.approve:
        review["review_state"] = "PASS"
        meta["policy_review"] = review
        if meta.get("base_state") == "DRAFT":
            meta["base_state"] = "READY"
        path.write_text(render_taskbook(meta, body), encoding="utf-8")
        dispatch_findings = audit_taskbook(path, dispatch=True)
        if any(f["severity"] == "ERROR" for f in dispatch_findings):
            print_findings(path.relative_to(ROOT), dispatch_findings)
            return 1
        print(f"{path.relative_to(ROOT)}: POLICY_REVIEW_PASS")
        return 0

    print(f"{path.relative_to(ROOT)}: review refreshed; approval still pending")
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
    audit.add_argument("--dispatch", action="store_true")
    audit.set_defaults(func=command_audit)

    review = sp.add_parser("review")
    review.add_argument("path")
    review.add_argument("--approve", action="store_true")
    review.set_defaults(func=command_review)

    digest = sp.add_parser("policy-digest")
    digest.set_defaults(func=command_digest)

    args = p.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())