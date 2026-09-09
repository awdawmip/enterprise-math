#!/usr/bin/env python3
"""Build a bounded, source-pinned startup packet for one canonical dispatch request.

The full dispatch receipt remains diagnostic authority.  This projection carries only
what a fresh researcher needs to start safely: exact route identity, exact immutable
task publication binding, a compact projection of the taskbook's authoritative
sections when it fits, and at most one exact first dependency path.

It deliberately never enumerates task/result directories and never parses natural
language to infer task availability or claim authority.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
POLICY_PATH = ROOT / "research_context_budget.json"
SCHEMA = "ENTERPRISE_MATH_RESEARCHER_STARTUP_PACKET_V1"
TASK_FRONTMATTER = re.compile(
    r"<!--\s*ENTERPRISE_MATH_TASK_V1\s*(\{.*?\})\s*-->", re.DOTALL
)
TASK_SECTIONS = (
    "Mother question",
    "Frozen inputs and scope",
    "Hard target and required outputs",
    "Research value to preserve",
    "Success, kill, and return criteria",
)
PATH_TOKEN = re.compile(
    r"(?P<path>(?:research_[A-Za-z0-9_.-]+|research|docs|definitions|scripts|src|EnterpriseMath|artifacts|control_plane)/[^\s,;]+\.(?:md|json|py|lean|txt|csv))"
)


class StartupPacketError(RuntimeError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise StartupPacketError(message)


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    _require(isinstance(value, dict), f"expected JSON object: {path}")
    return value


def _budget(root: Path) -> dict[str, Any]:
    policy = _load_json(root / "research_context_budget.json")
    value = policy.get("researcher_cold_start_envelope")
    _require(isinstance(value, dict), "missing researcher_cold_start_envelope policy")
    return value


def _git_blob_sha1(raw: bytes) -> str:
    """Return the Git blob object id format used by taskbook_blob_sha1."""
    payload = f"blob {len(raw)}\0".encode("ascii") + raw
    return "sha1:" + hashlib.sha1(payload).hexdigest()


def _task_metadata(text: str) -> dict[str, Any]:
    match = TASK_FRONTMATTER.search(text)
    if not match:
        return {}
    try:
        value = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        raise StartupPacketError(f"invalid ENTERPRISE_MATH_TASK_V1 metadata: {exc}") from exc
    _require(isinstance(value, dict), "task metadata must be an object")
    return value


def _extract_sections(text: str) -> dict[str, str]:
    lines = text.splitlines()
    wanted = set(TASK_SECTIONS)
    out: dict[str, list[str]] = {name: [] for name in TASK_SECTIONS}
    current: str | None = None
    for line in lines:
        if line.startswith("## "):
            name = line[3:].strip()
            current = name if name in wanted else None
            continue
        if current is not None:
            out[current].append(line)
    return {name: "\n".join(out[name]).strip() for name in TASK_SECTIONS if "\n".join(out[name]).strip()}


def _candidate_paths(value: Any) -> Iterable[str]:
    if isinstance(value, str):
        text = value.strip().strip("`\"'")
        if text:
            yield text
        for match in PATH_TOKEN.finditer(value):
            yield match.group("path").rstrip(".)]}")
        for part in value.split(" / "):
            part = part.strip().strip("`\"'").rstrip(".)]}")
            if "/" in part and "." in Path(part).name:
                yield part
    elif isinstance(value, list):
        for item in value:
            yield from _candidate_paths(item)


def _existing_repo_path(root: Path, values: Iterable[Any]) -> str | None:
    seen: set[str] = set()
    for value in values:
        for raw in _candidate_paths(value):
            candidate = raw.replace("\\", "/")
            if candidate in seen or candidate.startswith("/") or ".." in Path(candidate).parts:
                continue
            seen.add(candidate)
            if (root / candidate).is_file():
                return candidate
    return None


def _first_dependency_ref(
    root: Path, publication: dict[str, Any], metadata: dict[str, Any]
) -> str | None:
    explicit = publication.get("startup_read_plan")
    if isinstance(explicit, dict):
        path = _existing_repo_path(root, [explicit.get("first_dependency_ref")])
        if path:
            return path

    # A durable frontier is normally the highest-value first read for a resumed
    # HANDOFF task and is already exact/pinned by the task publication.
    path = _existing_repo_path(
        root,
        [publication.get("last_progress_ref"), metadata.get("last_progress_ref")],
    )
    if path:
        return path

    dependencies = metadata.get("dependencies")
    if isinstance(dependencies, list):
        unsatisfied: list[Any] = []
        for item in dependencies:
            if isinstance(item, dict) and item.get("satisfied") is not True:
                unsatisfied.extend([item.get("path"), item.get("target")])
        path = _existing_repo_path(root, unsatisfied)
        if path:
            return path

    return _existing_repo_path(root, [metadata.get("source_refs"), publication.get("source_refs")])


def _publication_for_target(root: Path, target: dict[str, Any]) -> tuple[dict[str, Any], Path]:
    task_id = target.get("task_id")
    publication_id = target.get("publication_id")
    _require(isinstance(task_id, str) and task_id, "dispatch target missing task_id")
    _require(
        isinstance(publication_id, str) and publication_id,
        "dispatch target missing publication_id",
    )
    path = root / "research_task_records" / task_id / f"{publication_id}.json"
    _require(path.is_file(), f"missing exact task publication: {path.relative_to(root)}")
    publication = _load_json(path)
    _require(publication.get("task_id") == task_id, "publication task_id mismatch")
    _require(
        publication.get("publication_id") == publication_id,
        "publication_id mismatch",
    )
    return publication, path


def _task_projection(
    root: Path, publication: dict[str, Any]
) -> tuple[dict[str, Any], dict[str, Any]]:
    taskbook_path = publication.get("taskbook_path")
    _require(isinstance(taskbook_path, str) and taskbook_path, "publication missing taskbook_path")
    path = root / taskbook_path
    _require(path.is_file(), f"missing exact taskbook: {taskbook_path}")
    raw = path.read_bytes()
    actual_sha1 = _git_blob_sha1(raw)
    expected_sha1 = publication.get("taskbook_blob_sha1")
    _require(expected_sha1 == actual_sha1, f"taskbook blob mismatch: {taskbook_path}")
    text = raw.decode("utf-8")
    metadata = _task_metadata(text)
    sections = _extract_sections(text)
    return (
        {
            "taskbook_path": taskbook_path,
            "taskbook_blob_sha1": actual_sha1,
            "sections": sections,
            "complete": all(name in sections for name in TASK_SECTIONS),
        },
        metadata,
    )


def _serialized_packet(value: dict[str, Any]) -> bytes:
    """Use the same readable UTF-8 LF bytes for budgeting and CLI output."""
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode(
        "utf-8"
    )


def _serialized_size(value: dict[str, Any]) -> int:
    return len(_serialized_packet(value))


def _annotate_packet_size(packet: dict[str, Any]) -> int:
    packet["packet_bytes"] = 0
    while True:
        size = _serialized_size(packet)
        if packet["packet_bytes"] == size:
            return size
        packet["packet_bytes"] = size


def build_packet(receipt: dict[str, Any], root: Path = ROOT) -> dict[str, Any]:
    budget = _budget(root)
    hard_max = budget.get("compact_packet_hard_max_bytes")
    _require(isinstance(hard_max, int) and hard_max > 0, "invalid compact packet budget")

    route = receipt.get("route")
    _require(isinstance(route, dict), "receipt missing route")
    request_id = receipt.get("request_id")
    source_sha = receipt.get("source_sha")
    _require(isinstance(request_id, str) and request_id, "receipt missing request_id")
    _require(isinstance(source_sha, str) and source_sha, "receipt missing source_sha")

    packet: dict[str, Any] = {
        "schema": SCHEMA,
        "request_id": request_id,
        "generated_at": receipt.get("generated_at"),
        "source_sha": source_sha,
        "control_epoch": (route.get("startup_transport") or {}).get("control_epoch"),
        "kind": receipt.get("kind"),
        "action": route.get("action"),
        "new_claim_required": route.get("new_claim_required"),
        "owner_claim_preserved": route.get("owner_claim_preserved"),
        "reason": route.get("reason"),
        "task": None,
        "read_plan": {
            "remote_source_reads_before_substantive_math_max": budget.get(
                "normal_remote_source_reads_before_math_max"
            ),
            "first_dependency_ref": None,
            "if_first_dependency_unknown": "TASK_UNDERSTANDING_THEN_BOUNDED_TARGETED_SEARCH_ONLY",
            "forbidden": [
                "REMOTE_FETCH_AGENTS_MD_FOR_ORDINARY_START",
                "FULL_DISPATCH_RECEIPT_ON_ORDINARY_START",
                "CURRENT_CONTROL_AUTHORITY_ON_ORDINARY_START",
                "ISSUE_240_FULL_COMMENT_STREAM_IN_CONVERSATION",
                "HIGH_FANOUT_DIRECTORY_OR_RECURSIVE_TREE_DISCOVERY",
            ],
        },
        "diagnostics": {
            "receipt_path": receipt.get("immutable_receipt_path"),
            "load_policy": "TRIGGERED_ONLY",
        },
    }

    target = route.get("target")
    if "assigned_driver_selection" in route:
        packet["assigned_driver_selection"] = route["assigned_driver_selection"]
        packet["required_guard"] = route.get("required_guard")
    if "assigned_research_selection" in route:
        packet["assigned_research_selection"] = route["assigned_research_selection"]
        packet["selection_scope"] = route.get("selection_scope")
        packet["selection_status"] = route.get("selection_status")
        packet["required_guard"] = route.get("required_guard")
        packet["next_control_steps"] = route.get("next_control_steps", [])
    if isinstance(target, dict) and target.get("task_id"):
        publication, publication_path = _publication_for_target(root, target)
        projection, metadata = _task_projection(root, publication)
        first_dependency = _first_dependency_ref(root, publication, metadata)
        packet["read_plan"]["first_dependency_ref"] = first_dependency
        packet["task"] = {
            "task_id": target.get("task_id"),
            "publication_id": target.get("publication_id"),
            "publication_record_path": publication_path.relative_to(root).as_posix(),
            "taskbook_path": projection["taskbook_path"],
            "taskbook_blob_sha1": projection["taskbook_blob_sha1"],
            "title": target.get("title"),
            "identity_lane": target.get("identity_lane"),
            "owner": target.get("owner"),
            "state": target.get("state"),
            "dispatch_state": target.get("dispatch_state"),
            "claim_id": target.get("claim_id"),
            "researcher_id": target.get("researcher_id"),
            "lease_until": target.get("lease_until"),
            "frontier": target.get("frontier"),
            "next_action": target.get("next_action"),
            "projection_mode": "INLINE_EXACT_TASKBOOK_SECTIONS"
            if projection["complete"]
            else "EXACT_TASKBOOK_REQUIRED",
            "projection": projection["sections"] if projection["complete"] else None,
            "required_task_sections": list(TASK_SECTIONS),
        }

    size = _annotate_packet_size(packet)
    if (
        size > hard_max
        and packet["task"] is not None
        and packet["task"]["projection"] is not None
    ):
        packet["task"]["projection"] = None
        packet["task"]["projection_mode"] = "EXACT_TASKBOOK_REQUIRED_PACKET_BUDGET"
        size = _annotate_packet_size(packet)
    _require(
        size <= hard_max,
        f"startup packet exceeds {hard_max} bytes: {size}",
    )
    return packet


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--receipt", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()

    receipt = _load_json(args.receipt)
    packet = build_packet(receipt, args.root.resolve())
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(_serialized_packet(packet))
    print(
        json.dumps(
            {
                "startup_packet": "PASS",
                "request_id": packet["request_id"],
                "action": packet["action"],
                "packet_bytes": packet["packet_bytes"],
                "output": str(args.output),
            },
            ensure_ascii=False,
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
