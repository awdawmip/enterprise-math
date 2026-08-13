import unittest

from tools.check_r052_finite_refinement import (
    half_cycle,
    is_half_involution,
    naturality,
    unique_order_two_power,
    compose_refinements,
    check_s3_witnesses,
)


class R052FiniteRefinementTests(unittest.TestCase):
    def test_even_cycles_have_unique_half_involution(self):
        for m in (4, 6, 8, 10, 12):
            self.assertTrue(is_half_involution(m))
            self.assertTrue(unique_order_two_power(m))

    def test_odd_cycles_reject_half_role(self):
        for m in (3, 5, 7, 9):
            with self.assertRaises(ValueError):
                half_cycle(m, 0)

    def test_uniform_refinement_naturality(self):
        for m in (4, 6, 8):
            for factor in (2, 3, 4, 5):
                self.assertTrue(naturality(m, factor))

    def test_refinement_composition(self):
        for m in (4, 6):
            self.assertTrue(compose_refinements(m, 2, 3))
            self.assertTrue(compose_refinements(m, 3, 5))

    def test_s3_deletion_witnesses_and_astar_exhaustion(self):
        evidence = check_s3_witnesses()
        self.assertTrue(all(evidence["M1_moves_base"].values()))
        self.assertTrue(all(evidence["M2_vertical_fixed"].values()))
        for row in evidence["A_star_small_fiber_exhaustion"].values():
            self.assertEqual(row["fixed_point_free_vertical_involutions"], 1)
            self.assertEqual(row["fixed_point_free_equal_deck"], 1)


if __name__ == "__main__":
    unittest.main()
