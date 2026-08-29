#!/usr/bin/env python3
"""Canonical result/review runtime over immutable history and exact-set authority.

Layers are intentionally ordered:

1. immutable-history compatibility + publication-generation result reduction;
2. same-execution control-only result replacement (history retained, final sink operational);
3. exact-set Driver-review authority (never reviewed_at/latest-review wins);
4. Driver-review follow-up barrier consuming the *operational* review authority;
5. parallel-result synthesis only after every genuinely parallel source result has
   resolved review and follow-up authority.

A second immutable review therefore does not publish follow-up work on its own.
It first reopens review exact-set control; follow-up is materialized only after the
review synthesis becomes the operational authority.

Canonical ``freeze`` and ``review`` writes are candidate-first: the record is
validated before it exists on disk, then created through an exclusive rollback-
safe local transaction.  A failed post-write audit removes only unchanged bytes
created by that transaction; existing immutable history is never rewritten.
"""
from __future__ import annotations

import argparse
import json
import sys
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from control_plane import immutable_write_transaction as _write_tx  # noqa: E402
from control_plane import research_immutable_candidate_validation as _candidate_validation  # noqa: E402
from control_plane import research_result_records_compat_runtime as _base  # noqa: E402

for _name in dir(_base):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_base, _name)

if str(_base.ROOT) not in sys.path:
    sys.path.insert(0, str(_base.ROOT))
import research_review_evidence as _review_evidence  # noqa: E402
import research_driver_followup as _followup_impl  # noqa: E402
import research_driver_followup_guard as _driver_followup  # noqa: E402
import research_driver_authority as _driver_authority  # noqa: E402
import research_result_control_replacements as _result_replacements  # noqa: E402

ROOT = _base.ROOT
_BASE_TASK_RESULT_STATE = _base.task_result_state
_BASE_ITER_RESULTS = _base.iter_results
_BASE_ITER_REVIEWS = _base.iter_reviews
_BASE_AUDIT = _base.audit
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


def _install_canonical_write_view() -> None:
    """Bind writers to the same fault-isolated operational view used by dispatch."""

    from control_plane import research_control_bootstrap

    research_control_bootstrap.install(ROOT)


def _replacement_edges(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    raw = _base._RAW_ITER_RESULTS(root)
    raw_map = {
        str(item.get("result_id")): item
        for item in raw
        if isinstance(item.get("result_id"), str) and item.get("result_id")
    }
    edges = _result_replacements.replacement_edges(raw_map, root)
    if not edges:
        return {}
    base_ids = {
        str(item.get("result_id"))
        for item in _BASE_ITER_RESULTS(root)
        if isinstance(item.get("result_id"), str) and item.get("result_id")
    }
    sources = set(edges)
    targets = {
        str(row.get("corrected_result_id"))
        for row in edges.values()
        if isinstance(row.get("corrected_result_id"), str)
    }
    missing_sources = sources - base_ids
    missing_targets = targets - base_ids
    if missing_sources:
        raise ResultRecordError(
            "control-result replacement source is already absent from the canonical compatibility view: "
            + repr(sorted(missing_sources))
        )
    if missing_targets:
        raise ResultRecordError(
            "control-result replacement target is absent from the canonical compatibility view: "
            + repr(sorted(missing_targets))
        )
    return edges


def iter_results(root: Path = ROOT) -> list[dict[str, Any]]:
    edges = _replacement_edges(root)
    replaced = set(edges)
    return [
        item for item in _BASE_ITER_RESULTS(root)
        if item.get("result_id") not in replaced
    ]


def iter_reviews(root: Path = ROOT) -> list[dict[str, Any]]:
    replaced = set(_replacement_edges(root))
    return [
        item for item in _BASE_ITER_REVIEWS(root)
        if item.get("result_id") not in replaced
    ]


def result_map(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for item in iter_results(root):
        rid = item.get("result_id")
        if not isinstance(rid, str) or not rid:
            raise ResultRecordError("result record missing result_id")
        if rid in out:
            raise ResultRecordError(f"duplicate result_id: {rid}")
        out[rid] = item
    return out


def audit(root: Path = ROOT) -> list[str]:
    errors = list(_BASE_AUDIT(root))
    errors.extend(_result_replacements.audit(root))
    try:
        iter_results(root)
        iter_reviews(root)
    except Exception as exc:
        errors.append(str(exc))
    return errors


def _parallel_results(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    return result_map(root)


def _parallel_reviews(root: Path = ROOT) -> dict[str, list[dict[str, Any]]]:
    out: dict[str, list[dict[str, Any]]] = {}
    for item in iter_reviews(root):
        rid = item.get("result_id")
        if isinstance(rid, str) and rid:
            out.setdefault(rid, []).append(item)
    return out


# Any parallel reducer reached through the canonical public result tool consumes
# the post-replacement operational view. The raw compatibility audit remains
# unchanged and still validates historical source bytes.
_base._parallel.results = _parallel_results
_base._parallel.result_reviews = _parallel_reviews


@contextmanager
def _base_runtime_view() -> Iterator[None]:
    """Bind the compatibility reducer to this public facade for one reduction."""

    names = ("iter_results", "iter_reviews", "latest_review", "_parallel_synthesis")
    previous = {name: getattr(_base, name) for name in names}
    try:
        for name in names:
            setattr(_base, name, globals()[name])
        yield
    finally:
        for name, value in previous.items():
            setattr(_base, name, value)


def _apply_followup_gate(
    reduced: dict[str, Any], result: dict[str, Any], root: Path
) -> dict[str, Any]:
    authority = reduced.get("review")
    if not isinstance(authority, dict):
        return reduced
    authority_id = authority.get("review_authority_id") or authority.get("review_id")
    if not isinstance(authority_id, str) or not authority_id:
        raise ResultRecordError("resolved review authority has no authority id")
    followup = _driver_followup.state_for_review(authority_id, root)
    if followup.get("required") is True and followup.get("ready") is not True:
        return {
            **reduced,
            "state": "AWAITING_DRIVER_REVIEW",
            "result": result,
            "terminal": False,
            "driver_followup_state": followup.get("state"),
            "driver_followup_error": followup.get("error"),
            "driver_followup": followup.get("packet"),
        }
    return {
        **reduced,
        "driver_followup_state": followup.get("state"),
        "driver_followup": followup.get("packet"),
    }


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
    if phase not in _RESOLVED_REVIEW_STATES:
        raise ResultRecordError(f"unexpected Driver-review authority state: {phase}")

    authority = _driver_followup.authority_for_result(str(result["result_id"]), root)
    if not isinstance(authority, dict):
        raise ResultRecordError("resolved review evidence has no operational authority tuple")
    disposition = authority.get("disposition")
    terminal = disposition in TERMINAL_DISPOSITIONS
    reduced = {
        "state": "TERMINAL" if terminal else "RETURN_TO_EXECUTION",
        "result": result,
        "review": authority,
        "terminal": terminal,
        "review_parallel_state": phase,
        "parallel_review_ids": list(state.get("review_ids") or []),
        "review_intake_id": state.get("intake_id"),
        "review_set_sha256": state.get("review_set_sha256"),
    }
    return _apply_followup_gate(reduced, result, root)


def _parallel_review_authority(
    result_ids: list[str], root: Path
) -> tuple[
    dict[str, dict[str, Any]],
    dict[str, dict[str, Any]],
    list[str],
    list[str],
]:
    evidence_states: dict[str, dict[str, Any]] = {}
    authorities: dict[str, dict[str, Any]] = {}
    review_pending: list[str] = []
    followup_pending: list[str] = []
    for result_id_value in sorted(result_ids):
        state = _review_evidence.state(result_id_value, root)
        evidence_states[result_id_value] = state
        if state.get("review_state") not in _RESOLVED_REVIEW_STATES:
            review_pending.append(result_id_value)
            continue
        authority = _driver_followup.authority_for_result(result_id_value, root)
        if authority is None:
            review_pending.append(result_id_value)
            continue
        authorities[result_id_value] = authority
        authority_id = authority.get("review_authority_id") or authority.get("review_id")
        followup = _driver_followup.state_for_review(str(authority_id), root)
        authority["driver_followup_state"] = followup.get("state")
        authority["driver_followup"] = followup.get("packet")
        if followup.get("required") is True and followup.get("ready") is not True:
            followup_pending.append(result_id_value)
    return evidence_states, authorities, review_pending, followup_pending


def task_result_state(
    task_id: str,
    root: Path = ROOT,
    publication_id: str | None = None,
) -> dict[str, Any] | None:
    """Compose generation, replacement, review, follow-up, and parallel-result authority."""
    with _base_runtime_view():
        base = _BASE_TASK_RESULT_STATE(task_id, root, publication_id)
    if base is None:
        return None

    result_ids = list(base.get("parallel_result_ids") or [])
    if result_ids:
        evidence, authorities, review_pending, followup_pending = _parallel_review_authority(
            result_ids, root
        )
        if review_pending:
            return {
                **base,
                "state": "AWAITING_DRIVER_REVIEW",
                "review": None,
                "terminal": False,
                "parallel_state": "AWAITING_RESULT_REVIEW_AUTHORITY",
                "pending_result_review_ids": review_pending,
                "result_review_authority": evidence,
                "result_operational_review_authority": authorities,
            }
        if followup_pending:
            return {
                **base,
                "state": "AWAITING_DRIVER_REVIEW",
                "review": None,
                "terminal": False,
                "parallel_state": "AWAITING_RESULT_REVIEW_FOLLOWUP",
                "pending_result_followup_ids": followup_pending,
                "result_review_authority": evidence,
                "result_operational_review_authority": authorities,
            }
        return {
            **base,
            "result_review_authority": evidence,
            "result_operational_review_authority": authorities,
        }

    result = base.get("result")
    if not isinstance(result, dict) or not isinstance(result.get("result_id"), str):
        return base
    return _single_review_authority(result, root)


def _load_followup_spec(path_value: str) -> tuple[dict[str, Any], Path]:
    path = Path(path_value)
    if not path.is_absolute():
        path = ROOT / path
    if not path.exists():
        raise ResultRecordError(f"follow-up spec not found: {path}")
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ResultRecordError("follow-up spec root must be an object")
    return value, path


def _preflight_first_review_followup(
    *,
    result: dict[str, Any],
    driver_id: str,
    disposition: str,
    destination_class: str,
    spec: dict[str, Any],
) -> None:
    probe_review = {
        "review_id": "DR-PREFLIGHT",
        "result_id": result["result_id"],
        "task_id": result["task_id"],
        "publication_id": result["publication_id"],
        "driver_id": driver_id.strip().upper(),
        "disposition": disposition,
        "destination_class": destination_class,
        "reviewed_at": "2000-01-01T00:00:00+00:00",
    }
    gates = _followup_impl._gate_map(spec.get("gate_decisions"))
    _followup_impl._forced_gate_rules(probe_review, result, gates)
    decision = spec.get("decision")
    tasks = spec.get("tasks", [])
    if decision not in _followup_impl.DECISIONS:
        raise ResultRecordError("follow-up spec decision is invalid")
    if not isinstance(tasks, list):
        raise ResultRecordError("follow-up spec tasks must be a list")
    if decision == "TASK_SET_PUBLISHED":
        if not tasks:
            raise ResultRecordError("TASK_SET_PUBLISHED follow-up requires at least one task")
        required_roles = {
            gate for gate, row in gates.items() if row["decision"] == "REQUIRED"
        }
        actual_roles: set[str] = set()
        parent = _followup_impl._source_parent_objective(probe_review, result, ROOT)
        for task_spec in tasks:
            if not isinstance(task_spec, dict):
                raise ResultRecordError("each follow-up task spec must be an object")
            role = task_spec.get("task_role")
            if role not in _followup_impl.TASK_ROLES:
                raise ResultRecordError(f"follow-up task has invalid task_role: {role}")
            actual_roles.add(str(role))
            text = _followup_impl._taskbook_text(task_spec, parent)
            _followup_impl._preflight_taskbook(text, ROOT)
        missing = sorted(required_roles - actual_roles)
        if missing:
            raise ResultRecordError(
                f"required follow-up gates have no matching task role: {missing}"
            )
    elif tasks:
        raise ResultRecordError("PARENT_OBJECTIVE_CLOSURE follow-up cannot include tasks")


def command_freeze_transactional(args: argparse.Namespace) -> int:
    _install_canonical_write_view()
    return_path = Path(args.return_path)
    if not return_path.is_absolute():
        return_path = ROOT / return_path
    values = json.loads(args.output_paths_json)
    if not isinstance(values, list):
        raise ResultRecordError("--output-paths-json must decode to an array")
    output_paths: list[Path] = []
    for value in values:
        if not isinstance(value, str):
            raise ResultRecordError("output paths must be strings")
        path = Path(value)
        output_paths.append(path if path.is_absolute() else ROOT / path)
    record = freeze_result(
        execution_record_id=args.execution_record_id,
        return_path=return_path,
        output_paths=output_paths,
        owner_head=args.owner_head,
        terminal_verdict=args.terminal_verdict,
        hard_target_disposition=args.hard_target_disposition,
        unresolved_residue=args.unresolved_residue,
        method_harvest=args.method_harvest,
        independence_status=args.independence_status,
        source_exposure_status=args.source_exposure_status,
        next_control_plane_recommendation=args.next_control_plane_recommendation,
        frozen_at=_now(args.frozen_at),
    )
    try:
        _candidate_validation.require_valid_result_candidate(record, root=ROOT)
    except _candidate_validation.ImmutableCandidateValidationError as exc:
        raise ResultRecordError(f"result candidate preflight failed: {exc}") from exc
    out = RESULT_ROOT / _safe_id(record["task_id"], "task_id") / f"{record['result_id']}.json"
    try:
        _write_tx.commit(
            [_write_tx.PlannedFile(out, _write_tx.json_bytes(record))],
            postcheck=lambda: audit(ROOT),
        )
    except _write_tx.ImmutableWriteTransactionError as exc:
        raise ResultRecordError(f"result transaction failed with no committed candidate: {exc}") from exc
    print(
        json.dumps(
            {**record, "record_path": out.relative_to(ROOT).as_posix()},
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def command_review_with_authority(args: argparse.Namespace) -> int:
    _install_canonical_write_view()
    result = result_map().get(args.result_id)
    if result is None:
        raise ResultRecordError(f"unknown result_id: {args.result_id}")

    existing = [
        row for row in iter_reviews() if row.get("result_id") == args.result_id
    ]
    spec: dict[str, Any] | None = None
    spec_path: Path | None = None
    if not existing:
        if not args.followup_spec:
            raise ResultRecordError(
                "the first immutable review becomes operational immediately and requires --followup-spec"
            )
        spec, spec_path = _load_followup_spec(args.followup_spec)
        _preflight_first_review_followup(
            result=result,
            driver_id=args.driver_id,
            disposition=args.disposition,
            destination_class=args.destination_class,
            spec=spec,
        )
    elif args.followup_spec:
        raise ResultRecordError(
            "a second-or-later review reopens exact-set review authority; "
            "materialize follow-up only after review synthesis"
        )

    reviewed_at = _now(args.reviewed_at)
    try:
        driver_authority = _driver_authority.require_active_driver(
            args.driver_id, reviewed_at, ROOT
        )
    except _driver_authority.DriverAuthorityError as exc:
        raise ResultRecordError(str(exc)) from exc

    path = Path(args.review_path)
    if not path.is_absolute():
        path = ROOT / path
    record = review_result(
        result=result,
        driver_id=args.driver_id,
        disposition=args.disposition,
        review_path=path,
        destination_class=args.destination_class,
        destination_ref_or_none=args.destination_ref_or_none,
        reviewed_at=reviewed_at,
    )
    if driver_authority is not None:
        record["driver_authority_record_id"] = driver_authority["authority_record_id"]
        record["driver_authority_source_comment_id"] = driver_authority["source_comment_id"]
        authority_errors = _driver_authority.review_authority_errors(record, ROOT)
        if authority_errors:
            raise ResultRecordError("; ".join(authority_errors))

    try:
        _candidate_validation.require_valid_review_candidate(record, root=ROOT)
    except _candidate_validation.ImmutableCandidateValidationError as exc:
        raise ResultRecordError(f"review candidate preflight failed: {exc}") from exc

    out = REVIEW_ROOT / _safe_id(args.result_id, "result_id") / f"{record['review_id']}.json"
    try:
        _write_tx.commit(
            [_write_tx.PlannedFile(out, _write_tx.json_bytes(record))],
            postcheck=lambda: audit(ROOT),
        )
    except _write_tx.ImmutableWriteTransactionError as exc:
        raise ResultRecordError(f"review transaction failed with no committed candidate: {exc}") from exc

    followup: dict[str, Any]
    if not existing:
        assert spec is not None
        followup = _driver_followup.materialize(
            review_id=record["review_id"],
            spec=spec,
            created_at=args.followup_created_at,
            root=ROOT,
        )
        followup_errors = _driver_followup.audit(ROOT)
        if followup_errors:
            raise ResultRecordError(
                "review/follow-up materialized but follow-up audit failed: "
                + "; ".join(followup_errors)
            )
    else:
        state = _review_evidence.state(args.result_id, ROOT)
        followup = {
            "state": "DEFERRED_UNTIL_EXACT_REVIEW_SYNTHESIS",
            "review_state": state.get("review_state"),
            "review_ids": state.get("review_ids"),
        }

    payload = {
        "review": {**record, "record_path": out.relative_to(ROOT).as_posix()},
        "followup": followup,
    }
    if spec_path is not None:
        payload["followup_spec_path"] = (
            spec_path.relative_to(ROOT).as_posix()
            if spec_path.is_relative_to(ROOT)
            else str(spec_path)
        )
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


# Keep the compatibility parser/CLI surface, but make canonical freeze candidate-first.
_base._impl.command_freeze = command_freeze_transactional


def canonical_main() -> int:
    if len(sys.argv) < 2 or sys.argv[1] != "review":
        return _base._impl.main()

    parser = argparse.ArgumentParser(
        description="Enterprise Math Driver review transaction over exact-set authority"
    )
    parser.add_argument("review")
    parser.add_argument("--result-id", required=True)
    parser.add_argument("--driver-id", required=True)
    parser.add_argument("--disposition", choices=sorted(ALL_DISPOSITIONS), required=True)
    parser.add_argument("--review-path", required=True)
    parser.add_argument("--destination-class", choices=sorted(DESTINATION_CLASSES), required=True)
    parser.add_argument("--destination-ref-or-none", default="")
    parser.add_argument("--reviewed-at")
    parser.add_argument("--followup-spec")
    parser.add_argument("--followup-created-at")
    args = parser.parse_args()
    return command_review_with_authority(args)


# Internal consumers importing the compatibility base after this public tool has
# initialized must see the same composed reducer.
_base.task_result_state = task_result_state


if __name__ == "__main__":
    try:
        raise SystemExit(canonical_main())
    except (
        ResultRecordError,
        _followup_impl.DriverFollowupError,
        _driver_authority.DriverAuthorityError,
        _result_replacements.ResultControlReplacementError,
        _candidate_validation.ImmutableCandidateValidationError,
        _write_tx.ImmutableWriteTransactionError,
    ) as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
