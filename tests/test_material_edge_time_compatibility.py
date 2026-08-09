import unittest

from enterprise_math.material_edge_time_compatibility import (
    OUTWARD_AFTER,
    TURN_AT_ENDPOINT,
    candidates_at_declared_duration,
    loading_endpoint_time_candidates,
    returning_endpoint_time_candidates,
)
from enterprise_math.material_force_work import uniform_force_law
from enterprise_math.material_response import explicit_material_curve_profile


class MaterialEdgeTimeCompatibilityTests(unittest.TestCase):
    def setUp(self):
        self.hooke = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 1, 2, 3, 4),
                returning=(0, 1, 2, 3, 4),
                amplitude=4,
            )
        )

    def test_hooke_p4_has_exact_turn_but_natural_duration_two_not_one(self):
        candidates = loading_endpoint_time_candidates(self.hooke, 0, 4)
        turn = [c for c in candidates if c.end_depth == 4 and c.momentum_after == 0]
        self.assertEqual(len(turn), 1)
        self.assertEqual(turn[0].motion_phase_after, TURN_AT_ENDPOINT)
        self.assertEqual(
            (turn[0].required_duration.numerator, turn[0].required_duration.denominator),
            (2, 1),
        )
        self.assertEqual(candidates_at_declared_duration(candidates, 1), ())
        self.assertEqual(candidates_at_declared_duration(candidates, 2), tuple(turn))

    def test_hooke_p5_has_unit_time_energy_consistent_endpoint(self):
        candidates = loading_endpoint_time_candidates(self.hooke, 0, 5)
        unit = candidates_at_declared_duration(candidates, 1)
        self.assertEqual(len(unit), 1)
        candidate = unit[0]
        self.assertEqual((candidate.end_depth, candidate.momentum_after), (4, 3))
        self.assertEqual(candidate.branch_work_numerator2, 16)

    def test_loading_energy_can_support_both_pre_and_post_turn_signs_at_different_durations(self):
        candidates = loading_endpoint_time_candidates(self.hooke, 0, 5)
        depth4 = [c for c in candidates if c.end_depth == 4]
        self.assertEqual(
            [(c.momentum_after, c.required_duration.numerator, c.required_duration.denominator) for c in depth4],
            [(-3, 4, 1), (3, 1, 1)],
        )
        self.assertEqual(depth4[0].motion_phase_after, OUTWARD_AFTER)

    def test_square_slope_hooke_turn_duration_is_depth_independent(self):
        # L_k=b^2*k with b=2 gives work2=(2K)^2. Starting p0=2K and p1=0,
        # the exact turn duration is 2K/(2K)=1 for every represented depth.
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=tuple(4 * k for k in range(9)),
                returning=tuple(4 * k for k in range(9)),
                amplitude=32,
            )
        )
        for depth in range(1, 9):
            candidates = loading_endpoint_time_candidates(law, 0, 2 * depth)
            turn = [c for c in candidates if c.end_depth == depth and c.momentum_after == 0]
            self.assertEqual(len(turn), 1)
            self.assertEqual(
                (turn[0].required_duration.numerator, turn[0].required_duration.denominator),
                (1, 1),
            )

    def test_square_slope_return_from_rest_has_depth_independent_duration_two_over_a(self):
        # R_k=a^2*k with a=1: from rest at K to zero deformation gives p1=K,
        # and tau=2K/K=2 independently of K.
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=tuple(4 * k for k in range(7)),
                returning=tuple(k for k in range(7)),
                amplitude=24,
            )
        )
        for depth in range(1, 7):
            candidates = returning_endpoint_time_candidates(law, depth, 0)
            target = [c for c in candidates if c.end_depth == 0]
            self.assertEqual(len(target), 1)
            self.assertEqual(target[0].momentum_after, depth)
            self.assertEqual(
                (target[0].required_duration.numerator, target[0].required_duration.denominator),
                (2, 1),
            )

    def test_non_square_remaining_energy_is_momentum_closure_failure_not_time_failure(self):
        # Hooke p0=4 to depth3 leaves 16-9=7, so there is no exact integer momentum
        # candidate at any rational duration in this value language.
        candidates = loading_endpoint_time_candidates(self.hooke, 0, 4)
        self.assertFalse(any(c.end_depth == 3 for c in candidates))

    def test_mass_rescales_required_duration_exactly(self):
        unit = loading_endpoint_time_candidates(self.hooke, 0, 5, mass_count=1)
        double = loading_endpoint_time_candidates(self.hooke, 0, 5, mass_count=2)
        unit_c = [c for c in unit if c.end_depth == 4 and c.momentum_after == 3][0]
        double_c = [c for c in double if c.end_depth == 4 and c.momentum_after == 3][0]
        self.assertEqual((unit_c.required_duration.numerator, unit_c.required_duration.denominator), (1, 1))
        self.assertEqual((double_c.required_duration.numerator, double_c.required_duration.denominator), (2, 1))

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            loading_endpoint_time_candidates(self.hooke, 0, -1)
        with self.assertRaises(ValueError):
            returning_endpoint_time_candidates(self.hooke, 99, 0)
        with self.assertRaises(ValueError):
            candidates_at_declared_duration((), 0)


if __name__ == "__main__":
    unittest.main()
