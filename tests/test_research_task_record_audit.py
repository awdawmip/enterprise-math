import unittest
from unittest.mock import patch

import research_task_record_audit as audit_layer


class RetainedTaskRecordAuditTests(unittest.TestCase):
    def test_only_retained_nonoperational_body_shape_errors_are_compatible(self):
        retained_path = "research_task_records/RS-T/TP2-OLD.json"
        errors = [
            retained_path + ": mandatory body section is missing or empty: Frozen inputs and scope",
            retained_path + ": taskbook blob drift",
            "research_task_records/RS-U/TP2-CURRENT.json: mandatory body section is missing or empty: Hard target and required outputs",
        ]
        resolutions = {
            "RS-T": {
                "canonical_publication_id": "TP2-NEW",
                "quarantined_publication_ids": ["TP2-OLD"],
                "working_truth_granted": False,
                "canonical_promotion_granted": False,
                "successor_triggered": False,
            }
        }
        with patch.object(audit_layer.records, "audit", return_value=errors), patch.object(
            audit_layer.records, "publication_resolutions", return_value=resolutions
        ):
            out = audit_layer.audit()
        self.assertEqual(
            [
                retained_path + ": taskbook blob drift",
                "research_task_records/RS-U/TP2-CURRENT.json: mandatory body section is missing or empty: Hard target and required outputs",
            ],
            out,
        )

    def test_placeholder_body_error_is_compatible_only_for_explicit_retained_head(self):
        path = "research_task_records/RS-T/TP2-OLD.json"
        with patch.object(
            audit_layer.records,
            "audit",
            return_value=[
                path + ": mandatory body section contains placeholder text: Research value to preserve"
            ],
        ), patch.object(
            audit_layer.records,
            "publication_resolutions",
            return_value={
                "RS-T": {
                    "canonical_publication_id": "TP2-NEW",
                    "quarantined_publication_ids": ["TP2-OLD"],
                }
            },
        ):
            self.assertEqual([], audit_layer.audit())

    def test_no_resolution_means_no_body_compatibility(self):
        error = (
            "research_task_records/RS-T/TP2-OLD.json: mandatory body section is missing or empty: "
            "Success, kill, and return criteria"
        )
        with patch.object(audit_layer.records, "audit", return_value=[error]), patch.object(
            audit_layer.records, "publication_resolutions", return_value={}
        ):
            self.assertEqual([error], audit_layer.audit())


if __name__ == "__main__":
    unittest.main()
