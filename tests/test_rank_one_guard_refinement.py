import itertools
import unittest

from enterprise_math.guard_branch_erasure import rank_one_branch_erasure_report
from enterprise_math.linear_observation_quotient import (
    refine_partition_for_linear_observations,
)
from enterprise_math.rank_one_guard_refinement import (
    analyze_rank_one_guard_refinement,
    rank_one_residue_branch_erasure_report,
    rank_one_residue_reachable_patterns,
    rank_one_step_index,
)
from enterprise_math.relation_precision_profile import relation_refinement_cost


def complete_effect_table(default="same"):
    return {
        pattern: default
        for pattern in itertools.product((False, True), repeat=2)
    }


class RankOneGuardRefinementTests(unittest.TestCase):
    def test_rank_one_child_image_is_integer_multiple_of_parent_step(self):
        guards = (
            (0, 1, 2),
            (0, -1, -2),
        )
        parent = ((0, 1, 2),)
        child = ((0, 2), (1,))
        analysis = analyze_rank_one_guard_refinement(guards, parent, child)
        self.assertEqual(analysis.parent_step, (1, -1))
        self.assertEqual(analysis.child_step, (2, -2))
        self.assertEqual(analysis.image_index, 2)
        self.assertEqual(analysis.child_hidden_rank, 1)
        self.assertEqual(
            rank_one_step_index(analysis.parent_step, analysis.child_step),
            2,
        )

    def test_residue_refinement_can_remove_narrow_reachable_pattern(self):
        base = (1, -1)
        parent_step = (1, -1)
        parent_patterns = set(
            rank_one_residue_reachable_patterns(base, parent_step, 1, 0)
        )
        even_parameter_patterns = set(
            rank_one_residue_reachable_patterns(base, parent_step, 2, 0)
        )
        self.assertEqual(
            parent_patterns,
            {(False, True), (True, True), (True, False)},
        )
        self.assertEqual(
            even_parameter_patterns,
            {(False, True), (True, False)},
        )
        self.assertNotIn((True, True), even_parameter_patterns)

    def test_one_relation_degree_can_make_branch_output_exact_without_guard_visibility(self):
        guards = (
            (0, 1, 2),
            (0, -1, -2),
        )
        parent = ((0, 1, 2),)
        child = ((0, 2), (1,))
        singleton = ((0,), (1,), (2,))
        base = (1, -1)  # fine state c=(0,1,0)
        parent_step = (1, -1)

        effects = complete_effect_table("same")
        effects[(True, True)] = "different"
        effects[(False, False)] = "irrelevant-unreachable"

        parent_report = rank_one_branch_erasure_report(
            base, parent_step, effects
        )
        self.assertFalse(parent_report.safe_to_erase)
        self.assertIn((True, True), parent_report.reachable_patterns)

        child_report = rank_one_residue_branch_erasure_report(
            base,
            parent_step,
            modulus=2,
            residue=0,
            branch_effects=effects,
        )
        self.assertTrue(child_report.safe_to_erase)
        self.assertNotIn((True, True), child_report.reachable_patterns)

        # Making both guards exactly observable requires singleton precision:
        # every fine coordinate has a distinct coefficient signature.
        visible_partition = refine_partition_for_linear_observations(
            guards, parent
        )
        self.assertEqual(visible_partition, singleton)

        fine_capacities = (1, 1, 1)
        child_cost = relation_refinement_cost(
            fine_capacities, parent, child
        )
        visible_cost = relation_refinement_cost(
            fine_capacities, parent, visible_partition
        )
        self.assertEqual(child_cost[0], 1)
        self.assertEqual(visible_cost[0], 2)
        self.assertLess(child_cost[0], visible_cost[0])

    def test_child_rank_can_drop_to_zero_when_guard_is_fully_exposed(self):
        guards = (
            (0, 1, 2),
            (0, -1, -2),
        )
        parent = ((0, 1, 2),)
        singleton = ((0,), (1,), (2,))
        analysis = analyze_rank_one_guard_refinement(guards, parent, singleton)
        self.assertEqual(analysis.child_hidden_rank, 0)
        self.assertIsNone(analysis.child_step)
        self.assertIsNone(analysis.image_index)


if __name__ == "__main__":
    unittest.main()
