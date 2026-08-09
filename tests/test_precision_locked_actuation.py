import itertools
import unittest
from math import gcd

from enterprise_math.precision_hysteresis import (
    ThresholdObservation,
    threshold_observation,
)
from enterprise_math.precision_locked_actuation import (
    action_family_grain,
    admissible_precision_widths,
    admissible_precisions,
    centered_coarse_projection,
    centered_precision_state,
    delayed_precision_locked_trace,
    exact_action_quotient_step,
    odd_power_precision_ladder,
    precision_cell_width,
    precision_from_cell_width,
    shared_exact_action_unit,
    stable_action_cell_width,
    stable_action_precision,
    stable_action_state,
    threshold_observation_from_quotient,
    translation_carry_bit,
    translation_certificate,
    translation_descends,
)


class CenteredPrecisionTests(unittest.TestCase):
    def test_centered_chart_exactly_reconstructs_error_and_threshold(self) -> None:
        for precision in range(1, 16):
            width = precision_cell_width(precision)
            self.assertEqual(precision_from_cell_width(width), precision)
            for error in range(-200, 201):
                state = centered_precision_state(error, precision)
                self.assertEqual(state.reconstruct_error(), error)
                self.assertLessEqual(0, state.detail)
                self.assertLess(state.detail, width)
                self.assertEqual(
                    threshold_observation_from_quotient(state.quotient),
                    threshold_observation(error, precision),
                )

    def test_target_cell_is_exactly_quotient_zero(self) -> None:
        for precision in range(1, 20):
            target_errors = tuple(range(-precision + 1, precision))
            self.assertEqual(len(target_errors), 2 * precision - 1)
            self.assertTrue(
                all(centered_precision_state(error, precision).quotient == 0 for error in target_errors)
            )
            self.assertEqual(
                centered_precision_state(-precision, precision).quotient,
                -1,
            )
            self.assertEqual(
                centered_precision_state(precision, precision).quotient,
                1,
            )

    def test_threshold_sign_map(self) -> None:
        self.assertEqual(threshold_observation_from_quotient(-7), ThresholdObservation.BELOW)
        self.assertEqual(threshold_observation_from_quotient(0), ThresholdObservation.COLLAPSED)
        self.assertEqual(threshold_observation_from_quotient(9), ThresholdObservation.ABOVE)


class TranslationCompatibilityTests(unittest.TestCase):
    def test_translation_certificate_matches_direct_state(self) -> None:
        for precision in range(1, 12):
            width = precision_cell_width(precision)
            for increment in range(-3 * width, 3 * width + 1):
                for error in range(-5 * width, 5 * width + 1):
                    certificate = translation_certificate(error, precision, increment)
                    after = centered_precision_state(error + increment, precision)
                    self.assertEqual(certificate.quotient_after, after.quotient)
                    self.assertEqual(certificate.detail_after, after.detail)
                    self.assertIn(certificate.carry, (0, 1))

    def test_translation_descends_iff_width_divides_increment(self) -> None:
        for precision in range(1, 15):
            width = precision_cell_width(precision)
            for increment in range(-4 * width, 4 * width + 1):
                expected = increment % width == 0
                self.assertEqual(translation_descends(precision, increment), expected)
                outcomes_per_fiber = []
                for quotient in range(-3, 4):
                    outputs = set()
                    for detail in range(width):
                        error = width * quotient + detail - (width - 1) // 2
                        outputs.add(centered_precision_state(error + increment, precision).quotient)
                    outcomes_per_fiber.append(len(outputs))
                if expected:
                    self.assertEqual(set(outcomes_per_fiber), {1})
                else:
                    self.assertEqual(set(outcomes_per_fiber), {2})

    def test_one_step_carry_bit_is_exact_repair(self) -> None:
        precision = 4
        width = precision_cell_width(precision)
        for increment in range(-2 * width, 2 * width + 1):
            by_key = {}
            for error in range(-6 * width, 6 * width + 1):
                state = centered_precision_state(error, precision)
                key = (state.quotient, translation_carry_bit(error, precision, increment))
                output = centered_precision_state(error + increment, precision).quotient
                previous = by_key.setdefault(key, output)
                self.assertEqual(previous, output)


class ActionFamilyClosureTests(unittest.TestCase):
    @staticmethod
    def _reachable_residues(width: int, actions: tuple[int, ...]) -> set[int]:
        reachable = {0}
        while True:
            expanded = set(reachable)
            for residue in reachable:
                for action in actions:
                    expanded.add((residue + action) % width)
            if expanded == reachable:
                return reachable
            reachable = expanded

    def test_gcd_width_is_closed_under_whole_action_family(self) -> None:
        action_families = (
            (2,),
            (3,),
            (2, 4),
            (3, 6),
            (-2, 6),
            (4, 10),
            (-9, 0, 15),
        )
        for precision in range(2, 10):
            width = precision_cell_width(precision)
            for actions in action_families:
                stable_width = stable_action_cell_width(precision, actions)
                expected = width
                for action in actions:
                    expected = gcd(expected, abs(action))
                self.assertEqual(stable_width, expected)
                refined_precision = stable_action_precision(precision, actions)
                self.assertEqual(precision_cell_width(refined_precision), stable_width)
                for error in range(-100, 101):
                    state = stable_action_state(error, precision, actions)
                    for action in actions:
                        direct = stable_action_state(error + action, precision, actions)
                        self.assertEqual(
                            direct.quotient,
                            exact_action_quotient_step(state.quotient, stable_width, action),
                        )
                        self.assertEqual(direct.detail, state.detail)

    def test_gcd_refinement_is_coarsest_for_all_action_words_on_one_fiber(self) -> None:
        for precision in range(2, 10):
            width = precision_cell_width(precision)
            for actions in ((2,), (3,), (2, 4), (3, 6), (2, 6), (4, 10), (-2, 6)):
                stable_width = stable_action_cell_width(precision, actions)
                reachable = self._reachable_residues(width, actions)
                self.assertEqual(reachable, set(range(0, width, stable_width)))
                for left in range(width):
                    for right in range(width):
                        same_stable_subcell = left // stable_width == right // stable_width
                        same_all_future_outputs = all(
                            (left + residue) // width == (right + residue) // width
                            for residue in reachable
                        )
                        self.assertEqual(same_stable_subcell, same_all_future_outputs)

    def test_admissible_precision_spectrum_is_odd_divisor_lattice(self) -> None:
        actions = (90, -150, 210)
        self.assertEqual(action_family_grain(actions), 30)
        self.assertEqual(admissible_precision_widths(actions), (1, 3, 5, 15))
        self.assertEqual(admissible_precisions(actions), (1, 2, 3, 8))
        for precision in admissible_precisions(actions):
            self.assertTrue(all(translation_descends(precision, action) for action in actions))
        for precision in range(1, 12):
            width = precision_cell_width(precision)
            expected = all(action % width == 0 for action in actions)
            self.assertEqual(precision in admissible_precisions(actions), expected)

    def test_all_zero_action_family_has_no_finite_maximum_spectrum(self) -> None:
        with self.assertRaises(ValueError):
            action_family_grain((0, 0))
        with self.assertRaises(ValueError):
            admissible_precision_widths((0, 0))


class AdaptivePrecisionTests(unittest.TestCase):
    def test_nested_centered_projection_is_exact_on_divisible_odd_widths(self) -> None:
        for fine_width in range(1, 22, 2):
            fine_precision = precision_from_cell_width(fine_width)
            for ratio in (1, 3, 5, 7):
                coarse_width = fine_width * ratio
                coarse_precision = precision_from_cell_width(coarse_width)
                for error in range(-250, 251):
                    fine = centered_precision_state(error, fine_precision)
                    coarse = centered_precision_state(error, coarse_precision)
                    self.assertEqual(
                        centered_coarse_projection(
                            fine.quotient,
                            fine_precision,
                            coarse_precision,
                        ),
                        coarse.quotient,
                    )

    def test_shared_exact_action_unit_is_lcm_of_cell_widths(self) -> None:
        precisions = (2, 3, 4)
        self.assertEqual(tuple(precision_cell_width(p) for p in precisions), (3, 5, 7))
        self.assertEqual(shared_exact_action_unit(precisions), 105)
        self.assertTrue(all(translation_descends(p, 105) for p in precisions))
        self.assertFalse(translation_descends(4, 15))

    def test_odd_power_ladder_has_nested_widths(self) -> None:
        ladder = odd_power_precision_ladder(3, 5)
        self.assertEqual(ladder, (1, 2, 5, 14, 41))
        widths = tuple(precision_cell_width(p) for p in ladder)
        self.assertEqual(widths, (1, 3, 9, 27, 81))
        for left, right in zip(widths, widths[1:]):
            self.assertEqual(right % left, 0)


class DelayedActuationTests(unittest.TestCase):
    def test_delayed_multilevel_actions_close_exactly_on_quotient(self) -> None:
        precision = 3
        width = precision_cell_width(precision)
        initial_error = -1
        initial_queue = (2 * width, -width, 0)
        issued = (-2 * width, width, width, 0, -width, 2 * width, -2 * width)
        trace = delayed_precision_locked_trace(
            initial_error,
            precision,
            initial_queue,
            issued,
        )
        self.assertEqual(len(trace), len(issued) + 1)
        initial_detail = centered_precision_state(initial_error, precision).detail
        for sample in trace:
            self.assertEqual(sample.detail, initial_detail)
        for current, following in zip(trace, trace[1:]):
            self.assertEqual(
                following.quotient,
                current.quotient + current.applied_increment // width,
            )
            self.assertEqual(
                following.error,
                current.error + current.applied_increment,
            )

    def test_misaligned_action_breaks_q_only_future_sufficiency(self) -> None:
        precision = 3
        width = precision_cell_width(precision)
        self.assertEqual(width, 5)
        left_error = -2
        right_error = -1
        left = centered_precision_state(left_error, precision)
        right = centered_precision_state(right_error, precision)
        self.assertEqual(left.quotient, right.quotient)
        increment = 4
        self.assertFalse(translation_descends(precision, increment))
        left_after = centered_precision_state(left_error + increment, precision)
        right_after = centered_precision_state(right_error + increment, precision)
        self.assertNotEqual(left_after.quotient, right_after.quotient)
        self.assertNotEqual(
            translation_carry_bit(left_error, precision, increment),
            translation_carry_bit(right_error, precision, increment),
        )


if __name__ == "__main__":
    unittest.main()
