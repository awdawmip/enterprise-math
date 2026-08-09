import unittest

from enterprise_math.abc_witness_flag import (
    exterior_two_form,
    primitive_flag_two_form,
    same_saturated_flag,
    shear_degeneracy_normal,
    witness_flag_signature,
)


class AbcWitnessFlagTests(unittest.TestCase):
    def test_two_form_coordinates(self) -> None:
        self.assertEqual(exterior_two_form((1, 2, 3), (4, 5, 6)), (-3, -6, -3))
        self.assertEqual(primitive_flag_two_form((1, 2, 3), (4, 5, 6)), (1, 2, 1))

    def test_shear_and_scale_do_not_change_flag(self) -> None:
        alpha = (80, -27, -1)
        beta = (0, 5, -1)
        transformed = shear_degeneracy_normal(alpha, beta, scale=2, shear=3)
        self.assertEqual(transformed, (240, -71, -5))
        self.assertTrue(same_saturated_flag(alpha, beta, alpha, transformed))

    def test_different_additive_normal_changes_flag(self) -> None:
        self.assertFalse(
            same_saturated_flag((1, -1), (1, 0), (2, -1), (1, 0))
        )

    def test_abc_flag_signature(self) -> None:
        signature = witness_flag_signature(5, 27, 32)
        self.assertEqual(signature["coordinates"], (2, 3, 5))
        self.assertEqual(signature["additive_normal"], (80, -27, -1))
        self.assertEqual(signature["flag_two_form"], (25, -5, 2))

    def test_dependent_rows_are_rejected(self) -> None:
        with self.assertRaises(ValueError):
            primitive_flag_two_form((1, 2), (2, 4))


if __name__ == "__main__":
    unittest.main()
