"""Strict cause composition must not change a reentrant authority reader."""
from __future__ import annotations

from contextlib import ExitStack
from pathlib import Path
import sys
import unittest
from unittest import mock

BASE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(BASE))
from control_plane import research_driver_followup_fault_isolation as followup
from control_plane import research_driver_review_authority_fault_isolation as authority
from control_plane import research_nonoperational_review_source_adapter as adapter
from control_plane import research_result_review_binding_fault_isolation as binding
from control_plane import research_result_review_audit_fault_isolation as invalid


class FollowupSourceProviderReentryTests(unittest.TestCase):
    def setUp(self):
        self.root = BASE
        self.authority_rows = {"DR-AUTHORITY": {"review_id": "DR-AUTHORITY"}}
        self.binding_rows = {"DR-BINDING": {"review_id": "DR-BINDING"}}
        self.invalid_rows = {"DR-INVALID": {"review_id": "DR-INVALID"}}
        old_public = followup.validated_quarantines
        flag = "_nonoperational_review_source_adapter_installed"
        old_flag = getattr(followup, flag, None)
        had_flag = hasattr(followup, flag)
        def restore():
            followup.validated_quarantines = old_public
            if had_flag:
                setattr(followup, flag, old_flag)
            elif hasattr(followup, flag):
                delattr(followup, flag)
        self.addCleanup(restore)
        setattr(followup, flag, False)
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        self.strict_authority = self.stack.enter_context(mock.patch.object(
            authority, "validated_quarantines", return_value=self.authority_rows))
        self.strict_binding = self.stack.enter_context(mock.patch.object(
            binding, "validated_quarantines", return_value=self.binding_rows))
        self.strict_invalid = self.stack.enter_context(mock.patch.object(
            invalid, "validated_rows", return_value=self.invalid_rows))

    def test_reentrant_operational_reader_keeps_its_exact_authority_scope(self):
        # Earlier binding/audit filters have already removed their own IDs.
        incoming = [{"review_id": "DR-AUTHORITY"}, {"review_id": "DR-CURRENT"}]
        union = {**self.authority_rows, **self.binding_rows, **self.invalid_rows}
        calls = []
        def reenter(root, source_rows):
            self.assertIs(authority.validated_quarantines, self.strict_authority)
            self.assertEqual(union, source_rows)
            self.assertEqual([{"review_id": "DR-CURRENT"}], authority.operational_reviews(incoming, root))
            calls.append(root)
            return {"DFU-OLD": {"source_review_id": "DR-BINDING"}}
        with mock.patch.object(followup, "_validated_quarantines", side_effect=reenter):
            adapter.install(self.root)
            self.assertEqual({"DFU-OLD": {"source_review_id": "DR-BINDING"}}, followup.validated_quarantines(self.root))
        self.assertEqual([self.root, self.root], calls)
        self.assertIs(authority.validated_quarantines, self.strict_authority)

    def test_missing_raw_authority_review_still_fails_on_reentry(self):
        def reenter(root, source_rows):
            return authority.operational_reviews([{"review_id": "DR-CURRENT"}], root)
        with mock.patch.object(followup, "_validated_quarantines", side_effect=reenter):
            with self.assertRaisesRegex(authority.DriverReviewAuthorityIsolationError,
                                        "quarantined review.*absent from pre-isolation view"):
                adapter.install(self.root)
        self.assertIs(authority.validated_quarantines, self.strict_authority)

    def test_conflicting_cause_scopes_are_rejected_before_packet_validation(self):
        self.strict_binding.return_value = dict(self.authority_rows)
        with mock.patch.object(followup, "_validated_quarantines") as packet_validator:
            with self.assertRaisesRegex(adapter.NonoperationalReviewSourceAdapterError,
                                        "multiple cause registries"):
                adapter.install(self.root)
            packet_validator.assert_not_called()
        self.assertIs(authority.validated_quarantines, self.strict_authority)

    def test_each_strict_source_validator_failure_is_preserved(self):
        for provider in (self.strict_authority, self.strict_binding, self.strict_invalid):
            with self.subTest(provider=provider):
                followup._nonoperational_review_source_adapter_installed = False
                provider.side_effect = ValueError("exact source pin drift")
                try:
                    with mock.patch.object(followup, "_validated_quarantines") as packet_validator:
                        with self.assertRaisesRegex(ValueError, "exact source pin drift"):
                            adapter.install(self.root)
                        packet_validator.assert_not_called()
                finally:
                    provider.side_effect = None
                self.assertIs(authority.validated_quarantines, self.strict_authority)

    def test_source_drift_after_install_is_revalidated_on_each_read(self):
        with mock.patch.object(followup, "_validated_quarantines", return_value={}) as packet_validator:
            adapter.install(self.root)
            packet_validator.assert_called_once_with(
                self.root, {**self.authority_rows, **self.binding_rows, **self.invalid_rows})
            for provider in (self.strict_authority, self.strict_binding, self.strict_invalid):
                with self.subTest(provider=provider):
                    provider.side_effect = ValueError("source pin drift after install")
                    try:
                        with self.assertRaisesRegex(ValueError, "source pin drift after install"):
                            followup.validated_quarantines(self.root)
                    finally:
                        provider.side_effect = None
            self.assertEqual(1, packet_validator.call_count)
        self.assertIs(authority.validated_quarantines, self.strict_authority)


if __name__ == "__main__":
    unittest.main()
