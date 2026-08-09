import unittest

from enterprise_math.abc_block_row_universality import (
    primitive_block_row,
    primitive_positive_rows_are_exact_block_row_class,
    realize_primitive_block_row,
)


class AbcBlockRowUniversalityTests(unittest.TestCase):
    def test_two_variable_row_is_realized_exactly(self) -> None:
        data = realize_primitive_block_row((5, 2), (2, 3))
        self.assertEqual(data.exponents, (10, 6))
        self.assertEqual(data.normalized_coefficients, (30, 12))
        self.assertEqual(data.block_content, 6)
        self.assertEqual(data.primitive_block_row, (5, 2))
        self.assertEqual(primitive_block_row(data.integer_block), (5, 2))

    def test_stage17_counterexample_rows_are_actual_block_rows(self) -> None:
        rows = (
            (2, 4, 5, 11),
            (2, 5, 7, 8),
            (2, 5, 6, 9),
        )
        primes = (2, 3, 5, 7)
        for row in rows:
            self.assertTrue(primitive_positive_rows_are_exact_block_row_class(row, primes))

    def test_three_coordinate_access_row_is_realizable(self) -> None:
        data = realize_primitive_block_row((15, 10, 6), (2, 3, 5))
        self.assertEqual(data.primitive_block_row, (15, 10, 6))
        self.assertEqual(data.exponents, (30, 30, 30))

    def test_single_coordinate_class_is_included(self) -> None:
        data = realize_primitive_block_row((1,), (2,))
        self.assertEqual(data.exponents, (2,))
        self.assertEqual(data.primitive_block_row, (1,))

    def test_nonprimitive_row_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            realize_primitive_block_row((2, 4), (2, 3))

    def test_prime_labels_must_be_distinct_and_canonical(self) -> None:
        with self.assertRaises(ValueError):
            realize_primitive_block_row((1, 2), (2, 2))
        with self.assertRaises(ValueError):
            realize_primitive_block_row((1, 2), (3, 2))
        with self.assertRaises(ValueError):
            realize_primitive_block_row((1, 2), (2, 4))


if __name__ == "__main__":
    unittest.main()
