import unittest

from enterprise_math.adaptive_precision import (
    complete_observation_cost_bound,
    conflict_multiplicity,
    conflict_profile,
    joint_predicate_complete,
    optimal_target_decision_cost,
    optimal_target_first_observation,
    optimal_worst_case_decision_cost,
    predicate_conflict_fiber,
    product_conflict_bound,
    refinement_proof_gain,
)
from enterprise_math.precision_system import (
    TRUE,
    UNRESOLVED,
    predicate_fiber_certificate,
)


def scale_observation(terminal_scale, scale):
    ratio = terminal_scale // scale
    return lambda state: state // ratio


class AdaptivePrecisionTests(unittest.TestCase):
    def test_conflict_multiplicity_decreases_under_refinement(self):
        states = list(range(32))
        predicate = lambda x: x < 13
        observations = [
            scale_observation(16, scale) for scale in [1, 2, 4, 8, 16]
        ]
        for state in states:
            profile = conflict_profile(states, observations, predicate, state)
            self.assertEqual(profile, sorted(profile, reverse=True))
            self.assertEqual(profile[-1], 0)

    def test_conflict_zero_exactly_matches_predicate_certificate(self):
        states = list(range(24))
        predicate = lambda x: x % 5 in {0, 1}
        observations = [
            scale_observation(12, scale) for scale in [1, 2, 3, 6, 12]
        ]
        for observation in observations:
            for state in states:
                conflicts = conflict_multiplicity(
                    states, observation, predicate, state
                )
                certificate = predicate_fiber_certificate(
                    states, observation, predicate, state
                )
                self.assertEqual(conflicts == 0, certificate != UNRESOLVED)
                if certificate != UNRESOLVED:
                    self.assertEqual(certificate, TRUE if predicate(state) else "FALSE")

    def test_conflict_fiber_contains_only_opposite_truth_states(self):
        states = list(range(18))
        predicate = lambda x: x < 9
        observation = scale_observation(6, 2)
        for state in states:
            conflicts = predicate_conflict_fiber(
                states, observation, predicate, state
            )
            for candidate in conflicts:
                self.assertEqual(observation(candidate), observation(state))
                self.assertNotEqual(predicate(candidate), predicate(state))

    def test_raw_ambiguity_gain_can_be_proof_irrelevant(self):
        states = ["x", "t1", "t2", "t3", "f"]
        predicate = lambda s: s != "f"
        coarse = lambda _s: 0
        proof_useful = lambda s: 1 if s == "f" else 0
        ambiguity_useful = lambda s: 0 if s in {"x", "f"} else s

        proof_gain = refinement_proof_gain(
            states, coarse, proof_useful, predicate, "x"
        )
        ambiguity_gain = refinement_proof_gain(
            states, coarse, ambiguity_useful, predicate, "x"
        )

        self.assertEqual(proof_gain["ambiguity_gain"], 1)
        self.assertEqual(proof_gain["conflict_gain"], 1)
        self.assertTrue(proof_gain["decides"])

        self.assertEqual(ambiguity_gain["ambiguity_gain"], 3)
        self.assertEqual(ambiguity_gain["conflict_gain"], 0)
        self.assertFalse(ambiguity_gain["decides"])

    def test_product_precision_never_increases_predicate_conflict(self):
        states = list(range(30))
        predicate = lambda x: x % 7 < 3
        observations = [
            lambda x: x // 5,
            lambda x: x % 3,
            lambda x: (x // 2) % 2,
        ]
        for state in states:
            data = product_conflict_bound(
                states, observations, predicate, state
            )
            self.assertLessEqual(
                data["joint_conflict"], min(data["axis_conflicts"])
            )

    def test_target_state_dynamic_program_beats_raw_conflict_greedy(self):
        states = ["x", "f1", "f2", "f3"]
        predicate = lambda s: s == "x"
        coarse = lambda _s: 0
        observations = {
            "A_expensive_direct": lambda s: 0 if s == "x" else 1,
            "B_remove_12": lambda s: 0 if s in {"x", "f3"} else 1,
            "C_remove_3": lambda s: 0 if s in {"x", "f1", "f2"} else 1,
        }
        costs = {
            "A_expensive_direct": 5,
            "B_remove_12": 1,
            "C_remove_3": 1,
        }

        gains = {
            name: refinement_proof_gain(
                states, coarse, observation, predicate, "x"
            )["conflict_gain"]
            for name, observation in observations.items()
        }
        self.assertEqual(max(gains, key=gains.get), "A_expensive_direct")

        self.assertEqual(
            optimal_target_decision_cost(
                states, observations, costs, predicate, "x"
            ),
            2,
        )
        first = optimal_target_first_observation(
            states, observations, costs, predicate, "x"
        )
        self.assertIsNotNone(first)
        self.assertIn(first[0], {"B_remove_12", "C_remove_3"})
        self.assertEqual(first[1], 2)

    def test_worst_case_decision_tree_uses_integer_bellman_recurrence(self):
        states = ["x", "f1", "f2", "f3"]
        predicate = lambda s: s == "x"
        observations = {
            "A_expensive_direct": lambda s: 0 if s == "x" else 1,
            "B_remove_12": lambda s: 0 if s in {"x", "f3"} else 1,
            "C_remove_3": lambda s: 0 if s in {"x", "f1", "f2"} else 1,
        }
        costs = {
            "A_expensive_direct": 5,
            "B_remove_12": 1,
            "C_remove_3": 1,
        }
        self.assertTrue(joint_predicate_complete(states, observations, predicate))
        self.assertEqual(
            optimal_worst_case_decision_cost(
                states, observations, costs, predicate
            ),
            2,
        )
        data = complete_observation_cost_bound(
            states, observations, costs, predicate
        )
        self.assertTrue(data["joint_complete"])
        self.assertEqual(data["optimal_cost"], 2)
        self.assertLessEqual(data["optimal_cost"], data["sum_cost_bound"])

    def test_incomplete_observation_family_has_no_finite_decision_tree(self):
        states = [0, 1, 2, 3]
        predicate = lambda x: x % 2 == 0
        observations = {"coarse": lambda x: x // 2}
        costs = {"coarse": 1}
        self.assertFalse(joint_predicate_complete(states, observations, predicate))
        self.assertIsNone(
            optimal_worst_case_decision_cost(
                states, observations, costs, predicate
            )
        )
        data = complete_observation_cost_bound(
            states, observations, costs, predicate
        )
        self.assertFalse(data["joint_complete"])
        self.assertIsNone(data["optimal_cost"])


if __name__ == "__main__":
    unittest.main()
