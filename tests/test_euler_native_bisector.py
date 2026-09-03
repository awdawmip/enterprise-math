import inspect
import unittest
from fractions import Fraction

from enterprise_math import euler_native_bisector as enb


class EulerNativeBisectorTests(unittest.TestCase):
    def test_cell_radius_square_is_exact(self):
        self.assertEqual(
            enb.radial() * enb.radial(),
            enb.QRadial.coerce(Fraction(1, 3)),
        )

    def test_complete_native_bisector_certificate(self):
        self.assertTrue(enb.native_bisector_certificate().valid)

    def test_c3_generates_c6_without_an_external_reversal_bit(self):
        rotor = enb.six_state_rotor()
        self.assertEqual(enb.matrix_pow(rotor, 2), enb.RIGHT_TURN)
        self.assertEqual(enb.matrix_pow(rotor, 3), enb.matrix_neg(enb.IDENTITY))
        self.assertEqual(enb.matrix_pow(rotor, 6), enb.IDENTITY)

    def test_cell_radius_generates_the_unit_gate_bisector(self):
        gate = enb.gate_rotor()
        self.assertEqual(enb.matrix_pow(gate, 2), enb.six_state_rotor())
        self.assertEqual(enb.matrix_pow(gate, 6), enb.matrix_neg(enb.IDENTITY))
        self.assertEqual(enb.matrix_pow(gate, 12), enb.IDENTITY)
        self.assertEqual(enb.gate_normalizer_square(), Fraction(1, 3))
        self.assertEqual(enb.adjacent_sum_gram(), enb.matrix_scale(3, enb.GRAM))

    def test_physical_gate_is_centroid_displacement(self):
        self.assertEqual(
            enb.physical_gate_displacement(),
            enb.physical_gate_centroid_form(),
        )
        self.assertEqual(
            enb.physical_gate_displacement(),
            enb.matrix_scale(enb.radial(), enb.gate_rotor()),
        )

    def test_quarter_turn_is_the_normalized_chiral_difference(self):
        quarter = enb.quarter_turn()
        self.assertEqual(quarter, enb.chiral_difference())
        self.assertEqual(enb.matrix_pow(quarter, 2), enb.matrix_neg(enb.IDENTITY))

    def test_all_rotors_preserve_one_exact_gram_form(self):
        self.assertTrue(enb.all_rotors_preserve_gram())

    def test_twelve_states_interleave_directions_and_gates(self):
        self.assertEqual(len(set(enb.interleaved_phase_states())), 12)
        self.assertTrue(enb.interleaving_identity())

    def test_checker_does_not_import_pi_or_trigonometry(self):
        source = inspect.getsource(enb)
        self.assertNotIn("math.pi", source)
        self.assertNotIn("sin(", source)
        self.assertNotIn("cos(", source)


if __name__ == "__main__":
    unittest.main()
