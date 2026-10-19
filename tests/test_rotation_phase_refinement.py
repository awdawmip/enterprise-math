import unittest
from decimal import Decimal
from fractions import Fraction

from enterprise_math.rotation_phase_refinement import (
    CyclicPhaseLevel,
    GatePhaseState,
    certificate,
    crt_six_generator_certificate,
    dyadic_trace_data,
    gate_iterate,
    gate_phase_index,
    gate_phase_state,
    gate_refinement_certificate,
    minimal_cyclic_refinement_order,
    pivot_gate_certificates,
    quarter_turn_roots,
    verify_dyadic_trace_data,
)


class RotationPhaseRefinementTests(unittest.TestCase):
    def test_six_pivot_gates_are_exact_triple_intersections(self):
        gates = pivot_gate_certificates()
        self.assertEqual(len(gates), 6)
        for item in gates:
            self.assertTrue(item.valid)
            self.assertEqual(item.pivot_distance_sq, Fraction(1, 3))
            self.assertEqual(item.left_distance_sq, Fraction(1, 3))
            self.assertEqual(item.right_distance_sq, Fraction(1, 3))

    def test_gate_phase_encoding_is_c12(self):
        for index in range(12):
            self.assertEqual(gate_phase_index(gate_phase_state(index)), index)
        origin = GatePhaseState("cell", 0)
        self.assertEqual(gate_iterate(origin, 2), GatePhaseState("cell", 1))
        self.assertEqual(gate_iterate(origin, 3), GatePhaseState("gate", 1))
        self.assertEqual(gate_iterate(origin, 4), GatePhaseState("cell", 2))
        self.assertEqual(gate_iterate(origin, 6), GatePhaseState("cell", 3))
        self.assertEqual(gate_iterate(origin, 12), origin)
        self.assertTrue(gate_refinement_certificate()["quarter_square"])

    def test_crt_c6_generator(self):
        cert = crt_six_generator_certificate()
        self.assertEqual(cert["generator"], (2, 1))
        self.assertEqual(cert["square"], (1, 0))
        self.assertEqual(cert["cube"], (0, 1))

    def test_quarter_turn_minimality(self):
        self.assertEqual(quarter_turn_roots(6), ())
        self.assertEqual(quarter_turn_roots(12), (3, 9))
        self.assertEqual(minimal_cyclic_refinement_order(6), 12)

    def test_refinement_embedding_and_phase_metric(self):
        for depth in range(5):
            level = CyclicPhaseLevel(depth)
            for left in range(level.order):
                for right in range(level.order):
                    self.assertTrue(level.embedding_isometric(left, right))

    def test_refinement_bit_and_carry(self):
        level = CyclicPhaseLevel(0)
        for fine in range(12):
            coarse, residual = level.split_fine_state(fine)
            self.assertEqual(level.recompose_fine_state(coarse, residual), fine)
        self.assertEqual(level.refined_successor_digits(2, 0), (2, 1))
        self.assertEqual(level.refined_successor_digits(2, 1), (3, 0))

    def test_i_is_first_refinement_residual_state(self):
        coarse = CyclicPhaseLevel(0)
        fine = CyclicPhaseLevel(1)
        self.assertIsNone(coarse.quarter_turn)
        self.assertEqual(fine.quarter_turn, 3)
        self.assertEqual(coarse.split_fine_state(fine.quarter_turn), (1, 1))

    def test_dyadic_half_trace_and_viete_readout(self):
        self.assertTrue(verify_dyadic_trace_data(25, precision=120))
        data = dyadic_trace_data(12, precision=100)
        self.assertEqual(data[0].half_trace, Decimal(0))
        self.assertEqual(data[0].skew_trace, Decimal(1))
        self.assertGreater(data[1].half_trace, Decimal(0))
        for left, right in zip(data, data[1:]):
            self.assertLess(left.finite_half_slope, right.finite_half_slope)

    def test_full_certificate(self):
        payload = certificate()
        self.assertTrue(payload["dyadic_trace_verified"])
        self.assertEqual(payload["minimal_order_from_c6_with_quarter_turn"], 12)


if __name__ == "__main__":
    unittest.main()
