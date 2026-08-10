import unittest

from enterprise_math.integer_action_capability_synergy import (
    action_marginal_state_rank_gain,
    action_subset_state_rank,
    first_rank_submodularity_violation,
    state_rank_is_monotone_over_action_subsets,
)


class IntegerActionCapabilitySynergyTests(unittest.TestCase):
    def test_sharp_compositional_synergy_violates_submodularity(self):
        action_a = (
            (0, 1, 0),
            (0, 0, 0),
            (0, 0, 0),
        )
        action_b = (
            (0, 0, 0),
            (0, 0, 1),
            (0, 0, 0),
        )
        actions = (action_a, action_b)
        observation = ((1, 0, 0),)

        self.assertEqual(action_subset_state_rank(actions, observation, ()), 1)
        self.assertEqual(action_subset_state_rank(actions, observation, (0,)), 2)
        self.assertEqual(action_subset_state_rank(actions, observation, (1,)), 1)
        self.assertEqual(action_subset_state_rank(actions, observation, (0, 1)), 3)

        self.assertEqual(
            action_marginal_state_rank_gain(actions, observation, (), 0),
            1,
        )
        self.assertEqual(
            action_marginal_state_rank_gain(actions, observation, (1,), 0),
            2,
        )
        self.assertEqual(
            action_marginal_state_rank_gain(actions, observation, (), 1),
            0,
        )
        self.assertEqual(
            action_marginal_state_rank_gain(actions, observation, (0,), 1),
            1,
        )

        violation = first_rank_submodularity_violation(actions, observation)
        self.assertIsNotNone(violation)
        assert violation is not None
        self.assertLess(violation.gain_on_smaller, violation.gain_on_larger)
        self.assertTrue(state_rank_is_monotone_over_action_subsets(actions, observation))

    def test_independent_coordinate_actions_have_no_submodularity_violation(self):
        actions = (
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
        self.assertIsNone(
            first_rank_submodularity_violation(actions, observation)
        )
        self.assertTrue(state_rank_is_monotone_over_action_subsets(actions, observation))

    def test_added_existing_action_has_zero_marginal_gain(self):
        action = (
            (0, 1),
            (0, 0),
        )
        self.assertEqual(
            action_marginal_state_rank_gain(
                (action,),
                ((1, 0),),
                (0,),
                0,
            ),
            0,
        )


if __name__ == "__main__":
    unittest.main()
