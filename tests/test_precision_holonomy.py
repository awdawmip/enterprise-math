import unittest

from enterprise_math.precision_holonomy import (
    collapse_holonomy_composition,
    defect_is_invisible,
    defect_transport,
    defect_transport_bulk_carry,
    staged_defect_transport,
    strict_recovery_threshold,
    transport_is_coherent,
)


class PrecisionHolonomyTests(unittest.TestCase):
    def test_defect_transport_bulk_carry_identity(self):
        for modulus in range(1, 12):
            for base_state in range(80):
                for defect in range(80):
                    transported, bulk, carry = defect_transport_bulk_carry(
                        modulus, base_state, defect
                    )
                    self.assertEqual(
                        transported,
                        defect_transport(modulus, base_state, defect),
                    )
                    self.assertEqual(transported, bulk + carry)
                    self.assertIn(carry, (0, 1))

    def test_defect_transport_coherence(self):
        for outer in range(1, 7):
            for inner in range(1, 7):
                for base_state in range(60):
                    for defect in range(40):
                        direct = defect_transport(
                            outer * inner, base_state, defect
                        )
                        staged = staged_defect_transport(
                            outer, inner, base_state, defect
                        )
                        self.assertEqual(staged, direct)
                        self.assertTrue(
                            transport_is_coherent(
                                outer, inner, base_state, defect
                            )
                        )

    def test_zero_visibility_threshold(self):
        for modulus in range(1, 12):
            for base_state in range(80):
                for defect in range(50):
                    invisible = defect_is_invisible(
                        modulus, base_state, defect
                    )
                    self.assertEqual(
                        invisible,
                        defect_transport(modulus, base_state, defect) == 0,
                    )

    def test_collapse_holonomy_composition(self):
        for n in range(30):
            for power in range(2, 5):
                for coarse in range(1, 4):
                    for ratio_one in range(1, 4):
                        middle = coarse * ratio_one
                        for ratio_two in range(1, 4):
                            fine = middle * ratio_two
                            direct, lower, _, transported = (
                                collapse_holonomy_composition(
                                    n, power, coarse, middle, fine
                                )
                            )
                            self.assertEqual(direct, lower + transported)

    def test_strict_recovery_criterion(self):
        for n in range(30):
            for power in range(2, 5):
                for coarse in range(1, 4):
                    for ratio_one in range(1, 4):
                        middle = coarse * ratio_one
                        for ratio_two in range(1, 4):
                            fine = middle * ratio_two
                            strict, upper, threshold = strict_recovery_threshold(
                                n, power, coarse, middle, fine
                            )
                            self.assertEqual(strict, upper >= threshold)


if __name__ == "__main__":
    unittest.main()
