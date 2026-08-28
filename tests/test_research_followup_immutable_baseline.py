import unittest
from unittest.mock import patch

import research_driver_followup_guard as guard


class FollowupImmutableBaselineTests(unittest.TestCase):
    def test_legacy_baseline_uses_immutable_store_not_operational_view(self):
        canonical = type(
            "Canonical",
            (),
            {"iter_reviews": staticmethod(lambda root: [])},
        )
        with patch.object(guard, "legacy_review_ids", return_value=frozenset({"DR-LEGACY"})), patch.object(
            guard._raw_result_store,
            "iter_reviews",
            return_value=[{"review_id": "DR-LEGACY", "result_id": "RR-HIST"}],
        ), patch.object(guard, "_canonical_results", return_value=canonical):
            self.assertEqual([], guard.baseline_audit(guard.ROOT))
            self.assertEqual({}, guard._raw_review_map(guard.ROOT))
            self.assertIn("DR-LEGACY", guard._immutable_review_map(guard.ROOT))

    def test_missing_immutable_legacy_review_still_fails_closed(self):
        with patch.object(guard, "legacy_review_ids", return_value=frozenset({"DR-MISSING"})), patch.object(
            guard._raw_result_store,
            "iter_reviews",
            return_value=[],
        ):
            errors = guard.baseline_audit(guard.ROOT)
        self.assertEqual(1, len(errors))
        self.assertIn("DR-MISSING", errors[0])
        self.assertIn("immutable historical store", errors[0])


if __name__ == "__main__":
    unittest.main()
