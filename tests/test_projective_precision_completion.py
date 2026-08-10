import unittest

from enterprise_math.projective_precision_completion import (
    finite_shadow_is_surjective,
    project_binary_profile,
    realize_finite_binary_pattern,
)


class ProjectivePrecisionCompletionTests(unittest.TestCase):
    def test_every_finite_binary_shadow_is_surjective(self) -> None:
        for size in range(0, 7):
            self.assertTrue(finite_shadow_is_surjective(tuple(range(size))))

    def test_arbitrary_finite_pattern_has_canonical_finite_support_realizer(self) -> None:
        pattern = {2: 1, 3: 0, 5: 1, 7: 0, 11: 1}
        profile = realize_finite_binary_pattern(pattern)
        self.assertEqual(profile, frozenset({2, 5, 11}))
        self.assertEqual(
            project_binary_profile(profile, pattern),
            tuple(pattern.values()),
        )

    def test_later_coordinates_default_to_zero_without_affecting_finite_shadow(self) -> None:
        profile = realize_finite_binary_pattern({2: 1, 3: 1, 5: 0})
        self.assertEqual(project_binary_profile(profile, (2, 3, 5)), (1, 1, 0))
        self.assertEqual(project_binary_profile(profile, (7, 11, 13)), (0, 0, 0))


if __name__ == "__main__":
    unittest.main()
