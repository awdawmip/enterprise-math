import unittest

from enterprise_math.prime_cubic_oppermann_gap_bridge import (
    CULLY_HUGILL_LEE_E55_DELTA,
    CULLY_HUGILL_LEE_E60_DELTA,
    CULLY_HUGILL_LEE_E60_FIT_K_MAX,
    CURRENT_COMPLETE_CLASSIFICATION_K_MAX,
    KADIRI_LUMLEY_E59_DELTA,
    KADIRI_LUMLEY_E59_K_MAX,
    OLD_COMPLETE_PREFIX_MAX,
    OPPERMANN_INDEX_LIMIT,
    OPPERMANN_ONLY_K_MAX,
    PRIME_GAP_COVERAGE_LIMIT,
    ceil_sqrt_half_cube,
    cully_hugill_lee_e60_fit_endpoint_arithmetic_holds,
    cubic_root_horizon_pair,
    current_complete_classification_endpoint_arithmetic_holds,
    effective_relative_interval_fits,
    horizontal_gap_database_covered,
    kadiri_lumley_e59_endpoint_arithmetic_holds,
    oppermann_endpoint_arithmetic_holds,
    oppermann_escape_forces_large_effective_scale,
    oppermann_index_covered,
    upper_closed_by_uniform_gap_cap,
    worst_q_gt_k_cofactor_floor,
)


class PrimeCubicOppermannGapBridgeTests(unittest.TestCase):
    def test_exact_oppermann_endpoint(self):
        self.assertEqual(
            ceil_sqrt_half_cube(OPPERMANN_ONLY_K_MAX),
            70_499_999_996_893,
        )
        self.assertEqual(
            ceil_sqrt_half_cube(OPPERMANN_ONLY_K_MAX + 1),
            70_500_000_046_075,
        )
        self.assertTrue(oppermann_endpoint_arithmetic_holds())

    def test_oppermann_coverage_has_exact_scale_complement(self):
        n2 = OPPERMANN_INDEX_LIMIT**2
        for k in range(3, 200):
            for q in range(2, k + 1):
                self.assertEqual(
                    oppermann_index_covered(k, q),
                    k**3 <= q * n2,
                )
                self.assertTrue(oppermann_escape_forces_large_effective_scale(k, q))

    def test_q_gt_k_cofactor_cutoff_is_exact(self):
        for k in range(2, 200):
            expected = max(k**3 // q for q in range(k + 1, 3 * k + 1))
            self.assertEqual(worst_q_gt_k_cofactor_floor(k), expected)
            self.assertEqual(worst_q_gt_k_cofactor_floor(k), k * k - k)

        k = CURRENT_COMPLETE_CLASSIFICATION_K_MAX
        self.assertEqual(
            worst_q_gt_k_cofactor_floor(k),
            99_999_999_990_000_000_000,
        )
        self.assertEqual(
            worst_q_gt_k_cofactor_floor(k + 1),
            100_000_000_010_000_000_000,
        )
        self.assertTrue(horizontal_gap_database_covered(k))
        self.assertFalse(horizontal_gap_database_covered(k + 1))
        self.assertEqual(PRIME_GAP_COVERAGE_LIMIT, 100_000_000_000_000_000_000)

    def test_historical_kadiri_lumley_e59_endpoint(self):
        k = KADIRI_LUMLEY_E59_K_MAX
        delta = KADIRI_LUMLEY_E59_DELTA
        self.assertTrue(effective_relative_interval_fits(k, delta))
        self.assertFalse(effective_relative_interval_fits(k + 1, delta))
        self.assertTrue(kadiri_lumley_e59_endpoint_arithmetic_holds())

    def test_corrected_chl_rows_are_stronger(self):
        self.assertEqual(CULLY_HUGILL_LEE_E55_DELTA, 10_288_400_000)
        self.assertEqual(CULLY_HUGILL_LEE_E60_DELTA, 76_918_400_000)
        self.assertGreater(CULLY_HUGILL_LEE_E60_DELTA, KADIRI_LUMLEY_E59_DELTA)

        k = CULLY_HUGILL_LEE_E60_FIT_K_MAX
        delta = CULLY_HUGILL_LEE_E60_DELTA
        self.assertEqual(k, 230_755_199_997)
        self.assertEqual(
            3 * (k + 1) * (delta - 1) - k * k,
            230_755_199_997,
        )
        self.assertEqual(
            3 * (k + 2) * (delta - 1) - (k + 1) * (k + 1),
            -1,
        )
        self.assertTrue(cully_hugill_lee_e60_fit_endpoint_arithmetic_holds())

    def test_current_10_billion_endpoint_is_horizontal_data_boundary(self):
        k = CURRENT_COMPLETE_CLASSIFICATION_K_MAX
        self.assertEqual(k, 10_000_000_000)
        self.assertTrue(effective_relative_interval_fits(k, CULLY_HUGILL_LEE_E60_DELTA))
        self.assertEqual(
            3 * (k + 1) * (CULLY_HUGILL_LEE_E60_DELTA - 1) - k * k,
            2_207_552_000_200_755_199_997,
        )
        self.assertTrue(current_complete_classification_endpoint_arithmetic_holds())

    def test_uniform_1724_cap_closes_upper_after_old_prefix(self):
        first = OLD_COMPLETE_PREFIX_MAX + 1
        self.assertTrue(upper_closed_by_uniform_gap_cap(first))
        self.assertTrue(upper_closed_by_uniform_gap_cap(CURRENT_COMPLETE_CLASSIFICATION_K_MAX))

        s0, f0, _ = cubic_root_horizon_pair(first)
        self.assertEqual(f0 - s0, 3628)

        s1, f1, _ = cubic_root_horizon_pair(CURRENT_COMPLETE_CLASSIFICATION_K_MAX)
        self.assertEqual(f1 - s1, 150_000)


if __name__ == "__main__":
    unittest.main()
