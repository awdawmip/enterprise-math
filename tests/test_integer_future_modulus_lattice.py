import itertools
import unittest
from math import gcd, lcm

from enterprise_math.integer_future_modulus_lattice import (
    modular_action_precision_lattice_report,
    modular_precision_join,
    modular_precision_meet,
    modulus_refines,
    pair_equal_mod_both_iff_equal_mod_lcm,
)


class IntegerFutureModulusLatticeTests(unittest.TestCase):
    def test_divisibility_is_the_precision_order_not_numeric_magnitude(self):
        self.assertTrue(modulus_refines(12, 6))
        self.assertTrue(modulus_refines(12, 4))
        self.assertFalse(modulus_refines(6, 4))
        self.assertFalse(modulus_refines(4, 6))
        self.assertTrue(modulus_refines(7, 1))

    def test_gcd_and_lcm_are_meet_and_join(self):
        for left in range(1, 13):
            for right in range(1, 13):
                meet = modular_precision_meet(left, right)
                join = modular_precision_join(left, right)
                self.assertEqual(meet, gcd(left, right))
                self.assertEqual(join, lcm(left, right))
                self.assertTrue(modulus_refines(left, meet))
                self.assertTrue(modulus_refines(right, meet))
                self.assertTrue(modulus_refines(join, left))
                self.assertTrue(modulus_refines(join, right))

    def test_pairwise_equality_mod_both_is_exactly_equality_mod_lcm(self):
        matrices = (
            ((1, 0), (0, 1)),
            ((2, 3),),
            ((1, 1), (1, -1)),
        )
        states = tuple(itertools.product(range(-3, 4), repeat=2))
        for matrix in matrices:
            for left_modulus in range(1, 7):
                for right_modulus in range(1, 7):
                    for left_state in states:
                        for right_state in states:
                            self.assertTrue(
                                pair_equal_mod_both_iff_equal_mod_lcm(
                                    matrix,
                                    left_state,
                                    right_state,
                                    left_modulus,
                                    right_modulus,
                                )
                            )

    def test_action_closure_horizon_respects_precision_lattice(self):
        action_a = (
            (0, 1, 0),
            (0, 0, 0),
            (0, 0, 0),
        )
        action_b = (
            (0, 0, 2),
            (0, 0, 1),
            (0, 0, 0),
        )
        for left, right in (
            (4, 6),
            (3, 8),
            (2, 12),
            (1, 9),
        ):
            report = modular_action_precision_lattice_report(
                (action_a, action_b),
                ((1, 0, 0),),
                left,
                right,
            )
            self.assertEqual(report.meet_modulus, gcd(left, right))
            self.assertEqual(report.join_modulus, lcm(left, right))
            self.assertTrue(report.join_horizon_is_max)
            self.assertTrue(report.meet_horizon_is_no_later_than_both)

    def test_numeric_larger_modulus_can_be_incomparable(self):
        # 6 > 4 numerically, but mod 6 does not retain the second 2-adic digit
        # that mod 4 sees, while mod 4 sees no 3-adic information.
        self.assertGreater(6, 4)
        self.assertFalse(modulus_refines(6, 4))
        self.assertFalse(modulus_refines(4, 6))
        self.assertEqual(modular_precision_meet(4, 6), 2)
        self.assertEqual(modular_precision_join(4, 6), 12)

    def test_validation(self):
        with self.assertRaises(ValueError):
            modular_precision_meet(0, 2)
        with self.assertRaises(TypeError):
            modulus_refines(False, 1)
        with self.assertRaises(ValueError):
            modular_action_precision_lattice_report(
                (((1,),),),
                ((1,),),
                0,
                1,
            )


if __name__ == "__main__":
    unittest.main()
