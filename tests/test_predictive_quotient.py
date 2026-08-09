import itertools
import unittest

from enterprise_math.precision_task_observable import (
    any_or_all_class_count,
    full_vector_class_count,
    linear_two_coordinate_class_count,
    symmetric_sum_class_count,
    two_coordinate_equality_class_count,
)
from enterprise_math.predictive_quotient import (
    distinguishing_horizon,
    finite_horizon_partition,
    observation_partition,
    partition_block_count,
    partition_blocks,
    predictive_block_profile,
    quotient_observation_table,
    quotient_transition_table,
    restricted_block_count,
    stable_predictive_partition,
)


def countdown_system(width: int, dimension: int):
    states = tuple(itertools.product(range(width + 1), repeat=dimension))
    initial = tuple(itertools.product(range(1, width + 1), repeat=dimension))

    def tick(state):
        return tuple(max(0, value - 1) for value in state)

    return states, initial, {"tick": tick}


def crossed_vector(state):
    return tuple(int(value == 0) for value in state)


class GenericCompilerTests(unittest.TestCase):
    def test_horizon_zero_is_current_observation_partition(self) -> None:
        states = (0, 1, 2, 3)
        actions = {"next": lambda state: min(3, state + 1)}
        observe = lambda state: state >= 2
        self.assertEqual(
            finite_horizon_partition(states, actions, observe, 0),
            observation_partition(states, observe),
        )

    def test_partition_refinement_is_monotone_and_finitely_stable(self) -> None:
        states = tuple(range(6))
        actions = {"tick": lambda state: max(0, state - 1)}
        observe = lambda state: state == 0
        counts = predictive_block_profile(states, actions, observe, 8)
        self.assertEqual(counts, tuple(sorted(counts)))
        stable = stable_predictive_partition(states, actions, observe)
        self.assertEqual(stable.block_count, 6)
        self.assertEqual(stable.stabilization_depth, 4)
        self.assertTrue(all(count == 6 for count in counts[5:]))

    def test_distinguishing_horizon_and_stable_equivalence(self) -> None:
        states = (0, 1, 2, 3)
        actions = {"tick": lambda state: max(0, state - 1)}
        observe = lambda state: state == 0
        self.assertEqual(distinguishing_horizon(states, actions, observe, 1, 2), 1)
        self.assertEqual(distinguishing_horizon(states, actions, observe, 2, 3), 2)
        self.assertIsNone(distinguishing_horizon(states, actions, lambda _state: 0, 1, 3))

    def test_stable_partition_builds_exact_quotient_tables(self) -> None:
        states = tuple(range(5))
        actions = {"tick": lambda state: max(0, state - 1)}
        observe = lambda state: int(state == 0)
        stable = stable_predictive_partition(states, actions, observe)
        transitions = quotient_transition_table(states, actions, stable.partition)
        outputs = quotient_observation_table(states, observe, stable.partition)
        self.assertEqual(len(outputs), 5)
        self.assertEqual(len(transitions), 5)

    def test_unsafe_partition_is_rejected_by_quotient_transition_table(self) -> None:
        states = (0, 1, 2)
        actions = {"tick": lambda state: max(0, state - 1)}
        with self.assertRaises(ValueError):
            quotient_transition_table(states, actions, (0, 1, 1))


class E002FormulaReconstructionTests(unittest.TestCase):
    def test_full_vector_stage4_formula_is_compiler_output(self) -> None:
        for width in (1, 3, 5, 7):
            for dimension in range(1, 4):
                states, initial, actions = countdown_system(width, dimension)
                for horizon in range(width):
                    partition = finite_horizon_partition(
                        states,
                        actions,
                        crossed_vector,
                        horizon,
                    )
                    self.assertEqual(
                        restricted_block_count(states, partition, initial),
                        full_vector_class_count(dimension, horizon),
                    )

    def test_stage5_symmetric_sum_formula_is_compiler_output(self) -> None:
        for width in (1, 3, 5):
            for dimension in range(1, 5):
                states, initial, actions = countdown_system(width, dimension)
                observe = lambda state: sum(int(value == 0) for value in state)
                for horizon in range(width):
                    partition = finite_horizon_partition(states, actions, observe, horizon)
                    self.assertEqual(
                        restricted_block_count(states, partition, initial),
                        symmetric_sum_class_count(dimension, horizon),
                    )

    def test_stage5_any_all_formulas_are_compiler_output(self) -> None:
        for width in (1, 3, 5):
            for dimension in range(1, 5):
                states, initial, actions = countdown_system(width, dimension)
                observations = (
                    lambda state: int(any(value == 0 for value in state)),
                    lambda state: int(all(value == 0 for value in state)),
                )
                for observe in observations:
                    for horizon in range(width):
                        partition = finite_horizon_partition(states, actions, observe, horizon)
                        self.assertEqual(
                            restricted_block_count(states, partition, initial),
                            any_or_all_class_count(horizon),
                        )

    def test_stage5_two_coordinate_linear_classification_is_compiler_output(self) -> None:
        for width in (1, 3, 5, 7):
            states, initial, actions = countdown_system(width, 2)
            for horizon in range(width):
                for alpha in range(-2, 3):
                    for beta in range(-2, 3):
                        observe = lambda state, a=alpha, b=beta: (
                            a * int(state[0] == 0) + b * int(state[1] == 0)
                        )
                        partition = finite_horizon_partition(states, actions, observe, horizon)
                        self.assertEqual(
                            restricted_block_count(states, partition, initial),
                            linear_two_coordinate_class_count(alpha, beta, horizon),
                        )

    def test_stage5_equality_formula_is_compiler_output(self) -> None:
        for width in (1, 3, 5, 7):
            states, initial, actions = countdown_system(width, 2)
            observe = lambda state: int((state[0] == 0) == (state[1] == 0))
            for horizon in range(width):
                partition = finite_horizon_partition(states, actions, observe, horizon)
                self.assertEqual(
                    restricted_block_count(states, partition, initial),
                    two_coordinate_equality_class_count(horizon),
                )


class PartitionShapeTests(unittest.TestCase):
    def test_partition_blocks_cover_state_set_once(self) -> None:
        states = tuple(range(7))
        partition = (0, 0, 1, 2, 2, 2, 3)
        blocks = partition_blocks(states, partition)
        self.assertEqual(sum(len(block) for block in blocks), len(states))
        self.assertEqual(set().union(*(set(block) for block in blocks)), set(states))
        self.assertEqual(partition_block_count(partition), 4)


if __name__ == "__main__":
    unittest.main()
