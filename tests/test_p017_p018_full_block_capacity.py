import ast
import inspect
import unittest

from enterprise_math import p017_p018_full_block_capacity as full_block_module
from enterprise_math.p017_p018_full_block_capacity import full_block_token_capacity


class P017P018FullBlockCapacityTests(unittest.TestCase):
    def test_prime_power_multiplicity_can_cross_single_use_threshold(self):
        # k=22, M=506, upper r=19: 525=3*5^2*7.
        data = full_block_token_capacity(22, 525, (3, 5))
        self.assertEqual(data["squarefree_token"], 15)
        self.assertEqual(data["full_block_token"], 75)
        self.assertEqual(data["quotient"], 7)
        self.assertFalse(data["squarefree_radical_single_use"])
        self.assertTrue(data["full_block_single_use"])
        self.assertTrue(data["prime_power_multiplicity_strictly_strengthened_threshold"])
        self.assertEqual(data["full_block_cg12_capacity"], 1)
        self.assertTrue(data["fully_k_smooth"])
        self.assertTrue(data["l053_singleton_side"])
        self.assertEqual(data["quotient_support"], (7,))
        self.assertFalse(data["repeated_residual_token_possible"])

    def test_order_five_full_support_token_is_singleton(self):
        state = 4_295_098_269
        data = full_block_token_capacity(
            65_536,
            state,
            (3, 7, 11, 23, 37, 7283),
        )
        self.assertEqual(data["full_block_token"], state)
        self.assertEqual(data["quotient"], 1)
        self.assertTrue(data["full_block_single_use"])
        self.assertTrue(data["fully_k_smooth"])
        self.assertEqual(data["quotient_support"], ())

    def test_small_full_block_remains_in_reusable_candidate_regime(self):
        # k=64, lower state 4096+64-47=4113 = 3*7*... ; select one
        # represented support prime only to keep the full block below k.
        data = full_block_token_capacity(64, 4113, (3,))
        self.assertLessEqual(data["full_block_token"], 63)
        self.assertFalse(data["full_block_single_use"])
        self.assertTrue(data["repeated_residual_token_possible"])

    def test_invalid_non_support_prime(self):
        with self.assertRaises(ValueError):
            full_block_token_capacity(22, 525, (11,))

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(full_block_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
