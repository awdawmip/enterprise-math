import ast
import inspect
import unittest

from enterprise_math import p017_p018_effective_anchor as anchor_module
from enterprise_math.p017_p018_effective_anchor import (
    anchor_critical_classification,
    anchor_surviving_radius_count,
    effective_odd_anchor_primes,
    is_power_of_two,
)


class P017P018EffectiveAnchorTests(unittest.TestCase):
    def test_critical_even_power_of_two_prime_successor_family(self):
        for k in (2, 4, 16, 256):
            data = anchor_critical_classification(k)
            self.assertTrue(data["critical"])
            self.assertEqual(data["kind"], "POWER_OF_TWO_WITH_PRIME_SUCCESSOR")
            self.assertEqual(data["surviving_radius_count"], k // 2)

    def test_critical_prime_before_power_of_two_family(self):
        for k in (3, 7, 31, 127):
            data = anchor_critical_classification(k)
            self.assertTrue(data["critical"])
            self.assertEqual(data["kind"], "PRIME_BEFORE_POWER_OF_TWO")
            self.assertEqual(data["surviving_radius_count"], (k - 1) // 2)

    def test_noncritical_scales_expose_effective_odd_anchor(self):
        expected = {
            8: (3,),
            15: (3, 5),
            17: (3,),
            32: (3, 11),
            64: (5, 13),
        }
        for k, anchors in expected.items():
            data = anchor_critical_classification(k)
            self.assertFalse(data["critical"])
            self.assertEqual(data["effective_odd_anchors"], anchors)
            self.assertEqual(effective_odd_anchor_primes(k), anchors)

    def test_classification_is_exhaustive_on_bounded_range(self):
        saw_both_critical_kinds = set()
        for k in range(2, 600):
            data = anchor_critical_classification(k)
            self.assertEqual(data["surviving_radius_count"], anchor_surviving_radius_count(k))
            if data["critical"]:
                self.assertEqual(data["effective_odd_anchors"], ())
                saw_both_critical_kinds.add(data["kind"])
            else:
                self.assertTrue(data["effective_odd_anchors"])
        self.assertEqual(
            saw_both_critical_kinds,
            {"POWER_OF_TWO_WITH_PRIME_SUCCESSOR", "PRIME_BEFORE_POWER_OF_TWO"},
        )

    def test_power_of_two_helper(self):
        self.assertTrue(is_power_of_two(1))
        self.assertTrue(is_power_of_two(1024))
        self.assertFalse(is_power_of_two(0))
        self.assertFalse(is_power_of_two(12))

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(anchor_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
