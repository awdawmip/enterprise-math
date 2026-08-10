import unittest

from enterprise_math.precision_valuation_repair import (
    add_capped_unit_signatures,
    capped_p_valuation,
    capped_unit_signature,
    equal_level_unbounded_carry_witness,
    p_valuation,
    repaired_class_count,
    separate_distinct_unit_residues,
    signature_residue_mod_power,
    unit_residue_class_count,
    universal_translation_closure_is_exact,
    universal_translation_signature,
    valuation_carry,
    valuation_only_sum_level,
)


class PrecisionValuationRepairTests(unittest.TestCase):
    def test_unequal_levels_make_addition_exactly_tropical_min(self):
        for prime in (2, 3, 5):
            for left in range(1, 80):
                for right in range(1, 80):
                    a = p_valuation(left, prime)
                    b = p_valuation(right, prime)
                    if a != b:
                        self.assertEqual(p_valuation(left + right, prime), min(a, b))
                        self.assertEqual(valuation_carry(left, right, prime), 0)

    def test_equal_level_carry_is_unbounded(self):
        for prime in (2, 3, 5):
            for level in range(4):
                for extra in range(1, 6):
                    left, right = equal_level_unbounded_carry_witness(prime, level, extra)
                    self.assertEqual(p_valuation(left, prime), level)
                    self.assertEqual(p_valuation(right, prime), level)
                    self.assertEqual(p_valuation(left + right, prime), level + extra)

    def test_level_only_predictor_fails_exactly_on_uncapped_equal_level(self):
        self.assertEqual(valuation_only_sum_level(4, 6, 2, 5), 1)
        self.assertIsNone(valuation_only_sum_level(4, 12, 2, 5))
        self.assertEqual(valuation_only_sum_level(32, 64, 2, 5), 5)

    def test_level_plus_unit_residue_is_exact_addition_repair(self):
        for prime in (2, 3, 5):
            for cap in range(1, 5):
                modulus = prime**cap
                for left in range(modulus):
                    left_signature = capped_unit_signature(left, prime, cap)
                    self.assertEqual(
                        signature_residue_mod_power(left_signature, prime, cap),
                        left % modulus,
                    )
                    for right in range(modulus):
                        repaired = add_capped_unit_signatures(
                            left_signature,
                            capped_unit_signature(right, prime, cap),
                            prime,
                            cap,
                        )
                        self.assertEqual(
                            repaired,
                            capped_unit_signature((left + right) % modulus, prime, cap),
                        )

    def test_distinct_same_level_unit_residues_are_future_distinguishable(self):
        for prime in (2, 3, 5):
            for height in range(1, 5):
                modulus = prime**height
                units = tuple(value for value in range(1, modulus) if value % prime)
                for index, left in enumerate(units):
                    for right in units[index + 1 :]:
                        partner = separate_distinct_unit_residues(
                            left, right, prime, height
                        )
                        self.assertEqual(capped_p_valuation(left + partner, prime, height), height)
                        self.assertLess(capped_p_valuation(right + partner, prime, height), height)

    def test_unit_repair_class_counts_telescope_to_full_residue_space(self):
        for prime in (2, 3, 5, 7):
            for cap in range(1, 6):
                self.assertEqual(repaired_class_count(prime, cap), prime**cap)
                self.assertEqual(unit_residue_class_count(prime, cap, cap), 1)

    def test_universal_translation_future_language_recovers_exact_residue(self):
        for prime, cap in ((2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (5, 1)):
            self.assertTrue(universal_translation_closure_is_exact(prime, cap))
            modulus = prime**cap
            signatures = [
                universal_translation_signature(residue, prime, cap)
                for residue in range(modulus)
            ]
            self.assertEqual(len(signatures), len(set(signatures)))

    def test_invalid_inputs_fail_closed(self):
        with self.assertRaises(ValueError):
            p_valuation(0, 2)
        with self.assertRaises(ValueError):
            p_valuation(4, 4)
        with self.assertRaises(ValueError):
            capped_p_valuation(-1, 2, 3)
        with self.assertRaises(ValueError):
            separate_distinct_unit_residues(1, 1, 3, 2)


if __name__ == "__main__":
    unittest.main()
