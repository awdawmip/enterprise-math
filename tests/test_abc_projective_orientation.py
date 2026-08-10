import unittest

from enterprise_math.abc_projective_orientation import (
    projective_orientation_state,
    raw_derivative_mass,
)


class ProjectiveOrientationTests(unittest.TestCase):
    def test_raw_derivative_mass(self) -> None:
        self.assertEqual(raw_derivative_mass(1), 0)
        self.assertEqual(raw_derivative_mass(30), 31)
        self.assertEqual(raw_derivative_mass(31), 1)
        self.assertEqual(raw_derivative_mass(128), 448)

    def test_squarefree_side_can_be_superdominant(self) -> None:
        state = projective_orientation_state(1, 30, 31)
        self.assertEqual(state.derivative_masses, (0, 31, 1))
        self.assertEqual(state.predicted_maximizers, (1,))

    def test_classical_high_quality_triple_is_b_oriented(self) -> None:
        b = 3**10 * 109
        c = 23**5
        self.assertEqual(2 + b, c)
        state = projective_orientation_state(2, b, c)
        self.assertEqual(state.derivative_masses[0], 1)
        self.assertGreater(
            state.derivative_masses[1],
            state.derivative_masses[0] + state.derivative_masses[2],
        )
        self.assertEqual(state.predicted_maximizers, (1,))

    def test_hard_unit_example_is_c_oriented(self) -> None:
        state = projective_orientation_state(1, 239**2, 2 * 13**4)
        self.assertEqual(state.predicted_maximizers, (2,))

    def test_equality_produces_exact_tie(self) -> None:
        state = projective_orientation_state(1, 2, 3)
        self.assertEqual(state.derivative_masses, (0, 1, 1))
        self.assertEqual(state.predicted_maximizers, (1, 2))
        self.assertEqual(state.exact_maximizers, (1, 2))


if __name__ == "__main__":
    unittest.main()
