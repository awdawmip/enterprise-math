import unittest

from enterprise_math.material_fit import (
    fit_integer_output_scale,
    predict_scaled_basis,
    project_interval_nearest,
    root_basin_versine_basis,
    search_root_basin_material_fit,
)


# Treloar vulcanized-rubber uniaxial data as published in the public
# thermalCANN benchmark repository (Steinmann transcription).  Decimal values
# are represented exactly as centi-units so these tests remain integer-only.
TRELOAR_STRETCH_CENTI = (
    100, 101, 112, 124, 139, 161, 189, 217, 242, 301, 358, 403, 476,
    536, 576, 616, 640, 662, 687, 705, 716, 727, 743, 750, 761,
)
TRELOAR_PK1_CENTI = (
    0, 3, 14, 23, 32, 41, 50, 58, 67, 85, 104, 121, 158,
    194, 229, 267, 302, 339, 375, 412, 447, 485, 521, 557, 630,
)


class MaterialFitTests(unittest.TestCase):
    def test_interval_projection_preserves_endpoints_and_order(self):
        amplitude = 64
        projected = tuple(
            project_interval_nearest(value, 100, 761, amplitude)
            for value in TRELOAR_STRETCH_CENTI
        )
        self.assertEqual(projected[0], 0)
        self.assertEqual(projected[-1], amplitude)
        self.assertEqual(projected, tuple(sorted(projected)))

    def test_root_basin_versine_basis_is_monotone_and_scale_preserving(self):
        amplitude = 128
        basis = root_basin_versine_basis(
            TRELOAR_STRETCH_CENTI,
            amplitude=amplitude,
            input_root_power=4,
            output_hardening_power=2,
        )
        self.assertEqual(basis[0], 0)
        self.assertEqual(basis[-1], amplitude)
        self.assertEqual(basis, tuple(sorted(basis)))
        self.assertTrue(all(0 <= value <= amplitude for value in basis))

    def test_output_scale_search_is_exact_on_declared_finite_range(self):
        basis = (0, 2, 4)
        targets = (0, 3, 7)
        result = fit_integer_output_scale(
            targets,
            basis,
            amplitude=4,
            max_output_scale=12,
        )
        output_scale, predictions, sse, l1, max_error = result
        brute = []
        for scale in range(13):
            pred = predict_scaled_basis(basis, 4, scale)
            brute.append(
                (
                    sum((t - p) ** 2 for t, p in zip(targets, pred, strict=True)),
                    sum(abs(t - p) for t, p in zip(targets, pred, strict=True)),
                    max(abs(t - p) for t, p in zip(targets, pred, strict=True)),
                    scale,
                    pred,
                )
            )
        expected = min(brute, key=lambda item: item[:4])
        self.assertEqual((sse, l1, max_error, output_scale, predictions), expected)

    def test_treloar_coarse_precision_selects_small_integer_shape(self):
        fit = search_root_basin_material_fit(
            TRELOAR_STRETCH_CENTI,
            TRELOAR_PK1_CENTI,
            amplitude=128,
            max_input_root_power=12,
            max_output_hardening_power=6,
            max_output_scale=800,
        )
        self.assertEqual(
            (
                fit.input_root_power,
                fit.output_hardening_power,
                fit.output_scale,
                fit.sse,
                fit.absolute_error,
                fit.max_absolute_error,
            ),
            (4, 2, 672, 9426, 394, 42),
        )

    def test_finer_precision_resolves_a_different_lower_error_shape(self):
        coarse = search_root_basin_material_fit(
            TRELOAR_STRETCH_CENTI,
            TRELOAR_PK1_CENTI,
            amplitude=128,
            max_input_root_power=12,
            max_output_hardening_power=6,
            max_output_scale=800,
        )
        fine_basis = root_basin_versine_basis(
            TRELOAR_STRETCH_CENTI,
            amplitude=2048,
            input_root_power=8,
            output_hardening_power=3,
        )
        fine_scale, _pred, fine_sse, _l1, _max = fit_integer_output_scale(
            TRELOAR_PK1_CENTI,
            fine_basis,
            amplitude=2048,
            max_output_scale=800,
        )
        self.assertEqual(fine_scale, 663)
        self.assertEqual(fine_sse, 5513)
        self.assertLess(fine_sse, coarse.sse)

    def test_invalid_fit_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            project_interval_nearest(5, 10, 0, 10)
        with self.assertRaises(ValueError):
            root_basin_versine_basis((1,), 10, 1, 1)
        with self.assertRaises(ValueError):
            search_root_basin_material_fit((0, 1), (0,), 10, 2, 2, 10)


if __name__ == "__main__":
    unittest.main()
