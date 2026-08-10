import unittest

from enterprise_math.p017_p018_core_adaptive_bonferroni import (
    core_adaptive_signed_profile,
)
from enterprise_math.p017_p018_full_core_incidence import (
    full_core_incidence_mobius,
    high_core_bonferroni_weight,
)


class P017P018FullCoreIncidenceTests(unittest.TestCase):
    def test_k22_full_core_mobius_matches_repeated_low_core(self):
        data = full_core_incidence_mobius(22, 17)

        self.assertEqual(data["full_core_incidence"], 2)
        self.assertEqual(data["direct_signed_points"], (-21, 13))
        self.assertFalse(data["high_core_single_use"])

    def test_k22_high_full_cores_are_single_use(self):
        expected = {
            525: (-19,),
            513: (-7,),
            507: (-1,),
        }
        for full_core, points in expected.items():
            data = full_core_incidence_mobius(22, full_core)
            self.assertEqual(data["full_core_incidence"], 1)
            self.assertEqual(data["direct_signed_points"], points)
            self.assertTrue(data["high_core_single_use"])

    def test_k22_high_core_column_weights_reconstruct_generic_correction(self):
        correction = sum(
            full_core_incidence_mobius(22, full_core)["full_core_incidence"]
            * high_core_bonferroni_weight(full_core, 1)
            for full_core in (525, 513, 507)
        )
        profile = core_adaptive_signed_profile(22, 1)

        self.assertEqual(correction, 4)
        self.assertEqual(profile["high_core_defect_correction"], correction)
        self.assertEqual(profile["ordinary_bonferroni_sum"], 17)
        self.assertEqual(profile["core_adaptive_sum"], 13)
        self.assertTrue(profile["core_adaptive_certificate"])


if __name__ == "__main__":
    unittest.main()
