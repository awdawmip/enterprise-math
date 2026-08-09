import unittest

from enterprise_math.lego_dimension_kernel import (
    apply_dimension_kernel,
    dimension_kernel_roundtrip,
    recover_dimension_kernel,
)
from enterprise_math.lego_dimension_ladder import allocation_row


class LegoDimensionKernelTests(unittest.TestCase):
    def test_free_dimension_step_has_all_one_kernel(self):
        lower = allocation_row(3, 8)
        free_kernel = tuple(1 for _ in range(9))
        raised = apply_dimension_kernel(lower, free_kernel)
        self.assertEqual(raised, allocation_row(4, 8))
        self.assertEqual(recover_dimension_kernel(lower, raised), free_kernel)

    def test_support_hole_in_new_block_is_recovered_exactly(self):
        lower = allocation_row(2, 7)
        kernel = (1, 1, 0, 1, 0, 1, 1, 0)
        raised = apply_dimension_kernel(lower, kernel)
        self.assertEqual(recover_dimension_kernel(lower, raised), kernel)
        self.assertTrue(dimension_kernel_roundtrip(lower, kernel))

    def test_split_multiplicity_in_new_block_is_recovered_exactly(self):
        lower = allocation_row(2, 6)
        kernel = (1, 1, 2, 1, 3, 0, 1)
        raised = apply_dimension_kernel(lower, kernel)
        self.assertEqual(recover_dimension_kernel(lower, raised), kernel)

    def test_signed_kernel_is_algebraically_recoverable_but_not_automatically_a_multiplicity(self):
        lower = allocation_row(2, 5)
        kernel = (1, -1, 2, 0, 1, -3)
        raised = apply_dimension_kernel(lower, kernel)
        self.assertEqual(recover_dimension_kernel(lower, raised), kernel)


if __name__ == "__main__":
    unittest.main()
