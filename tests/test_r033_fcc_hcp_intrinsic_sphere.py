import unittest
from collections import Counter

from experiments.r033_fcc_hcp_intrinsic_sphere import (
    bfs_layers,boundary_complex,boundary_orbit_counts,exposed_faces,
    fcc_A,fcc_V,fcc_distance,fcc_neighbors,fcc_shell_edges,fcc_shell_points,
    hcp_A,hcp_V,hcp_boundary_orbits,hcp_distance,hcp_neighbors,hcp_shell_edges,hcp_shell_points,
)


class R033Tests(unittest.TestCase):
    def test_degree_and_reciprocity(self):
        for p in [(0,0,0),(2,-1,1),(-2,0,0)]:
            if sum(p)%2==0:
                ns=fcc_neighbors(p); self.assertEqual(len(ns),12)
                self.assertTrue(all(p in fcc_neighbors(q) for q in ns))
        for p in [(0,0,0),(0,0,1),(2,-3,4),(-2,1,-3)]:
            ns=hcp_neighbors(p); self.assertEqual(len(ns),12)
            self.assertTrue(all(p in hcp_neighbors(q) for q in ns))

    def test_bfs_distance_and_growth_to_20(self):
        for neighbors,dist,A,V in [
            (fcc_neighbors,fcc_distance,fcc_A,fcc_V),
            (hcp_neighbors,hcp_distance,hcp_A,hcp_V),
        ]:
            layers=bfs_layers(neighbors,20); ball=set()
            for r,shell in enumerate(layers):
                ball |= shell
                self.assertEqual(len(shell),A(r)); self.assertEqual(len(ball),V(r))
                self.assertTrue(all(dist(p)==r for p in shell))

    def test_boundary_edges_and_symmetry_orbits(self):
        for world,neighbors,edge_formula in [
            ('fcc',fcc_neighbors,fcc_shell_edges),('hcp',hcp_neighbors,hcp_shell_edges)]:
            layers=bfs_layers(neighbors,12); ball=set()
            for r,shell in enumerate(layers):
                ball |= shell
                if r==0: continue
                induced=sum(sum(q in shell for q in neighbors(p)) for p in shell)//2
                outside=sum(sum(q not in ball for q in neighbors(p)) for p in shell)
                self.assertEqual(induced,edge_formula(r)); self.assertEqual(outside,exposed_faces(r))
                obs=boundary_orbit_counts(world,shell,ball)
                if world=='fcc':
                    expected=Counter({k:v for k,v in {
                        885:12,341:24*(r-1),85:6*(r-1)**2,273:4*(r-1)*(r-2)}.items() if v})
                    self.assertEqual(obs,expected)
                elif r>=4:
                    name_to_mask={'H69_out3':69,'H228_out4':228,'H229_out5':229,'H448_out3':448,
                                  'H453_out5':453,'H458_out5':458,'H469_out6':469,'H581_out4':581,
                                  'H1764_out6':1764,'H1765_out7':1765}
                    expected=Counter({name_to_mask[k]:v for k,v in hcp_boundary_orbits(r).items() if v})
                    self.assertEqual(obs,expected)

    def test_r100_holdout(self):
        for world,gen,dist,A,neighbors in [
            ('fcc',fcc_shell_points,fcc_distance,fcc_A,fcc_neighbors),
            ('hcp',hcp_shell_points,hcp_distance,hcp_A,hcp_neighbors),
        ]:
            shell=gen(100); self.assertEqual(len(shell),A(100))
            induced=sum(sum(dist(q)==100 for q in neighbors(p)) for p in shell)//2
            outside=sum(sum(dist(q)>100 for q in neighbors(p)) for p in shell)
            self.assertEqual(induced,240000 if world=='fcc' else 270000)
            self.assertEqual(outside,363612)

    def test_exposed_face_complex_is_closed_sphere_reference(self):
        for world,neighbors in [('fcc',fcc_neighbors),('hcp',hcp_neighbors)]:
            layers=bfs_layers(neighbors,8); ball=set()
            for r,shell in enumerate(layers):
                ball |= shell
                t=boundary_complex(world,ball); F=exposed_faces(r)
                self.assertEqual((t['V'],t['E'],t['F']),(F+2,2*F,F))
                self.assertEqual(t['chi'],2); self.assertEqual(t['components'],1)
                self.assertEqual(t['bad_edge_incidence'],0); self.assertEqual(t['bad_vertex_links'],0)

    def test_r1_rooted_graphs_are_already_distinct(self):
        def trace4(neighbors):
            shell=sorted(bfs_layers(neighbors,1)[1])
            A=[[int(q in neighbors(p)) for q in shell] for p in shell]
            def mm(X,Y):
                n=len(X)
                return [[sum(X[i][k]*Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
            A2=mm(A,A); A4=mm(A2,A2)
            return sum(A4[i][i] for i in range(len(A)))
        self.assertEqual(trace4(fcc_neighbors),384)
        self.assertEqual(trace4(hcp_neighbors),408)


if __name__=='__main__':
    unittest.main()
