import copy
import unittest
from unittest.mock import patch

import research_pre_final_authority as authority


class RepositoryDerivedPreFinalTests(unittest.TestCase):
    def state(self, **overrides):
        value = {
            "parent_objective": {"objective_id": "OBJ-CALLER", "status": "COMPLETE"},
            "task_registration": {"registry_key": "RS-T1", "state": "CLAIMABLE"},
            "task": {"task_id": "RS-T1", "status": "COMPLETE"},
            "owner_claim": {},
            "session": {"last_activity_at": "2026-08-27T00:00:00+00:00"},
            "durable_frontier": {},
            "current_unfinished_unit": None,
            "next_action": None,
            "terminal_scope": None,
            "final_allowed": False,
            "control": {},
        }
        value.update(overrides)
        return value

    @staticmethod
    def canonicalized(state, *, purpose, root):
        value = copy.deepcopy(dict(state))
        value["task_registration"] = {
            "state": "IMMUTABLE_REGISTERED",
            "registry_key": "RS-T1",
            "publication_id": "TP2-T1",
            "claimable": True,
        }
        return value

    @staticmethod
    def task_records(root):
        return {
            "RS-T1": {
                "task_id": "RS-T1",
                "publication_id": "TP2-T1",
                "parent_objective_id": "OBJ-REAL",
            }
        }

    @staticmethod
    def closure(complete, state="DERIVED_PARENT_COMPLETE"):
        return {
            "objective_id": "OBJ-REAL",
            "objective_generation_id": "OG-1",
            "derived_parent_complete": complete,
            "state": state,
            "final_permission_granted": False,
            "next_control_action": (
                "PRE_FINAL_LIVENESS_RECHECK" if complete else "CONTINUE_OBJECTIVE_WORK"
            ),
        }

    def run_gate(self, state, closure):
        with patch.object(
            authority.research_runtime_guard,
            "canonicalize_registration",
            side_effect=self.canonicalized,
        ), patch.object(
            authority.research_task_records,
            "current_records",
            side_effect=self.task_records,
        ), patch.object(
            authority.research_parent_closure,
            "derive_objective_closure",
            return_value=closure,
        ) as derive:
            out = authority.pre_final_gate(state)
        return out, derive

    def test_forged_caller_complete_is_ignored_when_repository_parent_open(self):
        out, derive = self.run_gate(
            self.state(), self.closure(False, "OBJECTIVE_HEAD_NOT_CLOSED")
        )
        self.assertFalse(out["canonical_final_allowed"])
        self.assertFalse(out["caller_supplied_parent_status_is_authority"])
        self.assertEqual("REPOSITORY_DERIVED_PARENT_CLOSURE", out["parent_status_authority"])
        self.assertEqual("OBJECTIVE_HEAD_NOT_CLOSED", out["parent_closure"]["state"])
        derive.assert_called_once_with("OBJ-REAL", authority.ROOT)

    def test_repository_closed_and_no_unfinished_runtime_allows_final(self):
        out, _ = self.run_gate(self.state(), self.closure(True))
        self.assertTrue(out["canonical_final_allowed"])
        self.assertEqual("FINAL_ALLOWED", out["transition"])

    def test_repository_closed_but_unfinished_runtime_fails_inconsistent(self):
        state = self.state(
            current_unfinished_unit="finish child synthesis",
            next_action={"description": "finish child synthesis", "executable": True},
        )
        out, _ = self.run_gate(state, self.closure(True))
        self.assertFalse(out["canonical_final_allowed"])
        self.assertEqual("CONTROL_STATE_INCONSISTENT", out["transition"])

    def test_incomplete_active_cohort_projection_forces_parent_open(self):
        out, _ = self.run_gate(
            self.state(),
            self.closure(False, "ACTIVE_CHILD_CONTROL_NOT_TERMINAL"),
        )
        self.assertFalse(out["canonical_final_allowed"])
        self.assertEqual("ACTIVE_CHILD_CONTROL_NOT_TERMINAL", out["parent_closure"]["state"])

    def test_forged_parent_complete_terminal_event_is_rejected(self):
        with patch.object(
            authority.research_runtime_guard,
            "canonicalize_registration",
            side_effect=self.canonicalized,
        ), patch.object(
            authority.research_task_records,
            "current_records",
            side_effect=self.task_records,
        ), patch.object(
            authority.research_parent_closure,
            "derive_objective_closure",
            return_value=self.closure(False, "ACTIVE_CHILD_CONTROL_NOT_TERMINAL"),
        ):
            out = authority.apply_terminal_event(
                self.state(), "PARENT_OBJECTIVE_COMPLETE"
            )
        self.assertFalse(out["parent_terminal_event_authorized"])
        self.assertEqual("OPEN", out["parent_objective"]["status"])
        self.assertIsNone(out["terminal_scope"])
        self.assertFalse(out["final_allowed"])

    def test_derived_parent_complete_terminal_event_is_authorized(self):
        with patch.object(
            authority.research_runtime_guard,
            "canonicalize_registration",
            side_effect=self.canonicalized,
        ), patch.object(
            authority.research_task_records,
            "current_records",
            side_effect=self.task_records,
        ), patch.object(
            authority.research_parent_closure,
            "derive_objective_closure",
            return_value=self.closure(True),
        ):
            out = authority.apply_terminal_event(
                self.state(), "PARENT_OBJECTIVE_COMPLETE"
            )
        self.assertTrue(out["parent_terminal_event_authorized"])
        self.assertEqual("PARENT_OBJECTIVE", out["terminal_scope"])
        self.assertTrue(out["final_allowed"])

    def test_legacy_unbound_parent_cannot_self_declare_complete(self):
        legacy = self.state()

        def legacy_canonicalized(state, *, purpose, root):
            value = copy.deepcopy(dict(state))
            value["task_registration"] = {
                "state": "LEGACY_BASELINE_REGISTERED",
                "registry_key": None,
                "fresh_redispatch": False,
            }
            return value

        with patch.object(
            authority.research_runtime_guard,
            "canonicalize_registration",
            side_effect=legacy_canonicalized,
        ), patch.object(
            authority.research_task_records,
            "current_records",
        ) as current:
            out = authority.pre_final_gate(legacy)
        current.assert_not_called()
        self.assertFalse(out["canonical_final_allowed"])
        self.assertEqual(
            "LEGACY_PARENT_OBJECTIVE_AUTHORITY_UNBOUND",
            out["parent_closure"]["state"],
        )

    def test_explicit_user_stop_remains_interaction_boundary_with_parent_open(self):
        state = self.state(
            control={
                "user_requested_stop_pause_review_or_wait": True,
                "independent_safe_work_exhausted": True,
            }
        )
        out, _ = self.run_gate(
            state, self.closure(False, "OBJECTIVE_HEAD_NOT_CLOSED")
        )
        self.assertTrue(out["canonical_final_allowed"])
        self.assertEqual("FINAL_ALLOWED", out["transition"])
        self.assertFalse(out["parent_closure"]["derived_parent_complete"])

    def test_repository_parent_id_overrides_caller_parent_id(self):
        out, derive = self.run_gate(
            self.state(
                parent_objective={"objective_id": "OBJ-FORGED", "status": "COMPLETE"}
            ),
            self.closure(False, "OBJECTIVE_HEAD_NOT_CLOSED"),
        )
        derive.assert_called_once_with("OBJ-REAL", authority.ROOT)
        self.assertFalse(out["caller_supplied_parent_status_is_authority"])


if __name__ == "__main__":
    unittest.main()
