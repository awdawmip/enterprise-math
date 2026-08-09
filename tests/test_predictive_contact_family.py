import itertools
import unittest
from math import gcd

from enterprise_math.predictive_contact_family import (
    action_family_gcd,
    apply_coordinate_action,
    apply_gap_action,
    close_coordinate,
    coordinate_cap,
    coordinate_future_signature,
    family_contact_coordinate,
    family_contact_from_coordinate,
    family_fiber_bounds,
    family_fiber_size,
    family_future_signature,
    separate_coordinate,
)


class ContactActionFamilyTests(unittest.TestCase):
    def test_family_gcd(self) -> None:
        self.assertEqual(action_family_gcd((6, 10, 14)), 2)
        self.assertEqual(action_family_gcd((15, 30)), 15)
        self.assertEqual(action_family_gcd((7,)), 7)

    def test_contact_observation_factors_through_coordinate(self) -> None:
        families = ((1,), (2, 4), (6, 10), (9, 15, 21))
        for precision in range(1, 30):
            for magnitudes in families:
                for gap in range(0, 80):
                    coordinate = family_contact_coordinate(gap, precision, magnitudes)
                    self.assertEqual(
                        family_contact_from_coordinate(coordinate),
                        gap < precision,
                    )

    def test_every_declared_action_transports_coordinate_exactly(self) -> None:
        families = ((2, 4), (6, 10), (6, 10, 14), (9, 15))
        for precision in range(1, 25):
            for magnitudes in families:
                for gap in range(0, 80):
                    coordinate = family_contact_coordinate(gap, precision, magnitudes)
                    for magnitude in magnitudes:
                        separated_gap = gap + magnitude
                        self.assertEqual(
                            family_contact_coordinate(
                                separated_gap,
                                precision,
                                magnitudes,
                            ),
                            separate_coordinate(coordinate, magnitude, magnitudes),
                        )

                        closed_gap = max(0, gap - magnitude)
                        self.assertEqual(
                            family_contact_coordinate(
                                closed_gap,
                                precision,
                                magnitudes,
                            ),
                            close_coordinate(
                                coordinate,
                                precision,
                                magnitude,
                                magnitudes,
                            ),
                        )

    def test_physical_and_coordinate_future_signatures_match_for_all_short_words(self) -> None:
        for precision, magnitudes in (
            (5, (2, 4)),
            (9, (4, 6)),
            (13, (6, 10)),
            (17, (6, 10, 14)),
        ):
            signed_actions = tuple(
                action
                for magnitude in magnitudes
                for action in (magnitude, -magnitude)
            )
            for gap in range(0, 35):
                coordinate = family_contact_coordinate(gap, precision, magnitudes)
                for length in range(0, 5):
                    for word in itertools.product(signed_actions, repeat=length):
                        self.assertEqual(
                            family_future_signature(gap, precision, word),
                            coordinate_future_signature(
                                coordinate,
                                precision,
                                magnitudes,
                                word,
                            ),
                        )

    def test_same_coordinate_fibers_have_identical_bounded_future_language(self) -> None:
        precision = 17
        magnitudes = (6, 10, 14)
        signed_actions = tuple(
            action
            for magnitude in magnitudes
            for action in (magnitude, -magnitude)
        )
        by_coordinate = {}
        for gap in range(0, 80):
            coordinate = family_contact_coordinate(gap, precision, magnitudes)
            by_coordinate.setdefault(coordinate, []).append(gap)
        for gaps in by_coordinate.values():
            if len(gaps) < 2:
                continue
            left, right = gaps[0], gaps[-1]
            for length in range(0, 5):
                for word in itertools.product(signed_actions, repeat=length):
                    self.assertEqual(
                        family_future_signature(left, precision, word),
                        family_future_signature(right, precision, word),
                    )

    @staticmethod
    def _bounded_distinguishing_word(
        precision: int,
        magnitudes: tuple[int, ...],
        left_coordinate: int,
        right_coordinate: int,
    ) -> tuple[int, ...] | None:
        if left_coordinate == right_coordinate:
            return ()
        signed_actions = tuple(
            action
            for magnitude in magnitudes
            for action in (magnitude, -magnitude)
        )
        # Finite BFS in coordinate space. The theorem says a word must exist;
        # bounded search is an executable audit rather than the proof.
        frontier = {(left_coordinate, right_coordinate): ()}
        seen = set(frontier)
        max_depth = 18
        for _depth in range(max_depth + 1):
            next_frontier = {}
            for (left, right), word in frontier.items():
                if family_contact_from_coordinate(left) != family_contact_from_coordinate(right):
                    return word
                for action in signed_actions:
                    next_left = apply_coordinate_action(left, precision, action, magnitudes)
                    next_right = apply_coordinate_action(right, precision, action, magnitudes)
                    pair = (next_left, next_right)
                    if pair not in seen:
                        seen.add(pair)
                        next_frontier[pair] = word + (action,)
            frontier = next_frontier
        return None

    def test_distinct_coordinate_values_are_finitely_distinguishable_bounded_audit(self) -> None:
        cases = (
            (7, (2, 4)),
            (11, (4, 6)),
            (17, (6, 10, 14)),
        )
        for precision, magnitudes in cases:
            coordinates = sorted(
                {
                    family_contact_coordinate(gap, precision, magnitudes)
                    for gap in range(0, 60)
                }
            )
            for left, right in itertools.combinations(coordinates, 2):
                word = self._bounded_distinguishing_word(
                    precision,
                    magnitudes,
                    left,
                    right,
                )
                self.assertIsNotNone(
                    word,
                    msg=(precision, magnitudes, left, right),
                )
                if word is None:
                    continue
                left_gap = family_fiber_bounds(left, precision, magnitudes)[0]
                right_gap = family_fiber_bounds(right, precision, magnitudes)[0]
                left_signature = family_future_signature(left_gap, precision, word)
                right_signature = family_future_signature(right_gap, precision, word)
                self.assertNotEqual(left_signature, right_signature)

    def test_fiber_bounds_and_sizes(self) -> None:
        for precision, magnitudes in (
            (10, (6, 10)),
            (17, (6, 10, 14)),
            (20, (9, 15)),
        ):
            step = action_family_gcd(magnitudes)
            cap = coordinate_cap(precision, magnitudes)
            seen = set()
            for gap in range(0, 100):
                coordinate = family_contact_coordinate(gap, precision, magnitudes)
                if coordinate not in seen:
                    lower, upper = family_fiber_bounds(
                        coordinate,
                        precision,
                        magnitudes,
                    )
                    self.assertLessEqual(lower, gap if coordinate == family_contact_coordinate(gap, precision, magnitudes) else upper)
                    self.assertEqual(
                        family_fiber_size(coordinate, precision, magnitudes),
                        upper - lower + 1,
                    )
                    if coordinate < cap:
                        self.assertEqual(upper - lower + 1, step)
                    else:
                        self.assertLessEqual(upper - lower + 1, step)
                    seen.add(coordinate)

    def test_normalized_action_family_has_gcd_one(self) -> None:
        for magnitudes in ((6, 10), (6, 10, 14), (9, 15, 21), (12, 18, 30)):
            step = action_family_gcd(magnitudes)
            normalized = tuple(value // step for value in magnitudes)
            current = normalized[0]
            for value in normalized[1:]:
                current = gcd(current, value)
            self.assertEqual(current, 1)


if __name__ == "__main__":
    unittest.main()
