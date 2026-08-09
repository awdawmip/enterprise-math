import unittest

from enterprise_math.material_fit import (
    fit_integer_output_scale,
    predict_scaled_basis,
    project_interval_nearest,
    root_basin_versine_basis,
    search_root_basin_material_fit,
)

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
        projected = tuple(
            project_interval_nearest(value, 100, 761, 64)
            for value in TRELOAR_STRETCH_CENTI
        )
        self.assertEqual(projected[0], 0)
        self.assertEqual(projected[-1], 64)
        self.assertEqual(projected, tuple(sorted(projected)))

    def test_root_basin_basis_is_monotone(self):
        basis = root_basin_versine_basis(TRELOAR_STRETCH_CENTI, 128, 4, 2)
        self.assertEqual(basis[0], 0)
        self.assertEqual(basis[-1], 128)
        self.assertEqual(basis, tuple(sorted(basis)))

    def test_output_scale_search_matches_bruteforce_ordering(self):
        basis = (0, 2, 4)
        targets = (0, 3, 7)
        result = fit_integer_output_scale(targets, basis, 4, 12)
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
        scale, predictions, sse, l1, max_error = result
        self.assertEqual((sse, l1, max_error, scale, predictions), expected)

    def test_treloar_coarse_precision_has_fixed_reference_fit(self):
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

    def test_finer_precision_resolves_lower_error_reference_shape(self):
        basis = root_basin_versine_basis(TRELOAR_STRETCH_CENTI, 2048, 8, 3)
        scale, _pred, sse, _l1, _max = fit_integer_output_scale(
            TRELOAR_PK1_CENTI, basis, 2048, 800
        )
        self.assertEqual(scale, 663)
        self.assertEqual(sse, 5513)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            project_interval_nearest(5, 10, 0, 10)
        with self.assertRaises(ValueError):
            root_basin_versine_basis((1,), 10, 1, 1)


if __name__ == "__main__":
    unittest.main()
