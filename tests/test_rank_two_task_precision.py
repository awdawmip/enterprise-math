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
from enterprise_math.rank_two_guard_refinement import (
    canonical_z2_subgroup,
    rank_two_canonical_sublattice_refinement,
    rank_two_guard_labels,
    rank_two_realizable_image_subgroups,
)
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


def brute_safe_partitions(guards, parent, base_scores, effects):
    fine_size = sum(len(group) for group in parent)
    safe = []
    for partition in set_partitions(range(fine_size)):
        if not partition_refines(partition, parent):
            continue
        rank = guard_kernel_image_rank(guards, partition)
        if rank == 0:
            report_safe = True
        elif rank == 1:
            report_safe = rank_one_branch_erasure_report(
                base_scores,
                guard_rank_one_step(guards, partition),
                effects,
            ).safe_to_erase
        elif rank == 2:
            report_safe = rank_two_branch_erasure_report(
                base_scores,
                guard_kernel_image_generators(guards, partition),
                effects,
            ).safe_to_erase
        else:
            raise AssertionError("rank-two parent refinement cannot gain hidden rank")
        if report_safe:
            safe.append(partition)
    return tuple(safe)


class RankTwoTaskPrecisionTests(unittest.TestCase):
    def setUp(self):
        # Hidden labels relative to the standard Z^2 basis are
        # 0, (1,1), (2,2), (0,1). Parent image is full Z^2.
        self.guards = (
            (0, 1, 2, 0),
            (0, 1, 2, 1),
        )
        self.parent = ((0, 1, 2, 3),)
        self.base = (1, 1)  # fine state c=(0,1,0,0)

    def test_rank_two_hidden_labels_match_intended_coordinates(self):
        hidden = rank_two_guard_labels(self.guards, self.parent)
        self.assertEqual(hidden.parent_basis, ((1, 0), (0, 1)))
        self.assertEqual(
            hidden.labeled_blocks[0],
            (
                (0, (0, 0)),
                (1, (1, 1)),
                (2, (2, 2)),
                (3, (0, 1)),
            ),
        )

    def test_diagonal_target_subgroup_has_canonical_coarsest_partition(self):
        diagonal = canonical_z2_subgroup(((1, 1),))
        canonical = rank_two_canonical_sublattice_refinement(
            self.guards, self.parent, diagonal
        )
        self.assertEqual(canonical, ((0, 1, 2), (3,)))
        self.assertEqual(guard_kernel_image_rank(self.guards, canonical), 1)
        self.assertEqual(guard_rank_one_step(self.guards, canonical), (1, 1))

        # A finer refinement with the same exact diagonal image must refine the
        # canonical partition.
        finer = ((0, 1), (2,), (3,))
        self.assertEqual(guard_rank_one_step(self.guards, finer), (1, 1))
        self.assertTrue(partition_refines(finer, canonical))

    def test_realizable_subgroup_enumeration_contains_zero_diagonal_and_parent(self):
        subgroups = set(rank_two_realizable_image_subgroups(self.guards, self.parent))
        self.assertIn((), subgroups)
        self.assertIn(((1, 1),), subgroups)
        self.assertIn(((1, 0), (0, 1)), subgroups)

    def test_rank_two_task_solver_finds_rank_gain_one_without_full_visibility(self):
        effects = complete_effect_table(2, "same")
        # Parent full-rank fiber reaches all four patterns. On the diagonal child
        # coset through base (1,1), (T,F) is impossible.
        effects[(True, False)] = "different"

        result = minimum_rank_two_task_precision(
            self.guards, self.parent, self.base, effects
        )
        self.assertEqual(result.minimum_relation_rank_gain, 1)
        partitions = {candidate.partition for candidate in result.candidates}
        self.assertIn(((0, 1, 2), (3,)), partitions)
        for candidate in result.candidates:
            self.assertTrue(candidate.erasure_report.safe_to_erase)

    def test_rank_two_solver_minimum_frontier_matches_full_partition_oracle(self):
        effects = complete_effect_table(2, "same")
        effects[(True, False)] = "different"

        solver = minimum_rank_two_task_precision(
            self.guards, self.parent, self.base, effects
        )
        brute = brute_safe_partitions(
            self.guards, self.parent, self.base, effects
        )
        minimum_gain = min(len(partition) - 1 for partition in brute)
        brute_frontier = {
            partition for partition in brute if len(partition) - 1 == minimum_gain
        }
        solver_frontier = {candidate.partition for candidate in solver.candidates}
        self.assertEqual(solver.minimum_relation_rank_gain, minimum_gain)
        self.assertEqual(solver_frontier, brute_frontier)

    def test_all_distinct_effects_force_guard_visible_singletons(self):
        effects = {
            pattern: pattern
            for pattern in itertools.product((False, True), repeat=2)
        }
        result = minimum_rank_two_task_precision(
            self.guards, self.parent, self.base, effects
        )
        # Coordinate 1 and 2 have different hidden labels even though they lie
        # on the same diagonal direction; to make the current branch pattern
        # deterministic for every child fiber containing this state, zero hidden
        # image is required here.
        self.assertGreaterEqual(result.minimum_relation_rank_gain, 2)


if __name__ == "__main__":
    unittest.main()
