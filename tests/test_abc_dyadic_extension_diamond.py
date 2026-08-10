import unittest
from fractions import Fraction

from enterprise_math.abc_dyadic_extension_diamond import (
    biaxial_extension_diamond,
    pareto_representations,
    representation_cost_vectors,
)
from enterprise_math.abc_dyadic_threshold_staircase import dyadic_threshold_staircase


class DyadicExtensionDiamondTests(unittest.TestCase):
    def test_threshold_and_orbit_extensions_commute(self) -> None:
        old = dyadic_threshold_staircase(
            3,
            41,
            2,
            3,
            (
                Fraction(1, 22),
                Fraction(1, 2),
                Fraction(1),
                Fraction(11),
            ),
        )
        diamond = biaxial_extension_diamond(old, Fraction(10))
        self.assertTrue(diamond.diamond_commutes)
        self.assertEqual(diamond.threshold_then_orbit_symbols, ("V", "H"))
        self.assertEqual(diamond.orbit_then_threshold_symbols, ("H", "V"))
        self.assertEqual(
            diamond.final_word_threshold_then_orbit,
            diamond.final_word_orbit_then_threshold,
        )
        self.assertEqual(diamond.final_crossings[:4], (0, 1, 2, 2))

    def test_nontrivial_grid_has_three_nondominated_charts(self) -> None:
        vectors = representation_cost_vectors(3, 4)
        self.assertEqual(
            [
                (
                    vector.representation,
                    vector.storage_coordinates,
                    vector.threshold_extension_worst_case_writes,
                    vector.orbit_extension_worst_case_writes,
                )
                for vector in vectors
            ],
            [
                ("crossings", 4, 1, 4),
                ("ranks", 4, 4, 1),
                ("boundary", 8, 1, 1),
            ],
        )
        self.assertEqual(
            set(pareto_representations(3, 4)),
            {"crossings", "ranks", "boundary"},
        )

    def test_one_threshold_degeneracy_makes_crossings_dominate(self) -> None:
        self.assertEqual(pareto_representations(5, 1), ("crossings",))
        vectors = representation_cost_vectors(5, 1)
        crossing = vectors[0]
        self.assertEqual(
            (
                crossing.storage_coordinates,
                crossing.threshold_extension_worst_case_writes,
                crossing.orbit_extension_worst_case_writes,
            ),
            (1, 1, 1),
        )

    def test_one_node_degeneracy_makes_ranks_dominate(self) -> None:
        self.assertEqual(pareto_representations(0, 5), ("ranks",))
        vectors = representation_cost_vectors(0, 5)
        rank = vectors[1]
        self.assertEqual(
            (
                rank.storage_coordinates,
                rank.threshold_extension_worst_case_writes,
                rank.orbit_extension_worst_case_writes,
            ),
            (1, 1, 1),
        )

    def test_two_by_two_is_first_full_pareto_grid(self) -> None:
        # h=1 means two orbit nodes, s=2 means two thresholds.
        self.assertEqual(
            set(pareto_representations(1, 2)),
            {"crossings", "ranks", "boundary"},
        )


if __name__ == "__main__":
    unittest.main()
