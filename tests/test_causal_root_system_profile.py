import unittest

from enterprise_math.causal_root_system_profile import (
    a_profile,
    causal_branching_number,
    d_profile,
    e_profile,
    low_rank_richest_sequence,
    richest_primitive_relation_candidates,
)


class CausalRootSystemProfileTests(unittest.TestCase):
    def test_a3_fcc_local_counts(self):
        profile = a_profile(3)
        self.assertEqual(profile.primitive_directions, 12)
        self.assertEqual(profile.direction_link_degree, 4)
        self.assertEqual(profile.edge_context_vertices, 4)
        self.assertEqual(profile.edge_context_degree, 1)
        self.assertEqual(profile.edge_context_edges, 2)
        self.assertEqual(causal_branching_number(profile), 4)

    def test_d4_local_counts(self):
        profile = d_profile(4)
        self.assertEqual(profile.primitive_directions, 24)
        self.assertEqual(profile.direction_link_degree, 8)
        self.assertEqual(profile.edge_context_vertices, 8)
        self.assertEqual(profile.edge_context_degree, 3)
        self.assertEqual(profile.edge_context_edges, 12)
        self.assertEqual(causal_branching_number(profile), 6)

    def test_exceptional_profiles(self):
        expected = {
            6: (72, 20, 9, 90),
            7: (126, 32, 15, 240),
            8: (240, 56, 27, 756),
        }
        for rank, values in expected.items():
            profile = e_profile(rank)
            self.assertEqual(
                (
                    profile.primitive_directions,
                    profile.direction_link_degree,
                    profile.edge_context_degree,
                    profile.edge_context_edges,
                ),
                values,
            )
            self.assertEqual(causal_branching_number(profile), profile.coxeter_number)

    def test_richest_ADE_sequence_through_rank_eight(self):
        self.assertEqual(
            low_rank_richest_sequence(),
            (
                (2, ("A_2",), 6),
                (3, ("A_3",), 12),
                (4, ("D_4",), 24),
                (5, ("D_5",), 40),
                (6, ("E_6",), 72),
                (7, ("E_7",), 126),
                (8, ("E_8",), 240),
            ),
        )

    def test_relation_richness_is_only_a_first_gate(self):
        winners = richest_primitive_relation_candidates(6)
        self.assertEqual(tuple(profile.family for profile in winners), ("E_6",))
        self.assertGreater(e_profile(6).primitive_directions, d_profile(6).primitive_directions)
        self.assertGreater(d_profile(6).primitive_directions, a_profile(6).primitive_directions)


if __name__ == "__main__":
    unittest.main()
