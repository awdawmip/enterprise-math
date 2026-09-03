import inspect
import unittest
from decimal import Decimal, localcontext

from enterprise_math import euler_dyadic_cayley_bridge as bridge


class EulerDyadicCayleyBridgeTests(unittest.TestCase):
    def test_cayley_reconstructs_every_root_state(self):
        tolerance = Decimal("1e-75")
        for depth in range(1, 12):
            residual = bridge.cayley_reconstruction_residual(depth, precision=100)
            self.assertLess(max(abs(value) for value in residual), tolerance)

    def test_each_finite_cayley_state_is_an_exact_half_turn_root(self):
        tolerance = Decimal("1e-65")
        for depth in range(1, 11):
            residual = bridge.finite_half_turn_residual(depth, precision=100)
            self.assertLess(max(abs(value) for value in residual), tolerance)

    def test_cayley_parameters_obey_the_exact_doubling_law(self):
        tolerance = Decimal("1e-75")
        with localcontext() as context:
            context.prec = 110
            for depth in range(1, 11):
                coarse = bridge.cayley_parameter(depth, precision=100)
                fine = bridge.cayley_parameter(depth + 1, precision=100)
                reconstructed = Decimal(2) * fine / (Decimal(1) - fine * fine)
                self.assertLess(abs(coarse - reconstructed), tolerance)

    def test_lower_and_upper_sequences_squeeze_monotonically(self):
        lowers = [bridge.lower_half_period(depth, precision=100) for depth in range(1, 13)]
        uppers = [bridge.upper_half_period(depth, precision=100) for depth in range(1, 13)]
        self.assertTrue(all(left < right for left, right in zip(lowers, lowers[1:])))
        self.assertTrue(all(left > right for left, right in zip(uppers, uppers[1:])))
        self.assertTrue(all(lower < upper for lower, upper in zip(lowers, uppers)))
        self.assertEqual(uppers[0], Decimal(4))

    def test_two_exact_upper_and_width_formulas(self):
        tolerance = Decimal("1e-75")
        for depth in range(1, 12):
            certificate = bridge.dyadic_cayley_certificate(depth, precision=100)
            self.assertTrue(certificate.valid(tolerance))

    def test_squeeze_width_strictly_decays(self):
        widths = [bridge.squeeze_width(depth, precision=100) for depth in range(1, 13)]
        self.assertTrue(all(left > right > 0 for left, right in zip(widths, widths[1:])))

    def test_checker_has_no_target_pi_or_trigonometry(self):
        source = inspect.getsource(bridge)
        self.assertNotIn("math.pi", source)
        self.assertNotIn("sin(", source)
        self.assertNotIn("cos(", source)


if __name__ == "__main__":
    unittest.main()
