import unittest

from enterprise_math.guard_quotient_module import (
    determinantal_divisor,
    guard_partition_quotient_profile,
    guard_quotient_module_profile,
)


class GuardQuotientModuleTests(unittest.TestCase):
    def test_rank_one_two_guard_step_recovers_free_plus_torsion(self):
        profile = guard_quotient_module_profile(((6, -4),))
        self.assertEqual(profile.hidden_rank, 1)
        self.assertEqual(profile.free_rank, 1)
        self.assertEqual(profile.smith_invariant_factors, (2,))
        self.assertEqual(profile.torsion_factors, (2,))
        self.assertEqual(profile.torsion_order, 2)

    def test_primitive_rank_one_step_has_no_torsion(self):
        profile = guard_quotient_module_profile(((1, -1, 2),))
        self.assertEqual(profile.hidden_rank, 1)
        self.assertEqual(profile.free_rank, 2)
        self.assertEqual(profile.smith_invariant_factors, (1,))
        self.assertEqual(profile.torsion_factors, ())
        self.assertEqual(profile.torsion_order, 1)

    def test_full_rank_diagonal_two_and_three_is_cyclic_six_torsion(self):
        # Z^2 / <(2,0),(0,3)> is Z/2 x Z/3, hence isomorphic to Z/6.
        # Smith invariant factors are (1,6).
        generators = ((2, 0), (0, 3))
        self.assertEqual(determinantal_divisor(generators, 1), 1)
        self.assertEqual(determinantal_divisor(generators, 2), 6)
        profile = guard_quotient_module_profile(generators)
        self.assertEqual(profile.hidden_rank, 2)
        self.assertEqual(profile.free_rank, 0)
        self.assertEqual(profile.smith_invariant_factors, (1, 6))
        self.assertEqual(profile.torsion_factors, (6,))
        self.assertEqual(profile.torsion_order, 6)

    def test_redundant_generators_do_not_change_quotient_invariants(self):
        base = ((2, 0), (0, 4))
        redundant = ((2, 0), (0, 4), (2, 4), (4, 8))
        self.assertEqual(
            guard_quotient_module_profile(base),
            guard_quotient_module_profile(redundant),
        )

    def test_zero_hidden_lattice_leaves_all_guard_coordinates_free(self):
        profile = guard_quotient_module_profile((), guard_count=4)
        self.assertEqual(profile.hidden_rank, 0)
        self.assertEqual(profile.free_rank, 4)
        self.assertEqual(profile.smith_invariant_factors, ())
        self.assertEqual(profile.torsion_factors, ())
        self.assertEqual(profile.torsion_order, 1)

    def test_full_primitive_hidden_lattice_leaves_trivial_quotient(self):
        profile = guard_quotient_module_profile(
            ((1, 0, 0), (0, 1, 0), (0, 0, 1))
        )
        self.assertEqual(profile.hidden_rank, 3)
        self.assertEqual(profile.free_rank, 0)
        self.assertEqual(profile.smith_invariant_factors, (1, 1, 1))
        self.assertEqual(profile.torsion_factors, ())

    def test_partition_profile_matches_known_guard_images(self):
        guards = (
            (1, -1, 2, 2),
            (-1, 1, 3, 3),
        )
        partition = ((0, 1), (2, 3))
        profile = guard_partition_quotient_profile(guards, partition)
        self.assertEqual(profile.hidden_rank, 1)
        self.assertEqual(profile.free_rank, 1)
        self.assertEqual(profile.torsion_factors, (2,))

    def test_determinantal_divisors_match_known_three_dimensional_example(self):
        generators = (
            (2, 0, 0),
            (0, 4, 0),
            (0, 0, 8),
        )
        self.assertEqual(determinantal_divisor(generators, 1), 2)
        self.assertEqual(determinantal_divisor(generators, 2), 8)
        self.assertEqual(determinantal_divisor(generators, 3), 64)
        profile = guard_quotient_module_profile(generators)
        self.assertEqual(profile.smith_invariant_factors, (2, 4, 8))
        self.assertEqual(profile.torsion_order, 64)


if __name__ == "__main__":
    unittest.main()
