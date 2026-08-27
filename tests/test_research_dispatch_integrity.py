import unittest
from unittest.mock import patch

import research_dispatch_integrity as integrity


class DispatchIntegrityCompositionTests(unittest.TestCase):
    def test_dispatch_integrity_uses_compatibility_audits_not_raw_history_audits(self):
        legacy = {"tasks": []}
        owners = {}
        with patch.object(integrity.dispatch, "load_json", side_effect=[legacy, owners]), patch.object(
            integrity.dispatch, "control_authorization_policy", return_value={}
        ), patch.object(
            integrity.dispatch.research_scheduler, "validate_scheduler", return_value=[]
        ), patch.object(
            integrity.research_task_record_audit, "audit", return_value=["task-compatible-marker"]
        ), patch.object(
            integrity.dispatch.research_task_records,
            "audit",
            side_effect=AssertionError("raw task audit must not be called"),
        ), patch.object(
            integrity.dispatch.research_execution_records, "audit", return_value=[]
        ), patch.object(
            integrity.research_result_record_audit, "audit", return_value=["result-compatible-marker"]
        ), patch.object(
            integrity.dispatch.research_result_records,
            "audit",
            side_effect=AssertionError("raw result audit must not be called"),
        ), patch.object(
            integrity.dispatch.research_cohort_runtime, "audit", return_value=[]
        ), patch.object(
            integrity.dispatch, "merged_definitions", return_value=[]
        ), patch.object(
            integrity.dispatch.research_task_records, "current_records", return_value={}
        ):
            out = integrity.audit()
        self.assertEqual(
            ["task-compatible-marker", "result-compatible-marker"], out
        )


if __name__ == "__main__":
    unittest.main()
