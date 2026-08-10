import unittest
from fractions import Fraction

from enterprise_math.abc_dyadic_boundary_update import (
    orbit_axis_extension,
    threshold_axis_extension,
)
from enterprise_math.abc_dyadic_threshold_staircase import dyadic_threshold_staircase


class DyadicBoundaryUpdateTests(unittest.TestCase):
    def test_threshold_extension_is_one_crossing_write_and_one_V_insertion(self) -> None:
        old = dyadic_threshold_staircase(
            3,
            41,
            2,
            3,
            (
                Fraction(1, 22),
                Fraction(1, 2),
                Fraction(1, 1),
                Fraction(11, 1),
            ),
        )
        update = threshold_axis_extension(old, Fraction(10, 1))
        self.assertEqual(update.new_crossings, (0, 1, 2, 2, None))
        self.assertEqual(update.old_ranks, (1, 2, 3, 3))
        self.assertEqual(update.new_ranks, (1, 2, 4, 4))
        self.assertEqual(update.crossing_coordinate_write_count, 1)
        self.assertEqual(update.rank_coordinate_write_count, 2)
        self.assertEqual(update.inserted_boundary_symbol, "V")
        self.assertTrue(update.boundary_single_insertion_verified)
        self.assertEqual(update.old_boundary_word, "VHVHVHHV")
        self.assertEqual(update.new_boundary_word, "VHVHVVHHV")

    def test_low_threshold_can_rewrite_every_existing_rank(self) -> None:
        old = dyadic_threshold_staircase(
            3,
            41,
            2,
            3,
            (Fraction(1, 2), Fraction(1), Fraction(11)),
        )
        update = threshold_axis_extension(old, Fraction(1, 100))
        self.assertEqual(update.crossing_coordinate_write_count, 1)
        self.assertEqual(update.rank_coordinate_write_count, 4)
        self.assertTrue(update.boundary_single_insertion_verified)

    def test_orbit_extension_is_one_rank_write_and_one_H_insertion(self) -> None:
        # rho_{2,-}=1/6 and rho_{4,-}=13/6 for (q,p)=(7,17).
        # Three thresholds are unreached at depth zero and all three are reached
        # by the appended node, so crossing coordinates require three rewrites.
        old = dyadic_threshold_staircase(
            7,
            17,
            2,
            0,
            (Fraction(1, 2), Fraction(1), Fraction(2)),
        )
        self.assertEqual(old.crossing_depths, (None, None, None))
        update = orbit_axis_extension(old)
        self.assertEqual(update.new_crossings, (1, 1, 1))
        self.assertEqual(update.old_ranks, (0,))
        self.assertEqual(update.new_ranks, (0, 3))
        self.assertEqual(update.crossing_coordinate_write_count, 3)
        self.assertEqual(update.rank_coordinate_write_count, 1)
        self.assertEqual(update.inserted_boundary_symbol, "H")
        self.assertTrue(update.boundary_single_insertion_verified)
        self.assertEqual(update.old_boundary_word, "HVVV")
        self.assertEqual(update.new_boundary_word, "HVVVH")

    def test_orbit_extension_may_leave_crossings_unchanged(self) -> None:
        old = dyadic_threshold_staircase(
            3,
            41,
            2,
            3,
            (Fraction(1, 22), Fraction(1, 2), Fraction(1)),
        )
        update = orbit_axis_extension(old)
        self.assertEqual(update.crossing_coordinate_write_count, 0)
        self.assertEqual(update.rank_coordinate_write_count, 1)
        self.assertTrue(update.boundary_single_insertion_verified)

    def test_boundary_word_is_symmetric_under_both_axis_extensions(self) -> None:
        old = dyadic_threshold_staircase(
            3,
            41,
            2,
            3,
            (Fraction(1, 2), Fraction(1), Fraction(11)),
        )
        threshold_update = threshold_axis_extension(old, Fraction(10))
        orbit_update = orbit_axis_extension(old)
        self.assertEqual(threshold_update.inserted_boundary_symbol, "V")
        self.assertEqual(orbit_update.inserted_boundary_symbol, "H")
        self.assertTrue(threshold_update.boundary_single_insertion_verified)
        self.assertTrue(orbit_update.boundary_single_insertion_verified)


if __name__ == "__main__":
    unittest.main()
