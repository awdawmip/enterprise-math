import unittest

from enterprise_math.causal_operation_language import generator_respects_partition
from enterprise_math.causal_operation_state_duality import (
    observation_removes_safe_monoid_degeneracy,
    refines_observation_kernel,
    safe_monoid_separator,
)


def _partitions(n):
    result = []

    def rec(prefix, maximum):
        if len(prefix) == n:
            result.append(tuple(prefix))
            return
        for value in range(maximum + 2):
            prefix.append(value)
            rec(prefix, max(maximum, value))
            prefix.pop()

    rec([0], 0)
    return result


def _as_map(pattern):
    return {index: class_id for index, class_id in enumerate(pattern)}


def _same(left, right):
    states = tuple(left)
    return all(
        (left[a] == left[b]) == (right[a] == right[b])
        for a in states
        for b in states
    )


class CausalOperationStateDualityTests(unittest.TestCase):
    def test_all_small_distinct_equivalences_have_different_safe_monoids_except_extremes(self):
        states = (0, 1, 2, 3)
        partitions = [_as_map(pattern) for pattern in _partitions(len(states))]
        for index, left in enumerate(partitions):
            for right in partitions[index + 1 :]:
                if _same(left, right):
                    continue
                left_classes = len(set(left.values()))
                right_classes = len(set(right.values()))
                extreme_pair = {left_classes, right_classes} == {1, len(states)}
                separator = safe_monoid_separator(states, left, right)
                if extreme_pair:
                    self.assertIsNone(separator)
                    continue
                self.assertIsNotNone(separator)
                direction, mapping = separator
                left_safe = generator_respects_partition(states, left, mapping)
                right_safe = generator_respects_partition(states, right, mapping)
                if direction == "left_only":
                    self.assertTrue(left_safe)
                    self.assertFalse(right_safe)
                else:
                    self.assertTrue(right_safe)
                    self.assertFalse(left_safe)

    def test_nonconstant_observation_excludes_discrete_indiscrete_degeneracy(self):
        states = (0, 1, 2, 3)
        observation = {0: 0, 1: 0, 2: 1, 3: 1}
        partitions = [_as_map(pattern) for pattern in _partitions(len(states))]
        valid = [
            partition
            for partition in partitions
            if refines_observation_kernel(states, observation, partition)
        ]
        for index, left in enumerate(valid):
            for right in valid[index + 1 :]:
                if _same(left, right):
                    continue
                self.assertTrue(
                    observation_removes_safe_monoid_degeneracy(
                        states,
                        observation,
                        left,
                        right,
                    )
                )
                self.assertIsNotNone(safe_monoid_separator(states, left, right))

    def test_discrete_and_indiscrete_partitions_share_all_endomaps(self):
        states = (0, 1, 2)
        discrete = {0: 0, 1: 1, 2: 2}
        indiscrete = {0: 0, 1: 0, 2: 0}
        self.assertIsNone(safe_monoid_separator(states, discrete, indiscrete))

    def test_constant_observation_does_not_remove_extreme_degeneracy(self):
        states = (0, 1, 2)
        observation = {0: 0, 1: 0, 2: 0}
        discrete = {0: 0, 1: 1, 2: 2}
        indiscrete = {0: 0, 1: 0, 2: 0}
        with self.assertRaises(ValueError):
            observation_removes_safe_monoid_degeneracy(
                states,
                observation,
                discrete,
                indiscrete,
            )


if __name__ == "__main__":
    unittest.main()
