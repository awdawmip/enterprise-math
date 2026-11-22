import ast
import inspect
import unittest

from enterprise_math import p017_p018_effective_rankin as rankin_module
from enterprise_math.p017_p018_effective_rankin import (
    effective_anchor_radical,
    p017_effective_rankin_parameters,
    truncated_coprimality_equivalence,
)


class P017P018EffectiveRankinTests(unittest.TestCase):
    def test_critical_scales_have_trivial_effective_anchor_radical(self):
        for k in (3, 4, 7, 16, 31, 127, 256):
            data = p017_effective_rankin_parameters(k)
            self.assertEqual(data["effective_anchor_radical"], 1)
            self.assertEqual(data["effective_odd_anchor_density"], (1, 1))
            self.assertEqual(data["effective_rankin_scale_product"], k)

    def test_noncritical_reference_scales_keep_only_primes_below_k(self):
        data = p017_effective_rankin_parameters(64)
        self.assertEqual(data["effective_odd_anchor_primes"], (5, 13))
        self.assertEqual(data["effective_anchor_radical"], 65)
        self.assertEqual(data["effective_odd_anchor_density"], (48, 65))

        data = p017_effective_rankin_parameters(32)
        self.assertEqual(data["effective_odd_anchor_primes"], (3, 11))
        self.assertEqual(data["effective_anchor_radical"], 33)

    def test_large_endpoint_prime_is_removed_from_finite_cutoff(self):
        # k=31 is prime and k+1=32.  The odd endpoint prime 31 divides M but
        # cannot divide any positive odd core S<31, so the effective radical is 1.
        center = 31 * 32
        data = effective_anchor_radical(center, 31)
        self.assertEqual(data["effective_odd_anchor_primes"], ())
        self.assertEqual(data["effective_anchor_radical"], 1)

    def test_truncated_coprimality_equivalence_for_every_odd_core_candidate(self):
        for k in range(3, 160):
            center = k * (k + 1)
            for value in range(1, k, 2):
                data = truncated_coprimality_equivalence(center, k, value)
                self.assertTrue(data["equivalent_on_odd_core_domain"])
                self.assertEqual(
                    data["coprime_to_center"],
                    data["coprime_to_effective_odd_radical"],
                )

    def test_even_value_need_not_obey_odd_core_equivalence(self):
        data = truncated_coprimality_equivalence(20, 5, 2)
        self.assertFalse(data["coprime_to_center"])
        self.assertTrue(data["coprime_to_effective_odd_radical"])
        self.assertTrue(data["equivalent_on_odd_core_domain"])

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(rankin_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
