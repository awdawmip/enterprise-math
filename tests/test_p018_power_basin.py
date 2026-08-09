import ast
import inspect
import unittest

import enterprise_math.p018_power_basin as power_basin
from enterprise_math.p018_power_basin import (
    iterated_power_basin_quotient_transport,
    power_basin_quotient_transport,
    power_basin_quotient_window,
    whole_basin_strict_root_descent,
)


class AllPowerQuotientBasinTests(unittest.TestCase):
    def test_window_always_meets_at_most_two_adjacent_root_indices(self):
        for power in range(1, 7):
            for k in range(1, 41):
                for divisor in range(2, 31):
                    data = power_basin_quotient_window(power, k, divisor)
                    self.assertLess(data["base_root"], k)
                    self.assertIn(data["max_root"], (data["base_root"], data["base_root"] + 1))

    def test_statewise_transport_matches_direct_roots_on_small_basins(self):
        for power in range(1, 5):
            for k in range(1, 13):
                lower = k**power
                upper = (k + 1) ** power
                for divisor in range(2, 13):
                    for n in range(lower, upper):
                        data = power_basin_quotient_transport(power, k, divisor, n)
                        self.assertIn(data["upper_bit"], (0, 1))
                        self.assertEqual(
                            data["quotient_root"], data["base_root"] + data["upper_bit"]
                        )

    def test_split_criterion_is_exact(self):
        for power in range(1, 7):
            for k in range(1, 50):
                for divisor in range(2, 40):
                    data = power_basin_quotient_window(power, k, divisor)
                    expected = int(
                        divisor * (data["base_root"] + 1) ** power
                        <= (k + 1) ** power - 1
                    )
                    self.assertEqual(data["split"], expected)
                    self.assertEqual(
                        data["max_root"], data["base_root"] + expected
                    )

    def test_strict_root_descent_criterion_is_exact(self):
        for power in range(1, 8):
            for k in range(1, 70):
                for divisor in range(2, 35):
                    expected = (k + 1) ** power <= divisor * k**power
                    self.assertEqual(
                        whole_basin_strict_root_descent(power, k, divisor), expected
                    )
                    data = power_basin_quotient_window(power, k, divisor)
                    self.assertEqual(bool(data["strict_root_descent"]), data["max_root"] < k)

    def test_iterated_quotients_flatten_before_root_transport(self):
        cases = [
            (2, 17, [2, 3], 17**2 + 19),
            (3, 11, [2, 5, 3], 11**3 + 37),
            (4, 7, [3, 2], 8**4 - 1),
            (5, 5, [2, 2, 2], 5**5),
        ]
        for power, k, divisors, n in cases:
            data = iterated_power_basin_quotient_transport(power, k, divisors, n)
            product = 1
            for divisor in divisors:
                product *= divisor
            self.assertEqual(data["divisor_product"], product)
            self.assertEqual(data["quotient"], n // product)
            self.assertEqual(data["path_states"][-1], n // product)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            power_basin_quotient_window(0, 2, 2)
        with self.assertRaises(ValueError):
            power_basin_quotient_window(2, 0, 2)
        with self.assertRaises(ValueError):
            power_basin_quotient_window(2, 2, 1)
        with self.assertRaises(ValueError):
            power_basin_quotient_transport(2, 3, 2, 8)

    def test_reference_module_has_no_float_or_true_division(self):
        tree = ast.parse(inspect.getsource(power_basin))
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
