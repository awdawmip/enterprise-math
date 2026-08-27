#!/usr/bin/env python3
"""Canonical result-registry shim with parallel-evidence and Driver follow-up gates.

The durable result/review writer/auditor lives in
``control_plane.research_result_records_impl``. This shim preserves its public
API while replacing task-level result-state reduction:

* multiple results are retained and routed through two-pass parallel evidence;
* new Driver reviews cannot terminalize runtime state until the automatic
  follow-up taskset (or canonical parent-closure exception) exists;
* the canonical CLI `review` command requires one follow-up specification and
  automatically materializes the next taskbook/taskset in the same review
  command.  The standalone follow-up guard remains a crash-recovery path.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

_REPO_ROOT = Path(__file__).resolve().parents[1]
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from control_plane import research_result_records_impl as _impl  # noqa: E402

for _name in dir(_impl):
    if not _name.startswith("__"):
        globals()[_name] = getattr(_impl, _name)

if str(_impl.ROOT) not in sys.path:
    sys.path.insert(0, str(_impl.ROOT))
import research_parallel_evidence as _parallel  # noqa: E402
import research_driver_followup as _followup_impl  # noqa: E402
import research_driver_followup_guard as _driver_followup  # noqa: E402

ROOT = _impl.ROOT


def _publication_for_state(
    task_id: str, root: Path, publication_id: str | None
) -> str | None:
    if publication_id is not None:
        return publication_id
    try:
        current = research_task_records.current_records(root).get(task_id)
    except Exception:
        current = None
    if isinstance(current, dict) and isinstance(current.get("publication_id"), str):
        return current["publication_id"]
    return None


def _review_followup_gate(
    result: dict[str, Any],
    review: dict[str, Any],
    root: Path,
) -> dict[str, Any] | None:
    """Return a nonterminal state while a governed review lacks its next taskset."""
    review_id = review.get("review_id")
    if not isinstance(review_id, str) or not review_id:
        return {
            "state": "AWAITING_DRIVER_REVIEW",
            "result": result,
            "review": review,
            "terminal": False,
            "driver_followup_state": "REVIEW_ID_UNAVAILABLE",
            "driver_followup": None,
        }
    followup = _driver_followup.state_for_review(review_id, root)
    if followup.get("required") is True and followup.get("ready") is not True:
        return {
            "state": "AWAITING_DRIVER_REVIEW",
            "result": result,
            "review": review,
            "terminal": False,
            "driver_followup_state": followup.get("state"),
            "driver_followup_error": followup.get("error"),
            "driver_followup": followup.get("packet"),
        }
    return None


def _single_result_state(
    task_id: str,
    root: Path,
    publication_id: str | None,
) -> dict[str, Any] | None:
    values = [
        item
        for item in iter_results(root)
        if item.get("task_id") == task_id
        and (publication_id is None or item.get("publication_id") == publication_id)
    ]
    if not values:
        return None
    values.sort(
        key=lambda item: (item.get("frozen_at", ""), item.get("result_id", ""))
    )
    result = values[-1]
    review = latest_review(result["result_id"], root)
    if review is None:
        return {
            "state": "AWAITING_DRIVER_REVIEW",
            "result": result,
            "review": None,
            "terminal": False,
        }

    pending = _review_followup_gate(result, review, root)
    if pending is not None:
        return pending

    followup = _driver_followup.state_for_review(review["review_id"], root)
    disposition = review.get("disposition")
    return {
        "state": (
            "TERMINAL"
            if disposition in TERMINAL_DISPOSITIONS
            else "RETURN_TO_EXECUTION"
        ),
        "result": result,
        "review": review,
        "terminal": disposition in TERMINAL_DISPOSITIONS,
        "driver_followup_state": followup.get("state"),
        "driver_followup": followup.get("packet"),
    }


def _parallel_synthesis(
    intake_id: str, evidence_set_sha256: str, root: Path
) -> dict[str, Any] | None:
    for item in _parallel.syntheses(root).values():
        if (
            item.get("intake_id") == intake_id
            and item.get("evidence_set_sha256") == evidence_set_sha256
        ):
            return item
    return None


def _parallel_followup_pending(
    result_ids: list[str], root: Path
) -> list[dict[str, Any]]:
    """Return governed reviewed results whose review->taskset barrier is incomplete."""
    by_result = {item.get("result_id"): item for item in iter_results(root)}
    pending: list[dict[str, Any]] = []
    for result_id_value in result_ids:
        result = by_result.get(result_id_value)
        if not isinstance(result, dict):
            continue
        review = latest_review(result_id_value, root)
        if review is None:
            continue
        review_id = review.get("review_id")
        if not isinstance(review_id, str) or not review_id:
            pending.append(
                {
                    "result_id": result_id_value,
                    "review_id": None,
                    "state": "REVIEW_ID_UNAVAILABLE",
                }
            )
            continue
        followup = _driver_followup.state_for_review(review_id, root)
        if followup.get("required") is True and followup.get("ready") is not True:
            pending.append(
                {
                    "result_id": result_id_value,
                    "review_id": review_id,
                    "state": followup.get("state"),
                    "error": followup.get("error"),
                }
            )
    return pending


def task_result_state(
    task_id: str,
    root: Path = ROOT,
    publication_id: str | None = None,
) -> dict[str, Any] | None:
    """Return one control state without discarding parallel research evidence.

    Single-result tasks retain generation-aware behavior except that governed
    Driver reviews remain nonterminal until their automatic follow-up taskset (or
    canonical parent-closure exception) is materialized. Parallel terminal
    synthesis inherits the same barrier for each governed reviewed result.
    """
    resolved_publication = _publication_for_state(task_id, root, publication_id)
    parallel = _parallel.state(task_id, resolved_publication, root)
    phase = parallel.get("parallel_state")
    if phase == "SINGLE_RESULT_FLOW":
        return _single_result_state(task_id, root, resolved_publication)

    result_ids = list(parallel.get("result_ids") or [])
    intake_id = parallel.get("intake_id")
    evidence_hash = parallel.get("evidence_set_sha256")
    synthetic_result = {
        "result_id": intake_id or f"PARALLEL-{task_id}",
        "task_id": task_id,
        "publication_id": resolved_publication,
        "parallel_result_ids": result_ids,
        "_record_path": None,
    }

    if phase in {
        "AWAITING_PARALLEL_INTAKE",
        "AWAITING_REFERENCE_PASS_1",
        "AWAITING_REFERENCE_PASS_2",
        "AWAITING_SYNTHESIS",
    }:
        return {
            "state": "AWAITING_DRIVER_REVIEW",
            "result": synthetic_result,
            "review": None,
            "terminal": False,
            "parallel_state": phase,
            "parallel_result_ids": result_ids,
            "parallel_intake_id": intake_id,
            "evidence_set_sha256": evidence_hash,
        }

    synthesis = (
        _parallel_synthesis(str(intake_id), str(evidence_hash), root)
        if intake_id and evidence_hash
        else None
    )
    if synthesis is None:
        return {
            "state": "AWAITING_DRIVER_REVIEW",
            "result": synthetic_result,
            "review": None,
            "terminal": False,
            "parallel_state": "AWAITING_SYNTHESIS",
            "parallel_result_ids": result_ids,
            "parallel_intake_id": intake_id,
            "evidence_set_sha256": evidence_hash,
        }

    synth_result = {
        **synthetic_result,
        "result_id": synthesis.get("synthesis_id"),
        "_record_path": synthesis.get("_path"),
    }
    if phase == "PARALLEL_SYNTHESIS_NONTERMINAL":
        return {
            "state": "RETURN_TO_EXECUTION",
            "result": synth_result,
            "review": {
                "review_id": synthesis.get("synthesis_id"),
                "disposition": synthesis.get("disposition"),
            },
            "terminal": False,
            "parallel_state": phase,
            "parallel_result_ids": result_ids,
            "parallel_intake_id": intake_id,
            "evidence_set_sha256": evidence_hash,
        }

    if phase == "PARALLEL_SYNTHESIS_TERMINAL":
        disposition = synthesis.get("terminal_control_disposition")
        if disposition not in TERMINAL_DISPOSITIONS:
            return {
                "state": "AWAITING_DRIVER_REVIEW",
                "result": synth_result,
                "review": None,
                "terminal": False,
                "parallel_state": "TERMINAL_SYNTHESIS_MISSING_CONTROL_DISPOSITION",
                "parallel_result_ids": result_ids,
                "parallel_intake_id": intake_id,
                "evidence_set_sha256": evidence_hash,
            }

        followup_pending = _parallel_followup_pending(result_ids, root)
        if followup_pending:
            return {
                "state": "AWAITING_DRIVER_REVIEW",
                "result": synth_result,
                "review": {
                    "review_id": synthesis.get("synthesis_id"),
                    "disposition": disposition,
                },
                "terminal": False,
                "parallel_state": "TERMINAL_SYNTHESIS_AWAITING_DRIVER_FOLLOWUP",
                "parallel_result_ids": result_ids,
                "parallel_intake_id": intake_id,
                "evidence_set_sha256": evidence_hash,
                "driver_followup_pending": followup_pending,
            }

        return {
            "state": "TERMINAL",
            "result": synth_result,
            "review": {
                "review_id": synthesis.get("synthesis_id"),
                "disposition": disposition,
            },
            "terminal": True,
            "parallel_state": phase,
            "parallel_result_ids": result_ids,
            "parallel_intake_id": intake_id,
            "evidence_set_sha256": evidence_hash,
        }

    raise ResultRecordError(f"unknown parallel result state: {phase}")


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


def _preflight_review_followup(
    *,
    result: dict[str, Any],
    driver_id: str,
    disposition: str,
    destination_class: str,
    spec: dict[str, Any],
) -> None:
    """Reject a bad gate/taskset specification before the immutable review write."""
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
            gate
            for gate, row in gates.items()
            if row["decision"] == "REQUIRED"
        }
        actual_roles: set[str] = set()
        for task_spec in tasks:
            if not isinstance(task_spec, dict):
                raise ResultRecordError("each follow-up task spec must be an object")
            role = task_spec.get("task_role")
            if role not in _followup_impl.TASK_ROLES:
                raise ResultRecordError(f"follow-up task has invalid task_role: {role}")
            actual_roles.add(str(role))
            text = _followup_impl._taskbook_text(
                task_spec,
                _followup_impl._source_parent_objective(probe_review, result, ROOT),
            )
            _followup_impl._preflight_taskbook(text, ROOT)
        missing = sorted(required_roles - actual_roles)
        if missing:
            raise ResultRecordError(
                f"required follow-up gates have no matching task role: {missing}"
            )
    elif tasks:
        raise ResultRecordError("PARENT_OBJECTIVE_CLOSURE follow-up cannot include tasks")


def command_review_with_followup(args: argparse.Namespace) -> int:
    result = result_map().get(args.result_id)
    if result is None:
        raise ResultRecordError(f"unknown result_id: {args.result_id}")
    spec, spec_path = _load_followup_spec(args.followup_spec)
    _preflight_review_followup(
        result=result,
        driver_id=args.driver_id,
        disposition=args.disposition,
        destination_class=args.destination_class,
        spec=spec,
    )

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
        reviewed_at=_now(args.reviewed_at),
    )
    out = REVIEW_ROOT / _safe_id(args.result_id, "result_id") / f"{record['review_id']}.json"
    _save_exclusive(out, record)

    followup = _driver_followup.materialize(
        review_id=record["review_id"],
        spec=spec,
        created_at=args.followup_created_at,
        root=ROOT,
    )

    errors = audit()
    errors.extend(_driver_followup.audit(ROOT))
    if errors:
        raise ResultRecordError(
            "review and follow-up were materialized but repository audit failed: "
            + "; ".join(errors)
        )
    print(
        json.dumps(
            {
                "review": {**record, "record_path": out.relative_to(ROOT).as_posix()},
                "followup": followup,
                "followup_spec_path": spec_path.relative_to(ROOT).as_posix()
                if spec_path.is_relative_to(ROOT)
                else str(spec_path),
            },
            ensure_ascii=False,
            indent=2,
        )
    )
    return 0


def canonical_main() -> int:
    """Own only the new review transaction; delegate other legacy-compatible commands."""
    if len(sys.argv) < 2 or sys.argv[1] != "review":
        return _impl.main()

    parser = argparse.ArgumentParser(
        description="Enterprise Math canonical Driver review + automatic follow-up taskset transaction"
    )
    parser.add_argument("review")
    parser.add_argument("--result-id", required=True)
    parser.add_argument("--driver-id", required=True)
    parser.add_argument("--disposition", choices=sorted(ALL_DISPOSITIONS), required=True)
    parser.add_argument("--review-path", required=True)
    parser.add_argument("--destination-class", choices=sorted(DESTINATION_CLASSES), required=True)
    parser.add_argument("--destination-ref-or-none", default="")
    parser.add_argument("--reviewed-at")
    parser.add_argument("--followup-spec", required=True)
    parser.add_argument("--followup-created-at")
    args = parser.parse_args()
    return command_review_with_followup(args)


if __name__ == "__main__":
    try:
        raise SystemExit(canonical_main())
    except (ResultRecordError, _followup_impl.DriverFollowupError) as exc:
        print("ERROR:", exc)
        raise SystemExit(1)
