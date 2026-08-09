import unittest

from enterprise_math.causal_basin_state import linear_growth, square_growth
from enterprise_math.causal_collapse_composition import (
    addition_congruence_defects,
    collapse_is_addition_congruence_on_sample,
    representative_level_operation_is_associative,
    safety_profile,
)


class CausalCollapseCompositionTests(unittest.TestCase):
    def test_linear_block_growth_passes_representative_associativity_but_fails_fiber_congruence(self):
        growth = linear_growth(5, 30)
        self.assertTrue(representative_level_operation_is_associative(growth, tuple(range(8))))
        self.assertFalse(collapse_is_addition_congruence_on_sample(growth, 12))
        defects = addition_congruence_defects(growth, 12)
        self.assertIn((0, 4, 1, 1), defects)
        self.assertEqual(safety_profile(growth, tuple(range(8)), 12), (True, False))

    def test_square_growth_can_fail_even_complete_representative_associativity(self):
        growth = square_growth(40)
        self.assertFalse(representative_level_operation_is_associative(growth, (3, 4)))
        self.assertFalse(collapse_is_addition_congruence_on_sample(growth, 20))
        self.assertEqual(safety_profile(growth, (3, 4), 20), (False, False))

    def test_identity_growth_has_no_detail_and_is_true_addition_congruence(self):
        growth = tuple(range(80))
        self.assertTrue(representative_level_operation_is_associative(growth, tuple(range(10))))
        self.assertTrue(collapse_is_addition_congruence_on_sample(growth, 20))
        self.assertEqual(safety_profile(growth, tuple(range(10)), 20), (True, True))

    def test_detail_free_identity_is_the_only_trivial_sample_with_no_collision(self):
        growth = tuple(range(50))
        self.assertEqual(addition_congruence_defects(growth, 15), ())


if __name__ == "__main__":
    unittest.main()
