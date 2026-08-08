import unittest

from enterprise_math.precision_signed_holonomy import (
    coarsened_scheduling_holonomy,
    scheduling_holonomy,
    signed_defect_is_invisible,
    signed_defect_transport,
    signed_transport_bulk_carry,
    signed_transport_is_coherent,
    staged_signed_defect_transport,
)


class PrecisionSignedHolonomyTests(unittest.TestCase):
    def test_scheduling_holonomy_has_both_signs_for_every_power(self):
        for power in range(2, 9):
            self.assertEqual(scheduling_holonomy(2, power, 2), 1)
            self.assertEqual(
                scheduling_holonomy(2**power, power, 2),
                1 - 2 ** (power - 1),
            )
            self.assertLess(scheduling_holonomy(2**power, power, 2), 0)

    def test_signed_transport_bulk_carry_identity(self):
        for modulus in range(1, 11):
            for base_state in range(-40, 41):
                for defect in range(-40, 41):
                    transported, bulk, carry = signed_transport_bulk_carry(
                        modulus, base_state, defect
                    )
                    self.assertEqual(
                        transported,
                        signed_defect_transport(modulus, base_state, defect),
                    )
                    self.assertEqual(transported, bulk + carry)
                    self.assertIn(carry, (0, 1))

    def test_signed_transport_coherence(self):
        for outer in range(1, 6):
            for inner in range(1, 6):
                for base_state in range(-30, 31):
                    for defect in range(-30, 31):
                        direct = signed_defect_transport(
                            outer * inner, base_state, defect
                        )
                        staged = staged_signed_defect_transport(
                            outer, inner, base_state, defect
                        )
                        self.assertEqual(staged, direct)
                        self.assertTrue(
                            signed_transport_is_coherent(
                                outer, inner, base_state, defect
                            )
                        )

    def test_signed_invisibility_window(self):
        for modulus in range(1, 11):
            for base_state in range(-40, 41):
                for defect in range(-40, 41):
                    invisible = signed_defect_is_invisible(
                        modulus, base_state, defect
                    )
                    self.assertEqual(
                        invisible,
                        signed_defect_transport(modulus, base_state, defect) == 0,
                    )

    def test_p009_holonomy_further_coarsening_uses_signed_transport(self):
        for state in range(80):
            for power in range(2, 5):
                for first_ratio in range(1, 6):
                    for second_ratio in range(1, 6):
                        direct, transported = coarsened_scheduling_holonomy(
                            state, power, first_ratio, second_ratio
                        )
                        self.assertEqual(direct, transported)


if __name__ == "__main__":
    unittest.main()
