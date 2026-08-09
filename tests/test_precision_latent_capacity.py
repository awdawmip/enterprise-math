import unittest

from enterprise_math.precision_latent_capacity import (
    full_support_string_count,
    maximum_full_support_steps,
    minimum_deterministic_seed_states,
    presampling_capacity_deficit,
    presampling_capacity_sufficient,
)


class PrecisionLatentCapacityTests(unittest.TestCase):
    def test_full_support_binary_strings_require_exponential_seed_support(self):
        self.assertEqual(
            tuple(minimum_deterministic_seed_states(steps, 2) for steps in range(1, 7)),
            (2, 4, 8, 16, 32, 64),
        )

    def test_bound_is_sharp_by_counting(self):
        self.assertEqual(full_support_string_count(3, 3), 27)
        self.assertFalse(presampling_capacity_sufficient(26, 3, 3))
        self.assertTrue(presampling_capacity_sufficient(27, 3, 3))
        self.assertEqual(presampling_capacity_deficit(20, 3, 3), 7)
        self.assertEqual(presampling_capacity_deficit(30, 3, 3), 0)

    def test_maximum_steps_uses_only_integer_resource_accounting(self):
        self.assertEqual(maximum_full_support_steps(1, 2), 0)
        self.assertEqual(maximum_full_support_steps(7, 2), 2)
        self.assertEqual(maximum_full_support_steps(8, 2), 3)
        self.assertEqual(maximum_full_support_steps(26, 3), 2)
        self.assertEqual(maximum_full_support_steps(27, 3), 3)

    def test_invalid_inputs_fail_closed(self):
        with self.assertRaises(ValueError):
            full_support_string_count(0, 2)
        with self.assertRaises(ValueError):
            presampling_capacity_sufficient(0, 1, 2)
        with self.assertRaises(ValueError):
            maximum_full_support_steps(8, 0)


if __name__ == "__main__":
    unittest.main()
