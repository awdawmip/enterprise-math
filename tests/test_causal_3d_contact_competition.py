import unittest

from enterprise_math.causal_3d_contact_competition import (
    body_centered_cubic_profile,
    candidates_passing_i1_i2,
    face_centered_cubic_profile,
    hexagonal_close_packed_profile,
    local_candidate_table,
    simple_cubic_profile,
)


class Causal3DContactCompetitionTests(unittest.TestCase):
    def test_sc_and_bcc_have_no_primitive_relations_inside_first_shell(self):
        sc = simple_cubic_profile()
        bcc = body_centered_cubic_profile()
        self.assertEqual(sc.coordination, 6)
        self.assertEqual(sc.direction_link_degree_histogram, ((0, 6),))
        self.assertEqual(sc.direction_link_edge_count, 0)
        self.assertEqual(sc.direction_link_component_sizes, (1, 1, 1, 1, 1, 1))
        self.assertFalse(sc.direction_link_connected)

        self.assertEqual(bcc.coordination, 8)
        self.assertEqual(bcc.direction_link_degree_histogram, ((0, 8),))
        self.assertEqual(bcc.direction_link_edge_count, 0)
        self.assertEqual(bcc.direction_link_component_sizes, (1,) * 8)
        self.assertFalse(bcc.direction_link_connected)

    def test_fcc_and_hcp_share_first_shell_degree_but_not_edge_context_uniformity(self):
        fcc = face_centered_cubic_profile()
        hcp = hexagonal_close_packed_profile()
        for profile in (fcc, hcp):
            self.assertEqual(profile.coordination, 12)
            self.assertEqual(profile.direction_link_degree_histogram, ((4, 12),))
            self.assertEqual(profile.direction_link_edge_count, 24)
            self.assertEqual(profile.direction_link_component_sizes, (12,))
            self.assertTrue(profile.direction_link_connected)

        self.assertTrue(fcc.edge_context_uniform)
        self.assertEqual(len(fcc.bond_context_histogram), 1)
        self.assertFalse(hcp.edge_context_uniform)
        self.assertEqual(len(hcp.bond_context_histogram), 2)

    def test_two_stage_local_candidate_filter_leaves_only_fcc_among_four_models(self):
        self.assertEqual(candidates_passing_i1_i2(), ("FCC",))

    def test_candidate_table_keeps_diagnostics_typed_not_collapsed_to_one_score(self):
        table = local_candidate_table()
        self.assertEqual(set(table), {"SC", "BCC", "FCC", "HCP"})
        self.assertEqual(
            {name: profile.coordination for name, profile in table.items()},
            {"SC": 6, "BCC": 8, "FCC": 12, "HCP": 12},
        )


if __name__ == "__main__":
    unittest.main()
