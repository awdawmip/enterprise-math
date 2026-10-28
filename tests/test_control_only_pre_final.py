"""Non-task control PRE_FINAL uses liveness without granting research authority."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

from tools import research_runtime_guard as guard


ROOT = Path(__file__).resolve().parents[1]
ROLES = ("CONTROL_PLANE_MAINTENANCE", "RESEARCH_DRIVER", "FOUNDATION_STEWARD")
BOOLEAN_FIELDS = (
    "parent_objective_complete", "user_requested_stop_pause_review_or_wait",
    "parent_hard_blocker", "platform_or_tool_hard_limit", "independent_safe_work_exhausted",
    "same_action_repeated_without_state_change", "supported_alternative_available",
    "parent_state_recomputed_without_change",
)


class ControlOnlyPreFinalTests(unittest.TestCase):
    def state(self, mode=ROLES[0], *, complete=False, next_actions=1):
        liveness = {name: False for name in BOOLEAN_FIELDS}
        liveness.update(parent_objective_complete=complete,
                        executable_next_actions=next_actions, continuation_lease_active=True)
        return {
            "research_mode": mode,
            "parent_objective": {"status": "COMPLETE" if complete else "OPEN"},
            "current_subflow": {"status": "COMPLETE"},
            "parent_liveness": liveness,
        }

    def test_open_parent_continues_for_all_control_roles_without_mutation(self):
        for mode in ROLES:
            with self.subTest(mode=mode):
                state = self.state(mode)
                before = copy.deepcopy(state)
                result = guard.pre_final_gate(state)
                self.assertEqual(state, before)
                self.assertFalse(result["final_allowed"])
                self.assertEqual(result["required_action"], "EXECUTE_SELECTED_NEXT_ACTION_NOW")
                self.assertTrue(result["parent_liveness"]["continuation_lease_preserved"])
                self.assertFalse(result["authorized"])
                self.assertEqual(result["authorization_authority"], "CONTROL_ONLY_PRE_FINAL_NO_TASK_AUTHORITY")
                self.assertNotIn("task_registration", result)
                self.assertNotIn("activity_allowed", result)

    def test_explicit_mode_alias_uses_the_same_control_route(self):
        state = self.state()
        state["mode"] = state.pop("research_mode")
        self.assertFalse(guard.pre_final_gate(state)["final_allowed"])

    def test_completed_standalone_control_objective_can_report_without_authorization(self):
        # This self-contained fixture finishes its own small control objective;
        # it does not mark the owner's ongoing research objective complete.
        state = self.state(complete=True, next_actions=0)
        state["parent_objective"]["description"] = "Repair the sole typo in a local control fixture"
        result = guard.pre_final_gate(state)
        self.assertTrue(result["final_allowed"])
        self.assertEqual(result["required_action"], "RETURN_FINAL")
        self.assertFalse(result["authorized"])
        self.assertFalse(result["parent_liveness"]["continuation_lease_preserved"])

    def test_completed_parent_with_executable_work_fails_closed_and_keeps_lease(self):
        result = guard.pre_final_gate(self.state(complete=True, next_actions=1))
        self.assertFalse(result["final_allowed"])
        self.assertEqual(result["parent_liveness"]["transition"], "CONTROL_STATE_INCONSISTENT")
        self.assertEqual(result["required_action"], "REBUILD_CONTROL_STATE_FROM_AUTHORITATIVE_PARENT_OBJECTIVE")
        self.assertTrue(result["parent_liveness"]["continuation_lease_preserved"])

    def test_missing_parent_liveness_requests_evaluation(self):
        for state in ({"research_mode": ROLES[0]}, {"research_mode": ROLES[0], "parent_liveness": None}):
            with self.subTest(state=state):
                result = guard.pre_final_gate(state)
                self.assertFalse(result["final_allowed"])
                self.assertFalse(result["authorized"])
                self.assertEqual(result["required_action"], "EVALUATE_PARENT_LIVENESS")

    def test_nonobject_or_empty_liveness_is_rejected(self):
        for value in ([], "", False, 0, {}):
            with self.subTest(value=value):
                state = self.state()
                state["parent_liveness"] = value
                with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "control-only PRE_FINAL"):
                    guard.pre_final_gate(state)

    def test_all_required_booleans_are_present_and_strict(self):
        for field in BOOLEAN_FIELDS:
            state = self.state()
            del state["parent_liveness"][field]
            with self.subTest(field=field, missing=True):
                with self.assertRaisesRegex(guard.RuntimeAuthorizationError, field):
                    guard.pre_final_gate(state)
            for value in (0, 1, "false", None):
                with self.subTest(field=field, value=value):
                    state = self.state()
                    state["parent_liveness"][field] = value
                    with self.assertRaisesRegex(guard.RuntimeAuthorizationError, field):
                        guard.pre_final_gate(state)

    def test_count_and_optional_lease_keep_primitive_types(self):
        for field, values in (("executable_next_actions", (True, -1, 1.0, "1", None)),
                              ("continuation_lease_active", (0, "true", None))):
            for value in values:
                with self.subTest(field=field, value=value):
                    state = self.state()
                    state["parent_liveness"][field] = value
                    with self.assertRaisesRegex(guard.RuntimeAuthorizationError, field):
                        guard.pre_final_gate(state)

    def test_control_label_cannot_hide_any_formal_binding_even_when_empty(self):
        for field in ("task", "task_id", "publication_id", "task_registration", "owner_claim",
                      "claim_id", "execution_scope", "execution_binding", "execution_record_id",
                      "execution_cohort_id", "execution_lane_id"):
            for value in (None, {}, ""):
                with self.subTest(field=field, value=value):
                    state = self.state(complete=True, next_actions=0)
                    state[field] = value
                    with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "task must be an object|task.task_id is required"):
                        guard.pre_final_gate(state)

    def test_noncontrol_and_free_still_require_research_activity(self):
        for mode in ("FREE_AXIOM_DISCOVERY", "TASK_RESEARCH", "UNRECOGNIZED", None):
            with self.subTest(mode=mode):
                state = self.state(mode, complete=True, next_actions=0)
                result = guard.pre_final_gate(state)
                self.assertFalse(result["final_allowed"])
                self.assertFalse(result["activity_allowed"])
                self.assertEqual(result["required_action"], "REGISTER_RESEARCH_ACTIVITY")

    def test_control_label_cannot_bypass_activity_bindings_but_session_id_is_allowed(self):
        state = self.state(complete=True, next_actions=0)
        state["session_id"] = "control-session-fixture"
        result = guard.pre_final_gate(state)
        self.assertTrue(result["final_allowed"])
        self.assertFalse(result["authorized"])
        for key in ("activity_id", "activity_registration_source", "research_checkpoint_event_id"):
            for value in (None, "", {}, "unverified-activity-binding"):
                with self.subTest(key=key, value=value):
                    mixed = copy.deepcopy(state)
                    mixed[key] = value
                    with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "task must be an object"):
                        guard.pre_final_gate(mixed)

    def test_control_pre_final_does_not_enable_execution_or_task_terminal_events(self):
        for mode in ROLES:
            with self.subTest(mode=mode):
                state = self.state(mode, complete=True, next_actions=0)
                with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "task must be an object"):
                    guard.authorize_execution(state, events=[])
                with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "task must be an object"):
                    guard.apply_terminal_event(state, "PARENT_OBJECTIVE_COMPLETE")

    def test_direct_and_module_cli_exit_codes_follow_actual_liveness(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp).joinpath("state.json")
            for complete, next_actions, expected in ((False, 1, 2), (True, 0, 0)):
                state = self.state(complete=complete, next_actions=next_actions)
                path.write_text(json.dumps(state), encoding="utf-8")
                for entry in ([str(ROOT.joinpath("tools/research_runtime_guard.py"))],
                              ["-m", "tools.research_runtime_guard"]):
                    with self.subTest(complete=complete, entry=entry):
                        run = subprocess.run([sys.executable, "-B", "-X", "utf8", *entry,
                            "pre-final", "--state-file", str(path)], cwd=ROOT,
                            capture_output=True, text=True, encoding="utf-8", timeout=30)
                        self.assertEqual(run.returncode, expected, run.stderr + run.stdout)
                        result = json.loads(run.stdout)
                        self.assertEqual(result["final_allowed"], complete)
                        self.assertFalse(result["authorized"])


if __name__ == "__main__":
    unittest.main()
