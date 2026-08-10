import unittest

from enterprise_math.precision_arithmetic_cut_compiler import (
    equal_weight_minimal_cuts,
    is_dissociated,
    minimal_nondissociated_supports,
    powers_of_two_weights,
    retained_signature,
    signed_relation_witness,
)
from enterprise_math.precision_structural_obstruction_basis import minimal_transversals


class ArithmeticCutCompilerTests(unittest.TestCase):
    def test_one_two_three_has_one_minimal_signed_dependency(self):
        weights = (1, 2, 3)
        cuts = minimal_nondissociated_supports(weights)
        self.assertEqual(cuts, (frozenset({0, 1, 2}),))
        witness = signed_relation_witness(weights, cuts[0])
        self.assertIsNotNone(witness)
        self.assertEqual(sum(e * w for e, w in zip(witness, weights)), 0)

    def test_equal_weights_give_complete_graph_cut_clutter(self):
        d = 4
        weights = (1,) * d
        cuts = minimal_nondissociated_supports(weights)
        self.assertEqual(set(cuts), set(equal_weight_minimal_cuts(d)))
        bases = minimal_transversals(tuple(range(d)), cuts)
        self.assertEqual({len(b) for b in bases}, {d - 1})
        self.assertEqual(len(bases), d)

    def test_powers_of_two_are_dissociated(self):
        weights = powers_of_two_weights(6)
        self.assertTrue(is_dissociated(weights))
        self.assertEqual(minimal_nondissociated_supports(weights), tuple())

    def test_retained_signature_exposes_retained_bits(self):
        weights = (1, 2, 3)
        x = (1, 0, 1)
        y = (0, 1, 1)
        # Both have weighted observation 4, but retaining coordinate 0 separates them.
        self.assertEqual(retained_signature(x, weights, []), retained_signature(y, weights, []))
        self.assertNotEqual(retained_signature(x, weights, [0]), retained_signature(y, weights, [0]))

    def test_zero_weight_is_rejected_for_flip_recovery(self):
        with self.assertRaises(ValueError):
            is_dissociated((1, 0, 2))


if __name__ == "__main__":
    unittest.main()
