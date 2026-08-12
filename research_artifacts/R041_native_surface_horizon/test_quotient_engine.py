import unittest
import quotient_engine as q

FCC_EXACT_H_A = ((0,0,0),(0,1,-3),(1,0,-1),(1,1,-2))
FCC_EXACT_H_B = ((0,0,0),(0,1,-1),(1,-1,0),(2,-1,1))
FCC_GAP_A = ((0,0,0),(0,1,-1),(1,-1,0))
FCC_GAP_B = ((0,0,0),(0,0,2),(0,1,1))
HCP_GAP_A = ((0,0,0),(0,1,0))
HCP_GAP_B = ((0,0,0),(0,0,1))
HCP_EXACT_H_A = ((0,0,0),(0,0,1),(0,1,0),(1,1,0))
HCP_EXACT_H_B = ((0,0,0),(0,0,1),(0,0,2),(0,1,0))

class R041CheckpointTests(unittest.TestCase):
    def test_fcc_exact_h_not_nested(self):
        self.assertEqual(q.surface(FCC_EXACT_H_A, q.fcc_neighbors), 42)
        self.assertEqual(q.surface(FCC_EXACT_H_B, q.fcc_neighbors), 42)
        self.assertEqual(q.terminal_support(FCC_EXACT_H_A, 3, q.fcc_neighbors),
                         q.terminal_support(FCC_EXACT_H_B, 3, q.fcc_neighbors))
        self.assertEqual(q.terminal_support(FCC_EXACT_H_A, 3, q.fcc_neighbors),
                         (58,60,62,64,66,68,70,72))
        self.assertEqual(q.terminal_support(FCC_EXACT_H_A, 2, q.fcc_neighbors),
                         (52,54,56,58,60,62))
        self.assertEqual(q.terminal_support(FCC_EXACT_H_B, 2, q.fcc_neighbors),
                         (54,56,58,60,62))

    def test_hcp_exact_h_not_nested(self):
        self.assertEqual(q.surface(HCP_EXACT_H_A, q.hcp_neighbors), 40)
        self.assertEqual(q.surface(HCP_EXACT_H_B, q.hcp_neighbors), 40)
        self.assertEqual(q.terminal_support(HCP_EXACT_H_A, 2, q.hcp_neighbors),
                         q.terminal_support(HCP_EXACT_H_B, 2, q.hcp_neighbors))
        self.assertEqual(q.terminal_support(HCP_EXACT_H_A, 1, q.hcp_neighbors), (44,46,48,50))
        self.assertEqual(q.terminal_support(HCP_EXACT_H_B, 1, q.hcp_neighbors), (46,48,50))

    def test_fcc_terminal_operational_gap(self):
        eng = q.SignatureEngine('fcc')
        A, B = q.canonical_fcc(FCC_GAP_A), q.canonical_fcc(FCC_GAP_B)
        self.assertEqual(eng.terminal(A, 2), eng.terminal(B, 2))
        self.assertEqual(eng.terminal(A, 2), (44,46,48,50,52))
        self.assertNotEqual(eng.operational(A, 2), eng.operational(B, 2))

    def test_hcp_terminal_operational_gap(self):
        eng = q.SignatureEngine('hcp')
        A, B = q.canonical_hcp(HCP_GAP_A), q.canonical_hcp(HCP_GAP_B)
        self.assertEqual(q.surface(A, q.hcp_neighbors), q.surface(B, q.hcp_neighbors))
        self.assertEqual(q.histogram(A, q.hcp_neighbors), q.histogram(B, q.hcp_neighbors))
        self.assertEqual(eng.terminal(A, 2), eng.terminal(B, 2))
        self.assertEqual(eng.terminal(A, 2), (36,38,40,42))
        self.assertNotEqual(eng.operational(A, 2), eng.operational(B, 2))

    def test_activation_pruned_cone_matches_direct_trajectories(self):
        fixtures = [
            ('fcc', FCC_GAP_A), ('fcc', FCC_EXACT_H_A),
            ('hcp', HCP_GAP_A), ('hcp', HCP_EXACT_H_A),
        ]
        for world, C in fixtures:
            neighbors = q.WORLD[world][0]
            for h in (1,2,3):
                self.assertEqual(q.carrier_trajectory_support(C,h,neighbors),
                                 q.direct_trajectory_support(C,h,neighbors))

    def test_singleton_cone_edge_reductions(self):
        fcc = [q.cone_stats(((0,0,0),),h,q.fcc_neighbors) for h in (1,2,3,4)]
        hcp = [q.cone_stats(((0,0,0),),h,q.hcp_neighbors) for h in (1,2,3,4)]
        self.assertEqual([(x['j_edges'],x['k_edges']) for x in fcc],
                         [(24,0),(204,108),(648,432),(1476,1092)])
        self.assertEqual([(x['j_edges'],x['k_edges']) for x in hcp],
                         [(24,0),(216,108),(684,444),(1560,1128)])

    def test_contact_score_factorization(self):
        for neighbors, C in [(q.fcc_neighbors,FCC_GAP_A),(q.hcp_neighbors,HCP_GAP_A)]:
            for h in (1,2,3):
                omega = q.contact_score_spectrum(C,h,neighbors)
                S0 = q.surface(C,neighbors)
                via_omega = tuple(sorted(S0+12*h-2*w for w in omega))
                self.assertEqual(via_omega, q.terminal_support(C,h,neighbors))

if __name__ == '__main__':
    unittest.main(verbosity=2)
