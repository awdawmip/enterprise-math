import unittest
from itertools import product

from enterprise_math.causal_transfer_higher_moments import (
    a2_fourth_moment_quadratic_identity,
    a2_sixth_moment_identity,
    a2_sixth_order_anisotropy_witness,
    a_fourth_moment_closed_form,
    a_fourth_moment_identity,
    a_oriented_even_moment,
    a_second_moment_identity,
    power_sum,
    quartic_is_not_quadratic_only_witness,
)


class CausalTransferHigherMomentsTests(unittest.TestCase):
    def test_second_and_fourth_integer_identities(self):
        for slots in range(2, 7):
            for state in product(range(-2, 3), repeat=slots):
                if sum(state) != 0:
                    continue
                self.assertTrue(a_second_moment_identity(state))
                self.assertTrue(a_fourth_moment_identity(state))
                self.assertEqual(a_oriented_even_moment(state, 4), a_fourth_moment_closed_form(state))

    def test_rank_three_fourth_moment_is_not_determined_by_quadratic_shadow(self):
        left, right, left_cross, right_cross = quartic_is_not_quadratic_only_witness()
        self.assertNotEqual(left_cross, right_cross)
        self.assertEqual(power_sum(left, 2), 2)
        self.assertEqual(power_sum(right, 2), 4)

    def test_a2_fourth_order_remains_quadratic_only(self):
        for state in product(range(-4, 5), repeat=3):
            if sum(state) != 0:
                continue
            self.assertTrue(a2_fourth_moment_quadratic_identity(state))

    def test_a2_sixth_order_identity_and_anisotropy_split(self):
        for state in product(range(-3, 4), repeat=3):
            if sum(state) != 0:
                continue
            self.assertTrue(a2_sixth_moment_identity(state))
        left, right, left_cross, right_cross = a2_sixth_order_anisotropy_witness()
        self.assertNotEqual(left_cross, right_cross)
        self.assertEqual(a_oriented_even_moment(left, 6), 132)
        self.assertEqual(a_oriented_even_moment(right, 6), 2916)

    def test_quartic_split_persists_in_higher_a_dimensions_by_zero_padding(self):
        base_left = (1, -1, 0, 0)
        base_right = (1, 1, -1, -1)
        for slots in range(4, 9):
            left = base_left + (0,) * (slots - 4)
            right = base_right + (0,) * (slots - 4)
            left_cross = a_oriented_even_moment(left, 4) * power_sum(right, 2) ** 2
            right_cross = a_oriented_even_moment(right, 4) * power_sum(left, 2) ** 2
            self.assertNotEqual(left_cross, right_cross)


if __name__ == "__main__":
    unittest.main()
