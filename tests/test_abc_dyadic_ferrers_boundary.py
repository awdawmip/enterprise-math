import unittest
from fractions import Fraction

from enterprise_math.abc_dyadic_ferrers_boundary import (
    boundary_word_from_node_ranks,
    crossings_from_node_ranks,
    ferrers_boundary_from_staircase,
    node_ranks_from_boundary_word,
    node_ranks_from_crossings,
)
from enterprise_math.abc_dyadic_threshold_staircase import dyadic_threshold_staircase


class DyadicFerrersBoundaryTests(unittest.TestCase):
    def setUp(self) -> None:
        self.staircase = dyadic_threshold_staircase(
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

    def test_crossings_and_node_ranks_are_exact_duals(self) -> None:
        ranks = node_ranks_from_crossings(3, (0, 1, 2, None))
        self.assertEqual(ranks, (1, 2, 3, 3))
        self.assertEqual(crossings_from_node_ranks(ranks, 4), (0, 1, 2, None))

    def test_boundary_word_encodes_same_state(self) -> None:
        ranks = (1, 2, 3, 3)
        word = boundary_word_from_node_ranks(ranks, 4)
        self.assertEqual(word, "VHVHVHHV")
        self.assertEqual(node_ranks_from_boundary_word(word, 3, 4), ranks)

    def test_ferrers_area_has_two_exact_sums(self) -> None:
        boundary = ferrers_boundary_from_staircase(self.staircase)
        self.assertEqual(boundary.node_ranks, (1, 2, 3, 3))
        self.assertEqual(boundary.crossing_depths, (0, 1, 2, None))
        self.assertEqual(boundary.rank_area, 9)
        self.assertEqual(boundary.crossing_area, 9)
        self.assertEqual(boundary.activation_area, 9)
        self.assertEqual(boundary.complement_area, 7)
        self.assertTrue(boundary.duality_verified)
        self.assertTrue(boundary.area_identity_verified)

    def test_plateau_staircase_has_flat_rank_jump_geometry(self) -> None:
        staircase = dyadic_threshold_staircase(
            3,
            41,
            2,
            3,
            (
                Fraction(1, 2),
                Fraction(1, 1),
                Fraction(10, 1),
                Fraction(11, 1),
            ),
        )
        boundary = ferrers_boundary_from_staircase(staircase)
        self.assertEqual(boundary.crossing_depths, (1, 2, 2, None))
        self.assertEqual(boundary.node_ranks, (0, 1, 3, 3))
        self.assertEqual(boundary.activation_area, 7)

    def test_all_inactive_and_all_active_boundaries(self) -> None:
        inactive_ranks = node_ranks_from_crossings(2, (None, None))
        self.assertEqual(inactive_ranks, (0, 0, 0))
        self.assertEqual(boundary_word_from_node_ranks(inactive_ranks, 2), "HHHVV")

        active_ranks = node_ranks_from_crossings(2, (0, 0))
        self.assertEqual(active_ranks, (2, 2, 2))
        self.assertEqual(boundary_word_from_node_ranks(active_ranks, 2), "VVHHH")

    def test_rejects_nonmonotone_rank_sequence(self) -> None:
        with self.assertRaises(ValueError):
            crossings_from_node_ranks((0, 2, 1), 2)


if __name__ == "__main__":
    unittest.main()
