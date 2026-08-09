import unittest

from enterprise_math.causal_basin_state import linear_growth, square_growth
from enterprise_math.causal_basin_translation import (
    has_wide_basin_obstruction,
    quotient_translation_safe_on_represented_sample,
    translation_separation_witness,
    witness_really_separates_after_translation,
)
from enterprise_math.lattice_geometry import a_ball_count
from enterprise_math.lego_partition_fiber import hidden_allocation_multiplicity


class CausalBasinTranslationTests(unittest.TestCase):
    def test_square_growth_has_a_separation_witness_for_every_tested_positive_increment(self):
        growth = square_growth(80)
        for increment in range(1, 20):
            witness = translation_separation_witness(growth, increment)
            self.assertIsNotNone(witness)
            self.assertTrue(witness_really_separates_after_translation(growth, increment, witness))
            self.assertTrue(has_wide_basin_obstruction(growth, increment))

    def test_linear_growth_only_has_wide_basin_obstruction_below_block_width(self):
        growth = linear_growth(5, 80)
        for increment in range(1, 5):
            self.assertTrue(has_wide_basin_obstruction(growth, increment))
        self.assertIsNone(translation_separation_witness(growth, 5))
        self.assertFalse(has_wide_basin_obstruction(growth, 5))
        self.assertTrue(quotient_translation_safe_on_represented_sample(growth, 5, 100))
        self.assertFalse(quotient_translation_safe_on_represented_sample(growth, 6, 100))

    def test_free_lego_degree_two_or_more_eventually_blocks_every_fixed_increment(self):
        # slots>=3 -> H_m has degree >=2 and widths H_(m-1)(c+1) are unbounded.
        for slots in range(3, 7):
            growth = tuple(hidden_allocation_multiplicity(slots, total) for total in range(80))
            for increment in range(1, 12):
                self.assertTrue(has_wide_basin_obstruction(growth, increment))

    def test_a_p_ball_growth_for_p_at_least_two_has_wide_basin_obstruction(self):
        for p in range(2, 5):
            growth = tuple(a_ball_count(p, radius) for radius in range(50))
            for increment in range(1, 15):
                self.assertTrue(has_wide_basin_obstruction(growth, increment))

    def test_a1_linear_ball_growth_has_only_even_safe_translations(self):
        growth = tuple(a_ball_count(1, radius) for radius in range(80))
        # V_1(r)=2r+1, constant basin width 2.
        self.assertTrue(has_wide_basin_obstruction(growth, 1))
        self.assertFalse(has_wide_basin_obstruction(growth, 2))
        self.assertTrue(quotient_translation_safe_on_represented_sample(growth, 2, 100))
        self.assertFalse(quotient_translation_safe_on_represented_sample(growth, 3, 100))


if __name__ == "__main__":
    unittest.main()
