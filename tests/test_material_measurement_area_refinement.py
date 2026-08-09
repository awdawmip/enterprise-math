import itertools
import unittest

from enterprise_math.material_measurement_area_refinement import (
    affine_transform_point,
    compare_refinement_orders,
    insert_measured_point,
    measured_point_lies_on_chord,
    measured_polyline_doubled_area,
    trace_measurement_refinement,
    trapezoid_refinement_shell,
    verify_refinement_shell_affine_covariance,
)


class MaterialMeasurementAreaRefinementTests(unittest.TestCase):
    def test_single_insert_shell_equals_exact_polyline_area_difference(self):
        left = (0, 0)
        inserted = (1, 2)
        right = (4, 0)
        shell = trapezoid_refinement_shell(left, inserted, right)
        self.assertEqual(shell, 8)
        self.assertEqual(
            shell,
            measured_polyline_doubled_area((left, inserted, right))
            - measured_polyline_doubled_area((left, right)),
        )

    def test_zero_shell_is_exact_integer_chord_collinearity(self):
        for e0 in range(-2, 3):
            for e2 in range(e0 + 2, e0 + 7):
                for s0 in range(-3, 4):
                    for s2 in range(-3, 4):
                        for e1 in range(e0 + 1, e2):
                            for s1 in range(-6, 7):
                                shell = trapezoid_refinement_shell(
                                    (e0, s0), (e1, s1), (e2, s2)
                                )
                                cross = (e2 - e0) * (s1 - s0)
                                chord = (e1 - e0) * (s2 - s0)
                                self.assertEqual(shell, cross - chord)
                                self.assertEqual(
                                    measured_point_lies_on_chord(
                                        (e0, s0), (e1, s1), (e2, s2)
                                    ),
                                    cross == chord,
                                )

    def test_affine_axis_translation_invariance_and_scale_covariance(self):
        points = ((-2, 3), (1, -4), (5, 2))
        original = trapezoid_refinement_shell(*points)
        for deformation_scale in range(1, 5):
            for response_scale in range(1, 5):
                for deformation_shift in (-7, 0, 5):
                    for response_shift in (-6, 0, 4):
                        self.assertTrue(
                            verify_refinement_shell_affine_covariance(
                                *points,
                                deformation_scale,
                                deformation_shift,
                                response_scale,
                                response_shift,
                            )
                        )
                        transformed = tuple(
                            affine_transform_point(
                                point,
                                deformation_scale,
                                deformation_shift,
                                response_scale,
                                response_shift,
                            )
                            for point in points
                        )
                        self.assertEqual(
                            trapezoid_refinement_shell(*transformed),
                            deformation_scale * response_scale * original,
                        )

    def test_multi_insert_local_shells_telescope_to_endpoint_area_difference(self):
        trace = trace_measurement_refinement(
            ((0, 0), (6, 0)),
            ((1, 3), (5, 2), (3, -1), (2, 4), (4, 1)),
        )
        self.assertEqual(sum(trace.local_area_shells), trace.total_area_shell)
        self.assertEqual(trace.total_area_shell, trace.endpoint_area_difference)
        self.assertEqual(
            trace.total_area_shell,
            measured_polyline_doubled_area(trace.final)
            - measured_polyline_doubled_area(trace.initial),
        )

    def test_same_final_measurements_can_have_different_local_witness_decomposition(self):
        comparison = compare_refinement_orders(
            ((0, 0), (4, 0)),
            ((1, 2), (3, 1)),
            ((3, 1), (1, 2)),
        )
        self.assertTrue(comparison.same_final_polyline)
        self.assertTrue(comparison.same_total_area_shell)
        self.assertFalse(comparison.same_local_shell_sequence)
        self.assertEqual(comparison.first.local_area_shells, (8, 1))
        self.assertEqual(comparison.second.local_area_shells, (4, 5))
        self.assertEqual(comparison.first.total_area_shell, 9)
        self.assertEqual(comparison.second.total_area_shell, 9)

    def test_nonzero_local_refinement_shells_can_cancel_in_final_area_coordinate(self):
        first = trace_measurement_refinement(
            ((0, 0), (3, 0)),
            ((1, 1), (2, -1)),
        )
        second = trace_measurement_refinement(
            ((0, 0), (3, 0)),
            ((2, -1), (1, 1)),
        )
        self.assertEqual(first.local_area_shells, (3, -3))
        self.assertEqual(second.local_area_shells, (-3, 3))
        self.assertEqual(first.total_area_shell, 0)
        self.assertEqual(second.total_area_shell, 0)
        self.assertEqual(first.final, second.final)
        self.assertEqual(
            measured_polyline_doubled_area(first.initial),
            measured_polyline_doubled_area(first.final),
        )

    def test_all_insertion_orders_share_total_shell_when_final_point_set_is_fixed(self):
        initial = ((0, 1), (8, -2))
        inserted = ((1, 3), (3, -1), (5, 4), (7, 0))
        expected_final = tuple(sorted(initial + inserted))
        expected_total = (
            measured_polyline_doubled_area(expected_final)
            - measured_polyline_doubled_area(initial)
        )
        witnessed_local_sequences = set()
        for order in itertools.permutations(inserted):
            trace = trace_measurement_refinement(initial, order)
            self.assertEqual(trace.final, expected_final)
            self.assertEqual(trace.total_area_shell, expected_total)
            witnessed_local_sequences.add(trace.local_area_shells)
        self.assertGreater(len(witnessed_local_sequences), 1)

    def test_inserting_real_measurement_does_not_silently_replace_existing_deformation_count(self):
        points = ((0, 0), (2, 4), (4, 0))
        with self.assertRaises(ValueError):
            insert_measured_point(points, (2, 9))
        with self.assertRaises(ValueError):
            insert_measured_point(points, (-1, 3))
        with self.assertRaises(ValueError):
            insert_measured_point(points, (5, 3))

    def test_invalid_polyline_and_affine_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            measured_polyline_doubled_area(((0, 0),))
        with self.assertRaises(ValueError):
            measured_polyline_doubled_area(((0, 0), (0, 1)))
        with self.assertRaises(ValueError):
            trapezoid_refinement_shell((0, 0), (2, 1), (1, 0))
        with self.assertRaises(ValueError):
            affine_transform_point((0, 0), 0, 0, 1, 0)
        with self.assertRaises(ValueError):
            affine_transform_point((0, 0), 1, 0, -1, 0)


if __name__ == "__main__":
    unittest.main()
