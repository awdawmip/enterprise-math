#!/usr/bin/env python3
"""Resolve or allocate Enterprise Math role identities.

Researcher conversations use a visible `Researcher-ID`; Driver conversations use
`Driver-ID`. The underlying execution-ID grammar remains compatible with existing
`EM-<LANE>-<SHORTCODE>` handles. Driver-mediated manual dispatches may preallocate
a deterministic Researcher-ID outside the reusable taskbook.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import secrets
import sys
from typing import Any

ID_RE = re.compile(r"^EM-[A-Z0-9]+-(?:[0-9]{2}|[A-Z0-9]{4,8})$")
LANE_RE = re.compile(r"[^A-Z0-9]+")
TASK_LANE_RE = re.compile(r"^RS-((?:R|P)\d{3}[A-Z]?)\b")
REGISTRATION_ROOT = "projects/enterprise-math/researchers"


def normalize_lane(value: str) -> str:
    lane = LANE_RE.sub("", value.strip().upper())
    if not lane:
        raise ValueError("identity lane must contain an alphanumeric character")
    return lane[:16]


def infer_lane(task_id: str | None, *, role: str, explicit_lane: str | None = None) -> str:
    if explicit_lane:
        return normalize_lane(explicit_lane)
    if role == "RESEARCH_DRIVER":
        return "DVR"
    if task_id:
        match = TASK_LANE_RE.match(task_id.strip().upper())
        if match:
            return normalize_lane(match.group(1))
        compact = task_id.strip().upper()
        if compact.startswith("RS-"):
            compact = compact[3:]
        first = compact.split("-", 1)[0]
        if first:
            return normalize_lane(first)
    return "DIRECT"


def valid_execution_id(value: str) -> bool:
    return bool(ID_RE.fullmatch(value.strip().upper()))


def valid_researcher_id(value: str) -> bool:
    """Backward-compatible validator name for existing scheduler/tests."""
    return valid_execution_id(value)


def identity_label(role: str) -> str:
    if role == "RESEARCH_DRIVER":
        return "Driver-ID"
    if role == "RESEARCHER":
        return "Researcher-ID"
    raise ValueError(f"unsupported research role: {role}")


def _deterministic_id(task_id: str, token: str, *, lane: str | None = None) -> str:
    if not task_id.strip() or not token.strip():
        raise ValueError("task_id and identity token are required")
    resolved_lane = infer_lane(task_id, role="RESEARCHER", explicit_lane=lane)
    digest = hashlib.sha256(f"{task_id}\0{token}".encode("utf-8")).hexdigest()[:6].upper()
    return f"EM-{resolved_lane}-{digest}"


def deterministic_claim_id(task_id: str, claim_id: str, *, lane: str | None = None) -> str:
    return _deterministic_id(task_id, claim_id, lane=lane)


def deterministic_dispatch_id(task_id: str, dispatch_id: str, *, lane: str | None = None) -> str:
    """Preallocate one Researcher-ID for one Driver-mediated manual dispatch."""
    return _deterministic_id(task_id, dispatch_id, lane=lane)


def allocate_direct(
    *,
    task_id: str | None,
    role: str,
    lane: str | None = None,
    primary_driver: bool = False,
) -> str:
    if role == "RESEARCH_DRIVER" and primary_driver:
        return "EM-DRIVER-01"
    resolved_lane = infer_lane(task_id, role=role, explicit_lane=lane)
    suffix = secrets.token_hex(3).upper()
    return f"EM-{resolved_lane}-{suffix}"


def registration_path(execution_id: str) -> str:
    normalized = execution_id.strip().upper()
    if not valid_execution_id(normalized):
        raise ValueError(f"invalid Enterprise Math execution identity: {execution_id}")
    return f"{REGISTRATION_ROOT}/{normalized}.json"


def identity_payload(
    *,
    task_id: str | None,
    role: str,
    source: str,
    execution_id: str | None = None,
    researcher_id: str | None = None,
) -> dict[str, Any]:
    """Build role-aware identity metadata.

    `researcher_id` remains accepted as an input alias so existing callers do not
    need a flag-day migration. Output is role-aware: Researchers expose
    `researcher_id`; Drivers expose `driver_id`. Both expose `execution_id`.
    """
    resolved = execution_id or researcher_id
    if not resolved or not valid_execution_id(resolved):
        raise ValueError(f"invalid Enterprise Math execution identity: {resolved}")
    task = task_id or ("CONTROL_PLANE" if role == "RESEARCH_DRIVER" else "DIRECT")
    label = identity_label(role)
    payload: dict[str, Any] = {
        "schema": "ENTERPRISE_MATH_ROLE_IDENTITY_V2",
        "execution_id": resolved,
        "identity_label": label,
        "research_task": task,
        "research_role": role,
        "identity_source": source,
        "registration_repository": "awdawmip/chatgpt-global-knowledge",
        "registration_path": registration_path(resolved),
        "registration_state": "REGISTER_PENDING",
        "visible_marker": f"{label}: {resolved} / {task}",
    }
    if role == "RESEARCH_DRIVER":
        payload["driver_id"] = resolved
    else:
        payload["researcher_id"] = resolved
    return payload


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Enterprise Math role identity resolver")
    sub = parser.add_subparsers(dest="command", required=True)

    allocate = sub.add_parser("allocate")
    allocate.add_argument("--task")
    allocate.add_argument("--role", choices=["RESEARCHER", "RESEARCH_DRIVER"], default="RESEARCHER")
    allocate.add_argument("--lane")
    allocate.add_argument("--claim-id")
    allocate.add_argument("--dispatch-id")
    allocate.add_argument("--primary-driver", action="store_true")
    allocate.add_argument("--marker-only", action="store_true")

    validate = sub.add_parser("validate")
    validate.add_argument("execution_id")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "validate":
        if valid_execution_id(args.execution_id):
            print(args.execution_id.strip().upper())
            return 0
        print("invalid Enterprise Math execution identity", file=sys.stderr)
        return 1

    if args.claim_id and args.dispatch_id:
        raise ValueError("--claim-id and --dispatch-id are mutually exclusive")

    if args.claim_id:
        if args.role != "RESEARCHER":
            raise ValueError("scheduler CLAIM identity is a Researcher-ID")
        if not args.task:
            raise ValueError("--claim-id requires --task")
        execution_id = deterministic_claim_id(args.task, args.claim_id, lane=args.lane)
        source = "SCHEDULER_CLAIM_DERIVED"
    elif args.dispatch_id:
        if args.role != "RESEARCHER":
            raise ValueError("manual dispatch preallocation is a Researcher-ID")
        if not args.task:
            raise ValueError("--dispatch-id requires --task")
        execution_id = deterministic_dispatch_id(args.task, args.dispatch_id, lane=args.lane)
        source = "MANUAL_DISPATCH_DERIVED"
    else:
        execution_id = allocate_direct(
            task_id=args.task,
            role=args.role,
            lane=args.lane,
            primary_driver=args.primary_driver,
        )
        source = "DIRECT_AUTO_GENERATED"

    payload = identity_payload(
        execution_id=execution_id,
        task_id=args.task,
        role=args.role,
        source=source,
    )
    if args.marker_only:
        print(payload["visible_marker"])
    else:
        print(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(2)
