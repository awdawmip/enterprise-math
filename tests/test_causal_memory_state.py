import unittest

from enterprise_math.causal_memory_state import (
    continuation_types_per_current,
    current_state_is_future_sufficient,
    hidden_memory_excess,
    minimal_memory_refinement,
)


class CausalMemoryStateTests(unittest.TestCase):
    def test_current_label_with_one_continuation_type_is_future_sufficient(self):
        state_to_current = {"h0": "r", "h1": "r", "h2": "s"}
        state_to_type = {"h0": "tau", "h1": "tau", "h2": "upsilon"}
        self.assertTrue(current_state_is_future_sufficient(state_to_current, state_to_type))
        self.assertEqual(hidden_memory_excess(state_to_current, state_to_type), 0)

    def test_same_current_label_can_hide_future_relevant_memory(self):
        state_to_current = {"h0": "r", "h1": "r"}
        state_to_type = {"h0": "tau0", "h1": "tau1"}
        self.assertFalse(current_state_is_future_sufficient(state_to_current, state_to_type))
        self.assertEqual(hidden_memory_excess(state_to_current, state_to_type), 1)
        self.assertEqual(
            continuation_types_per_current(state_to_current, state_to_type),
            {"r": frozenset(("tau0", "tau1"))},
        )

    def test_minimal_refinement_keeps_type_not_raw_history_identity(self):
        state_to_current = {"h0": "r", "h1": "r", "h2": "r"}
        state_to_type = {"h0": "tau0", "h1": "tau0", "h2": "tau1"}
        refined = minimal_memory_refinement(state_to_current, state_to_type)
        self.assertEqual(refined["h0"], refined["h1"])
        self.assertNotEqual(refined["h0"], refined["h2"])
        self.assertEqual(len(set(refined.values())), 2)

    def test_dimension_contraction_total_only_can_be_memory_free_or_not_by_future_language(self):
        # Fine lifts of one unit into two slots: (1,0) and (0,1).
        states = ("10", "01")
        state_to_current = {state: 1 for state in states}  # coarse total only

        # If all future observations are symmetric total-only, the two lifts have
        # one continuation type and the contraction is future-sufficient.
        symmetric_types = {state: "same-total-future" for state in states}
        self.assertTrue(current_state_is_future_sufficient(state_to_current, symmetric_types))

        # If a later causal operation/observation distinguishes which slot carried
        # the unit, the same coarse total hides two continuation types.
        slot_sensitive_types = {"10": "left-unit", "01": "right-unit"}
        self.assertFalse(current_state_is_future_sufficient(state_to_current, slot_sensitive_types))
        self.assertEqual(hidden_memory_excess(state_to_current, slot_sensitive_types), 1)


if __name__ == "__main__":
    unittest.main()
