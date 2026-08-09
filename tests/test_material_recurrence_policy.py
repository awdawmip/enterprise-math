import unittest

from enterprise_math.material_oscillator import PythagoreanRotation
from enterprise_math.material_recurrence_policy import (
    MIN_QUADRATIC,
    TOWARD_ZERO,
    recurrence_policy_orbit,
    recurrence_policy_step,
)


class MaterialRecurrencePolicyTests(unittest.TestCase):
    def test_min_quadratic_policy_never_increases_Q_on_small_domain(self):
        rotation = PythagoreanRotation(3, 4, 5)
        for u in range(-25, 26):
            for v in range(-25, 26):
                report = recurrence_policy_step(u, v, rotation, MIN_QUADRATIC)
                self.assertGreaterEqual(report.selected.quadratic_defect, 0)

    def test_min_quadratic_policy_repairs_explicit_toward_zero_pumping_state(self):
        rotation = PythagoreanRotation(3, 4, 5)
        toward = recurrence_policy_step(-20, -19, rotation, TOWARD_ZERO)
        dissipative = recurrence_policy_step(-20, -19, rotation, MIN_QUADRATIC)
        self.assertEqual(toward.after, (-19, -2))
        self.assertEqual(toward.selected.quadratic_defect, -72)
        self.assertEqual(dissipative.after, (-19, -3))
        self.assertEqual(dissipative.selected.quadratic_defect, 17)

    def test_nonincrease_policy_can_stabilize_at_nonzero_fixed_plateau(self):
        rotation = PythagoreanRotation(3, 4, 5)
        orbit = recurrence_policy_orbit(
            (1, 0), rotation, MIN_QUADRATIC, max_steps=20
        )
        self.assertEqual(orbit[:4], ((1, 0), (0, -1), (-1, -1), (-1, -1)))
        self.assertNotEqual(orbit[-1], (0, 0))

    def test_toward_zero_and_min_quadratic_are_genuinely_different_policies(self):
        rotation = PythagoreanRotation(3, 4, 5)
        toward = recurrence_policy_orbit(
            (2, 0), rotation, TOWARD_ZERO, max_steps=20
        )
        min_q = recurrence_policy_orbit(
            (2, 0), rotation, MIN_QUADRATIC, max_steps=20
        )
        self.assertNotEqual(toward, min_q)

    def test_exact_divisible_step_has_identical_floor_ceil_candidate(self):
        rotation = PythagoreanRotation(3, 4, 5)
        report = recurrence_policy_step(1, 0, rotation, MIN_QUADRATIC)
        self.assertEqual(report.raw_second, -5)
        self.assertEqual(
            report.floor_candidate.next_value,
            report.ceil_candidate.next_value,
        )
        self.assertEqual(report.selected.detail, 0)

    def test_unknown_policy_is_rejected(self):
        with self.assertRaises(ValueError):
            recurrence_policy_step(
                1, 2, PythagoreanRotation(3, 4, 5), "UNKNOWN"
            )


if __name__ == "__main__":
    unittest.main()
