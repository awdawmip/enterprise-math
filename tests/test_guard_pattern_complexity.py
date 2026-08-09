import math
import unittest

from enterprise_math.guard_pattern_complexity import (
    arrangement_total_face_bound,
    arrangement_total_face_recurrence,
    hidden_guard_pattern_bound,
    nonconstant_guard_count,
)


class GuardPatternComplexityTests(unittest.TestCase):
    def test_dimension_zero_has_one_face(self):
        for hyperplanes in range(0, 12):
            self.assertEqual(arrangement_total_face_bound(hyperplanes, 0), 1)

    def test_rank_one_and_rank_two_closed_forms(self):
        for q in range(0, 15):
            self.assertEqual(arrangement_total_face_bound(q, 1), 2 * q + 1)
            self.assertEqual(arrangement_total_face_bound(q, 2), 2 * q * q + 1)

    def test_closed_form_satisfies_deletion_restriction_recurrence(self):
        for dimension in range(1, 7):
            for hyperplanes in range(1, 15):
                closed, recurrence = arrangement_total_face_recurrence(
                    hyperplanes, dimension
                )
                self.assertEqual(closed, recurrence)

    def test_fixed_dimension_growth_has_expected_leading_order(self):
        # F_d(q) is a degree-d integer-valued polynomial in q.
        for dimension in range(1, 6):
            values = [
                arrangement_total_face_bound(q, dimension)
                for q in range(0, 15)
            ]
            differences = values
            for _ in range(dimension):
                differences = [
                    right - left for left, right in zip(differences, differences[1:])
                ]
            self.assertTrue(all(value == 2**dimension for value in differences))

    def test_nonconstant_guard_count_ignores_constant_coordinates(self):
        generators = (
            (1, 0, 2, 0, -1),
            (0, 0, 3, 0, 1),
        )
        self.assertEqual(nonconstant_guard_count(generators), 3)

    def test_hidden_pattern_bound_uses_rank_not_guard_count_as_geometry_dimension(self):
        generators = (
            (1, 0, 1, -1, 2, 0, 3, 1),
            (0, 1, 1, 1, -1, 0, 2, -2),
        )
        rank, varying, face_bound, binary_bound = hidden_guard_pattern_bound(generators)
        self.assertEqual(rank, 2)
        self.assertEqual(varying, 7)
        self.assertEqual(face_bound, 2 * varying * varying + 1)
        self.assertEqual(binary_bound, min(2**varying, face_bound))

    def test_full_hidden_rank_recovers_all_binary_patterns_as_sharper_bound(self):
        generators = (
            (2, 0, 0),
            (0, 3, 0),
            (0, 0, 5),
        )
        rank, varying, face_bound, binary_bound = hidden_guard_pattern_bound(generators)
        self.assertEqual((rank, varying), (3, 3))
        self.assertGreaterEqual(face_bound, 2**3)
        self.assertEqual(binary_bound, 2**3)

    def test_empty_hidden_lattice_has_one_pattern(self):
        rank, varying, face_bound, binary_bound = hidden_guard_pattern_bound(
            (), guard_count=5
        )
        self.assertEqual((rank, varying, face_bound, binary_bound), (0, 0, 1, 1))


if __name__ == "__main__":
    unittest.main()
