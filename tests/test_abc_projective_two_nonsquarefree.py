import unittest

from enterprise_math.abc_projective_two_nonsquarefree import (
    composite_squarefree_derivative_gap,
    two_nonsquarefree_projective_state,
)


class ProjectiveTwoNonsquarefreeTests(unittest.TestCase):
    def test_prime_squarefree_side_has_unit_derivative_gain(self) -> None:
        state = two_nonsquarefree_projective_state(3, 125, 128, 4)
        self.assertIsNotNone(state)
        assert state is not None
        self.assertEqual(state.squarefree_side_value, 3)
        self.assertEqual(state.squarefree_side_derivative, 1)
        self.assertEqual(state.repeated_pair, (125, 128))
        self.assertEqual(state.repeated_pair_radical, 10)
        self.assertLessEqual(
            4 * state.squarefree_side_derivative * state.repeated_pair_radical,
            128,
        )

    def test_composite_squarefree_side_gives_real_derivative_gain(self) -> None:
        # 10 + 3^7 = 13^3; sigma is the b-oriented 729/121 > 6.
        state = two_nonsquarefree_projective_state(10, 2187, 2197, 6)
        self.assertIsNotNone(state)
        assert state is not None
        self.assertEqual(state.squarefree_side_value, 10)
        self.assertEqual(state.squarefree_side_derivative, 7)
        self.assertEqual(state.repeated_pair, (2187, 2197))
        self.assertEqual(state.repeated_pair_radical, 39)
        self.assertLessEqual(6 * 7 * 39, 2197)
        self.assertTrue(composite_squarefree_derivative_gap(10))

    def test_another_composite_squarefree_side_threshold_one(self) -> None:
        # 22 + 3^7 = 47^2; sigma is 729/655 > 1.
        state = two_nonsquarefree_projective_state(22, 2187, 2209, 1)
        self.assertIsNotNone(state)
        assert state is not None
        self.assertEqual(state.squarefree_side_derivative, 13)
        self.assertEqual(state.repeated_pair_radical, 141)
        self.assertLessEqual(13 * 141, 2209)
        self.assertTrue(composite_squarefree_derivative_gap(22))

    def test_below_threshold_returns_none(self) -> None:
        self.assertIsNone(two_nonsquarefree_projective_state(3, 125, 128, 5))

    def test_shape_is_strict(self) -> None:
        with self.assertRaises(ValueError):
            two_nonsquarefree_projective_state(3, 5, 8, 1)
        with self.assertRaises(ValueError):
            two_nonsquarefree_projective_state(125, 361, 486, 1)


if __name__ == "__main__":
    unittest.main()
