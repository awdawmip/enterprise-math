import unittest

from enterprise_math.abc_certificate_index import normalized_wronskian_certificate_index


class AbcCertificateIndexTests(unittest.TestCase):
    def test_perfect_absorption_is_saturated_certificate_image(self) -> None:
        data = normalized_wronskian_certificate_index(2, 3, 5)
        self.assertEqual(data.raw_wronskian_image_generator, 1)
        self.assertEqual(data.residual_product, 1)
        self.assertEqual(data.normalized_saturation_index, 1)
        self.assertEqual(data.obstruction_spectrum, ())

    def test_5_plus_7_has_intrinsic_mod_two_certificate_defect(self) -> None:
        data = normalized_wronskian_certificate_index(5, 7, 12)
        self.assertEqual(data.raw_wronskian_image_generator, 4)
        self.assertEqual(data.residual_product, 2)
        self.assertEqual(data.normalized_image_generator, 2)
        self.assertEqual(data.normalized_saturation_index, 2)
        self.assertEqual(data.obstruction_spectrum, ((2, 1),))

    def test_high_quality_1_plus_242_retains_mod_five_defect(self) -> None:
        data = normalized_wronskian_certificate_index(1, 242, 243)
        self.assertEqual(data.raw_wronskian_image_generator, 4455)
        self.assertEqual(data.residual_product, 891)
        self.assertEqual(data.normalized_saturation_index, 5)
        self.assertEqual(data.obstruction_spectrum, ((5, 1),))

    def test_347_certificate_complete_can_still_be_intrinsically_unsaturated(self) -> None:
        data = normalized_wronskian_certificate_index(3, 4, 7)
        self.assertEqual(data.raw_wronskian_image_generator, 4)
        self.assertEqual(data.residual_product, 2)
        self.assertEqual(data.normalized_saturation_index, 2)


if __name__ == "__main__":
    unittest.main()
