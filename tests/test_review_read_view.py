"""Read-only reuse keeps the exact review/follow-up validators and failures."""
from pathlib import Path
from unittest.mock import Mock,patch

import pytest
from control_plane import research_result_review_audit_fault_isolation as audit
from control_plane.research_read_view import read_view,immutable_source_view

ROOT=Path(__file__).resolve().parents[1]


def test_exact_validator_runs_once_and_returns_independent_copies():
    expected=audit.validated_rows(ROOT)
    assert expected
    with patch.object(audit,'_validated_rows',wraps=audit._validated_rows) as compute:
        with immutable_source_view(ROOT),read_view(ROOT):
            first=audit.validated_rows(ROOT)
            first[next(iter(first))]['task_id']='synthetic-mutation'
            assert audit.validated_rows(ROOT)==expected
            assert compute.call_count==1
        assert audit.validated_rows(ROOT)==expected
        assert compute.call_count==2


def test_changed_exact_validator_still_rejects_and_failure_is_not_cached():
    original=audit._review_errors
    with read_view(ROOT):
        audit.validated_rows(ROOT)
        with patch.object(audit,'_review_errors',side_effect=lambda *a:original(*a)+['synthetic unexpected error']) as errors:
            for _ in range(2):
                with pytest.raises(audit.ReviewAuditIsolationError,match='exact audit error set drift'):
                    audit.validated_rows(ROOT)
            assert errors.call_count>=2


def test_other_root_does_not_use_current_root_validation(tmp_path):
    expected=audit.validated_rows(ROOT)
    with read_view(ROOT):
        assert audit.validated_rows(ROOT)==expected
        assert audit.validated_rows(tmp_path)=={}


def test_followup_cause_validation_reuses_only_stable_operational_readers():
    import research_control_dispatch
    from control_plane import research_driver_followup_fault_isolation as followup
    from tools import research_result_records as results
    with patch.object(followup,'_validated_quarantines',wraps=followup._validated_quarantines) as compute:
        with read_view(ROOT):
            first=followup.validated_quarantines(ROOT)
            assert followup.validated_quarantines(ROOT)==first
            assert compute.call_count==1
            with patch.object(results,'iter_reviews',wraps=results.iter_reviews):
                assert followup.validated_quarantines(ROOT)==first
                assert compute.call_count==2
