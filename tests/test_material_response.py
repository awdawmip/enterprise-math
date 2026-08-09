import unittest

from enterprise_math.material_response import (
    branch_gap_sum,
    hardening_branch,
    hardening_sample,
    material_curve_profile,
    offset_sample,
    retained_branch,
    retained_sample,
    signed_branch_area,
    softening_branch,
    softening_sample,
)


class MaterialResponseTests(unittest.TestCase):
    def test_hardening_and_softening_preserve_scale_and_order(self):
        for amplitude in range(1, 25):
            for power in range(1, 5):
                hard = []
                soft = []
                for sample in range(amplitude + 1):
                    h = hardening_sample(sample, amplitude, power)
                    g = softening_sample(sample, amplitude, power)
                    self.assertLessEqual(h, sample)
                    self.assertLessEqual(sample, g)
                    self.assertLessEqual(g, amplitude)
                    hard.append(h)
                    soft.append(g)
                self.assertEqual(hard, sorted(hard))
                self.assertEqual(soft, sorted(soft))
                self.assertEqual(hard[0], 0)
                self.assertEqual(soft[0], 0)
                self.assertEqual(hard[-1], amplitude)
                self.assertEqual(soft[-1], amplitude)

    def test_reference_power_two_samples_match_pressure_test(self):
        amplitude = 1000
        expected = {
            197: (38, 443),
            386: (148, 621),
            560: (313, 748),
            712: (506, 843),
            835: (697, 913),
            924: (853, 961),
            977: (954, 988),
        }
        for sample, pair in expected.items():
            self.assertEqual(
                (
                    hardening_sample(sample, amplitude, 2),
                    softening_sample(sample, amplitude, 2),
                ),
                pair,
            )

    def test_retention_is_explicit_integer_amplitude_collapse(self):
        self.assertEqual(retained_sample(1000, 1000, 1000), 1000)
        self.assertEqual(retained_sample(1000, 1000, 0), 0)
        self.assertEqual(retained_sample(777, 1000, 500), 388)
        branch = retained_branch((0, 250, 500, 750, 1000), 1000, 500)
        self.assertEqual(branch, (0, 125, 250, 375, 500))

    def test_offset_is_finite_and_clamped(self):
        self.assertEqual(offset_sample(3, 10, -5), 0)
        self.assertEqual(offset_sample(3, 10, 4), 7)
        self.assertEqual(offset_sample(8, 10, 5), 10)

    def test_profile_keeps_loading_and_return_branches_separate(self):
        base = (0, 250, 500, 750, 1000)
        profile = material_curve_profile(
            base,
            amplitude=1000,
            loading_power=2,
            return_power=1,
            return_retention=500,
        )
        self.assertEqual(profile.loading, (0, 62, 250, 562, 1000))
        self.assertEqual(profile.returning, (0, 125, 250, 375, 500))
        self.assertEqual(profile.branch_gap, 687)
        self.assertEqual(profile.signed_area, 624)
        self.assertEqual(profile.peak_loading, 1000)
        self.assertEqual(profile.peak_returning, 500)

    def test_branch_gap_and_signed_area_are_distinct_observables(self):
        loading = (0, 2, 5, 4)
        returning = (0, 3, 1, 4)
        self.assertEqual(branch_gap_sum(loading, returning), 4)
        self.assertEqual(signed_branch_area(loading, returning), 3)

    def test_branch_helpers_are_pointwise_and_finite(self):
        base = (0, 10, 25, 50, 75, 100)
        hard = hardening_branch(base, 100, 3)
        soft = softening_branch(base, 100, 3)
        self.assertEqual(len(hard), len(base))
        self.assertEqual(len(soft), len(base))
        self.assertTrue(all(0 <= value <= 100 for value in hard + soft))

    def test_invalid_curve_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            hardening_sample(11, 10, 2)
        with self.assertRaises(ValueError):
            softening_sample(1, 10, 0)
        with self.assertRaises(ValueError):
            retained_sample(1, 10, 11)
        with self.assertRaises(ValueError):
            branch_gap_sum((1,), (1, 2))


if __name__ == "__main__":
    unittest.main()
