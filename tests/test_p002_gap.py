import unittest

from enterprise_math.core import collapse, integer_nth_root


class CollapseGapTests(unittest.TestCase):
    def test_sharp_bound_and_equality_state(self) -> None:
        for p in range(1, 7):
            for n in range(0, 5001):
                k = integer_nth_root(n, p)
                gap = n - collapse(n, p)
                bound = (k + 1) ** p - k**p - 1
                self.assertGreaterEqual(gap, 0)
                self.assertLessEqual(gap, bound)
                self.assertEqual(gap == bound, n == (k + 1) ** p - 1)

    def test_basin_gap_coordinate_is_complete(self) -> None:
        for p in range(1, 6):
            for k in range(0, 25):
                start = k**p
                stop = (k + 1) ** p
                gaps = [n - collapse(n, p) for n in range(start, stop)]
                self.assertEqual(gaps, list(range(stop - start)))

    def test_square_example(self) -> None:
        self.assertEqual(integer_nth_root(20000, 2), 141)
        self.assertEqual(collapse(20000, 2), 19881)
        self.assertEqual((142**2 - 141**2) - 1, 282)
        self.assertEqual(20163 - 19881, 282)


if __name__ == "__main__":
    unittest.main()
