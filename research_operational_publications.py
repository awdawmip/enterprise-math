#!/usr/bin/env python3
"""Select one operational publication without discarding parallel evidence."""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
PUBLICATION_ROOT = ROOT / "research_task_records"
RESOLUTION_PATH = ROOT / "research_task_publication_resolutions.json"
SYNTHESIS_ROOT = ROOT / "research_parallel_syntheses"
RECORD_SCHEMA = "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2"
RESOLUTION_SCHEMA = "ENTERPRISE_MATH_TASK_PUBLICATION_RESOLUTION_REGISTRY_V1"
SYNTHESIS_SCHEMA = "ENTERPRISE_MATH_PARALLEL_SYNTHESIS_V1"
TERMINAL_RECORD_STATES = {"PARKED", "SUPERSEDED", "CLOSED"}


class OperationalPublicationError(ValueError):
    pass


def _load(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise OperationalPublicationError(f"{path}: JSON root must be object")
    return value


def iter_publications(root: Path = ROOT) -> list[dict[str, Any]]:
    directory = root / "research_task_records"
    if not directory.exists():
        return []
    out: list[dict[str, Any]] = []
    for path in sorted(directory.glob("*/*.json")):
        item = _load(path)
        item["_record_path"] = path.relative_to(root).as_posix()
        out.append(item)
    return out


def publication_heads(root: Path = ROOT) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for item in iter_publications(root):
        task_id = item.get("task_id")
        if isinstance(task_id, str) and task_id:
            grouped[task_id].append(item)
    out: dict[str, list[dict[str, Any]]] = {}
    for task_id, values in grouped.items():
        superseded = {
            item.get("supersedes_publication_id")
            for item in values
            if isinstance(item.get("supersedes_publication_id"), str)
            and item.get("supersedes_publication_id")
        }
        heads = [
            item
            for item in values
            if item.get("publication_id") not in superseded
            and item.get("record_state", "ACTIVE") not in TERMINAL_RECORD_STATES
        ]
        if heads:
            out[task_id] = heads
    return out


def resolution_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    path = root / "research_task_publication_resolutions.json"
    if not path.exists():
        return {}
    payload = _load(path)
    if payload.get("schema") != RESOLUTION_SCHEMA:
        raise OperationalPublicationError("research_task_publication_resolutions.json: wrong schema")
    if payload.get("status") != "ACTIVE":
        raise OperationalPublicationError("research_task_publication_resolutions.json: status must be ACTIVE")
    rows = payload.get("resolutions")
    if not isinstance(rows, list):
        raise OperationalPublicationError("research_task_publication_resolutions.json: resolutions must be list")
    out: dict[str, dict[str, Any]] = {}
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise OperationalPublicationError(f"resolution {index} must be object")
        task_id = row.get("task_id")
        if not isinstance(task_id, str) or not task_id:
            raise OperationalPublicationError(f"resolution {index} missing task_id")
        if task_id in out:
            raise OperationalPublicationError(f"duplicate resolution for {task_id}")
        out[task_id] = row
    return out


def synthesis_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    directory = root / "research_parallel_syntheses"
    if not directory.exists():
        return {}
    out: dict[str, dict[str, Any]] = {}
    for path in sorted(directory.glob("*/*.json")):
        item = _load(path)
        sid = item.get("synthesis_id")
        if isinstance(sid, str) and sid:
            if sid in out:
                raise OperationalPublicationError(f"duplicate synthesis_id {sid}")
            item["_path"] = path.relative_to(root).as_posix()
            out[sid] = item
    return out


def _normalized_resolution(
    task_id: str,
    row: dict[str, Any],
    head_ids: set[str],
    syntheses: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    operational = row.get("operational_publication_id")
    legacy_canonical = row.get("canonical_publication_id")
    if operational is None:
        operational = legacy_canonical
    if not isinstance(operational, str) or not operational:
        raise OperationalPublicationError(f"{task_id}: resolution missing operational_publication_id")
    if legacy_canonical is not None and legacy_canonical != operational:
        raise OperationalPublicationError(
            f"{task_id}: legacy canonical_publication_id disagrees with operational_publication_id"
        )

    retained = row.get("retained_parallel_publication_ids")
    if retained is None:
        legacy_other = row.get("quarantined_publication_ids", [])
        if not isinstance(legacy_other, list):
            raise OperationalPublicationError(f"{task_id}: legacy quarantined_publication_ids invalid")
        retained = [operational, *legacy_other]
    if (
        not isinstance(retained, list)
        or not retained
        or any(not isinstance(item, str) or not item for item in retained)
        or len(set(retained)) != len(retained)
    ):
        raise OperationalPublicationError(f"{task_id}: retained_parallel_publication_ids invalid")
    retained_set = set(retained)
    if operational not in head_ids:
        raise OperationalPublicationError(f"{task_id}: operational publication is not an active head: {operational}")
    if retained_set != head_ids:
        missing = sorted(head_ids - retained_set)
        extra = sorted(retained_set - head_ids)
        raise OperationalPublicationError(
            f"{task_id}: retained parallel head set mismatch; missing={missing}; extra={extra}"
        )

    legacy_quarantined = row.get("quarantined_publication_ids")
    if legacy_quarantined is not None:
        if not isinstance(legacy_quarantined, list) or any(
            not isinstance(item, str) or not item for item in legacy_quarantined
        ):
            raise OperationalPublicationError(f"{task_id}: legacy quarantined_publication_ids invalid")
        if operational in legacy_quarantined:
            raise OperationalPublicationError(f"{task_id}: operational publication appears in legacy quarantine alias")
        if not set(legacy_quarantined) <= retained_set - {operational}:
            raise OperationalPublicationError(f"{task_id}: legacy quarantine alias references non-retained publication")

    if row.get("working_truth_granted") is not False:
        raise OperationalPublicationError(f"{task_id}: operational resolution cannot grant Working Truth")
    if row.get("canonical_promotion_granted") is not False:
        raise OperationalPublicationError(f"{task_id}: operational resolution cannot grant canonical promotion")
    if row.get("successor_triggered") is not False:
        raise OperationalPublicationError(f"{task_id}: operational resolution cannot trigger successor research")

    synthesis_id = row.get("parallel_synthesis_id")
    if len(head_ids) > 1:
        if not isinstance(synthesis_id, str) or not synthesis_id:
            raise OperationalPublicationError(
                f"{task_id}: multiple active heads require parallel_synthesis_id after two reference passes"
            )
        synthesis = syntheses.get(synthesis_id)
        if synthesis is None:
            raise OperationalPublicationError(f"{task_id}: missing parallel synthesis {synthesis_id}")
        if synthesis.get("schema") != SYNTHESIS_SCHEMA:
            raise OperationalPublicationError(f"{task_id}: wrong synthesis schema")
        if synthesis.get("task_id") != task_id:
            raise OperationalPublicationError(f"{task_id}: synthesis belongs to another task")
        synth_publications = synthesis.get("publication_ids")
        if not isinstance(synth_publications, list) or set(synth_publications) != head_ids:
            raise OperationalPublicationError(f"{task_id}: synthesis does not cover exact retained head set")
        if synthesis.get("operational_publication_id") != operational:
            raise OperationalPublicationError(f"{task_id}: synthesis operational selection disagrees with resolution")
        pass_ids = synthesis.get("reference_pass_ids")
        if not isinstance(pass_ids, list) or len(pass_ids) != 2 or len(set(pass_ids)) != 2:
            raise OperationalPublicationError(f"{task_id}: synthesis must reference exactly two distinct reference passes")
    elif synthesis_id is not None:
        synthesis = syntheses.get(str(synthesis_id))
        if synthesis is None:
            raise OperationalPublicationError(f"{task_id}: resolution references missing synthesis {synthesis_id}")

    return {
        "operational_publication_id": operational,
        "retained_parallel_publication_ids": sorted(retained_set),
        "parallel_synthesis_id": synthesis_id,
    }


def selection(task_id: str, root: Path = ROOT) -> dict[str, Any] | None:
    heads = publication_heads(root).get(task_id, [])
    if not heads:
        return None
    head_by_id = {str(item.get("publication_id")): item for item in heads}
    if len(head_by_id) != len(heads) or any(not key for key in head_by_id):
        raise OperationalPublicationError(f"{task_id}: active head missing/duplicating publication_id")
    head_ids = set(head_by_id)
    row = resolution_map(root).get(task_id)
    if len(head_ids) == 1 and row is None:
        operational = next(iter(head_ids))
        return {
            "task_id": task_id,
            "operational_publication_id": operational,
            "retained_parallel_publication_ids": [operational],
            "operational_record": head_by_id[operational],
            "selection_source": "SINGLE_ACTIVE_HEAD",
            "parallel_synthesis_id": None,
        }
    if row is None:
        raise OperationalPublicationError(
            f"{task_id}: multiple active publication heads require explicit operational selection; retained={sorted(head_ids)}"
        )
    normalized = _normalized_resolution(task_id, row, head_ids, synthesis_map(root))
    operational = normalized["operational_publication_id"]
    return {
        "task_id": task_id,
        **normalized,
        "operational_record": head_by_id[operational],
        "selection_source": (
            "EXPLICIT_PARALLEL_SYNTHESIS_RESOLUTION" if len(head_ids) > 1 else "EXPLICIT_SINGLE_HEAD_RESOLUTION"
        ),
    }


def selections(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    tasks = set(publication_heads(root))
    unknown_resolutions = sorted(set(resolution_map(root)) - tasks)
    if unknown_resolutions:
        raise OperationalPublicationError(
            f"publication resolution references task without active head: {unknown_resolutions}"
        )
    out: dict[str, dict[str, Any]] = {}
    for task_id in sorted(tasks):
        value = selection(task_id, root)
        if value is not None:
            out[task_id] = value
    return out


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        pubs = iter_publications(root)
        for item in pubs:
            prefix = item.get("_record_path", "<publication>")
            if item.get("record_schema") != RECORD_SCHEMA:
                errors.append(f"{prefix}: wrong record_schema")
        selections(root)
    except Exception as exc:
        errors.append(str(exc))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Enterprise Math operational publication selector")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("audit")
    show = sub.add_parser("show")
    show.add_argument("--task-id", required=True)
    args = parser.parse_args()
    if args.command == "audit":
        errors = audit()
        if errors:
            for error in errors:
                print("ERROR:", error)
            return 1
        print(f"PASS: operational publication selections valid ({len(selections())} active task(s)).")
        return 0
    value = selection(args.task_id)
    print(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True))
    return 0 if value is not None else 2


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except OperationalPublicationError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
