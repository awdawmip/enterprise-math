#!/usr/bin/env python3
"""Audit Enterprise Math branch lifecycle, scope, and retirement evidence.

The auditor separates three independent questions:

1. ancestry/lifecycle: ahead/behind, semantic absorption, replay state;
2. scope purity: whether branch-side changes stay inside an explicitly
   declared owner/integration asset set;
3. retirement evidence: whether an ABSORBED/PROVENANCE classification that
   still has branch-only commits is mechanically justified, grandfathered,
   or backed by one resolved result-conservation certificate.

A branch may legitimately be behind main while remaining scope-pure. Conversely,
a branch may be close to main while carrying unrelated theorem homes and should
then be reported as SCOPE_DRIFT.

This tool never deletes, moves, merges, rebases, or force-updates refs.
"""

from __future__ import annotations

import argparse
import json
import subprocess
from dataclasses import asdict, dataclass, replace
from pathlib import Path
from typing import Iterable

try:
    from tools.check_references import validate_result_conservation_manifest
except ModuleNotFoundError:  # direct `python tools/audit_branch_lifecycle.py`
    from check_references import validate_result_conservation_manifest

LIFECYCLE_STATES = {
    "ACTIVE_OWNER",
    "ACTIVE_BRIDGE",
    "INTEGRATION",
    "REPLAY_REQUIRED",
    "ABSORBED",
    "PROVENANCE",
}

SCOPE_STATES = {"PURE", "SCOPE_DRIFT", "NOT_CONFIGURED", "NOT_APPLICABLE"}
RETIREMENT_STATES = {"ABSORBED", "PROVENANCE"}
RETIREMENT_BASES = {
    "MECHANICAL_ANCESTRY",
    "LEGACY_PRE_RESULT_CONSERVATION",
    "RESULT_CONSERVATION",
}
RETIREMENT_EVIDENCE_FAILURES = {
    "INVALID_RETIREMENT_EVIDENCE",
    "UNDECLARED_SEMANTIC_RETIREMENT",
}
OVERRIDE_SCHEMA = "ENTERPRISE_MATH_BRANCH_GOVERNANCE_OVERRIDES_V3"
LEGACY_RETIREMENT_CUTOFF = "2026-08-10"
LEGACY_RETIREMENT_ALLOWLIST = frozenset({
    "agent/p018-critical-grid",
    "engineering/e001-material-impulse-world",
    "engineering/e001-material-multiaction-protocol",
    "engineering/e001-material-pair-impulse",
    "program/p021-causal-focusing-v2",
    "research/core/admissible-support-relations",
    "research/e002-task-observable-v2",
    "research/p018-all-power-quotient-basin-final",
    "research/p023-composition-safe-collapse",
    "research/p023-safe-selector-semigroup",
})


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
    branch_head: str = ""
    retirement_evidence_state: str = "NOT_CHECKED"
    retirement_evidence_reason: str = ""
    retirement_certificate: str | None = None


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


def _load_certificate(root: Path, relative_path: str, label: str) -> dict:
    path = Path(relative_path)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"{label}: result_conservation_certificate must be a safe repo-relative path")
    full_path = root / path
    if not full_path.exists():
        raise ValueError(f"{label}: result-conservation certificate does not exist: {relative_path}")
    try:
        manifest = json.loads(full_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{label}: invalid result-conservation JSON: {exc}") from exc
    errors = validate_result_conservation_manifest(manifest, relative_path)
    if errors:
        raise ValueError(f"{label}: invalid result-conservation certificate: {'; '.join(errors)}")
    return manifest


def load_overrides(path: Path | None) -> dict[str, dict[str, object]]:
    if path is None or not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != OVERRIDE_SCHEMA:
        raise ValueError(f"unexpected branch governance override schema; expected {OVERRIDE_SCHEMA}")

    contract = data.get("retirement_contract")
    if not isinstance(contract, dict):
        raise ValueError("retirement_contract must be an object")
    declared_bases = contract.get("basis_values")
    if not isinstance(declared_bases, list) or set(declared_bases) != RETIREMENT_BASES:
        raise ValueError("retirement_contract.basis_values must match the canonical retirement basis vocabulary")
    if contract.get("legacy_cutoff") != LEGACY_RETIREMENT_CUTOFF:
        raise ValueError(
            f"retirement_contract.legacy_cutoff must remain {LEGACY_RETIREMENT_CUTOFF}"
        )
    legacy_value = contract.get("legacy_branches")
    if not isinstance(legacy_value, list) or any(
        not isinstance(item, str) or not item for item in legacy_value
    ):
        raise ValueError("retirement_contract.legacy_branches must be a list of non-empty strings")
    if len(legacy_value) != len(set(legacy_value)):
        raise ValueError("retirement_contract.legacy_branches contains duplicates")
    legacy_branches = set(legacy_value)
    if legacy_branches != LEGACY_RETIREMENT_ALLOWLIST:
        raise ValueError(
            "retirement_contract.legacy_branches is frozen; "
            f"expected {sorted(LEGACY_RETIREMENT_ALLOWLIST)}"
        )

    entries = data.get("branches", {})
    if not isinstance(entries, dict):
        raise ValueError("branches must be an object")

    actual_legacy: set[str] = set()
    root = path.parent
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

        if state not in RETIREMENT_STATES:
            if "retirement_basis" in entry:
                raise ValueError(f"non-retired override {branch} must not declare retirement_basis")
            continue

        basis = entry.get("retirement_basis")
        if basis not in RETIREMENT_BASES:
            raise ValueError(
                f"retired override {branch} must declare retirement_basis in {sorted(RETIREMENT_BASES)}"
            )

        if basis == "LEGACY_PRE_RESULT_CONSERVATION":
            actual_legacy.add(branch)
            if branch not in legacy_branches:
                raise ValueError(f"legacy retirement {branch} is not in the frozen legacy_branches allowlist")
        elif basis == "RESULT_CONSERVATION":
            certificate = entry.get("result_conservation_certificate")
            owner_id = entry.get("source_owner_id")
            if not isinstance(certificate, str) or not certificate:
                raise ValueError(f"{branch}: RESULT_CONSERVATION requires result_conservation_certificate")
            if not isinstance(owner_id, str) or not owner_id:
                raise ValueError(f"{branch}: RESULT_CONSERVATION requires source_owner_id")
            manifest = _load_certificate(root, certificate, branch)
            actual_owner_id = manifest.get("source_owner", {}).get("id")
            if actual_owner_id != owner_id:
                raise ValueError(
                    f"{branch}: certificate source_owner.id {actual_owner_id!r} != declared {owner_id!r}"
                )
        else:
            for forbidden in ("result_conservation_certificate", "source_owner_id"):
                if forbidden in entry:
                    raise ValueError(
                        f"{branch}: {basis} retirement must not declare {forbidden}"
                    )

    if actual_legacy != legacy_branches:
        missing = sorted(legacy_branches - actual_legacy)
        extra = sorted(actual_legacy - legacy_branches)
        raise ValueError(
            f"legacy retirement allowlist drift: missing_entries={missing}; unlisted_entries={extra}"
        )
    return entries


def retirement_evidence(
    branch: str,
    *,
    ahead: int,
    branch_head: str,
    semantic_state: str,
    override: dict[str, object] | None,
    root: Path,
) -> tuple[str, str, str | None]:
    """Return retirement evidence state, reason, and certificate path.

    Mechanical absorption is free only when ``ahead == 0``. Ahead-positive
    ABSORBED/PROVENANCE source owners need either a frozen pre-contract legacy
    declaration or a resolved result-conservation certificate whose frozen
    source head is the exact branch tip being retired.
    """
    if semantic_state not in RETIREMENT_STATES:
        return "NOT_APPLICABLE", "branch is not in a retirement lifecycle state", None

    if override is None:
        if ahead == 0:
            return "MECHANICAL_ANCESTRY", "ahead=0 mechanically proves branch commits are absorbed", None
        if name_layer(branch) == "L5_PROVENANCE":
            return "CHECKPOINT_PROVENANCE", "immutable checkpoint naming is provenance, not source-owner retirement", None
        return (
            "UNDECLARED_SEMANTIC_RETIREMENT",
            "ahead-positive retired branch has no explicit retirement declaration",
            None,
        )

    basis = override.get("retirement_basis")
    if basis == "MECHANICAL_ANCESTRY":
        if ahead != 0:
            return (
                "INVALID_RETIREMENT_EVIDENCE",
                f"declared MECHANICAL_ANCESTRY but branch is ahead by {ahead}",
                None,
            )
        return "MECHANICAL_ANCESTRY", "ahead=0 matches the declared mechanical retirement basis", None

    if basis == "LEGACY_PRE_RESULT_CONSERVATION":
        return (
            "LEGACY_GRANDFATHERED",
            "retirement predates the result-conservation contract and is in the frozen legacy allowlist",
            None,
        )

    if basis != "RESULT_CONSERVATION":
        return "INVALID_RETIREMENT_EVIDENCE", f"unknown retirement basis {basis!r}", None

    certificate = override.get("result_conservation_certificate")
    owner_id = override.get("source_owner_id")
    if not isinstance(certificate, str) or not certificate:
        return "INVALID_RETIREMENT_EVIDENCE", "missing result_conservation_certificate", None
    if not isinstance(owner_id, str) or not owner_id:
        return "INVALID_RETIREMENT_EVIDENCE", "missing source_owner_id", certificate

    try:
        manifest = _load_certificate(root, certificate, branch)
    except (OSError, ValueError) as exc:
        return "INVALID_RETIREMENT_EVIDENCE", str(exc), certificate

    source_owner = manifest.get("source_owner", {})
    if source_owner.get("id") != owner_id:
        return (
            "INVALID_RETIREMENT_EVIDENCE",
            f"certificate owner {source_owner.get('id')!r} != declared {owner_id!r}",
            certificate,
        )
    if source_owner.get("source_head") != branch_head:
        return (
            "INVALID_RETIREMENT_EVIDENCE",
            f"certificate source_head {source_owner.get('source_head')!r} != branch head {branch_head!r}",
            certificate,
        )
    return (
        "RESULT_CONSERVATION_CERTIFIED",
        "resolved result-conservation certificate matches the exact retired source head",
        certificate,
    )


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
        "| Branch | Ahead | Behind | Semantic | Scope | Retirement evidence | Unexpected |",
        "|---|---:|---:|---|---|---|---:|",
    ]
    for item in audits:
        lines.append(
            f"| `{item.branch}` | {item.ahead} | {item.behind} | "
            f"`{item.semantic_state}` | `{item.scope_state}` | "
            f"`{item.retirement_evidence_state}` | {len(item.unexpected_paths)} |"
        )
    lines.extend(
        [
            "",
            "## Notes",
            "",
            "- Read-only: this tool never mutates refs.",
            "- `ahead=0` is sufficient for mechanical absorption, not necessary for semantic absorption.",
            "- Ahead-positive ABSORBED/PROVENANCE source owners require explicit retirement evidence.",
            "- `RESULT_CONSERVATION` retirement must match one resolved certificate to the exact branch head.",
            "- `LEGACY_PRE_RESULT_CONSERVATION` is restricted to the frozen V3 allowlist and is not a reusable escape hatch.",
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
    certificate_root = args.overrides.parent if args.overrides is not None else Path(".")
    audits: list[BranchAudit] = []
    for display, full_ref in iter_refs(args.ref_prefix):
        if display == "HEAD":
            continue
        ahead, behind = ahead_behind(args.main, full_ref)
        changed = branch_side_changed_files(args.main, full_ref)
        audit = classify_branch(display, ahead, behind, changed, overrides)
        branch_head = run_git("rev-parse", full_ref)
        evidence_state, evidence_reason, certificate = retirement_evidence(
            display,
            ahead=ahead,
            branch_head=branch_head,
            semantic_state=audit.semantic_state,
            override=overrides.get(display),
            root=certificate_root,
        )
        audits.append(
            replace(
                audit,
                branch_head=branch_head,
                retirement_evidence_state=evidence_state,
                retirement_evidence_reason=evidence_reason,
                retirement_certificate=certificate,
            )
        )
    audits.sort(
        key=lambda item: (
            item.retirement_evidence_state in RETIREMENT_EVIDENCE_FAILURES,
            item.scope_state == "SCOPE_DRIFT",
            item.semantic_state,
            item.branch,
        ),
        reverse=True,
    )

    payload = {
        "schema": "ENTERPRISE_MATH_BRANCH_GOVERNANCE_AUDIT_V3",
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

    failures = [
        item for item in audits
        if item.retirement_evidence_state in RETIREMENT_EVIDENCE_FAILURES
    ]
    if failures:
        for item in failures:
            print(
                f"ERROR: {item.branch}: {item.retirement_evidence_state}: "
                f"{item.retirement_evidence_reason}"
            )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
