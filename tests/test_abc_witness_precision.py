import unittest

from enterprise_math.abc_witness_precision import (
    additive_relation_vector,
    bounded_nondegenerate_witnesses,
    is_additive_witness,
    is_nondegenerate_witness,
    minimal_witness_cost,
    primitive_kernel_signature_complete,
    same_radical_state_witness_precision_counterexample,
    witness_coordinates,
    witness_flag,
    wronskian_relation_vector,
)


class AbcWitnessPrecisionTests(unittest.TestCase):
    def test_relation_vectors_for_123(self) -> None:
        self.assertEqual(witness_coordinates(1, 2, 3), (2, 3))
        self.assertEqual(additive_relation_vector(1, 2, 3), (1, -1))
        self.assertEqual(wronskian_relation_vector(1, 2, 3), (1, 0))
        self.assertTrue(is_additive_witness(1, 2, 3, (1, 1)))
        self.assertTrue(is_nondegenerate_witness(1, 2, 3, (1, 1)))
        self.assertEqual(minimal_witness_cost(1, 2, 3), 1)

    def test_relation_vectors_for_189(self) -> None:
        self.assertEqual(witness_coordinates(1, 8, 9), (2, 3))
        self.assertEqual(additive_relation_vector(1, 8, 9), (2, -1))
        self.assertEqual(wronskian_relation_vector(1, 8, 9), (1, 0))
        self.assertTrue(is_additive_witness(1, 8, 9, (1, 2)))
        self.assertTrue(is_nondegenerate_witness(1, 8, 9, (1, 2)))
        self.assertEqual(minimal_witness_cost(1, 8, 9), 2)

    def test_same_radical_state_has_different_witness_precision(self) -> None:
        data = same_radical_state_witness_precision_counterexample()
        self.assertEqual(data["radical_state"], (1, 2, 3))
        self.assertEqual(data["additive_normals"], ((1, -1), (2, -1)))
        self.assertEqual(data["minimum_witness_costs"], (1, 2))

    def test_bounded_witness_family_is_monotone(self) -> None:
        radius_1 = set(bounded_nondegenerate_witnesses(1, 2, 3, 1))
        radius_2 = set(bounded_nondegenerate_witnesses(1, 2, 3, 2))
        self.assertTrue(radius_1)
        self.assertTrue(radius_1.issubset(radius_2))

    def test_flag_ranks(self) -> None:
        data = witness_flag(5, 27, 32)
        self.assertEqual(data["coordinates"], (2, 3, 5))
        self.assertEqual(data["rank_ambient"], 3)
        self.assertEqual(data["rank_additive_kernel"], 2)
        self.assertEqual(minimal_witness_cost(5, 27, 32, max_bound=4), 3)

    def test_primitive_signature_for_scaled_normals(self) -> None:
        self.assertTrue(primitive_kernel_signature_complete((2, -2), (-7, 7)))
        self.assertFalse(primitive_kernel_signature_complete((1, -1), (2, -1)))

    def test_enumeration_guard(self) -> None:
        with self.assertRaises(ValueError):
            bounded_nondegenerate_witnesses(5, 27, 32, 100, state_cap=1000)


if __name__ == "__main__":
    unittest.main()
