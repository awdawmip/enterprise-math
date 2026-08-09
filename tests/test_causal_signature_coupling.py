import unittest

from enterprise_math.causal_signature_coupling import (
    compose_forgetting,
    coupling_certificate,
    coupling_fiber_multiplicities,
    coupling_kernel,
    coupling_split_spectrum,
    forgetting_defect,
    kernel_defects,
    staged_forgetting_defects,
)


class CausalSignatureCouplingTests(unittest.TestCase):
    def test_independent_signature_product_has_zero_typed_defect(self):
        joint_to_marginal = {
            "j00": ("a0", "b0"),
            "j01": ("a0", "b1"),
            "j10": ("a1", "b0"),
            "j11": ("a1", "b1"),
        }
        certificate = coupling_certificate(joint_to_marginal, 2, 2, 3)
        self.assertTrue(certificate.is_signature_independent)
        self.assertEqual(certificate.missing_reachability, 0)
        self.assertEqual(certificate.signature_split_excess, 0)
        self.assertEqual(certificate.split_spectrum, (4, 4, 0, 0))
        kernel = coupling_kernel(
            joint_to_marginal,
            ("a0", "a1"),
            ("b0", "b1"),
        )
        self.assertEqual(set(kernel.values()), {1})
        self.assertEqual(kernel_defects(kernel), (0, 0))

    def test_reachability_coupling_and_signature_splitting_are_distinct(self):
        constrained = {
            "j00": ("a0", "b0"),
            "j11": ("a1", "b1"),
        }
        constrained_certificate = coupling_certificate(constrained, 2, 2, 2)
        self.assertEqual(constrained_certificate.missing_reachability, 2)
        self.assertEqual(constrained_certificate.signature_split_excess, 0)

        split = {
            "j00a": ("a0", "b0"),
            "j00b": ("a0", "b0"),
            "j01": ("a0", "b1"),
            "j10": ("a1", "b0"),
            "j11": ("a1", "b1"),
        }
        split_certificate = coupling_certificate(split, 2, 2, 3)
        self.assertEqual(split_certificate.missing_reachability, 0)
        self.assertEqual(split_certificate.signature_split_excess, 1)
        self.assertEqual(coupling_fiber_multiplicities(split)[("a0", "b0")], 2)
        self.assertEqual(split_certificate.split_spectrum[2], 1)

    def test_kernel_values_keep_support_and_split_mechanisms_local(self):
        mixed = {
            "j0": ("a0", "b0"),
            "j1": ("a0", "b0"),
            "j2": ("a1", "b1"),
            "j3": ("a1", "b1"),
        }
        kernel = coupling_kernel(mixed, ("a0", "a1"), ("b0", "b1"))
        self.assertEqual(kernel[("a0", "b0")], 2)
        self.assertEqual(kernel[("a1", "b1")], 2)
        self.assertEqual(kernel[("a0", "b1")], 0)
        self.assertEqual(kernel[("a1", "b0")], 0)
        self.assertEqual(kernel_defects(kernel), (2, 2))

    def test_higher_split_spectrum_is_p011_collision_spectrum_of_forgetting(self):
        mapping = {
            "j0": ("a0", "b0"),
            "j1": ("a0", "b0"),
            "j2": ("a0", "b0"),
            "j3": ("a1", "b1"),
            "j4": ("a1", "b1"),
        }
        self.assertEqual(coupling_split_spectrum(mapping, 3), (2, 5, 4, 1))

    def test_first_order_split_excess_is_class_loss_under_cross_forgetting(self):
        mapping = {
            "j0": "r0",
            "j1": "r0",
            "j2": "r1",
            "j3": "r1",
            "j4": "r1",
        }
        self.assertEqual(forgetting_defect(mapping), 3)

    def test_staged_forgetting_has_exact_additive_first_order_defect(self):
        fine_to_middle = {
            "x0": "m0",
            "x1": "m0",
            "x2": "m1",
            "x3": "m2",
            "x4": "m3",
            "x5": "m3",
        }
        middle_to_coarse = {
            "m0": "c0",
            "m1": "c0",
            "m2": "c1",
            "m3": "c1",
        }
        first, second, total = staged_forgetting_defects(
            fine_to_middle,
            middle_to_coarse,
        )
        self.assertEqual((first, second, total), (2, 2, 4))
        self.assertEqual(total, first + second)
        composed = compose_forgetting(fine_to_middle, middle_to_coarse)
        self.assertEqual(forgetting_defect(composed), 4)

    def test_scalar_joint_minus_product_is_not_a_valid_coupling_summary(self):
        mixed = {
            "j0": ("a0", "b0"),
            "j1": ("a0", "b0"),
            "j2": ("a1", "b1"),
            "j3": ("a1", "b1"),
        }
        certificate = coupling_certificate(mixed, 2, 2, 2)
        self.assertEqual(certificate.joint_class_count, 4)
        self.assertEqual(2 * 2, 4)
        self.assertEqual(certificate.missing_reachability, 2)
        self.assertEqual(certificate.signature_split_excess, 2)
        self.assertFalse(certificate.is_signature_independent)


if __name__ == "__main__":
    unittest.main()
