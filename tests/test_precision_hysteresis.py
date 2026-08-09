import itertools
import math
import unittest

from enterprise_math.precision_hysteresis import (
    RelayState,
    ThresholdObservation,
    apply_relay_to_errors,
    compatible_relay_states,
    minimum_switch_spacing,
    noise_immunity_precision,
    one_step_future_key,
    precision_relay,
    switch_count_upper_bound,
    switch_times,
    thermostat_invariant_bounds,
    thermostat_step,
    threshold_observation,
    total_variation,
    two_relay_outputs,
    upper_switch_return,
)


class PrecisionHysteresisTests(unittest.TestCase):
    def test_target_centered_partition_and_symmetry(self) -> None:
        for precision in range(1, 7):
            collapsed = []
            for error in range(-20, 21):
                observation = threshold_observation(error, precision)
                if error <= -precision:
                    self.assertIs(observation, ThresholdObservation.BELOW)
                elif error >= precision:
                    self.assertIs(observation, ThresholdObservation.ABOVE)
                else:
                    self.assertIs(observation, ThresholdObservation.COLLAPSED)
                    collapsed.append(error)

                reflected = threshold_observation(-error, precision)
                expected_reflection = {
                    ThresholdObservation.BELOW: ThresholdObservation.ABOVE,
                    ThresholdObservation.ABOVE: ThresholdObservation.BELOW,
                    ThresholdObservation.COLLAPSED: ThresholdObservation.COLLAPSED,
                }[observation]
                self.assertIs(reflected, expected_reflection)

            self.assertEqual(len(collapsed), 2 * precision - 1)

    def test_precision_plus_persistence_is_symmetric_hysteretic_relay(self) -> None:
        for precision in range(1, 6):
            for error in range(-12, 13):
                for state in RelayState:
                    output = precision_relay(error, state, precision)
                    if error <= -precision:
                        self.assertIs(output, RelayState.ON)
                    elif error >= precision:
                        self.assertIs(output, RelayState.OFF)
                    else:
                        self.assertIs(output, state)

    def test_exact_noise_immunity_threshold(self) -> None:
        for noise_radius in range(0, 8):
            precision = noise_immunity_precision(noise_radius)
            self.assertEqual(precision, noise_radius + 1)
            for state in RelayState:
                self.assertEqual(
                    compatible_relay_states(0, state, precision, noise_radius),
                    (state,),
                )

            if noise_radius > 0:
                for smaller_precision in range(1, noise_radius + 1):
                    self.assertIn(
                        RelayState.OFF,
                        compatible_relay_states(
                            0,
                            RelayState.ON,
                            smaller_precision,
                            noise_radius,
                        ),
                    )
                    self.assertIn(
                        RelayState.ON,
                        compatible_relay_states(
                            0,
                            RelayState.OFF,
                            smaller_precision,
                            noise_radius,
                        ),
                    )

    def test_bounded_noise_may_must_bands(self) -> None:
        for precision in range(1, 6):
            for noise_radius in range(0, 5):
                for true_error in range(-15, 16):
                    off_possible = set(
                        compatible_relay_states(
                            true_error,
                            RelayState.OFF,
                            precision,
                            noise_radius,
                        )
                    )
                    if true_error <= -precision - noise_radius:
                        self.assertEqual(off_possible, {RelayState.ON})
                    elif true_error >= -precision + noise_radius + 1:
                        self.assertEqual(off_possible, {RelayState.OFF})
                    else:
                        self.assertEqual(off_possible, {RelayState.OFF, RelayState.ON})

                    on_possible = set(
                        compatible_relay_states(
                            true_error,
                            RelayState.ON,
                            precision,
                            noise_radius,
                        )
                    )
                    if true_error <= precision - noise_radius - 1:
                        self.assertEqual(on_possible, {RelayState.ON})
                    elif true_error >= precision + noise_radius:
                        self.assertEqual(on_possible, {RelayState.OFF})
                    else:
                        self.assertEqual(on_possible, {RelayState.OFF, RelayState.ON})

    def test_switch_spacing_and_variation_bounds_exhaustively(self) -> None:
        alphabet = range(-4, 5)
        for errors in itertools.product(alphabet, repeat=4):
            variation = total_variation(errors)
            for precision in range(1, 4):
                states = apply_relay_to_errors(errors, RelayState.OFF, precision)
                times = switch_times(states)
                switches = len(times)
                self.assertLessEqual(
                    switches,
                    switch_count_upper_bound(precision, variation),
                )

                maximum_step = max(
                    (abs(right - left) for left, right in zip(errors, errors[1:])),
                    default=0,
                )
                if maximum_step > 0:
                    guaranteed = minimum_switch_spacing(precision, maximum_step)
                    for left, right in zip(times, times[1:]):
                        self.assertGreaterEqual(right - left, guaranteed)

    def test_coarse_observation_and_mode_are_not_future_sufficient(self) -> None:
        precision = 2
        heat_step = 1
        cool_step = 1
        state = RelayState.ON
        left_error = 0
        right_error = 1

        self.assertIs(
            threshold_observation(left_error, precision),
            ThresholdObservation.COLLAPSED,
        )
        self.assertIs(
            threshold_observation(right_error, precision),
            ThresholdObservation.COLLAPSED,
        )
        self.assertIs(precision_relay(left_error, state, precision), RelayState.ON)
        self.assertIs(precision_relay(right_error, state, precision), RelayState.ON)
        self.assertNotEqual(
            two_relay_outputs(
                left_error,
                state,
                precision,
                heat_step,
                cool_step,
            ),
            two_relay_outputs(
                right_error,
                state,
                precision,
                heat_step,
                cool_step,
            ),
        )

    def test_one_bit_repair_is_sufficient_for_one_additional_decision(self) -> None:
        for precision in range(1, 5):
            for heat_step in range(1, 5):
                for cool_step in range(1, 5):
                    outputs_by_key = {}
                    for error in range(-10, 11):
                        for state in RelayState:
                            key = one_step_future_key(
                                error,
                                state,
                                precision,
                                heat_step,
                                cool_step,
                            )
                            outputs = two_relay_outputs(
                                error,
                                state,
                                precision,
                                heat_step,
                                cool_step,
                            )
                            previous = outputs_by_key.setdefault(key, outputs)
                            self.assertEqual(previous, outputs)

    def test_noiseless_thermostat_has_finite_invariant_band(self) -> None:
        for precision in range(1, 6):
            for heat_step in range(1, 5):
                for cool_step in range(1, 5):
                    lower, upper = thermostat_invariant_bounds(
                        precision,
                        heat_step,
                        cool_step,
                    )
                    self.assertEqual(lower, -precision - cool_step + 1)
                    self.assertEqual(upper, precision + heat_step - 1)

                    for error in range(lower, upper + 1):
                        for state in RelayState:
                            next_error, _ = thermostat_step(
                                error,
                                state,
                                precision,
                                heat_step,
                                cool_step,
                            )
                            self.assertGreaterEqual(next_error, lower)
                            self.assertLessEqual(next_error, upper)

                    for start in (lower - 12, upper + 12):
                        error = start
                        state = RelayState.OFF
                        for _ in range(100):
                            if lower <= error <= upper:
                                break
                            error, state = thermostat_step(
                                error,
                                state,
                                precision,
                                heat_step,
                                cool_step,
                            )
                        self.assertGreaterEqual(error, lower)
                        self.assertLessEqual(error, upper)

    def test_upper_switch_return_bounds_and_residue_invariance(self) -> None:
        for precision in range(1, 7):
            for heat_step in range(1, 7):
                for cool_step in range(1, 7):
                    modulus = math.gcd(heat_step, cool_step)
                    for upper_error in range(precision, precision + heat_step):
                        result = upper_switch_return(
                            upper_error,
                            precision,
                            heat_step,
                            cool_step,
                        )
                        lower_error = result["lower_error"]
                        next_upper = result["next_upper_error"]
                        self.assertGreaterEqual(
                            lower_error,
                            -precision - cool_step + 1,
                        )
                        self.assertLessEqual(lower_error, -precision)
                        self.assertGreaterEqual(next_upper, precision)
                        self.assertLessEqual(next_upper, precision + heat_step - 1)
                        self.assertEqual(
                            (next_upper - upper_error) % modulus,
                            0,
                        )

    def test_equal_plant_steps_fix_each_upper_switch_sample(self) -> None:
        for precision in range(1, 8):
            for step in range(1, 8):
                for upper_error in range(precision, precision + step):
                    result = upper_switch_return(
                        upper_error,
                        precision,
                        step,
                        step,
                    )
                    self.assertEqual(result["next_upper_error"], upper_error)


if __name__ == "__main__":
    unittest.main()
