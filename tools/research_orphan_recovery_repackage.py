#!/usr/bin/env python3
"""Repackage a raw orphan scan into existing TASK/FREE state vocabularies.

Input is the audit-only branch inventory.  This pass is intentionally stricter:
- exact descendant coverage is collapsed with one Git graph operation;
- only references recorded against the pre-output main-state corpus count;
- Issue-240 lineages are preserved, never repackaged;
- TASK residue becomes BLOCKED recovery state;
- FREE residue becomes DISCOVERY_IN_PROGRESS candidate state.

Output is recovery state, not task availability and not claim authority.
"""
from __future__ import annotations
import argparse, hashlib, json, subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = "ENTERPRISE_MATH_RESEARCH_ORPHAN_RECOVERY_STATE_V1"


def git(*args: str, check: bool = True) -> str:
    p = subprocess.run(["git", *args], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if check and p.returncode:
        raise RuntimeError(p.stderr.strip())
    return p.stdout.strip()


def rid(prefix: str, branch: str, tip: str) -> str:
    h = hashlib.sha256(f"{branch}\0{tip}".encode()).hexdigest()[:16].upper()
    return f"{prefix}-{h}"


def free_lane(row: dict) -> tuple[bool, list[str]]:
    branch = str(row.get("branch", ""))
    subject = str(row.get("tip_subject", ""))
    low = branch.lower(); subj = subject.lower()
    evidence = []
    if branch.startswith("free/"):
        evidence.append("FREE_BRANCH_PREFIX")
    if branch.startswith("research/free-") or low.startswith("research/em-free-") or "-em-free-" in low:
        evidence.append("EXPLICIT_FREE_BRANCH_NAMING")
    if "free research" in subj or "free_research" in subj or "free researcher" in subj or "free_axiom" in subj:
        evidence.append("EXPLICIT_FREE_COMMIT_MARKER")
    return bool(evidence), evidence


def provenance(branch: str) -> dict:
    base = git("merge-base", "origin/main", f"origin/{branch}")
    paths = [x for x in git("diff", "--name-only", f"{base}..origin/{branch}", check=False).splitlines() if x]
    task_ids = set(); pubs = set(); results = set()
    for p in paths:
        parts = p.split("/")
        if len(parts) == 3 and parts[0] == "research_task_records" and p.endswith(".json"):
            task_ids.add(parts[1]); pubs.add(parts[2][:-5])
        if len(parts) == 3 and parts[0] == "research_result_records" and p.endswith(".json"):
            task_ids.add(parts[1]); results.add(parts[2][:-5])
        if len(parts) >= 2 and parts[0] == "research_execution_records":
            task_ids.add(parts[1])
    return {
        "merge_base": base,
        "changed_file_count": len(paths),
        "changed_files_sample": paths[:24],
        "exact_task_ids": sorted(task_ids),
        "publication_ids": sorted(pubs),
        "result_ids": sorted(results),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    raw = json.loads(args.raw.read_text())
    rows = raw.get("all_frontiers", [])
    live = [r for r in rows if int(r.get("unmerged_patch_commits", 0)) > 0]

    # `merge-base --independent` returns exactly those tips not reachable from any
    # other supplied tip.  It is the exact Git-ancestry notion needed here.
    tips = sorted({str(r["tip_sha"]) for r in live})
    independent = set(git("merge-base", "--independent", *tips).splitlines()) if tips else set()

    exclusions = Counter()
    task = []; free = []
    seen_tip = set()
    for row in sorted(live, key=lambda r: (r.get("tip_at") or "", r.get("branch") or ""), reverse=True):
        branch = str(row["branch"]); tip = str(row["tip_sha"])
        if tip not in independent:
            exclusions["COVERED_BY_EXACT_DESCENDANT_BRANCH"] += 1
            continue
        if tip in seen_tip:
            exclusions["DUPLICATE_BRANCH_ALIAS_SAME_TIP"] += 1
            continue
        seen_tip.add(tip)
        if row.get("control_events"):
            exclusions["EXISTING_ISSUE240_CONTROL_LINEAGE"] += 1
            continue
        refs = row.get("main_reference") or {}
        if refs.get("branch_mentioned") or refs.get("tip_mentioned"):
            exclusions["EXISTING_MAIN_STATE_REFERENCE"] += 1
            continue

        is_free, free_evidence = free_lane(row)
        prov = provenance(branch)
        common = {
            "source_branch": branch,
            "source_tip_sha": tip,
            "source_tip_at": row.get("tip_at"),
            "source_tip_subject": row.get("tip_subject"),
            "unmerged_patch_commits": row.get("unmerged_patch_commits"),
            "provenance": prov,
        }
        if is_free:
            free.append({
                "recovery_id": rid("OFR", branch, tip),
                "state_machine": "research_axiom_candidate_state_machine.json",
                "state": "DISCOVERY_IN_PROGRESS",
                "ordinary_dispatch_eligible": False,
                "promotion": "NOT_PERFORMED",
                "free_lane_evidence": free_evidence,
                "next_action": "Resume from this durable frontier and audit under the existing FREE candidate state machine; only explicit later promotion may enter ordinary task publication.",
                **common,
            })
        else:
            ids = prov["exact_task_ids"]
            task.append({
                "recovery_id": rid("OTR", branch, tip),
                "state_machine": "TASK_RESEARCH_RUNTIME",
                "state": "BLOCKED",
                "dispatch_state": "BLOCKED",
                "ordinary_dispatch_eligible": False,
                "task_id": ids[0] if len(ids) == 1 else None,
                "hard_block": {
                    "code": "ORPHAN_BRANCH_REQUIRES_CANONICAL_RECONCILIATION" if ids else "ORPHAN_EXACT_TASK_PROVENANCE_REQUIRED",
                    "missing_object": "Exact canonical task/publication reconciliation for the durable branch frontier",
                    "owner": "Driver/control maintenance",
                    "necessity": "Preserve unowned durable work without silently creating claim authority.",
                    "unblock_condition": "Bind to the exact current V2 task/publication and preserved lifecycle, supersede as duplicate/history, or deliberately publish a successor through the normal V2 contract.",
                },
                "next_action": "Reconcile provenance; this capsule itself must never be CLAIMed.",
                **common,
            })

    result = {
        "schema": SCHEMA,
        "status": "ACTIVE_RECOVERY_STATE / NOT_TASK_AVAILABILITY / NO_CLAIM_AUTHORITY",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "source_main_sha": raw.get("source_main_sha"),
        "raw_scan_schema": raw.get("schema"),
        "contracts": {
            "task_publication": "research_task_publication_contract_v2.json",
            "task_runtime": "research_control_dispatch.py -> tools/research_dispatch.py -> tools/research_runtime_reducer.py",
            "free_candidate_state_machine": "research_axiom_candidate_state_machine.json",
        },
        "invariants": [
            "RAW_SCAN != RECOVERY_STATE",
            "EXACT_DESCENDANT_COVERAGE != ORPHAN",
            "EXISTING_ISSUE240_OR_MAIN_STATE_REFERENCE != ORPHAN",
            "RECOVERY_CAPSULE != TASK_AVAILABILITY",
            "RECOVERY_CAPSULE != CLAIM",
            "TASK_ORPHAN -> BLOCKED_UNTIL_PROVENANCE_RECONCILIATION",
            "FREE_ORPHAN -> DISCOVERY_IN_PROGRESS_NOT_AUTOMATIC_TASK",
        ],
        "summary": {
            "raw_branches_scanned": raw.get("summary", {}).get("branches_scanned"),
            "raw_live_frontiers": len(live),
            "independent_tip_frontiers": len(independent),
            "recovered_task_frontiers": len(task),
            "recovered_free_frontiers": len(free),
            "total_recovery_capsules": len(task) + len(free),
            "exclusion_counts": dict(sorted(exclusions.items())),
        },
        "task_recovery": task,
        "free_recovery": free,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result["summary"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
