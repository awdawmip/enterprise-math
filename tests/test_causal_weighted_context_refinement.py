import unittest

from enterprise_math.causal_recursive_join import kernel_is_associative
from enterprise_math.causal_weighted_context_refinement import (
    compile_weighted_contextual_kernel,
    induced_weighted_type_kernel,
    stable_weighted_contextual_types,
)


def _set_partitions(items):
    if not items:
        yield ()
        return
    first = items[0]
    for rest in _set_partitions(items[1:]):
        yield (frozenset({first}),) + rest
        for index in range(len(rest)):
            merged = list(rest)
            merged[index] = frozenset(set(merged[index]) | {first})
            yield tuple(merged)


def _classes_from_partition(states, partition):
    result = {}
    for class_id, block in enumerate(partition):
        for state in block:
            result[state] = class_id
    if set(result) != set(states):
        raise AssertionError("partition did not cover states")
    return result


def _partition_refines(left, right, states):
    """Whether `left` is finer than `right`."""
    return all(
        left[a] != left[b] or right[a] == right[b]
        for a in states
        for b in states
    )


class CausalWeightedContextRefinementTests(unittest.TestCase):
    def test_grade_channel_can_force_finer_types_than_value_observation(self):
        states = (0, 1, 2, 3)
        observations = {state: state % 2 for state in states}
        # Base-4 residue join with exact local carry grade.
        raw_kernel = {
            (left, right, (left + right) % 4, (left + right) // 4): 1
            for left in states
            for right in states
        }
        self.assertTrue(kernel_is_associative(states, raw_kernel))
        classes, induced, _ = compile_weighted_contextual_kernel(
            states, observations, raw_kernel
        )
        # Parity alone would identify 0~2 and 1~3, but future carry grades can
        # distinguish those residues, so all four raw states remain necessary.
        self.assertEqual(len(set(classes.values())), 4)
        self.assertTrue(kernel_is_associative(tuple(sorted(set(classes.values()))), induced))

    def test_without_grade_observation_parity_can_remain_two_types(self):
        states = (0, 1, 2, 3)
        observations = {state: state % 2 for state in states}
        raw_kernel = {
            (left, right, (left + right) % 4, 0): 1
            for left in states
            for right in states
        }
        classes, induced, _ = compile_weighted_contextual_kernel(
            states, observations, raw_kernel
        )
        self.assertEqual(len(set(classes.values())), 2)
        self.assertTrue(kernel_is_associative(tuple(sorted(set(classes.values()))), induced))

    def test_duplicate_raw_identities_with_same_future_join_profile_collapse(self):
        states = ("a0", "a1")
        observations = {"a0": 0, "a1": 0}
        # Every pair produces the same raw output a0 with no grade shift.
        raw_kernel = {
            (left, right, "a0", 0): 1
            for left in states
            for right in states
        }
        classes, induced, _ = compile_weighted_contextual_kernel(
            states, observations, raw_kernel
        )
        self.assertEqual(len(set(classes.values())), 1)
        self.assertEqual(induced, {(0, 0, 0, 0): 1})

    def test_unsafe_manual_partition_is_rejected_by_induced_kernel(self):
        states = (0, 1)
        # Same current observation, but pair grade distinguishes left raw state.
        raw_kernel = {
            (0, 0, 0, 0): 1,
            (0, 1, 1, 0): 1,
            (1, 0, 1, 1): 1,
            (1, 1, 0, 1): 1,
        }
        manual = {0: 0, 1: 0}
        with self.assertRaises(ValueError):
            induced_weighted_type_kernel(states, raw_kernel, manual)

        observations = {0: 0, 1: 0}
        stable, _ = stable_weighted_contextual_types(states, observations, raw_kernel)
        self.assertEqual(len(set(stable.values())), 2)

    def test_stable_partition_is_coarsest_safe_refinement_by_full_partition_oracle(self):
        states = ("a0", "a1", "b")
        observations = {"a0": "A", "a1": "A", "b": "B"}

        def out(left, right):
            left_b = left == "b"
            right_b = right == "b"
            return "b" if (left_b or right_b) else "a0"

        raw_kernel = {
            (left, right, out(left, right), 0): 1
            for left in states
            for right in states
        }
        stable, _ = stable_weighted_contextual_types(states, observations, raw_kernel)
        self.assertEqual(stable["a0"], stable["a1"])
        self.assertNotEqual(stable["a0"], stable["b"])

        safe_partitions = []
        seen = set()
        for partition in _set_partitions(states):
            canonical = tuple(sorted((tuple(sorted(block)) for block in partition)))
            if canonical in seen:
                continue
            seen.add(canonical)
            classes = _classes_from_partition(states, partition)
            observation_safe = all(
                classes[a] != classes[b] or observations[a] == observations[b]
                for a in states
                for b in states
            )
            if not observation_safe:
                continue
            try:
                induced_weighted_type_kernel(states, raw_kernel, classes)
            except ValueError:
                continue
            safe_partitions.append(classes)

        self.assertTrue(safe_partitions)
        # Every safe partition refines the automatically compiled stable one.
        self.assertTrue(
            all(_partition_refines(candidate, stable, states) for candidate in safe_partitions)
        )
        # The stable partition itself is safe.
        induced_weighted_type_kernel(states, raw_kernel, stable)


if __name__ == "__main__":
    unittest.main()
