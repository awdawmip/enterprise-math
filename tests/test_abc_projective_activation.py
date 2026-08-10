import unittest
from fractions import Fraction

from enterprise_math.abc_projective_activation import (
    projective_activation_state,
    same_activation_different_projective_value,
)


class ProjectiveActivationTests(unittest.TestCase):
    def test_subunit_basin(self) -> None:
        state = projective_activation_state(2, 3, 5)
        self.assertFalse(state.activated)
        self.assertTrue(all(state.cyclic_subunit))
        self.assertEqual(state.active_cyclic_indices, ())

    def test_boundary_and_superunit_states_activate(self) -> None:
        boundary = projective_activation_state(1, 2, 3)
        self.assertTrue(boundary.activated)
        self.assertEqual(boundary.sigma_projective, Fraction(1, 1))

        high = projective_activation_state(3, 125, 128)
        self.assertTrue(high.activated)
        self.assertGreater(high.sigma_projective, 4)

    def test_activation_erases_exact_projective_value(self) -> None:
        data = same_activation_different_projective_value()
        self.assertTrue(data["shared_activation"])
        self.assertEqual(data["projective_values"], (Fraction(1, 1), Fraction(2, 1)))


if __name__ == "__main__":
    unittest.main()
