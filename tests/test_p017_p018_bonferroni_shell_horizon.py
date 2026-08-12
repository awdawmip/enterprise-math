import ast
import inspect
import unittest

from enterprise_math import p017_p018_bonferroni_shell_horizon as shell_module
from enterprise_math.p017_p018_bonferroni_precision import signed_support_profile
from enterprise_math.p017_p018_bonferroni_shell_horizon import (
    bonferroni_least_factor_horizon,
    defect_shell_localization,
    residual_first_defect_band_rigidity,
)


class P017P018BonferroniShellHorizonTests(unittest.TestCase):
    def test_exact_root_horizons(self):
        self.assertEqual(bonferroni_least_factor_horizon(65536, 3)["least_factor_horizon"], 256)
        self.assertEqual(bonferroni_least_factor_horizon(65536, 5)["least_factor_horizon"], 40)
        self.assertEqual(bonferroni_least_factor_horizon(65536, 7)["least_factor_horizon"], 16)
        self.assertEqual(bonferroni_least_factor_horizon(8191, 5)["least_factor_horizon"], 20)

    def test_bounded_signed_profiles_obey_shell_localization(self):
        for k in range(4, 70):
            profile = signed_support_profile(k)
            for order in (1, 3, 5):
                for row in profile["rows"]:
                    support = tuple(int(p) for p in row["support"])
                    if len(support) < order + 1:
                        continue
                    data = defect_shell_localization(
                        k,
                        int(row["state"]),
                        support,
                        order,
                    )
                    self.assertTrue(data["defect_possible"])
                    self.assertTrue(data["localized"])
                    self.assertLessEqual(
                        data["least_support_prime"],
                        data["least_factor_horizon"],
                    )

    def test_order_five_defect_is_cubic_least_factor_localized(self):
        k = 65536

        # Four small primes do not yet create order-five defect.
        four_support_state = k * (k + 1) + 883
        four_support = (3, 5, 7, 43)
        self.assertFalse(
            defect_shell_localization(k, four_support_state, four_support, 5)["defect_possible"]
        )

        # This actual basin state has six distinct small prime divisors:
        # 4295098269 = 3^2 * 7 * 11 * 23 * 37 * 7283.
        six_support_state = 4_295_098_269
        six_support = (3, 7, 11, 23, 37, 7283)
        data = defect_shell_localization(k, six_support_state, six_support, 5)
        self.assertEqual(data["least_factor_horizon"], 40)
        self.assertEqual(data["least_support_prime"], 3)
        self.assertTrue(data["localized"])

    def test_first_order_three_residual_defect_band_is_rigid(self):
        data = residual_first_defect_band_rigidity(65536, 883, 3)
        self.assertEqual(data["first_band_lower_barrier"], 15015)
        self.assertEqual(data["first_band_upper_barrier"], 255255)
        self.assertEqual(
            sorted((data["lower_support_size"], data["upper_support_size"])),
            [1, 4],
        )
        self.assertEqual(data["total_support_size"], 5)
        self.assertEqual(data["total_pair_defect"], 1)
        self.assertTrue(data["rigid_first_band_defect"])

    def test_reference_nondefect_cell_stays_nondefective(self):
        data = residual_first_defect_band_rigidity(20000, 67, 3)
        self.assertEqual(data["total_pair_defect"], 0)
        self.assertFalse(data["rigid_first_band_defect"])

    def test_invalid_even_order(self):
        with self.assertRaises(ValueError):
            bonferroni_least_factor_horizon(100, 2)

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(shell_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
