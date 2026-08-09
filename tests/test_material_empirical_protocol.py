import unittest

from enterprise_math.material_empirical_protocol import (
    UNDERRESOLVED_STATE,
    EmpiricalProtocolSample,
    compile_empirical_material_protocol,
    first_future_observation_difference,
    protocol_states_future_equivalent,
)


class MaterialEmpiricalProtocolTests(unittest.TestCase):
    def test_same_current_material_observation_can_split_by_measured_future(self):
        machine = compile_empirical_material_protocol(
            (
                EmpiricalProtocolSample("history_a", 2, 50, "a_next"),
                EmpiricalProtocolSample("history_b", 2, 50, "b_next"),
                EmpiricalProtocolSample("a_next", 1, 40, None),
                EmpiricalProtocolSample("b_next", 1, 30, None),
            )
        )
        self.assertEqual(
            machine.current_observation["history_a"],
            machine.current_observation["history_b"],
        )
        self.assertFalse(
            protocol_states_future_equivalent(machine, "history_a", "history_b")
        )
        self.assertEqual(
            first_future_observation_difference(machine, "history_a", "history_b"),
            1,
        )
        self.assertGreater(machine.stable_class_count, machine.current_class_count)

    def test_identical_late_cycle_futures_merge_without_named_cycle_count(self):
        machine = compile_empirical_material_protocol(
            (
                EmpiricalProtocolSample("cycle2_peak", 3, 80, "cycle2_return"),
                EmpiricalProtocolSample("cycle3_peak", 3, 80, "cycle3_return"),
                EmpiricalProtocolSample("cycle2_return", 1, 30, "steady"),
                EmpiricalProtocolSample("cycle3_return", 1, 30, "steady"),
                EmpiricalProtocolSample("steady", 0, 0, "steady"),
            )
        )
        self.assertTrue(
            protocol_states_future_equivalent(machine, "cycle2_peak", "cycle3_peak")
        )
        self.assertTrue(
            protocol_states_future_equivalent(machine, "cycle2_return", "cycle3_return")
        )
        self.assertIsNone(
            first_future_observation_difference(machine, "cycle2_peak", "cycle3_peak")
        )

    def test_unmeasured_future_is_explicit_underresolved_not_wraparound(self):
        machine = compile_empirical_material_protocol(
            (EmpiricalProtocolSample("last_measured", 0, 0, None),)
        )
        self.assertEqual(
            machine.next_operation["last_measured"],
            UNDERRESOLVED_STATE,
        )
        self.assertEqual(
            machine.next_operation[UNDERRESOLVED_STATE],
            UNDERRESOLVED_STATE,
        )
        self.assertEqual(
            first_future_observation_difference(
                machine,
                "last_measured",
                UNDERRESOLVED_STATE,
            ),
            0,
        )

    def test_two_terminal_states_with_same_current_measurement_are_prediction_equivalent(self):
        machine = compile_empirical_material_protocol(
            (
                EmpiricalProtocolSample("left", 2, 50, None),
                EmpiricalProtocolSample("right", 2, 50, None),
            )
        )
        self.assertTrue(protocol_states_future_equivalent(machine, "left", "right"))
        self.assertIsNone(first_future_observation_difference(machine, "left", "right"))
        # This is equivalence of the declared empirical prediction interface;
        # both histories become UNDERRESOLVED after one NEXT.  It is not a claim
        # that their unknown physical futures are equal.

    def test_delayed_difference_horizon_can_exceed_one_step(self):
        machine = compile_empirical_material_protocol(
            (
                EmpiricalProtocolSample("a0", 2, 50, "a1"),
                EmpiricalProtocolSample("b0", 2, 50, "b1"),
                EmpiricalProtocolSample("a1", 1, 40, "a2"),
                EmpiricalProtocolSample("b1", 1, 40, "b2"),
                EmpiricalProtocolSample("a2", 0, 20, None),
                EmpiricalProtocolSample("b2", 0, 10, None),
            )
        )
        self.assertEqual(first_future_observation_difference(machine, "a0", "b0"), 2)
        self.assertFalse(protocol_states_future_equivalent(machine, "a0", "b0"))

    def test_invalid_ids_and_dangling_successors_are_rejected(self):
        with self.assertRaises(ValueError):
            EmpiricalProtocolSample(UNDERRESOLVED_STATE, 0, 0, None)
        with self.assertRaises(ValueError):
            compile_empirical_material_protocol(
                (
                    EmpiricalProtocolSample("dup", 0, 0, None),
                    EmpiricalProtocolSample("dup", 1, 1, None),
                )
            )
        with self.assertRaises(ValueError):
            compile_empirical_material_protocol(
                (EmpiricalProtocolSample("a", 0, 0, "missing"),)
            )


if __name__ == "__main__":
    unittest.main()
