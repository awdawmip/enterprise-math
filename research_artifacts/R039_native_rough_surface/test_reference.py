import unittest
import reference as r

FCC_S_PAIR = (
    ((0,0,0),(0,1,-1),(1,-1,0)),
    ((0,0,0),(0,1,-1),(0,2,-2)),
)
HCP_S_PAIR = (
    ((0,0,0),(0,0,1),(0,1,1)),
    ((0,0,0),(0,1,0),(0,2,0)),
)
FCC_H_PAIR = (
    ((0,0,0),(0,1,-3),(1,0,-1),(1,1,-2)),
    ((0,0,0),(0,1,-1),(1,-2,1),(1,-1,0)),
)
HCP_H_PAIR = (
    ((0,0,1),(0,1,0),(1,0,2),(1,1,0)),
    ((0,0,0),(0,0,1),(0,1,1),(1,1,2)),
)
FCC_TYPE_PAIR = (
    ((0,0,0),(0,1,-3),(1,0,-1),(1,1,-2)),
    ((0,0,0),(0,1,-1),(1,-1,0),(1,1,-2)),
)
HCP_TYPE_PAIR = (
    ((0,0,1),(0,1,0),(1,0,2),(1,1,0)),
    ((0,0,0),(0,0,1),(0,1,2),(1,1,2)),
)

class R039ReferenceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        r.validate_symmetries()
        cls.levels = {w: r.enumerate_animals(w, 6) for w in ('fcc','hcp')}

    def test_exact_counts_and_minima_through_n6(self):
        for world in ('fcc','hcp'):
            neighbors,_ = r.WORLD[world]
            for n, level in self.levels[world].items():
                row = r.level_row(level, neighbors)
                self.assertEqual(
                    (row['count'],row['S_min'],row['S_max'],row['minimizer_count']),
                    r.EXPECTED[world][n],
                )

    def test_handshake_frontier_sum_addition_and_second_order_update(self):
        for world in ('fcc','hcp'):
            neighbors,_ = r.WORLD[world]
            # exhaustive through N=4 keeps the unit test bounded while checking every branch
            for n in range(1,5):
                for C in self.levels[world][n]:
                    S = r.boundary_size(C, neighbors)
                    self.assertEqual(r.direct_cut_size(C, neighbors), S)
                    H = r.frontier_histogram(C, neighbors)
                    self.assertEqual(r.frontier_weighted_boundary(H), S)
                    Cset=set(C)
                    for x in r.frontier(Cset,neighbors):
                        self.assertEqual(
                            r.boundary_size(Cset|{x},neighbors)-S,
                            r.delta_s_for_addition(Cset,x,neighbors),
                        )
                        pred=r.predict_histogram_after_addition(H,r.second_order_profile(Cset,x,neighbors))
                        self.assertEqual(pred,r.frontier_histogram(Cset|{x},neighbors))

    def test_scalar_S_is_one_step_unsafe_at_n3(self):
        for world,pair in [('fcc',FCC_S_PAIR),('hcp',HCP_S_PAIR)]:
            neighbors,_=r.WORLD[world]
            C,D=pair
            self.assertEqual(r.boundary_size(C,neighbors),32)
            self.assertEqual(r.boundary_size(D,neighbors),32)
            self.assertNotEqual(r.one_step_delta_support(C,neighbors),r.one_step_delta_support(D,neighbors))

    def test_H_is_two_step_unsafe_at_n4(self):
        for world,pair in [('fcc',FCC_H_PAIR),('hcp',HCP_H_PAIR)]:
            neighbors,_=r.WORLD[world]
            C,D=pair
            self.assertEqual(r.boundary_size(C,neighbors),42)
            self.assertEqual(r.boundary_size(D,neighbors),42)
            self.assertEqual(r.frontier_histogram(C,neighbors),r.frontier_histogram(D,neighbors))
            self.assertNotEqual(r.two_step_surface_support(C,neighbors),r.two_step_surface_support(D,neighbors))

    def test_local_type_multiset_loses_correlation_at_n4(self):
        for world,pair in [('fcc',FCC_TYPE_PAIR),('hcp',HCP_TYPE_PAIR)]:
            neighbors,_=r.WORLD[world]
            C,D=pair
            self.assertEqual(r.surface_type_multiset(world,C),r.surface_type_multiset(world,D))
            self.assertNotEqual(r.frontier_histogram(C,neighbors),r.frontier_histogram(D,neighbors))

    def test_fcc_greedy_down_trap_at_n6(self):
        levels=r.greedy_levels('fcc',6)
        neighbors,_=r.WORLD['fcc']
        self.assertEqual({r.boundary_size(C,neighbors) for C in levels[5]}, {44})
        self.assertEqual({r.boundary_size(C,neighbors) for C in levels[6]}, {50})
        self.assertEqual(r.EXPECTED['fcc'][6][1],48)

    def test_hcp_has_two_bond_orbits_at_n2(self):
        level=self.levels['hcp'][2]
        self.assertEqual(len(level),2)
        spectra={r.surface_type_multiset('hcp',C) for C in level}
        self.assertEqual(len(spectra),2)
        self.assertEqual({r.boundary_size(C,r.hcp_neighbors) for C in level},{22})

if __name__ == '__main__':
    unittest.main(verbosity=2)
