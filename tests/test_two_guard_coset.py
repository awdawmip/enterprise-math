import itertools
import unittest

from enterprise_math.two_guard_coset import (
    canonical_scores_from_two_guard_coordinate,
    evaluate_two_guard_coarse_map,
    two_guard_coarse_map,
    two_guard_coset_coordinate,
    two_guard_quotient_basis,
    two_guard_reachable_patterns_from_coordinate,
    two_guard_same_hidden_coset,
)


def coarse_totals(values, partition):
    return tuple(sum(values[index] for index in group) for group in partition)


def scores(guards, biases, values):
    return tuple(
        bias + sum(weight * value for weight, value in zip(guard, values))
        for guard, bias in zip(guards, biases)
    )


class TwoGuardCosetTests(unittest.TestCase):
    def test_quotient_basis_maps_hidden_step_to_torsion_axis(self):
        basis = two_guard_quotient_basis((6, -4))
        self.assertEqual(basis.torsion_modulus, 2)
        self.assertEqual(basis.primitive_direction, (3, -2))
        u, v = basis.bezout_row
        p1, p2 = basis.primitive_direction
        self.assertEqual(u * p1 + v * p2, 1)
        self.assertEqual(
            basis.free_row[0] * basis.hidden_step[0]
            + basis.free_row[1] * basis.hidden_step[1],
            0,
        )

    def test_coordinates_are_complete_hidden_coset_invariants(self):
        step = (6, -4)
        for left in itertools.product(range(-5, 6), repeat=2):
            for multiple in range(-4, 5):
                right = (
                    left[0] + multiple * step[0],
                    left[1] + multiple * step[1],
                )
                self.assertEqual(
                    two_guard_coset_coordinate(left, step),
                    two_guard_coset_coordinate(right, step),
                )
                self.assertTrue(two_guard_same_hidden_coset(left, right, step))

        # Same free coordinate but wrong torsion residue is not the same coset.
        self.assertFalse(two_guard_same_hidden_coset((0, 0), (3, -2), step))

    def test_canonical_representative_reconstructs_same_coset(self):
        step = (6, -4)
        for value in itertools.product(range(-7, 8), repeat=2):
            coordinate = two_guard_coset_coordinate(value, step)
            representative = canonical_scores_from_two_guard_coordinate(
                coordinate, step
            )
            self.assertTrue(
                two_guard_same_hidden_coset(value, representative, step)
            )

    def test_symbolic_coarse_map_is_independent_of_fine_section(self):
        guards = (
            (1, -1, 2, 2),
            (-1, 1, 3, 3),
        )
        biases = (2, -3)
        partition = ((0, 1), (2, 3))
        coarse_map = two_guard_coarse_map(guards, biases, partition)
        self.assertEqual(coarse_map.basis.hidden_step, (2, -2))

        seen = {}
        for values in itertools.product(range(-2, 3), repeat=4):
            coarse = coarse_totals(values, partition)
            coordinate = two_guard_coset_coordinate(
                scores(guards, biases, values),
                coarse_map.basis.hidden_step,
            )
            symbolic = evaluate_two_guard_coarse_map(coarse_map, coarse)
            self.assertEqual(coordinate, symbolic)
            previous = seen.setdefault(coarse, coordinate)
            self.assertEqual(previous, coordinate)

    def test_reachable_patterns_depend_only_on_quotient_coordinate(self):
        step = (2, -2)
        left = (3, -1)
        right = (7, -5)
        self.assertTrue(two_guard_same_hidden_coset(left, right, step))
        coordinate = two_guard_coset_coordinate(left, step)
        expected = two_guard_reachable_patterns_from_coordinate(
            coordinate, step
        )
        direct_left = {
            tuple(score >= 0 for score in (left[0] + 2*t, left[1] - 2*t))
            for t in range(-20, 21)
        }
        direct_right = {
            tuple(score >= 0 for score in (right[0] + 2*t, right[1] - 2*t))
            for t in range(-20, 21)
        }
        self.assertEqual(set(expected), direct_left)
        self.assertEqual(direct_left, direct_right)

    def test_support_guard_pair_has_constant_free_coordinate_and_residue_torsion(self):
        # Relation z=c0-c1. Support |z|<=R is encoded by guards
        # s1=R-z, s2=R+z. Under the partition hiding c0-c1, the hidden step is
        # (-2,2); the primitive free row is proportional to (1,1), so s1+s2=2R
        # is the coarse-readable free coordinate while torsion records z mod 2.
        radius = 3
        guards = (
            (-1, 1, 0),
            (1, -1, 0),
        )
        biases = (radius, radius)
        partition = ((0, 1), (2,))
        coarse_map = two_guard_coarse_map(guards, biases, partition)
        self.assertEqual(coarse_map.basis.hidden_step, (2, -2))

        for values in itertools.product(range(-4, 5), repeat=3):
            coordinate = evaluate_two_guard_coarse_map(
                coarse_map,
                coarse_totals(values, partition),
            )
            self.assertEqual(abs(coordinate.free_coordinate), 2 * radius)
            relation = values[0] - values[1]
            # Torsion modulus is two: its residue distinguishes the parity class
            # of the hidden relation (up to the deterministic transform sign).
            self.assertEqual(coordinate.torsion_residue, relation % 2)


if __name__ == "__main__":
    unittest.main()
