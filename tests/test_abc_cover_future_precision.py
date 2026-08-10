import unittest
from fractions import Fraction

from enterprise_math.abc_cover_future_precision import (
    binary_nonattenuating_from_bits,
    binary_observation_trace,
    cover_future_precision_state,
    exact_multiplier_from_resonance_residual,
    exact_observation_trace,
    ternary_observation_trace,
    ternary_transport_class_from_bits,
)


class CoverFuturePrecisionTests(unittest.TestCase):
    def setUp(self) -> None:
        # A: nonresonant + squarefree -> attenuated.
        self.A = cover_future_precision_state(5, 59, 3, 3, "sum")
        # B: resonant + squarefree -> exact resonance.
        self.B = cover_future_precision_state(11, 13, 3, 3, "sum")
        # C: resonant + repeated -> amplified.
        self.C = cover_future_precision_state(7, 29, 3, 3, "sum")
        # D: nonresonant + repeated -> amplified.
        self.D = cover_future_precision_state(3, 13, 3, 3, "difference")

    def test_four_logical_bit_states_map_to_expected_future_outputs(self) -> None:
        self.assertEqual(
            (self.A.support_resonance, self.A.quotient_squarefree),
            (False, True),
        )
        self.assertFalse(self.A.binary_nonattenuating)
        self.assertEqual(self.A.ternary_transport_class, "attenuated")
        self.assertEqual(self.A.exact_multiplier, Fraction(1, 3))

        self.assertEqual(
            (self.B.support_resonance, self.B.quotient_squarefree),
            (True, True),
        )
        self.assertTrue(self.B.binary_nonattenuating)
        self.assertEqual(self.B.ternary_transport_class, "resonant")
        self.assertEqual(self.B.exact_multiplier, 1)

        self.assertEqual(
            (self.C.support_resonance, self.C.quotient_squarefree),
            (True, False),
        )
        self.assertTrue(self.C.binary_nonattenuating)
        self.assertEqual(self.C.ternary_transport_class, "amplified")
        self.assertEqual(self.C.exact_multiplier, 19)

        self.assertEqual(
            (self.D.support_resonance, self.D.quotient_squarefree),
            (False, False),
        )
        self.assertTrue(self.D.binary_nonattenuating)
        self.assertEqual(self.D.ternary_transport_class, "amplified")
        self.assertEqual(self.D.exact_multiplier, Fraction(19, 3))

    def test_binary_query_has_two_complementary_short_circuit_orders(self) -> None:
        # Resonance-first wins on B: R=True already proves non-attenuation.
        trace = binary_observation_trace(self.B, "resonance_first")
        self.assertTrue(trace.short_circuited)
        self.assertEqual(trace.observed_fields, ("support_resonance",))
        self.assertTrue(trace.result)
        trace_other = binary_observation_trace(self.B, "squarefree_first")
        self.assertFalse(trace_other.short_circuited)
        self.assertEqual(
            trace_other.observed_fields,
            ("quotient_squarefree", "support_resonance"),
        )

        # Squarefree-first wins on D: S=False already proves amplification/non-attenuation.
        trace = binary_observation_trace(self.D, "squarefree_first")
        self.assertTrue(trace.short_circuited)
        self.assertEqual(trace.observed_fields, ("quotient_squarefree",))
        self.assertTrue(trace.result)
        trace_other = binary_observation_trace(self.D, "resonance_first")
        self.assertFalse(trace_other.short_circuited)
        self.assertEqual(
            trace_other.observed_fields,
            ("support_resonance", "quotient_squarefree"),
        )

    def test_no_binary_observation_order_uniformly_dominates(self) -> None:
        self.assertLess(
            len(binary_observation_trace(self.B, "resonance_first").observed_fields),
            len(binary_observation_trace(self.B, "squarefree_first").observed_fields),
        )
        self.assertLess(
            len(binary_observation_trace(self.D, "squarefree_first").observed_fields),
            len(binary_observation_trace(self.D, "resonance_first").observed_fields),
        )

    def test_squarefree_first_weakly_dominates_for_ternary_query(self) -> None:
        for state in (self.A, self.B, self.C, self.D):
            squarefree_first = ternary_observation_trace(state, "squarefree_first")
            resonance_first = ternary_observation_trace(state, "resonance_first")
            self.assertEqual(squarefree_first.result, state.ternary_transport_class)
            self.assertEqual(resonance_first.result, state.ternary_transport_class)
            self.assertLessEqual(
                len(squarefree_first.observed_fields),
                len(resonance_first.observed_fields),
            )

        for state in (self.C, self.D):
            trace = ternary_observation_trace(state, "squarefree_first")
            self.assertTrue(trace.short_circuited)
            self.assertEqual(trace.observed_fields, ("quotient_squarefree",))
            self.assertEqual(trace.result, "amplified")

        for state in (self.A, self.B):
            trace = ternary_observation_trace(state, "squarefree_first")
            self.assertFalse(trace.short_circuited)
            self.assertEqual(
                trace.observed_fields,
                ("quotient_squarefree", "support_resonance"),
            )

    def test_each_single_natural_bit_is_insufficient_for_ternary_class(self) -> None:
        # Same R=True, different classes.
        self.assertEqual(self.B.support_resonance, self.C.support_resonance)
        self.assertNotEqual(self.B.ternary_transport_class, self.C.ternary_transport_class)
        # Same S=True, different classes.
        self.assertEqual(self.A.quotient_squarefree, self.B.quotient_squarefree)
        self.assertNotEqual(self.A.ternary_transport_class, self.B.ternary_transport_class)

    def test_exact_multiplier_requires_residual_value_not_only_squarefree_bit(self) -> None:
        trace = exact_observation_trace(self.C)
        self.assertEqual(
            trace.observed_fields,
            ("support_resonance", "quotient_residual"),
        )
        self.assertEqual(trace.result, 19)
        self.assertEqual(
            exact_multiplier_from_resonance_residual(True, 19, 3),
            19,
        )
        self.assertEqual(
            exact_multiplier_from_resonance_residual(False, 19, 3),
            Fraction(19, 3),
        )

    def test_semantic_quotients_form_a_strict_natural_precision_hierarchy(self) -> None:
        # Exact state (R,d) determines ternary (R,S), because S iff d=1.
        for state in (self.A, self.B, self.C, self.D):
            derived_squarefree = state.quotient_residual == 1
            self.assertEqual(derived_squarefree, state.quotient_squarefree)
            self.assertEqual(
                ternary_transport_class_from_bits(
                    state.support_resonance, derived_squarefree
                ),
                state.ternary_transport_class,
            )
            self.assertEqual(
                binary_nonattenuating_from_bits(
                    state.support_resonance, derived_squarefree
                ),
                state.binary_nonattenuating,
            )

        # Ternary state does not determine exact multiplier: two repeated states
        # can share the same qualitative class while numerical multipliers differ.
        self.assertEqual(self.C.ternary_transport_class, self.D.ternary_transport_class)
        self.assertNotEqual(self.C.exact_multiplier, self.D.exact_multiplier)


if __name__ == "__main__":
    unittest.main()
