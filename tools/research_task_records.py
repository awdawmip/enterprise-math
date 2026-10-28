#!/usr/bin/env python3
"""Immutable publication facade preserving source-backed semantic fields.

Task body headings are presentation. Historical heading-only waiver records
remain untouched provenance; they no longer participate in current admission.
The strict implementation retains metadata, identity, bytes and lineage checks.
"""
from __future__ import annotations

import copy
import sys
from pathlib import Path
from typing import Any

_BOOT_ROOT = Path(__file__).resolve().parents[1]
if str(_BOOT_ROOT) not in sys.path:
    sys.path.insert(0, str(_BOOT_ROOT))

from control_plane import research_task_records_impl as _core  # noqa: E402
from tools import research_taskbook  # noqa: E402

# Preserve the historical public API, including helper names used by tests and
# downstream runtime modules. Only audit/writer semantics are wrapped below.
for _name in dir(_core):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_core, _name)

# Pin the byte-identical implementation functions once. The facade can be
# imported both as tools.research_task_records and as bare research_task_records
# by historical CLI entrypoints; neither path may wrap an already-wrapped call.
if "_immutable_history_original_audit" not in _core.__dict__:
    _core.__dict__["_immutable_history_original_audit"] = _core.audit
if "_semantic_preservation_original_build_record" not in _core.__dict__:
    _core.__dict__["_semantic_preservation_original_build_record"] = _core.build_record
_STRICT_AUDIT = _core.__dict__["_immutable_history_original_audit"]
_STRICT_BUILD_RECORD = _core.__dict__["_semantic_preservation_original_build_record"]

ROOT = _core.ROOT
# Historical file vocabulary remains import-compatible; no current gate reads it.
COMPATIBILITY_FILE = "research_task_record_compatibility_waivers.json"
COMPATIBILITY_SCHEMA = "ENTERPRISE_MATH_TASK_RECORD_COMPATIBILITY_WAIVERS_V1"
COMPATIBILITY_SCOPE = "MANDATORY_BODY_SECTION_HEADING_ALIAS_ONLY"
SEMANTIC_RECORD_FIELDS = (
    "identity_lane",
    "source_refs",
    "dependencies",
    "evidence_status",
    "successor_gate",
    "migration_source",
    "parent_objective_generation_id",
)


def build_record(
    meta: dict[str, Any],
    *,
    path: Path,
    publisher_role: str,
    publisher_id: str,
    research_value: str,
    published_at: str,
    supersedes_publication_id: str | None,
    root: Path = ROOT,
) -> dict[str, Any]:
    """Create the strict record and persist exact semantic taskbook fields.

    Migration provenance remains in ``migration_source``; it must not replace
    ``identity_lane``, ``origin_kind``, ``task_lineage``, ``parent_task_id``,
    ``successor_gate`` or ``source_refs``.  This wrapper does not infer or repair
    those values: it copies the prepared taskbook bytes' parsed metadata.
    """
    record = _STRICT_BUILD_RECORD(
        meta,
        path=path,
        publisher_role=publisher_role,
        publisher_id=publisher_id,
        research_value=research_value,
        published_at=published_at,
        supersedes_publication_id=supersedes_publication_id,
        root=root,
    )
    for field in SEMANTIC_RECORD_FIELDS:
        if field in meta:
            record[field] = copy.deepcopy(meta.get(field))
    return record


def audit(root: Path = ROOT) -> list[str]:
    """Run actual V2 checks; no heading aliases or body-style waivers needed."""
    return _STRICT_AUDIT(root)


def main() -> int:
    # Bootstrap patches the canonical module, which need not be this facade
    # instance when invoked as __main__ or by a historical bare import.
    from control_plane import research_control_bootstrap
    from tools import research_task_records as canonical

    research_control_bootstrap.install(ROOT)
    # The strict CLI resolves global build_record/audit functions dynamically.
    # Patch only for this call so duplicate facade imports never stack.
    previous_audit = _core.audit
    previous_build_record = _core.build_record
    _core.audit = canonical.audit
    _core.build_record = canonical.build_record
    try:
        return _core.main()
    finally:
        _core.audit = previous_audit
        _core.build_record = previous_build_record


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except _core.TaskRecordError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
