import unittest

from enterprise_math.material_empirical_action_protocol import (
    UNDERRESOLVED_STATE,
    EmpiricalActionProtocolSample,
    action_word_observation_trace,
    compile_empirical_action_protocol,
    protocol_states_future_equivalent,
)


def sample(state_id, deformation, response, **successors):
    return EmpiricalActionProtocolSample(
        state_id=state_id,
        deformation_index=deformation,
        response_sample=response,
        action_successors=tuple(successors.items()),
    )


class MaterialEmpiricalActionProtocolTests(unittest.TestCase):
    def test_equal_current_response_splits_when_one_declared_future_differs(self):
        machine = compile_empirical_action_protocol(
            [
                sample("A", 0, 5, LOAD="C", UNLOAD="E"),
                sample("B", 0, 5, LOAD="D", UNLOAD="E"),
                sample("C", 1, 6, LOAD="C", UNLOAD="E"),
                sample("D", 1, 7, LOAD="D", UNLOAD="E"),
                sample("E", 0, 4, LOAD="A", UNLOAD="E"),
            ]
        )
        self.assertEqual(machine.current_observation["A"], machine.current_observation["B"])
        self.assertFalse(protocol_states_future_equivalent(machine, "A", "B"))
        self.assertGreater(machine.stable_class_count, machine.current_class_count)
        self.assertEqual(
            action_word_observation_trace(machine, "A", ("LOAD",))[1],
            ("MEASURED", 1, 6),
        )
        self.assertEqual(
            action_word_observation_trace(machine, "B", ("LOAD",))[1],
            ("MEASURED", 1, 7),
        )

    def test_history_labels_merge_when_all_declared_futures_are_identical(self):
        machine = compile_empirical_action_protocol(
            [
                sample("history-1", 0, 5, LOAD="C", UNLOAD="D"),
                sample("history-2", 0, 5, UNLOAD="D", LOAD="C"),
                sample("C", 1, 7, LOAD="C", UNLOAD="D"),
                sample("D", 0, 3, LOAD="C", UNLOAD="D"),
            ]
        )
        self.assertEqual(machine.action_names, ("LOAD", "UNLOAD"))
        self.assertTrue(
            protocol_states_future_equivalent(machine, "history-1", "history-2")
        )

    def test_missing_successor_enters_explicit_underresolved_sink(self):
        machine = compile_empirical_action_protocol(
            [
                sample("A", 0, 5, LOAD=None, UNLOAD="B"),
                sample("B", 1, 6, LOAD="B", UNLOAD="A"),
            ]
        )
        self.assertEqual(machine.missing_transitions, (("A", "LOAD"),))
        self.assertEqual(machine.operations["LOAD"]["A"], UNDERRESOLVED_STATE)
        self.assertEqual(
            action_word_observation_trace(machine, "A", ("LOAD", "UNLOAD")),
            (
                ("MEASURED", 0, 5),
                ("UNDERRESOLVED",),
                ("UNDERRESOLVED",),
            ),
        )
        self.assertEqual(
            machine.operations["LOAD"][UNDERRESOLVED_STATE], UNDERRESOLVED_STATE
        )
        self.assertEqual(
            machine.operations["UNLOAD"][UNDERRESOLVED_STATE], UNDERRESOLVED_STATE
        )

    def test_every_measured_state_must_declare_same_action_alphabet(self):
        with self.assertRaises(ValueError):
            compile_empirical_action_protocol(
                [
                    sample("A", 0, 1, LOAD="A", UNLOAD="A"),
                    sample("B", 0, 1, LOAD="B"),
                ]
            )

    def test_explicit_successor_must_be_measured(self):
        with self.assertRaises(ValueError):
            compile_empirical_action_protocol(
                [sample("A", 0, 1, LOAD="UNKNOWN")]
            )

    def test_duplicate_action_name_is_rejected_at_sample_boundary(self):
        with self.assertRaises(ValueError):
            EmpiricalActionProtocolSample(
                state_id="A",
                deformation_index=0,
                response_sample=1,
                action_successors=(("LOAD", "A"), ("LOAD", None)),
            )

    def test_undeclared_action_word_is_rejected(self):
        machine = compile_empirical_action_protocol(
            [sample("A", 0, 1, LOAD="A")]
        )
        with self.assertRaises(ValueError):
            action_word_observation_trace(machine, "A", ("UNLOAD",))


if __name__ == "__main__":
    unittest.main()
