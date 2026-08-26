import ast
import inspect
import unittest

from enterprise_math import p017_p018_token_remainder_repair as repair_module
from enterprise_math.p017_p018_token_remainder_repair import (
    quotient_remainder_token_repair,
    signed_token_fiber,
)


class P017P018TokenRemainderRepairTests(unittest.TestCase):
    def test_524287_minimum_order_five_token_has_exact_binary_repair(self):
        data = quotient_remainder_token_repair(524_287, 255_255)
        self.assertEqual(data["universal_capacity"], 3)
        self.assertEqual(data["actual_fiber_size"], 2)
        self.assertEqual(data["boundary_savings"], 1)
        self.assertEqual(data["signed_points"], (-345_469, 165_041))
        self.assertEqual(data["repair_modulus"], 4)
        self.assertEqual(data["repair_symbol_count"], 2)
        self.assertEqual(data["repair_residues"], (3, 1))
        self.assertTrue(data["injective_remainder_repair"])
        self.assertFalse(data["repair_is_trivial"])

    def test_singleton_token_has_trivial_repair(self):
        data = quotient_remainder_token_repair(524_287, 435_435)
        self.assertEqual(data["actual_fiber_size"], 1)
        self.assertEqual(data["repair_symbol_count"], 1)
        self.assertEqual(data["repair_modulus"], 2)
        self.assertTrue(data["repair_is_trivial"])

    def test_actual_fiber_never_exceeds_universal_cg12_capacity(self):
        for k in range(4, 100):
            center = k * (k + 1)
            for divisor in range(3, k + 15, 2):
                from math import gcd

                if gcd(divisor, center) != 1:
                    continue
                data = signed_token_fiber(k, divisor)
                self.assertLessEqual(data["actual_fiber_size"], data["universal_capacity"])
                if data["actual_fiber_size"]:
                    repaired = quotient_remainder_token_repair(k, divisor)
                    self.assertEqual(
                        len(set(repaired["repair_residues"])),
                        repaired["actual_fiber_size"],
                    )

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(repair_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
