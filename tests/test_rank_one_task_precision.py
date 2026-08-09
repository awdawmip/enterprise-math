import itertools
import unittest

from enterprise_math.guard_branch_erasure import rank_one_branch_erasure_report
from enterprise_math.guard_image_lattice import (
    guard_kernel_image_rank,
    guard_rank_one_step,
)
from enterprise_math.rank_one_task_precision import minimum_rank_one_task_precision
from enterprise_math.relation_precision_profile import partition_refines


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


def complete_effect_table(guard_count, default="same"):
    return {
        pattern: default
        for pattern in itertools.product((False, True), repeat=guard_count)
    }


def brute_safe_partitions(guards, parent, base_scores, effects):
    fine_size = sum(len(group) for group in parent)
    result = []
    for partition in set_partitions(range(fine_size)):
        if not partition_refines(partition, parent):
            continue
        child_rank = guard_kernel_image_rank(guards, partition)
        if child_rank == 0:
            pattern = tuple(score >= 0 for score in base_scores)
            safe = pattern in effects
        elif child_rank == 1:
            step = guard_rank_one_step(guards, partition)
            safe = rank_one_branch_erasure_report(
                base_scores, step, effects
            ).safe_to_erase
        else:
            raise AssertionError("refinement of parent rank-one image cannot increase hidden rank")
        if safe:
            result.append(partition)
    return tuple(result)


class RankOneTaskPrecisionTests(unittest.TestCase):
    def test_three_slot_example_finds_rank_gain_one_instead_of_full_visibility(self):
        guards = (
            (0, 1, 2),
            (0, -1, -2),
        )
        parent = ((0, 1, 2),)
        base = (1, -1)
        effects = complete_effect_table(2, "same")
        effects[(True, True)] = "different"
        effects[(False, False)] = "unreachable"

        result = minimum_rank_one_task_precision(
            guards, parent, base, effects
        )
        self.assertEqual(result.minimum_relation_rank_gain, 1)
        self.assertEqual(len(result.candidates), 1)
        candidate = result.candidates[0]
        self.assertEqual(candidate.partition, ((0, 2), (1,)))
        self.assertEqual(candidate.modulus, 2)
        self.assertEqual(candidate.child_hidden_rank, 1)
        self.assertEqual(candidate.child_step, (2, -2))
        self.assertTrue(candidate.erasure_report.safe_to_erase)

    def test_solver_minimum_rank_matches_full_partition_oracle(self):
        guards = (
            (0, 1, 2),
            (0, -1, -2),
        )
        parent = ((0, 1, 2),)
        base = (1, -1)
        effects = complete_effect_table(2, "same")
        effects[(True, True)] = "different"
        effects[(False, False)] = "unreachable"

        solver = minimum_rank_one_task_precision(
            guards, parent, base, effects
        )
        brute = brute_safe_partitions(guards, parent, base, effects)
        minimum_brute_gain = min(len(partition) - len(parent) for partition in brute)
        brute_minimum = {
            partition
            for partition in brute
            if len(partition) - len(parent) == minimum_brute_gain
        }
        solver_minimum = {candidate.partition for candidate in solver.candidates}
        self.assertEqual(solver.minimum_relation_rank_gain, minimum_brute_gain)
        self.assertEqual(solver_minimum, brute_minimum)

    def test_minimum_rank_frontier_can_have_incomparable_partitions(self):
        guards = (
            (0, 1, 3),
            (0, -1, -3),
        )
        parent = ((0, 1, 2),)
        base = (1, -1)
        effects = complete_effect_table(2, "same")
        effects[(True, True)] = "different"
        effects[(False, False)] = "unreachable"

        result = minimum_rank_one_task_precision(
            guards, parent, base, effects
        )
        self.assertEqual(result.minimum_relation_rank_gain, 1)
        frontier = {candidate.partition for candidate in result.candidates}
        self.assertEqual(
            frontier,
            {
                ((0,), (1, 2)),   # label residues mod 2
                ((0, 2), (1,)),   # label residues mod 3
            },
        )
        partitions = tuple(frontier)
        self.assertFalse(partition_refines(partitions[0], partitions[1]))
        self.assertFalse(partition_refines(partitions[1], partitions[0]))

        brute = brute_safe_partitions(guards, parent, base, effects)
        minimum_brute_gain = min(len(partition) - 1 for partition in brute)
        brute_frontier = {
            partition
            for partition in brute
            if len(partition) - 1 == minimum_brute_gain
        }
        self.assertEqual(frontier, brute_frontier)

    def test_already_safe_parent_returns_zero_precision_gain(self):
        guards = (
            (0, 1, 2),
            (0, -1, -2),
        )
        parent = ((0, 1, 2),)
        base = (1, -1)
        effects = complete_effect_table(2, "same")
        result = minimum_rank_one_task_precision(
            guards, parent, base, effects
        )
        self.assertEqual(result.minimum_relation_rank_gain, 0)
        self.assertEqual(result.candidates[0].partition, parent)
        self.assertEqual(result.candidates[0].modulus, 1)

    def test_single_guard_with_distinct_branch_effects_requires_visibility(self):
        guards = ((0, 1, 2),)
        parent = ((0, 1, 2),)
        base = (1,)
        effects = {(False,): "negative", (True,): "nonnegative"}
        result = minimum_rank_one_task_precision(
            guards, parent, base, effects
        )
        self.assertEqual(result.minimum_relation_rank_gain, 2)
        self.assertEqual(
            {candidate.partition for candidate in result.candidates},
            {((0,), (1,), (2,))},
        )

        brute = brute_safe_partitions(guards, parent, base, effects)
        minimum_brute_gain = min(len(partition) - 1 for partition in brute)
        self.assertEqual(minimum_brute_gain, 2)


if __name__ == "__main__":
    unittest.main()
