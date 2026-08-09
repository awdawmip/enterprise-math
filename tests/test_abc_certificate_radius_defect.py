import unittest

from enterprise_math.abc_certificate_radius_defect import (
    normalized_wronskian_radius_defect,
)


class AbcCertificateRadiusDefectTests(unittest.TestCase):
    def test_4_plus_11_realizes_nonsplit_order_factorization(self) -> None:
        first = normalized_wronskian_radius_defect(4, 11, 15, 1)
        self.assertEqual(first.certificate_rank, 1)
        self.assertEqual(first.generated_normalized_image, 4)
        self.assertEqual(first.intrinsic_saturation_index, 2)
        self.assertEqual(first.access_image_index, 2)
        self.assertEqual(first.total_saturation_index, 4)

        second = normalized_wronskian_radius_defect(4, 11, 15, 2)
        self.assertEqual(second.generated_normalized_image, 2)
        self.assertEqual(second.intrinsic_saturation_index, 2)
        self.assertEqual(second.access_image_index, 1)
        self.assertEqual(second.total_saturation_index, 2)

    def test_5_plus_7_has_intrinsic_two_and_access_three_at_radius_one(self) -> None:
        first = normalized_wronskian_radius_defect(5, 7, 12, 1)
        self.assertEqual(first.generated_normalized_image, 6)
        self.assertEqual(first.intrinsic_saturation_index, 2)
        self.assertEqual(first.access_image_index, 3)
        self.assertEqual(first.total_saturation_index, 6)

        second = normalized_wronskian_radius_defect(5, 7, 12, 2)
        self.assertEqual(second.generated_normalized_image, 2)
        self.assertEqual(second.access_image_index, 1)

    def test_certificate_rank_can_be_zero_before_first_witness(self) -> None:
        data = normalized_wronskian_radius_defect(1, 242, 243, 4)
        self.assertEqual(data.certificate_rank, 0)
        self.assertEqual(data.generated_normalized_image, 0)
        self.assertEqual(data.intrinsic_saturation_index, 5)
        self.assertIsNone(data.access_image_index)
        self.assertIsNone(data.total_saturation_index)


if __name__ == "__main__":
    unittest.main()
