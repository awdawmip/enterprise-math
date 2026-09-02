import unittest

from enterprise_math.exact_arithmetic import (
    add_divisions,
    brc_decimal_readout,
    brc_evaluate_division,
    brc_integer_value,
    brc_is_integral,
    brc_scaled_evaluate,
    compare_divisions,
    decimal_scale,
    division,
    multiply_divisions,
)


class ExactArithmeticBRCRuntimeTests(unittest.TestCase):
    def test_division_travels_unevaluated(self) -> None:
        expr = division(10, 3)
        self.assertEqual(expr.numerator, 10)
        self.assertEqual(expr.denominator, 3)

    def test_structural_state_is_not_auto_reduced(self) -> None:
        self.assertNotEqual(division(2, 4), division(1, 2))
        self.assertEqual(compare_divisions(division(2, 4), division(1, 2)), 0)

    def test_addition_and_multiplication_carry_division(self) -> None:
        left = division(1, 3)
        right = division(2, 5)
        self.assertEqual(add_divisions(left, right), division(11, 15))
        self.assertEqual(multiply_divisions(left, right), division(2, 15))

    def test_materialization_emits_brc_trace(self) -> None:
        trace = brc_evaluate_division(division(10, 3))
        self.assertEqual(trace.evaluation_kind, "BRC_DIVISION_EVALUATION")
        self.assertEqual(trace.quotient, 3)
        self.assertEqual(trace.remainder, 1)
        self.assertEqual(trace.collapsed_numerator, 9)
        self.assertEqual(trace.reconstruct(), 10)

    def test_divisibility_decision_is_brc_gated(self) -> None:
        integral, trace = brc_is_integral(division(12, 3))
        self.assertTrue(integral)
        self.assertEqual(trace.quotient, 4)
        nonintegral, trace2 = brc_is_integral(division(13, 3))
        self.assertFalse(nonintegral)
        self.assertEqual(trace2.remainder, 1)

    def test_integer_materialization_is_brc_gated(self) -> None:
        value, trace = brc_integer_value(division(84, 7))
        self.assertEqual(value, 12)
        self.assertEqual(trace.evaluation_kind, "BRC_DIVISION_EVALUATION")
        with self.assertRaises(ValueError):
            brc_integer_value(division(85, 7))

    def test_decimal_readout_descends_from_brc(self) -> None:
        readout = brc_decimal_readout(division(1, 3), 12)
        self.assertEqual(readout.text, "0.333333333333")
        self.assertFalse(readout.exact)
        self.assertEqual(readout.scaled.trace.remainder, 1)
        self.assertEqual(
            readout.scaled.trace.evaluation_kind,
            "BRC_DIVISION_EVALUATION",
        )

    def test_bigint_precision_has_no_float_fallback(self) -> None:
        scale = decimal_scale(10_000)
        readout = brc_scaled_evaluate(division(1, 3), scale)
        q = readout.scaled_value
        self.assertEqual(readout.trace.remainder, 1)
        self.assertEqual(3 * q + 1, scale)
        self.assertGreater(q.bit_length(), 30_000)


if __name__ == "__main__":
    unittest.main()
