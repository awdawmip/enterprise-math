import unittest

from enterprise_math.witness_quantifier_order import (
    add_joint_support,
    missing_pairwise_lcm_refinements,
    verify_present_lcm_refinements,
    witness_quantifier_report,
)


class WitnessQuantifierOrderTests(unittest.TestCase):
    def test_prime_only_local_witnesses_need_not_have_one_common_label(self):
        supports = {
            2: {"A"},
            3: {"B"},
        }
        report = witness_quantifier_report(supports)
        self.assertTrue(report.every_precision_has_witness)
        self.assertFalse(report.one_witness_survives_every_precision)
        self.assertTrue(report.forall_exists_but_not_exists_forall)
        self.assertEqual(report.common_witnesses, frozenset())
        self.assertEqual(missing_pairwise_lcm_refinements(supports), (6,))

    def test_joint_lcm_precision_exposes_incompatible_local_labels(self):
        report = add_joint_support(
            {
                2: {"A"},
                3: {"B"},
            },
            2,
            3,
            set(),
        )
        self.assertFalse(report.every_precision_has_witness)
        self.assertFalse(report.one_witness_survives_every_precision)
        self.assertIn((6, frozenset()), report.supports)

    def test_common_label_survives_directed_refinement(self):
        supports = {
            2: {"A", "B"},
            3: {"A", "C"},
            6: {"A"},
            12: {"A"},
        }
        self.assertTrue(verify_present_lcm_refinements(supports))
        report = witness_quantifier_report(supports)
        self.assertTrue(report.every_precision_has_witness)
        self.assertEqual(report.common_witnesses, frozenset({"A"}))
        self.assertTrue(report.one_witness_survives_every_precision)

    def test_joint_support_cannot_create_new_label(self):
        with self.assertRaises(ValueError):
            add_joint_support(
                {
                    2: {"A"},
                    3: {"B"},
                },
                2,
                3,
                {"C"},
            )

    def test_present_joint_support_violation_is_rejected(self):
        with self.assertRaises(AssertionError):
            verify_present_lcm_refinements(
                {
                    2: {"A"},
                    3: {"B"},
                    6: {"A"},
                }
            )

    def test_empty_local_support_breaks_forall_exists_even_if_other_precisions_have_witnesses(self):
        report = witness_quantifier_report(
            {
                2: {"A", "B"},
                4: set(),
            }
        )
        self.assertFalse(report.every_precision_has_witness)
        self.assertFalse(report.one_witness_survives_every_precision)
        self.assertFalse(report.forall_exists_but_not_exists_forall)

    def test_validation(self):
        with self.assertRaises(ValueError):
            witness_quantifier_report({})
        with self.assertRaises(ValueError):
            witness_quantifier_report({0: {"A"}})
        with self.assertRaises(TypeError):
            witness_quantifier_report({True: {"A"}})
        with self.assertRaises(ValueError):
            add_joint_support({2: {"A"}}, 2, 3, set())


if __name__ == "__main__":
    unittest.main()
