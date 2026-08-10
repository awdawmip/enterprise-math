import ast
import inspect
import unittest

from enterprise_math import p017_p018_token_capacity_recursion as recursion_module
from enterprise_math.p017_p018_token_capacity_recursion import (
    token_capacity_descent,
    token_capacity_step,
)


class P017P018TokenCapacityRecursionTests(unittest.TestCase):
    def test_524287_capacity_excess_is_exact_nested_quotient_chain(self):
        data = token_capacity_descent(524_287, 7)
        rows = data["rows"]
        self.assertEqual(
            tuple((row["order"], row["capacity"], row["excess"]) for row in rows),
            ((1, 34_953, 34_952), (3, 454, 453), (5, 3, 2), (7, 1, 0)),
        )
        self.assertEqual(rows[1]["incoming_prime_pair"], (7, 11))
        self.assertEqual(rows[1]["incoming_scale_factor"], 77)
        self.assertEqual(rows[2]["incoming_prime_pair"], (13, 17))
        self.assertEqual(rows[2]["incoming_scale_factor"], 221)
        self.assertEqual(rows[3]["incoming_prime_pair"], (19, 23))
        self.assertEqual(rows[3]["incoming_scale_factor"], 437)
        self.assertEqual(data["first_zero_excess_order_within_horizon"], 7)

    def test_each_step_is_exact_floor_projection(self):
        for k in (8191, 65_536, 131_071, 524_287):
            for order in (1, 3, 5):
                step = token_capacity_step(k, order)
                self.assertTrue(step["quotient_recursion_exact"])
                self.assertLessEqual(step["next_excess"], step["current_excess"])
                if step["pair_scale_factor"] is not None:
                    self.assertEqual(
                        step["next_excess"],
                        step["current_excess"] // step["pair_scale_factor"],
                    )

    def test_next_mersenne_scale_reaches_zero_at_order_nine(self):
        k = 2_147_483_647
        data = token_capacity_descent(k, 9)
        self.assertEqual(data["first_zero_excess_order_within_horizon"], 9)
        self.assertEqual(data["rows"][-1]["excess"], 0)

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(recursion_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
