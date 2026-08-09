import unittest

from enterprise_math.causal_semantic_grade import (
    declared_costs_dominate_semantic_grades,
    distinguishing_depth_matrix,
    generator_semantic_grades,
    semantic_grade_is_componentwise_necessary,
    semantic_grade_subadditivity,
    semantic_loss_grade,
    semantic_loss_witness,
    semantic_regrading_preserves_depth_matrix,
)


class CausalSemanticGradeTests(unittest.TestCase):
    def test_declared_grades_can_contain_semantic_slack(self):
        states = (0, 1, 2, 3)
        observation = {0: 0, 1: 0, 2: 0, 3: 1}
        g = {0: 0, 1: 0, 2: 1, 3: 0}
        h = {0: 0, 1: 3, 2: 0, 3: 0}
        generators = {
            "g": g,
            "g_slow_duplicate": g,
            "h": h,
            "id": {state: state for state in states},
        }
        costs = {
            "g": 2,
            "g_slow_duplicate": 11,
            "h": 5,
            "id": 13,
        }
        semantic = generator_semantic_grades(
            states, observation, generators, costs
        )
        self.assertEqual(semantic["g"], 2)
        self.assertEqual(semantic["g_slow_duplicate"], 2)
        self.assertEqual(semantic["h"], 5)
        self.assertEqual(semantic["id"], 0)
        self.assertTrue(
            declared_costs_dominate_semantic_grades(
                states, observation, generators, costs
            )
        )

    def test_componentwise_minimal_semantic_regrading_preserves_all_pair_depths(self):
        states = (0, 1, 2, 3)
        observation = {0: 0, 1: 0, 2: 0, 3: 1}
        generators = {
            "g": {0: 0, 1: 0, 2: 1, 3: 0},
            "h": {0: 0, 1: 3, 2: 0, 3: 0},
            "id": {state: state for state in states},
        }
        costs = {"g": 2, "h": 5, "id": 9}
        self.assertTrue(
            semantic_regrading_preserves_depth_matrix(
                states, observation, generators, costs
            )
        )
        semantic = generator_semantic_grades(
            states, observation, generators, costs
        )
        self.assertEqual(semantic, {"g": 2, "h": 5, "id": 0})
        self.assertTrue(
            semantic_grade_is_componentwise_necessary(
                states,
                observation,
                generators,
                costs,
                candidate_costs=semantic,
            )
        )
        self.assertTrue(
            semantic_grade_is_componentwise_necessary(
                states,
                observation,
                generators,
                costs,
                candidate_costs={"g": 3, "h": 6, "id": 4},
            )
            is False  # Larger grades change exact depths; dominance is necessary, not sufficient.
        )

    def test_lowering_below_semantic_grade_changes_future_geometry(self):
        states = (0, 1, 2, 3)
        observation = {0: 0, 1: 0, 2: 0, 3: 1}
        generators = {
            "g": {0: 0, 1: 0, 2: 1, 3: 0},
            "h": {0: 0, 1: 3, 2: 0, 3: 0},
        }
        costs = {"g": 2, "h": 5}
        self.assertFalse(
            semantic_grade_is_componentwise_necessary(
                states,
                observation,
                generators,
                costs,
                candidate_costs={"g": 1, "h": 5},
            )
        )

    def test_positive_semantic_grade_has_exact_depth_drop_witness(self):
        states = (0, 1, 2, 3)
        observation = {0: 0, 1: 0, 2: 0, 3: 1}
        generators = {
            "g": {0: 0, 1: 0, 2: 1, 3: 0},
            "h": {0: 0, 1: 3, 2: 0, 3: 0},
        }
        costs = {"g": 2, "h": 5}
        depth = distinguishing_depth_matrix(
            states, observation, generators, costs
        )
        for label, operation in generators.items():
            grade = semantic_loss_grade(states, depth, operation)
            witness = semantic_loss_witness(states, depth, operation)
            self.assertIsNotNone(witness)
            left, right, before, after = witness
            self.assertEqual(before - after, grade)
            self.assertEqual(grade, costs[label])

    def test_semantic_loss_grade_is_subadditive_under_operation_composition(self):
        states = (0, 1, 2, 3)
        observation = {0: 0, 1: 0, 2: 0, 3: 1}
        g = {0: 0, 1: 0, 2: 1, 3: 0}
        h = {0: 0, 1: 3, 2: 0, 3: 0}
        generators = {"g": g, "h": h}
        costs = {"g": 2, "h": 5}
        depth = distinguishing_depth_matrix(
            states, observation, generators, costs
        )
        self.assertTrue(semantic_grade_subadditivity(states, depth, g, h))
        self.assertTrue(semantic_grade_subadditivity(states, depth, h, g))


if __name__ == "__main__":
    unittest.main()
