import unittest

from enterprise_math.causal_hidden_motion import (
    basis_coordinates,
    hidden_motion_basis,
    hidden_motion_rank,
    is_zero_sum_motion,
    reconstruct_motion,
    same_total_difference,
)
from enterprise_math.causal_dimension_agreement import free_slot_fiber_growth_degree


class CausalHiddenMotionTests(unittest.TestCase):
    def test_explicit_zero_sum_basis_has_m_minus_one_generators(self):
        for slots in range(1, 8):
            basis = hidden_motion_basis(slots)
            self.assertEqual(len(basis), slots - 1)
            self.assertEqual(hidden_motion_rank(slots), slots - 1)
            self.assertTrue(all(is_zero_sum_motion(vector) for vector in basis))

    def test_every_zero_sum_vector_has_exact_integer_basis_coordinates(self):
        examples = (
            (0,),
            (3, -3),
            (2, -5, 3),
            (-4, 1, 0, 3),
            (7, -2, 5, -10, 0),
        )
        for vector in examples:
            coordinates = basis_coordinates(vector)
            self.assertEqual(reconstruct_motion(coordinates), vector)

    def test_same_total_fine_states_differ_only_by_hidden_motion(self):
        left = (4, 1, 0, 3)
        right = (0, 2, 5, 1)
        difference = same_total_difference(left, right)
        self.assertEqual(difference, (4, -1, -5, 2))
        self.assertTrue(is_zero_sum_motion(difference))
        self.assertEqual(reconstruct_motion(basis_coordinates(difference)), difference)

    def test_hidden_motion_rank_equals_fiber_growth_degree_in_free_regime(self):
        for slots in range(1, 7):
            self.assertEqual(
                hidden_motion_rank(slots),
                free_slot_fiber_growth_degree(slots),
            )


if __name__ == "__main__":
    unittest.main()
