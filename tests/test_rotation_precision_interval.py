import unittest
from decimal import Decimal

from enterprise_math.rotation_precision_interval import (
    certificate,
    rotation_precision_intervals,
    verify_nested_rotation_precision_intervals,
)


class RotationPrecisionIntervalTests(unittest.TestCase):
    def test_intervals_are_strictly_nested_without_pi_target(self):
        self.assertTrue(verify_nested_rotation_precision_intervals(35, precision=140))

    def test_first_interval(self):
        first = rotation_precision_intervals(1, precision=100)[0]
        self.assertEqual(first.level, 1)
        self.assertEqual(first.lower, Decimal(2))
        self.assertGreater(first.upper, first.lower)
        self.assertGreater(first.total_tail_defect_bound, Decimal(0))
        self.assertLess(first.total_tail_defect_bound, Decimal(1))

    def test_upper_endpoints_decrease(self):
        intervals = rotation_precision_intervals(24, precision=120)
        for left, right in zip(intervals, intervals[1:]):
            self.assertGreater(left.upper, right.upper)

    def test_lower_endpoints_increase(self):
        intervals = rotation_precision_intervals(24, precision=120)
        for left, right in zip(intervals, intervals[1:]):
            self.assertLess(left.lower, right.lower)

    def test_level_ten_certificate_values(self):
        item = rotation_precision_intervals(10, precision=100)[-1]
        self.assertTrue(str(item.lower).startswith("3.1415877252771597"))
        self.assertTrue(str(item.upper).startswith("3.1415926535921126"))
        self.assertLess(item.certified_width, Decimal("0.000005"))

    def test_serializable_certificate(self):
        payload = certificate(12, precision=100)
        self.assertTrue(payload["verified_nested"])
        self.assertEqual(len(payload["intervals"]), 12)
        self.assertIn("no target numerical pi", payload["construction"])


if __name__ == "__main__":
    unittest.main()
