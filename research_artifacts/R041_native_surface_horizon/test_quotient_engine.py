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

class R041CompactR3Tests(unittest.TestCase):
    def test_r2_determines_b2_on_bounded_atlas(self):
        for world, max_n in [('fcc',4),('hcp',4)]:
            neighbors = q.WORLD[world][0]
            eng = q.SignatureEngine(world)
            for level in q.enumerate_animals(world,max_n).values():
                for C in level:
                    self.assertEqual(q.b2_from_r2(q.reduced_r2(C,neighbors)), eng.operational(C,2))

    def test_m3_reconstructs_every_first_successor_r2_on_bounded_atlas(self):
        for world, max_n in [('fcc',4),('hcp',3)]:
            neighbors = q.WORLD[world][0]
            for level in q.enumerate_animals(world,max_n).values():
                for C in level:
                    Cset=set(C)
                    for x in q.frontier(Cset,neighbors):
                        actual=q.reduced_r2(tuple(sorted(Cset|{x})),neighbors)
                        predicted=q.m3_reconstructed_child_r2(C,x,neighbors)
                        self.assertEqual(predicted,actual)

    def test_m3_matches_recursive_b3_on_regressions(self):
        fcc_ce6_a=((0,0,0),(0,0,2),(0,1,-1),(1,-1,4),(1,0,1),(1,0,3))
        fcc_ce6_b=((0,0,0),(0,0,2),(0,1,-1),(0,1,1),(1,0,3),(1,1,-2))
        for C in [FCC_GAP_A,FCC_EXACT_H_A,fcc_ce6_a,fcc_ce6_b]:
            Cc=q.canonical_fcc(C)
            self.assertEqual(q.b3_from_m3(Cc,q.fcc_neighbors),q.SignatureEngine('fcc').operational(Cc,3))
        for C in [HCP_GAP_A,HCP_EXACT_H_A]:
            Cc=q.canonical_hcp(C)
            self.assertEqual(q.b3_from_m3(Cc,q.hcp_neighbors),q.SignatureEngine('hcp').operational(Cc,3))

    def test_r2_operational_debt_precedes_terminal_debt_fcc_ce6(self):
        A=q.canonical_fcc(((0,0,0),(0,0,2),(0,1,-1),(1,-1,4),(1,0,1),(1,0,3)))
        B=q.canonical_fcc(((0,0,0),(0,0,2),(0,1,-1),(0,1,1),(1,0,3),(1,1,-2)))
        eng=q.SignatureEngine('fcc')
        self.assertEqual(q.reduced_r2(A,q.fcc_neighbors),q.reduced_r2(B,q.fcc_neighbors))
        self.assertEqual(eng.operational(A,2),eng.operational(B,2))
        self.assertEqual(eng.terminal(A,3),eng.terminal(B,3))
        self.assertNotEqual(q.b3_from_m3(A,q.fcc_neighbors),q.b3_from_m3(B,q.fcc_neighbors))


class R041GeneralCompactConeTests(unittest.TestCase):
    @staticmethod
    def _raw_operational(C, h, neighbors):
        cache = {}
        def rec(current, depth):
            key = (current, depth)
            if key in cache:
                return cache[key]
            s = q.surface(current, neighbors)
            if depth == 0:
                ans = (s,)
            else:
                children = set()
                for x in q.frontier(current, neighbors):
                    k = q.attachment_count(current, x, neighbors)
                    children.add((k, rec(frozenset(set(current) | {x}), depth - 1)))
                ans = (s, tuple(sorted(children, key=repr)))
            cache[key] = ans
            return ans
        return rec(frozenset(C), h)

    def test_compact_mh_matches_recursive_operational_h2_h3(self):
        fixtures=[
            ('fcc',FCC_GAP_A),('fcc',FCC_EXACT_H_A),
            ('hcp',HCP_GAP_A),('hcp',HCP_EXACT_H_A),
        ]
        for world,C in fixtures:
            neighbors,canonical=q.WORLD[world]
            Cc=canonical(C)
            eng=q.SignatureEngine(world)
            for h in (2,3):
                self.assertEqual(q.operational_from_compact_mh(Cc,h,neighbors),eng.operational(Cc,h))

    def test_compact_mh_h4_independent_singleton_oracle(self):
        for world in ('fcc','hcp'):
            neighbors,canonical=q.WORLD[world]
            C=canonical(((0,0,0),))
            self.assertEqual(q.operational_from_compact_mh(C,4,neighbors),
                             self._raw_operational(C,4,neighbors))
