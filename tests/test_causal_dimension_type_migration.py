import unittest

from enterprise_math.causal_dimension_type_migration import intrinsic_type_migration
from enterprise_math.causal_laminated_lattice import (
    lambda9_minimal_vectors,
    lambda10_minimal_vectors,
    lambda11_minimal_vectors,
    lambda12_minimal_vectors,
)


class CausalDimensionTypeMigrationTests(unittest.TestCase):
    def test_lambda9_to_lambda10_has_both_split_and_merge(self):
        profile = intrinsic_type_migration(
            lambda9_minimal_vectors(), lambda10_minimal_vectors(), maximum_order=4
        )
        self.assertEqual(profile.old_type_sizes, (128, 112, 32))
        self.assertEqual(profile.new_retained_type_sizes, (192, 48, 32))
        self.assertEqual(profile.common_refinement_sizes, (128, 64, 48, 32))
        self.assertTrue(profile.has_split)
        self.assertTrue(profile.has_merge)
        self.assertEqual(profile.revelation_spectrum, (0, 3072, 168960, 5380864))
        self.assertEqual(profile.healing_spectrum, (0, 8192, 778240, 43567104))

    def test_lambda10_to_lambda11_transports_old_types_without_split_or_merge(self):
        profile = intrinsic_type_migration(
            lambda10_minimal_vectors(), lambda11_minimal_vectors(), maximum_order=4
        )
        self.assertEqual(profile.old_type_sizes, (192, 96, 48))
        self.assertEqual(profile.new_retained_type_sizes, (192, 96, 48))
        self.assertEqual(profile.common_refinement_sizes, (192, 96, 48))
        self.assertFalse(profile.has_split)
        self.assertFalse(profile.has_merge)
        self.assertEqual(profile.revelation_spectrum, (0, 0, 0, 0))
        self.assertEqual(profile.healing_spectrum, (0, 0, 0, 0))

    def test_lambda11_to_lambda12_is_pure_intrinsic_healing_on_retained_shell(self):
        profile = intrinsic_type_migration(
            lambda11_minimal_vectors(), lambda12_minimal_vectors(), maximum_order=4
        )
        self.assertEqual(profile.old_type_sizes, (192, 192, 48, 6))
        self.assertEqual(profile.new_retained_type_sizes, (384, 54))
        self.assertEqual(profile.common_refinement_sizes, (192, 192, 48, 6))
        self.assertFalse(profile.has_split)
        self.assertTrue(profile.has_merge)
        self.assertEqual(profile.revelation_spectrum, (0, 0, 0, 0))
        self.assertEqual(profile.healing_spectrum, (0, 37152, 7048512, 782262072))


if __name__ == "__main__":
    unittest.main()
