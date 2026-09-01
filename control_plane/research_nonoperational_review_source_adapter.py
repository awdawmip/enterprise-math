#!/usr/bin/env python3
"""Compose independent nonoperational-review causes for follow-up isolation.

Driver-authority quarantine, stale result-binding quarantine, and exact immutable
review-audit quarantine remain separate registries with separate validators. The
follow-up isolation needs one derived fact only: whether its source review is
currently nonoperational. This adapter supplies their disjoint union without
changing any underlying cause semantics or Driver disposition.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]


class NonoperationalReviewSourceAdapterError(ValueError):
    pass


def _disjoint_union(
    sources: dict[str, dict[str, dict[str, Any]]]
) -> dict[str, dict[str, Any]]:
    owners: dict[str, str] = {}
    out: dict[str, dict[str, Any]] = {}
    overlaps: list[str] = []
    for label, rows in sources.items():
        for review_id, row in rows.items():
            prior = owners.get(review_id)
            if prior is not None:
                overlaps.append(f"{review_id}:{prior}+{label}")
                continue
            owners[review_id] = label
            out[review_id] = row
    if overlaps:
        raise NonoperationalReviewSourceAdapterError(
            "review cannot be quarantined by multiple cause registries without "
            f"explicit synthesis: {sorted(overlaps)}"
        )
    return out


def review_rows(root: Path = ROOT) -> dict[str, dict[str, Any]]:
    from control_plane import research_driver_review_authority_fault_isolation as authority
    from control_plane import research_result_review_audit_fault_isolation as audit
    from control_plane import research_result_review_binding_fault_isolation as binding

    return _disjoint_union(
        {
            "DRIVER_AUTHORITY": authority.validated_quarantines(root),
            "RESULT_BINDING": binding.validated_quarantines(root),
            "REVIEW_AUDIT": audit.validated_rows(root),
        }
    )


def install(root: Path = ROOT) -> None:
    """Teach the existing follow-up isolation to consume all exact causes."""
    from control_plane import research_driver_followup_fault_isolation as followup
    from control_plane import research_driver_review_authority_fault_isolation as authority

    if getattr(followup, "_nonoperational_review_source_adapter_installed", False):
        return
    base_validated: Callable[[Path], dict[str, dict[str, Any]]] = followup.validated_quarantines
    original_authority_validated = authority.validated_quarantines

    def combined_followup_validated(
        local_root: Path = followup.ROOT,
    ) -> dict[str, dict[str, Any]]:
        def combined_review_rows(
            review_root: Path = local_root,
        ) -> dict[str, dict[str, Any]]:
            # Use the original authority validator so the temporary substitution
            # cannot recurse through itself.
            from control_plane import research_result_review_audit_fault_isolation as audit
            from control_plane import research_result_review_binding_fault_isolation as binding

            return _disjoint_union(
                {
                    "DRIVER_AUTHORITY": original_authority_validated(review_root),
                    "RESULT_BINDING": binding.validated_quarantines(review_root),
                    "REVIEW_AUDIT": audit.validated_rows(review_root),
                }
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
