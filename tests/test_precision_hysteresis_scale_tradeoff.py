import itertools
import unittest

from enterprise_math.precision_hysteresis import (
    RelayState,
    compatible_relay_states,
    precision_relay,
)


def classical_variable_hysteresis(
    error: int,
    state: RelayState,
    half_width: int,
) -> RelayState:
    if error <= -half_width:
        return RelayState.ON
    if error >= half_width:
        return RelayState.OFF
    return state


class PrecisionHysteresisScaleTradeoffTests(unittest.TestCase):
    def test_black_box_equivalence_under_variable_precision_schedules(self) -> None:
        error_alphabet = range(-3, 4)
        precision_alphabet = range(1, 4)

        for errors in itertools.product(error_alphabet, repeat=4):
            for precisions in itertools.product(precision_alphabet, repeat=4):
                for initial_state in RelayState:
                    e002_state = initial_state
                    classical_state = initial_state
                    for error, precision in zip(errors, precisions):
                        e002_state = precision_relay(error, e002_state, precision)
                        classical_state = classical_variable_hysteresis(
                            error,
                            classical_state,
                            precision,
                        )
                        self.assertIs(e002_state, classical_state)

    def test_exact_immediate_switch_extinction_threshold(self) -> None:
        for magnitude in range(1, 10):
            negative_error = -magnitude
            positive_error = magnitude

            for precision in range(1, 12):
                off_output = precision_relay(
                    negative_error,
                    RelayState.OFF,
                    precision,
                )
                on_output = precision_relay(
                    positive_error,
                    RelayState.ON,
                    precision,
                )

                if precision <= magnitude:
                    self.assertIs(off_output, RelayState.ON)
                    self.assertIs(on_output, RelayState.OFF)
                else:
                    self.assertIs(off_output, RelayState.OFF)
                    self.assertIs(on_output, RelayState.ON)

            extinction_precision = magnitude + 1
            self.assertIs(
                precision_relay(
                    negative_error,
                    RelayState.OFF,
                    extinction_precision,
                ),
                RelayState.OFF,
            )
            self.assertIs(
                precision_relay(
                    positive_error,
                    RelayState.ON,
                    extinction_precision,
                ),
                RelayState.ON,
            )

    def test_robust_immunity_detection_window_is_exact(self) -> None:
        for noise_radius in range(0, 7):
            for excursion in range(1, 15):
                feasible = []
                for precision in range(1, 16):
                    target_off = compatible_relay_states(
                        0,
                        RelayState.OFF,
                        precision,
                        noise_radius,
                    )
                    target_on = compatible_relay_states(
                        0,
                        RelayState.ON,
                        precision,
                        noise_radius,
                    )
                    negative_excursion = compatible_relay_states(
                        -excursion,
                        RelayState.OFF,
                        precision,
                        noise_radius,
                    )
                    positive_excursion = compatible_relay_states(
                        excursion,
                        RelayState.ON,
                        precision,
                        noise_radius,
                    )

                    target_immune = (
                        target_off == (RelayState.OFF,)
                        and target_on == (RelayState.ON,)
                    )
                    robust_correct = (
                        negative_excursion == (RelayState.ON,)
                        and positive_excursion == (RelayState.OFF,)
                    )
                    if target_immune and robust_correct:
                        feasible.append(precision)

                expected = list(
                    range(
                        noise_radius + 1,
                        excursion - noise_radius + 1,
                    )
                )
                expected = [precision for precision in expected if precision <= 15]
                self.assertEqual(feasible, expected)
                self.assertEqual(bool(feasible), excursion >= 2 * noise_radius + 1)

                if excursion >= 2 * noise_radius + 1:
                    self.assertEqual(len(feasible), excursion - 2 * noise_radius)


if __name__ == "__main__":
    unittest.main()
