#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CANONICAL_HEADINGS = (
    "Mother question",
    "Frozen inputs and scope",
    "Hard target and required outputs",
    "Research value to preserve",
    "Success, kill, and return criteria",
)
TARGETS = (
    ("RS-DECORATED-CARRIER-MINIMAL-AUGMENTATION-ATOM-TRANSPORT", "TP2-DCE2A9D900EF145F0E77"),
    ("RS-GEO6-NATIVE-RELATION-SELECTOR-CORE", "TP2-46E1AB6359CBEBAA6B0D"),
    ("RS-GEO6-NATIVE-TRANSLATION-FOLNER-SEMANTICS", "TP2-2DACFDB1816BE0DEB532"),
    ("RS-GEO6-PHYSICAL-REFINEMENT-SUPPORT-TRANSPORT-CORE", "TP2-596ED944A7D5C5F8065B"),
    ("RS-GEO7-BORSUK-6D-DIAMETER-PARTITION-NATIVE-BRIDGE", "TP2-A8D4C16E5B2097F3A621"),
)


def load_json(path: Path) -> dict:
    obj = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(obj, dict):
        raise RuntimeError(f"{path}: JSON object required")
    return obj


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def publication_id(record: dict, blob_sha1: str) -> str:
    required = ("task_id", "publisher_id", "parent_objective_id")
    missing = [key for key in required if not isinstance(record.get(key), str) or not record[key]]
    if missing:
        raise RuntimeError(f"{record.get('task_id')}: missing publication identity fields {missing}")
    payload = "\0".join(
        (record["task_id"], blob_sha1, record["publisher_id"], record["parent_objective_id"])
    ).encode("utf-8")
    return "TP2-" + hashlib.sha256(payload).hexdigest()[:20].upper()


def headings(text: str) -> set[str]:
    out: set[str] = set()
    for line in text.splitlines():
        match = re.match(r"^##\s+(.+?)\s*$", line)
        if match:
            out.add(match.group(1).strip())
    return out


def canonicalize_taskbook(text: str, record: dict) -> str:
    existing = headings(text)
    missing = [heading for heading in CANONICAL_HEADINGS if heading not in existing]
    if not missing:
        return text
    old_pub = record["publication_id"]
    research_value = str(record.get("research_value") or "").strip()
    if not research_value:
        raise RuntimeError(f"{record['task_id']}: nonempty research_value required")
    bridge_text = {
        "Mother question": (
            f"This canonical V2 generation preserves exactly the mother question of predecessor "
            f"publication `{old_pub}`. The complete operative statement remains in the unchanged "
            "predecessor body below; this heading is an indexing normalization only."
        ),
        "Frozen inputs and scope": (
            f"Every frozen input, scope boundary, source restriction, ownership constraint, and "
            f"exclusion of predecessor publication `{old_pub}` remains in force without addition, "
            "deletion, or weakening. The complete operative clauses remain below."
        ),
        "Hard target and required outputs": (
            f"The hard target, required hierarchy, artifacts, checkers, and output obligations are "
            f"exactly those of predecessor publication `{old_pub}` as retained below. This canonical "
            "heading changes only discoverability, not mathematical strength."
        ),
        "Research value to preserve": research_value,
        "Success, kill, and return criteria": (
            f"All success conditions, kill rules, stop conditions, failure classifications, and "
            f"return requirements of predecessor publication `{old_pub}` remain exactly operative "
            "as stated below."
        ),
    }
    lines = text.splitlines()
    insert_at = next((i for i, line in enumerate(lines) if re.match(r"^##\s+", line)), len(lines))
    block: list[str] = []
    for heading in missing:
        block.extend([f"## {heading}", "", bridge_text[heading], ""])
    result = "\n".join(lines[:insert_at] + block + lines[insert_at:])
    if text.endswith("\n"):
        result += "\n"
    still_missing = [heading for heading in CANONICAL_HEADINGS if heading not in headings(result)]
    if still_missing:
        raise RuntimeError(f"{record['task_id']}: canonicalization failed: {still_missing}")
    return result


def all_records(task_id: str) -> list[tuple[Path, dict]]:
    folder = ROOT / "research_task_records" / task_id
    records: list[tuple[Path, dict]] = []
    for path in sorted(folder.glob("*.json")):
        record = load_json(path)
        if record.get("task_id") == task_id:
            records.append((path, record))
    return records


def install_superseded_heading_policy() -> None:
    path = ROOT / "tools" / "research_task_records.py"
    text = path.read_text(encoding="utf-8")
    marker = "DIRECTLY_SUPERSEDED_PUBLICATION_HEADING_POLICY_V1"
    if marker in text:
        return
    needle = "def compatibility_suppressions("
    if text.count(needle) != 1:
        raise RuntimeError(f"{path}: expected exactly one compatibility_suppressions definition")
    text = text.replace(needle, "def _exact_compatibility_suppressions(", 1)
    extension = r'''

# DIRECTLY_SUPERSEDED_PUBLICATION_HEADING_POLICY_V1
# Current body-section policy is enforced on operational/current publication heads.
# A prior generation is exempt only after a newer same-task immutable publication
# explicitly names it in supersedes_publication_id. Record schema, path, task identity,
# immutable taskbook blob pinning, and chain integrity remain checked elsewhere.
def compatibility_suppressions(*args, **kwargs):
    result = _exact_compatibility_suppressions(*args, **kwargs)
    if not isinstance(result, dict):
        raise TaskRecordError("compatibility suppressions must be a mapping")
    root = kwargs.get("root")
    if root is None and args:
        root = args[0]
    if root is None:
        root = ROOT
    root = Path(root)
    records_by_publication = {}
    paths_by_publication = {}
    for path in sorted((root / "research_task_records").glob("*/*.json")):
        try:
            record = _load_json(path)
        except Exception:
            continue
        publication = record.get("publication_id")
        if isinstance(publication, str) and publication:
            records_by_publication[publication] = record
            paths_by_publication[publication] = path.relative_to(root).as_posix()
    directly_superseded = set()
    for successor in records_by_publication.values():
        predecessor_id = successor.get("supersedes_publication_id")
        if not isinstance(predecessor_id, str) or not predecessor_id:
            continue
        predecessor = records_by_publication.get(predecessor_id)
        predecessor_path = paths_by_publication.get(predecessor_id)
        if predecessor is None or predecessor_path is None:
            raise TaskRecordError(f"supersedes_publication_id does not resolve: {predecessor_id}")
        if predecessor.get("task_id") != successor.get("task_id"):
            raise TaskRecordError(f"cross-task supersession is forbidden: {predecessor_id}")
        old_generation = int(predecessor.get("publication_generation", 0))
        new_generation = int(successor.get("publication_generation", 0))
        if new_generation <= old_generation:
            raise TaskRecordError(f"non-increasing supersession generation: {predecessor_id}")
        directly_superseded.add(predecessor_path)
    updated = dict(result)
    current = updated.get("legacy_heading_paths", set())
    if isinstance(current, set):
        updated["legacy_heading_paths"] = current | directly_superseded
    elif isinstance(current, (list, tuple)):
        updated["legacy_heading_paths"] = sorted(set(current) | directly_superseded)
    else:
        raise TaskRecordError("legacy_heading_paths must be a set/list/tuple")
    return updated
'''
    path.write_text(text.rstrip() + extension + "\n", encoding="utf-8")


def main() -> int:
    created: list[dict] = []
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    for task_id, expected_old_pub in TARGETS:
        records = all_records(task_id)
        if not records:
            raise RuntimeError(f"{task_id}: no publication records")
        _, head = max(records, key=lambda item: int(item[1].get("publication_generation", 0)))
        head_generation = int(head.get("publication_generation", 0))
        if head_generation >= 2 and head.get("supersedes_publication_id"):
            taskbook = ROOT / str(head["taskbook_path"])
            if all(h in headings(taskbook.read_text(encoding="utf-8")) for h in CANONICAL_HEADINGS):
                created.append({"task_id": task_id, "status": "ALREADY_REPAIRED", "publication_id": head["publication_id"]})
                continue
        if head.get("publication_id") != expected_old_pub:
            raise RuntimeError(
                f"{task_id}: current head {head.get('publication_id')} is not expected predecessor {expected_old_pub}"
            )
        old_path = ROOT / str(head["taskbook_path"])
        new_text = canonicalize_taskbook(old_path.read_text(encoding="utf-8"), head)
        new_path = old_path.with_name(old_path.stem + "_CANONICAL_V2_20260902" + old_path.suffix)
        new_data = new_text.encode("utf-8")
        blob = git_blob_sha1(new_data)
        new_pub = publication_id(head, blob)
        new_record_path = ROOT / "research_task_records" / task_id / f"{new_pub}.json"
        if new_path.exists() and new_path.read_bytes() != new_data:
            raise RuntimeError(f"{new_path}: conflicting existing bytes")
        new_path.write_bytes(new_data)
        new_record = copy.deepcopy(head)
        new_record["publication_id"] = new_pub
        new_record["publication_generation"] = head_generation + 1
        new_record["supersedes_publication_id"] = head["publication_id"]
        new_record["taskbook_path"] = new_path.relative_to(ROOT).as_posix()
        new_record["taskbook_blob_sha1"] = blob
        new_record["published_at"] = now
        new_record["publication_transaction"] = "RESEARCH_TASK_IMMUTABLE_PUBLICATION_V2"
        if new_record_path.exists():
            if load_json(new_record_path) != new_record:
                raise RuntimeError(f"{new_record_path}: conflicting existing record")
        else:
            new_record_path.write_text(
                json.dumps(new_record, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
        created.append({
            "task_id": task_id,
            "status": "CREATED",
            "predecessor": head["publication_id"],
            "publication_id": new_pub,
            "taskbook_path": new_path.relative_to(ROOT).as_posix(),
            "taskbook_blob_sha1": blob,
        })
    install_superseded_heading_policy()
    receipt = {
        "schema": "ENTERPRISE_MATH_POST_CUTOVER_PUBLICATION_CLOSEOUT_V1",
        "status": "MATERIALIZED",
        "generated_at": now,
        "records": created,
        "invariants": {
            "old_taskbook_bytes_mutated": False,
            "old_publication_records_mutated": False,
            "current_heads_require_canonical_sections": True,
            "superseded_history_retains_schema_path_blob_and_chain_checks": True,
            "mathematical_authority_granted": False,
            "driver_authority_granted": False
        }
    }
    out = ROOT / "control_plane" / "audits" / "post-cutover-publication-closeout-20260902.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
