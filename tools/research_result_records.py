#!/usr/bin/env python3
"""Canonical result/review runtime over immutable-history and exact-set authority.

The compatibility + parallel-result base lives in
``control_plane.research_result_records_compat_runtime``. This public tool adds
only the Driver-review multiplicity layer: zero/one review keeps the low-burden
flow, while two or more immutable reviews require exact-set intake, two reference
passes, and synthesis. No reviewed_at/latest-review ordering is control authority.
"""
from __future__ import annotations

import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from control_plane import research_result_records_compat_runtime as _base  # noqa: E402

for _name in dir(_base):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_base, _name)

if str(_base.ROOT) not in sys.path:
    sys.path.insert(0, str(_base.ROOT))
import research_review_evidence as _review_evidence  # noqa: E402

ROOT = _base.ROOT
_BASE_TASK_RESULT_STATE = _base.task_result_state
_PENDING_REVIEW_STATES = {
    "AWAITING_REVIEW_INTAKE",
    "AWAITING_REVIEW_REFERENCE_PASS_1",
    "AWAITING_REVIEW_REFERENCE_PASS_2",
    "AWAITING_REVIEW_SYNTHESIS",
}
_RESOLVED_REVIEW_STATES = {
    "SINGLE_REVIEW_FLOW",
    "REVIEW_SYNTHESIS_TERMINAL",
    "REVIEW_SYNTHESIS_NONTERMINAL",
}


@contextmanager
def _base_runtime_view() -> Iterator[None]:
    """Bind the compatibility reducer to this public facade for one reduction.

    The public tool is the canonical runtime surface. Consumers and tests may
    deliberately substitute its active result/review helpers (for example to
    query an isolated publication generation). The compatibility reducer must
    observe that same facade rather than a stale module-local copy of helpers
    captured before the exact-set review overlay was installed.
    """

    names = ("iter_results", "iter_reviews", "latest_review", "_parallel_synthesis")
    previous = {name: getattr(_base, name) for name in names}
    try:
        for name in names:
            setattr(_base, name, globals()[name])
        yield
    finally:
        for name, value in previous.items():
            setattr(_base, name, value)


def _single_review_authority(result: dict[str, Any], root: Path) -> dict[str, Any]:
    state = _review_evidence.state(str(result["result_id"]), root)
    phase = state.get("review_state")
    if phase == "NO_REVIEW":
        return {
            "state": "AWAITING_DRIVER_REVIEW",
            "result": result,
            "review": None,
            "terminal": False,
            "review_parallel_state": phase,
            "parallel_review_ids": [],
        }
    if phase in _PENDING_REVIEW_STATES:
        return {
            "state": "AWAITING_DRIVER_REVIEW",
            "result": result,
            "review": None,
            "terminal": False,
            "review_parallel_state": phase,
            "parallel_review_ids": list(state.get("review_ids") or []),
            "review_intake_id": state.get("intake_id"),
            "review_set_sha256": state.get("review_set_sha256"),
        }
    if phase == "SINGLE_REVIEW_FLOW":
        review = state.get("review")
        if not isinstance(review, dict):
            raise ResultRecordError("single-review authority is missing its immutable review")
        disposition = state.get("operational_disposition")
        terminal = disposition in TERMINAL_DISPOSITIONS
        return {
            "state": "TERMINAL" if terminal else "RETURN_TO_EXECUTION",
            "result": result,
            "review": review,
            "terminal": terminal,
            "review_parallel_state": phase,
            "parallel_review_ids": list(state.get("review_ids") or []),
        }
    if phase in {"REVIEW_SYNTHESIS_TERMINAL", "REVIEW_SYNTHESIS_NONTERMINAL"}:
        synthesis = state.get("synthesis")
        if not isinstance(synthesis, dict):
            raise ResultRecordError("review synthesis authority is missing its synthesis record")
        disposition = state.get("operational_disposition")
        terminal = disposition in TERMINAL_DISPOSITIONS
        return {
            "state": "TERMINAL" if terminal else "RETURN_TO_EXECUTION",
            "result": result,
            "review": {
                "review_id": synthesis.get("synthesis_id"),
                "disposition": disposition,
                "review_synthesis": synthesis,
                "parallel_review_ids": list(state.get("review_ids") or []),
            },
            "terminal": terminal,
            "review_parallel_state": phase,
            "parallel_review_ids": list(state.get("review_ids") or []),
            "review_intake_id": state.get("intake_id"),
            "review_set_sha256": state.get("review_set_sha256"),
        }
    raise ResultRecordError(f"unexpected Driver-review authority state: {phase}")


def _parallel_review_authority(
    result_ids: list[str], root: Path
) -> tuple[dict[str, dict[str, Any]], list[str]]:
    states: dict[str, dict[str, Any]] = {}
    pending: list[str] = []
    for result_id_value in sorted(result_ids):
        state = _review_evidence.state(result_id_value, root)
        states[result_id_value] = state
        if state.get("review_state") not in _RESOLVED_REVIEW_STATES:
            pending.append(result_id_value)
    return states, pending


def task_result_state(
    task_id: str,
    root: Path = ROOT,
    publication_id: str | None = None,
) -> dict[str, Any] | None:
    """Compose parallel-result control with exact current review authority."""
    with _base_runtime_view():
        base = _BASE_TASK_RESULT_STATE(task_id, root, publication_id)
    if base is None:
        return None

    result_ids = list(base.get("parallel_result_ids") or [])
    if result_ids:
        states, pending = _parallel_review_authority(result_ids, root)
        if pending:
            return {
                **base,
                "state": "AWAITING_DRIVER_REVIEW",
                "review": None,
                "terminal": False,
                "parallel_state": "AWAITING_RESULT_REVIEW_AUTHORITY",
                "pending_result_review_ids": pending,
                "result_review_authority": states,
            }
        return {**base, "result_review_authority": states}

    result = base.get("result")
    if not isinstance(result, dict) or not isinstance(result.get("result_id"), str):
        return base
    return _single_review_authority(result, root)


# Internal consumers that deliberately import the compatibility base after this
# public tool has initialized should see the same composed task reducer.
_base.task_result_state = task_result_state


if __name__ == "__main__":
    try:
        raise SystemExit(_base._impl.main())
    except ResultRecordError as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
