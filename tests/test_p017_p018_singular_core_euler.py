import ast
import inspect
import unittest

from enterprise_math import p017_p018_singular_core_euler as euler_module
from enterprise_math.p017_p018_singular_core_euler import (
    allowed_prime_leading_cancellation,
    anchor_prime_leading_factor,
    core_prime_power_local_sum,
    finite_leading_correction,
    generic_twin_local_factor,
)


class P017P018SingularCoreEulerTests(unittest.TestCase):
    def test_allowed_odd_primes_cancel_exactly(self):
        for prime in (3, 5, 7, 11, 13, 31, 101):
            data = allowed_prime_leading_cancellation(prime)
            self.assertEqual(data["combined"], (1, 1))

    def test_local_closed_forms(self):
        self.assertEqual(generic_twin_local_factor(5), (15, 16))
        self.assertEqual(core_prime_power_local_sum(5), (5, 3))
        self.assertEqual(anchor_prime_leading_factor(5), (16, 25))

    def test_empty_odd_anchor_set_gives_one_eighth_candidate_log2_coefficient(self):
        data = finite_leading_correction(())
        self.assertEqual(data["odd_anchor_density"], (1, 1))
        self.assertEqual(data["leading_correction"], (1, 4))
        self.assertEqual(data["candidate_log2_coefficient"], (1, 8))

    def test_anchor_factors_give_delta_squared_over_eight_candidate(self):
        data = finite_leading_correction((3, 5, 7))
        self.assertEqual(data["odd_anchor_density"], (16, 35))
        self.assertEqual(data["leading_correction"], (64, 1225))
        self.assertEqual(data["candidate_log2_coefficient"], (32, 1225))

    def test_duplicate_or_nonprime_anchor_rejected(self):
        with self.assertRaises(ValueError):
            finite_leading_correction((3, 3))
        with self.assertRaises(ValueError):
            finite_leading_correction((9,))

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(euler_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
