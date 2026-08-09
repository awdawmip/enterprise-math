import unittest

from enterprise_math.precision_partition_margin import (
    binary_margin_identity,
    block_margin,
    dyadic_margin_levels,
    partition_margin_identity,
)


class PrecisionPartitionMarginTests(unittest.TestCase):
    def test_block_margin_is_off_diagonal_sum(self):
        x = (-1, 0, 2, 1)
        y = (1, -1, 0, 3)
        data = block_margin(x, y)
        direct = sum(x[i] * y[j] for i in range(len(x)) for j in range(len(y)) if i != j)
        self.assertEqual(data["D"], direct)

    def test_binary_exact_transport(self):
        data = binary_margin_identity(
            (-1, 2),
            (1, 0),
            (0, 1),
            (-1, 3),
        )
        self.assertEqual(
            data["parent_margin"],
            data["left_margin"]
            + data["right_margin"]
            + data["left_to_right"]
            + data["right_to_left"],
        )

    def test_arbitrary_partition_identity(self):
        data = partition_margin_identity(
            ((-1, 0), (2,), (1, -2, 3)),
            ((1, -1), (0,), (2, 1, -1)),
        )
        self.assertEqual(
            data["parent_margin"],
            data["child_margin_sum"] + data["cross_compensation"],
        )

    def test_prime_free_positive_cone_has_nonnegative_merge_compensation(self):
        # The MC08 prime-free cone corresponds to nonnegative child X and Y.
        left_x, left_y = (0, 1, 2), (1, 0, 1)
        right_x, right_y = (3, 0), (0, 2)
        data = binary_margin_identity(left_x, left_y, right_x, right_y)
        self.assertGreaterEqual(data["left_to_right"], 0)
        self.assertGreaterEqual(data["right_to_left"], 0)
        self.assertGreaterEqual(data["cross_compensation"], 0)
        self.assertGreaterEqual(data["parent_margin"], data["child_margin_sum"])

    def test_signed_cross_compensation_can_mask_fine_negative_margin(self):
        # A negative fine margin can be hidden at the coarser parent by a
        # positive sibling compensation term.  This is the exact algebraic
        # mechanism behind proof resolution under precision refinement.
        data = binary_margin_identity(
            (-1,),
            (2,),
            (3,),
            (-1,),
        )
        self.assertEqual(data["left_margin"], 0)
        self.assertEqual(data["right_margin"], 0)
        self.assertEqual(data["cross_compensation"], 7)
        self.assertEqual(data["parent_margin"], 7)

    def test_dyadic_shells_telescope_to_singletons(self):
        x = (-1, 0, 2, 1, -1, 3, 0)
        y = (1, -1, 0, 3, 2, 0, -1)
        data = dyadic_margin_levels(x, y)
        self.assertEqual(data["level_margin_sums"][-1], 0)
        self.assertEqual(data["level_margin_sums"][0], sum(data["shell_budgets"]))
        for coarse, fine, shell in zip(
            data["level_margin_sums"],
            data["level_margin_sums"][1:],
            data["shell_budgets"],
        ):
            self.assertEqual(coarse, fine + shell)

    def test_empty_and_singleton_boundaries(self):
        self.assertEqual(block_margin((), ())["D"], 0)
        self.assertEqual(dyadic_margin_levels((), ())["level_margin_sums"], (0,))
        self.assertEqual(dyadic_margin_levels((3,), (-2,))["level_margin_sums"], (0,))

    def test_validation(self):
        with self.assertRaises(ValueError):
            block_margin((1, 2), (1,))
        with self.assertRaises(ValueError):
            block_margin((True,), (1,))
        with self.assertRaises(ValueError):
            partition_margin_identity(((1,),), ((1,), (2,)))


if __name__ == "__main__":
    unittest.main()
