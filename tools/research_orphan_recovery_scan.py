#!/usr/bin/env python3
"""Audit dangling Enterprise Math research branches without creating claims.

This scanner is deliberately authority-conservative.  It discovers durable branch
frontiers that are not patch-equivalent to main and projects them onto the
existing TASK_RESEARCH or FREE axiom-candidate state machines.  The output is an
audit/recovery input, never task-availability or claim authority.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

SCHEMA = "ENTERPRISE_MATH_RESEARCH_ORPHAN_RECOVERY_SCAN_V1"
FREE_STATE_MACHINE = "research_axiom_candidate_state_machine.json"
TASK_CONTRACT = "research_task_publication_contract_v2.json"
BRANCH_PREFIXES = ("research/", "research-task/", "free/")
TEXT_SUFFIXES = {".json", ".md", ".txt", ".yaml", ".yml", ".lean", ".py"}
FREE_STATES = {
    "DISCOVERY_IN_PROGRESS", "BLIND_CANDIDATE_FROZEN",
    "PHASE_B_AUDIT_IN_PROGRESS", "FALSIFIED", "DUPLICATE_OR_ALREADY_KNOWN",
    "DERIVED_NOT_AXIOM", "IMPLEMENTATION_ARTIFACT", "PRIOR_ART_ANALOGUE",
    "EXACT_NEGATIVE_OBSTRUCTION", "AUDITED_AXIOM_CANDIDATE",
    "AUDITED_REPLACEMENT_CANDIDATE", "TASK_PUBLICATION_ELIGIBLE",
    "DRIVER_INTAKE", "PARKED", "REJECTED", "INDEPENDENT_REPLICATION_REQUESTED",
    "PROMOTED_TO_EXPLICIT_TASK", "PROMOTED_TO_FOUNDATION_QUESTION", "CANONICALIZED",
}


def sh(*args: str, check: bool = True) -> str:
    p = subprocess.run(args, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and p.returncode:
        raise RuntimeError(f"command failed {args!r}: {p.stderr.strip()}")
    return p.stdout.strip()


def git(*args: str, check: bool = True) -> str:
    return sh("git", *args, check=check)


def parse_json_body(body: str) -> dict[str, Any] | None:
    body = (body or "").strip()
    candidates = [body]
    m = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", body, re.S)
    if m:
        candidates.append(m.group(1))
    first, last = body.find("{"), body.rfind("}")
    if first >= 0 and last > first:
        candidates.append(body[first:last + 1])
    for text in candidates:
        try:
            value = json.loads(text)
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
        value = parse_json_body(str(item.get("body", "")))
        if value:
            value = dict(value)
            value["_server_comment_id"] = item.get("id")
            value["_server_created_at"] = item.get("created_at")
            out.append(value)
    return out


def tracked_text_corpus() -> tuple[str, list[str]]:
    paths = git("ls-files").splitlines()
    selected: list[str] = []
    chunks: list[str] = []
    for rel in paths:
        p = Path(rel)
        if p.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if not (
            rel.startswith("research_task_records/")
            or rel.startswith("research_result_records/")
            or rel.startswith("research_execution_records/")
            or rel.startswith("control_plane/")
            or rel.startswith("research_tasks/")
            or "candidate" in rel.lower()
        ):
            continue
        try:
            text = p.read_text(errors="replace")
        except OSError:
            continue
        if len(text) > 2_000_000:
            continue
        selected.append(rel)
        chunks.append(f"\n@@PATH:{rel}\n{text}")
    return "".join(chunks), selected


def refs() -> list[str]:
    raw = git("for-each-ref", "--format=%(refname:short)", "refs/remotes/origin/")
    names = []
    for ref in raw.splitlines():
        if ref == "origin/main" or ref.endswith("/HEAD"):
            continue
        if not ref.startswith("origin/"):
            continue
        name = ref[len("origin/"):]
        if name.startswith(BRANCH_PREFIXES):
            names.append(name)
    return sorted(set(names))


def cherry_plus(branch: str) -> tuple[int, int, list[str]]:
    out = git("cherry", "origin/main", f"origin/{branch}", check=False)
    plus = minus = 0
    commits: list[str] = []
    for line in out.splitlines():
        if not line:
            continue
        if line[0] == "+":
            plus += 1
            commits.append(line[2:].strip())
        elif line[0] == "-":
            minus += 1
    return plus, minus, commits


def branch_meta(branch: str) -> dict[str, Any]:
    tip = git("rev-parse", f"origin/{branch}")
    fields = git("show", "-s", "--format=%cI%x00%s", tip).split("\x00", 1)
    plus, minus, commits = cherry_plus(branch)
    return {
        "branch": branch,
        "lane": "FREE_RESEARCH" if branch.startswith("free/") else "TASK_RESEARCH",
        "tip_sha": tip,
        "tip_at": fields[0] if fields else None,
        "tip_subject": fields[1] if len(fields) > 1 else "",
        "unmerged_patch_commits": plus,
        "patch_equivalent_commits": minus,
        "unique_commit_shas": commits,
    }


def descendant_cover(free_rows: list[dict[str, Any]]) -> dict[str, str]:
    """Collapse only exact ancestry; never infer semantic equivalence from names."""
    covered: dict[str, str] = {}
    ordered = sorted(free_rows, key=lambda r: r.get("tip_at") or "")
    for i, row in enumerate(ordered):
        if row["unmerged_patch_commits"] <= 0:
            continue
        tip = row["tip_sha"]
        best: dict[str, Any] | None = None
        for other in ordered[i + 1:]:
            if other["unmerged_patch_commits"] <= 0:
                continue
            rc = subprocess.run(
                ["git", "merge-base", "--is-ancestor", tip, other["tip_sha"]],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            ).returncode
            if rc == 0:
                best = other
        if best:
            covered[row["branch"]] = best["branch"]
    return covered


def event_index(events: list[dict[str, Any]]) -> tuple[dict[str, list[dict[str, Any]]], dict[str, list[dict[str, Any]]]]:
    by_branch: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_task: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for e in events:
        b = e.get("execution_branch")
        t = e.get("task_id")
        if isinstance(b, str):
            by_branch[b].append(e)
        if isinstance(t, str):
            by_task[t].append(e)
    return by_branch, by_task


def main_refs(corpus: str, row: dict[str, Any]) -> dict[str, Any]:
    branch, tip = row["branch"], row["tip_sha"]
    branch_hits = corpus.count(branch)
    tip_hits = corpus.count(tip)
    free_states = sorted(s for s in FREE_STATES if s in corpus and (branch in corpus or tip in corpus))
    return {"branch_mentions": branch_hits, "tip_mentions": tip_hits, "candidate_state_hints": free_states}


def classify(
    row: dict[str, Any],
    *,
    covered: dict[str, str],
    branch_events: dict[str, list[dict[str, Any]]],
    corpus: str,
) -> dict[str, Any]:
    out = dict(row)
    out["main_reference"] = main_refs(corpus, row)
    events = branch_events.get(row["branch"], [])
    out["control_events"] = [
        {
            "event": e.get("event"), "task_id": e.get("task_id"),
            "publication_id": e.get("publication_id"), "claim_id": e.get("claim_id"),
            "result_id": e.get("result_id"), "server_comment_id": e.get("_server_comment_id"),
            "at": e.get("at") or e.get("_server_created_at"),
        }
        for e in events
    ]
    if row["unmerged_patch_commits"] == 0:
        out.update(classification="INTEGRATED_OR_PATCH_EQUIVALENT", actionable=False)
        return out
    if row["branch"] in covered:
        out.update(
            classification="COVERED_BY_DESCENDANT_FREE_BRANCH",
            covered_by=covered[row["branch"]], actionable=False,
        )
        return out
    if row["lane"] == "TASK_RESEARCH":
        if events:
            out.update(
                classification="EXISTING_CONTROL_EVENT_LINEAGE",
                actionable=False,
                projection="PRESERVE_EXISTING_TASK_RUNTIME_STATE",
            )
        else:
            out.update(
                classification="DANGLING_TASK_RESEARCH_FRONTIER",
                actionable=True,
                projection="BLOCKED_RECOVERY_CAPSULE_PENDING_EXACT_TASK_PROVENANCE",
                projected_dispatch_state="BLOCKED",
            )
        return out
    # FREE lane: a main-side durable reference is evidence of some stateful intake.
    refs = out["main_reference"]
    if refs["branch_mentions"] or refs["tip_mentions"]:
        out.update(
            classification="FREE_FRONTIER_WITH_MAIN_STATE_REFERENCE",
            actionable=False,
            projection="PRESERVE_EXISTING_FREE_CANDIDATE_OR_DURABLE_INTAKE",
        )
    else:
        out.update(
            classification="DANGLING_FREE_RESEARCH_FRONTIER",
            actionable=True,
            projection="FREE_AXIOM_CANDIDATE_STATE_MACHINE",
            projected_candidate_state="DISCOVERY_IN_PROGRESS",
        )
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--events", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    corpus, corpus_files = tracked_text_corpus()
    events = load_events(args.events)
    branch_events, _ = event_index(events)
    rows = [branch_meta(b) for b in refs()]
    free_rows = [r for r in rows if r["lane"] == "FREE_RESEARCH"]
    covered = descendant_cover(free_rows)
    classified = [
        classify(r, covered=covered, branch_events=branch_events, corpus=corpus)
        for r in rows
    ]
    actionable = [r for r in classified if r.get("actionable")]
    counts = defaultdict(int)
    for r in classified:
        counts[r["classification"]] += 1
    result = {
        "schema": SCHEMA,
        "status": "AUDIT_ONLY_NOT_DISPATCH_NOT_CLAIM_AUTHORITY",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_main_sha": git("rev-parse", "origin/main"),
        "contracts": {
            "task_publication": TASK_CONTRACT,
            "free_candidate_state_machine": FREE_STATE_MACHINE,
        },
        "invariants": [
            "BRANCH_PRESENCE != ORPHAN",
            "PATCH_EQUIVALENT_TO_MAIN != ORPHAN",
            "ANCESTRY_COVERED_FREE_BRANCH != ORPHAN",
            "AUDIT_OUTPUT != TASK_AVAILABILITY",
            "AUDIT_OUTPUT != CLAIM",
            "DANGLING_FREE_RESEARCH != AUTOMATIC_EXPLICIT_TASK",
            "FREE_RECOVERY_STARTS_AT_DISCOVERY_IN_PROGRESS_UNLESS_EXISTING_AUDIT_PROVES_STRONGER_STATE",
            "DANGLING_TASK_WITHOUT_EXACT_PROVENANCE_FAILS_CLOSED_BLOCKED",
        ],
        "inputs": {
            "remote_branch_prefixes": list(BRANCH_PREFIXES),
            "raw_issue_240_comments": len(json.loads(args.events.read_text())) if args.events else 0,
            "parsed_control_events": len(events),
            "main_state_corpus_files": len(corpus_files),
        },
        "summary": {
            "branches_scanned": len(classified),
            "free_branches_scanned": len(free_rows),
            "actionable_orphan_frontiers": len(actionable),
            "actionable_task_frontiers": sum(r["lane"] == "TASK_RESEARCH" for r in actionable),
            "actionable_free_frontiers": sum(r["lane"] == "FREE_RESEARCH" for r in actionable),
            "classification_counts": dict(sorted(counts.items())),
        },
        "actionable": actionable,
        "all_frontiers": classified,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
