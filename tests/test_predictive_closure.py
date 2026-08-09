import unittest
from itertools import product

from enterprise_math.predictive_closure import (
    block_map,
    candidate_refines_predictive_closure,
    first_stable_horizon,
    horizon_partition,
    observation_partition,
    partition_is_forward_compatible,
    partition_refines,
    predictive_closure_partition,
    quotient_observation,
    quotient_transition,
)


def set_partitions(values):
    values = tuple(values)
    if not values:
        yield frozenset()
        return
    first, *rest = values
    for partition in set_partitions(rest):
        blocks = list(partition)
        yield frozenset([frozenset({first}), *blocks])
        for index, block in enumerate(blocks):
            merged = set(block)
            merged.add(first)
            replacement = [
                frozenset(merged) if i == index else candidate
                for i, candidate in enumerate(blocks)
            ]
            yield frozenset(replacement)


class PredictiveClosureTests(unittest.TestCase):
    def test_horizon_partitions_refine_monotonically(self) -> None:
        states = tuple(range(10))
        operation = lambda n: max(n - 1, 0)
        observation = lambda n: n // 3
        previous = horizon_partition(states, operation, observation, 0)
        for horizon in range(1, 10):
            current = horizon_partition(states, operation, observation, horizon)
            self.assertTrue(partition_refines(current, previous))
            previous = current

    def test_tight_two_step_refinement_example(self) -> None:
        states = (0, 1, 2, 3)
        transition = {0: 0, 1: 0, 2: 1, 3: 2}
        outputs = {0: 0, 1: 1, 2: 0, 3: 0}
        operation = transition.__getitem__
        observation = outputs.__getitem__
        horizon, partition = first_stable_horizon(states, operation, observation)
        self.assertEqual(horizon, 2)
        self.assertEqual(len(observation_partition(states, observation)), 2)
        self.assertEqual(partition, frozenset(frozenset({x}) for x in states))

    def test_exhaustive_bound_on_four_state_binary_observations(self) -> None:
        states = (0, 1, 2, 3)
        for transition_values in product(states, repeat=len(states)):
            transition = dict(zip(states, transition_values, strict=True))
            operation = transition.__getitem__
            for output_values in product((0, 1), repeat=len(states)):
                outputs = dict(zip(states, output_values, strict=True))
                observation = outputs.__getitem__
                horizon, _ = first_stable_horizon(states, operation, observation)
                c0 = len(observation_partition(states, observation))
                self.assertLessEqual(horizon, len(states) - c0)

    def test_stable_partition_is_forward_compatible_and_refines_observation(self) -> None:
        examples = [
            (
                tuple(range(10)),
                lambda n: max(n - 1, 0),
                lambda n: n // 3,
            ),
            (
                tuple(range(8)),
                lambda n: (2 * n) % 8,
                lambda n: n // 2,
            ),
        ]
        for states, operation, observation in examples:
            closure = predictive_closure_partition(states, operation, observation)
            original = observation_partition(states, observation)
            self.assertTrue(partition_refines(closure, original))
            self.assertTrue(partition_is_forward_compatible(closure, operation))

    def test_stable_horizon_zero_exactly_for_closed_observation_in_examples(self) -> None:
        closed_states = tuple(range(24))
        closed_operation = lambda n: max(n - 2, 0)
        quotient2 = lambda n: n // 2
        closed_horizon, _ = first_stable_horizon(
            closed_states, closed_operation, quotient2
        )
        self.assertEqual(closed_horizon, 0)

        open_states = tuple(range(8))
        open_operation = lambda n: (2 * n) % 8
        open_horizon, _ = first_stable_horizon(
            open_states, open_operation, quotient2
        )
        self.assertGreater(open_horizon, 0)

    def test_predictive_closure_is_coarsest_compatible_refinement(self) -> None:
        states = (0, 1, 2, 3, 4)
        operation = lambda n: max(n - 1, 0)
        observation = lambda n: n // 2
        closure = predictive_closure_partition(states, operation, observation)
        for candidate in set_partitions(states):
            if set(block_map(candidate)) != set(states):
                continue
            if all(
                len({observation(state) for state in block}) == 1
                for block in candidate
            ) and partition_is_forward_compatible(candidate, operation):
                self.assertTrue(
                    candidate_refines_predictive_closure(
                        states, operation, observation, candidate
                    )
                )
                self.assertTrue(partition_refines(candidate, closure))

    def test_quotient_dynamics_and_output_are_exact(self) -> None:
        states = tuple(range(10))
        operation = lambda n: max(n - 1, 0)
        observation = lambda n: n // 3
        closure = predictive_closure_partition(states, operation, observation)
        state_to_block = block_map(closure)
        quotient_step = quotient_transition(closure, operation)
        quotient_output = quotient_observation(closure, observation)
        for state in states:
            block = state_to_block[state]
            self.assertEqual(quotient_step[block], state_to_block[operation(state)])
            self.assertEqual(quotient_output[block], observation(state))

    def test_if_closure_is_equality_no_nontrivial_exact_refinement_survives(self) -> None:
        states = (0, 1, 2, 3)
        transition = {0: 0, 1: 0, 2: 1, 3: 2}
        outputs = {0: 0, 1: 1, 2: 0, 3: 0}
        operation = transition.__getitem__
        observation = outputs.__getitem__
        closure = predictive_closure_partition(states, operation, observation)
        self.assertEqual(closure, frozenset(frozenset({x}) for x in states))
        for candidate in set_partitions(states):
            if set(block_map(candidate)) != set(states):
                continue
            if all(
                len({observation(state) for state in block}) == 1
                for block in candidate
            ) and partition_is_forward_compatible(candidate, operation):
                self.assertEqual(candidate, closure)


if __name__ == "__main__":
    unittest.main()
