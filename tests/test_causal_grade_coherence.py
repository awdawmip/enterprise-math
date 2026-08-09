import unittest

from enterprise_math.causal_grade_coherence import (
    base_carry_law,
    fold_residues_and_carry,
    grade_associativity_defect,
    grade_shift_is_coherent,
    regrade_pair_shift,
)


class CausalGradeCoherenceTests(unittest.TestCase):
    def test_binary_carry_is_bracket_independent(self):
        types, operation, carry = base_carry_law(2)
        self.assertTrue(grade_shift_is_coherent(types, operation, carry))
        self.assertEqual(grade_associativity_defect(types, operation, carry), {})

    def test_base_carry_is_coherent_for_multiple_bases(self):
        for base in range(2, 9):
            types, operation, carry = base_carry_law(base)
            self.assertTrue(grade_shift_is_coherent(types, operation, carry))

    def test_fold_reconstructs_exact_integer_sum(self):
        cases = (
            (2, (1, 1, 1, 1)),
            (3, (2, 2, 1, 0, 2)),
            (5, (4, 4, 4, 1)),
            (7, (6, 3, 5, 1, 2)),
        )
        for base, values in cases:
            residue, carry = fold_residues_and_carry(values, base)
            self.assertEqual(sum(values), residue + base * carry)

    def test_type_baseline_regrading_preserves_three_body_defect(self):
        types, operation, carry = base_carry_law(4)
        baseline = {0: 3, 1: -2, 2: 5, 3: 1}
        regraded = regrade_pair_shift(types, operation, carry, baseline)
        self.assertEqual(
            grade_associativity_defect(types, operation, carry),
            grade_associativity_defect(types, operation, regraded),
        )
        self.assertTrue(grade_shift_is_coherent(types, operation, regraded))

    def test_incoherent_pair_grade_requires_three_body_compatibility_detail(self):
        types = (0, 1)
        operation = {
            (left, right): left ^ right
            for left in types
            for right in types
        }
        bad_grade = {
            (0, 0): 0,
            (0, 1): 0,
            (1, 0): 0,
            (1, 1): 2,
        }
        defect = grade_associativity_defect(types, operation, bad_grade)
        self.assertTrue(defect)
        self.assertFalse(grade_shift_is_coherent(types, operation, bad_grade))

    def test_binary_carry_is_pair_interaction_not_new_unit_value(self):
        types, operation, carry = base_carry_law(2)
        self.assertEqual(operation[(1, 1)], 0)
        self.assertEqual(carry[(1, 1)], 1)
        # The exact sum 1+1=2 is represented as residue 0 plus one base-2 carry.
        self.assertEqual(operation[(1, 1)] + 2 * carry[(1, 1)], 2)


if __name__ == "__main__":
    unittest.main()
