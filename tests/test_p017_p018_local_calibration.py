import ast
import inspect
import unittest

from enterprise_math import p017_p018_local_calibration as calibration_module
from enterprise_math.p017_p018_local_calibration import (
    local_radius_euler_calibration,
    singular_core_local_split,
    transverse_radius_residue_split,
)


class P017P018LocalCalibrationTests(unittest.TestCase):
    def test_reference_primes_match_exact_residue_proportions(self):
        expected = {
            3: ((2, 3), (1, 3)),
            5: ((2, 5), (3, 5)),
            7: ((2, 7), (5, 7)),
            11: ((2, 11), (9, 11)),
        }
        for prime, (present, absent) in expected.items():
            data = local_radius_euler_calibration(prime)
            self.assertTrue(data["calibrated"])
            self.assertEqual(data["core_present_share"], present)
            self.assertEqual(data["core_absent_share"], absent)

    def test_radius_and_euler_splits_agree_for_many_primes(self):
        for prime in (3, 5, 7, 11, 13, 17, 19, 31, 43, 101):
            radius = transverse_radius_residue_split(prime)
            euler = singular_core_local_split(prime)
            self.assertEqual(radius["core_present_density"], euler["core_present_share"])
            self.assertEqual(radius["core_absent_density"], euler["core_absent_share"])

    def test_p3_near_saturation_is_the_two_thirds_local_branch(self):
        data = local_radius_euler_calibration(3)
        self.assertEqual(data["core_present_share"], (2, 3))
        self.assertEqual(data["core_absent_share"], (1, 3))

    def test_invalid_prime_rejected(self):
        with self.assertRaises(ValueError):
            local_radius_euler_calibration(2)
        with self.assertRaises(ValueError):
            local_radius_euler_calibration(9)

    def test_reference_module_is_integer_only(self):
        tree = ast.parse(inspect.getsource(calibration_module))
        self.assertFalse(
            any(isinstance(node, ast.Constant) and isinstance(node.value, float) for node in ast.walk(tree))
        )
        self.assertFalse(
            any(isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div) for node in ast.walk(tree))
        )


if __name__ == "__main__":
    unittest.main()
