import itertools
import unittest
from fractions import Fraction

from enterprise_math.a3_a4_support_bridge import (
    all_cross_pairs_supported,
    coarse_pair_supported_from_partition,
    common_target_support,
    existential_threshold_block_state,
    existential_threshold_query,
    generated_support_relation,
    generated_support_report,
    interval_hull_from_potential_support,
    merge_existential_threshold_states,
    merge_universal_threshold_states,
    missing_interpolations,
    split_complete_at,
    universal_fine_support_implies_coarse_support,
    universal_threshold_block_state,
    universal_threshold_query,
    zero_relation_classes,
)
from enterprise_math.admissible_support import common_target_relation
from enterprise_math.weighted_relation_field import weighted_relation_field


def test_zero_classes_and_radius_zero_identity():
    sizes = (1, 2, 1, 3)
    field = weighted_relation_field(sizes, (0, 4, 0, 6))
    assert zero_relation_classes(sizes, field) == ((0, 2), (1, 3))
    assert generated_support_relation(sizes, field, 0) == frozenset({(0, 0), (1, 1)})


def test_generated_family_uses_a4_contract():
    sizes = (1, 2, 3, 1)
    field = weighted_relation_field(sizes, (0, 3, 9, 5))
    report = generated_support_report(sizes, field, 8)
    assert report.zero_identity
    assert report.monotone
    assert report.subadditive


def test_common_target_is_canonical_a4_operation():
    sizes = (1, 1, 1)
    field = weighted_relation_field(sizes, (0, 1, 2))
    relation = generated_support_relation(sizes, field, 1)
    assert common_target_support(sizes, field, 1, 1) == common_target_relation(relation, relation)


def test_split_witness_and_missing_interpolation_cases():
    sizes = (1, 1, 1)
    field = weighted_relation_field(sizes, (0, 1, 2))
    assert split_complete_at(sizes, field, 1, 1)
    assert missing_interpolations(sizes, field, 1, 1) == frozenset()

    sizes = (1, 1)
    field = weighted_relation_field(sizes, (0, 2))
    assert not split_complete_at(sizes, field, 1, 1)
    missing = missing_interpolations(sizes, field, 1, 1)
    assert (0, 1) in missing and (1, 0) in missing


def test_fine_to_coarse_support_is_one_way():
    sizes = (1, 2, 1, 3)
    field = weighted_relation_field(sizes, (0, 2, 1, 6))
    assert all_cross_pairs_supported(sizes, field, (0, 1), (2, 3), 2)
    assert universal_fine_support_implies_coarse_support(sizes, field, (0, 1), (2, 3), 2)

    sizes = (1, 1, 1, 1)
    field = weighted_relation_field(sizes, (0, 10, 0, 10))
    assert coarse_pair_supported_from_partition(sizes, field, (0, 1), (2, 3), 0)
    assert not all_cross_pairs_supported(sizes, field, (0, 1), (2, 3), 0)


class ContextualMinimalityTests(unittest.TestCase):
    def test_universal_state_matches_direct_all_pairs_query_and_merge(self):
        sizes = (2, 3, 4, 5)
        totals = (1, -3, 8, 5)
        left_block = (0, 1)
        right_block = (2, 3)
        left_values = tuple(Fraction(totals[i], sizes[i]) for i in left_block)
        right_values = tuple(Fraction(totals[i], sizes[i]) for i in right_block)

        left = universal_threshold_block_state(sizes, totals, left_block)
        right = universal_threshold_block_state(sizes, totals, right_block)
        for radius in range(5):
            direct = all(abs(x - y) <= radius for x in left_values for y in right_values)
            self.assertEqual(universal_threshold_query(left, right, radius), direct)

        merged = merge_universal_threshold_states(left, right)
        self.assertEqual(
            merged,
            universal_threshold_block_state(sizes, totals, left_block + right_block),
        )

    def test_existential_state_matches_direct_any_pair_query_and_merge(self):
        sizes = (2, 3, 4, 5)
        totals = (1, -3, 8, 5)
        left_block = (0, 1)
        right_block = (2, 3)
        left_values = tuple(Fraction(totals[i], sizes[i]) for i in left_block)
        right_values = tuple(Fraction(totals[i], sizes[i]) for i in right_block)

        left = existential_threshold_block_state(sizes, totals, left_block)
        right = existential_threshold_block_state(sizes, totals, right_block)
        for radius in range(5):
            direct = any(abs(x - y) <= radius for x in left_values for y in right_values)
            self.assertEqual(existential_threshold_query(left, right, radius), direct)

        merged = merge_existential_threshold_states(left, right)
        self.assertEqual(
            merged,
            existential_threshold_block_state(sizes, totals, left_block + right_block),
        )
        self.assertEqual(interval_hull_from_potential_support(merged),
                         merge_universal_threshold_states(
                             universal_threshold_block_state(sizes, totals, left_block),
                             universal_threshold_block_state(sizes, totals, right_block),
                         ))

    def test_universal_language_really_needs_both_interval_endpoints_over_same_base_state(self):
        sizes = (1, 1, 1, 1, 1, 1)
        totals = (0, 0, 3, 0, 1, 2)
        left = universal_threshold_block_state(sizes, totals, (0, 1, 2))
        right = universal_threshold_block_state(sizes, totals, (3, 4, 5))
        probe = (Fraction(0), Fraction(0))
        self.assertEqual(sum(totals[i] for i in (0, 1, 2)), 3)
        self.assertEqual(sum(totals[i] for i in (3, 4, 5)), 3)
        self.assertEqual(left[0], right[0])
        self.assertNotEqual(left[1], right[1])
        self.assertFalse(universal_threshold_query(left, probe, 2))
        self.assertTrue(universal_threshold_query(right, probe, 2))

    def test_existential_language_requires_exact_support_even_with_same_base_and_hull(self):
        sizes = (1,) * 8
        totals = (0, 0, 3, 3, 0, 1, 2, 3)
        left = existential_threshold_block_state(sizes, totals, (0, 1, 2, 3))
        right = existential_threshold_block_state(sizes, totals, (4, 5, 6, 7))
        self.assertEqual(sum(totals[i] for i in (0, 1, 2, 3)), 6)
        self.assertEqual(sum(totals[i] for i in (4, 5, 6, 7)), 6)
        self.assertEqual(
            interval_hull_from_potential_support(left),
            interval_hull_from_potential_support(right),
        )
        probe = frozenset({Fraction(1)})
        self.assertFalse(existential_threshold_query(left, probe, 0))
        self.assertTrue(existential_threshold_query(right, probe, 0))

    def test_exhaustive_small_rational_oracle_for_sufficiency_merge_and_minimality(self):
        grid = tuple(Fraction(i, 2) for i in range(-3, 4))
        supports = tuple(
            frozenset(values)
            for size in range(1, len(grid) + 1)
            for values in itertools.combinations(grid, size)
        )

        for left in supports:
            left_hull = interval_hull_from_potential_support(left)
            for right in supports:
                right_hull = interval_hull_from_potential_support(right)
                direct_max = max(abs(x - y) for x in left for y in right)
                direct_min = min(abs(x - y) for x in left for y in right)
                for radius in range(4):
                    self.assertEqual(
                        universal_threshold_query(left_hull, right_hull, radius),
                        direct_max <= radius,
                    )
                    self.assertEqual(
                        existential_threshold_query(left, right, radius),
                        direct_min <= radius,
                    )
                union = left | right
                self.assertEqual(
                    merge_existential_threshold_states(left, right),
                    union,
                )
                self.assertEqual(
                    merge_universal_threshold_states(left_hull, right_hull),
                    interval_hull_from_potential_support(union),
                )

        # Existential global minimality: radius-zero singleton probes recover support.
        for left_index, left in enumerate(supports):
            for right in supports[left_index + 1:]:
                probe_value = next(iter(left.symmetric_difference(right)))
                probe = frozenset({probe_value})
                self.assertNotEqual(
                    existential_threshold_query(left, probe, 0),
                    existential_threshold_query(right, probe, 0),
                )

        # Universal global minimality on this rational oracle: distinct hulls are
        # separated by a singleton context and some integer radius.
        hulls = tuple(sorted({interval_hull_from_potential_support(s) for s in supports}))
        probes = tuple(Fraction(i, 2) for i in range(-12, 13))
        for left_index, left in enumerate(hulls):
            for right in hulls[left_index + 1:]:
                separated = False
                for probe_value in probes:
                    probe = (probe_value, probe_value)
                    for radius in range(9):
                        if universal_threshold_query(left, probe, radius) != universal_threshold_query(
                            right, probe, radius
                        ):
                            separated = True
                            break
                    if separated:
                        break
                self.assertTrue(separated, (left, right))


if __name__ == "__main__":
    unittest.main()
