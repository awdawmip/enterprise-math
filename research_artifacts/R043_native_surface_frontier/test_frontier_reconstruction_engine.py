#!/usr/bin/env python3
import unittest

import frontier_reconstruction_engine as e


class R043FrontierReconstructionTests(unittest.TestCase):
    def test_frozen_small_atlas_counts(self):
        self.assertEqual([len(e.enumerate_animals('fcc', 4)[n]) for n in range(1, 5)], [1, 1, 4, 20])
        self.assertEqual([len(e.enumerate_animals('hcp', 4)[n]) for n in range(1, 5)], [1, 2, 9, 57])

    def test_exact_weighted_graph_checker_and_hcp_action_split(self):
        C = ((0, 0, 0),)
        Ff, wf, af = e.g0_data(C, e.fcc_neighbors)
        Fh, wh, ah = e.g0_data(C, e.hcp_neighbors)
        self.assertTrue(e.weighted_graph_isomorphic(wf, af, wf, af))
        self.assertFalse(e.weighted_graph_isomorphic(wf, af, wh, ah))
        # FCC singleton is rooted-vertex transitive in G0.
        xf = next(iter(Ff))
        yf = next(v for v in Ff if v != xf)
        self.assertTrue(e.weighted_graph_isomorphic(wf, af, wf, af, xf, yf))
        # HCP singleton G0 already distinguishes basal versus interlayer action classes.
        self.assertFalse(e.weighted_graph_isomorphic(wh, ah, wh, ah, (1, 0, 0), (0, 0, 1)))

    def _check_coexposure(self, world, clusters):
        nb, _ = e.WORLD[world]
        for C in clusters:
            carrier = e.coexposure_carrier(C, nb)
            F = carrier[0]
            for x in F:
                Vp, wp, ap = e.successor_g0_from_coexposure(carrier, x)
                D = tuple(sorted(set(C) | {x}))
                Vd, wd, ad = e.g0_data(D, nb)
                self.assertEqual(Vp, Vd)
                self.assertEqual(wp, wd)
                self.assertEqual(ap, ad)

    def test_coexposure_exact_update(self):
        self._check_coexposure('fcc', [
            ((0, 0, 0),),
            ((0, 0, 0), (0, 1, 1)),
            ((0, 0, 0), (0, 1, 1), (1, 0, 1)),
        ])
        self._check_coexposure('hcp', [
            ((0, 0, 0),),
            ((0, 0, 0), (1, 0, 0)),
            ((0, 0, 0), (0, 0, 1)),
        ])

    def test_singleton_coexposure_pruning(self):
        sf = e.coexposure_stats(((0, 0, 0),), e.fcc_neighbors)
        sh = e.coexposure_stats(((0, 0, 0),), e.hcp_neighbors)
        self.assertEqual((sf['L0_vertices'], sf['L1_vertices'], sf['E11_full'], sf['E11_pruned']), (12, 42, 96, 0))
        self.assertEqual((sh['L0_vertices'], sh['L1_vertices'], sh['E11_full'], sh['E11_pruned']), (12, 44, 108, 6))

    def test_hidden_successor_touch_escapes_radius_three(self):
        witnesses = [
            (
                'fcc',
                ((0, 0, 0), (0, 0, 2), (0, 1, -1), (0, 1, 3), (0, 3, -1), (1, 0, 1), (1, 2, -1)),
                (0, 4, 0), (0, 3, 1), (0, 2, 2),
            ),
            (
                'hcp',
                ((0, 0, 0), (0, 1, 0), (0, 1, 1), (1, 0, 3), (1, 1, 2), (1, 1, 4), (2, 0, 2)),
                (1, -1, 0), (1, -1, 1), (2, -1, 2),
            ),
        ]
        for world, C, x, z, y in witnesses:
            nb, _ = e.WORLD[world]
            F, _w, adj = e.g0_data(C, nb)
            self.assertIn(x, F)
            self.assertIn(y, F)
            L1 = set().union(*(set(nb(u)) for u in F)) - set(C) - set(F)
            self.assertIn(z, L1)
            self.assertIn(z, nb(x))
            self.assertIn(y, nb(z))
            self.assertEqual(e.graph_distance(adj, x, y), 4)

    def test_boolean_oracle_smoke(self):
        C = ((0, 0, 0),)
        self.assertNotEqual(e.operational_signature('fcc', C, 3), e.operational_signature('hcp', C, 3))
        self.assertEqual(e.operational_signature('fcc', C, 0), (12,))


if __name__ == '__main__':
    unittest.main(verbosity=2)
