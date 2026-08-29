#!/usr/bin/env python3
"""Rollback-safe local transaction for newly-created immutable control artifacts.

The transaction never overwrites an existing path.  Every target is preflighted,
then created exclusively.  If a deterministic post-check fails, only files whose
bytes still exactly equal this transaction's planned bytes are removed.  Existing
immutable history is never deleted or rewritten.

This is local working-tree safety, not remote Git authority.  Remote publication
still requires the repository's compare-and-swap / non-force rules.
"""
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable


class ImmutableWriteTransactionError(ValueError):
    pass


@dataclass(frozen=True)
class PlannedFile:
    path: Path
    content: bytes


def json_bytes(value: object) -> bytes:
    import json

    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def text_bytes(value: str) -> bytes:
    return value.encode("utf-8")


def preflight(files: Iterable[PlannedFile]) -> list[PlannedFile]:
    rows = list(files)
    if not rows:
        raise ImmutableWriteTransactionError("immutable transaction has no files")
    seen: set[Path] = set()
    for row in rows:
        path = row.path.resolve()
        if path in seen:
            raise ImmutableWriteTransactionError(f"duplicate immutable transaction target: {row.path}")
        seen.add(path)
        if row.path.exists():
            raise ImmutableWriteTransactionError(f"immutable transaction target already exists: {row.path}")
        if not row.content:
            raise ImmutableWriteTransactionError(f"immutable transaction target has empty payload: {row.path}")
    return rows


def _write_exclusive(row: PlannedFile) -> None:
    row.path.parent.mkdir(parents=True, exist_ok=True)
    try:
        with row.path.open("xb") as handle:
            handle.write(row.content)
            handle.flush()
            os.fsync(handle.fileno())
    except FileExistsError as exc:
        raise ImmutableWriteTransactionError(
            f"immutable transaction target appeared after preflight: {row.path}"
        ) from exc


def _rollback(created: list[PlannedFile]) -> list[str]:
    errors: list[str] = []
    for row in reversed(created):
        try:
            if not row.path.exists():
                continue
            actual = row.path.read_bytes()
            if actual != row.content:
                errors.append(
                    f"refused rollback because immutable candidate changed after creation: {row.path}"
                )
                continue
            row.path.unlink()
        except Exception as exc:
            errors.append(f"rollback failed for {row.path}: {exc}")
    return errors


def commit(
    files: Iterable[PlannedFile],
    *,
    postcheck: Callable[[], list[str] | None] | None = None,
) -> list[Path]:
    """Create all planned files or roll back this transaction's unchanged bytes."""

    rows = preflight(files)
    created: list[PlannedFile] = []
    try:
        for row in rows:
            _write_exclusive(row)
            created.append(row)
        if postcheck is not None:
            errors = postcheck() or []
            if errors:
                raise ImmutableWriteTransactionError(
                    "immutable transaction post-check failed: " + "; ".join(errors)
                )
    except Exception as exc:
        rollback_errors = _rollback(created)
        detail = f"{exc}"
        if rollback_errors:
            detail += "; " + "; ".join(rollback_errors)
        if isinstance(exc, ImmutableWriteTransactionError):
            raise ImmutableWriteTransactionError(detail) from exc
        raise ImmutableWriteTransactionError(detail) from exc
    return [row.path for row in rows]
