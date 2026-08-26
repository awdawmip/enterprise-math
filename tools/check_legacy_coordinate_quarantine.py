#!/usr/bin/env python3
"""Validate main-side quarantine metadata for superseded coordinate ontologies."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "legacy_coordinate_quarantine_registry.json"
SCHEMA = "ENTERPRISE_MATH_LEGACY_COORDINATE_QUARANTINE_REGISTRY_V1"


def audit() -> list[str]:
    errors: list[str] = []
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    if data.get("schema") != SCHEMA:
        errors.append("wrong quarantine registry schema")
    if data.get("status") != "ACTIVE":
        errors.append("quarantine registry must be ACTIVE")
    entries = data.get("entries")
    if not isinstance(entries, list) or not entries:
        return errors + ["quarantine registry requires at least one entry"]
    seen: set[str] = set()
    for entry in entries:
        qid = entry.get("quarantine_id")
        prefix = qid if isinstance(qid, str) else "<entry>"
        if not isinstance(qid, str) or not qid or qid in seen:
            errors.append(f"{prefix}: missing or duplicate quarantine_id")
        if isinstance(qid, str):
            seen.add(qid)
        if not str(entry.get("branch", "")).startswith("archive/"):
            errors.append(f"{prefix}: quarantine branch must use archive/ namespace")
        if len(str(entry.get("archive_head", ""))) != 40:
            errors.append(f"{prefix}: archive_head must be a full commit SHA")
        if not str(entry.get("archive_manifest_blob_sha1", "")).startswith("sha1:"):
            errors.append(f"{prefix}: archive manifest blob SHA-1 is required")
        if entry.get("runtime_effect") != "NONE":
            errors.append(f"{prefix}: runtime_effect must be NONE")
        if entry.get("foundation_authority") != "NONE":
            errors.append(f"{prefix}: foundation_authority must be NONE")
        for field in (
            "working_truth_granted",
            "task_authority_granted",
            "canonical_promotion_granted",
            "successor_triggered",
        ):
            if entry.get(field) is not False:
                errors.append(f"{prefix}: {field} must be false")
        if entry.get("requires_explicit_revalidation") is not True:
            errors.append(f"{prefix}: requires_explicit_revalidation must be true")
        router = entry.get("current_authority_router")
        if not isinstance(router, str) or not (ROOT / router).exists():
            errors.append(f"{prefix}: current authority router missing")
    return errors


if __name__ == "__main__":
    failures = audit()
    if failures:
        for failure in failures:
            print("ERROR:", failure)
        raise SystemExit(1)
    print("PASS: legacy coordinate quarantine registry is authority-safe.")
