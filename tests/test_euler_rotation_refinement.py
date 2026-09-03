import inspect
import unittest
from decimal import Decimal, localcontext

from enterprise_math import euler_rotation_refinement as err


class EulerRotationRefinementTests(unittest.TestCase):
    def test_minimal_orders_and_distinguished_root_orders(self):
        for depth in range(8):
            cert = err.rotation_level_certificate(depth)
            self.assertTrue(cert.valid)
            self.assertEqual(cert.order, 6 * 2**depth)
            self.assertEqual(cert.root_order, 2 ** (depth + 1))

    def test_square_root_compatibility(self):
        for depth in range(8):
            self.assertEqual(*err.root_square_certificate(depth))

    def test_first_refinement_is_cell_gate_cycle(self):
        cycle = err.cell_gate_cycle()
        self.assertEqual(len(cycle), 12)
        self.assertEqual(cycle[0], "C0")
        self.assertEqual(cycle[1], "G0")
        self.assertEqual(cycle[3], "G1")
        self.assertEqual(cycle[6], "C3")
        self.assertEqual(err.phase_kind(3, 1), "gate")
        self.assertEqual(err.half_turn_index(1), 6)

    def test_chiral_quarter_roots_are_swapped_by_reflection(self):
        positive, negative = err.quarter_turn_roots(1)
        self.assertEqual((positive, negative), (3, 9))
        self.assertEqual(err.reflection(positive, 1), negative)
        half = err.half_turn_index(1)
        self.assertEqual((2 * positive) % err.phase_order(1), half)
        self.assertEqual((2 * negative) % err.phase_order(1), half)

    def test_every_new_root_is_born_at_its_level(self):
        self.assertEqual(err.phase_kind(3, 0), "cell")
        self.assertEqual(err.phase_kind(3, 1), "gate")
        for depth in range(2, 8):
            self.assertEqual(err.phase_birth_level(3, depth), depth)
            self.assertEqual(err.phase_kind(3, depth), "higher-transition")

    def test_cell_gate_geometry_is_saturated_at_c12(self):
        self.assertEqual(err.local_cell_gate_capacity(), 12)
        self.assertEqual(err.required_nonlocal_phase_states(0), 0)
        self.assertEqual(err.required_nonlocal_phase_states(1), 0)
        self.assertEqual(err.required_nonlocal_phase_states(2), 12)

    def test_target_free_viete_identity(self):
        with localcontext() as context:
            context.prec = 120
            for depth in range(1, 12):
                left = err.rotation_pi_approximant(depth, precision=110)
                right = err.rotation_pi_viete_form(depth, precision=110)
                self.assertLess(abs(left - right), Decimal("1e-95"))

    def test_rotation_approximants_strictly_increase(self):
        values = [
            err.rotation_pi_approximant(depth, precision=100)
            for depth in range(1, 14)
        ]
        self.assertTrue(all(a < b for a, b in zip(values, values[1:])))

    def test_trace_norm_and_half_angle_recursion(self):
        with localcontext() as context:
            context.prec = 120
            for depth in range(1, 12):
                c = err.symmetric_trace(depth, precision=110)
                s = err.antisymmetric_trace(depth, precision=110)
                self.assertLess(abs(c * c + s * s - 1), Decimal("1e-95"))
            for depth in range(1, 11):
                coarse = err.symmetric_trace(depth, precision=110)
                fine = err.symmetric_trace(depth + 1, precision=110)
                self.assertLess(
                    abs(coarse - (2 * fine * fine - 1)),
                    Decimal("1e-95"),
                )

    def test_completion_bound_is_positive_and_decays(self):
        bounds = [
            err.completion_tail_bound(depth, precision=100)
            for depth in range(2, 10)
        ]
        self.assertTrue(all(value > 0 for value in bounds))
        self.assertTrue(all(a > b for a, b in zip(bounds, bounds[1:])))

    def test_no_hidden_pi_or_trigonometry_in_checker(self):
        source = inspect.getsource(err)
        self.assertNotIn("math.pi", source)
        self.assertNotIn("sin(", source)
        self.assertNotIn("cos(", source)


if __name__ == "__main__":
    unittest.main()
