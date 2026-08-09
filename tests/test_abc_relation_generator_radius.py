import unittest

from enterprise_math.abc_relation_generator_radius import (
    accessible_unit_relation_scale_factors,
    exact_unit_relation_generator_radius,
    generated_scale_gcd,
    sophie_relation_generator_profile,
    unit_relation_common_group_step,
)


class AbcRelationGeneratorRadiusTests(unittest.TestCase):
    def test_189_all_three_scales_coincide(self) -> None:
        self.assertEqual(unit_relation_common_group_step(8, 9), 12)
        data = exact_unit_relation_generator_radius(8, 9)
        self.assertEqual(data.first_nonzero_radius, 2)
        self.assertEqual(data.generator_radius, 2)
        self.assertEqual(data.primitive_direct_radius, 2)
        self.assertIn(1, data.scale_factors_at_generator_radius)

    def test_1_plus_22_equals_23_has_three_distinct_scales(self) -> None:
        self.assertEqual(unit_relation_common_group_step(22, 23), 1)
        self.assertEqual(accessible_unit_relation_scale_factors(22, 23, 2), (0, 2))
        self.assertEqual(generated_scale_gcd(22, 23, 2), 2)
        self.assertEqual(generated_scale_gcd(22, 23, 3), 2)
        self.assertEqual(generated_scale_gcd(22, 23, 4), 1)

        data = exact_unit_relation_generator_radius(22, 23)
        self.assertEqual(
            (
                data.first_nonzero_radius,
                data.generator_radius,
                data.primitive_direct_radius,
            ),
            (2, 4, 5),
        )
        self.assertIn(2, data.scale_factors_at_generator_radius)
        self.assertIn(3, data.scale_factors_at_generator_radius)

    def test_sophie_closed_form_examples(self) -> None:
        for q, expected in (
            (5, (2, 2, 2)),
            (11, (2, 4, 5)),
            (23, (2, 8, 11)),
            (29, (2, 10, 14)),
            (41, (2, 14, 20)),
        ):
            data = sophie_relation_generator_profile(q)
            self.assertEqual(
                (data["mu"], data["generator_radius"], data["nu"]),
                expected,
            )

    def test_strict_separation_for_sophie_q_at_least_11(self) -> None:
        for q in (11, 23, 29, 41):
            data = sophie_relation_generator_profile(q)
            self.assertLess(data["mu"], data["generator_radius"])
            self.assertLess(data["generator_radius"], data["nu"])

    def test_invalid_non_sophie_input_rejected(self) -> None:
        with self.assertRaises(ValueError):
            sophie_relation_generator_profile(7)
        with self.assertRaises(ValueError):
            sophie_relation_generator_profile(9)


if __name__ == "__main__":
    unittest.main()
