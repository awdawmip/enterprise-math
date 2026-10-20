import unittest

from enterprise_math.prime_cubic_horizontal_placement import (
    database_overflow_q_max,
    effective_row_fits_cubic,
    effective_row_q_max,
    effective_row_visible_horizontally,
    horizontal_cofactor_upper_scale_max,
    linear_cursor_offset_limit,
    lower_band_q_max,
    real_seam_sufficient,
    square_boundary_cursor_width,
    unresolved_lower_q_interval,
    unresolved_lower_q_width,
)


class PrimeCubicHorizontalPlacementTests(unittest.TestCase):
    def test_horizontal_scale_max_is_exact(self):
        for k in range(2, 200):
            u = (k + 1) ** 3 - 1
            self.assertEqual(horizontal_cofactor_upper_scale_max(k), u // (k + 1))
            self.assertEqual(horizontal_cofactor_upper_scale_max(k), (k + 1) ** 2 - 1)

    def test_unresolved_cursor_matches_literal_conditions(self):
        for k in range(3, 80):
            for x in (20, 50, 200, 1000):
                lo, hi = unresolved_lower_q_interval(k, x)
                literal = [
                    q
                    for q in range(k + 1, lower_band_q_max(k) + 1)
                    if k**3 // q >= x
                ]
                compiled = list(range(lo, hi + 1)) if lo <= hi else []
                self.assertEqual(compiled, literal)

    def test_hybrid_row_exact_integer_cursor(self):
        k = 100
        x = 4000
        x0 = 3500
        delta = 100
        self.assertTrue(effective_row_visible_horizontally(k, x0))
        self.assertTrue(effective_row_fits_cubic(k, delta))
        lo, hi = unresolved_lower_q_interval(k, x, scale_min=x0, delta=delta)
        expected_lo = max(k + 1, effective_row_q_max(k, x0) + 1)
        expected_hi = min(lower_band_q_max(k), database_overflow_q_max(k, x))
        self.assertEqual((lo, hi), (expected_lo, expected_hi))
        self.assertEqual(unresolved_lower_q_width(k, x, scale_min=x0, delta=delta), max(0, hi-lo+1))

    def test_real_seam_is_sufficient(self):
        for k in range(10, 100):
            a = k**3
            u = (k + 1) ** 3 - 1
            for x in (100, 1000, 10000):
                x0 = x
                self.assertEqual(real_seam_sufficient(k, x, x0), x0 * a <= x * u)

    def test_current_square_boundary_cursor_law(self):
        K = 10_000_000_000
        self.assertEqual(linear_cursor_offset_limit(K), 57_734)
        for d in (0, 1, 2, 10, 1000, 57_734):
            self.assertEqual(square_boundary_cursor_width(K, d), 2 * d)
        self.assertEqual(square_boundary_cursor_width(K, 57_735), 2 * 57_735 + 1)

        for d in range(1, 100):
            k = K + d
            self.assertEqual(
                unresolved_lower_q_interval(k, 10**20),
                (k + 1, k + 2 * d),
            )


if __name__ == "__main__":
    unittest.main()
