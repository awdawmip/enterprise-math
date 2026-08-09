import unittest

from enterprise_math.material_cyclotomic_phase import (
    cyclotomic_orbit_invariant,
    cyclotomic_polynomial,
    cyclotomic_step,
    euler_totient,
    primitive_cyclotomic_clock,
)


class MaterialCyclotomicPhaseTests(unittest.TestCase):
    def test_reference_cyclotomic_polynomials_are_exact_integer_coefficients(self):
        expected = {
            1: (-1, 1),
            2: (1, 1),
            3: (1, 1, 1),
            4: (1, 0, 1),
            5: (1, 1, 1, 1, 1),
            6: (1, -1, 1),
            8: (1, 0, 0, 0, 1),
            10: (1, -1, 1, -1, 1),
            12: (1, 0, -1, 0, 1),
        }
        for order, poly in expected.items():
            self.assertEqual(cyclotomic_polynomial(order), poly)
            self.assertEqual(len(poly) - 1, euler_totient(order))

    def test_primitive_companion_clocks_have_exact_declared_order(self):
        for order in range(1, 21):
            clock = primitive_cyclotomic_clock(order)
            self.assertTrue(clock.exact_order_verified)
            self.assertEqual(clock.dimension, euler_totient(order))
            basis = (1,) + (0,) * (clock.dimension - 1)
            current = basis
            first_return = None
            for step in range(1, order + 1):
                current = cyclotomic_step(clock, current)
                if current == basis:
                    first_return = step
                    break
            self.assertEqual(first_return, order)

    def test_two_dimensional_primitive_orders_are_exactly_1_2_3_4_6_in_small_search(self):
        orders = [n for n in range(1, 50) if euler_totient(n) <= 2]
        self.assertEqual(orders, [1, 2, 3, 4, 6])

    def test_higher_exact_phase_resolution_costs_internal_dimension(self):
        cases = ((5, 4), (7, 6), (8, 4), (10, 4), (12, 4), (15, 8))
        for order, dimension in cases:
            clock = primitive_cyclotomic_clock(order)
            self.assertEqual(clock.dimension, dimension)
            self.assertGreater(clock.dimension, 2)

    def test_orbit_sum_is_positive_and_exactly_invariant_under_one_clock_step(self):
        for order in (3, 4, 5, 6, 7, 8, 10, 12):
            clock = primitive_cyclotomic_clock(order)
            states = [
                (1,) + (0,) * (clock.dimension - 1),
                tuple(range(1, clock.dimension + 1)),
            ]
            for state in states:
                before = cyclotomic_orbit_invariant(clock, state)
                after_state = cyclotomic_step(clock, state)
                after = cyclotomic_orbit_invariant(clock, after_state)
                self.assertEqual(before, after)
                self.assertGreater(before, 0)

    def test_zero_state_has_zero_orbit_invariant(self):
        clock = primitive_cyclotomic_clock(7)
        zero = (0,) * clock.dimension
        self.assertEqual(cyclotomic_orbit_invariant(clock, zero), 0)

    def test_general_exact_order_need_not_equal_one_primitive_mode_dimension(self):
        # This regression protects the scope of the phi(n) statement: a direct
        # sum of lower primitive modes can have order lcm without containing Phi_n.
        # For n=15, primitive dimension is phi(15)=8, while separate order-3 and
        # order-5 modes use 2+4=6 dimensions and their block order is lcm(3,5)=15.
        self.assertEqual(euler_totient(15), 8)
        self.assertEqual(euler_totient(3) + euler_totient(5), 6)

    def test_invalid_order_is_rejected(self):
        with self.assertRaises(ValueError):
            primitive_cyclotomic_clock(0)


if __name__ == "__main__":
    unittest.main()
