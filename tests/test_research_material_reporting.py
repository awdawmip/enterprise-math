"""Communication and private derivation never mint shared-task authority."""
import unittest
from unittest.mock import patch

import research_pre_final_authority as authority
from tools import research_runtime_guard as guard


class ResearchMaterialReportingTests(unittest.TestCase):
    def test_ordinary_reports_do_not_require_legacy_administrative_bindings(self):
        states = ({}, {"task": {"task_id": "old-task"}},
                  {"task_registration": {"state": "LEGACY_BASELINE_REGISTERED"}},
                  {"parent_objective": {"status": "COMPLETE"}, "publication_id": "missing"})
        for state in states:
            for module in (authority, guard):
                with self.subTest(state=state, module=module.__name__):
                    with patch.object(guard, "canonicalize_registration", side_effect=AssertionError("report is no authority check")):
                        result = module.pre_final_gate(state)
                    self.assertTrue(result["material_report_allowed"])
                    self.assertTrue(result["persistence_allowed"])
                    self.assertFalse(result["authorized"])
                    self.assertFalse(result["task_completion_authorized"])

    def test_formal_completion_still_authenticates_registration(self):
        for module in (authority, guard):
            with self.subTest(module=module.__name__):
                with self.assertRaises((guard.RuntimeAuthorizationError, ValueError)):
                    module.pre_final_gate({"task": {"task_id": "missing"}}, formal_task_completion=True)

    def test_unshared_derivation_does_not_require_or_mint_an_activity(self):
        with patch.object(guard._activity, "guard", side_effect=AssertionError("no ledger precondition")):
            result = guard.authorize_execution({"research_mode": "FREE_AXIOM_DISCOVERY"}, events=[])
        self.assertTrue(result["activity_allowed"])
        self.assertFalse(result["authorized"])
        self.assertEqual("UNSHARED_DERIVATION_AND_MATERIALS", result["scope"])

    def test_even_empty_formal_binding_cannot_use_unshared_path(self):
        for key in ("task", "task_id", "publication_id", "owner_claim", "execution_binding", "claim_id", "execution_cohort_id", "execution_lane_id"):
            state = {key: None, "research_mode": "FREE_AXIOM_DISCOVERY"}
            with self.subTest(key=key):
                self.assertFalse(guard._is_activity_state(state))

    def test_supplied_invalid_activity_still_rejected(self):
        with self.assertRaises(guard.RuntimeAuthorizationError):
            guard.authorize_execution({"activity_id": "", "research_mode": "FREE_AXIOM_DISCOVERY"}, events=[])


if __name__ == "__main__":
    unittest.main()
