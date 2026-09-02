from fractions import Fraction
import unittest

from enterprise_math.brc_weighted_recurrent import (
    finite_recurrent_mass_analysis,
    gauge_recurrent_mass_matrix,
    recurrent_mass_power,
    verify_recurrent_integer_divergence_certificate,
    verify_recurrent_integer_stable_certificate,
)

Q = Fraction


class FiniteRecurrentWeightedBRCTests(unittest.TestCase):
    def test_stable_raw_supercritical_example(self) -> None:
        matrix = [[Q(0), Q(1, 2)], [Q(1, 2), Q(2, 3)]]
        result = finite_recurrent_mass_analysis(matrix)
        self.assertTrue(result.stable)
        self.assertEqual(result.star, ((Q(4), Q(6)), (Q(6), Q(12))))
        self.assertEqual(result.canonical_potential, (Q(10), Q(18)))
        self.assertEqual(result.primitive_integer_potential, (5, 9))
        self.assertEqual(result.gauged_row_sums, (Q(9, 10), Q(17, 18)))
        self.assertTrue(result.verify_stable_certificate())

    def test_one_state_reduces_to_old_threshold(self) -> None:
        stable = finite_recurrent_mass_analysis([[Q(3, 5)]])
        self.assertTrue(stable.stable)
        self.assertEqual(stable.star, ((Q(5, 2),),))
        self.assertEqual(stable.primitive_integer_potential, (1,))

        unstable = finite_recurrent_mass_analysis([[Q(6, 5)]])
        self.assertFalse(unstable.stable)
        self.assertIsNone(unstable.star)
        self.assertTrue(verify_recurrent_integer_divergence_certificate([[Q(6, 5)]], [1]))

    def test_dominant_paths_can_contract_while_total_mass_diverges(self) -> None:
        matrix = [[Q(3, 5), Q(3, 5)], [Q(3, 5), Q(3, 5)]]
        result = finite_recurrent_mass_analysis(matrix)
        self.assertFalse(result.stable)
        self.assertTrue(verify_recurrent_integer_divergence_certificate(matrix, [1, 1]))
        for k in range(1, 7):
            power = recurrent_mass_power(matrix, k)
            self.assertEqual(sum(power[0], Q(0)), Q(6, 5) ** k)
            self.assertLess(Q(3, 5) ** k, 1)

    def test_stable_and_divergent_certificates_are_typed(self) -> None:
        stable_matrix = [[Q(0), Q(1, 2)], [Q(1, 2), Q(2, 3)]]
        self.assertTrue(verify_recurrent_integer_stable_certificate(stable_matrix, [5, 9]))
        self.assertFalse(verify_recurrent_integer_divergence_certificate(stable_matrix, [1, 1]))

        unstable_matrix = [[Q(3, 5), Q(3, 5)], [Q(3, 5), Q(3, 5)]]
        self.assertFalse(verify_recurrent_integer_stable_certificate(unstable_matrix, [1, 1]))
        self.assertTrue(verify_recurrent_integer_divergence_certificate(unstable_matrix, [1, 1]))

    def test_gauge_is_exact(self) -> None:
        matrix = [[Q(0), Q(1, 2)], [Q(1, 2), Q(2, 3)]]
        gauged = gauge_recurrent_mass_matrix(matrix, [10, 18])
        self.assertEqual(gauged, ((Q(0), Q(9, 10)), (Q(5, 18), Q(2, 3))))
        self.assertEqual(tuple(sum(row, Q(0)) for row in gauged), (Q(9, 10), Q(17, 18)))
        # Closed 0->1->0 product is gauge invariant.
        self.assertEqual(gauged[0][1] * gauged[1][0], matrix[0][1] * matrix[1][0])

    def test_validation_rejects_bad_carriers(self) -> None:
        with self.assertRaises(ValueError):
            finite_recurrent_mass_analysis([])
        with self.assertRaises(ValueError):
            finite_recurrent_mass_analysis([[1, 2, 3], [4, 5, 6]])
        with self.assertRaises(ValueError):
            finite_recurrent_mass_analysis([[1, -1], [0, 1]])
        with self.assertRaises(TypeError):
            finite_recurrent_mass_analysis([[0.5]])
        self.assertFalse(verify_recurrent_integer_stable_certificate([[Q(1, 2)]], [0]))
        self.assertFalse(verify_recurrent_integer_divergence_certificate([[Q(2)]], [0]))


if __name__ == "__main__":
    unittest.main()
