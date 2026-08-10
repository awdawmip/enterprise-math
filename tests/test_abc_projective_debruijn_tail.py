import unittest

from enterprise_math.abc_projective_debruijn_tail import (
    dyadic_pair_radical_envelope_holds,
    normalized_projective_moment_bounded_range,
    projective_tail_external_power,
    projective_tail_pair_state,
)


class ProjectiveDebruijnTailTests(unittest.TestCase):
    def test_small_threshold_failure_has_pair_radical_envelope(self) -> None:
        # sigma_proj(3,125,128)=32/7, so threshold 4 is active.
        state = projective_tail_pair_state(3, 125, 128, 4)
        self.assertIsNotNone(state)
        assert state is not None
        self.assertEqual(state.component_values, (128, 125))
        self.assertEqual(state.residual_product, 1600)
        self.assertEqual(state.pair_radical_product, 10)
        self.assertTrue(dyadic_pair_radical_envelope_holds(state, 128))

    def test_threshold_above_sigma_returns_none(self) -> None:
        self.assertIsNone(projective_tail_pair_state(3, 125, 128, 5))

    def test_external_tail_power_is_X_over_T(self) -> None:
        self.assertEqual(projective_tail_external_power(), (1, -1))

    def test_normalized_moment_threshold_moves_to_two(self) -> None:
        for p, q in ((1, 2), (1, 1), (3, 2), (19, 10)):
            self.assertTrue(normalized_projective_moment_bounded_range(p, q))
        self.assertFalse(normalized_projective_moment_bounded_range(2, 1))
        self.assertFalse(normalized_projective_moment_bounded_range(5, 2))


if __name__ == "__main__":
    unittest.main()
