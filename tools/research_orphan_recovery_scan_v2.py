#!/usr/bin/env python3
"""Recover dangling research frontiers into existing Enterprise Math state vocabularies.

This tool never creates a CLAIM and never asserts ordinary task availability.
It separates exact durable branch residue from already integrated/referenced/
descendant-covered history, then emits:

- TASK_RESEARCH residue -> fail-closed BLOCKED recovery capsules;
- FREE_RESEARCH residue -> FREE axiom-candidate DISCOVERY_IN_PROGRESS capsules.

A Driver may later reconcile a BLOCKED task capsule to an exact existing task or
publish a new V2 task deliberately.  FREE capsules remain outside ordinary task
dispatch until the existing candidate state machine promotes them.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA = "ENTERPRISE_MATH_RESEARCH_ORPHAN_RECOVERY_STATE_V1"
PREFIXES = ("research/", "research-task/", "free/")
TEXT_SUFFIXES = {".json", ".md", ".txt", ".yaml", ".yml", ".lean", ".py"}
BRANCH_TOKEN_RE = re.compile(r"(?:free|research|research-task)/[A-Za-z0-9._/-]+")
SHA_RE = re.compile(r"(?<![0-9a-f])[0-9a-f]{40}(?![0-9a-f])")
TASK_PATH_RE = re.compile(r"^research_task_records/([^/]+)/([^/]+)\.json$")
RESULT_PATH_RE = re.compile(r"^research_result_records/([^/]+)/([^/]+)\.json$")
EXEC_PATH_RE = re.compile(r"^research_execution_records/([^/]+)/")


def run(args: list[str], *, check: bool = True) -> str:
    p = subprocess.run(args, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and p.returncode:
        raise RuntimeError(f"command failed {args!r}: {p.stderr.strip()}")
    return p.stdout.strip()


def git(*args: str, check: bool = True) -> str:
    return run(["git", *args], check=check)


def parse_body(body: str) -> dict[str, Any] | None:
    s = (body or "").strip()
    choices = [s]
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", s, re.S)
    if m:
        choices.append(m.group(1))
    i, j = s.find("{"), s.rfind("}")
    if i >= 0 and j > i:
        choices.append(s[i:j + 1])
    for candidate in choices:
        try:
            value = json.loads(candidate)
        except Exception:
            continue
        if isinstance(value, dict):
            return value
    return None


def load_events(path: Path | None) -> list[dict[str, Any]]:
    if not path:
        return []
    raw = json.loads(path.read_text())
    out: list[dict[str, Any]] = []
    for item in raw if isinstance(raw, list) else []:
        if not isinstance(item, dict):
            continue
        value = parse_body(str(item.get("body", "")))
        if not value:
            continue
        value = dict(value)
        value["_server_comment_id"] = item.get("id")
        value["_server_created_at"] = item.get("created_at")
        out.append(value)
    return out


def main_state_index() -> tuple[set[str], set[str], int]:
    branch_tokens: set[str] = set()
    sha_tokens: set[str] = set()
    files = 0
    prefixes = (
        "research_task_records/", "research_result_records/",
        "research_execution_records/", "research_tasks/",
        "driver_reviews/", "control_plane/",
    )
    for rel in git("ls-files").splitlines():
        p = Path(rel)
        if p.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if not (rel.startswith(prefixes) or "candidate" in rel.lower()):
            continue
        try:
            text = p.read_text(errors="replace")
        except OSError:
            continue
        if len(text) > 2_000_000:
            continue
        files += 1
        branch_tokens.update(BRANCH_TOKEN_RE.findall(text))
        sha_tokens.update(SHA_RE.findall(text))
    return branch_tokens, sha_tokens, files


def remote_branches() -> list[str]:
    out: list[str] = []
    for ref in git("for-each-ref", "--format=%(refname:short)", "refs/remotes/origin/").splitlines():
        if not ref.startswith("origin/") or ref == "origin/main" or ref.endswith("/HEAD"):
            continue
        branch = ref[len("origin/"):]
        if branch.startswith(PREFIXES):
            out.append(branch)
    return sorted(set(out))


def free_evidence(branch: str, commit_message: str) -> list[str]:
    evidence: list[str] = []
    low = branch.lower()
    msg = commit_message.lower()
    if branch.startswith("free/"):
        evidence.append("FREE_BRANCH_PREFIX")
    if branch.startswith("research/free-") or "-em-free-" in low or low.startswith("research/em-free-"):
        evidence.append("EXPLICIT_FREE_BRANCH_NAMING")
    if "free_research" in msg or "free research" in msg or "free researcher" in msg or "free_axiom" in msg:
        evidence.append("EXPLICIT_FREE_COMMIT_MARKER")
    return evidence


def branch_meta(branch: str) -> dict[str, Any]:
    tip = git("rev-parse", f"origin/{branch}")
    commit_message = git("show", "-s", "--format=%B", tip)
    fields = git("show", "-s", "--format=%cI%x00%s", tip).split("\x00", 1)
    cherry = git("cherry", "origin/main", f"origin/{branch}", check=False)
    plus: list[str] = []
    minus = 0
    for line in cherry.splitlines():
        if line.startswith("+"):
            plus.append(line[2:].strip())
        elif line.startswith("-"):
            minus += 1
    evidence = free_evidence(branch, commit_message)
    return {
        "branch": branch,
        "lane": "FREE_RESEARCH" if evidence else "TASK_RESEARCH",
        "free_lane_evidence": evidence,
        "tip_sha": tip,
        "tip_at": fields[0] if fields else None,
        "tip_subject": fields[1] if len(fields) > 1 else "",
        "unmerged_patch_commits": len(plus),
        "patch_equivalent_commits": minus,
        "unique_commit_shas": plus,
    }


def exact_descendant_cover(rows: list[dict[str, Any]]) -> dict[str, str]:
    """Collapse a frontier only when another scanned remote branch exactly contains its tip."""
    by_branch = {r["branch"]: r for r in rows}
    live = [r for r in rows if r["unmerged_patch_commits"] > 0]
    cover: dict[str, str] = {}
    for row in live:
        refs = git("branch", "-r", "--contains", row["tip_sha"], check=False).splitlines()
        candidates: list[dict[str, Any]] = []
        for raw in refs:
            ref = raw.strip().lstrip("*").strip()
            if not ref.startswith("origin/"):
                continue
            branch = ref[len("origin/"):]
            if branch == row["branch"] or branch == "main":
                continue
            other = by_branch.get(branch)
            if other and other["unmerged_patch_commits"] > 0:
                candidates.append(other)
        if candidates:
            candidates.sort(key=lambda x: (x.get("tip_at") or "", x["branch"]))
            cover[row["branch"]] = candidates[-1]["branch"]
    return cover


def event_index(events: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    out: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        branch = event.get("execution_branch")
        if isinstance(branch, str):
            out[branch].append(event)
    return out


def changed_provenance(branch: str) -> dict[str, Any]:
    base = git("merge-base", "origin/main", f"origin/{branch}")
    paths = [p for p in git("diff", "--name-only", f"{base}..origin/{branch}", check=False).splitlines() if p]
    task_ids: set[str] = set()
    publication_ids: set[str] = set()
    result_ids: set[str] = set()
    for path in paths:
        m = TASK_PATH_RE.match(path)
        if m:
            task_ids.add(m.group(1)); publication_ids.add(m.group(2))
        m = RESULT_PATH_RE.match(path)
        if m:
            task_ids.add(m.group(1)); result_ids.add(m.group(2))
        m = EXEC_PATH_RE.match(path)
        if m:
            task_ids.add(m.group(1))
    return {
        "merge_base": base,
        "changed_file_count": len(paths),
        "changed_files_sample": paths[:24],
        "exact_task_ids": sorted(task_ids),
        "publication_ids": sorted(publication_ids),
        "result_ids": sorted(result_ids),
    }


def recovery_id(prefix: str, branch: str, tip: str) -> str:
    digest = hashlib.sha256(f"{branch}\0{tip}".encode()).hexdigest()[:16].upper()
    return f"{prefix}-{digest}"


def compact_event(event: dict[str, Any]) -> dict[str, Any]:
    return {
        "event": event.get("event"),
        "task_id": event.get("task_id"),
        "publication_id": event.get("publication_id"),
        "claim_id": event.get("claim_id"),
        "result_id": event.get("result_id"),
        "server_comment_id": event.get("_server_comment_id"),
        "at": event.get("at") or event.get("_server_created_at"),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--events", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    branch_tokens, sha_tokens, corpus_files = main_state_index()
    events = load_events(args.events)
    events_by_branch = event_index(events)
    rows = [branch_meta(branch) for branch in remote_branches()]
    cover = exact_descendant_cover(rows)

    exclusions = Counter()
    task_recovery: list[dict[str, Any]] = []
    free_recovery: list[dict[str, Any]] = []

    for row in rows:
        branch = row["branch"]
        tip = row["tip_sha"]
        if row["unmerged_patch_commits"] == 0:
            exclusions["INTEGRATED_OR_PATCH_EQUIVALENT"] += 1
            continue
        if branch in cover:
            exclusions["COVERED_BY_EXACT_DESCENDANT_BRANCH"] += 1
            continue
        refs = {"branch_mentioned": branch in branch_tokens, "tip_mentioned": tip in sha_tokens}
        branch_events = events_by_branch.get(branch, [])
        if branch_events:
            exclusions["EXISTING_ISSUE240_CONTROL_LINEAGE"] += 1
            continue
        if refs["branch_mentioned"] or refs["tip_mentioned"]:
            exclusions["EXISTING_MAIN_STATE_REFERENCE"] += 1
            continue

        provenance = changed_provenance(branch)
        base = {
            "source_branch": branch,
            "source_tip_sha": tip,
            "source_tip_at": row["tip_at"],
            "source_tip_subject": row["tip_subject"],
            "unmerged_patch_commits": row["unmerged_patch_commits"],
            "free_lane_evidence": row["free_lane_evidence"],
            "provenance": provenance,
        }
        if row["lane"] == "FREE_RESEARCH":
            free_recovery.append({
                "recovery_id": recovery_id("OFR", branch, tip),
                "state_machine": "research_axiom_candidate_state_machine.json",
                "state": "DISCOVERY_IN_PROGRESS",
                "ordinary_dispatch_eligible": False,
                "promotion": "NOT_PERFORMED",
                "next_action": "Resume from the durable frontier, audit the candidate under the existing FREE state machine, then explicitly promote/reject/park according to that machine.",
                **base,
            })
        else:
            exact_tasks = provenance["exact_task_ids"]
            task_recovery.append({
                "recovery_id": recovery_id("OTR", branch, tip),
                "state_machine": "TASK_RESEARCH_RUNTIME",
                "state": "BLOCKED",
                "dispatch_state": "BLOCKED",
                "ordinary_dispatch_eligible": False,
                "task_id": exact_tasks[0] if len(exact_tasks) == 1 else None,
                "hard_block": {
                    "code": "ORPHAN_BRANCH_REQUIRES_CANONICAL_RECONCILIATION" if exact_tasks else "ORPHAN_EXACT_TASK_PROVENANCE_REQUIRED",
                    "missing_object": "Canonical task/publication reconciliation for this durable branch frontier",
                    "owner": "Driver/control maintenance",
                    "necessity": "Prevent an unowned durable frontier from disappearing or being redispatched without provenance.",
                    "unblock_condition": "Driver either binds this capsule to the exact current V2 task/publication and preserved lifecycle, supersedes it as duplicate/history, or deliberately republishes a successor through the normal V2 contract.",
                },
                "next_action": "Reconcile exact provenance; do not CLAIM this recovery capsule directly.",
                **base,
            })

    task_recovery.sort(key=lambda x: (x.get("source_tip_at") or "", x["source_branch"]), reverse=True)
    free_recovery.sort(key=lambda x: (x.get("source_tip_at") or "", x["source_branch"]), reverse=True)
    result = {
        "schema": SCHEMA,
        "status": "ACTIVE_RECOVERY_STATE / NOT_TASK_AVAILABILITY / NO_CLAIM_AUTHORITY",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_main_sha": git("rev-parse", "origin/main"),
        "contracts": {
            "task_publication": "research_task_publication_contract_v2.json",
            "task_runtime": "research_control_dispatch.py -> tools/research_dispatch.py -> tools/research_runtime_reducer.py",
            "free_candidate_state_machine": "research_axiom_candidate_state_machine.json",
        },
        "invariants": [
            "BRANCH_PRESENCE != ORPHAN",
            "PATCH_EQUIVALENT_TO_MAIN != ORPHAN",
            "EXACT_DESCENDANT_COVERAGE != ORPHAN",
            "EXISTING_ISSUE240_OR_MAIN_STATE_REFERENCE != ORPHAN",
            "RECOVERY_CAPSULE != TASK_AVAILABILITY",
            "RECOVERY_CAPSULE != CLAIM",
            "TASK_ORPHAN -> BLOCKED_UNTIL_PROVENANCE_RECONCILIATION",
            "FREE_ORPHAN -> DISCOVERY_IN_PROGRESS_NOT_AUTOMATIC_TASK",
        ],
        "inputs": {
            "branch_prefixes": list(PREFIXES),
            "raw_issue_240_comments": len(json.loads(args.events.read_text())) if args.events else 0,
            "parsed_control_events": len(events),
            "main_state_corpus_files": corpus_files,
            "branches_scanned": len(rows),
        },
        "summary": {
            "branches_scanned": len(rows),
            "recovered_task_frontiers": len(task_recovery),
            "recovered_free_frontiers": len(free_recovery),
            "total_recovery_capsules": len(task_recovery) + len(free_recovery),
            "exclusion_counts": dict(sorted(exclusions.items())),
        },
        "task_recovery": task_recovery,
        "free_recovery": free_recovery,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
