import unittest

from enterprise_math.material_force_work import uniform_force_law
from enterprise_math.material_response import explicit_material_curve_profile
from enterprise_math.material_turn_return_witness import (
    EXACT_TURN_RETURN,
    NO_RETURN_MOTION,
    RETURN_MOMENTUM_UNDERRESOLVED,
    material_turn_return_witness,
)
from enterprise_math.material_work_energy_oracle import (
    MATERIAL_UNDERRESOLVED,
    TURN_UNDERRESOLVED,
)


class MaterialTurnReturnWitnessTests(unittest.TestCase):
    def test_square_slope_half_retention_is_complete_branch_aware_rebound_event(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=tuple(4 * k for k in range(9)),
                returning=tuple(k for k in range(9)),
                amplitude=32,
            )
        )
        for depth in range(1, 9):
            witness = material_turn_return_witness(law, incoming_momentum=2 * depth)
            self.assertEqual(witness.status, EXACT_TURN_RETURN)
            self.assertEqual(witness.turn_depth, depth)
            self.assertEqual(witness.outgoing_momentum, depth)
            self.assertEqual(
                (witness.momentum_retention_numerator, witness.momentum_retention_denominator),
                (1, 2),
            )
            self.assertEqual(
                (witness.loading_duration.numerator, witness.loading_duration.denominator),
                (1, 1),
            )
            self.assertEqual(
                (witness.returning_duration.numerator, witness.returning_duration.denominator),
                (2, 1),
            )
            self.assertEqual(
                (witness.total_duration.numerator, witness.total_duration.denominator),
                (3, 1),
            )

    def test_elastic_hooke_full_return_has_equal_momentum_and_equal_branch_times(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=tuple(k for k in range(7)),
                returning=tuple(k for k in range(7)),
                amplitude=6,
            )
        )
        for momentum in range(1, 7):
            witness = material_turn_return_witness(law, momentum)
            self.assertEqual(witness.status, EXACT_TURN_RETURN)
            self.assertEqual(witness.turn_depth, momentum)
            self.assertEqual(witness.outgoing_momentum, momentum)
            self.assertEqual(
                (witness.momentum_retention_numerator, witness.momentum_retention_denominator),
                (1, 1),
            )
            self.assertEqual(witness.loading_duration, witness.returning_duration)
            self.assertEqual(
                (witness.loading_duration.numerator, witness.loading_duration.denominator),
                (2, 1),
            )

    def test_turn_inside_material_interval_is_explicitly_underresolved(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 2, 4), returning=(0, 1, 2), amplitude=4
            )
        )
        witness = material_turn_return_witness(law, 2)
        self.assertEqual(witness.status, TURN_UNDERRESOLVED)
        self.assertIsNone(witness.turn_depth)
        self.assertIsNone(witness.outgoing_momentum)

    def test_incoming_resource_beyond_finite_material_depth_is_not_clamped(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 2, 4), returning=(0, 1, 2), amplitude=4
            )
        )
        witness = material_turn_return_witness(law, 4)
        self.assertEqual(witness.status, MATERIAL_UNDERRESOLVED)
        self.assertIsNone(witness.outgoing_momentum)

    def test_exact_turn_with_non_square_return_work_exposes_momentum_language_gap(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 4), returning=(0, 2), amplitude=4
            )
        )
        witness = material_turn_return_witness(law, 2)
        self.assertEqual(witness.turn_depth, 1)
        self.assertEqual(witness.returning_work_numerator2, 2)
        self.assertEqual(witness.status, RETURN_MOMENTUM_UNDERRESOLVED)
        self.assertIsNone(witness.outgoing_momentum)
        self.assertIsNotNone(witness.loading_duration)
        self.assertIsNone(witness.returning_duration)

    def test_zero_return_work_does_not_fabricate_a_return_motion(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 4), returning=(0, 0), amplitude=4
            )
        )
        witness = material_turn_return_witness(law, 2)
        self.assertEqual(witness.status, NO_RETURN_MOTION)
        self.assertEqual(witness.outgoing_momentum, 0)
        self.assertIsNone(witness.returning_duration)
        self.assertIsNone(witness.total_duration)

    def test_mass_rescales_both_branch_durations_but_not_retention(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 4, 8), returning=(0, 1, 2), amplitude=8
            )
        )
        unit = material_turn_return_witness(law, 4, mass_count=1)
        double = material_turn_return_witness(law, 4, mass_count=2)
        self.assertEqual(unit.status, EXACT_TURN_RETURN)
        self.assertEqual(double.status, EXACT_TURN_RETURN)
        self.assertEqual(unit.outgoing_momentum, double.outgoing_momentum)
        self.assertEqual(unit.momentum_retention_numerator, double.momentum_retention_numerator)
        self.assertEqual(unit.momentum_retention_denominator, double.momentum_retention_denominator)
        self.assertEqual(double.loading_duration.numerator, 2 * unit.loading_duration.numerator)
        self.assertEqual(double.returning_duration.numerator, 2 * unit.returning_duration.numerator)

    def test_invalid_zero_incoming_momentum_is_rejected_for_full_rebound_event(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 1), returning=(0, 1), amplitude=1
            )
        )
        with self.assertRaises(ValueError):
            material_turn_return_witness(law, 0)


if __name__ == "__main__":
    unittest.main()
