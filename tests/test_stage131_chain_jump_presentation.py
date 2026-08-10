import itertools
import unittest

from enterprise_math.stage131_chain_jump_presentation import (
    adjacent_jump_lengths,
    best_two_jump_presentation,
    binary_chain_closure_rounds_closed,
    binary_jump_lengths,
    binary_jump_rule_count_closed,
    canonical_chain_presentation_points,
    chain_jump_closure_rounds,
    chain_jump_rule_count,
    chain_presentation_point,
    closure_sequence_matches_coin_rounds,
    exact_chain_jump_pareto_frontier,
    full_transitive_jump_lengths,
    geometric_jump_lengths,
    geometric_jump_rule_count_closed,
    minimum_jump_rounds_by_distance,
    point_dominates,
    synchronous_chain_closure_sequence,
    two_jump_closure_rounds_closed,
)


class Stage131ChainJumpPresentationTests(unittest.TestCase):
    def test_adjacent_and_full_transitive_endpoints(self):
        for n in range(1, 40):
            adjacent = chain_presentation_point(n, adjacent_jump_lengths(n))
            self.assertEqual(adjacent.stored_rules, n)
            self.assertEqual(adjacent.full_closure_rounds, n)

            full = chain_presentation_point(n, full_transitive_jump_lengths(n))
            self.assertEqual(full.stored_rules, n * (n + 1) // 2)
            self.assertEqual(full.full_closure_rounds, 1)

    def test_coin_count_equals_synchronous_first_derivation_round(self):
        for n in range(1, 9):
            optional = tuple(range(2, n + 1))
            for mask in range(1 << len(optional)):
                lengths = (1,) + tuple(
                    optional[index]
                    for index in range(len(optional))
                    if (mask >> index) & 1
                )
                self.assertTrue(closure_sequence_matches_coin_rounds(n, lengths))

    def test_binary_closed_storage_and_depth_formulas(self):
        for n in range(1, 1000):
            lengths = binary_jump_lengths(n)
            self.assertEqual(
                chain_jump_rule_count(n, lengths),
                binary_jump_rule_count_closed(n),
            )
            self.assertEqual(
                chain_jump_closure_rounds(n, lengths),
                binary_chain_closure_rounds_closed(n),
            )

    def test_binary_rounds_equal_popcount_distance_formula(self):
        for n in range(1, 200):
            rounds = minimum_jump_rounds_by_distance(n, binary_jump_lengths(n))
            self.assertEqual(
                rounds,
                tuple(value.bit_count() for value in range(n + 1)),
            )

    def test_geometric_rule_count_closed_form(self):
        for n in range(2, 100):
            for base in range(2, 8):
                lengths = geometric_jump_lengths(n, base)
                self.assertEqual(
                    chain_jump_rule_count(n, lengths),
                    geometric_jump_rule_count_closed(n, base),
                )

    def test_geometric_power_chain_has_digit_sum_depth(self):
        # For n=b^m, every t<n has at most m base-b digits and the worst digit
        # sum is attained by b^m-1: m*(b-1).
        for base in range(2, 7):
            for exponent in range(1, 6):
                n = base**exponent
                self.assertEqual(
                    chain_jump_closure_rounds(n, geometric_jump_lengths(n, base)),
                    exponent * (base - 1),
                )

    def test_two_jump_closed_depth_formula(self):
        for n in range(2, 100):
            for jump in range(2, n + 1):
                self.assertEqual(
                    chain_jump_closure_rounds(n, (1, jump)),
                    two_jump_closure_rounds_closed(n, jump),
                )

    def test_binary_is_not_generically_pareto_optimal(self):
        # The smallest sharp boundary: long jump3 costs only one positional rule.
        binary = chain_presentation_point(3, (1, 2))
        better = chain_presentation_point(3, (1, 3))
        self.assertEqual((binary.stored_rules, binary.full_closure_rounds), (5, 2))
        self.assertEqual((better.stored_rules, better.full_closure_rounds), (4, 2))
        self.assertTrue(point_dominates(better, binary))

    def test_small_chain_exact_pareto_storage_depth_pairs(self):
        expected = {
            3: ((3, 3), (4, 2), (6, 1)),
            4: ((4, 4), (5, 3), (6, 2), (10, 1)),
            6: ((6, 6), (7, 5), (8, 4), (9, 3), (12, 2), (21, 1)),
            8: ((8, 8), (9, 7), (10, 6), (11, 5), (12, 4), (15, 3), (19, 2), (36, 1)),
        }
        for n, pairs in expected.items():
            frontier = exact_chain_jump_pareto_frontier(n)
            actual_pairs = tuple(
                sorted({(point.stored_rules, point.full_closure_rounds) for point in frontier})
            )
            self.assertEqual(actual_pairs, pairs)
            for point in frontier:
                self.assertFalse(
                    any(
                        point_dominates(other, point)
                        for other in frontier
                        if other != point
                    )
                )

    def test_chain_1024_resource_landscape(self):
        n = 1024
        canonical = canonical_chain_presentation_points(n)
        self.assertEqual(
            (canonical["adjacent"].stored_rules, canonical["adjacent"].full_closure_rounds),
            (1024, 1024),
        )
        self.assertEqual(
            (canonical["binary"].stored_rules, canonical["binary"].full_closure_rounds),
            (9228, 10),
        )
        self.assertEqual(
            (canonical["full"].stored_rules, canonical["full"].full_closure_rounds),
            (524800, 1),
        )

        best_two = best_two_jump_presentation(n)
        self.assertEqual(best_two.jump_lengths, (1, 38))
        self.assertEqual((best_two.stored_rules, best_two.full_closure_rounds), (2011, 62))

        base3 = chain_presentation_point(n, geometric_jump_lengths(n, 3))
        self.assertEqual((base3.stored_rules, base3.full_closure_rounds), (6082, 12))

        # These are different exact resource points, not a claim that every one
        # lies on the globally optimal frontier over arbitrary jump sets.
        self.assertLess(best_two.stored_rules, base3.stored_rules)
        self.assertGreater(best_two.full_closure_rounds, base3.full_closure_rounds)
        self.assertLess(base3.stored_rules, canonical["binary"].stored_rules)
        self.assertGreater(base3.full_closure_rounds, canonical["binary"].full_closure_rounds)

    def test_closure_sequence_binary_nine(self):
        sequence = synchronous_chain_closure_sequence(9, binary_jump_lengths(9))
        self.assertEqual(len(sequence) - 1, binary_chain_closure_rounds_closed(9))
        self.assertEqual(sequence[-1], frozenset(range(10)))

    def test_validation(self):
        with self.assertRaises(ValueError):
            chain_presentation_point(5, (2, 3))
        with self.assertRaises(ValueError):
            geometric_jump_lengths(5, 1)
        with self.assertRaises(ValueError):
            exact_chain_jump_pareto_frontier(21)


if __name__ == "__main__":
    unittest.main()
