#!/usr/bin/env python3
"""Resolve or allocate visible Enterprise Math Researcher-IDs.

Scheduler CLAIM identities are deterministic from (task_id, claim_id). Direct
user tasks or role transitions without a claim receive a random short-code ID
that the conversation must retain. GLOBAL_KNOWLEDGE registration is one file
per identity, avoiding shared-directory startup races.
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


def valid_researcher_id(value: str) -> bool:
    return bool(ID_RE.fullmatch(value.strip().upper()))


def deterministic_claim_id(task_id: str, claim_id: str, *, lane: str | None = None) -> str:
    if not task_id.strip() or not claim_id.strip():
        raise ValueError("task_id and claim_id are required")
    resolved_lane = infer_lane(task_id, role="RESEARCHER", explicit_lane=lane)
    digest = hashlib.sha256(f"{task_id}\0{claim_id}".encode("utf-8")).hexdigest()[:6].upper()
    return f"EM-{resolved_lane}-{digest}"


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


def registration_path(researcher_id: str) -> str:
    normalized = researcher_id.strip().upper()
    if not valid_researcher_id(normalized):
        raise ValueError(f"invalid Researcher-ID: {researcher_id}")
    return f"{REGISTRATION_ROOT}/{normalized}.json"


def identity_payload(
    *,
    researcher_id: str,
    task_id: str | None,
    role: str,
    source: str,
) -> dict[str, Any]:
    if not valid_researcher_id(researcher_id):
        raise ValueError(f"invalid Researcher-ID: {researcher_id}")
    task = task_id or ("CONTROL_PLANE" if role == "RESEARCH_DRIVER" else "DIRECT")
    return {
        "schema": "ENTERPRISE_MATH_RESEARCH_IDENTITY_V1",
        "researcher_id": researcher_id,
        "research_task": task,
        "research_role": role,
        "identity_source": source,
        "registration_repository": "awdawmip/chatgpt-global-knowledge",
        "registration_path": registration_path(researcher_id),
        "registration_state": "REGISTER_PENDING",
        "visible_marker": f"Researcher-ID: {researcher_id} / {task}",
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Enterprise Math research identity resolver")
    sub = parser.add_subparsers(dest="command", required=True)

    allocate = sub.add_parser("allocate")
    allocate.add_argument("--task")
    allocate.add_argument("--role", choices=["RESEARCHER", "RESEARCH_DRIVER"], default="RESEARCHER")
    allocate.add_argument("--lane")
    allocate.add_argument("--claim-id")
    allocate.add_argument("--primary-driver", action="store_true")
    allocate.add_argument("--marker-only", action="store_true")

    validate = sub.add_parser("validate")
    validate.add_argument("researcher_id")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "validate":
        if valid_researcher_id(args.researcher_id):
            print(args.researcher_id.strip().upper())
            return 0
        print("invalid Researcher-ID", file=sys.stderr)
        return 1

    if args.claim_id:
        if not args.task:
            raise ValueError("--claim-id requires --task")
        researcher_id = deterministic_claim_id(args.task, args.claim_id, lane=args.lane)
        source = "SCHEDULER_CLAIM_DERIVED"
    else:
        researcher_id = allocate_direct(
            task_id=args.task,
            role=args.role,
            lane=args.lane,
            primary_driver=args.primary_driver,
        )
        source = "DIRECT_AUTO_GENERATED"

    payload = identity_payload(
        researcher_id=researcher_id,
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
