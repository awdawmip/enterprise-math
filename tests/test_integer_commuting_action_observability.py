import unittest

from enterprise_math.integer_action_language_observability import (
    action_language_smith_profile,
)
from enterprise_math.integer_commuting_action_observability import (
    commuting_action_family,
    commuting_action_observability_bound_report,
    commuting_cayley_hamilton_horizon_bound,
)


class IntegerCommutingActionObservabilityTests(unittest.TestCase):
    def test_diagonal_commuting_family_stabilizes_by_k_times_n_minus_one(self):
        actions = (
            (
                (2, 0, 0),
                (0, 1, 0),
                (0, 0, -1),
            ),
            (
                (1, 0, 0),
                (0, 3, 0),
                (0, 0, 2),
            ),
        )
        observation = ((1, 1, 1),)
        self.assertTrue(commuting_action_family(actions))
        self.assertEqual(commuting_cayley_hamilton_horizon_bound(actions), 4)
        report = commuting_action_observability_bound_report(actions, observation)
        self.assertEqual(report.horizon_bound, 4)
        at_bound = action_language_smith_profile(actions, observation, 4)
        later = action_language_smith_profile(actions, observation, 8)
        self.assertEqual(at_bound.rational_rank, later.rational_rank)
        self.assertEqual(
            at_bound.smith_invariant_factors,
            later.smith_invariant_factors,
        )
        self.assertEqual(
            at_bound.maximal_nonzero_determinantal_divisor,
            later.maximal_nonzero_determinantal_divisor,
        )

    def test_commuting_nondiagonal_shear_family_obeys_bound(self):
        action_a = (
            (1, 1, 0),
            (0, 1, 0),
            (0, 0, 1),
        )
        action_b = (
            (1, 2, 0),
            (0, 1, 0),
            (0, 0, 1),
        )
        actions = (action_a, action_b)
        observation = ((1, 0, 1),)
        self.assertTrue(commuting_action_family(actions))
        bound = commuting_cayley_hamilton_horizon_bound(actions)
        self.assertEqual(bound, 4)
        at_bound = action_language_smith_profile(actions, observation, bound)
        for horizon in range(bound, bound + 5):
            later = action_language_smith_profile(actions, observation, horizon)
            self.assertEqual(later.rational_rank, at_bound.rational_rank)
            self.assertEqual(
                later.smith_invariant_factors,
                at_bound.smith_invariant_factors,
            )

    def test_single_action_reduces_to_n_minus_one_bound(self):
        action = (
            (0, 1, 0, 0),
            (0, 0, 1, 0),
            (0, 0, 0, 1),
            (1, 2, 3, 4),
        )
        self.assertTrue(commuting_action_family((action,)))
        self.assertEqual(
            commuting_cayley_hamilton_horizon_bound((action,)),
            3,
        )
        observation = ((1, 0, 0, 0),)
        at_bound = action_language_smith_profile((action,), observation, 3)
        later = action_language_smith_profile((action,), observation, 9)
        self.assertEqual(at_bound.rational_rank, later.rational_rank)
        self.assertEqual(
            at_bound.smith_invariant_factors,
            later.smith_invariant_factors,
        )

    def test_noncommuting_delayed_index_witness_is_outside_commuting_theorem(self):
        action_a = (
            (0, 1, 0),
            (0, 0, 0),
            (0, 0, 0),
        )
        action_b = (
            (0, 0, 2),
            (0, 0, 1),
            (0, 0, 0),
        )
        actions = (action_a, action_b)
        self.assertFalse(commuting_action_family(actions))
        with self.assertRaises(ValueError):
            commuting_cayley_hamilton_horizon_bound(actions)

        observation = ((1, 0, 0),)
        h1 = action_language_smith_profile(actions, observation, 1)
        h2 = action_language_smith_profile(actions, observation, 2)
        self.assertEqual(h1.rational_rank, h2.rational_rank)
        self.assertEqual(h1.maximal_nonzero_determinantal_divisor, 2)
        self.assertEqual(h2.maximal_nonzero_determinantal_divisor, 1)

    def test_repeated_identical_commuting_actions_keep_valid_but_nonminimal_bound(self):
        action = (
            (1, 1),
            (0, 1),
        )
        actions = (action, action, action)
        self.assertTrue(commuting_action_family(actions))
        self.assertEqual(commuting_cayley_hamilton_horizon_bound(actions), 3)
        observation = ((1, 0),)
        at_bound = action_language_smith_profile(actions, observation, 3)
        earlier = action_language_smith_profile(actions, observation, 1)
        later = action_language_smith_profile(actions, observation, 7)
        self.assertEqual(earlier.rational_rank, at_bound.rational_rank)
        self.assertEqual(
            at_bound.smith_invariant_factors,
            later.smith_invariant_factors,
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            commuting_action_family(())
        with self.assertRaises(ValueError):
            commuting_action_family((((1, 0),),))
        with self.assertRaises(TypeError):
            commuting_action_family((((1, False), (0, 1)),))


if __name__ == "__main__":
    unittest.main()
