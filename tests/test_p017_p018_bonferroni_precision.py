import ast
import inspect
import unittest

from enterprise_math import p017_p018_bonferroni_precision as bonf_module
from enterprise_math.p017_p018_bonferroni_precision import (
    bonferroni_precision_certificate,
    odd_bonferroni_upper_from_moments,
    signed_support_profile,
)


class P017P018BonferroniPrecisionTests(unittest.TestCase):
    def test_anchor_surviving_empty_support_is_exactly_prime(self):
        for k in (7, 16, 31, 64):
            data = signed_support_profile(k)
            for row in data["rows"]:
                self.assertEqual(not bool(row["support"]), bool(row["is_prime"]))

    def test_reference_scales_need_increasing_proof_precision(self):
        self.assertEqual(
            bonferroni_precision_certificate(16, 5)["first_certifying_order"],
            1,
        )
        self.assertEqual(
            bonferroni_precision_certificate(31, 5)["first_certifying_order"],
            3,
        )
        self.assertEqual(
            bonferroni_precision_certificate(127, 5)["first_certifying_order"],
            3,
        )
        self.assertEqual(
            bonferroni_precision_certificate(256, 5)["first_certifying_order"],
            3,
        )

    def test_k862_is_explicit_order_five_witness(self):
        data = bonferroni_precision_certificate(862, 5)
        rows = {row["order"]: row for row in data["odd_order_rows"]}
        self.assertFalse(rows[3]["certificate"])
        self.assertLessEqual(rows[3]["slack_to_all_states"], 0)
        self.assertTrue(rows[5]["certificate"])
        self.assertEqual(data["first_certifying_order"], 5)

    def test_bonferroni_upper_is_above_actual_composite_union(self):
        for k in range(4, 45):
            data = bonferroni_precision_certificate(k, 5)
            composite = data["composite_state_count"]
            for row in data["odd_order_rows"]:
                self.assertGreaterEqual(row["upper_bound"], composite)

    def test_alternating_sum_helper(self):
        moments = (10, 6, 2, 1, 0)
        self.assertEqual(odd_bonferroni_upper_from_moments(moments, 1), 10)
        self.assertEqual(odd_bonferroni_upper_from_moments(moments, 3), 6)
        self.assertEqual(odd_bonferroni_upper_from_moments(moments, 5), 5)
        with self.assertRaises(ValueError):
            odd_bonferroni_upper_from_moments(moments, 2)

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(bonf_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
