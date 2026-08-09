#!/usr/bin/env python3
"""Audit Enterprise Math branch lifecycle and theorem-home scope without mutation.

The auditor separates two independent questions:

1. ancestry/lifecycle: ahead/behind, semantic absorption, replay state;
2. scope purity: whether the branch-side changes stay inside an explicitly
   declared owner/integration asset set.

A branch may legitimately be behind main while remaining scope-pure. Conversely,
a branch may be close to main while carrying unrelated theorem homes and should
then be reported as SCOPE_DRIFT.

This tool never deletes, moves, merges, rebases, or force-updates refs.
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

SCOPE_STATES = {"PURE", "SCOPE_DRIFT", "NOT_CONFIGURED", "NOT_APPLICABLE"}


@dataclass(frozen=True)
class BranchAudit:
    branch: str
    ahead: int
    behind: int
    name_layer: str
    mechanical_candidate: str
    semantic_state: str
    reason: str
    scope_state: str
    branch_side_changes: tuple[str, ...]
    unexpected_paths: tuple[str, ...]


def run_git(*args: str) -> str:
    return subprocess.check_output(["git", *args], text=True).strip()


def ahead_behind(main_ref: str, branch_ref: str) -> tuple[int, int]:
    raw = run_git("rev-list", "--left-right", "--count", f"{main_ref}...{branch_ref}")
    left, right = (int(part) for part in raw.split())
    return right, left


def branch_side_changed_files(main_ref: str, branch_ref: str) -> tuple[str, ...]:
    """Files changed on the branch side since its merge-base with main.

    This intentionally ignores changes that happened only on main after the
    branch diverged, so an isolated owner is not punished merely for being
    behind canonical main.
    """
    base = run_git("merge-base", main_ref, branch_ref)
    raw = run_git("diff", "--name-only", f"{base}..{branch_ref}")
    return tuple(sorted(filter(None, raw.splitlines())))


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
    if layer in {"L1_CORE_OWNER", "L2_PROGRAM_OWNER"}:
        return "ACTIVE_OWNER"
    if layer == "L3_BRIDGE":
        return "ACTIVE_BRIDGE"
    return "NEEDS_REVIEW"


def _require_string_list(entry: dict[str, object], key: str, branch: str) -> tuple[str, ...]:
    value = entry.get(key, [])
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise ValueError(f"{key} for {branch} must be a list of strings")
    return tuple(value)


def load_overrides(path: Path | None) -> dict[str, dict[str, object]]:
    if path is None or not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != "ENTERPRISE_MATH_BRANCH_GOVERNANCE_OVERRIDES_V2":
        raise ValueError("unexpected branch governance override schema")
    entries = data.get("branches", {})
    if not isinstance(entries, dict):
        raise ValueError("branches must be an object")
    for branch, entry in entries.items():
        if not isinstance(entry, dict):
            raise ValueError(f"override for {branch} must be an object")
        state = entry.get("state")
        if state not in LIFECYCLE_STATES:
            raise ValueError(f"invalid lifecycle state for {branch}: {state!r}")
        if not entry.get("reason"):
            raise ValueError(f"override for {branch} must include a reason")
        _require_string_list(entry, "allowed_paths", branch)
        _require_string_list(entry, "allowed_prefixes", branch)
    return entries


def path_allowed(path: str, allowed_paths: tuple[str, ...], allowed_prefixes: tuple[str, ...]) -> bool:
    if path in allowed_paths:
        return True
    return any(path.startswith(prefix) for prefix in allowed_prefixes)


def scope_status(
    branch: str,
    semantic_state: str,
    changed_files: tuple[str, ...],
    override: dict[str, object] | None,
) -> tuple[str, tuple[str, ...]]:
    layer = name_layer(branch)
    if layer == "L0_CANONICAL" or semantic_state in {"ABSORBED", "PROVENANCE"}:
        return "NOT_APPLICABLE", ()
    if override is None:
        return "NOT_CONFIGURED", ()
    allowed_paths = _require_string_list(override, "allowed_paths", branch)
    allowed_prefixes = _require_string_list(override, "allowed_prefixes", branch)
    if not allowed_paths and not allowed_prefixes:
        return "NOT_CONFIGURED", ()
    unexpected = tuple(
        path for path in changed_files if not path_allowed(path, allowed_paths, allowed_prefixes)
    )
    return ("SCOPE_DRIFT", unexpected) if unexpected else ("PURE", ())


def classify_branch(
    branch: str,
    ahead: int,
    behind: int,
    changed_files: tuple[str, ...],
    overrides: dict[str, dict[str, object]],
) -> BranchAudit:
    mechanical = mechanical_candidate(branch, ahead, behind)
    override = overrides.get(branch)
    if override is not None:
        state = str(override["state"])
        reason = str(override["reason"])
    elif mechanical in LIFECYCLE_STATES:
        state = mechanical
        reason = "mechanical Git/lifecycle rule; semantic audit may still refine provenance"
    else:
        state = "NEEDS_REVIEW"
        reason = "no semantic override and no unique lifecycle state follows mechanically"
    scope, unexpected = scope_status(branch, state, changed_files, override)
    if scope not in SCOPE_STATES:
        raise AssertionError("unknown scope state")
    return BranchAudit(
        branch=branch,
        ahead=ahead,
        behind=behind,
        name_layer=name_layer(branch),
        mechanical_candidate=mechanical,
        semantic_state=state,
        reason=reason,
        scope_state=scope,
        branch_side_changes=changed_files,
        unexpected_paths=unexpected,
    )


def iter_refs(ref_prefix: str) -> Iterable[tuple[str, str]]:
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
        "# Branch Governance Audit",
        "",
        f"Main ref: `{main_ref}`",
        "",
        "| Branch | Ahead | Behind | Semantic | Scope | Unexpected |",
        "|---|---:|---:|---|---|---:|",
    ]
    for item in audits:
        lines.append(
            f"| `{item.branch}` | {item.ahead} | {item.behind} | "
            f"`{item.semantic_state}` | `{item.scope_state}` | {len(item.unexpected_paths)} |"
        )
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- Read-only: this tool never mutates refs.",
            "- `ahead=0` is sufficient for mechanical absorption, not necessary for semantic absorption.",
            "- Owner branches may be behind main; scope is computed only from merge-base to the branch side.",
            "- `SCOPE_DRIFT` means branch-side changes escaped the declared owner/integration asset set.",
            "- `NOT_CONFIGURED` means ancestry was audited but owner-path metadata still needs to be declared.",
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
        default=Path("branch_governance_overrides.json"),
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
        changed = branch_side_changed_files(args.main, full_ref)
        audits.append(classify_branch(display, ahead, behind, changed, overrides))
    audits.sort(key=lambda item: (item.scope_state == "SCOPE_DRIFT", item.semantic_state, item.branch), reverse=True)

    payload = {
        "schema": "ENTERPRISE_MATH_BRANCH_GOVERNANCE_AUDIT_V2",
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
