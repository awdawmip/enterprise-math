import unittest
from unittest.mock import patch

import research_result_record_audit as audit_layer


class ResultRecordAuditCompatibilityTests(unittest.TestCase):
    def test_return_only_without_destination_is_narrow_historical_alias(self):
        path = "research_result_reviews/RR-X/DR-X.json"
        with patch.object(
            audit_layer.records,
            "audit",
            return_value=[
                path + ": invalid destination_class",
                path + ": review artifact blob drift",
            ],
        ), patch.object(
            audit_layer.records,
            "iter_reviews",
            return_value=[
                {
                    "record_schema": audit_layer.records.REVIEW_SCHEMA,
                    "_review_path": path,
                    "destination_class": "RETURN_ONLY",
                    "destination_ref_or_none": None,
                }
            ],
        ):
            self.assertEqual(
                [path + ": review artifact blob drift"], audit_layer.audit()
            )

    def test_return_only_with_destination_reference_is_not_compatible(self):
        path = "research_result_reviews/RR-X/DR-X.json"
        error = path + ": invalid destination_class"
        with patch.object(audit_layer.records, "audit", return_value=[error]), patch.object(
            audit_layer.records,
            "iter_reviews",
            return_value=[
                {
                    "record_schema": audit_layer.records.REVIEW_SCHEMA,
                    "_review_path": path,
                    "destination_class": "RETURN_ONLY",
                    "destination_ref_or_none": "somewhere",
                }
            ],
        ):
            self.assertEqual([error], audit_layer.audit())

    def test_current_unknown_destination_class_is_not_filtered(self):
        path = "research_result_reviews/RR-X/DR-X.json"
        error = path + ": invalid destination_class"
        with patch.object(audit_layer.records, "audit", return_value=[error]), patch.object(
            audit_layer.records,
            "iter_reviews",
            return_value=[
                {
                    "record_schema": audit_layer.records.REVIEW_SCHEMA,
                    "_review_path": path,
                    "destination_class": "SOMETHING_NEW",
                    "destination_ref_or_none": None,
                }
            ],
        ):
            self.assertEqual([error], audit_layer.audit())


if __name__ == "__main__":
    unittest.main()
