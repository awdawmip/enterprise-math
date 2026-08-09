import unittest

from enterprise_math.abc_precision_bridge import residual_root_horizon


class AbcPrecisionBridgeTests(unittest.TestCase):
    def test_classic_high_quality_triple_crosses_root_horizon(self) -> None:
        data = residual_root_horizon(2, 3**10 * 109, 23**5, 3, 2)
        self.assertTrue(data["high_quality"])
        self.assertEqual(data["root_exponent"], 9)
        self.assertEqual(data["residual_root_horizon"], 1061)
        self.assertEqual(data["max_residual"], 23**4)
        self.assertTrue(data["crosses_root_horizon"])

    def test_nonexceptional_state_need_not_cross(self) -> None:
        data = residual_root_horizon(1, 1, 2, 3, 2)
        self.assertFalse(data["high_quality"])


if __name__ == "__main__":
    unittest.main()
