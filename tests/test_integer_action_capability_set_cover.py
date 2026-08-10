import itertools
import unittest

from enterprise_math.integer_action_capability_basis import (
    INTEGER_MODULE,
    STATE_KERNEL,
    inclusion_minimal_action_subsets,
)
from enterprise_math.integer_action_capability_core import (
    action_capability_unavoidable_core,
)
from enterprise_math.integer_action_capability_search import (
    minimum_action_capability_subsets,
)
from enterprise_math.integer_action_capability_set_cover import (
    selected_sets_cover_universe,
    set_cover_action_capability_report,
    set_cover_action_matrices,
    set_cover_actions_commute_and_are_idempotent,
    set_cover_observation_rows,
    verify_set_cover_capability_equivalence,
)


class IntegerActionCapabilitySetCoverTests(unittest.TestCase):
    def test_every_subset_matches_cover_kernel_and_integer_module_exactly(self):
        universe_size = 4
        sets = (
            {0, 1},
            {2, 3},
            {0, 2},
            {1, 3},
        )
        for size in range(len(sets) + 1):
            for subset in itertools.combinations(range(len(sets)), size):
                self.assertTrue(
                    verify_set_cover_capability_equivalence(
                        universe_size,
                        sets,
                        subset,
                    )
                )

    def test_compiled_actions_are_pairwise_commuting_idempotent_zero_one_matrices(self):
        sets = ({0, 2}, {1, 2}, {0, 1})
        actions = set_cover_action_matrices(3, sets)
        self.assertTrue(set_cover_actions_commute_and_are_idempotent(3, sets))
        for action in actions:
            self.assertTrue(all(value in (0, 1) for row in action for value in row))

    def test_unequal_minimal_set_covers_become_unequal_minimal_action_families(self):
        # {A} and {B,C} are the two inclusion-minimal covers.
        sets = (
            {0, 1, 2},
            {0, 1},
            {2},
        )
        actions = set_cover_action_matrices(3, sets)
        observations = set_cover_observation_rows(3)
        for mode in (STATE_KERNEL, INTEGER_MODULE):
            self.assertEqual(
                inclusion_minimal_action_subsets(
                    actions,
                    observations,
                    mode=mode,
                ),
                ((0,), (1, 2)),
            )
            minimum = minimum_action_capability_subsets(
                actions,
                observations,
                mode=mode,
            )
            self.assertEqual(minimum.minimum_cardinality, 1)
            self.assertEqual(minimum.minimum_subsets, ((0,),))

    def test_unavoidable_action_core_matches_sets_with_private_elements(self):
        sets = (
            {0, 1},
            {1, 2},
            {1},
        )
        actions = set_cover_action_matrices(3, sets)
        observations = set_cover_observation_rows(3)
        for mode in (STATE_KERNEL, INTEGER_MODULE):
            core = action_capability_unavoidable_core(
                actions,
                observations,
                mode=mode,
            )
            self.assertEqual(core.unavoidable_core, (0, 1))
            self.assertEqual(core.optional_actions, (2,))
            self.assertTrue(core.core_preserves_full_precision)
            self.assertEqual(core.unique_least_subset, (0, 1))

    def test_full_family_must_cover_universe_for_equivalence_verifier(self):
        with self.assertRaises(ValueError):
            verify_set_cover_capability_equivalence(
                3,
                ({0}, {1}),
                (0, 1),
            )

    def test_report_and_cover_validation(self):
        sets = ({0, 1}, {1, 2})
        report = set_cover_action_capability_report(3, sets)
        self.assertTrue(report.full_family_covers_universe)
        self.assertTrue(report.compiled_actions_commute_and_are_idempotent)
        self.assertFalse(selected_sets_cover_universe(3, sets, (0,)))
        self.assertTrue(selected_sets_cover_universe(3, sets, (0, 1)))

    def test_validation(self):
        with self.assertRaises(ValueError):
            set_cover_observation_rows(0)
        with self.assertRaises(ValueError):
            set_cover_action_matrices(2, ())
        with self.assertRaises(ValueError):
            set_cover_action_matrices(2, ({2},))
        with self.assertRaises(ValueError):
            selected_sets_cover_universe(2, ({0}, {1}), (0, 0))


if __name__ == "__main__":
    unittest.main()
