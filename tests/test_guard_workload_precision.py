import itertools
import unittest

from enterprise_math.guard_branch_erasure import (
    rank_one_branch_erasure_report,
    rank_two_branch_erasure_report,
)
from enterprise_math.guard_image_lattice import (
    guard_kernel_image_generators,
    guard_kernel_image_rank,
    guard_rank_one_step,
)
from enterprise_math.guard_workload_precision import (
    minimum_rank_one_workload_precision,
    minimum_rank_two_workload_precision,
)
from enterprise_math.rank_one_task_precision import minimum_rank_one_task_precision
from enterprise_math.rank_two_task_precision import minimum_rank_two_task_precision
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


def partition_safe_for_workload(guards, partition, workload, effects):
    rank = guard_kernel_image_rank(guards, partition)
    for scores in workload:
        if rank == 0:
            pattern = tuple(score >= 0 for score in scores)
            if pattern not in effects:
                return False
        elif rank == 1:
            if not rank_one_branch_erasure_report(
                scores, guard_rank_one_step(guards, partition), effects
            ).safe_to_erase:
                return False
        elif rank == 2:
            if not rank_two_branch_erasure_report(
                scores,
                guard_kernel_image_generators(guards, partition),
                effects,
            ).safe_to_erase:
                return False
        else:
            raise AssertionError("test workload expects parent hidden rank <=2")
    return True


def brute_workload_frontier(guards, parent, workload, effects):
    fine_size = sum(len(group) for group in parent)
    safe = []
    for partition in set_partitions(range(fine_size)):
        if not partition_refines(partition, parent):
            continue
        if partition_safe_for_workload(guards, partition, workload, effects):
            safe.append(partition)
    minimum_gain = min(len(partition) - len(parent) for partition in safe)
    return minimum_gain, {
        partition
        for partition in safe
        if len(partition) - len(parent) == minimum_gain
    }


class GuardWorkloadPrecisionTests(unittest.TestCase):
    def test_rank_one_two_local_gain_one_states_need_common_gain_two(self):
        guards = (
            (0, 1, 3),
            (0, -1, -3),
        )
        parent = ((0, 1, 2),)
        effects = complete_effect_table(2, "same")
        effects[(True, True)] = "different"
        effects[(False, False)] = "unreachable"

        # First state: the dangerous zero crossing is t=3. Mod 2 removes it,
        # mod 3 retains it.
        first = (-3, 3)
        # Second state: the dangerous zero crossing is t=2. Mod 3 removes it,
        # mod 2 retains it.
        second = (-2, 2)

        first_local = minimum_rank_one_task_precision(
            guards, parent, first, effects
        )
        second_local = minimum_rank_one_task_precision(
            guards, parent, second, effects
        )
        self.assertEqual(first_local.minimum_relation_rank_gain, 1)
        self.assertEqual(second_local.minimum_relation_rank_gain, 1)
        self.assertIn(
            ((0,), (1, 2)),
            {candidate.partition for candidate in first_local.candidates},
        )
        self.assertIn(
            ((0, 2), (1,)),
            {candidate.partition for candidate in second_local.candidates},
        )

        workload = (first, second)
        common = minimum_rank_one_workload_precision(
            guards, parent, workload, effects
        )
        self.assertEqual(common.minimum_relation_rank_gain, 2)
        self.assertEqual(
            {candidate.partition for candidate in common.candidates},
            {((0,), (1,), (2,))},
        )

        brute_gain, brute_frontier = brute_workload_frontier(
            guards, parent, workload, effects
        )
        self.assertEqual(common.minimum_relation_rank_gain, brute_gain)
        self.assertEqual(
            {candidate.partition for candidate in common.candidates},
            brute_frontier,
        )

    def test_rank_two_common_workload_can_require_finer_subgroup_than_one_state(self):
        guards = (
            (0, 1, 2, 0),
            (0, 1, 2, 1),
        )
        parent = ((0, 1, 2, 3),)
        effects = complete_effect_table(2, "same")
        effects[(True, False)] = "different"

        first = (1, 1)  # diagonal subgroup makes (T,F) unreachable
        second = (2, 0)  # diagonal subgroup still reaches (T,F)

        first_local = minimum_rank_two_task_precision(
            guards, parent, first, effects
        )
        self.assertEqual(first_local.minimum_relation_rank_gain, 1)
        self.assertIn(
            ((0, 1, 2), (3,)),
            {candidate.partition for candidate in first_local.candidates},
        )

        common = minimum_rank_two_workload_precision(
            guards, parent, (first, second), effects
        )
        self.assertEqual(common.minimum_relation_rank_gain, 2)
        # Horizontal hidden subgroup groups equal second hidden-label coordinate:
        # labels (0,0),(1,1),(2,2),(0,1) -> {0},{1,3},{2}.
        self.assertIn(
            ((0,), (1, 3), (2,)),
            {candidate.partition for candidate in common.candidates},
        )

        brute_gain, brute_frontier = brute_workload_frontier(
            guards, parent, (first, second), effects
        )
        self.assertEqual(common.minimum_relation_rank_gain, brute_gain)
        self.assertEqual(
            {candidate.partition for candidate in common.candidates},
            brute_frontier,
        )

    def test_workload_of_one_matches_state_local_minimum_cost(self):
        guards = (
            (0, 1, 3),
            (0, -1, -3),
        )
        parent = ((0, 1, 2),)
        effects = complete_effect_table(2, "same")
        effects[(True, True)] = "different"
        base = (-3, 3)
        local = minimum_rank_one_task_precision(guards, parent, base, effects)
        workload = minimum_rank_one_workload_precision(
            guards, parent, (base,), effects
        )
        self.assertEqual(
            workload.minimum_relation_rank_gain,
            local.minimum_relation_rank_gain,
        )
        self.assertEqual(
            {candidate.partition for candidate in workload.candidates},
            {candidate.partition for candidate in local.candidates},
        )


if __name__ == "__main__":
    unittest.main()
