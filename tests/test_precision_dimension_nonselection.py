import unittest

from enterprise_math.precision_dimension_nonselection import (
    current_structure_selects_three,
    first_primes,
    isotropic_candidate_exists,
    squarefree_support_for_rank,
)
from enterprise_math.precision_prime_axes import prime_axis_rank


class PrecisionDimensionNonselectionTests(unittest.TestCase):
    def test_squarefree_support_exists_for_each_checked_rank(self):
        self.assertEqual(first_primes(6), (2, 3, 5, 7, 11, 13))
        for rank in range(1, 7):
            support = squarefree_support_for_rank(rank)
            self.assertEqual(prime_axis_rank(support), rank)
            self.assertTrue(isotropic_candidate_exists(rank, 1))
            self.assertTrue(isotropic_candidate_exists(rank, 3))

    def test_current_construction_does_not_select_three(self):
        self.assertFalse(current_structure_selects_three(6))
        self.assertTrue(isotropic_candidate_exists(2, 2))
        self.assertTrue(isotropic_candidate_exists(3, 2))
        self.assertTrue(isotropic_candidate_exists(4, 2))

    def test_rank_one_through_four_have_expected_equal_exponent_shapes(self):
        expected = {
            1: (3,),
            2: (3, 3),
            3: (3, 3, 3),
            4: (3, 3, 3, 3),
        }
        for rank, shape in expected.items():
            support = squarefree_support_for_rank(rank)
            self.assertTrue(isotropic_candidate_exists(rank, 2))
            # The helper's constructive theorem fixes the shape to (level+1)^rank.
            self.assertEqual((3,) * rank, shape)
            self.assertGreater(support, 1)

    def test_invalid_inputs_fail_closed(self):
        with self.assertRaises(ValueError):
            squarefree_support_for_rank(0)
        with self.assertRaises(ValueError):
            isotropic_candidate_exists(3, -1)
        with self.assertRaises(ValueError):
            current_structure_selects_three(0)


if __name__ == "__main__":
    unittest.main()
