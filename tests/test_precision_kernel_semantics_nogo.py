import unittest

from enterprise_math.precision_kernel_semantics_nogo import (
    add_mod_four,
    kernel_semantics_nogo_holds,
    multiply_mod_four,
    operation_descends_through_parity,
    parity_addition_table,
    parity_multiplication_table,
    parity_partition,
)


class PrecisionKernelSemanticsNogoTests(unittest.TestCase):
    def test_same_parity_kernel_supports_different_descended_operations(self):
        self.assertEqual(parity_partition(), frozenset({frozenset({0, 2}), frozenset({1, 3})}))
        self.assertTrue(operation_descends_through_parity(add_mod_four))
        self.assertTrue(operation_descends_through_parity(multiply_mod_four))
        self.assertEqual(parity_addition_table(), ((0, 1), (1, 0)))
        self.assertEqual(parity_multiplication_table(), ((0, 0), (0, 1)))
        self.assertNotEqual(parity_addition_table(), parity_multiplication_table())
        self.assertTrue(kernel_semantics_nogo_holds())

    def test_kernel_partition_alone_does_not_encode_required_operation_family(self):
        # Both languages use exactly the same quotient carrier and equality
        # partition; only the typed future operation requirement distinguishes
        # which quotient table must be emitted.
        quotient = parity_partition()
        self.assertEqual(quotient, parity_partition())
        tables = {parity_addition_table(), parity_multiplication_table()}
        self.assertEqual(len(tables), 2)


if __name__ == "__main__":
    unittest.main()
