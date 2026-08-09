import unittest

from enterprise_math.material_impulse_reversal_certificate import (
    loading_branch_is_nondecreasing,
    monotone_loading_reversal_certificate,
)
from enterprise_math.material_impulse_world_1d import (
    TERMINAL_CONTACT,
    MomentumMaterialState1D,
    run_impulse_material_world_1d,
)
from enterprise_math.material_response import explicit_material_curve_profile
from enterprise_math.scale_tunneling_1d import Wall1D


class MaterialImpulseReversalCertificateTests(unittest.TestCase):
    def test_constant_branch_reduces_to_sharp_stopping_distance(self):
        profile = explicit_material_curve_profile(
            loading=(0, 4, 4, 4, 4, 4),
            returning=(0, 4, 4, 4, 4, 4),
            amplitude=4,
        )
        cert = monotone_loading_reversal_certificate(
            primitive_clearance=5,
            current_depth=1,
            initial_lifted_inward_numerator=20,
            profile=profile,
            mass_quanta=1,
            max_impulse_per_tick=2,
        )
        self.assertEqual(cert.minimum_impulse_numerator_per_tick, 8)
        self.assertEqual(cert.comparison_positive_drift_ticks, 2)
        self.assertEqual(cert.maximum_inward_drift_cells, 4)
        self.assertEqual(cert.maximum_reached_depth_before_noninward, 5)
        self.assertEqual(cert.latest_noninward_tick, 3)
        self.assertEqual(cert.latest_true_outward_tick, 3)
        self.assertTrue(cert.guaranteed_precontact_reversal)

        history = run_impulse_material_world_1d(
            MomentumMaterialState1D(-5, 5),
            Wall1D(0, 0),
            radius=0,
            collapse_factor=6,
            material_profile=profile,
            mass_quanta=1,
            max_impulse_per_tick=2,
            ticks=3,
        )
        self.assertIsNone(history.halted_kind)
        self.assertEqual(history.first_reversal_tick, 2)
        self.assertEqual(history.final.momentum_quanta, -1)

    def test_clearance_boundary_is_sharp_for_constant_branch(self):
        profile = explicit_material_curve_profile(
            loading=(0, 4, 4, 4, 4, 4),
            returning=(0, 4, 4, 4, 4, 4),
            amplitude=4,
        )
        cert = monotone_loading_reversal_certificate(
            4, 1, 20, profile, mass_quanta=1, max_impulse_per_tick=2
        )
        self.assertFalse(cert.clearance_sufficient)
        self.assertFalse(cert.guaranteed_precontact_reversal)
        history = run_impulse_material_world_1d(
            MomentumMaterialState1D(-4, 5),
            Wall1D(0, 0),
            0,
            5,
            profile,
            1,
            2,
            ticks=3,
        )
        self.assertEqual(history.halted_kind, TERMINAL_CONTACT)
        self.assertIsNone(history.final)

    def test_hardening_curve_can_reverse_strictly_before_comparison_deadline(self):
        profile = explicit_material_curve_profile(
            loading=(0, 1, 2, 4, 4, 4),
            returning=(0, 1, 2, 4, 4, 4),
            amplitude=4,
        )
        cert = monotone_loading_reversal_certificate(
            5, 1, 20, profile, mass_quanta=2, max_impulse_per_tick=4
        )
        self.assertTrue(cert.guaranteed_precontact_reversal)
        self.assertEqual(cert.maximum_inward_drift_cells, 4)
        self.assertEqual(cert.latest_true_outward_tick, 6)
        history = run_impulse_material_world_1d(
            MomentumMaterialState1D(-5, 5),
            Wall1D(0, 0),
            0,
            6,
            profile,
            2,
            4,
            ticks=6,
        )
        self.assertIsNone(history.halted_kind)
        self.assertIsNotNone(history.first_reversal_tick)
        self.assertLess(history.first_reversal_tick + 1, cert.latest_true_outward_tick)

    def test_finite_material_depth_is_part_of_the_certificate(self):
        short = explicit_material_curve_profile(
            loading=(0, 4, 4, 4),
            returning=(0, 4, 4, 4),
            amplitude=4,
        )
        cert = monotone_loading_reversal_certificate(
            5, 1, 20, short, mass_quanta=1, max_impulse_per_tick=2
        )
        self.assertTrue(cert.clearance_sufficient)
        self.assertFalse(cert.material_depth_sufficient)
        self.assertFalse(cert.guaranteed_precontact_reversal)

    def test_zero_current_force_and_nonmonotone_loading_do_not_get_the_certificate(self):
        zero_start = explicit_material_curve_profile(
            loading=(0, 0, 1, 2),
            returning=(0, 0, 1, 2),
            amplitude=2,
        )
        with self.assertRaises(ValueError):
            monotone_loading_reversal_certificate(4, 1, 8, zero_start, 1, 2)

        nonmonotone = explicit_material_curve_profile(
            loading=(0, 2, 1, 2),
            returning=(0, 2, 1, 2),
            amplitude=2,
        )
        self.assertFalse(loading_branch_is_nondecreasing(nonmonotone))
        with self.assertRaises(ValueError):
            monotone_loading_reversal_certificate(4, 1, 8, nonmonotone, 1, 2)


if __name__ == "__main__":
    unittest.main()
