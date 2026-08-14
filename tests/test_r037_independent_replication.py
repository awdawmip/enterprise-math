import unittest
from fractions import Fraction

from research.r037_independent_replication import (
    bfs, fcc_neighbors, hcp_neighbors, fcc_distance, hcp_distance,
    fcc_A, fcc_V, hcp_A, hcp_V, exposed_faces, shell_edge_count,
    outside_edge_count, shell_four_cycles, path_counts, fcc_norm2, hcp_norm2,
    radial_moment, boundary_complex
)

class R037IndependentReplicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fd=bfs(fcc_neighbors,20)
        cls.hd=bfs(hcp_neighbors,20)

    def test_distance_oracles_independent_bfs(self):
        self.assertTrue(all(fcc_distance(v)==d for v,d in self.fd.items()))
        self.assertTrue(all(hcp_distance(v)==d for v,d in self.hd.items()))

    def test_growth_r0_r20_and_holdout_r100(self):
        sf={r:0 for r in range(21)}; sh={r:0 for r in range(21)}
        for d in self.fd.values(): sf[d]+=1
        for d in self.hd.values(): sh[d]+=1
        for r in range(21):
            self.assertEqual(sf[r],fcc_A(r)); self.assertEqual(sh[r],hcp_A(r))
        self.assertEqual((fcc_A(100),fcc_V(100)),(100002,3383701))
        self.assertEqual((hcp_A(100),hcp_V(100)),(105002,3552851))

    def test_first_graph_and_shell_difference(self):
        self.assertEqual(shell_four_cycles(fcc_neighbors),6)
        self.assertEqual(shell_four_cycles(hcp_neighbors),9)
        self.assertEqual((fcc_A(1),hcp_A(1)),(12,12))
        self.assertEqual((fcc_A(2),hcp_A(2)),(42,44))

    def test_shell_edges_and_exposed_faces(self):
        for r in range(1,21):
            self.assertEqual(shell_edge_count(fcc_neighbors,self.fd,r),24*r*r)
            self.assertEqual(shell_edge_count(hcp_neighbors,self.hd,r),27*r*r-(3 if r%2 else 0))
            self.assertEqual(outside_edge_count(fcc_neighbors,self.fd,r),exposed_faces(r))
            self.assertEqual(outside_edge_count(hcp_neighbors,self.hd,r),exposed_faces(r))

    def test_exact_topology_reference_samples(self):
        for kind in ("fcc","hcp"):
            for r in (0,1,2,10,20):
                bc=boundary_complex(kind,r); F=exposed_faces(r)
                self.assertEqual((bc["V"],bc["E"],bc["F"],bc["chi"]),(F+2,2*F,F,2))
                self.assertTrue(bc["connected"]); self.assertTrue(bc["vertex_links_cycles"])
                self.assertEqual(bc["edge_incidence"],{2:2*F})

    def test_finite_path_counts_and_radial_moments(self):
        for n in range(13):
            cf=path_counts(fcc_neighbors,n); ch=path_counts(hcp_neighbors,n)
            self.assertEqual(cf.get((0,0,0),0),ch.get((0,0,0),0))
            target4=Fraction(5*n*n-2*n,3)
            self.assertEqual(radial_moment(cf,fcc_norm2,2,n),target4)
            self.assertEqual(radial_moment(ch,hcp_norm2,2,n),target4)
            target6f=Fraction(n*(35*n*n-42*n+16),9)
            self.assertEqual(radial_moment(cf,fcc_norm2,3,n),target6f)
            if n:
                target6h=Fraction(210*n**3-252*n*n+95*n+1,54)
                self.assertEqual(radial_moment(ch,hcp_norm2,3,n),target6h)
                self.assertEqual(target6h-target6f,-Fraction(n-1,54))
        self.assertEqual((len(path_counts(fcc_neighbors,2)),len(path_counts(hcp_neighbors,2))),(55,57))

if __name__=="__main__":
    unittest.main()
