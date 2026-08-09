import unittest

from enterprise_math.certificate_lattice_kernel import (
    adjoining_target_index,
    certificate_lattice_kernel,
    quotient_order,
    same_certificate_quotient_class,
    target_in_certificate_lattice,
    target_in_saturation,
)


class CertificateLatticeKernelTests(unittest.TestCase):
    def test_full_rank_membership_by_index_equality(self) -> None:
        kernel = certificate_lattice_kernel(((2, 0), (0, 3)))
        self.assertEqual(quotient_order(kernel), 6)
        self.assertTrue(target_in_saturation(kernel, (1, 1)))
        self.assertTrue(target_in_certificate_lattice(kernel, (4, 9)))
        self.assertFalse(target_in_certificate_lattice(kernel, (1, 1)))
        self.assertEqual(adjoining_target_index(kernel, (1, 1)), 1)
        self.assertEqual(adjoining_target_index(kernel, (2, 1)), 2)

    def test_low_rank_span_and_membership_are_separate(self) -> None:
        kernel = certificate_lattice_kernel(((2, 4), (4, 8)))
        self.assertEqual(kernel.signature.rank, 1)
        self.assertEqual(quotient_order(kernel), 2)
        self.assertTrue(target_in_saturation(kernel, (1, 2)))
        self.assertFalse(target_in_certificate_lattice(kernel, (1, 2)))
        self.assertTrue(target_in_certificate_lattice(kernel, (6, 12)))
        self.assertFalse(target_in_saturation(kernel, (1, 3)))
        self.assertIsNone(adjoining_target_index(kernel, (1, 3)))

    def test_equal_smith_type_different_labelled_kernel(self) -> None:
        first = certificate_lattice_kernel(((2, 0), (0, 1)))
        second = certificate_lattice_kernel(((1, 1), (1, -1)))
        self.assertEqual(first.signature.invariant_factors, (1, 2))
        self.assertEqual(second.signature.invariant_factors, (1, 2))
        target = (0, 1)
        self.assertTrue(target_in_certificate_lattice(first, target))
        self.assertFalse(target_in_certificate_lattice(second, target))

    def test_exact_quotient_class_equality(self) -> None:
        kernel = certificate_lattice_kernel(((4, 0), (0, 1)))
        self.assertTrue(same_certificate_quotient_class(kernel, (1, 5), (5, 2)))
        self.assertFalse(same_certificate_quotient_class(kernel, (1, 5), (2, 2)))

    def test_scalar_eta_kernel_is_mod_eta_without_explicit_normal_form(self) -> None:
        kernel = certificate_lattice_kernel(((5,),))
        self.assertTrue(same_certificate_quotient_class(kernel, (12,), (2,)))
        self.assertFalse(same_certificate_quotient_class(kernel, (12,), (3,)))
        self.assertTrue(target_in_certificate_lattice(kernel, (15,)))
        self.assertFalse(target_in_certificate_lattice(kernel, (12,)))


if __name__ == "__main__":
    unittest.main()
