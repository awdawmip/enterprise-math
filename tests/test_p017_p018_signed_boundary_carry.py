import ast
import inspect
import unittest

from enterprise_math import p017_p018_signed_boundary_carry as carry_module
from enterprise_math.p017_p018_bonferroni_precision import support_moments
from enterprise_math.p017_p018_signed_boundary_carry import (
    anchor_surviving_divisor_boundary_carry,
    raw_signed_divisor_boundary_carry,
    transverse_support_moment_from_boundary_carries,
)
from enterprise_math.p017_p018_token_remainder_repair import (
    raw_signed_token_fiber,
    signed_token_fiber,
)


class P017P018SignedBoundaryCarryTests(unittest.TestCase):
    def test_raw_centered_carry_exactly_matches_raw_token_fiber(self):
        for k in range(4, 60):
            center = k * (k + 1)
            from math import gcd

            for divisor in range(3, 3 * k + 10, 2):
                if gcd(divisor, center) != 1:
                    continue
                carry = raw_signed_divisor_boundary_carry(k, divisor)
                fiber = raw_signed_token_fiber(k, divisor)
                self.assertEqual(
                    carry["raw_signed_fiber_size"],
                    fiber["raw_fiber_size"],
                )
                self.assertEqual(
                    carry["cg12_universal_capacity"],
                    fiber["universal_capacity"],
                )
                self.assertEqual(
                    carry["raw_boundary_savings"],
                    fiber["raw_boundary_savings"],
                )

    def test_anchor_mobius_spectrum_matches_direct_survival_filter(self):
        saw_nontrivial_anchor_filter = False
        for k in range(4, 50):
            center = k * (k + 1)
            from math import gcd

            for divisor in range(3, 2 * k + 10, 2):
                if gcd(divisor, center) != 1:
                    continue
                data = anchor_surviving_divisor_boundary_carry(k, divisor)
                fiber = signed_token_fiber(k, divisor)
                self.assertEqual(
                    data["anchor_surviving_fiber_size"],
                    fiber["actual_fiber_size"],
                )
                self.assertEqual(
                    data["anchor_mobius_bulk_mass"]
                    + data["anchor_mobius_boundary_carry_mass"],
                    data["anchor_surviving_fiber_size"],
                )
                if data["anchor_filter_savings"]:
                    saw_nontrivial_anchor_filter = True
        self.assertTrue(saw_nontrivial_anchor_filter)

    def test_critical_524287_collapses_to_single_raw_carry(self):
        data = anchor_surviving_divisor_boundary_carry(524_287, 255_255)
        self.assertTrue(data["critical_single_carry_regime"])
        self.assertEqual(data["effective_odd_anchor_primes"], ())
        self.assertEqual(len(data["mobius_rows"]), 1)
        self.assertEqual(data["coarse_quotient"], 2)
        self.assertEqual(data["boundary_carry"], 0)
        self.assertEqual(data["anchor_surviving_fiber_size"], 2)
        self.assertEqual(data["cg12_universal_capacity"], 3)
        self.assertEqual(data["raw_boundary_savings"], 1)

    def test_boundary_spectrum_reconstructs_existing_support_moments(self):
        for k in range(4, 32):
            direct = support_moments(k, 3)["moments"]
            for order in (1, 2, 3):
                reconstructed = transverse_support_moment_from_boundary_carries(k, order)
                self.assertEqual(
                    reconstructed["exact_support_moment"],
                    direct[order - 1],
                )
                self.assertEqual(
                    reconstructed["exact_support_moment"],
                    reconstructed["anchor_mobius_bulk_mass"]
                    + reconstructed["anchor_mobius_boundary_carry_mass"],
                )

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(carry_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
