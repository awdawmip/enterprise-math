import unittest

from enterprise_math.material_oscillator import PythagoreanRotation
from enterprise_math.material_peak_profile import (
    intrinsic_peak_base_samples,
    intrinsic_peak_material_profile,
)


class MaterialPeakProfileTests(unittest.TestCase):
    def test_base_domain_is_generated_by_integer_peak_not_external_step_count(self):
        for rotation in (
            PythagoreanRotation(3, 4, 5),
            PythagoreanRotation(5, 12, 13),
            PythagoreanRotation(399, 40, 401),
        ):
            for amplitude in (10, 50, 200):
                samples = intrinsic_peak_base_samples(amplitude, rotation)
                self.assertEqual(samples[0], 0)
                self.assertTrue(
                    all(left < right for left, right in zip(samples, samples[1:]))
                )
                self.assertLessEqual(samples[-1], amplitude)

    def test_reference_399_40_401_profile_has_large_intrinsic_peak(self):
        result = intrinsic_peak_material_profile(
            1000,
            PythagoreanRotation(399, 40, 401),
            loading_power=1,
            return_power=1,
        )
        self.assertEqual(result.base_samples[0], 0)
        self.assertGreater(result.base_samples[-1], 900)
        self.assertEqual(
            result.base_samples[-1],
            result.peak_trace.peak_state[1],
        )
        self.assertEqual(len(result.material_profile.loading), len(result.base_samples))
        self.assertEqual(len(result.material_profile.returning), len(result.base_samples))

    def test_same_intrinsic_base_can_generate_distinct_integer_material_branches(self):
        rotation = PythagoreanRotation(399, 40, 401)
        linear = intrinsic_peak_material_profile(
            1000, rotation, loading_power=1, return_power=1
        )
        shaped = intrinsic_peak_material_profile(
            1000,
            rotation,
            loading_power=2,
            return_power=2,
            return_retention=700,
        )
        self.assertEqual(linear.base_samples, shaped.base_samples)
        self.assertNotEqual(
            linear.material_profile.loading,
            shaped.material_profile.loading,
        )
        self.assertNotEqual(
            linear.material_profile.returning,
            shaped.material_profile.returning,
        )

    def test_small_amplitude_still_uses_certified_finite_peak_domain(self):
        result = intrinsic_peak_material_profile(
            3,
            PythagoreanRotation(3, 4, 5),
            loading_power=1,
            return_power=1,
        )
        self.assertGreaterEqual(len(result.base_samples), 1)
        self.assertEqual(result.base_samples[0], 0)


if __name__ == "__main__":
    unittest.main()
