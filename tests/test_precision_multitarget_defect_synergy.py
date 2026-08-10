import unittest

from enterprise_math.precision_multitarget_defect_synergy import (
    multi_target_defect_decomposition,
    two_target_defect_synergy,
)


class MultiTargetDefectSynergyTests(unittest.TestCase):
    def test_xor_observation_creates_synergy(self):
        data = two_target_defect_synergy(
            U_rows=((1, 1),), W1_rows=((1, 0),), W2_rows=((0, 1),), p=2, K=1
        )
        self.assertEqual(data["target1_mass"], 1)
        self.assertEqual(data["target2_mass"], 1)
        self.assertEqual(data["intersection_mass"], 0)
        self.assertEqual(data["synergy_mass"], 1)
        self.assertEqual(data["joint_mass"], 1)

    def test_same_individual_overlap_data_can_have_different_joint(self):
        independent = two_target_defect_synergy(tuple(), ((1, 0),), ((0, 1),), 2, 1)
        coupled = two_target_defect_synergy(((1, 1),), ((1, 0),), ((0, 1),), 2, 1)
        self.assertEqual(
            (independent["target1_mass"], independent["target2_mass"], independent["intersection_mass"]),
            (coupled["target1_mass"], coupled["target2_mass"], coupled["intersection_mass"]),
        )
        self.assertNotEqual(independent["joint_mass"], coupled["joint_mass"])

    def test_three_target_canonical_decomposition(self):
        data = multi_target_defect_decomposition(
            U_rows=((1, 1, 0),),
            targets=(((1, 0, 0),), ((0, 1, 0),), ((0, 0, 1),)),
            p=2,
            K=1,
        )
        self.assertEqual(data["individual_masses"], (1, 1, 1))
        self.assertEqual(data["dependency_rebate_mass"], 0)
        self.assertEqual(data["synergy_rebate_mass"], 1)
        self.assertEqual(data["joint_mass"], 2)

    def test_target_dependency_rebate(self):
        data = multi_target_defect_decomposition(
            U_rows=tuple(),
            targets=(((1, 0),), ((0, 1),), ((1, 1),)),
            p=2,
            K=1,
        )
        self.assertEqual(data["individual_masses"], (1, 1, 1))
        self.assertEqual(data["dependency_rebate_mass"], 1)
        self.assertEqual(data["synergy_rebate_mass"], 0)
        self.assertEqual(data["joint_mass"], 2)


if __name__ == "__main__":
    unittest.main()
