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


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def policy_manifest(root: Path = ROOT) -> dict[str, Any]:
    return load_json(root / "research_taskbook_policy.json")


def policy_digest(root: Path = ROOT) -> str:
    policy = policy_manifest(root)
    h = hashlib.sha256()
    paths = ["research_taskbook_policy.json", *policy["policy_inputs"]]
    for rel in paths:
        path = root / rel
        data = path.read_bytes()
        h.update(rel.encode("utf-8"))
        h.update(b"\0")
        h.update(hashlib.sha256(data).digest())
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
        elif isinstance(expected, str) and meta[key] != expected:
            findings.append({"severity": "ERROR", "code": "TB-META", "message": f"{key} must be {expected!r}"})

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
    return {
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
        "identity_lane": args.lane,
        "policy_review": {
            "policy_set": "research_taskbook_policy.json",
            "policy_digest": policy_digest(ROOT),
            "review_state": "PENDING_DRIVER_REVIEW",
            "temporary_overrides": [],
        },
    }


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

<task-specific PASS/KILL conditions>
"""
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_taskbook(meta, body), encoding="utf-8")
    print(out.relative_to(ROOT))
    print("created with PENDING_DRIVER_REVIEW; edit task-local content, then run review --approve")
    return 0


def command_review(args: argparse.Namespace) -> int:
    path = Path(args.path)
    if not path.is_absolute():
        path = ROOT / path
    text = path.read_text(encoding="utf-8")
    meta, body = split_taskbook(text)
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
