#!/usr/bin/env python3
"""One-shot canonical publication of the EBP6JT successor task pair.

This script is intentionally branch-scoped. It uses the repository's unchanged
research_taskbook/research_task_records machinery for policy review and immutable
V2 publication. It creates no CLAIM, Working Truth, review, or theorem promotion.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
HANDOFF_DIR = ROOT / "research_handoffs/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_JACOBI_JET_20260909"
BRANCH = "handoff/ebp6jt-successors-20260909-25c94a"
PARENT_TASK = "RS-ENTERPRISE-BRC-HALF-COUPLING-INERT-PLUS-TERMINATING-JACOBI-JET-CERTIFICATE"
PUBLISHER_ID = "EM-EBP6JT-25C94A"
PARENT_OBJECTIVE = "ENTERPRISE_BOTTOM_LAYER_LOGIC_BLIND_VALIDATION"
HANDOFF_COMMIT = "399f2b5af8dcc993d7cb88f036c10f1c0029ebb6"

sys.path.insert(0, str(ROOT))
from control_plane import research_control_bootstrap  # noqa: E402
research_control_bootstrap.install(ROOT)
from tools import research_taskbook, research_task_records  # noqa: E402


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def run(args: list[str], log_name: str) -> str:
    cp = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    HANDOFF_DIR.mkdir(parents=True, exist_ok=True)
    (HANDOFF_DIR / log_name).write_text(cp.stdout + cp.stderr, encoding="utf-8")
    if cp.returncode:
        raise RuntimeError(f"{args!r}: exit {cp.returncode}\n{cp.stdout}\n{cp.stderr}")
    return cp.stdout


def save(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def build_draft(spec: dict, policy_digest: str) -> str:
    task_id = spec["task_id"]
    meta = {
        "task_id": task_id,
        "title": spec["title"],
        "kind": "RESEARCH",
        "owner": spec["owner"],
        "base_state": "DRAFT",
        "priority": spec["priority"],
        "leverage": spec["leverage"],
        "frontier": spec["frontier"],
        "next_action": spec["next_action"],
        "dependencies": spec["dependencies"],
        "source_refs": spec["source_refs"],
        "evidence_status": spec["evidence_status"],
        "last_progress_ref": f"research_handoffs/ENTERPRISE_BRC_HALF_COUPLING_INERT_PLUS_JACOBI_JET_20260909/RESEARCH_HANDOFF.md@{HANDOFF_COMMIT}",
        "last_progress_at": "2026-09-09T02:20:00+00:00",
        "hard_block": None,
        "tags": spec["tags"],
        "claim_lease_minutes": 240,
        "created_by_role": "RESEARCHER",
        "task_authority": "PENDING_PUBLICATION",
        "publication_contract": "RESEARCH_TASK_PUBLICATION_V1",
        "publication_template": "RESEARCH_TASK_PUBLICATION_TEMPLATE_V1",
        "registry_key": task_id,
        "parent_objective_id": PARENT_OBJECTIVE,
        "identity_policy": "AUTO_RESOLVE_OR_ALLOCATE",
        "final_response_identity_policy": "INHERIT_GLOBAL",
        "identity_lane": spec["identity_lane"],
        "origin_kind": "DIRECT_USER_DIRECTION",
        "task_lineage": "CONTINUATION",
        "parent_task_id": PARENT_TASK,
        "successor_gate": spec["successor_gate"],
        "policy_review": {
            "policy_set": "research_taskbook_policy.json",
            "policy_digest": policy_digest,
            "review_state": "PENDING_POLICY_REVIEW",
            "temporary_overrides": [],
        },
    }
    return research_taskbook.render_taskbook(meta, spec["body"])


def parse_publish_output(text: str) -> dict:
    start = text.find("{")
    if start < 0:
        raise RuntimeError("canonical publish returned no JSON record")
    return json.loads(text[start:])


def main() -> None:
    if os.environ.get("GITHUB_REF_NAME") != BRANCH:
        raise RuntimeError("publisher is restricted to its dedicated branch")

    request = json.loads((HERE / "request.json").read_text(encoding="utf-8"))
    if request.get("schema") != "EBP6JT_SUCCESSOR_PUBLICATION_REQUEST_V1":
        raise RuntimeError("invalid publication request schema")
    if request.get("publisher_id") != PUBLISHER_ID:
        raise RuntimeError("publication request publisher mismatch")
    if request.get("handoff_commit") != HANDOFF_COMMIT:
        raise RuntimeError("publication request handoff pin mismatch")

    raw_specs = (HERE / "task_specs.json").read_bytes()
    if request.get("task_spec_git_blob_sha1") != git_blob_sha1(raw_specs):
        raise RuntimeError("publication request does not bind the exact task specifications")
    specs = json.loads(raw_specs)
    if specs.get("schema") != "EBP6JT_SUCCESSOR_TASK_SPECS_V1":
        raise RuntimeError("invalid task spec schema")
    if specs.get("publisher_id") != PUBLISHER_ID or specs.get("parent_objective_id") != PARENT_OBJECTIVE:
        raise RuntimeError("task spec publisher/parent objective mismatch")
    if specs.get("handoff_commit") != HANDOFF_COMMIT:
        raise RuntimeError("task spec handoff pin mismatch")

    receipt_path = HANDOFF_DIR / "publication_receipt.json"
    if receipt_path.exists():
        old = json.loads(receipt_path.read_text(encoding="utf-8"))
        if old.get("task_spec_sha256") != sha256(raw_specs):
            raise RuntimeError("existing publication receipt binds different task specs")
        run([sys.executable, "tools/research_task_records.py", "audit"], "record_audit.log")
        print("Verified existing EBP6JT successor publication; no duplicate tasks created")
        return

    run([sys.executable, "tools/research_task_records.py", "audit"], "baseline_record_audit.log")
    current = research_task_records.current_records(ROOT)
    task_ids = [spec["task_id"] for spec in specs["tasks"]]
    existing_exact = [task_id for task_id in task_ids if task_id in current]
    if existing_exact:
        raise RuntimeError(f"exact successor already published; reconcile instead of duplicating: {existing_exact}")

    # Bounded semantic dedup against current publication records. This is not a literature search.
    tokens = ("ur-legendre", "qtf3", "unit reciprocity", "frobenius lift")
    semantic_matches = []
    for task_id, record in current.items():
        haystack = json.dumps(record, ensure_ascii=False).lower()
        if any(token in haystack for token in tokens) and record.get("parent_task_id") == PARENT_TASK:
            semantic_matches.append(task_id)
    save(HANDOFF_DIR / "dedup_check.json", {
        "scope": "current immutable V2 publications",
        "exact_task_ids": task_ids,
        "semantic_tokens": list(tokens),
        "matching_parent_continuations": semantic_matches,
    })
    if semantic_matches:
        raise RuntimeError(f"potential duplicate parent continuations require reconciliation: {semantic_matches}")

    if not (HANDOFF_DIR / "RESEARCH_HANDOFF.md").exists() or not (HANDOFF_DIR / "source_manifest.json").exists():
        raise RuntimeError("durable predecessor handoff is missing")

    policy_digest = research_taskbook.policy_digest(ROOT)
    publication_rows = []
    for spec in specs["tasks"]:
        taskbook = ROOT / "research_tasks" / spec["filename"]
        if taskbook.exists():
            raise RuntimeError(f"taskbook already exists before first publication: {taskbook}")
        taskbook.write_text(build_draft(spec, policy_digest), encoding="utf-8")

        research_task_records.prepare_taskbook(
            taskbook,
            publisher_role="RESEARCHER",
            parent_objective_id=PARENT_OBJECTIVE,
            root=ROOT,
        )
        findings = research_taskbook.audit_taskbook(taskbook, root=ROOT, dispatch=True)
        hard = [item for item in findings if item.get("severity") == "ERROR"]
        if hard:
            raise RuntimeError(f"prepared taskbook audit failed for {spec['task_id']}: {hard}")

        output = run([
            sys.executable,
            "tools/research_task_records.py",
            "publish",
            "--taskbook", taskbook.relative_to(ROOT).as_posix(),
            "--publisher-role", "RESEARCHER",
            "--publisher-id", PUBLISHER_ID,
            "--research-value", spec["research_value"],
            "--published-at", "2026-09-09T02:30:00+00:00",
        ], f"publish_{spec['identity_lane'].lower()}.log")
        row = parse_publish_output(output)
        publication_rows.append({
            "task_id": row["task_id"],
            "publication_id": row["publication_id"],
            "taskbook_path": row["taskbook_path"],
            "taskbook_blob_sha1": row["taskbook_blob_sha1"],
            "record_path": row["record_path"],
            "requested_priority": spec["priority"],
            "requested_leverage": spec["leverage"],
            "effective_priority": row["effective_priority"],
            "effective_leverage": row["effective_leverage"],
            "claimable": row["claimable"],
        })

    run([sys.executable, "tools/research_task_records.py", "audit"], "record_audit.log")
    save(receipt_path, {
        "schema": "EBP6JT_SUCCESSOR_PUBLICATION_RECEIPT_V1",
        "status": "CANONICAL_TOOLS_PASS_ON_STAGING_BRANCH",
        "publisher_role": "RESEARCHER",
        "publisher_id": PUBLISHER_ID,
        "parent_task_id": PARENT_TASK,
        "parent_objective_id": PARENT_OBJECTIVE,
        "handoff_commit": HANDOFF_COMMIT,
        "task_spec_git_blob_sha1": git_blob_sha1(raw_specs),
        "task_spec_sha256": sha256(raw_specs),
        "publications": publication_rows,
        "claim_created": False,
        "working_truth_granted": False,
        "canonical_promotion_granted": False,
        "note": "Taskbooks and immutable V2 records passed the repository's canonical publication audit on the owned staging branch. Main authority begins only after complete integration and immutable readback.",
    })
    print(json.dumps(publication_rows, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
