import unittest

from enterprise_math.causal_geometry_selection import (
    SplitPoint,
    anisotropy_split_frontier,
    anonymous_single_charge_forces_a_dimension,
    full_rank_flag_coherence,
    minimal_ambient_slots_for_exact_charge,
    symmetric_integer_charge_is_total,
)
from enterprise_math.causal_primitive_link_profile import (
    a_roots,
    d_roots,
    e6_scaled_roots,
    e7_scaled_roots,
    hcp_direction_graph,
    primitive_direction_graph,
    primitive_link_profile,
)


class CausalGeometrySelectionTests(unittest.TestCase):
    def test_hcp_has_two_incomparable_minimal_anisotropy_split_points(self):
        frontier = anisotropy_split_frontier(
            hcp_direction_graph(),
            maximum_relation_arity=3,
            maximum_future_depth=3,
        )
        self.assertEqual(
            frontier,
            (
                SplitPoint(1, 2, 2),
                SplitPoint(2, 1, 3),
            ),
        )

    def test_fcc_a3_has_no_split_inside_full_compatible_flag_language(self):
        adjacency = primitive_direction_graph(a_roots(3))
        self.assertEqual(
            anisotropy_split_frontier(adjacency, 3, 3),
            (),
        )
        self.assertTrue(full_rank_flag_coherence(primitive_link_profile(a_roots(3)), 3))

    def test_d5_first_split_frontier_is_three_relations_one_future_step(self):
        adjacency = primitive_direction_graph(d_roots(5))
        self.assertEqual(
            anisotropy_split_frontier(adjacency, 4, 3),
            (SplitPoint(3, 1, 2),),
        )
        self.assertFalse(full_rank_flag_coherence(primitive_link_profile(d_roots(5)), 5))

    def test_a_family_has_full_rank_flag_coherence(self):
        for p in range(1, 7):
            self.assertTrue(full_rank_flag_coherence(primitive_link_profile(a_roots(p)), p))

    def test_d4_and_e6_fail_full_rank_flag_coherence_for_different_reasons(self):
        self.assertFalse(full_rank_flag_coherence(primitive_link_profile(d_roots(4)), 4))
        self.assertFalse(full_rank_flag_coherence(primitive_link_profile(e6_scaled_roots()), 6))

    def test_e7_fails_before_rank_seven_due_to_five_flag_split(self):
        profile = primitive_link_profile(e7_scaled_roots(), maximum_flag_size=5)
        histograms = tuple(dict(hist) for hist in profile.flag_extension_histograms)
        self.assertEqual(len(histograms[4]), 2)
        self.assertFalse(full_rank_flag_coherence(profile, 7))

    def test_full_slot_permutation_invariant_linear_charge_is_total_charge_up_to_scale(self):
        self.assertTrue(symmetric_integer_charge_is_total((1, 1, 1, 1)))
        self.assertTrue(symmetric_integer_charge_is_total((-3, -3, -3)))
        self.assertFalse(symmetric_integer_charge_is_total((0, 0, 0)))
        self.assertFalse(symmetric_integer_charge_is_total((1, 1, 2, 1)))

    def test_minimal_anonymous_one_charge_ontology_uses_rank_plus_one_slots(self):
        for p in range(1, 10):
            self.assertEqual(minimal_ambient_slots_for_exact_charge(p, 1), p + 1)
            self.assertEqual(anonymous_single_charge_forces_a_dimension(p), (p + 1, p))


if __name__ == "__main__":
    unittest.main()
