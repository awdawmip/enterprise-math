from fractions import Fraction
from itertools import combinations, permutations, product
import unittest

from enterprise_math.euler_fcc_spin_holonomy import (
    BASIS,
    FCC_LINE_FAMILIES,
    NORMALS,
    SLICES,
    add,
    agrees_up_to_sign,
    dot,
    exact_certificate,
    expected_face_spin_numerator,
    face_spin_numerator,
    face_transport,
    half_turn_about_slice,
    neg,
    outgoing_chart,
    quaternion_multiply,
    scale,
    scalar_orientation_flattening_exists,
    shared_line,
    spin_conjugation_numerator,
    tangent_complex_numerator,
    transition,
    unoriented_line_family,
    vec,
)


class EulerFccSpinHolonomyTests(unittest.TestCase):
    def test_regular_tetrahedral_normals(self) -> None:
        self.assertEqual(
            add(add(NORMALS["A"], NORMALS["B"]), add(NORMALS["C"], NORMALS["D"])),
            vec(0, 0, 0),
        )
        for source in SLICES:
            self.assertEqual(dot(NORMALS[source], NORMALS[source]), 3)
        for source, target in permutations(SLICES, 2):
            self.assertEqual(dot(NORMALS[source], NORMALS[target]), -1)

    def test_cross_normals_recover_six_fcc_line_families(self) -> None:
        seen = set()
        for source, target in combinations(SLICES, 2):
            line = shared_line(source, target)
            family_name = unoriented_line_family(source, target)
            self.assertTrue(agrees_up_to_sign(line, FCC_LINE_FAMILIES[family_name]))
            self.assertEqual(shared_line(target, source), neg(line))
            self.assertEqual(dot(line, line), 2)
            seen.add(family_name)
        self.assertEqual(seen, set(FCC_LINE_FAMILIES))

    def test_each_outgoing_chart_is_120_degree_and_zero_sum(self) -> None:
        for source in SLICES:
            chart = outgoing_chart(source)
            self.assertEqual(add(add(chart[0], chart[1]), chart[2]), vec(0, 0, 0))
            for line in chart:
                self.assertEqual(dot(line, line), 2)
            for left, right in combinations(chart, 2):
                self.assertEqual(dot(left, right), -1)

    def test_transition_is_proper_inverse_transport(self) -> None:
        for source, target in permutations(SLICES, 2):
            line = shared_line(source, target)
            self.assertEqual(transition(source, target, NORMALS[source]), NORMALS[target])
            self.assertEqual(transition(source, target, line), line)
            for basis in BASIS:
                self.assertEqual(
                    transition(target, source, transition(source, target, basis)),
                    basis,
                )
                self.assertEqual(
                    transition(source, target, tangent_complex_numerator(source, basis)),
                    tangent_complex_numerator(
                        target, transition(source, target, basis)
                    ),
                )
            for left_index, left in enumerate(BASIS):
                for right_index, right in enumerate(BASIS):
                    self.assertEqual(
                        dot(
                            transition(source, target, left),
                            transition(source, target, right),
                        ),
                        Fraction(1 if left_index == right_index else 0),
                    )

    def test_spin_numerator_transports_normal(self) -> None:
        for source, target in permutations(SLICES, 2):
            self.assertEqual(
                spin_conjugation_numerator(source, target),
                scale_quaternion(3, pure_quaternion(NORMALS[target])),
            )

    def test_every_oriented_triangle_has_spin_J_holonomy(self) -> None:
        for first, second, third in permutations(SLICES, 3):
            actual = face_spin_numerator(first, second, third)
            self.assertEqual(actual, expected_face_spin_numerator(first, second, third))
            self.assertEqual(
                quaternion_multiply(actual, actual),
                (Fraction(-27), Fraction(0), Fraction(0), Fraction(0)),
            )

    def test_every_triangle_has_tangent_half_turn_holonomy(self) -> None:
        for first, second, third in permutations(SLICES, 3):
            for basis in BASIS:
                self.assertEqual(
                    face_transport(first, second, third, basis),
                    half_turn_about_slice(first, basis),
                )
            for tangent in outgoing_chart(first):
                self.assertEqual(
                    face_transport(first, second, third, tangent),
                    neg(tangent),
                )

    def test_scalar_orientation_connection_cannot_be_flattened(self) -> None:
        self.assertFalse(scalar_orientation_flattening_exists())
        for choices in product((-1, 1), repeat=3):
            g0, g1, g2 = choices
            self.assertFalse(g0 == -g1 and g1 == -g2 and g2 == -g0)

    def test_complete_exact_certificate(self) -> None:
        certificate = exact_certificate()
        self.assertEqual(certificate["status"], "PASS")
        self.assertEqual(certificate["slices"], 4)
        self.assertEqual(certificate["unoriented_line_families"], 6)
        self.assertEqual(certificate["ordered_triangular_loops"], 24)
        self.assertEqual(certificate["spin_holonomy_square"], -1)


def pure_quaternion(value):
    return Fraction(0), *value


def scale_quaternion(scalar, value):
    factor = Fraction(scalar)
    return tuple(factor * coordinate for coordinate in value)


if __name__ == "__main__":
    unittest.main()
