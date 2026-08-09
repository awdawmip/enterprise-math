import unittest

from enterprise_math.causal_coxeter_shadow import (
    a_has_lower_local_relation_load_than_d,
    a_is_minimum_ade_shadow_at_rank,
    a_shadow_profile,
    causal_h_from_link_degree,
    d_shadow_profile,
    exceptional_shadow_profile,
)
from enterprise_math.causal_root_system_competition import (
    d_roots,
    e8_roots_scaled,
    root_system_local_profile,
)


class CausalCoxeterShadowTests(unittest.TestCase):
    def test_a_and_d_closed_profiles_match_causal_h_formula(self):
        for rank in range(4, 9):
            for profile in (a_shadow_profile(rank), d_shadow_profile(rank)):
                self.assertEqual(
                    causal_h_from_link_degree(profile.direction_link_degree),
                    profile.coxeter_shadow,
                )
                self.assertEqual(
                    profile.edge_common_neighbor_count,
                    profile.direction_link_degree,
                )
                self.assertEqual(
                    profile.edge_common_graph_degree,
                    profile.coxeter_shadow - 3,
                )

    def test_d_n_integer_enumeration_matches_shadow_profile(self):
        for rank in range(4, 8):
            enumerated = root_system_local_profile(d_roots(rank))
            shadow = d_shadow_profile(rank)
            self.assertEqual(enumerated[0], shadow.primitive_direction_count)
            self.assertEqual(enumerated[1], shadow.direction_link_degree)
            self.assertEqual(enumerated[2][0], shadow.edge_common_neighbor_count)
            self.assertEqual(enumerated[2][1], shadow.edge_common_graph_edge_count)
            self.assertEqual(enumerated[2][3], ((shadow.edge_common_graph_degree, shadow.edge_common_neighbor_count),))

    def test_e8_integer_enumeration_recovers_h_thirty(self):
        enumerated = root_system_local_profile(e8_roots_scaled())
        shadow = exceptional_shadow_profile("E8")
        self.assertEqual(shadow.coxeter_shadow, 30)
        self.assertEqual(enumerated[0], 240)
        self.assertEqual(enumerated[1], 56)
        self.assertEqual(causal_h_from_link_degree(enumerated[1]), 30)
        self.assertEqual(enumerated[2][1], 756)
        self.assertEqual(shadow.edge_common_graph_edge_count, 756)

    def test_a_has_lower_local_relation_load_than_d_from_rank_four_upward(self):
        for rank in range(4, 13):
            self.assertTrue(a_has_lower_local_relation_load_than_d(rank))

    def test_a_is_minimum_among_ade_shadow_candidates_at_exceptional_ranks(self):
        for rank in (6, 7, 8):
            self.assertTrue(a_is_minimum_ade_shadow_at_rank(rank))


if __name__ == "__main__":
    unittest.main()
