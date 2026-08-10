import unittest

from enterprise_math.precision_structural_defect_diamond import structural_defect_diamond


class StructuralDefectDiamondTests(unittest.TestCase):
    def test_one_bit_premature_collapse_price(self):
        data = structural_defect_diamond(
            U_fine_rows=((1, 0),),
            U_coarse_rows=tuple(),
            W_strong_rows=((1, 0),),
            W_weak_rows=tuple(),
            p=2,
            K=1,
        )
        self.assertEqual(data["strong_observation_loss_mass"], 1)
        self.assertEqual(data["weak_observation_loss_mass"], 0)
        self.assertEqual(data["interaction_mass"], 1)

    def test_padic_depth_is_interaction_depth(self):
        data = structural_defect_diamond(
            U_fine_rows=((2, 0),),
            U_coarse_rows=tuple(),
            W_strong_rows=((2, 0),),
            W_weak_rows=tuple(),
            p=2,
            K=3,
        )
        self.assertEqual(data["interaction_mass"], 2)

    def test_zero_interaction_for_irrelevant_observation_direction(self):
        data = structural_defect_diamond(
            U_fine_rows=((1, 0),),
            U_coarse_rows=tuple(),
            W_strong_rows=((0, 1),),
            W_weak_rows=tuple(),
            p=2,
            K=2,
        )
        self.assertEqual(data["interaction_mass"], 0)
        self.assertEqual(data["strong_observation_loss_mass"], 0)

    def test_four_point_identity(self):
        data = structural_defect_diamond(
            U_fine_rows=((1, 0), (0, 2)),
            U_coarse_rows=((0, 2),),
            W_strong_rows=((1, 0), (0, 1)),
            W_weak_rows=((0, 1),),
            p=2,
            K=2,
        )
        cross = (
            data["delta_coarse_strong"]
            + data["delta_fine_weak"]
            - data["delta_fine_strong"]
            - data["delta_coarse_weak"]
        )
        self.assertEqual(cross, data["interaction_mass"])


if __name__ == "__main__":
    unittest.main()
