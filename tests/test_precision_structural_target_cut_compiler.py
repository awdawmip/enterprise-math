import unittest

from enterprise_math.precision_structural_target_cut_compiler import (
    field_relative_cuts,
    minimal_target_cuts,
    target_defect_exponent,
    target_safe,
)


class StructuralTargetCutCompilerTests(unittest.TestCase):
    def test_mod_p_rank_can_miss_higher_padic_target(self):
        A = ((1, 1),)
        B = ((0, 2),)
        self.assertEqual(field_relative_cuts(A, B, 2), ())
        self.assertEqual(minimal_target_cuts(A, B, 2, 2), ((0, 1),))
        self.assertEqual(target_defect_exponent(A, B, (0, 1), 2, 2), 1)

    def test_padic_depth_family(self):
        K = 4
        A = ((1, 1),)
        for t in (1, 2, 3):
            B = ((0, 2 ** t),)
            self.assertEqual(minimal_target_cuts(A, B, 2, K), ((0, 1),))
            self.assertEqual(target_defect_exponent(A, B, (0, 1), 2, K), K - t)

    def test_field_relative_circuit_formula(self):
        A = ((0, 1, 1, 1),)
        B = ((0, 0, 0, 1),)
        expected = ((1, 3), (2, 3))
        self.assertEqual(field_relative_cuts(A, B, 2), expected)
        self.assertEqual(minimal_target_cuts(A, B, 2, 1), expected)

    def test_relative_cuts_need_not_be_matroid_circuits(self):
        A = ((0, 1, 1, 1),)
        B = ((0, 0, 0, 1),)
        cuts = set(field_relative_cuts(A, B, 2))
        self.assertIn((1, 3), cuts)
        self.assertIn((2, 3), cuts)
        self.assertNotIn((1, 2), cuts)

    def test_target_safety_is_monotone_under_more_resets(self):
        A = ((1, 1),)
        B = ((0, 2),)
        self.assertFalse(target_safe(A, B, (), 2, 2))
        self.assertTrue(target_safe(A, B, (0,), 2, 2))
        self.assertTrue(target_safe(A, B, (1,), 2, 2))
        self.assertTrue(target_safe(A, B, (0, 1), 2, 2))

    def test_exact_state_specialization_recovers_module_cut(self):
        A = ((1, 1, 0), (0, 1, 1))
        I = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        self.assertEqual(field_relative_cuts(A, I, 2), ((0, 1, 2),))
        self.assertEqual(minimal_target_cuts(A, I, 2, 1), ((0, 1, 2),))


if __name__ == "__main__":
    unittest.main()
