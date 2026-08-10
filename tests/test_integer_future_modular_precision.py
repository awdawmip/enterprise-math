import itertools
import unittest
from math import gcd

from enterprise_math.integer_future_modular_precision import (
    modular_observation_signature,
    modular_smith_precision_report,
    modular_state_partition,
    row_extension_modular_precision_refines,
    verify_modular_smith_count_by_enumeration,
)


class IntegerFutureModularPrecisionTests(unittest.TestCase):
    def test_scalar_formula_is_exact_M_over_gcd(self):
        for coefficient in range(-6, 7):
            for modulus in range(1, 9):
                report = modular_smith_precision_report(
                    ((coefficient,),),
                    modulus,
                )
                if coefficient == 0:
                    self.assertEqual(report.image_size, 1)
                    self.assertEqual(report.kernel_size, modulus)
                else:
                    self.assertEqual(
                        report.image_size,
                        modulus // gcd(abs(coefficient), modulus),
                    )
                    self.assertEqual(
                        report.kernel_size,
                        gcd(abs(coefficient), modulus),
                    )
                self.assertTrue(
                    verify_modular_smith_count_by_enumeration(
                        ((coefficient,),),
                        modulus,
                    )
                )

    def test_all_small_two_by_two_integer_maps_match_finite_torus_enumeration(self):
        for entries in itertools.product(range(-2, 3), repeat=4):
            matrix = (
                (entries[0], entries[1]),
                (entries[2], entries[3]),
            )
            for modulus in range(1, 5):
                self.assertTrue(
                    verify_modular_smith_count_by_enumeration(
                        matrix,
                        modulus,
                    ),
                    (matrix, modulus),
                )

    def test_three_pair_ledger_is_exactly_two_to_one_mod_two_before_singleton_repair(self):
        pair_rows = (
            (1, 1, 0, 0),
            (0, 0, 1, 1),
            (1, 0, 1, 0),
            (0, 1, 0, 1),
            (1, 0, 0, 1),
            (0, 1, 1, 0),
        )
        before = modular_smith_precision_report(pair_rows, 2)
        self.assertEqual(before.rational_rank, 4)
        self.assertEqual(before.hidden_free_rank, 0)
        self.assertEqual(before.smith_factors, (1, 1, 1, 2))
        self.assertEqual(before.kernel_size, 2)
        self.assertEqual(before.image_size, 8)
        self.assertFalse(before.modularly_injective)

        after_rows = pair_rows + ((1, 0, 0, 0),)
        after = modular_smith_precision_report(after_rows, 2)
        self.assertEqual(after.smith_factors, (1, 1, 1, 1))
        self.assertEqual(after.kernel_size, 1)
        self.assertEqual(after.image_size, 16)
        self.assertTrue(after.modularly_injective)
        self.assertTrue(
            row_extension_modular_precision_refines(
                pair_rows,
                ((1, 0, 0, 0),),
                2,
            )
        )

    def test_full_ttl_age_observation_is_injective_mod_every_modulus(self):
        # Total queue traces for D=3 give q0+q1+q2, q0+q1, q0.
        ttl = (
            (1, 1, 1),
            (1, 1, 0),
            (1, 0, 0),
        )
        for modulus in range(1, 10):
            report = modular_smith_precision_report(ttl, modulus)
            self.assertEqual(report.smith_factors, (1, 1, 1))
            self.assertEqual(report.kernel_size, 1)
            self.assertEqual(report.image_size, modulus ** 3)
            self.assertTrue(report.modularly_injective)
            self.assertTrue(report.unimodular_integer_full_rank)

    def test_hidden_free_direction_contributes_one_full_modulus_factor(self):
        matrix = ((1, 0, 0),)
        for modulus in range(1, 8):
            report = modular_smith_precision_report(matrix, modulus)
            self.assertEqual(report.hidden_free_rank, 2)
            self.assertEqual(report.kernel_size, modulus ** 2)
            self.assertEqual(report.image_size, modulus)

    def test_row_extension_never_coarsens_modular_precision(self):
        bases = (
            ((2, 0),),
            ((2, 0), (0, 2)),
            ((1, 1),),
        )
        additions = (
            ((0, 2),),
            ((1, 0),),
            ((1, -1),),
        )
        for base in bases:
            for added in additions:
                for modulus in range(1, 7):
                    self.assertTrue(
                        row_extension_modular_precision_refines(
                            base,
                            added,
                            modulus,
                        )
                    )

    def test_explicit_partition_has_uniform_homomorphism_fibers(self):
        matrix = ((2, 0), (0, 3))
        modulus = 6
        report = modular_smith_precision_report(matrix, modulus)
        partition = modular_state_partition(matrix, modulus)
        self.assertEqual(len(partition), report.image_size)
        self.assertEqual({len(block) for block in partition}, {report.kernel_size})
        for block in partition:
            signatures = {
                modular_observation_signature(matrix, state, modulus)
                for state in block
            }
            self.assertEqual(len(signatures), 1)

    def test_validation(self):
        with self.assertRaises(ValueError):
            modular_smith_precision_report((), 2)
        with self.assertRaises(ValueError):
            modular_smith_precision_report(((1,),), 0)
        with self.assertRaises(TypeError):
            modular_smith_precision_report(((1,),), False)
        with self.assertRaises(ValueError):
            modular_observation_signature(((1, 0),), (1,), 2)


if __name__ == "__main__":
    unittest.main()
