"""Compatibility shim binding review-evidence storage to the active result/review view.

The append-only storage primitive remains ``research_review_evidence_store``.
This shim is the only bridge to the canonical result registry: every operational
review-evidence read/writer validates against ``tools.research_result_records`` so
exact historical normalization and quarantined invalid records cannot be bypassed
by a second raw-file reader.
"""
from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

import research_review_evidence_store as _impl

for _name in dir(_impl):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_impl, _name)

ROOT = _impl.ROOT


def _result_registry():
    # Lazy import avoids a module cycle: tools.research_result_records imports the
    # authoritative review reducer only after establishing its active history view.
    from tools import research_result_records as records

    return records


def result_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    return _result_registry().result_map(root)


def reviews_for_result(result_id: str, root: Path = ROOT) -> list[dict[str, Any]]:
    return sorted(
        [
            item
            for item in _result_registry().iter_reviews(root)
            if item.get("result_id") == result_id
        ],
        key=lambda item: str(item.get("review_id", "")),
    )


@contextmanager
def _active_store_view() -> Iterator[None]:
    """Temporarily bind primitive store globals to the canonical active view."""
    previous_result_map = _impl.result_map
    previous_reviews = _impl.reviews_for_result
    _impl.result_map = result_map
    _impl.reviews_for_result = reviews_for_result
    try:
        yield
    finally:
        _impl.result_map = previous_result_map
        _impl.reviews_for_result = previous_reviews


def state(result_id: str, root: Path = ROOT) -> dict[str, Any]:
    with _active_store_view():
        return _impl.state(result_id, root)


def create_intake(result_id: str, opened_by: str, root: Path = ROOT) -> dict[str, Any]:
    with _active_store_view():
        return _impl.create_intake(result_id, opened_by, root)


def create_reference_pass(
    intake_id_value: str,
    pass_number: int,
    reviewer_id: str,
    finding: str,
    independence_status: str,
    root: Path = ROOT,
) -> dict[str, Any]:
    with _active_store_view():
        return _impl.create_reference_pass(
            intake_id_value,
            pass_number,
            reviewer_id,
            finding,
            independence_status,
            root,
        )


def create_synthesis(
    intake_id_value: str,
    operational_disposition: str,
    synthesized_by: str,
    rationale: str,
    root: Path = ROOT,
) -> dict[str, Any]:
    with _active_store_view():
        return _impl.create_synthesis(
            intake_id_value,
            operational_disposition,
            synthesized_by,
            rationale,
            root,
        )


def audit(root: Path = ROOT) -> list[str]:
    with _active_store_view():
        return _impl.audit(root)
