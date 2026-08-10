import unittest

from enterprise_math.coefficient_branch_mixing import (
    CONSTANTS,
    branch_blocker_moduli,
    labelled_branch_has_root_modulus,
    product_zero_modulus,
)
from enterprise_math.finite_branch_descent import (
    blocker_lcm,
    branch_support_at_modulus,
    branch_support_descends_under_divisibility,
    finite_branch_blocker_report,
    finite_branch_survival_theorem_statement,
)


def ghost_branch_solver(label, modulus):
    return labelled_branch_has_root_modulus(label, modulus)


class FiniteBranchDescentTests(unittest.TestCase):
    def test_ghost_blockers_collapse_to_mod15_branch_reflection_failure(self):
        blockers = dict(branch_blocker_moduli())
        report = finite_branch_blocker_report(
            blockers,
            ghost_branch_solver,
            unlabelled_solver=lambda modulus: any(
                product_zero_modulus(value, modulus)
                for value in range(modulus)
            ),
        )
        self.assertEqual(report.joint_modulus, 15)
        self.assertEqual(report.joint_branch_support, frozenset())
        self.assertTrue(report.every_label_blocked)
        self.assertTrue(report.unlabelled_locally_solvable)
        self.assertTrue(report.branch_reflection_failure)

    def test_joint_modulus_has_no_labelled_branch_but_product_root(self):
        support = branch_support_at_modulus(
            CONSTANTS,
            15,
            ghost_branch_solver,
        )
        self.assertEqual(support, frozenset())
        self.assertTrue(any(product_zero_modulus(value, 15) for value in range(15)))

    def test_branch_support_is_monotone_under_divisibility_for_real_branch_equations(self):
        pairs = (
            (2, 4),
            (3, 15),
            (5, 15),
            (3, 9),
            (13, 13 * 17),
        )
        for coarse, fine in pairs:
            self.assertTrue(
                branch_support_descends_under_divisibility(
                    CONSTANTS,
                    coarse,
                    fine,
                    ghost_branch_solver,
                )
            )

    def test_lcm_of_any_declared_blocker_per_label_blocks_all_labels(self):
        blockers = {13: 5, 17: 3, 221: 3}
        self.assertEqual(blocker_lcm(blockers), 15)
        for label, blocker in blockers.items():
            self.assertFalse(ghost_branch_solver(label, blocker))
            self.assertFalse(ghost_branch_solver(label, 15))

    def test_positive_abstract_branch_family_has_one_label_surviving_every_checked_precision(self):
        labels = ("even", "multiple3")

        def solver(label, modulus):
            # The "even" branch is deliberately solvable at every modulus;
            # the other branch is allowed to disappear.  This locks the set-level
            # support interpretation without importing polynomial structure.
            if label == "even":
                return True
            if label == "multiple3":
                return modulus % 2 == 1
            raise AssertionError("unknown label")

        for modulus in (1, 2, 3, 4, 6, 12, 30):
            support = branch_support_at_modulus(labels, modulus, solver)
            self.assertIn("even", support)
            self.assertTrue(support)

    def test_theorem_statement_is_explicit_about_fixed_finite_labels_and_all_moduli(self):
        statement = finite_branch_survival_theorem_statement()
        self.assertIn("fixed finite labelled branch family", statement)
        self.assertIn("every positive modulus", statement)
        self.assertIn("one fixed label", statement)

    def test_validation(self):
        with self.assertRaises(ValueError):
            blocker_lcm({})
        with self.assertRaises(ValueError):
            branch_support_at_modulus((), 2, ghost_branch_solver)
        with self.assertRaises(ValueError):
            branch_support_at_modulus((13, 13), 2, ghost_branch_solver)
        with self.assertRaises(ValueError):
            finite_branch_blocker_report(
                {13: 13},
                ghost_branch_solver,
            )
        with self.assertRaises(ValueError):
            branch_support_descends_under_divisibility(
                CONSTANTS,
                4,
                6,
                ghost_branch_solver,
            )


if __name__ == "__main__":
    unittest.main()
