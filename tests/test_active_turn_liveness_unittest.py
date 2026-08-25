import unittest
from itertools import product

from tools import active_turn_liveness as liveness


def base_state(**overrides):
    state = {
        "parent_objective_complete": False,
        "user_requested_stop_pause_review_or_wait": False,
        "parent_hard_blocker": False,
        "platform_or_tool_hard_limit": False,
        "independent_safe_work_exhausted": False,
        "same_action_repeated_without_state_change": False,
        "supported_alternative_available": False,
        "parent_state_recomputed_without_change": False,
        "executable_next_actions": 0,
        "continuation_lease_active": False,
    }
    state.update(overrides)
    return state


class ActiveTurnPreFinalUnittest(unittest.TestCase):
    def test_open_parent_with_action_never_allows_final(self):
        decision = liveness.evaluate(base_state(executable_next_actions=1))
        self.assertEqual(decision["transition"], liveness.EXECUTE_NEXT_ACTION)
        self.assertFalse(decision["final_allowed"])

    def test_user_stop_allows_final_even_if_more_actions_exist(self):
        decision = liveness.evaluate(
            base_state(
                user_requested_stop_pause_review_or_wait=True,
                executable_next_actions=3,
                continuation_lease_active=True,
            )
        )
        self.assertEqual(decision["transition"], liveness.FINAL_ALLOWED)
        self.assertTrue(decision["final_allowed"])

    def test_true_blocker_requires_safe_work_exhaustion(self):
        open_decision = liveness.evaluate(
            base_state(parent_hard_blocker=True, independent_safe_work_exhausted=False)
        )
        self.assertFalse(open_decision["final_allowed"])
        closed_decision = liveness.evaluate(
            base_state(parent_hard_blocker=True, independent_safe_work_exhausted=True)
        )
        self.assertEqual(closed_decision["transition"], liveness.FINAL_ALLOWED_WITH_BLOCKER)
        self.assertTrue(closed_decision["final_allowed"])

    def test_no_progress_loop_switches_or_recomputes_instead_of_final(self):
        switched = liveness.evaluate(
            base_state(
                executable_next_actions=1,
                same_action_repeated_without_state_change=True,
                supported_alternative_available=True,
            )
        )
        self.assertEqual(switched["transition"], liveness.SWITCH_STRATEGY)
        self.assertFalse(switched["final_allowed"])
        recompute = liveness.evaluate(
            base_state(
                executable_next_actions=1,
                same_action_repeated_without_state_change=True,
                supported_alternative_available=False,
            )
        )
        self.assertEqual(recompute["transition"], liveness.RECOMPUTE_PARENT_STATE)
        self.assertFalse(recompute["final_allowed"])

    def test_exhaustive_open_parent_with_executable_action_forbids_final(self):
        bool_keys = [
            "parent_hard_blocker",
            "platform_or_tool_hard_limit",
            "independent_safe_work_exhausted",
            "same_action_repeated_without_state_change",
            "supported_alternative_available",
            "parent_state_recomputed_without_change",
            "continuation_lease_active",
        ]
        for bits in product((False, True), repeat=len(bool_keys)):
            overrides = dict(zip(bool_keys, bits, strict=True))
            with self.subTest(**overrides):
                decision = liveness.evaluate(
                    base_state(executable_next_actions=1, **overrides)
                )
                self.assertFalse(decision["final_allowed"])


if __name__ == "__main__":
    unittest.main()
