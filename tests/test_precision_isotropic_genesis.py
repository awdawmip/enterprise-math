import unittest
from fractions import Fraction

from enterprise_math.precision_isotropic_genesis import (
    genesis_rank_jump,
    isotropic_genesis_signature,
    isotropic_zero_overlap_sequence,
    same_rank_supports_same_unlabeled_geometry,
)


class PrecisionIsotropicGenesisTests(unittest.TestCase):
    def test_equal_rank_supports_have_equal_unlabeled_geometry(self):
        for level in range(1, 5):
            self.assertTrue(same_rank_supports_same_unlabeled_geometry(30, 42, level))
            self.assertTrue(same_rank_supports_same_unlabeled_geometry(30, 105, level))
        self.assertFalse(same_rank_supports_same_unlabeled_geometry(30, 6, 2))

    def test_three_axis_signature_and_record_sequence_are_exact(self):
        signature = isotropic_genesis_signature(30, 3)
        self.assertEqual(signature.dimension, 3)
        self.assertEqual(signature.shape, (4, 4, 4))
        self.assertEqual(signature.vertex_count, 64)
        self.assertEqual(signature.edge_count, 144)
        self.assertEqual(signature.diameter, 9)
        expected = (
            Fraction(0, 1),
            Fraction(4, 7),
            Fraction(11, 13),
            Fraction(13, 14),
            Fraction(149, 155),
        )
        self.assertEqual(isotropic_zero_overlap_sequence(30, 4, 2), expected)
        self.assertEqual(isotropic_zero_overlap_sequence(42, 4, 2), expected)

    def test_rank_jump_depends_on_support_size_not_prime_labels(self):
        self.assertEqual(genesis_rank_jump(6), 2)
        self.assertEqual(genesis_rank_jump(30), 3)
        self.assertEqual(genesis_rank_jump(42), 3)
        self.assertEqual(genesis_rank_jump(210), 4)

    def test_non_squarefree_support_fails_closed(self):
        with self.assertRaises(ValueError):
            isotropic_genesis_signature(12, 2)


if __name__ == "__main__":
    unittest.main()
