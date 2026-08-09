import math
import unittest

from enterprise_math.abc_block_access_apery import (
    access_defect_transform,
    apery_access_profile,
    apery_values,
    eventual_block_access_radius,
    eventual_period_shift_holds,
    exact_block_access_radius,
    minimum_nonnegative_linf_factorization,
    primitive_positive_row,
)
from enterprise_math.abc_diophantine_modular import minimum_linf_two_variable_modular


class AbcBlockAccessAperyTests(unittest.TestCase):
    def test_signed_access_to_nonnegative_defect_transform(self) -> None:
        data = access_defect_transform((5, 2), 1, (1, -2))
        self.assertEqual(data["radius"], 2)
        self.assertEqual(data["period"], 7)
        self.assertEqual(data["defect"], 13)
        self.assertEqual(data["nonnegative_coordinates"], (1, 4))
        self.assertEqual(5 * 1 + 2 * 4, 13)

    def test_two_variable_apery_profile_is_exact(self) -> None:
        profile = apery_access_profile((5, 2))
        self.assertEqual(profile.period, 7)
        self.assertEqual(apery_values((5, 2)), (0, 8, 2, 10, 4, 5, 6))
        self.assertEqual(profile.exceptional_targets, (1,))

        records = {record.target_residue: record for record in profile.residues}
        self.assertEqual(records[1].apery_value, 6)
        self.assertEqual(records[1].apery_min_linf, 3)
        self.assertEqual(records[1].first_stable_target, 8)
        self.assertEqual(records[2].first_stable_target, 2)

        for target in range(0, 80):
            exact = minimum_linf_two_variable_modular(5, 2, target).radius
            self.assertEqual(exact_block_access_radius((5, 2), target), exact)
            if target in profile.exceptional_targets:
                with self.assertRaises(ValueError):
                    eventual_block_access_radius((5, 2), target)
            else:
                self.assertEqual(eventual_block_access_radius((5, 2), target), exact)

    def test_three_coordinate_profile_matches_exact_oracle(self) -> None:
        coefficients = (15, 10, 6)
        profile = apery_access_profile(coefficients)
        self.assertEqual(profile.period, 31)
        for target in range(0, 70):
            exact = exact_block_access_radius(coefficients, target, max_radius=30)
            if target in profile.exceptional_targets:
                continue
            self.assertEqual(eventual_block_access_radius(coefficients, target), exact)

    def test_unit_relation_block_examples(self) -> None:
        primitive, scale = primitive_positive_row((121, 44))
        self.assertEqual((primitive, scale), ((11, 4), 11))
        self.assertEqual(exact_block_access_radius((121, 44), 4455), 27)
        self.assertEqual(eventual_block_access_radius((121, 44), 4455), 27)

        self.assertEqual(exact_block_access_radius((513, 27), 6912), 13)
        self.assertEqual(eventual_block_access_radius((513, 27), 6912), 13)

    def test_apery_factorization_radius(self) -> None:
        self.assertEqual(minimum_nonnegative_linf_factorization((5, 2), 8), 4)
        self.assertEqual(minimum_nonnegative_linf_factorization((11, 4), 16), 4)
        self.assertEqual(minimum_nonnegative_linf_factorization((15, 10, 6), 32), 2)
        with self.assertRaises(ValueError):
            minimum_nonnegative_linf_factorization((4, 6), 3)

    def test_eventual_period_shift(self) -> None:
        for coefficients, target in (((5, 2), 8), ((11, 4), 405), ((15, 10, 6), 62)):
            self.assertTrue(eventual_period_shift_holds(coefficients, target))

    def test_scaled_rows_preserve_access_after_target_reduction(self) -> None:
        for target in range(0, 100, 2):
            self.assertEqual(
                exact_block_access_radius((10, 4), target),
                exact_block_access_radius((5, 2), target // 2),
            )

    def test_profile_against_all_small_coprime_two_variable_rows(self) -> None:
        checked = 0
        for A in range(1, 10):
            for B in range(1, 10):
                if math.gcd(A, B) != 1:
                    continue
                profile = apery_access_profile((A, B))
                exceptions = set(profile.exceptional_targets)
                for target in range(0, 45):
                    reference = minimum_linf_two_variable_modular(A, B, target).radius
                    self.assertEqual(
                        exact_block_access_radius((A, B), target, max_radius=50),
                        reference,
                    )
                    if target not in exceptions:
                        self.assertEqual(
                            eventual_block_access_radius((A, B), target),
                            reference,
                        )
                    checked += 1
        self.assertGreater(checked, 2000)


if __name__ == "__main__":
    unittest.main()
