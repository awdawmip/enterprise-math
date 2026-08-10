import unittest
from collections import Counter
from fractions import Fraction

from enterprise_math.r004_local_window_presampling import (
    cycle_period_symbols,
    cyclic_window_counts,
    decompose_stationary_block_counts,
    minimum_uniform_window_width_exceeding_atom_budget,
    periodic_cycle_mixture_block_law,
    reduced_stationary_window_counts,
    stationary_block_counts_balanced,
    stationary_rational_window_presampling_certificate,
    stationary_window_atom_rank_bounds,
    uniform_full_support_window_rank,
)


class R004LocalWindowPresamplingTests(unittest.TestCase):
    def test_width_one_rational_marginal_is_static_finite_presampling(self):
        counts = {("a",): 2, ("b",): 1}
        cycles, law = stationary_rational_window_presampling_certificate(counts)
        self.assertEqual(sum(len(cycle) for cycle in cycles), 3)
        self.assertEqual(
            law,
            {("a",): Fraction(2, 3), ("b",): Fraction(1, 3)},
        )
        self.assertEqual(stationary_window_atom_rank_bounds(counts), (2, 3))

    def test_uniform_binary_pair_law_has_exact_four_atom_rank(self):
        counts = {
            (0, 0): 1,
            (0, 1): 1,
            (1, 0): 1,
            (1, 1): 1,
        }
        self.assertTrue(stationary_block_counts_balanced(counts))
        cycles, law = stationary_rational_window_presampling_certificate(counts)
        self.assertEqual(sum(len(cycle) for cycle in cycles), 4)
        self.assertEqual(set(law.values()), {Fraction(1, 4)})
        self.assertEqual(set(law), set(counts))
        self.assertEqual(stationary_window_atom_rank_bounds(counts), (4, 4))
        self.assertEqual(uniform_full_support_window_rank(2, 2), 4)

    def test_common_count_scale_is_removed_before_certificate_construction(self):
        doubled_uniform = {
            (0, 0): 2,
            (0, 1): 2,
            (1, 0): 2,
            (1, 1): 2,
        }
        self.assertEqual(
            reduced_stationary_window_counts(doubled_uniform),
            {block: 1 for block in doubled_uniform},
        )
        cycles, law = stationary_rational_window_presampling_certificate(doubled_uniform)
        self.assertEqual(sum(len(cycle) for cycle in cycles), 4)
        self.assertEqual(set(law.values()), {Fraction(1, 4)})
        self.assertEqual(stationary_window_atom_rank_bounds(doubled_uniform), (4, 4))

    def test_nonuniform_stationary_pair_law_is_reproduced_exactly(self):
        counts = {
            (0, 0): 2,
            (0, 1): 1,
            (1, 0): 1,
        }
        cycles, law = stationary_rational_window_presampling_certificate(counts)
        self.assertEqual(
            law,
            {
                (0, 0): Fraction(1, 2),
                (0, 1): Fraction(1, 4),
                (1, 0): Fraction(1, 4),
            },
        )
        reconstructed = Counter(block for cycle in cycles for block in cycle)
        self.assertEqual(reconstructed, Counter(counts))
        self.assertEqual(stationary_window_atom_rank_bounds(counts), (3, 4))

    def test_periodic_word_gives_stationary_triple_cycle_certificate(self):
        period = (0, 0, 1, 1)
        counts = cyclic_window_counts(period, 3)
        self.assertEqual(
            counts,
            {(0, 0, 1): 1, (0, 1, 1): 1, (1, 1, 0): 1, (1, 0, 0): 1},
        )
        self.assertTrue(stationary_block_counts_balanced(counts))
        cycles = decompose_stationary_block_counts(counts)
        self.assertEqual(
            periodic_cycle_mixture_block_law(cycles),
            {block: Fraction(1, 4) for block in counts},
        )
        for cycle in cycles:
            recovered_period = cycle_period_symbols(cycle)
            self.assertEqual(
                sum(cyclic_window_counts(recovered_period, 3).values()),
                len(cycle),
            )

    def test_cycle_mixture_reconstructs_aggregated_periodic_sources(self):
        source_periods = ((0,), (0, 1), (0, 0, 1, 1))
        aggregate = Counter()
        for period in source_periods:
            aggregate.update(cyclic_window_counts(period, 2))
        self.assertTrue(stationary_block_counts_balanced(aggregate))
        _, law = stationary_rational_window_presampling_certificate(aggregate)
        reduced = reduced_stationary_window_counts(aggregate)
        total = sum(reduced.values())
        self.assertEqual(
            law,
            {block: Fraction(count, total) for block, count in reduced.items()},
        )

    def test_unbalanced_local_law_is_rejected(self):
        counts = {(0, 1): 1}
        self.assertFalse(stationary_block_counts_balanced(counts))
        with self.assertRaisesRegex(ValueError, "stationary prefix/suffix balance"):
            decompose_stationary_block_counts(counts)
        with self.assertRaisesRegex(ValueError, "stationary prefix/suffix balance"):
            stationary_window_atom_rank_bounds(counts)

    def test_input_validation_fails_closed(self):
        with self.assertRaises(ValueError):
            stationary_block_counts_balanced({})
        with self.assertRaises(ValueError):
            stationary_block_counts_balanced({(0,): 1, (0, 1): 1})
        with self.assertRaises(ValueError):
            stationary_block_counts_balanced({(0,): -1})
        with self.assertRaises(ValueError):
            uniform_full_support_window_rank(0, 2)
        with self.assertRaises(ValueError):
            uniform_full_support_window_rank(2, 0)
        with self.assertRaises(ValueError):
            minimum_uniform_window_width_exceeding_atom_budget(0, 10)
        with self.assertRaises(ValueError):
            minimum_uniform_window_width_exceeding_atom_budget(2, -1)

    def test_uniform_rank_formula_is_exact_integer_resource_level(self):
        for alphabet_size in range(1, 5):
            for width in range(1, 6):
                self.assertEqual(
                    uniform_full_support_window_rank(alphabet_size, width),
                    alphabet_size**width,
                )

    def test_window_width_inverts_a_declared_finite_atom_budget(self):
        self.assertEqual(minimum_uniform_window_width_exceeding_atom_budget(2, 0), 1)
        self.assertEqual(minimum_uniform_window_width_exceeding_atom_budget(2, 1), 1)
        self.assertEqual(minimum_uniform_window_width_exceeding_atom_budget(2, 2), 2)
        self.assertEqual(minimum_uniform_window_width_exceeding_atom_budget(2, 3), 2)
        self.assertEqual(minimum_uniform_window_width_exceeding_atom_budget(2, 4), 3)
        self.assertEqual(minimum_uniform_window_width_exceeding_atom_budget(3, 8), 2)
        self.assertEqual(minimum_uniform_window_width_exceeding_atom_budget(3, 9), 3)
        self.assertIsNone(minimum_uniform_window_width_exceeding_atom_budget(1, 1))


if __name__ == "__main__":
    unittest.main()
