import unittest
from itertools import product

from enterprise_math.integer_action_language_observability import (
    action_language_closure_report,
    action_language_observation_rows,
    action_language_smith_profile,
    prime_factor_multiplicity,
)
from enterprise_math.integer_future_observability import integer_matrix_rank


class IntegerActionLanguageObservabilityTests(unittest.TestCase):
    def test_minimal_multi_action_rank_full_then_index_two_to_one(self):
        observation = ((1, 0, 0),)
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

        h0 = action_language_smith_profile(actions, observation, 0)
        h1 = action_language_smith_profile(actions, observation, 1)
        h2 = action_language_smith_profile(actions, observation, 2)
        self.assertEqual((h0.rational_rank, h1.rational_rank, h2.rational_rank), (1, 3, 3))
        self.assertEqual(h1.smith_invariant_factors, (1, 1, 2))
        self.assertEqual(h2.smith_invariant_factors, (1, 1, 1))
        self.assertEqual(h1.maximal_nonzero_determinantal_divisor, 2)
        self.assertEqual(h2.maximal_nonzero_determinantal_divisor, 1)

        rows1 = set(action_language_observation_rows(actions, observation, 1))
        rows2 = set(action_language_observation_rows(actions, observation, 2))
        self.assertIn((1, 0, 0), rows1)
        self.assertIn((0, 1, 0), rows1)
        self.assertIn((0, 0, 2), rows1)
        self.assertNotIn((0, 0, 1), rows1)
        self.assertIn((0, 0, 1), rows2)  # C A B

        report = action_language_closure_report(actions, observation)
        self.assertEqual(report.rational_stabilization_horizon, 1)
        self.assertEqual(report.rational_stabilization_index, 2)
        self.assertEqual(report.arithmetic_refinement_bound, 1)
        self.assertEqual(report.final_lattice_attainment_bound, 2)
        self.assertEqual(report.exact_integer_stabilization_horizon, 2)
        self.assertTrue(report.delayed_integer_refinement_after_rational_stability)

    def test_index_four_can_drop_directly_to_one_before_omega_bound(self):
        observation = ((1, 0, 0),)
        action_a = (
            (0, 1, 0),
            (0, 0, 0),
            (0, 0, 0),
        )
        action_b = (
            (0, 0, 4),
            (0, 0, 1),
            (0, 0, 0),
        )
        actions = (action_a, action_b)
        h1 = action_language_smith_profile(actions, observation, 1)
        h2 = action_language_smith_profile(actions, observation, 2)
        self.assertEqual(h1.maximal_nonzero_determinantal_divisor, 4)
        self.assertEqual(h2.maximal_nonzero_determinantal_divisor, 1)
        self.assertEqual(prime_factor_multiplicity(4), 2)

        report = action_language_closure_report(actions, observation)
        self.assertEqual(report.rational_stabilization_horizon, 1)
        self.assertEqual(report.rational_stabilization_index, 4)
        self.assertEqual(report.arithmetic_refinement_bound, 2)
        self.assertEqual(report.final_lattice_attainment_bound, 3)
        self.assertEqual(report.exact_integer_stabilization_horizon, 2)
        self.assertLess(
            report.exact_integer_stabilization_horizon,
            report.final_lattice_attainment_bound,
        )

    def test_single_action_integer_power_module_stabilizes_by_dimension_minus_one(self):
        examples = (
            (
                ((1, 0, 0),),
                (
                    (0, 1, 0),
                    (0, 0, 1),
                    (1, 1, 1),
                ),
            ),
            (
                ((1, 1, 0),),
                (
                    (1, 1, 0),
                    (0, 1, 1),
                    (1, 0, 1),
                ),
            ),
            (
                ((2, 1, -1),),
                (
                    (2, 0, 1),
                    (1, 1, 0),
                    (0, 1, 1),
                ),
            ),
        )
        for observation, action in examples:
            dimension = len(action)
            rows_bound = action_language_observation_rows(
                (action,),
                observation,
                dimension - 1,
            )
            rows_later = action_language_observation_rows(
                (action,),
                observation,
                dimension + 3,
            )
            # Cayley-Hamilton says the later rows lie in the Z-lattice generated
            # by the first n powers.  The Smith profile and rank must therefore
            # already be stable even if the literal row sets contain new vectors.
            profile_bound = action_language_smith_profile(
                (action,),
                observation,
                dimension - 1,
            )
            profile_later = action_language_smith_profile(
                (action,),
                observation,
                dimension + 3,
            )
            self.assertEqual(profile_bound.rational_rank, profile_later.rational_rank)
            self.assertEqual(
                profile_bound.smith_invariant_factors,
                profile_later.smith_invariant_factors,
            )
            self.assertGreaterEqual(len(rows_later), len(rows_bound))
            report = action_language_closure_report((action,), observation)
            self.assertLessEqual(report.exact_integer_stabilization_horizon, dimension - 1)

    def test_first_equal_rank_step_is_permanent_rational_plateau(self):
        action_sets = (
            (
                (
                    (0, 1, 0),
                    (0, 0, 0),
                    (0, 0, 0),
                ),
                (
                    (0, 0, 2),
                    (0, 0, 1),
                    (0, 0, 0),
                ),
            ),
            (
                (
                    (1, 1, 0),
                    (0, 1, 1),
                    (0, 0, 1),
                ),
                (
                    (1, 0, 1),
                    (1, 1, 0),
                    (0, 1, 1),
                ),
            ),
        )
        for actions in action_sets:
            observation = ((1, 0, 0),)
            ranks = [
                action_language_smith_profile(actions, observation, horizon).rational_rank
                for horizon in range(7)
            ]
            plateau = next(
                index
                for index in range(len(ranks) - 1)
                if ranks[index] == ranks[index + 1]
            )
            self.assertTrue(all(rank == ranks[plateau] for rank in ranks[plateau:]))

    def test_first_equal_rank_and_index_step_is_permanent_integer_plateau(self):
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
        observation = ((1, 0, 0),)
        profiles = [
            action_language_smith_profile(actions, observation, horizon)
            for horizon in range(7)
        ]
        plateau = next(
            index
            for index in range(len(profiles) - 1)
            if profiles[index].rational_rank == profiles[index + 1].rational_rank
            and profiles[index].maximal_nonzero_determinantal_divisor
            == profiles[index + 1].maximal_nonzero_determinantal_divisor
        )
        for profile in profiles[plateau + 1 :]:
            self.assertEqual(profile.rational_rank, profiles[plateau].rational_rank)
            self.assertEqual(
                profile.maximal_nonzero_determinantal_divisor,
                profiles[plateau].maximal_nonzero_determinantal_divisor,
            )
            self.assertEqual(
                profile.smith_invariant_factors,
                profiles[plateau].smith_invariant_factors,
            )

    def test_prime_factor_multiplicity(self):
        expected = {
            1: 0,
            2: 1,
            4: 2,
            8: 3,
            12: 3,
            18: 3,
            36: 4,
            72: 5,
            97: 1,
        }
        for value, count in expected.items():
            self.assertEqual(prime_factor_multiplicity(value), count)

    def test_row_generation_matches_direct_literal_word_enumeration(self):
        observation = ((1, 0),)
        actions = (
            ((1, 1), (0, 1)),
            ((0, 1), (1, 0)),
        )
        for horizon in range(4):
            expected = {observation[0]}
            frontier = {observation[0]}
            for _ in range(horizon):
                next_frontier = set()
                for row in frontier:
                    for matrix in actions:
                        next_frontier.add(
                            tuple(
                                sum(row[k] * matrix[k][column] for k in range(2))
                                for column in range(2)
                            )
                        )
                frontier = next_frontier
                expected.update(frontier)
            self.assertEqual(
                set(action_language_observation_rows(actions, observation, horizon)),
                expected,
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            action_language_observation_rows((), ((1, 0),), 1)
        with self.assertRaises(ValueError):
            action_language_observation_rows(
                (((1, 0),),),
                ((1, 0),),
                1,
            )
        with self.assertRaises(ValueError):
            action_language_observation_rows(
                (((1, 0), (0, 1)),),
                ((1, 0),),
                -1,
            )
        with self.assertRaises(TypeError):
            prime_factor_multiplicity(False)
        with self.assertRaises(ValueError):
            prime_factor_multiplicity(0)


if __name__ == "__main__":
    unittest.main()
