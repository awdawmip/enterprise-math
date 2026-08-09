import unittest
from itertools import product

from enterprise_math.causal_zad_word_distance import (
    a_word_distance,
    apply_event_program,
    d_canonical_event_program,
    d_word_distance,
    z_word_distance,
)
from enterprise_math.lattice_geometry import a_graph_distance


class CausalZADWordDistanceTests(unittest.TestCase):
    def test_z_axis_grammar_distance_is_l1(self):
        self.assertEqual(z_word_distance((0, 0, 0), (2, -3, 1)), 6)

    def test_a_transfer_grammar_distance_is_half_l1_and_existing_a_graph_distance(self):
        cases = (
            ((0, 0, 0, 0), (2, -1, 0, -1)),
            ((3, -2, -1, 0), (0, 1, -3, 2)),
        )
        for left, right in cases:
            self.assertEqual(a_word_distance(left, right), a_graph_distance(left, right))
            self.assertEqual(a_word_distance(left, right), sum(abs(a - b) for a, b in zip(left, right)) // 2)

    def test_d_closed_formula_handles_balanced_and_dominant_coordinates(self):
        self.assertEqual(d_word_distance((0, 0, 0), (1, 1, 0)), 1)
        self.assertEqual(d_word_distance((0, 0, 0), (4, 0, 0)), 4)
        self.assertEqual(d_word_distance((0, 0, 0), (3, 1, 0)), 3)
        self.assertEqual(d_word_distance((0, 0, 0, 0), (2, -2, 2, -2)), 4)

    def test_constructed_d_program_attains_formula_for_many_small_even_parity_targets(self):
        origin = (0, 0, 0, 0)
        for target in product(range(-2, 3), repeat=4):
            if sum(target) % 2:
                continue
            program = d_canonical_event_program(origin, target)
            self.assertEqual(len(program), d_word_distance(origin, target))
            self.assertEqual(apply_event_program(origin, program), target)

    def test_d_distance_rejects_different_total_parity(self):
        with self.assertRaises(ValueError):
            d_word_distance((0, 0, 0), (1, 0, 0))


if __name__ == "__main__":
    unittest.main()
