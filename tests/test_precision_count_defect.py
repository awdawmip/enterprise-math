import unittest

from enterprise_math.precision_count_defect import (
    bell_excess,
    chsh_count_word,
    count_ray_equal,
    cross_defect,
    max_seed_transfer_defect,
    path_crossover_count_word,
    path_crossover_growth_cross_defect,
    primitive_count_vector,
    r004_bell_target_count_tables,
    r004_sharp_setting_weight_rows,
    relaxed_bell_slack,
    seed_transfer_defect,
    threshold_count_margin,
    threshold_record_count_word,
)
from enterprise_math.precision_locality_obstruction import (
    local_joint_counts_for_setting,
)


class PrecisionCountDefectTests(unittest.TestCase):
    def test_rational_count_rays_have_unique_primitive_integer_words(self):
        self.assertEqual(primitive_count_vector((2, 8, 8, 2)), (1, 4, 4, 1))
        self.assertTrue(count_ray_equal((2, 8, 8, 2), (1, 4, 4, 1)))
        self.assertFalse(count_ray_equal((2, 8, 8, 2), (1, 3, 5, 1)))

    def test_cross_defect_compares_normalized_parts_without_division(self):
        self.assertEqual(cross_defect(2, 5, 4, 10), 0)
        self.assertGreater(cross_defect(3, 5, 4, 10), 0)
        self.assertLess(cross_defect(1, 5, 4, 10), 0)

    def test_bell_target_is_integer_excess_word(self):
        numerator, total = chsh_count_word(r004_bell_target_count_tables())
        self.assertEqual((numerator, total), (-56, 20))
        self.assertEqual(bell_excess(numerator, total), 16)

    def test_sharp_measurement_dependence_is_seed_transfer_saturation(self):
        rows = r004_sharp_setting_weight_rows()
        self.assertEqual({sum(row) for row in rows.values()}, {60})
        transfer = max_seed_transfer_defect(rows)
        self.assertEqual(transfer, 8)

        observed = {
            setting: local_joint_counts_for_setting(rows[setting], setting)
            for setting in rows
        }
        numerator, total = chsh_count_word(observed)
        self.assertEqual((numerator, total), (-168, 60))
        self.assertEqual(bell_excess(numerator, total), 48)
        self.assertEqual(relaxed_bell_slack(numerator, total, transfer), 0)

        # Every pair of setting rows differs by exactly eight seed reassignments.
        settings = tuple(rows)
        for index, left in enumerate(settings):
            for right in settings[index + 1 :]:
                self.assertEqual(seed_transfer_defect(rows[left], rows[right]), 8)

    def test_threshold_record_is_two_integer_counts_and_external_margin(self):
        self.assertEqual(threshold_record_count_word(3, 10), (7, 3))
        self.assertEqual(threshold_record_count_word(12, 10), (0, 10))
        agreement, separated = threshold_record_count_word(9, 10)
        self.assertEqual(agreement + separated, 10)
        self.assertGreaterEqual(threshold_count_margin(agreement, 10, 9, 100), 0)
        agreement, _ = threshold_record_count_word(10, 10)
        self.assertLess(threshold_count_margin(agreement, 10, 9, 100), 0)

    def test_path_macro_crossover_stays_as_count_word(self):
        self.assertEqual(path_crossover_count_word(8, 3), (15, 13))
        for resolution in range(1, 8):
            for vertices in range(2, 20):
                self.assertGreaterEqual(
                    path_crossover_growth_cross_defect(vertices, resolution), 0
                )

    def test_invalid_count_states_fail_closed(self):
        with self.assertRaises(ValueError):
            primitive_count_vector((0, 0))
        with self.assertRaises(ValueError):
            seed_transfer_defect((1, 2), (1, 3))
        with self.assertRaises(ValueError):
            cross_defect(6, 5, 1, 2)


if __name__ == "__main__":
    unittest.main()
