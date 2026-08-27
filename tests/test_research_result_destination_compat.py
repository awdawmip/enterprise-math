import unittest

from tools import research_result_records as records


class HistoricalReviewDestinationCompatibilityTests(unittest.TestCase):
    def test_historical_alias_is_visible_to_audit_enum(self):
        self.assertIn("RETURN_ONLY", records._impl.DESTINATION_CLASSES)
        self.assertIn("NONE", records._impl.DESTINATION_CLASSES)

    def test_new_writer_rejects_historical_return_only_alias(self):
        with self.assertRaisesRegex(records.ResultRecordError, "historical immutable-review alias"):
            records.review_result(destination_class="RETURN_ONLY")


if __name__ == "__main__":
    unittest.main()
