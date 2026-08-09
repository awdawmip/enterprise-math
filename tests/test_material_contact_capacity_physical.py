import unittest

from enterprise_math.material_contact_capacity_physical import (
    contact_impulse_capacity_at_precision,
    contact_impulse_capacity_refinement,
    exact_material_impulse_capacity,
)
from enterprise_math.material_physical_projection import ForceImpulseCountScale


def scale(
    force_scale=1,
    time_scale=1,
    momentum_scale=1,
    tick=1,
):
    return ForceImpulseCountScale(
        force_scale_factor=force_scale,
        time_scale_factor=time_scale,
        momentum_scale_factor=momentum_scale,
        tick_duration_count=tick,
        force_unit="F",
        time_unit="T",
        momentum_unit="P",
    )


class MaterialContactCapacityPhysicalTests(unittest.TestCase):
    def test_quarter_force_sample_is_not_destroyed_by_hidden_intermediate_rounding(self):
        exact = exact_material_impulse_capacity(
            response_sample=1,
            response_amplitude=4,
            full_scale_force_count=1,
            scale=scale(),
        )
        self.assertEqual((exact.reduced_numerator, exact.reduced_denominator), (1, 4))
        coarse = contact_impulse_capacity_at_precision(1, 4, 1, scale(), 1)
        fine = contact_impulse_capacity_at_precision(1, 4, 1, scale(), 4)
        self.assertEqual((coarse.capacity_numerator, coarse.projection_remainder), (0, 1))
        self.assertFalse(coarse.exactly_represented)
        self.assertEqual((fine.capacity_numerator, fine.projection_remainder), (1, 0))
        self.assertTrue(fine.exactly_represented)
        # If the material fraction had first been rounded to whole force counts,
        # it would have become zero and this exact quarter-impulse state would be lost.

    def test_declared_physical_scales_enter_exact_divisor_independently_of_material_amplitude(self):
        physical = scale(
            force_scale=100,
            time_scale=1000,
            momentum_scale=1000,
            tick=10,
        )
        exact = exact_material_impulse_capacity(
            response_sample=1,
            response_amplitude=2,
            full_scale_force_count=200,
            scale=physical,
        )
        self.assertEqual(exact.raw_numerator, 2_000_000)
        self.assertEqual(exact.raw_denominator, 200_000)
        self.assertEqual((exact.reduced_numerator, exact.reduced_denominator), (10, 1))
        at_one = contact_impulse_capacity_at_precision(
            1, 2, 200, physical, 1
        )
        self.assertEqual(at_one.capacity_numerator, 10)
        self.assertTrue(at_one.exactly_represented)

    def test_exact_representability_is_one_divisibility_sublattice(self):
        physical = scale()
        # Exact material impulse is 2/3.
        exact = exact_material_impulse_capacity(2, 3, 1, physical)
        self.assertEqual(exact.reduced_denominator, 3)
        for denominator in range(1, 16):
            report = contact_impulse_capacity_at_precision(
                2, 3, 1, physical, denominator
            )
            self.assertEqual(
                report.exactly_represented,
                denominator % 3 == 0,
            )

    def test_true_refinement_obeys_exact_capacity_carry_formula(self):
        physical = scale()
        for amplitude in range(1, 9):
            for response in range(amplitude + 1):
                for force_count in range(0, 6):
                    for coarse_denominator in range(1, 7):
                        for multiplier in (2, 3, 5):
                            report = contact_impulse_capacity_refinement(
                                response,
                                amplitude,
                                force_count,
                                physical,
                                coarse_denominator,
                                multiplier,
                            )
                            self.assertTrue(report.coarse_capacity_embeds)
                            self.assertGreaterEqual(
                                report.fine.capacity_numerator,
                                multiplier * report.coarse.capacity_numerator,
                            )
                            self.assertEqual(
                                report.fine.capacity_numerator,
                                multiplier * report.coarse.capacity_numerator
                                + report.exact_capacity_carry,
                            )

    def test_represented_physical_capacity_is_monotone_on_divisibility_refinement(self):
        physical = scale(force_scale=3, time_scale=5, momentum_scale=7, tick=2)
        for response in range(0, 6):
            coarse = contact_impulse_capacity_at_precision(
                response,
                5,
                11,
                physical,
                4,
            )
            fine = contact_impulse_capacity_at_precision(
                response,
                5,
                11,
                physical,
                12,
            )
            self.assertGreaterEqual(
                fine.capacity_numerator,
                3 * coarse.capacity_numerator,
            )
            # Compare represented rational capacities without floats.
            self.assertGreaterEqual(
                fine.capacity_numerator * coarse.contact_denominator,
                coarse.capacity_numerator * fine.contact_denominator,
            )

    def test_zero_material_response_has_zero_capacity_and_exact_denominator_one(self):
        exact = exact_material_impulse_capacity(0, 7, 100, scale())
        self.assertEqual(exact.reduced_numerator, 0)
        self.assertEqual(exact.reduced_denominator, 1)
        for denominator in (1, 2, 5, 12):
            report = contact_impulse_capacity_at_precision(
                0, 7, 100, scale(), denominator
            )
            self.assertEqual(report.capacity_numerator, 0)
            self.assertEqual(report.projection_remainder, 0)
            self.assertTrue(report.exactly_represented)

    def test_invalid_material_or_contact_precision_is_rejected(self):
        with self.assertRaises(ValueError):
            exact_material_impulse_capacity(3, 2, 1, scale())
        with self.assertRaises(ValueError):
            contact_impulse_capacity_at_precision(1, 2, 1, scale(), 0)
        with self.assertRaises(ValueError):
            contact_impulse_capacity_refinement(1, 2, 1, scale(), 1, 0)


if __name__ == "__main__":
    unittest.main()
