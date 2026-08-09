import unittest

from enterprise_math.material_validation import (
    cross_validate_fixed_domain_material_fit,
    evaluate_fit_indices,
    modulo_test_folds,
    search_fixed_domain_material_fit,
)

TRELOAR_STRETCH_CENTI = (
    100, 101, 112, 124, 139, 161, 189, 217, 242, 301, 358, 403, 476,
    536, 576, 616, 640, 662, 687, 705, 716, 727, 743, 750, 761,
)
TRELOAR_PK1_CENTI = (
    0, 3, 14, 23, 32, 41, 50, 58, 67, 85, 104, 121, 158,
    194, 229, 267, 302, 339, 375, 412, 447, 485, 521, 557, 630,
)


class MaterialValidationTests(unittest.TestCase):
    def test_fixed_domain_full_fit_reproduces_reference(self):
        fit = search_fixed_domain_material_fit(
            TRELOAR_STRETCH_CENTI,
            TRELOAR_PK1_CENTI,
            100,
            761,
            128,
            tuple(range(25)),
            4,
            2,
            700,
        )
        self.assertEqual(
            (
                fit.input_root_power,
                fit.output_hardening_power,
                fit.output_scale,
                fit.training_error.sse,
            ),
            (4, 2, 672, 9426),
        )

    def test_held_out_target_cannot_change_training_fit(self):
        x = (0, 1, 2, 3, 4)
        y = (0, 1, 3, 6, 10)
        changed = (0, 1, 3, 6, 999)
        args = dict(
            deformations=x,
            lower_deformation=0,
            upper_deformation=4,
            amplitude=32,
            training_indices=(0, 1, 2, 3),
            max_input_root_power=4,
            max_output_hardening_power=3,
            max_output_scale=32,
        )
        first = search_fixed_domain_material_fit(targets=y, **args)
        second = search_fixed_domain_material_fit(targets=changed, **args)
        self.assertEqual(
            (
                first.input_root_power,
                first.output_hardening_power,
                first.output_scale,
                first.training_error,
                first.predictions,
            ),
            (
                second.input_root_power,
                second.output_hardening_power,
                second.output_scale,
                second.training_error,
                second.predictions,
            ),
        )
        self.assertNotEqual(
            evaluate_fit_indices(first, y, (4,)),
            evaluate_fit_indices(second, changed, (4,)),
        )

    def test_treloar_five_fold_result_is_fixed(self):
        report = cross_validate_fixed_domain_material_fit(
            TRELOAR_STRETCH_CENTI,
            TRELOAR_PK1_CENTI,
            100,
            761,
            128,
            5,
            4,
            2,
            700,
        )
        self.assertEqual(report.aggregate_test_error.sse, 11505)
        self.assertEqual(report.aggregate_test_error.count, 25)
        self.assertEqual(
            tuple(
                (
                    fold.fit.input_root_power,
                    fold.fit.output_hardening_power,
                    fold.fit.output_scale,
                    fold.test_error.sse,
                )
                for fold in report.folds
            ),
            (
                (4, 2, 672, 2149),
                (4, 2, 672, 1433),
                (4, 2, 672, 927),
                (4, 2, 669, 2598),
                (4, 2, 688, 4398),
            ),
        )

    def test_modulo_folds_cover_each_observation_once(self):
        folds = modulo_test_folds(11, 3)
        flattened = tuple(index for fold in folds for index in fold)
        self.assertEqual(sorted(flattened), list(range(11)))
        self.assertEqual(len(flattened), len(set(flattened)))

    def test_mismatched_evaluation_dataset_is_rejected(self):
        fit = search_fixed_domain_material_fit(
            (0, 1, 2), (0, 1, 2), 0, 2, 8, (0, 1), 2, 2, 5
        )
        with self.assertRaises(ValueError):
            evaluate_fit_indices(fit, (0, 1), (0,))


if __name__ == "__main__":
    unittest.main()
