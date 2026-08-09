import unittest

from enterprise_math.material_contact_bridge import (
    CONTACT_DEAD_ZONE,
    CONTACT_REBOUND_RESOLVED,
    NO_CONTACT,
    material_contact_phase,
    minimum_collapse_factor_for_contact_and_rebound,
    minimum_collapse_factor_for_parameter_rebound,
    rebound_layer_capacity,
)


class MaterialContactBridgeTests(unittest.TestCase):
    def test_rebound_layer_capacity_is_exact_positive_gap_shell(self):
        for collapse_factor in range(1, 30):
            self.assertEqual(
                rebound_layer_capacity(collapse_factor), collapse_factor - 1
            )

    def test_material_rebound_threshold_has_closed_form(self):
        for m in range(2, 50):
            self.assertEqual(
                minimum_collapse_factor_for_parameter_rebound(m),
                m // 2 + 2,
            )

    def test_combined_threshold_is_maximum_of_contact_and_material_requirements(self):
        for gap in range(15):
            for m in range(2, 20):
                threshold = minimum_collapse_factor_for_contact_and_rebound(gap, m)
                self.assertEqual(threshold, max(gap + 1, m // 2 + 2))
                below = material_contact_phase(gap, threshold - 1, m)
                at = material_contact_phase(gap, threshold, m)
                self.assertFalse(below.rebound_resolved)
                self.assertEqual(at.status, CONTACT_REBOUND_RESOLVED)

    def test_reference_gap_and_material_parameter_have_three_scale_phases(self):
        gap = 3
        m = 20
        statuses = {
            d: material_contact_phase(gap, d, m).status for d in range(1, 15)
        }
        self.assertTrue(all(statuses[d] == NO_CONTACT for d in range(1, 4)))
        self.assertTrue(
            all(statuses[d] == CONTACT_DEAD_ZONE for d in range(4, 12))
        )
        self.assertTrue(
            all(statuses[d] == CONTACT_REBOUND_RESOLVED for d in range(12, 15))
        )

    def test_large_gap_can_skip_contact_dead_zone(self):
        gap = 20
        m = 4
        threshold = minimum_collapse_factor_for_contact_and_rebound(gap, m)
        self.assertEqual(threshold, 21)
        self.assertEqual(material_contact_phase(gap, 20, m).status, NO_CONTACT)
        self.assertEqual(
            material_contact_phase(gap, 21, m).status,
            CONTACT_REBOUND_RESOLVED,
        )

    def test_persistent_primitive_contact_can_still_be_materially_unresolved(self):
        gap = 0
        m = 20
        self.assertEqual(material_contact_phase(gap, 1, m).status, CONTACT_DEAD_ZONE)
        self.assertEqual(
            material_contact_phase(gap, 12, m).status,
            CONTACT_REBOUND_RESOLVED,
        )

    def test_phase_is_monotone_toward_resolved_rebound_under_coarsening(self):
        order = {
            NO_CONTACT: 0,
            CONTACT_DEAD_ZONE: 1,
            CONTACT_REBOUND_RESOLVED: 2,
        }
        for gap in range(10):
            for m in range(2, 20):
                phases = [
                    order[material_contact_phase(gap, d, m).status]
                    for d in range(1, 30)
                ]
                self.assertEqual(phases, sorted(phases))

    def test_invalid_factors_are_rejected(self):
        with self.assertRaises(ValueError):
            rebound_layer_capacity(0)
        with self.assertRaises(ValueError):
            material_contact_phase(-1, 2, 4)


if __name__ == "__main__":
    unittest.main()
