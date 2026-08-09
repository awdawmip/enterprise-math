import unittest

from enterprise_math.material_empirical_action_protocol import (
    EmpiricalActionProtocolSample,
    compile_empirical_action_protocol,
)
from enterprise_math.material_empirical_protocol_coverage import (
    empirical_protocol_coverage,
    shortest_underresolved_action_word,
)


def sample(state_id, deformation, response, **successors):
    return EmpiricalActionProtocolSample(
        state_id=state_id,
        deformation_index=deformation,
        response_sample=response,
        action_successors=tuple(successors.items()),
    )


class MaterialEmpiricalProtocolCoverageTests(unittest.TestCase):
    def test_shortest_underresolved_depth_is_exact(self):
        machine = compile_empirical_action_protocol(
            [
                sample("A", 0, 5, LOAD="B", HOLD="A"),
                sample("B", 1, 6, LOAD=None, HOLD="B"),
            ]
        )
        self.assertEqual(shortest_underresolved_action_word(machine, "A"), ("LOAD", "LOAD"))
        self.assertEqual(shortest_underresolved_action_word(machine, "B"), ("LOAD",))
        report = empirical_protocol_coverage(machine)
        by_id = {item.state_id: item for item in report.states}
        self.assertEqual(by_id["A"].first_underresolved_depth, 2)
        self.assertEqual(by_id["B"].first_underresolved_depth, 1)

    def test_action_closed_measured_component_has_unbounded_measured_future(self):
        machine = compile_empirical_action_protocol(
            [
                sample("A", 0, 5, LOAD=None, HOLD="A"),
                sample("C", 0, 7, LOAD="D", HOLD="C"),
                sample("D", 1, 8, LOAD="D", HOLD="C"),
            ]
        )
        report = empirical_protocol_coverage(machine)
        self.assertEqual(report.fully_measured_state_ids, ("C", "D"))
        self.assertEqual(report.eventually_underresolved_state_ids, ("A",))
        self.assertIsNone(shortest_underresolved_action_word(machine, "C"))
        self.assertIsNone(shortest_underresolved_action_word(machine, "D"))

    def test_shortest_witness_is_deterministic_under_sorted_action_names(self):
        machine = compile_empirical_action_protocol(
            [sample("A", 0, 5, UNLOAD=None, LOAD=None)]
        )
        self.assertEqual(machine.action_names, ("LOAD", "UNLOAD"))
        self.assertEqual(shortest_underresolved_action_word(machine, "A"), ("LOAD",))

    def test_coverage_does_not_confuse_predictive_equivalence_with_measurement_closure(self):
        machine = compile_empirical_action_protocol(
            [
                sample("A", 0, 5, STEP=None),
                sample("B", 0, 5, STEP=None),
            ]
        )
        self.assertEqual(
            machine.stable_partition["A"], machine.stable_partition["B"]
        )
        report = empirical_protocol_coverage(machine)
        self.assertEqual(report.fully_measured_state_ids, ())
        self.assertEqual(report.eventually_underresolved_state_ids, ("A", "B"))

    def test_only_measured_start_states_are_accepted(self):
        machine = compile_empirical_action_protocol(
            [sample("A", 0, 5, STEP=None)]
        )
        with self.assertRaises(ValueError):
            shortest_underresolved_action_word(machine, "UNKNOWN")


if __name__ == "__main__":
    unittest.main()
