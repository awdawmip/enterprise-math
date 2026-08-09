import unittest

from enterprise_math.guard_image_lattice import (
    guard_kernel_image_rank,
    guard_rank_one_step,
)
from enterprise_math.rank_one_guard_modulus import (
    rank_one_guard_labels,
    rank_one_modulus_refinement,
    rank_one_modulus_visibility_bound,
)
from enterprise_math.rank_one_guard_refinement import rank_one_step_index
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


def refines_parent(candidate, parent):
    return partition_refines(candidate, parent)


class RankOneGuardModulusTests(unittest.TestCase):
    def test_hidden_labels_reconstruct_guard_coefficient_differences(self):
        guards = (
            (4, 5, 7, 10),
            (-3, -5, -9, -15),
        )
        parent = ((0, 1, 2, 3),)
        step = guard_rank_one_step(guards, parent)
        self.assertEqual(step, (1, -2))
        labeled = rank_one_guard_labels(guards, parent)[0]
        labels = dict(labeled)
        self.assertEqual(labels, {0: 0, 1: 1, 2: 3, 3: 6})
        for coordinate, label in labeled:
            difference = tuple(
                guard[coordinate] - guard[0]
                for guard in guards
            )
            self.assertEqual(
                difference,
                tuple(label * value for value in step),
            )

    def test_modulus_two_recovers_three_slot_precision_example(self):
        guards = (
            (0, 1, 2),
            (0, -1, -2),
        )
        parent = ((0, 1, 2),)
        refined = rank_one_modulus_refinement(guards, parent, 2)
        self.assertEqual(refined, ((0, 2), (1,)))
        parent_step = guard_rank_one_step(guards, parent)
        child_step = guard_rank_one_step(guards, refined)
        self.assertEqual(parent_step, (1, -1))
        self.assertEqual(child_step, (2, -2))
        self.assertEqual(rank_one_step_index(parent_step, child_step), 2)

    def test_modulus_refinement_is_coarsest_for_requested_image_divisibility(self):
        guards = (
            (4, 5, 7, 10),
            (-3, -5, -9, -15),
        )
        parent = ((0, 1, 2, 3),)
        parent_step = guard_rank_one_step(guards, parent)

        for modulus in range(1, 7):
            canonical = rank_one_modulus_refinement(guards, parent, modulus)
            for candidate in set_partitions(range(4)):
                if not refines_parent(candidate, parent):
                    continue
                child_rank = guard_kernel_image_rank(guards, candidate)
                if child_rank == 0:
                    qualifies = True
                elif child_rank == 1:
                    child_step = guard_rank_one_step(guards, candidate)
                    index = rank_one_step_index(parent_step, child_step)
                    qualifies = index % modulus == 0
                else:
                    raise AssertionError("subgroup of rank-one image cannot gain rank")
                if qualifies:
                    # Any refinement whose hidden image lies in q*parent-image
                    # must keep only equal label residues together.
                    self.assertTrue(
                        partition_refines(candidate, canonical),
                        msg=(modulus, candidate, canonical),
                    )

    def test_large_modulus_stabilizes_to_label_equality_partition(self):
        guards = (
            (4, 5, 7, 10),
            (-3, -5, -9, -15),
        )
        parent = ((0, 1, 2, 3),)
        bound = rank_one_modulus_visibility_bound(guards, parent)
        self.assertEqual(bound, 7)
        expected = ((0,), (1,), (2,), (3,))
        for modulus in range(bound, bound + 5):
            self.assertEqual(
                rank_one_modulus_refinement(guards, parent, modulus),
                expected,
            )

    def test_modulus_one_is_parent_partition(self):
        guards = (
            (0, 1, 2),
            (0, -1, -2),
        )
        parent = ((0, 1, 2),)
        self.assertEqual(rank_one_modulus_refinement(guards, parent, 1), parent)


if __name__ == "__main__":
    unittest.main()
