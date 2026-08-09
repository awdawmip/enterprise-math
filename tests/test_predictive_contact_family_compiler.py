import unittest

from enterprise_math.predictive_contact_family import (
    family_contact_coordinate,
)
from enterprise_math.predictive_quotient import stable_predictive_partition


class ContactActionFamilyCompilerTests(unittest.TestCase):
    def test_generic_stable_compiler_partition_equals_gcd_coordinate_fibers(self) -> None:
        cases = (
            (7, (2, 4), 42),
            (11, (4, 6), 54),
            (17, (6, 10, 14), 72),
            (20, (9, 15), 90),
        )
        for precision, magnitudes, cap in cases:
            states = tuple(range(cap + 1))
            actions = {}
            for magnitude in magnitudes:
                actions[f"sep_{magnitude}"] = (
                    lambda gap, m=magnitude, c=cap: min(c, gap + m)
                )
                actions[f"close_{magnitude}"] = (
                    lambda gap, m=magnitude: max(0, gap - m)
                )
            observe = lambda gap, d=precision: gap < d
            stable = stable_predictive_partition(states, actions, observe)

            by_label = {}
            by_coordinate = {}
            for state, label in zip(states, stable.partition):
                coordinate = family_contact_coordinate(state, precision, magnitudes)
                previous_coordinate = by_label.setdefault(label, coordinate)
                self.assertEqual(previous_coordinate, coordinate)
                previous_label = by_coordinate.setdefault(coordinate, label)
                self.assertEqual(previous_label, label)

            expected_coordinates = {
                family_contact_coordinate(state, precision, magnitudes)
                for state in states
            }
            self.assertEqual(stable.block_count, len(expected_coordinates))


if __name__ == "__main__":
    unittest.main()
