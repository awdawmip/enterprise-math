import unittest

from enterprise_math.integer_action_capability_basis import (
    INTEGER_MODULE,
    STATE_KERNEL,
    preserving_action_subsets,
)
from enterprise_math.integer_action_capability_search import (
    minimum_action_capability_subsets,
)


def brute_force_minimum(actions, observation, mode):
    preserving = preserving_action_subsets(
        actions,
        observation,
        mode=mode,
    )
    minimum = min(map(len, preserving))
    return minimum, tuple(
        subset for subset in preserving if len(subset) == minimum
    )


class IntegerActionCapabilitySearchTests(unittest.TestCase):
    def test_branch_and_bound_matches_bruteforce_on_unequal_minimal_basis_witness(self):
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
        for mode in (STATE_KERNEL, INTEGER_MODULE):
            expected_size, expected_subsets = brute_force_minimum(
                actions,
                observation,
                mode,
            )
            report = minimum_action_capability_subsets(
                actions,
                observation,
                mode=mode,
            )
            self.assertEqual(report.minimum_cardinality, expected_size)
            self.assertEqual(report.minimum_subsets, expected_subsets)
            self.assertEqual(report.unavoidable_core, ())
            self.assertGreater(report.impossible_extension_prunes, 0)
        self.assertEqual(
            minimum_action_capability_subsets(
                actions,
                observation,
                mode=INTEGER_MODULE,
            ).minimum_subsets,
            ((0,),),
        )

    def test_kernel_and_integer_module_search_return_different_optima_and_cores(self):
        actions = (
            ((0, 1), (0, 0)),
            ((0, 2), (0, 0)),
        )
        observation = ((1, 0),)

        kernel = minimum_action_capability_subsets(
            actions,
            observation,
            mode=STATE_KERNEL,
        )
        module = minimum_action_capability_subsets(
            actions,
            observation,
            mode=INTEGER_MODULE,
        )
        self.assertEqual(kernel.minimum_cardinality, 1)
        self.assertEqual(kernel.minimum_subsets, ((0,), (1,)))
        self.assertEqual(kernel.unavoidable_core, ())

        self.assertEqual(module.minimum_cardinality, 1)
        self.assertEqual(module.minimum_subsets, ((0,),))
        self.assertEqual(module.unavoidable_core, (0,))
        self.assertEqual(module.optional_actions, (1,))
        self.assertEqual(module.core_reduced_subset_count, 2)

    def test_full_current_observation_prunes_entire_action_search_at_root(self):
        actions = (
            ((1, 1), (0, 1)),
            ((0, 1), (1, 0)),
            ((2, 0), (0, 3)),
            ((1, -1), (1, 1)),
        )
        observation = ((1, 0), (0, 1))
        for mode in (STATE_KERNEL, INTEGER_MODULE):
            report = minimum_action_capability_subsets(
                actions,
                observation,
                mode=mode,
            )
            self.assertEqual(report.minimum_cardinality, 0)
            self.assertEqual(report.minimum_subsets, ((),))
            self.assertEqual(report.unavoidable_core, ())
            self.assertEqual(report.visited_nodes, 1)
            self.assertEqual(report.preserving_node_prunes, 1)
            self.assertTrue(report.oracle_avoided_full_original_enumeration)

    def test_unavoidable_core_can_remove_every_search_dimension(self):
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
        report = minimum_action_capability_subsets(
            actions,
            ((1, 0, 0),),
            mode=STATE_KERNEL,
        )
        self.assertEqual(report.unavoidable_core, (0, 1))
        self.assertEqual(report.optional_actions, ())
        self.assertEqual(report.core_reduced_subset_count, 1)
        self.assertEqual(report.minimum_subsets, ((0, 1),))
        self.assertEqual(report.visited_nodes, 1)

    def test_exact_search_can_still_have_exponential_worst_case_boundary(self):
        # This regression does not assert a complexity theorem.  It only locks
        # the explicit 2^k comparison surface rather than pretending pruning is
        # always effective.
        actions = (
            ((0, 1), (0, 0)),
            ((0, 1), (0, 0)),
            ((0, 1), (0, 0)),
        )
        report = minimum_action_capability_subsets(
            actions,
            ((1, 0),),
            mode=INTEGER_MODULE,
        )
        self.assertEqual(report.full_subset_count, 8)
        self.assertEqual(report.core_reduced_subset_count, 8)
        self.assertEqual(report.minimum_cardinality, 1)
        self.assertEqual(report.minimum_subsets, ((0,), (1,), (2,)))

    def test_validation(self):
        with self.assertRaises(ValueError):
            minimum_action_capability_subsets((), ((1,),))
        with self.assertRaises(ValueError):
            minimum_action_capability_subsets(
                (((1,),),),
                ((1,),),
                mode="UNKNOWN",
            )


if __name__ == "__main__":
    unittest.main()
