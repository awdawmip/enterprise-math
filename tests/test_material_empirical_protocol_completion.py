import unittest

from enterprise_math.material_empirical_action_protocol import (
    EmpiricalActionProtocolSample,
    compile_empirical_action_protocol,
)
from enterprise_math.material_empirical_protocol_completion import (
    AFTER_COARSENS,
    AFTER_REFINES,
    INCOMPARABLE,
    compare_protocol_completion,
)


def sample(state_id, deformation, response, **successors):
    return EmpiricalActionProtocolSample(
        state_id=state_id,
        deformation_index=deformation,
        response_sample=response,
        action_successors=tuple(successors.items()),
    )


class MaterialEmpiricalProtocolCompletionTests(unittest.TestCase):
    def test_measuring_one_missing_edge_can_split_a_predictive_class(self):
        before = compile_empirical_action_protocol(
            [
                sample("A", 0, 5, STEP=None),
                sample("B", 0, 5, STEP=None),
                sample("X", 1, 7, STEP="X"),
            ]
        )
        after = compile_empirical_action_protocol(
            [
                sample("A", 0, 5, STEP="X"),
                sample("B", 0, 5, STEP=None),
                sample("X", 1, 7, STEP="X"),
            ]
        )
        report = compare_protocol_completion(before, after)
        self.assertEqual(report.relation, AFTER_REFINES)
        self.assertEqual(report.newly_split_pairs, (("A", "B"),))
        self.assertEqual(
            (report.before_shared_class_count, report.after_shared_class_count),
            (2, 3),
        )

    def test_measuring_one_missing_edge_can_merge_predictive_classes(self):
        before = compile_empirical_action_protocol(
            [
                sample("A", 0, 5, STEP=None),
                sample("B", 0, 5, STEP="X"),
                sample("X", 1, 7, STEP="X"),
            ]
        )
        after = compile_empirical_action_protocol(
            [
                sample("A", 0, 5, STEP="X"),
                sample("B", 0, 5, STEP="X"),
                sample("X", 1, 7, STEP="X"),
            ]
        )
        report = compare_protocol_completion(before, after)
        self.assertEqual(report.relation, AFTER_COARSENS)
        self.assertEqual(report.newly_merged_pairs, (("A", "B"),))
        self.assertEqual(
            (report.before_shared_class_count, report.after_shared_class_count),
            (3, 2),
        )

    def test_one_completion_can_split_and_merge_different_history_pairs(self):
        before = compile_empirical_action_protocol(
            [
                sample("A", 0, 5, STEP=None),
                sample("B", 0, 5, STEP=None),
                sample("C", 0, 8, STEP=None),
                sample("D", 0, 8, STEP="Y"),
                sample("X", 1, 6, STEP="X"),
                sample("Y", 1, 9, STEP="Y"),
            ]
        )
        after = compile_empirical_action_protocol(
            [
                sample("A", 0, 5, STEP="X"),
                sample("B", 0, 5, STEP=None),
                sample("C", 0, 8, STEP="Y"),
                sample("D", 0, 8, STEP="Y"),
                sample("X", 1, 6, STEP="X"),
                sample("Y", 1, 9, STEP="Y"),
            ]
        )
        report = compare_protocol_completion(before, after)
        self.assertEqual(report.relation, INCOMPARABLE)
        self.assertIn(("A", "B"), report.newly_split_pairs)
        self.assertIn(("C", "D"), report.newly_merged_pairs)

    def test_completion_may_add_new_measured_states(self):
        before = compile_empirical_action_protocol(
            [sample("A", 0, 5, STEP=None)]
        )
        after = compile_empirical_action_protocol(
            [
                sample("A", 0, 5, STEP="X"),
                sample("X", 1, 6, STEP="X"),
            ]
        )
        report = compare_protocol_completion(before, after)
        self.assertEqual(report.shared_state_ids, ("A",))

    def test_completion_cannot_change_existing_observation(self):
        before = compile_empirical_action_protocol(
            [sample("A", 0, 5, STEP=None)]
        )
        after = compile_empirical_action_protocol(
            [sample("A", 0, 6, STEP=None)]
        )
        with self.assertRaises(ValueError):
            compare_protocol_completion(before, after)

    def test_completion_cannot_rewrite_existing_measured_transition(self):
        before = compile_empirical_action_protocol(
            [
                sample("A", 0, 5, STEP="X"),
                sample("X", 1, 6, STEP="X"),
                sample("Y", 1, 7, STEP="Y"),
            ]
        )
        after = compile_empirical_action_protocol(
            [
                sample("A", 0, 5, STEP="Y"),
                sample("X", 1, 6, STEP="X"),
                sample("Y", 1, 7, STEP="Y"),
            ]
        )
        with self.assertRaises(ValueError):
            compare_protocol_completion(before, after)

    def test_completion_cannot_remove_measured_state_or_action(self):
        before = compile_empirical_action_protocol(
            [
                sample("A", 0, 5, LOAD="A", HOLD=None),
                sample("B", 1, 6, LOAD="B", HOLD=None),
            ]
        )
        removed_state = compile_empirical_action_protocol(
            [sample("A", 0, 5, LOAD="A", HOLD=None)]
        )
        with self.assertRaises(ValueError):
            compare_protocol_completion(before, removed_state)

        changed_actions = compile_empirical_action_protocol(
            [
                sample("A", 0, 5, LOAD="A", UNLOAD=None),
                sample("B", 1, 6, LOAD="B", UNLOAD=None),
            ]
        )
        with self.assertRaises(ValueError):
            compare_protocol_completion(before, changed_actions)


if __name__ == "__main__":
    unittest.main()
