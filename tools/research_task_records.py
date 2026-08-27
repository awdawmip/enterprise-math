#!/usr/bin/env python3
"""Canonical task-publication shim with supersession-aware historical audit.

The immutable task-publication implementation lives in
``control_plane.research_task_records_impl``. Current publication heads must
satisfy the current taskbook body schema. A historical generation that is
*exactly superseded* by another immutable publication remains auditable under
its original bytes: only current-body-heading errors are grandfathered for that
superseded record; blob, task/objective identity and every other invariant stay
fail-closed.
"""
from __future__ import annotations

from pathlib import Path

from control_plane import research_task_records_impl as _impl

# Preserve the historical public/module surface for every existing consumer.
for _name in dir(_impl):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_impl, _name)

_legacy_audit = _impl.audit
ROOT = _impl.ROOT


def _superseded_record_paths(root: Path) -> set[str]:
    records = _impl.iter_records(root)
    superseded_ids = {
        str(item["supersedes_publication_id"])
        for item in records
        if isinstance(item.get("supersedes_publication_id"), str)
        and item["supersedes_publication_id"]
    }
    return {
        str(item.get("_record_path"))
        for item in records
        if item.get("publication_id") in superseded_ids
        and isinstance(item.get("_record_path"), str)
    }


def audit(root: Path = ROOT) -> list[str]:
    """Run the canonical audit without retroactively rewriting immutable history.

    A current schema upgrade may not make a previously published immutable
    generation impossible to retain. The compatibility allowance is therefore
    deliberately tiny: for an exact superseded record only, suppress errors of
    the form ``mandatory body section ...``. Every other error from the original
    auditor survives unchanged, and any unsuperseded/current head must satisfy
    the current mandatory section schema.
    """
    errors = _legacy_audit(root)
    historical_paths = _superseded_record_paths(root)
    filtered: list[str] = []
    for error in errors:
        allow_historical_body_heading = any(
            error.startswith(f"{path}: mandatory body section")
            for path in historical_paths
        )
        if not allow_historical_body_heading:
            filtered.append(error)
    return filtered


# The implementation's command_publish/command_audit resolve ``audit`` from the
# implementation module globals, so patch the one compatibility-aware reducer
# back into that module rather than maintaining a second command implementation.
_impl.audit = audit


if __name__ == "__main__":
    try:
        raise SystemExit(_impl.main())
    except TaskRecordError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
