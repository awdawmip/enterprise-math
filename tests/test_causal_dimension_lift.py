import unittest

from enterprise_math.causal_dimension_lift import (
    coordinate_append_zero,
    dimension_lift_profile,
)
from enterprise_math.causal_gram_lattice import minimal_vectors
from enterprise_math.causal_laminated_lattice import (
    LAMBDA9_GRAM,
    lambda9_minimal_vectors,
    lambda10_minimal_vectors,
)


class CausalDimensionLiftTests(unittest.TestCase):
    def test_e8_to_lambda9_splits_one_uniform_old_type_into_128_plus_112(self):
        e8_gram = tuple(tuple(row[:8]) for row in LAMBDA9_GRAM[:8])
        old = minimal_vectors(e8_gram, 4)
        new = lambda9_minimal_vectors()
        profile = dimension_lift_profile(
            old,
            new,
            coordinate_append_zero,
            maximum_collision_order=4,
        )
        self.assertEqual(profile.old_primitive_count, 240)
        self.assertEqual(profile.new_primitive_count, 272)
        self.assertEqual(profile.added_primitive_count, 32)
        self.assertEqual(profile.old_type_sizes, (240,))
        self.assertEqual(profile.refined_old_type_sizes, (128, 112))
        self.assertEqual(profile.added_type_sizes, (32,))
        self.assertEqual(profile.old_type_count, 1)
        self.assertEqual(profile.refined_old_type_count, 2)
        self.assertEqual(profile.added_type_count, 1)
        self.assertEqual(
            profile.dimension_revelation_spectrum,
            (0, 14336, 1705984, 117931520),
        )

    def test_lambda9_to_lambda10_refines_only_one_old_local_type(self):
        profile = dimension_lift_profile(
            lambda9_minimal_vectors(),
            lambda10_minimal_vectors(),
            coordinate_append_zero,
            maximum_collision_order=4,
        )
        self.assertEqual(profile.old_primitive_count, 272)
        self.assertEqual(profile.new_primitive_count, 336)
        self.assertEqual(profile.added_primitive_count, 64)
        self.assertEqual(profile.old_type_sizes, (128, 112, 32))
        self.assertEqual(profile.refined_old_type_sizes, (128, 64, 48, 32))
        self.assertEqual(profile.added_type_sizes, (64,))
        self.assertEqual(profile.old_type_count, 3)
        self.assertEqual(profile.refined_old_type_count, 4)
        self.assertEqual(profile.added_type_count, 1)
        self.assertEqual(
            profile.dimension_revelation_spectrum,
            (0, 3072, 168960, 5380864),
        )

    def test_revelation_is_zero_when_new_context_does_not_split_old_types(self):
        # Synthetic causal lift: two old classes gain the same new relation context
        # inside each retained class.  The test guards the general theorem that
        # expansion may add states without forcing old-state refinement.
        old = ((1, 0), (-1, 0))
        new = ((1, 0, 0), (-1, 0, 0))
        profile = dimension_lift_profile(
            old,
            new,
            coordinate_append_zero,
            maximum_collision_order=2,
        )
        self.assertEqual(profile.dimension_revelation_spectrum, (0, 0))


if __name__ == "__main__":
    unittest.main()
