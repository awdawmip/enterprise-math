import importlib.util, pathlib, unittest, sys
from fractions import Fraction as F

P=pathlib.Path(__file__).resolve().parents[1]/'experiments'/'r034_fcc_hcp_propagation_sphere.py'
spec=importlib.util.spec_from_file_location('r034_fcc_hcp_propagation_sphere',P)
r=importlib.util.module_from_spec(spec); sys.modules[spec.name]=r; spec.loader.exec_module(r)

class TestR034(unittest.TestCase):
    def test_local_zero_drift_and_covariance(self):
        for world,ps in [('fcc',[0]),('hcp',[0,1])]:
            for parity in ps:
                mean,C,target=r.local_mean_cov(world,parity)
                self.assertEqual(mean,(F(0),F(0),F(0)))
                self.assertEqual(C,target)

    def test_unit_steps(self):
        for steps in (r.fcc_steps_physical(),r.hcp_steps_physical(0),r.hcp_steps_physical(1)):
            m2=r.moment_poly(steps,2)
            one3=r.Q23.q(F(1,3))
            self.assertEqual(m2,{(2,0,0):one3,(0,2,0):one3,(0,0,2):one3})

    def test_first_local_memory_order(self):
        f3=r.moment_poly(r.fcc_steps_physical(),3)
        a3=r.moment_poly(r.hcp_steps_physical(0),3)
        b3=r.moment_poly(r.hcp_steps_physical(1),3)
        self.assertEqual(f3,{})
        self.assertTrue(a3)
        self.assertEqual(a3,{m:-c for m,c in b3.items()})
        self.assertNotEqual(r.moment_poly(r.fcc_steps_physical(),4),r.moment_poly(r.hcp_steps_physical(0),4))

    def test_exact_second_radial_moments(self):
        for n in range(0,9):
            for neigh,r2fn in ((r.fcc_neighbors,r.fcc_r2),(r.hcp_neighbors,r.hcp_r2)):
                c=r.path_counts(neigh,n)
                self.assertEqual(r.radial_moment(c,r2fn,1),r.radial2(n))
                self.assertEqual(r.radial_moment(c,r2fn,2),r.radial4(n))

    def test_radial_sixth_memory(self):
        for n in range(1,7):
            fc=r.path_counts(r.fcc_neighbors,n); hc=r.path_counts(r.hcp_neighbors,n)
            self.assertEqual(r.radial_moment(fc,r.fcc_r2,3),r.radial6_fcc(n))
            self.assertEqual(r.radial_moment(hc,r.hcp_r2,3),r.radial6_hcp(n))
            self.assertEqual(r.radial6_hcp(n)-r.radial6_fcc(n),-F(n-1,54))

    def test_n2_distribution_witness(self):
        f=r.path_counts(r.fcc_neighbors,2); h=r.path_counts(r.hcp_neighbors,2)
        self.assertEqual(len(f),55); self.assertEqual(len(h),57)
        self.assertEqual(r.count_hist(f),{1:12,2:24,4:18,12:1})
        self.assertEqual(r.count_hist(h),{1:18,2:18,3:2,4:18,12:1})

    def test_return_counts_equal_reference_range(self):
        for n in range(0,13):
            self.assertEqual(r.path_counts(r.fcc_neighbors,n).get((0,0,0),0),
                             r.path_counts(r.hcp_neighbors,n).get((0,0,0),0))

if __name__=='__main__': unittest.main()
