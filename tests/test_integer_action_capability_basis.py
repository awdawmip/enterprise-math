import unittest

from enterprise_math.integer_action_capability_basis import (
    INTEGER_MODULE,
    STATE_KERNEL,
    action_capability_basis_report,
    action_subset_final_basis,
    action_subset_preserves,
    greedy_redundant_action_deletion,
    inclusion_minimal_action_subsets,
    least_preserving_action_subset,
    preserving_action_subsets,
)


class IntegerActionCapabilityBasisTests(unittest.TestCase):
    def test_generic_minimal_action_families_can_have_unequal_cardinalities(self):
        action_a = (
            (0, 1, 0),
            (0, 0, 1),
            (0, 0, 0),
        )
        action_b = (
            (0, 1, 0),
            (0, 0, 0),
            (0, 0, 0),
        )
        action_c = (
            (0, 0, 1),
            (0, 0, 0),
            (0, 0, 0),
        )
        actions = (action_a, action_b, action_c)
        observation = ((1, 0, 0),)

        report = action_capability_basis_report(actions, observation)
        self.assertEqual(
            report.minimal_integer_module_subsets,
            ((0,), (1, 2)),
        )
        self.assertEqual(report.integer_module_minimal_cardinalities, (1, 2))
        self.assertTrue(report.unequal_integer_module_minimal_cardinalities)
        self.assertIsNone(report.least_integer_module_subset)
        self.assertEqual(
            report.individually_integer_module_redundant_actions,
            (0, 1, 2),
        )

    def test_greedy_deletion_of_locally_redundant_actions_is_order_dependent(self):
        actions = (
            (
                (0, 1, 0),
                (0, 0, 1),
                (0, 0, 0),
            ),
            (
                (0, 1, 0),
                (0, 0, 0),
                (0, 0, 0),
            ),
            (
                (0, 0, 1),
                (0, 0, 0),
                (0, 0, 0),
            ),
        )
        observation = ((1, 0, 0),)
        self.assertEqual(
            greedy_redundant_action_deletion(
                actions,
                observation,
                (0, 1, 2),
                mode=INTEGER_MODULE,
            ),
            (1, 2),
        )
        self.assertEqual(
            greedy_redundant_action_deletion(
                actions,
                observation,
                (1, 2, 0),
                mode=INTEGER_MODULE,
            ),
            (0,),
        )

    def test_state_kernel_redundancy_is_weaker_than_integer_module_redundancy(self):
        action_a = (
            (0, 1),
            (0, 0),
        )
        action_b = (
            (0, 2),
            (0, 0),
        )
        actions = (action_a, action_b)
        observation = ((1, 0),)

        # Keeping only B still reaches full rational rank but only sees 2*e2.
        self.assertTrue(
            action_subset_preserves(
                actions,
                observation,
                (1,),
                mode=STATE_KERNEL,
            )
        )
        self.assertFalse(
            action_subset_preserves(
                actions,
                observation,
                (1,),
                mode=INTEGER_MODULE,
            )
        )
        self.assertEqual(
            action_subset_final_basis(actions, observation, (1,)),
            ((1, 0), (0, 2)),
        )
        self.assertEqual(
            action_subset_final_basis(actions, observation, (0,)),
            ((1, 0), (0, 1)),
        )

        report = action_capability_basis_report(actions, observation)
        self.assertEqual(
            report.minimal_kernel_preserving_subsets,
            ((0,), (1,)),
        )
        self.assertEqual(
            report.minimal_integer_module_subsets,
            ((0,),),
        )
        self.assertIsNone(report.least_kernel_subset)
        self.assertEqual(report.least_integer_module_subset, (0,))
        self.assertEqual(report.individually_kernel_redundant_actions, (0, 1))
        self.assertEqual(report.individually_integer_module_redundant_actions, (1,))

    def test_preserving_subset_family_is_upward_closed_at_both_levels(self):
        actions = (
            ((0, 1), (0, 0)),
            ((0, 2), (0, 0)),
            ((1, 0), (0, 1)),
        )
        observation = ((1, 0),)
        for mode in (STATE_KERNEL, INTEGER_MODULE):
            preserving = preserving_action_subsets(
                actions,
                observation,
                mode=mode,
            )
            preserving_sets = {frozenset(subset) for subset in preserving}
            for subset in preserving_sets:
                for candidate in preserving_sets:
                    if subset.issubset(candidate):
                        self.assertIn(candidate, preserving_sets)
            minimal = inclusion_minimal_action_subsets(
                actions,
                observation,
                mode=mode,
            )
            for subset in preserving:
                self.assertTrue(
                    any(set(base).issubset(subset) for base in minimal)
                )

    def test_zero_observation_language_has_empty_least_action_family(self):
        actions = (
            ((1, 1), (0, 1)),
            ((0, 1), (1, 0)),
        )
        observation = ((0, 0),)
        for mode in (STATE_KERNEL, INTEGER_MODULE):
            self.assertEqual(
                least_preserving_action_subset(
                    actions,
                    observation,
                    mode=mode,
                ),
                (),
            )
            self.assertEqual(
                inclusion_minimal_action_subsets(
                    actions,
                    observation,
                    mode=mode,
                ),
                ((),),
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            action_subset_final_basis((), ((1,),), ())
        with self.assertRaises(ValueError):
            preserving_action_subsets(
                (((1,),),),
                ((1,),),
                mode="UNKNOWN",
            )
        with self.assertRaises(ValueError):
            greedy_redundant_action_deletion(
                (((1,),), ((1,),)),
                ((1,),),
                (0, 0),
            )


if __name__ == "__main__":
    unittest.main()
