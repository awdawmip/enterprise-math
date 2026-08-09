import itertools
import unittest

from enterprise_math.linear_observation_quotient import (
    descended_linear_observable,
    linear_observable_descends,
    minimum_exact_partition_for_linear_language,
    observation_family_descends,
    refine_partition_for_linear_observations,
)
from enterprise_math.linear_relation_quotient import linear_family_descends


def is_refinement(fine_partition, coarse_partition):
    coarse_group_of = {}
    for group_index, group in enumerate(coarse_partition):
        for vertex in group:
            coarse_group_of[vertex] = group_index
    return all(
        len({coarse_group_of[vertex] for vertex in group}) == 1
        for group in fine_partition
    )


def set_partitions(items):
    items = tuple(items)
    if not items:
        yield ()
        return
    first = items[0]
    for rest in set_partitions(items[1:]):
        yield ((first,),) + rest
        for index in range(len(rest)):
            yield rest[:index] + ((first,) + rest[index],) + rest[index + 1 :]


class LinearObservationQuotientTests(unittest.TestCase):
    def test_observable_descends_iff_coefficients_are_block_constant(self):
        partition = ((0, 1), (2, 3, 4))
        observable = (2, 2, -3, -3, -3)
        self.assertTrue(linear_observable_descends(observable, partition))
        self.assertEqual(descended_linear_observable(observable, partition), (2, -3))

        hidden = (2, 1, -3, -3, -3)
        self.assertFalse(linear_observable_descends(hidden, partition))

    def test_observation_refinement_splits_only_coefficient_distinctions(self):
        initial = ((0, 1, 2, 3),)
        observables = (
            (1, 1, 0, 0),
            (2, 2, -1, -1),
        )
        refined = refine_partition_for_linear_observations(observables, initial)
        self.assertEqual(refined, ((0, 1), (2, 3)))
        self.assertTrue(observation_family_descends(observables, refined))

    def test_hidden_internal_relation_score_forces_refinement(self):
        # For unit capacities, Z_01 = c_0-c_1.
        initial = ((0, 1), (2, 3))
        relation_score = (1, -1, 0, 0)
        refined = refine_partition_for_linear_observations(
            (relation_score,), initial
        )
        self.assertEqual(refined, ((0,), (1,), (2, 3)))

    def test_coarse_relation_score_does_not_force_internal_split(self):
        # Difference between coarse totals C_A-C_B is block-constant.
        initial = ((0, 1), (2, 3))
        coarse_score = (1, 1, -1, -1)
        refined = refine_partition_for_linear_observations(
            (coarse_score,), initial
        )
        self.assertEqual(refined, initial)

    def test_dynamics_and_observations_jointly_determine_partition(self):
        matrix = (
            (1, 0, 0, 0),
            (0, 1, 0, 0),
            (1, 0, 1, 0),
            (0, 2, 0, 1),
        )
        observable = (0, 0, 1, -1)
        initial = ((0, 1), (2, 3))
        result = minimum_exact_partition_for_linear_language(
            (matrix,), (observable,), initial
        )
        self.assertEqual(result, ((0,), (1,), (2,), (3,)))
        self.assertTrue(linear_family_descends((matrix,), result))
        self.assertTrue(observation_family_descends((observable,), result))

    def test_joint_solver_is_coarsest_common_exact_refinement_by_bruteforce(self):
        matrices = (
            (
                (1, 0, 1, 0),
                (0, 1, 0, 1),
                (0, 0, 1, 0),
                (0, 0, 0, 1),
            ),
        )
        observables = ((1, 1, -1, -1), (0, 0, 1, -1))
        initial = ((0, 1, 2, 3),)
        result = minimum_exact_partition_for_linear_language(
            matrices, observables, initial
        )
        self.assertTrue(linear_family_descends(matrices, result))
        self.assertTrue(observation_family_descends(observables, result))

        for candidate in set_partitions(range(4)):
            if not is_refinement(candidate, initial):
                continue
            if not linear_family_descends(matrices, candidate):
                continue
            if not observation_family_descends(observables, candidate):
                continue
            self.assertTrue(is_refinement(candidate, result), msg=candidate)

    def test_affine_observable_constant_never_changes_partition(self):
        # Exact score w^T c + b only needs w to descend; b is already coarse.
        partition = ((0, 1), (2, 3))
        observable = (3, 3, -2, -2)
        coarse = descended_linear_observable(observable, partition)
        offset = 17
        for state in itertools.product(range(-2, 3), repeat=4):
            fine_score = sum(a * b for a, b in zip(observable, state)) + offset
            coarse_state = (state[0] + state[1], state[2] + state[3])
            coarse_score = sum(a * b for a, b in zip(coarse, coarse_state)) + offset
            self.assertEqual(fine_score, coarse_score)


if __name__ == "__main__":
    unittest.main()
