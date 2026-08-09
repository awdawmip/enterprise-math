import unittest

from enterprise_math.material_force_work import uniform_force_law
from enterprise_math.material_radical_field_complexity import (
    material_radical_field_complexity,
    radical_field_complexity,
    squarefree_prime_support,
)
from enterprise_math.material_response import explicit_material_curve_profile


class MaterialRadicalFieldComplexityTests(unittest.TestCase):
    def test_single_rational_field_has_rank_zero(self):
        report = radical_field_complexity((1,))
        self.assertEqual(report.radical_rank, 0)
        self.assertEqual(report.exact_field_degree, 1)
        self.assertEqual(report.prime_basis, ())

    def test_one_nontrivial_radical_has_quadratic_degree(self):
        report = radical_field_complexity((1, 2))
        self.assertEqual(report.radical_rank, 1)
        self.assertEqual(report.exact_field_degree, 2)
        self.assertEqual(report.independent_radicand_witnesses, (2,))

    def test_two_three_six_have_only_two_independent_radicals(self):
        report = radical_field_complexity((2, 3, 6))
        self.assertEqual(report.prime_basis, (2, 3))
        self.assertEqual(report.radical_rank, 2)
        self.assertEqual(report.exact_field_degree, 4)
        self.assertEqual(len(report.independent_radicand_witnesses), 2)

    def test_full_squarefree_product_family_has_rank_three_not_seven(self):
        report = radical_field_complexity((1, 2, 3, 5, 6, 10, 15, 30))
        self.assertEqual(report.prime_basis, (2, 3, 5))
        self.assertEqual(report.radical_rank, 3)
        self.assertEqual(report.exact_field_degree, 8)

    def test_material_profile_can_require_multiple_quadratic_generators(self):
        # Return force (0,2,2,4) gives doubled return-work prefixes
        # 0,2,6,12, whose squarefree momentum radicals are 1,2,6,3.
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 2, 2, 4),
                returning=(0, 2, 2, 4),
                amplitude=4,
            )
        )
        report = material_radical_field_complexity(law)
        self.assertEqual(report.radicands_by_depth, (1, 2, 6, 3))
        self.assertEqual(report.radical_field.radical_rank, 2)
        self.assertEqual(report.radical_field.exact_field_degree, 4)
        self.assertEqual(report.algebraic_depth_count, 3)

    def test_square_slope_material_stays_rational_rank_zero(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=tuple(9 * k for k in range(8)),
                returning=tuple(4 * k for k in range(8)),
                amplitude=63,
            )
        )
        report = material_radical_field_complexity(law)
        self.assertEqual(report.radical_field.radical_rank, 0)
        self.assertEqual(report.radical_field.exact_field_degree, 1)
        self.assertEqual(set(report.radicands_by_depth), {1})

    def test_squarefree_validation_is_explicit(self):
        self.assertEqual(squarefree_prime_support(30), (2, 3, 5))
        with self.assertRaises(ValueError):
            squarefree_prime_support(12)
        with self.assertRaises(ValueError):
            radical_field_complexity(())


if __name__ == "__main__":
    unittest.main()
