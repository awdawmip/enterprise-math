import unittest

from enterprise_math.semantic_operation_refinement import (
    coarsest_operation_safe_refinement,
    operation_refinement_step,
    partition_is_safe_for_all,
    verify_coarsest_against_candidate,
)
from enterprise_math.semantic_precision_preorder import (
    normalize_partition,
    partition_refines,
)


def all_set_partitions(values):
    values = tuple(values)
    if not values:
        yield ()
        return

    def rec(index, blocks):
        if index == len(values):
            yield normalize_partition(tuple(frozenset(block) for block in blocks))
            return
        value = values[index]
        for block_index in range(len(blocks)):
            next_blocks = [set(block) for block in blocks]
            next_blocks[block_index].add(value)
            yield from rec(index + 1, next_blocks)
        yield from rec(index + 1, [*blocks, {value}])

    seen = set()
    for partition in rec(0, []):
        if partition not in seen:
            seen.add(partition)
            yield partition


class SemanticOperationRefinementTests(unittest.TestCase):
    def test_unsafe_fine_partition_gets_minimal_extra_split(self):
        initial = ({0, 1}, {2}, {3})
        operations = {
            "t": {
                0: 0,
                1: 2,
                2: 0,
                3: 3,
            }
        }
        report = coarsest_operation_safe_refinement(initial, operations)
        self.assertEqual(
            set(report.final_partition),
            {frozenset({0}), frozenset({1}), frozenset({2}), frozenset({3})},
        )
        self.assertEqual(report.strict_refinement_steps, 1)
        self.assertEqual(report.added_state_distinctions, 1)
        self.assertTrue(partition_is_safe_for_all(report.final_partition, operations))

    def test_one_operation_can_require_two_cascading_refinement_steps(self):
        initial = ({0, 1}, {2, 3})
        operations = {
            "t": {
                0: 2,
                1: 3,
                2: 0,
                3: 3,
            }
        }
        first = operation_refinement_step(initial, operations)
        self.assertEqual(
            set(first),
            {frozenset({0, 1}), frozenset({2}), frozenset({3})},
        )
        second = operation_refinement_step(first, operations)
        self.assertEqual(
            set(second),
            {frozenset({0}), frozenset({1}), frozenset({2}), frozenset({3})},
        )
        report = coarsest_operation_safe_refinement(initial, operations)
        self.assertEqual(report.strict_refinement_steps, 2)
        self.assertEqual(report.final_partition, second)
        self.assertEqual(
            report.strict_refinement_steps,
            4 - len(normalize_partition(initial)),
        )

    def test_already_safe_partition_is_fixed_at_horizon_zero(self):
        initial = ({0, 1, 2}, {3})
        operations = {
            "t": {
                0: 0,
                1: 2,
                2: 0,
                3: 3,
            }
        }
        report = coarsest_operation_safe_refinement(initial, operations)
        self.assertEqual(report.final_partition, normalize_partition(initial))
        self.assertEqual(report.strict_refinement_steps, 0)

    def test_exhaustive_four_state_coarsest_property_for_cascade_operation(self):
        states = (0, 1, 2, 3)
        initial = normalize_partition(({0, 1}, {2, 3}))
        operations = {
            "t": {
                0: 2,
                1: 3,
                2: 0,
                3: 3,
            }
        }
        report = coarsest_operation_safe_refinement(initial, operations)
        safe_candidates = 0
        for candidate in all_set_partitions(states):
            if not partition_refines(candidate, initial):
                continue
            if not partition_is_safe_for_all(candidate, operations):
                continue
            safe_candidates += 1
            self.assertTrue(
                verify_coarsest_against_candidate(
                    report,
                    candidate,
                    operations,
                )
            )
        self.assertGreater(safe_candidates, 0)

    def test_multiple_operations_refine_by_joint_target_signature(self):
        initial = ({0, 1, 2}, {3, 4})
        operations = {
            "a": {0: 0, 1: 1, 2: 3, 3: 3, 4: 4},
            "b": {0: 3, 1: 4, 2: 4, 3: 0, 4: 0},
        }
        report = coarsest_operation_safe_refinement(initial, operations)
        self.assertTrue(partition_is_safe_for_all(report.final_partition, operations))
        self.assertTrue(partition_refines(report.final_partition, initial))
        self.assertLessEqual(report.strict_refinement_steps, 5 - len(normalize_partition(initial)))

    def test_no_operations_requires_no_refinement(self):
        initial = ({0, 1}, {2, 3})
        report = coarsest_operation_safe_refinement(initial, {})
        self.assertEqual(report.final_partition, normalize_partition(initial))
        self.assertEqual(report.strict_refinement_steps, 0)

    def test_validation(self):
        with self.assertRaises(ValueError):
            coarsest_operation_safe_refinement(
                ({0, 1},),
                {"bad": {0: 0}},
            )
        report = coarsest_operation_safe_refinement(
            ({0, 1},),
            {"id": {0: 0, 1: 1}},
        )
        with self.assertRaises(ValueError):
            verify_coarsest_against_candidate(
                report,
                ({0}, {1}),
                {"bad": {0: 0, 1: 0}},
            )


if __name__ == "__main__":
    unittest.main()
