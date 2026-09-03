import math
import unittest
from decimal import Decimal

from enterprise_math.cyclic_rotation_refinement import (
    add_refinement_coordinates,
    all_refinement_states,
    dyadic_half_turn_root,
    effective_character,
    element_order,
    finite_euler_coordinates,
    half_turn_roots_after_refinement,
    refined_index,
    refinement_coordinates,
    refinement_embedding,
    refinement_extension_splits,
    rotation_completion_enclosure,
    rotation_pi_approximant,
    splitting_section_generator,
    trace_coordinates,
)


class CyclicRotationRefinementTests(unittest.TestCase):
    def test_embedding_and_coordinate_bijection(self):
        for modulus in range(2, 18):
            embedded = [refinement_embedding(k, modulus) for k in range(modulus)]
            self.assertEqual(len(set(embedded)), modulus)
            states = all_refinement_states(modulus)
            self.assertEqual(len(set(states)), 2 * modulus)
            for j in range(2 * modulus):
                coords = refinement_coordinates(j, modulus)
                self.assertEqual(refined_index(coords.coarse, coords.detail, modulus), j)

    def test_binary_carry_is_exact_group_law(self):
        for modulus in range(2, 15):
            for left_index in range(2 * modulus):
                for right_index in range(2 * modulus):
                    left = refinement_coordinates(left_index, modulus)
                    right = refinement_coordinates(right_index, modulus)
                    total = add_refinement_coordinates(left, right, modulus)
                    self.assertEqual(
                        refined_index(total.coarse, total.detail, modulus),
                        (left_index + right_index) % (2 * modulus),
                    )

    def test_split_criterion(self):
        for modulus in range(2, 24):
            brute = [
                j
                for j in range(2 * modulus)
                if j % 2 == 1 and (2 * j) % (2 * modulus) == 0
            ]
            self.assertEqual(bool(brute), refinement_extension_splits(modulus))
            witness = splitting_section_generator(modulus)
            if modulus % 2:
                self.assertEqual(witness, modulus)
                self.assertEqual(brute, [modulus])
            else:
                self.assertIsNone(witness)
                self.assertEqual(brute, [])

    def test_half_turn_roots_and_dyadic_orders(self):
        self.assertEqual(half_turn_roots_after_refinement(6), (3, 9))
        for depth in range(0, 12):
            modulus, root = dyadic_half_turn_root(depth)
            self.assertEqual(modulus, 6 * 2**depth)
            self.assertEqual(root, 3)
            self.assertEqual(element_order(root, modulus), 2 ** (depth + 1))
            self.assertEqual((2**depth * root) % modulus, modulus // 2)

    def test_trace_spectral_decimation(self):
        values = trace_coordinates(14, precision=100)
        self.assertEqual(values[0], Decimal(-1))
        self.assertEqual(values[1], Decimal(0))
        tolerance = Decimal("1e-90")
        for current, refined in zip(values, values[1:]):
            self.assertLess(
                abs(refined * refined - (Decimal(1) + current) / 2), tolerance
            )
        for value in values[2:]:
            self.assertGreater(value, 0)
            self.assertLess(value, 1)

    def test_rotation_approximants_are_monotone_and_enclose_classical_pi(self):
        approximants = [
            rotation_pi_approximant(depth, precision=100) for depth in range(2, 13)
        ]
        self.assertTrue(all(a < b for a, b in zip(approximants, approximants[1:])))
        pi_decimal = Decimal(str(math.pi))
        for depth in range(2, 11):
            enclosure = rotation_completion_enclosure(depth, precision=100)
            self.assertLess(enclosure.lower, enclosure.upper)
            self.assertLess(enclosure.lower, pi_decimal)
            self.assertGreater(enclosure.upper, pi_decimal)

    def test_finite_euler_even_odd_decomposition(self):
        for depth in range(1, 10):
            u, c, s = finite_euler_coordinates(depth)
            self.assertAlmostEqual((c + 1j * s).real, u.real, places=13)
            self.assertAlmostEqual((c + 1j * s).imag, u.imag, places=13)
            self.assertAlmostEqual(c.imag, 0.0, places=13)
            self.assertAlmostEqual(s.imag, 0.0, places=13)
            self.assertAlmostEqual(c.real * c.real + s.real * s.real, 1.0, places=12)
            self.assertAlmostEqual(
                u.real,
                float(trace_coordinates(depth, precision=60)[depth]),
                places=13,
            )

    def test_external_character_refinement(self):
        for depth in range(0, 9):
            coarse = effective_character(depth)
            refined = effective_character(depth + 1)
            self.assertAlmostEqual((refined * refined).real, coarse.real, places=13)
            self.assertAlmostEqual((refined * refined).imag, coarse.imag, places=13)


if __name__ == "__main__":
    unittest.main()
