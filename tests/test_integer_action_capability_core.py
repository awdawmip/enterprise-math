import unittest

from enterprise_math.integer_action_capability_basis import (
    INTEGER_MODULE,
    STATE_KERNEL,
    least_preserving_action_subset,
)
from enterprise_math.integer_action_capability_core import (
    action_capability_unavoidable_core,
)


class IntegerActionCapabilityCoreTests(unittest.TestCase):
    def test_unequal_minimal_basis_witness_has_empty_core_and_no_least_family(self):
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
        report = action_capability_unavoidable_core(
            actions,
            observation,
            mode=INTEGER_MODULE,
        )
        self.assertEqual(report.unavoidable_core, ())
        self.assertEqual(report.optional_actions, (0, 1, 2))
        self.assertFalse(report.core_preserves_full_precision)
        self.assertTrue(report.least_subset_nonexistence_certified)
        self.assertIsNone(report.unique_least_subset)
        self.assertIsNone(
            least_preserving_action_subset(
                actions,
                observation,
                mode=INTEGER_MODULE,
            )
        )

    def test_kernel_and_integer_module_can_have_different_unavoidable_cores(self):
        actions = (
            ((0, 1), (0, 0)),
            ((0, 2), (0, 0)),
        )
        observation = ((1, 0),)

        kernel = action_capability_unavoidable_core(
            actions,
            observation,
            mode=STATE_KERNEL,
        )
        module = action_capability_unavoidable_core(
            actions,
            observation,
            mode=INTEGER_MODULE,
        )

        self.assertEqual(kernel.unavoidable_core, ())
        self.assertFalse(kernel.core_preserves_full_precision)
        self.assertIsNone(kernel.unique_least_subset)

        self.assertEqual(module.unavoidable_core, (0,))
        self.assertTrue(module.core_preserves_full_precision)
        self.assertEqual(module.unique_least_subset, (0,))
        self.assertEqual(
            module.unique_least_subset,
            least_preserving_action_subset(
                actions,
                observation,
                mode=INTEGER_MODULE,
            ),
        )

    def test_serial_synergy_can_make_every_action_unavoidable(self):
        actions = (
            (
                (0, 1, 0),
                (0, 0, 0),
                (0, 0, 0),
            ),
            (
                (0, 0, 0),
                (0, 0, 1),
                (0, 0, 0),
            ),
        )
        observation = ((1, 0, 0),)
        for mode in (STATE_KERNEL, INTEGER_MODULE):
            report = action_capability_unavoidable_core(
                actions,
                observation,
                mode=mode,
            )
            self.assertEqual(report.unavoidable_core, (0, 1))
            self.assertEqual(report.optional_actions, ())
            self.assertTrue(report.core_preserves_full_precision)
            self.assertEqual(report.unique_least_subset, (0, 1))

    def test_full_current_observation_makes_empty_action_family_the_unique_least(self):
        actions = (
            ((1, 1), (0, 1)),
            ((0, 1), (1, 0)),
            ((2, 0), (0, 3)),
        )
        observation = ((1, 0), (0, 1))
        for mode in (STATE_KERNEL, INTEGER_MODULE):
            report = action_capability_unavoidable_core(
                actions,
                observation,
                mode=mode,
            )
            self.assertEqual(report.unavoidable_core, ())
            self.assertTrue(report.core_preserves_full_precision)
            self.assertEqual(report.unique_least_subset, ())

    def test_core_needs_only_one_leave_one_out_test_per_action(self):
        actions = (
            ((1, 0), (0, 1)),
            ((1, 1), (0, 1)),
            ((0, 1), (1, 0)),
            ((2, 0), (0, 2)),
        )
        report = action_capability_unavoidable_core(
            actions,
            ((1, 0),),
        )
        self.assertEqual(report.leave_one_out_tests, 4)

    def test_validation(self):
        with self.assertRaises(ValueError):
            action_capability_unavoidable_core((), ((1,),))
        with self.assertRaises(ValueError):
            action_capability_unavoidable_core(
                (((1,),),),
                ((1,),),
                mode="UNKNOWN",
            )


if __name__ == "__main__":
    unittest.main()
