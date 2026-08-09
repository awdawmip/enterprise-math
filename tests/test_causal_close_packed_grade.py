import unittest

from enterprise_math.causal_close_packed_grade import (
    enumerate_domain_wall_spectrum,
    fcc_like_layer_count,
    hcp_like_layer_count,
    local_421_bond_count,
    local_422_bond_count,
    stacking_domain_wall_spectrum,
    stacking_grade,
    stacking_grade_spectrum,
    stacking_pascal_recurrence,
    stacking_word_count,
)


class CausalClosePackedGradeTests(unittest.TestCase):
    def test_fcc_and_hcp_are_extreme_trajectories_of_one_sign_language(self):
        fcc = (1, 1, 1, 1, 1)
        hcp = (1, -1, 1, -1, 1)
        self.assertEqual(hcp_like_layer_count(fcc), 0)
        self.assertEqual(fcc_like_layer_count(fcc), 4)
        self.assertEqual(hcp_like_layer_count(hcp), 4)
        self.assertEqual(fcc_like_layer_count(hcp), 0)
        self.assertEqual(local_422_bond_count(fcc), 0)
        self.assertEqual(local_422_bond_count(hcp), 24)
        self.assertEqual(local_421_bond_count(fcc), 48)
        self.assertEqual(local_421_bond_count(hcp), 24)

    def test_domain_wall_multiplicity_is_exact_binomial_spectrum(self):
        for length in range(1, 10):
            closed = stacking_domain_wall_spectrum(length)
            brute = enumerate_domain_wall_spectrum(length)
            self.assertEqual(closed, brute)
            self.assertEqual(sum(closed), stacking_word_count(length))
            self.assertEqual(closed[0], 2)
            self.assertEqual(closed[-1], 2)

    def test_one_layer_lift_has_pascal_shadow(self):
        for length in range(2, 10):
            for walls in range(length):
                self.assertTrue(stacking_pascal_recurrence(length, walls))

    def test_integer_material_grade_is_read_from_same_continuation_word(self):
        signs = (1, 1, -1, -1, 1)
        self.assertEqual(hcp_like_layer_count(signs), 2)
        self.assertEqual(fcc_like_layer_count(signs), 2)
        self.assertEqual(stacking_grade(signs, fcc_like_grade=3, hcp_like_grade=7), 20)

    def test_grade_spectrum_aggregates_equal_integer_grades_without_probability(self):
        spectrum = stacking_grade_spectrum(5, fcc_like_grade=0, hcp_like_grade=6)
        self.assertEqual(spectrum, {0: 2, 6: 8, 12: 12, 18: 8, 24: 2})
        self.assertEqual(sum(spectrum.values()), 32)


if __name__ == "__main__":
    unittest.main()
