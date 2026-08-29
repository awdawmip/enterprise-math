#!/usr/bin/env python3
"""Audit the chat/GitHub remote-manual task-publication fallback.

Remote/manual publication is transport fallback only.  It must preserve the same
canonical preflight as ``tools/research_task_records.py`` and may never treat a
later green CI run as retroactive publication authorization.

This checker is control-plane only; it does not inspect task mathematics.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from control_plane import research_task_records_impl as record_core  # noqa: E402


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
    protocol = (ROOT / "docs" / "RESEARCH_TASK_PUBLICATION_PROTOCOL.md").read_text(
        encoding="utf-8"
    )
    envelope = (
        ROOT / "control_plane" / "check_post_cutover_publication_envelope.py"
    ).read_text(encoding="utf-8")

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
    require(
        tuple(task.get("remote_manual_required_body_sections", []))
        == tuple(record_core.MANDATORY_BODY_SECTIONS),
        "remote/manual mandatory body sections drifted from canonical publication tool",
    )
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

    for marker in (
        "LOCAL_PUBLICATION_TOOL_UNAVAILABLE != PREFLIGHT_OPTIONAL",
        "REMOTE_MANUAL_RECORD_WRITE != CANONICAL_PUBLISH_UNLESS_EQUIVALENT_PREFLIGHT_PASSES",
        "REFERENCE_INTEGRITY_IS_BACKSTOP_NOT_PUBLICATION_AUTHORIZATION",
        "Direct GitHub publication is therefore a **transport fallback**, not a semantic or validation fallback.",
    ):
        require(marker in protocol, f"publication protocol missing remote fallback invariant: {marker}")

    for section in record_core.MANDATORY_BODY_SECTIONS:
        require(section in protocol, f"publication protocol missing canonical body section {section}")

    require(
        "record_core.validate_body(body)" in envelope,
        "earliest post-cutover envelope gate must execute canonical body validation",
    )
    require(
        "known_defect_paths" in envelope,
        "post-cutover envelope must isolate only exact already-known defects",
    )


def main() -> int:
    try:
        check()
    except (RemotePublicationPreflightError, OSError, json.JSONDecodeError) as exc:
        print("ERROR:", exc)
        return 1
    print(
        "PASS: remote/manual task publication is transport-only and retains canonical "
        "body/blob/supersedes/CAS preflight; CI is backstop, not authorization."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
