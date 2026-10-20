import ast
import inspect
import unittest

import enterprise_math.p017_p018_core_mass_rankin as rankin
from enterprise_math.p017_p018_core_mass_rankin import (
    anchor_local_rankin_margin,
    odd_zeta_correction_partial,
    unrestricted_local_correction,
)


class P017P018CoreMassRankinTests(unittest.TestCase):
    def test_anchor_local_ratio_never_exceeds_y_on_rational_grid(self):
        for prime in (3, 5, 7, 11, 17, 31, 101):
            for denominator in range(1, 10):
                for numerator in range(denominator, 4 * denominator + 1):
                    data = anchor_local_rankin_margin(prime, numerator, denominator)
                    rn, rd = data["rankin_ratio"]
                    yn, yd = data["y"]
                    self.assertLessEqual(rn * yd, rd * yn)
                    self.assertGreater(data["cleared_margin"], 0)

    def test_exact_y_one_ratio_is_p_squared_over_p_squared_plus_one(self):
        for prime in (3, 5, 7, 11, 19):
            data = anchor_local_rankin_margin(prime, 1, 1)
            self.assertEqual(
                data["rankin_ratio"],
                (prime * prime, prime * prime + 1),
            )

    def test_zeta_correction_quadratic_maximum_at_one_over_p_plus_one(self):
        for prime in (3, 5, 7, 11, 23):
            data = unrestricted_local_correction(prime, 1, prime + 1)
            self.assertEqual(data["correction"], data["maximum"])
            self.assertEqual(data["maximum"], (prime * prime, prime * prime - 1))

    def test_zeta_correction_bound_on_full_rational_interval(self):
        for prime in (3, 5, 7, 13):
            for denominator in range(prime, 8 * prime + 1):
                for numerator in range(0, denominator // prime + 1):
                    data = unrestricted_local_correction(prime, numerator, denominator)
                    cn, cd = data["correction"]
                    mn, md = data["maximum"]
                    self.assertLessEqual(cn * md, mn * cd)

    def test_partial_odd_correction_product_increases(self):
        primes = (3, 5, 7, 11, 13, 17, 19)
        previous = (1, 1)
        for end in range(1, len(primes) + 1):
            current = odd_zeta_correction_partial(primes[:end])
            self.assertGreater(current[0] * previous[1], previous[0] * current[1])
            previous = current

    def test_validation(self):
        with self.assertRaises(ValueError):
            anchor_local_rankin_margin(9, 1, 1)
        with self.assertRaises(ValueError):
            anchor_local_rankin_margin(3, 1, 2)
        with self.assertRaises(ValueError):
            unrestricted_local_correction(3, 2, 3)
        with self.assertRaises(ValueError):
            odd_zeta_correction_partial((3, 3))

    def test_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(rankin))
        floats = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.Constant) and isinstance(node.value, float)
        ]
        divisions = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div)
        ]
        self.assertEqual(floats, [])
        self.assertEqual(divisions, [])


if __name__ == "__main__":
    unittest.main()
