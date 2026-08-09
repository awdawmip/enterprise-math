import unittest

from enterprise_math.future_quotient import (
    ambiguity_multiplicities,
    class_count,
    composition_horizon,
    future_partition_sequence,
)


class FutureQuotientTests(unittest.TestCase):
    def test_future_distinctions_appear_only_when_required(self):
        states = ("a", "b", "c", "d", "e", "f")
        observations = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 1,
            "f": 0,
        }
        transitions = {
            "step": {
                "a": "c",
                "b": "d",
                "c": "e",
                "d": "f",
                "e": "e",
                "f": "f",
            }
        }
        sequence = future_partition_sequence(states, observations, transitions)
        counts = [class_count(partition) for partition in sequence]
        self.assertEqual(counts, sorted(counts))
        self.assertGreater(counts[-1], counts[0])

        # c and d are indistinguishable now but distinguishable one step ahead.
        self.assertEqual(sequence[0][2], sequence[0][3])
        self.assertNotEqual(sequence[1][2], sequence[1][3])

        # a and b need one additional lookahead step.
        self.assertEqual(sequence[1][0], sequence[1][1])
        self.assertNotEqual(sequence[2][0], sequence[2][1])
        self.assertEqual(composition_horizon(states, observations, transitions), 2)

    def test_ambiguity_multiplicity_never_increases_under_refinement(self):
        states = (0, 1, 2, 3, 4)
        observations = {0: 0, 1: 0, 2: 0, 3: 0, 4: 1}
        transitions = {
            "a": {0: 1, 1: 2, 2: 3, 3: 4, 4: 4},
            "b": {0: 0, 1: 1, 2: 4, 3: 3, 4: 4},
        }
        sequence = future_partition_sequence(states, observations, transitions)
        ambiguities = [ambiguity_multiplicities(partition) for partition in sequence]
        for earlier, later in zip(ambiguities, ambiguities[1:]):
            for old, new in zip(earlier, later):
                self.assertLessEqual(new, old)

    def test_stable_partition_is_closed_under_actions(self):
        states = (0, 1, 2, 3)
        observations = {0: 0, 1: 0, 2: 1, 3: 1}
        transitions = {
            "flip": {0: 2, 1: 3, 2: 0, 3: 1},
            "stay": {0: 0, 1: 1, 2: 2, 3: 3},
        }
        stable = future_partition_sequence(states, observations, transitions)[-1]
        index = {state: position for position, state in enumerate(states)}
        for left in states:
            for right in states:
                if stable[index[left]] != stable[index[right]]:
                    continue
                for transition in transitions.values():
                    self.assertEqual(
                        stable[index[transition[left]]],
                        stable[index[transition[right]]],
                    )


if __name__ == "__main__":
    unittest.main()
