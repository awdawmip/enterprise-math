import unittest

from enterprise_math.causal_relation_boundary import (
    enumerated_directed_cut_counts,
    lower_a_ball_count,
    per_direction_cut_formula,
    relation_boundary_matches_lower_dimension,
    total_directed_cut_formula,
)
from enterprise_math.lattice_geometry import a_ball_count, a_coordinator_shell_count


class CausalRelationBoundaryTests(unittest.TestCase):
    def test_each_directed_root_sees_one_lower_dimensional_ball(self):
        for p in range(1, 4):
            for radius in range(0, 3):
                self.assertTrue(relation_boundary_matches_lower_dimension(p, radius))
                counts = enumerated_directed_cut_counts(p, radius)
                self.assertEqual(set(counts.values()), {per_direction_cut_formula(p, radius)})

    def test_total_relation_boundary_has_local_direction_factor(self):
        for p in range(1, 5):
            for radius in range(0, 5):
                expected_lower = lower_a_ball_count(p - 1, radius)
                self.assertEqual(
                    total_directed_cut_formula(p, radius),
                    p * (p + 1) * expected_lower,
                )

    def test_state_shell_and_relation_boundary_are_different_observations(self):
        # In A_3, state shell is 10r^2+2 for r>=1, while relation cut is
        # 12 * A_2-ball = 12*(3r^2+3r+1).  They are not the same boundary.
        p = 3
        radius = 2
        state_shell = a_coordinator_shell_count(p, radius)
        relation_cut = total_directed_cut_formula(p, radius)
        self.assertNotEqual(state_shell, relation_cut)
        self.assertEqual(
            relation_cut,
            12 * a_ball_count(2, radius),
        )

    def test_a1_relation_boundary_is_two_end_relations(self):
        for radius in range(0, 6):
            self.assertEqual(total_directed_cut_formula(1, radius), 2)


if __name__ == "__main__":
    unittest.main()
