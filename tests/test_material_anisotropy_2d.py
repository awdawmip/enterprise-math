import unittest
from collections import Counter
from itertools import product

from enterprise_math.material_anisotropy_2d import (
    X_ACTIVE,
    Y_ACTIVE,
    XY_ACTIVE,
    anisotropic_material_profile_2d,
    anisotropic_response_for_clearance_2d,
    anisotropic_response_spectrum_2d,
    minimum_clearance_observable_for_anisotropy_2d,
)
from enterprise_math.material_clearance_precision import (
    ACTIVE_COUNT,
    ACTIVE_SET,
    SCALAR_DEPTH,
)
from enterprise_math.material_hysteresis import RETURNING
from enterprise_math.material_response import explicit_material_curve_profile


def profile(samples, amplitude=100):
    return explicit_material_curve_profile(samples, samples, amplitude)


class MaterialAnisotropy2DTests(unittest.TestCase):
    def test_minimum_clearance_observable_tracks_declared_anisotropy(self):
        isotropic = anisotropic_material_profile_2d(
            profile((0, 20, 40, 60, 80, 100)),
            profile((0, 20, 40, 60, 80, 100)),
            profile((0, 20, 40, 60, 80, 100)),
        )
        count_only = anisotropic_material_profile_2d(
            profile((0, 20, 40, 60, 80, 100)),
            profile((0, 20, 40, 60, 80, 100)),
            profile((0, 10, 20, 30, 40, 50)),
        )
        exact_set = anisotropic_material_profile_2d(
            profile((0, 20, 40, 60, 80, 100)),
            profile((0, 15, 30, 45, 60, 75)),
            profile((0, 10, 20, 30, 40, 50)),
        )
        self.assertEqual(
            minimum_clearance_observable_for_anisotropy_2d(isotropic),
            SCALAR_DEPTH,
        )
        self.assertEqual(
            minimum_clearance_observable_for_anisotropy_2d(count_only),
            ACTIVE_COUNT,
        )
        self.assertEqual(
            minimum_clearance_observable_for_anisotropy_2d(exact_set),
            ACTIVE_SET,
        )

    def test_active_set_selects_axis_or_corner_profile_without_full_vector(self):
        anisotropic = anisotropic_material_profile_2d(
            profile((0, 20, 40, 60, 80, 100)),
            profile((0, 10, 20, 30, 40, 50)),
            profile((0, 5, 10, 15, 20, 25)),
        )
        d = 6
        # All have depth 2 because max(clearance)=4, but active sets differ.
        x = anisotropic_response_for_clearance_2d((4, 1), d, anisotropic)
        y = anisotropic_response_for_clearance_2d((1, 4), d, anisotropic)
        corner = anisotropic_response_for_clearance_2d((4, 4), d, anisotropic)
        self.assertEqual(x.clearance.active_indices, X_ACTIVE)
        self.assertEqual(y.clearance.active_indices, Y_ACTIVE)
        self.assertEqual(corner.clearance.active_indices, XY_ACTIVE)
        self.assertEqual(x.response_sample, 40)
        self.assertEqual(y.response_sample, 20)
        self.assertEqual(corner.response_sample, 10)

        # A different nonactive coordinate is intentionally discarded by this law.
        x2 = anisotropic_response_for_clearance_2d((4, 3), d, anisotropic)
        self.assertEqual(x2.clearance.layer_depth, x.clearance.layer_depth)
        self.assertEqual(x2.clearance.active_indices, x.clearance.active_indices)
        self.assertEqual(x2.response_sample, x.response_sample)

    def test_anisotropic_spectrum_matches_direct_clearance_enumeration(self):
        anisotropic = anisotropic_material_profile_2d(
            profile((0, 20, 40, 60, 80, 100)),
            profile((0, 10, 20, 30, 40, 50)),
            profile((0, 5, 10, 15, 20, 25)),
        )
        for d in range(2, 7):
            report = anisotropic_response_spectrum_2d(d, anisotropic, RETURNING)
            direct = Counter()
            for clearance in product(range(d), repeat=2):
                if clearance == (0, 0):
                    continue
                observation = anisotropic_response_for_clearance_2d(
                    clearance, d, anisotropic, RETURNING
                )
                if observation.response_sample is not None:
                    direct[observation.response_sample] += 1
            self.assertEqual(
                {(item.response_sample, item.state_count) for item in report.bins},
                set(direct.items()),
            )
            self.assertEqual(
                sum(item.state_count for item in report.bins),
                report.coverage.represented_states,
            )

    def test_isotropic_specialization_matches_one_response_per_depth(self):
        common = profile((0, 20, 40, 60, 80, 100))
        isotropic = anisotropic_material_profile_2d(common, common, common)
        report = anisotropic_response_spectrum_2d(6, isotropic)
        self.assertEqual(report.minimum_clearance_observable, SCALAR_DEPTH)
        # Every depth has one response value despite three active-set geometries.
        self.assertEqual(len(report.bins), 5)

    def test_common_scale_and_domain_are_required(self):
        with self.assertRaises(ValueError):
            anisotropic_material_profile_2d(
                profile((0, 50, 100), 100),
                profile((0, 100, 200), 200),
                profile((0, 50, 100), 100),
            )
        with self.assertRaises(ValueError):
            anisotropic_material_profile_2d(
                profile((0, 50, 100), 100),
                profile((0, 25, 50, 75, 100), 100),
                profile((0, 50, 100), 100),
            )


if __name__ == "__main__":
    unittest.main()
