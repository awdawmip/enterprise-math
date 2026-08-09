import unittest

from enterprise_math.causal_weighted_transition_refinement import (
    compile_weighted_transition_system,
    induced_weighted_transitions,
    stable_weighted_transition_types,
)


def binary_suffix_transitions(width, increment):
    states = tuple(
        tuple((value >> shift) & 1 for shift in reversed(range(width)))
        for value in range(2**width)
    )
    transitions = {}
    for symbol in (0, 1):
        transitions[symbol] = {
            state: (state[1:] + (symbol,), increment(state, symbol))
            for state in states
        }
    return states, transitions


class CausalWeightedTransitionRefinementTests(unittest.TestCase):
    def test_zero_grade_collapses_all_raw_suffix_memory(self):
        states, transitions = binary_suffix_transitions(3, lambda state, symbol: 0)
        observations = {state: 0 for state in states}
        classes, induced, _ = compile_weighted_transition_system(observations, transitions)
        self.assertEqual(len(set(classes.values())), 1)
        self.assertEqual(induced[0], {0: (0, 0)})
        self.assertEqual(induced[1], {0: (0, 0)})

    def test_three_window_raw_memory_can_reduce_to_last_symbol_only(self):
        # Raw state stores two prior symbols (four states), but the local grade
        # only reads the most recent symbol and the newly appended symbol.
        states, transitions = binary_suffix_transitions(
            2,
            lambda state, symbol: 3 if state[-1] == symbol else -1,
        )
        observations = {state: 0 for state in states}
        classes, induced, _ = compile_weighted_transition_system(observations, transitions)
        self.assertEqual(len(set(classes.values())), 2)
        for left in states:
            for right in states:
                self.assertEqual(
                    classes[left] == classes[right],
                    left[-1] == right[-1],
                )
        # The induced state is exact for both append actions and grade increments.
        self.assertEqual(set(induced), {0, 1})

    def test_genuine_three_window_grade_can_need_all_four_suffix_states(self):
        states, transitions = binary_suffix_transitions(
            2,
            lambda state, symbol: 5 if state[0] == symbol else (2 if state[1] == symbol else -3),
        )
        observations = {state: 0 for state in states}
        classes, _, _ = compile_weighted_transition_system(observations, transitions)
        self.assertEqual(len(set(classes.values())), 4)

    def test_manual_overcollapse_is_rejected(self):
        states, transitions = binary_suffix_transitions(
            1,
            lambda state, symbol: 1 if state[-1] == symbol else 0,
        )
        observations = {state: 0 for state in states}
        manual = {state: 0 for state in states}
        with self.assertRaises(ValueError):
            induced_weighted_transitions(observations, transitions, manual)
        stable, _ = stable_weighted_transition_types(observations, transitions)
        self.assertEqual(len(set(stable.values())), 2)


if __name__ == "__main__":
    unittest.main()
