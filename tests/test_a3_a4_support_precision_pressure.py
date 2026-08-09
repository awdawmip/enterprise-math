import unittest

from enterprise_math.guard_quotient_module import guard_partition_quotient_profile
from enterprise_math.hidden_band_predicate import hidden_band_profile_for_partition


CROSS_RELATION_GUARDS = (
    (1, 0, -1, 0),  # z_02 = c0-c2
    (1, 0, 0, -1),  # z_03 = c0-c3
    (0, 1, -1, 0),  # z_12 = c1-c2
    (0, 1, 0, -1),  # z_13 = c1-c3
)
PARTITION = ((0, 1), (2, 3))


def coarse_totals(state):
    return (state[0] + state[1], state[2] + state[3])


def cross_relations(state):
    return tuple(
        sum(weight * value for weight, value in zip(guard, state))
        for guard in CROSS_RELATION_GUARDS
    )


def universal_radius_zero_support(state):
    return all(value == 0 for value in cross_relations(state))


def coarse_cross_relation(state):
    # Sum of all four unit-capacity cross relations; this equals
    # 2*(coarse_total_left-coarse_total_right).
    return sum(cross_relations(state))


class A3A4SupportPrecisionPressureTests(unittest.TestCase):
    def test_cross_relation_guard_module_has_rank_two_and_z2_torsion(self):
        profile = guard_partition_quotient_profile(
            CROSS_RELATION_GUARDS, PARTITION
        )
        self.assertEqual(profile.guard_count, 4)
        self.assertEqual(profile.hidden_rank, 2)
        self.assertEqual(profile.free_rank, 2)
        self.assertEqual(profile.smith_invariant_factors, (1, 2))
        self.assertEqual(profile.torsion_factors, (2,))
        self.assertEqual(profile.torsion_order, 2)

    def test_same_coarse_state_contains_universal_support_true_and_false_lifts(self):
        supported = (5, 5, 5, 5)
        cancelled = (0, 10, 0, 10)
        self.assertEqual(coarse_totals(supported), (10, 10))
        self.assertEqual(coarse_totals(cancelled), (10, 10))
        self.assertEqual(coarse_cross_relation(supported), 0)
        self.assertEqual(coarse_cross_relation(cancelled), 0)
        self.assertTrue(universal_radius_zero_support(supported))
        self.assertFalse(universal_radius_zero_support(cancelled))
        self.assertEqual(cross_relations(cancelled), (0, -10, 10, 0))

    def test_each_hidden_fine_pair_radius_zero_query_is_ambiguous_at_zero_base(self):
        for guard in CROSS_RELATION_GUARDS:
            profile = hidden_band_profile_for_partition(
                guard,
                PARTITION,
                base_value=0,
                radius=0,
            )
            self.assertEqual(profile.hidden_step, 1)
            self.assertTrue(profile.has_supported_value)
            self.assertTrue(profile.has_unsupported_value)
            self.assertFalse(profile.exact)

    def test_coarse_relation_is_visible_even_when_universal_fine_support_is_not(self):
        # The coarse relation has coefficient vector (2,2,-2,-2), constant
        # inside both coarse blocks, so it is partition-readable.
        coarse_guard = (2, 2, -2, -2)
        visible = hidden_band_profile_for_partition(
            coarse_guard,
            PARTITION,
            base_value=0,
            radius=0,
        )
        self.assertEqual(visible.hidden_step, 0)
        self.assertTrue(visible.exact)
        self.assertTrue(visible.exact_value)


if __name__ == "__main__":
    unittest.main()
