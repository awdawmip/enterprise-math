#!/usr/bin/env python3
"""Audit the chat/GitHub remote-manual task-publication fallback.

Remote/manual publication is transport fallback only.  It must preserve the same
canonical preflight as ``tools/research_task_records.py`` and may never treat a
later green CI run as retroactive publication authorization.

This maintenance checker reads configuration only. Documentation wording and
implementation spelling are not publication gates; native writers validate the
actual operation. It does not inspect task mathematics.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))



class RemotePublicationPreflightError(ValueError):
    pass


def _load(path: str) -> dict:
    value = json.loads((ROOT / path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise RemotePublicationPreflightError(f"{path}: JSON object required")
    return value


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RemotePublicationPreflightError(message)


def check() -> None:
    authority = _load("control_plane/current_control_authority.json")
    task = authority.get("task_publication", {})
    require(
        task.get("remote_manual_transport_fallback_allowed") is True,
        "remote/manual GitHub transport fallback must remain available",
    )
    require(
        task.get("remote_manual_validation_fallback_allowed") is False,
        "remote/manual transport must not become a validation fallback",
    )
    require(
        task.get("remote_manual_equivalent_preflight_required") is True,
        "remote/manual publication must require canonical-equivalent preflight",
    )
    require(task.get("remote_manual_body_style_required") is False,
            "remote/manual publication must not require fixed heading style")
    require(
        task.get("remote_manual_exact_taskbook_blob_required") is True,
        "remote/manual publication must pin exact taskbook Git blob",
    )
    require(
        task.get("remote_manual_exact_supersedes_required_when_revision") is True,
        "remote/manual revision must pin exact superseded publication",
    )
    require(
        task.get("remote_manual_unresolved_fork") == "FAIL_CLOSED_NO_HEAD_SELECTION",
        "remote/manual publication must not choose a head from unresolved fork",
    )
    require(
        task.get("remote_manual_cas_nonforce_required") is True,
        "remote/manual mutation must use CAS/non-force semantics",
    )
    require(
        task.get("reference_integrity_is_publication_authorization") is False,
        "reference-integrity may not retroactively authorize publication",
    )
    require(
        task.get("if_equivalent_preflight_unavailable")
        == "NONEXECUTABLE_DRAFT_OR_HANDOFF_ONLY",
        "missing equivalent preflight must degrade to non-executable draft/handoff",
    )



def main() -> int:
    try:
        check()
    except (RemotePublicationPreflightError, OSError, json.JSONDecodeError) as exc:
        print("ERROR:", exc)
        return 1
    print(
        "PASS: remote/manual task-publication configuration declares canonical "
        "body/blob/supersedes/CAS preflight; CI is backstop, not authorization."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

