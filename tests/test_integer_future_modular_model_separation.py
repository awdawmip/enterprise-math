import itertools
import unittest

from enterprise_math.integer_future_modular_model_separation import (
    first_distinguishing_prime_power_exponent,
    first_distinguishing_prime_power_modulus,
    modular_model_separation_report,
    modular_separating_state_witness,
    models_indistinguishable_modulus,
    observation_model_difference_content,
)


class IntegerFutureModularModelSeparationTests(unittest.TestCase):
    def test_indistinguishable_moduli_are_exact_divisors_of_difference_content(self):
        left = (
            (1, 4),
            (7, -2),
        )
        right = (
            (1, -8),
            (-5, 10),
        )
        # Difference entries are 0,12,12,-12, so content=12.
        self.assertEqual(observation_model_difference_content(left, right), 12)
        for modulus in range(1, 25):
            self.assertEqual(
                models_indistinguishable_modulus(left, right, modulus),
                12 % modulus == 0,
            )

    def test_first_prime_power_separation_is_v_p_content_plus_one(self):
        left = ((0, 0), (0, 0))
        right = ((12, 0), (0, 36))
        self.assertEqual(observation_model_difference_content(left, right), 12)
        self.assertEqual(first_distinguishing_prime_power_exponent(left, right, 2), 3)
        self.assertEqual(first_distinguishing_prime_power_modulus(left, right, 2), 8)
        self.assertEqual(first_distinguishing_prime_power_exponent(left, right, 3), 2)
        self.assertEqual(first_distinguishing_prime_power_modulus(left, right, 3), 9)
        self.assertEqual(first_distinguishing_prime_power_exponent(left, right, 5), 1)
        self.assertEqual(first_distinguishing_prime_power_modulus(left, right, 5), 5)

    def test_unit_coordinate_always_witnesses_noncongruent_linear_maps(self):
        left = (
            (2, 3, 5),
            (7, 11, 13),
        )
        right = (
            (2, 3, 1),
            (7, 11, 13),
        )
        for modulus in range(1, 9):
            witness = modular_separating_state_witness(left, right, modulus)
            if models_indistinguishable_modulus(left, right, modulus):
                self.assertIsNone(witness)
            else:
                self.assertIsNotNone(witness)
                assert witness is not None
                self.assertEqual(sum(witness), 1)

    def test_free_vs_finite_torsion_pair_has_exact_divisor_downset(self):
        depth = 60
        free = (
            (1, 0),
            (0, 0),
        )
        finite = (
            (1, 0),
            (0, depth),
        )
        report = modular_model_separation_report(
            free,
            finite,
            tuple(range(1, 21)),
        )
        self.assertEqual(report.difference_content, depth)
        self.assertEqual(
            report.indistinguishable_tested_moduli,
            tuple(modulus for modulus in range(1, 21) if depth % modulus == 0),
        )
        self.assertEqual(
            report.distinguishing_tested_moduli,
            tuple(modulus for modulus in range(1, 21) if depth % modulus != 0),
        )

    def test_identical_integer_models_are_indistinguishable_at_every_modulus(self):
        matrix = (
            (1, -2),
            (3, 4),
        )
        self.assertEqual(observation_model_difference_content(matrix, matrix), 0)
        for modulus in range(1, 12):
            self.assertTrue(models_indistinguishable_modulus(matrix, matrix, modulus))
            self.assertIsNone(modular_separating_state_witness(matrix, matrix, modulus))
        self.assertIsNone(first_distinguishing_prime_power_exponent(matrix, matrix, 2))

    def test_random_small_matrix_pairs_match_direct_entrywise_congruence(self):
        matrices = tuple(
            (
                (entries[0], entries[1]),
                (entries[2], entries[3]),
            )
            for entries in itertools.product(range(-1, 2), repeat=4)
        )
        for left in matrices:
            for right in matrices:
                for modulus in range(1, 6):
                    direct = all(
                        (a - b) % modulus == 0
                        for left_row, right_row in zip(left, right, strict=True)
                        for a, b in zip(left_row, right_row, strict=True)
                    )
                    self.assertEqual(
                        models_indistinguishable_modulus(left, right, modulus),
                        direct,
                    )

    def test_validation(self):
        with self.assertRaises(ValueError):
            observation_model_difference_content(((1,),), ((1, 2),))
        with self.assertRaises(ValueError):
            models_indistinguishable_modulus(((1,),), ((0,),), 0)
        with self.assertRaises(TypeError):
            models_indistinguishable_modulus(((1,),), ((0,),), False)
        with self.assertRaises(ValueError):
            modular_model_separation_report(((1,),), ((0,),), ())


if __name__ == "__main__":
    unittest.main()
