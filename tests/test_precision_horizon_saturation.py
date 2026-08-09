import itertools
import unittest
from math import gcd

from enterprise_math.precision_horizon_saturation import (
    action_family_stable_class_count,
    clip_integer,
    finite_horizon_class_count,
    finite_horizon_repair_rank,
    finite_horizon_repaired_key,
    horizon_stabilization_depth,
    reachable_action_residues,
    saturation_range_collapses,
    saturated_quotient_step,
    saturated_translation_descends,
    single_action_horizon_class_count,
)
from enterprise_math.precision_locked_actuation import (
    centered_precision_state,
    precision_cell_width,
)


class FiniteHorizonTests(unittest.TestCase):
    @staticmethod
    def _words(actions: tuple[int, ...], horizon: int) -> tuple[tuple[int, ...], ...]:
        words = [()]
        for length in range(1, horizon + 1):
            words.extend(itertools.product(actions, repeat=length))
        return tuple(words)

    @staticmethod
    def _signature(
        error: int,
        precision: int,
        actions: tuple[int, ...],
        horizon: int,
    ) -> tuple[int, ...]:
        return tuple(
            centered_precision_state(error + sum(word), precision).quotient
            for word in FiniteHorizonTests._words(actions, horizon)
        )

    def test_finite_horizon_class_count_matches_direct_operation_word_partition(self) -> None:
        action_families = (
            (1,),
            (2,),
            (3,),
            (-2,),
            (2, 4),
            (3, 5),
            (-2, 3),
        )
        for precision in range(1, 9):
            width = precision_cell_width(precision)
            center = (width - 1) // 2
            errors = tuple(detail - center for detail in range(width))
            for actions in action_families:
                for horizon in range(0, 5):
                    signatures = {
                        self._signature(error, precision, actions, horizon)
                        for error in errors
                    }
                    residues = reachable_action_residues(width, actions, horizon)
                    self.assertEqual(len(signatures), len(residues))
                    self.assertEqual(
                        finite_horizon_class_count(precision, actions, horizon),
                        len(signatures),
                    )

    def test_scalar_repair_rank_is_exactly_the_operation_word_partition(self) -> None:
        for precision in range(2, 9):
            width = precision_cell_width(precision)
            center = (width - 1) // 2
            errors = tuple(detail - center for detail in range(width))
            for actions in ((2,), (3,), (2, 4), (-2, 3), (4, 6)):
                for horizon in range(0, 5):
                    by_rank = {}
                    by_signature = {}
                    for error in errors:
                        rank = finite_horizon_repair_rank(
                            error,
                            precision,
                            actions,
                            horizon,
                        )
                        signature = self._signature(
                            error,
                            precision,
                            actions,
                            horizon,
                        )
                        previous_signature = by_rank.setdefault(rank, signature)
                        self.assertEqual(previous_signature, signature)
                        previous_rank = by_signature.setdefault(signature, rank)
                        self.assertEqual(previous_rank, rank)
                    self.assertEqual(
                        len(by_rank),
                        finite_horizon_class_count(precision, actions, horizon),
                    )

    def test_repaired_key_works_across_neighboring_coarse_cells(self) -> None:
        precision = 5
        actions = (-3, 4)
        horizon = 3
        by_key = {}
        for error in range(-100, 101):
            key = finite_horizon_repaired_key(error, precision, actions, horizon)
            signature = self._signature(error, precision, actions, horizon)
            previous = by_key.setdefault(key, signature)
            self.assertEqual(previous, signature)

    def test_single_action_closed_form(self) -> None:
        for precision in range(1, 16):
            width = precision_cell_width(precision)
            for action in range(-10, 11):
                period = width // gcd(width, abs(action))
                for horizon in range(0, 12):
                    expected = min(horizon + 1, period)
                    self.assertEqual(
                        single_action_horizon_class_count(
                            precision,
                            action,
                            horizon,
                        ),
                        expected,
                    )
                    self.assertEqual(
                        finite_horizon_class_count(
                            precision,
                            (action,),
                            horizon,
                        ),
                        expected,
                    )

    def test_horizon_classes_grow_monotonically_and_stabilize_at_gcd_count(self) -> None:
        for precision in range(1, 12):
            for actions in ((2,), (3,), (2, 4), (3, 5), (-2, 3), (6, 10)):
                stable = action_family_stable_class_count(precision, actions)
                depth = horizon_stabilization_depth(precision, actions)
                self.assertLessEqual(depth, stable - 1)
                counts = [
                    finite_horizon_class_count(precision, actions, horizon)
                    for horizon in range(depth + 3)
                ]
                self.assertEqual(counts, sorted(counts))
                self.assertEqual(counts[depth], stable)
                self.assertTrue(all(count == stable for count in counts[depth:]))


class SaturationTests(unittest.TestCase):
    @staticmethod
    def _brute_descends(
        precision: int,
        increment: int,
        lower: int,
        upper: int,
    ) -> bool:
        width = precision_cell_width(precision)
        center = (width - 1) // 2
        for quotient in range(-8, 9):
            outputs = set()
            for detail in range(width):
                error = width * quotient + detail - center
                output = clip_integer(error + increment, lower, upper)
                outputs.add(centered_precision_state(output, precision).quotient)
            if len(outputs) > 1:
                return False
        return True

    def test_saturation_criterion_matches_bounded_direct_fiber_check(self) -> None:
        for precision in range(1, 10):
            for increment in range(-12, 13):
                for lower in range(-8, 5):
                    for upper in range(lower, 9):
                        expected = self._brute_descends(
                            precision,
                            increment,
                            lower,
                            upper,
                        )
                        self.assertEqual(
                            saturated_translation_descends(
                                precision,
                                increment,
                                lower,
                                upper,
                            ),
                            expected,
                        )

    def test_nontrivial_saturation_does_not_rescue_misaligned_translation(self) -> None:
        for precision in range(2, 10):
            width = precision_cell_width(precision)
            center = (width - 1) // 2
            lower = -3 * width - center
            upper = 3 * width + center
            self.assertFalse(saturation_range_collapses(precision, lower, upper))
            for increment in range(-2 * width, 2 * width + 1):
                self.assertEqual(
                    saturated_translation_descends(
                        precision,
                        increment,
                        lower,
                        upper,
                    ),
                    increment % width == 0,
                )

    def test_trivial_one_cell_saturation_makes_every_translation_coarse_safe(self) -> None:
        precision = 5
        lower = -2
        upper = 2
        self.assertTrue(saturation_range_collapses(precision, lower, upper))
        for increment in range(-30, 31):
            self.assertTrue(
                saturated_translation_descends(
                    precision,
                    increment,
                    lower,
                    upper,
                )
            )

    def test_saturated_quotient_step_matches_every_fine_state_when_compatible(self) -> None:
        for precision in range(1, 8):
            width = precision_cell_width(precision)
            center = (width - 1) // 2
            scenarios = (
                (2 * width, -4 * width, 4 * width),
                (-width, -2 * width + 1, 3 * width - 1),
                (1, -center, center),
            )
            for increment, lower, upper in scenarios:
                if not saturated_translation_descends(
                    precision,
                    increment,
                    lower,
                    upper,
                ):
                    continue
                for quotient in range(-5, 6):
                    expected = saturated_quotient_step(
                        quotient,
                        precision,
                        increment,
                        lower,
                        upper,
                    )
                    for detail in range(width):
                        error = width * quotient + detail - center
                        output = clip_integer(error + increment, lower, upper)
                        self.assertEqual(
                            centered_precision_state(output, precision).quotient,
                            expected,
                        )


if __name__ == "__main__":
    unittest.main()
