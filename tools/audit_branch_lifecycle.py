#!/usr/bin/env python3
"""Audit Enterprise Math branch lifecycle without mutating Git refs.

The auditor deliberately separates mechanical Git ancestry from semantic
absorption.  `ahead(main)=0` is sufficient for ABSORBED, but branches with
independent replay histories can require an explicit semantic override even when
Git still reports ahead commits.

This tool never deletes, moves, or merges a branch.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

LIFECYCLE_STATES = {
    "ACTIVE_OWNER",
    "ACTIVE_BRIDGE",
    "INTEGRATION",
    "REPLAY_REQUIRED",
    "ABSORBED",
    "PROVENANCE",
}


@dataclass(frozen=True)
class BranchAudit:
    branch: str
    ahead: int
    behind: int
    name_layer: str
    mechanical_candidate: str
    semantic_state: str
    reason: str


def run_git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def ahead_behind(main_ref: str, branch_ref: str) -> tuple[int, int]:
    """Return ``(ahead, behind)`` for ``branch_ref`` relative to ``main_ref``."""
    raw = run_git("rev-list", "--left-right", "--count", f"{main_ref}...{branch_ref}")
    left, right = (int(part) for part in raw.split())
    # left = commits only on main; right = commits only on branch
    return right, left


def name_layer(branch: str) -> str:
    if branch == "main" or branch.endswith("/main"):
        return "L0_CANONICAL"
    if branch.startswith("core/"):
        return "L1_CORE_OWNER"
    if branch.startswith("program/") or branch.startswith("engineering/"):
        return "L2_PROGRAM_OWNER"
    if branch.startswith("bridge/"):
        return "L3_BRIDGE"
    if branch.startswith("integration/"):
        return "L4_INTEGRATION"
    if branch.startswith("checkpoint/"):
        return "L5_PROVENANCE"
    if branch.startswith("agent/"):
        return "SHORT_AGENT"
    if branch.startswith("research/"):
        return "HISTORICAL_RESEARCH_OR_OWNER"
    if branch.startswith("chore/") or branch.startswith("ci/"):
        return "MAINTENANCE"
    if branch.startswith("formal/"):
        return "FORMALIZATION"
    return "UNCLASSIFIED_NAME"


def mechanical_candidate(branch: str, ahead: int, behind: int) -> str:
    """Return a Git-only candidate state; never claims semantic equivalence."""
    layer = name_layer(branch)
    if layer == "L0_CANONICAL":
        return "CANONICAL"
    if ahead == 0:
        return "ABSORBED"
    if layer == "L5_PROVENANCE":
        return "PROVENANCE"
    if layer == "L4_INTEGRATION":
        return "INTEGRATION"
    if behind >= 50 or ahead > 100:
        return "REPLAY_REQUIRED"
    if layer == "L1_CORE_OWNER" or layer == "L2_PROGRAM_OWNER":
        return "ACTIVE_OWNER"
    if layer == "L3_BRIDGE":
        return "ACTIVE_BRIDGE"
    return "NEEDS_REVIEW"


def load_overrides(path: Path | None) -> dict[str, dict[str, str]]:
    if path is None or not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != "ENTERPRISE_MATH_BRANCH_LIFECYCLE_OVERRIDES_V1":
        raise ValueError("unexpected lifecycle override schema")
    entries = data.get("branches", {})
    for branch, entry in entries.items():
        state = entry.get("state")
        if state not in LIFECYCLE_STATES:
            raise ValueError(f"invalid lifecycle state for {branch}: {state!r}")
        if not entry.get("reason"):
            raise ValueError(f"override for {branch} must include a reason")
    return entries


def classify_branch(
    branch: str,
    ahead: int,
    behind: int,
    overrides: dict[str, dict[str, str]],
) -> BranchAudit:
    mechanical = mechanical_candidate(branch, ahead, behind)
    override = overrides.get(branch)
    if override is not None:
        state = override["state"]
        reason = override["reason"]
    elif mechanical in LIFECYCLE_STATES:
        state = mechanical
        reason = "mechanical Git/lifecycle rule; semantic audit may still add provenance detail"
    else:
        state = "NEEDS_REVIEW"
        reason = "no semantic override and no unique lifecycle state follows mechanically"
    return BranchAudit(
        branch=branch,
        ahead=ahead,
        behind=behind,
        name_layer=name_layer(branch),
        mechanical_candidate=mechanical,
        semantic_state=state,
        reason=reason,
    )


def iter_refs(ref_prefix: str) -> Iterable[tuple[str, str]]:
    """Yield ``(display_name, full_ref)`` pairs under one Git ref prefix."""
    raw = run_git("for-each-ref", "--format=%(refname)", ref_prefix)
    for full_ref in filter(None, raw.splitlines()):
        display = full_ref
        if ref_prefix == "refs/remotes/origin/" and full_ref.startswith(ref_prefix):
            display = full_ref[len(ref_prefix) :]
        elif full_ref.startswith("refs/heads/"):
            display = full_ref[len("refs/heads/") :]
        yield display, full_ref


def render_markdown(audits: list[BranchAudit], main_ref: str) -> str:
    lines = [
        "# Branch Lifecycle Audit",
        "",
        f"Main ref: `{main_ref}`",
        "",
        "| Branch | Ahead | Behind | Name layer | Mechanical | Semantic |",
        "|---|---:|---:|---|---|---|",
    ]
    for item in audits:
        lines.append(
            f"| `{item.branch}` | {item.ahead} | {item.behind} | "
            f"`{item.name_layer}` | `{item.mechanical_candidate}` | "
            f"`{item.semantic_state}` |"
        )
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- This report is read-only and never deletes or moves refs.",
            "- `ahead=0` is a mechanical sufficient condition for absorption.",
            "- `ahead>0` is not proof of unique mathematics; semantic overrides may mark independently replayed branches as absorbed.",
            "- `NEEDS_REVIEW` means theorem/provenance audit is still required.",
        ]
    )
    return "\n".join(lines) + "\n"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--main", default="refs/remotes/origin/main")
    parser.add_argument("--ref-prefix", default="refs/remotes/origin/")
    parser.add_argument(
        "--overrides",
        type=Path,
        default=Path("branch_lifecycle_overrides.json"),
    )
    parser.add_argument("--json-out", type=Path)
    parser.add_argument("--markdown-out", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    overrides = load_overrides(args.overrides)
    audits: list[BranchAudit] = []
    for display, full_ref in iter_refs(args.ref_prefix):
        if display == "HEAD":
            continue
        ahead, behind = ahead_behind(args.main, full_ref)
        audits.append(classify_branch(display, ahead, behind, overrides))
    audits.sort(key=lambda item: (item.semantic_state, item.branch))

    payload = {
        "schema": "ENTERPRISE_MATH_BRANCH_LIFECYCLE_AUDIT_V1",
        "main_ref": args.main,
        "branches": [asdict(item) for item in audits],
    }
    json_text = json.dumps(payload, ensure_ascii=False, indent=2) + "\n"
    md_text = render_markdown(audits, args.main)

    if args.json_out:
        args.json_out.write_text(json_text, encoding="utf-8")
    else:
        print(json_text, end="")
    if args.markdown_out:
        args.markdown_out.write_text(md_text, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
