import unittest

from enterprise_math.material_oscillator import (
    FLOOR,
    TOWARD_ZERO,
    PythagoreanRotation,
    projected_rotation_step,
)
from enterprise_math.material_projection import rotation_projection_loss_identity


class MaterialProjectionTests(unittest.TestCase):
    def test_toward_zero_loss_is_exactly_reconstructed_from_details(self):
        rotation = PythagoreanRotation(3, 4, 5)
        saw_strict_loss = False
        for x in range(-10, 11):
            for y in range(-10, 11):
                report = projected_rotation_step(x, y, rotation, TOWARD_ZERO)
                identity = rotation_projection_loss_identity(report, rotation)
                self.assertEqual(
                    identity.scaled_norm_sq_loss,
                    identity.reconstructed_scaled_loss,
                )
                self.assertTrue(identity.nonnegative_from_sign_alignment)
                self.assertGreaterEqual(identity.quotient_detail_cross_term, 0)
                self.assertGreaterEqual(identity.detail_square_term, 0)
                self.assertGreaterEqual(identity.scaled_norm_sq_loss, 0)
                saw_strict_loss |= identity.scaled_norm_sq_loss > 0
        self.assertTrue(saw_strict_loss)

    def test_floor_growth_is_explained_by_negative_quotient_detail_cross_term(self):
        rotation = PythagoreanRotation(3, 4, 5)
        report = projected_rotation_step(-20, -19, rotation, FLOOR)
        identity = rotation_projection_loss_identity(report, rotation)
        self.assertLess(identity.scaled_norm_sq_loss, 0)
        self.assertLess(identity.quotient_detail_cross_term, 0)
        self.assertFalse(identity.nonnegative_from_sign_alignment)
        self.assertEqual(
            identity.scaled_norm_sq_loss,
            25 * (761 - 793),
        )

    def test_identity_holds_for_floor_policy_even_when_loss_sign_varies(self):
        rotation = PythagoreanRotation(5, 12, 13)
        saw_negative = False
        saw_nonnegative = False
        for x in range(-8, 9):
            for y in range(-8, 9):
                report = projected_rotation_step(x, y, rotation, FLOOR)
                identity = rotation_projection_loss_identity(report, rotation)
                self.assertEqual(
                    identity.scaled_norm_sq_loss,
                    identity.reconstructed_scaled_loss,
                )
                saw_negative |= identity.scaled_norm_sq_loss < 0
                saw_nonnegative |= identity.scaled_norm_sq_loss >= 0
        self.assertTrue(saw_negative)
        self.assertTrue(saw_nonnegative)


if __name__ == "__main__":
    unittest.main()
