#!/usr/bin/env python3
"""Compose independent nonoperational-review causes for follow-up isolation.

Driver-authority quarantine, result-binding quarantine, and invalid-review audit
quarantine are deliberately separate registries with separate validators. The
existing follow-up isolation only needs one fact: whether its source review is
currently nonoperational. This adapter supplies the union to that layer without
changing any underlying quarantine's semantics.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]


class NonoperationalReviewSourceAdapterError(ValueError):
    pass


def _merge_causes(
    causes: list[tuple[str, dict[str, dict[str, Any]]]],
) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    source: dict[str, str] = {}
    for cause_name, rows in causes:
        for review_id, row in rows.items():
            if review_id in out:
                raise NonoperationalReviewSourceAdapterError(
                    f"review cannot be quarantined by multiple cause registries without explicit synthesis: "
                    f"{review_id} ({source[review_id]}, {cause_name})"
                )
            out[review_id] = row
            source[review_id] = cause_name
    return out


def review_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    from control_plane import research_driver_review_authority_fault_isolation as authority
    from control_plane import research_result_review_binding_fault_isolation as binding
    from control_plane import research_result_review_audit_fault_isolation as invalid_review

    return _merge_causes(
        [
            ("DRIVER_AUTHORITY", authority.validated_quarantines(root)),
            ("RESULT_BINDING", binding.validated_quarantines(root)),
            ("INVALID_REVIEW_RECORD", invalid_review.validated_rows(root)),
        ]
    )


def install(root: Path = ROOT) -> None:
    """Teach the existing follow-up isolation to consume the union of causes."""
    from control_plane import research_driver_followup_fault_isolation as followup
    from control_plane import research_driver_review_authority_fault_isolation as authority

    if getattr(followup, "_nonoperational_review_source_adapter_installed", False):
        return
    base_validated: Callable[[Path], dict[str, dict[str, Any]]] = followup.validated_quarantines
    original_authority_validated = authority.validated_quarantines

    def combined_followup_validated(local_root: Path = followup.ROOT) -> dict[str, dict[str, Any]]:
        def combined_review_rows(review_root: Path = local_root) -> dict[str, dict[str, Any]]:
            # Use the original authority validator here so this temporary adapter
            # cannot recurse through itself.
            from control_plane import research_result_review_binding_fault_isolation as binding
            from control_plane import research_result_review_audit_fault_isolation as invalid_review

            return _merge_causes(
                [
                    ("DRIVER_AUTHORITY", original_authority_validated(review_root)),
                    ("RESULT_BINDING", binding.validated_quarantines(review_root)),
                    ("INVALID_REVIEW_RECORD", invalid_review.validated_rows(review_root)),
                ]
            )

        saved = authority.validated_quarantines
        authority.validated_quarantines = combined_review_rows
        try:
            return base_validated(local_root)
        finally:
            authority.validated_quarantines = saved

    followup.validated_quarantines = combined_followup_validated
    followup._nonoperational_review_source_adapter_installed = True
    # Validate immediately so bootstrap fails closed on any stale exact pin.
    combined_followup_validated(root)


def audit(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        review_rows(root)
        install(root)
        from control_plane import research_driver_followup_fault_isolation as followup

        errors.extend(followup.audit(root))
    except Exception as exc:
        errors.append(str(exc))
    return errors


if __name__ == "__main__":
    failures = audit()
    if failures:
        for failure in failures:
            print("ERROR:", failure)
        raise SystemExit(1)
    print("PASS: follow-up isolation consumes all exact nonoperational review causes.")
