import unittest

from enterprise_math.abc_block_pareto_profile import (
    compressed_and_fine_frontiers_agree_on_reference_examples,
    exact_block_pareto_profile,
    frontier_cardinality_bound_holds,
    minimum_absorption_at_radius,
)


class AbcBlockParetoProfileTests(unittest.TestCase):
    def test_235_strict_drop_profile(self) -> None:
        data = exact_block_pareto_profile(2, 3, 5)
        self.assertEqual((data.mu, data.nu, data.eta_min), (1, 2, 1))
        self.assertEqual(
            tuple((point.radius, point.minimum_absorption) for point in data.profile),
            ((1, 2), (2, 1)),
        )
        self.assertEqual(data.frontier, ((1, 2), (2, 1)))

    def test_279_three_level_frontier(self) -> None:
        data = exact_block_pareto_profile(2, 7, 9)
        self.assertEqual((data.mu, data.nu, data.eta_min), (1, 5, 1))
        self.assertEqual(
            tuple((point.radius, point.minimum_absorption) for point in data.profile),
            ((1, 3), (2, 3), (3, 3), (4, 2), (5, 1)),
        )
        self.assertEqual(data.frontier, ((1, 3), (4, 2), (5, 1)))

    def test_irreducible_absorption_overhead_frontier(self) -> None:
        data = exact_block_pareto_profile(5, 7, 12)
        self.assertEqual((data.mu, data.nu, data.eta_min), (1, 2, 2))
        self.assertEqual(data.frontier, ((1, 6), (2, 2)))

    def test_squarefree_access_delay_frontier(self) -> None:
        data = exact_block_pareto_profile(1, 22, 23)
        self.assertEqual((data.mu, data.nu, data.eta_min), (2, 5, 1))
        self.assertEqual(
            tuple((point.radius, point.minimum_absorption) for point in data.profile),
            ((2, 2), (3, 2), (4, 2), (5, 1)),
        )
        self.assertEqual(data.frontier, ((2, 2), (5, 1)))

    def test_singleton_frontiers(self) -> None:
        first = exact_block_pareto_profile(25, 704, 729)
        self.assertEqual((first.mu, first.nu, first.eta_min), (6, 6, 6))
        self.assertEqual(first.frontier, ((6, 6),))

        second = exact_block_pareto_profile(1, 512, 513)
        self.assertEqual((second.mu, second.nu, second.eta_min), (13, 13, 3))
        self.assertEqual(second.frontier, ((13, 3),))

    def test_absorption_is_undefined_before_mu(self) -> None:
        self.assertIsNone(minimum_absorption_at_radius(1, 8, 9, 1))
        self.assertEqual(minimum_absorption_at_radius(1, 8, 9, 2), 1)

    def test_reference_fine_and_compressed_frontiers_agree(self) -> None:
        self.assertTrue(compressed_and_fine_frontiers_agree_on_reference_examples())

    def test_frontier_cardinality_bounds(self) -> None:
        for triple in (
            (2, 3, 5),
            (2, 7, 9),
            (5, 7, 12),
            (1, 22, 23),
            (25, 704, 729),
            (1, 512, 513),
        ):
            self.assertTrue(frontier_cardinality_bound_holds(*triple))


if __name__ == "__main__":
    unittest.main()
