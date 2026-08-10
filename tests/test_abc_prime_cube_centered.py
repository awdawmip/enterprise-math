import unittest
from fractions import Fraction

from enterprise_math.abc_prime_cube_centered import (
    prime_cube_difference_centered_state,
    prime_cube_sum_centered_state,
)


class PrimeCubeCenteredTests(unittest.TestCase):
    def test_active_cube_sum_formula(self) -> None:
        state = prime_cube_sum_centered_state(5, 59)
        self.assertEqual((state.center, state.radius), (32, 27))
        self.assertEqual(state.quadratic_factor, 3211)
        self.assertEqual(state.overlap_three, 1)
        self.assertEqual(state.parity_multiplier, 2)
        self.assertEqual(state.projective_atom_value, Fraction(13, 6))
        self.assertFalse(state.cheap_squarefree_guard)

    def test_squarefree_cube_sum_quadratic_factor_is_safe(self) -> None:
        state = prime_cube_sum_centered_state(3, 5)
        self.assertEqual((state.center, state.radius), (4, 1))
        self.assertEqual(state.quadratic_factor, 19)
        self.assertTrue(state.cheap_squarefree_guard)
        self.assertEqual(state.projective_atom_value, Fraction(1, 6))

    def test_active_cube_difference_formula(self) -> None:
        state = prime_cube_difference_centered_state(5, 101)
        self.assertEqual((state.center, state.radius), (53, 48))
        self.assertEqual(state.overlap_three, 3)
        self.assertEqual(state.parity_multiplier, 2)
        self.assertEqual(state.projective_atom_value, Fraction(56, 53))
        self.assertFalse(state.cheap_squarefree_guard)

    def test_double_squarefree_cube_difference_is_safe(self) -> None:
        state = prime_cube_difference_centered_state(3, 7)
        self.assertEqual((state.center, state.radius), (5, 2))
        self.assertEqual(state.quadratic_factor, 79)
        self.assertTrue(state.cheap_squarefree_guard)
        self.assertEqual(state.projective_atom_value, Fraction(1, 15))


if __name__ == "__main__":
    unittest.main()
