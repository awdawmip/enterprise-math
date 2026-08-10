import itertools
import unittest

from enterprise_math.integer_action_capability_basis import (
    INTEGER_MODULE,
    STATE_KERNEL,
    inclusion_minimal_action_subsets,
)
from enterprise_math.integer_action_capability_monotone_universality import (
    all_action_subsets,
    compile_monotone_capability_family,
    maximal_nonpreserving_subsets,
    normalize_upward_closed_family,
    sperner_maximal_minimal_family_count,
    upward_closure_of_antichain,
    verify_antichain_minimal_family_realization,
    verify_monotone_capability_compilation,
)


class IntegerActionCapabilityMonotoneUniversalityTests(unittest.TestCase):
    def test_arbitrary_small_upward_closed_family_is_realized_exactly(self):
        # Minimal true sets {0} and {1,2}; preserving family is their upward closure.
        family = upward_closure_of_antichain(3, ((0,), (1, 2)))
        compilation = compile_monotone_capability_family(3, tuple(family))
        self.assertTrue(verify_monotone_capability_compilation(compilation))
        self.assertEqual(
            set(compilation.maximal_false_subsets),
            {frozenset({1}), frozenset({2})},
        )
        for mode in (STATE_KERNEL, INTEGER_MODULE):
            self.assertEqual(
                inclusion_minimal_action_subsets(
                    compilation.action_matrices,
                    compilation.observation_rows,
                    mode=mode,
                ),
                ((0,), (1, 2)),
            )

    def test_every_two_of_four_actions_can_be_the_full_minimal_antichain(self):
        minimal = tuple(itertools.combinations(range(4), 2))
        self.assertEqual(len(minimal), 6)
        self.assertEqual(sperner_maximal_minimal_family_count(4), 6)
        self.assertTrue(
            verify_antichain_minimal_family_realization(4, minimal)
        )

    def test_sperner_middle_layer_counts(self):
        self.assertEqual(sperner_maximal_minimal_family_count(1), 1)
        self.assertEqual(sperner_maximal_minimal_family_count(2), 2)
        self.assertEqual(sperner_maximal_minimal_family_count(5), 10)
        self.assertEqual(sperner_maximal_minimal_family_count(6), 20)

    def test_trivial_all_preserving_family_compiles_to_already_complete_observation(self):
        family = all_action_subsets(3)
        compilation = compile_monotone_capability_family(3, family)
        self.assertTrue(compilation.trivial_all_preserving)
        self.assertEqual(compilation.maximal_false_subsets, ())
        self.assertTrue(verify_monotone_capability_compilation(compilation))
        for mode in (STATE_KERNEL, INTEGER_MODULE):
            self.assertEqual(
                inclusion_minimal_action_subsets(
                    compilation.action_matrices,
                    compilation.observation_rows,
                    mode=mode,
                ),
                ((),),
            )

    def test_maximal_false_sets_generate_monotone_cnf_boundary(self):
        # P(S) iff |S|>=2 on three actions.  Maximal false contexts are the
        # three singleton sets; every preserving S must escape all three.
        family = tuple(
            subset for subset in all_action_subsets(3) if len(subset) >= 2
        )
        maximal_false = maximal_nonpreserving_subsets(3, family)
        self.assertEqual(
            set(maximal_false),
            {frozenset({0}), frozenset({1}), frozenset({2})},
        )
        compilation = compile_monotone_capability_family(3, family)
        self.assertTrue(verify_monotone_capability_compilation(compilation))

    def test_validation(self):
        with self.assertRaises(ValueError):
            normalize_upward_closed_family(2, ())
        with self.assertRaises(ValueError):
            normalize_upward_closed_family(2, ((0,), (0, 1)))
        with self.assertRaises(ValueError):
            upward_closure_of_antichain(3, ((0,), (0, 1)))
        with self.assertRaises(ValueError):
            compile_monotone_capability_family(0, ((),))


if __name__ == "__main__":
    unittest.main()
