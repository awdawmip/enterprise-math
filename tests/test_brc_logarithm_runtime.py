import unittest

from enterprise_math.brc_logarithm import (
    brc_evaluate_ln,
    brc_evaluate_log,
    brc_ln_decimal_readout,
    brc_log_decimal_readout,
    ln,
    log10,
    logarithm,
)
from enterprise_math.exact_arithmetic import decimal_scale, division


class BRCLogarithmRuntimeTests(unittest.TestCase):
    def test_ln_and_log_travel_unevaluated(self) -> None:
        ln_expr = ln(division(2, 1))
        log_expr = logarithm(division(32, 1), division(8, 1))
        self.assertEqual(ln_expr.argument, division(2, 1))
        self.assertEqual(log_expr.argument, division(32, 1))
        self.assertEqual(log_expr.base, division(8, 1))

    def test_domain_is_positive_and_log_base_is_not_one(self) -> None:
        with self.assertRaises(ValueError):
            ln(division(0, 1))
        with self.assertRaises(ValueError):
            logarithm(division(2, 1), division(0, 1))
        with self.assertRaises(ValueError):
            logarithm(division(2, 1), division(7, 7))

    def test_ln_two_decimal_readout_is_brc_interval_gated(self) -> None:
        readout = brc_ln_decimal_readout(ln(division(2, 1)), 12)
        self.assertEqual(readout.text, "0.693147180559")
        trace = readout.scaled.trace
        self.assertEqual(trace.evaluation_kind, "BRC_LN_INTERVAL_EVALUATION")
        self.assertEqual(trace.sign, 1)
        self.assertEqual(trace.lower_floor_trace.quotient, trace.magnitude_index)
        self.assertEqual(trace.upper_floor_trace.quotient, trace.magnitude_index)
        self.assertEqual(
            trace.lower_floor_trace.evaluation_kind,
            "BRC_DIVISION_EVALUATION",
        )

    def test_ln_reciprocal_uses_signed_magnitude_without_float(self) -> None:
        readout = brc_ln_decimal_readout(ln(division(1, 2)), 12)
        self.assertEqual(readout.text, "-0.693147180559")
        self.assertEqual(readout.scaled.trace.sign, -1)
        self.assertEqual(
            readout.scaled.trace.magnitude_index,
            brc_ln_decimal_readout(ln(division(2, 1)), 12).scaled.trace.magnitude_index,
        )

    def test_ln_one_is_exact_zero_boundary(self) -> None:
        readout = brc_ln_decimal_readout(ln(division(1, 1)), 12)
        self.assertEqual(readout.text, "0.000000000000")
        self.assertTrue(readout.exact)
        self.assertEqual(readout.scaled.trace.terms, 0)

    def test_log10_power_hits_exact_boundary_by_power_relation(self) -> None:
        readout = brc_log_decimal_readout(log10(division(1000, 1)), 12)
        self.assertEqual(readout.text, "3.000000000000")
        trace = readout.scaled.trace
        self.assertTrue(trace.exact_boundary)
        self.assertIsNotNone(trace.boundary_proof)
        proof = trace.boundary_proof
        assert proof is not None
        self.assertEqual(proof.boundary_numerator, 3)
        self.assertEqual(proof.boundary_denominator, 1)
        self.assertEqual(proof.common_root_numerator, 10)
        self.assertEqual(proof.common_root_denominator, 1)
        self.assertTrue(proof.root_traces)
        self.assertTrue(
            all(
                root_trace.evaluation_kind == "BRC_ROOT_EVALUATION"
                for root_trace in proof.root_traces
            )
        )

    def test_fractional_exact_log_boundary_reuses_brc_root(self) -> None:
        readout = brc_log_decimal_readout(
            logarithm(division(2, 1), division(4, 1)),
            12,
        )
        self.assertEqual(readout.text, "0.500000000000")
        proof = readout.scaled.trace.boundary_proof
        self.assertIsNotNone(proof)
        assert proof is not None
        self.assertEqual(proof.boundary_numerator, 1)
        self.assertEqual(proof.boundary_denominator, 2)
        self.assertEqual(proof.common_root_numerator, 2)
        self.assertEqual(proof.common_root_denominator, 1)

    def test_boundary_power_relation_handles_unreduced_div_carrier(self) -> None:
        readout = brc_log_decimal_readout(
            logarithm(division(4, 2), division(4, 1)),
            12,
        )
        self.assertEqual(readout.text, "0.500000000000")
        proof = readout.scaled.trace.boundary_proof
        self.assertIsNotNone(proof)
        assert proof is not None
        self.assertEqual(proof.reduced_argument_numerator, 2)
        self.assertEqual(proof.reduced_argument_denominator, 1)
        self.assertTrue(proof.reduction_traces)
        self.assertTrue(
            all(
                reduction.evaluation_kind == "BRC_DIVISION_EVALUATION"
                for reduction in proof.reduction_traces
            )
        )

    def test_non_boundary_log_returns_unique_precision_cell(self) -> None:
        readout = brc_log_decimal_readout(
            logarithm(division(32, 1), division(8, 1)),
            12,
        )
        self.assertEqual(readout.text, "1.666666666666")
        trace = readout.scaled.trace
        self.assertFalse(trace.exact_boundary)
        self.assertIsNone(trace.boundary_proof)
        self.assertEqual(trace.lower_floor_trace.quotient, trace.magnitude_index)
        self.assertEqual(trace.upper_floor_trace.quotient, trace.magnitude_index)

    def test_log_sign_handles_argument_or_base_below_one(self) -> None:
        argument_below_one = brc_log_decimal_readout(
            log10(division(1, 2)),
            12,
        )
        base_below_one = brc_log_decimal_readout(
            logarithm(division(2, 1), division(1, 10)),
            12,
        )
        self.assertEqual(argument_below_one.text, "-0.301029995663")
        self.assertEqual(base_below_one.text, "-0.301029995663")
        self.assertEqual(argument_below_one.scaled.trace.sign, -1)
        self.assertEqual(base_below_one.scaled.trace.sign, -1)

    def test_high_precision_ln_uses_bigint_interval_refinement(self) -> None:
        digits = 1_000
        readout = brc_ln_decimal_readout(ln(division(2, 1)), digits)
        self.assertTrue(
            readout.text.startswith(
                "0.69314718055994530941723212145817656807550013436025"
            )
        )
        self.assertEqual(len(readout.text), digits + 2)
        trace = readout.scaled.trace
        self.assertEqual(trace.scale, decimal_scale(digits))
        self.assertEqual(trace.lower_floor_trace.quotient, trace.magnitude_index)
        self.assertEqual(trace.upper_floor_trace.quotient, trace.magnitude_index)
        self.assertGreater(trace.magnitude_index.bit_length(), 3_000)

    def test_direct_scaled_log_trace_is_reproducible(self) -> None:
        scale = decimal_scale(20)
        trace = brc_evaluate_log(log10(division(2, 1)), scale)
        self.assertEqual(trace.sign, 1)
        self.assertEqual(trace.scale, scale)
        self.assertEqual(trace.lower_floor_trace.quotient, trace.magnitude_index)
        self.assertEqual(trace.upper_floor_trace.quotient, trace.magnitude_index)

    def test_direct_scaled_ln_trace_is_reproducible(self) -> None:
        scale = decimal_scale(20)
        trace = brc_evaluate_ln(ln(division(3, 2)), scale)
        self.assertEqual(trace.sign, 1)
        self.assertEqual(trace.scale, scale)
        self.assertEqual(trace.lower_floor_trace.quotient, trace.magnitude_index)
        self.assertEqual(trace.upper_floor_trace.quotient, trace.magnitude_index)


if __name__ == "__main__":
    unittest.main()
