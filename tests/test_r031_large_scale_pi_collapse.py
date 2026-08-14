import pathlib
import sys
import unittest
from fractions import Fraction

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "experiments"))
import r031_large_scale_pi_collapse as r


class R031Tests(unittest.TestCase):
    def test_pi_36_reference_coordinate(self):
        self.assertEqual(
            r.pi_floor(36),
            3141592653589793238462643383279502884,
        )

    def test_exact_floor_root_bracket(self):
        n = r.pi_floor(36)
        for p in r.P_LIST:
            k,L,U,G = r.local_gap(n,p)
            self.assertLessEqual(L,n)
            self.assertLess(n,U)
            self.assertEqual(U-L,G)
            self.assertEqual(L,k**p)
            self.assertEqual(U,(k+1)**p)

    def test_frozen_d36_binary64_and_square_gap(self):
        n=r.pi_floor(36)
        m=r.binary64_integer_cell(n)
        self.assertEqual(m["exponent"],121)
        self.assertEqual(m["ulp"],Fraction(590295810358705651712,1))
        self.assertEqual(m["phase"],Fraction(80551212002059080073,147573952589676412928))
        self.assertEqual(m["nearest_direction"],"UP")
        _,_,_,g2=r.local_gap(n,2)
        _,_,_,g3=r.local_gap(n,3)
        self.assertEqual(g2,3544907701811032055)
        self.assertEqual(g3,6435088191332872375248847)
        self.assertGreater(m["ulp"]/g2,1)
        self.assertLess(m["ulp"]/g3,1)
        cov=r.basin_coverage(int(m["lower"]),int(m["upper"]),2)
        self.assertEqual(cov,{"touched":167,"full":165,"partial":2})

    def test_crossover_binades(self):
        c2=r.crossover_binades(2)
        c3=r.crossover_binades(3)
        self.assertEqual(c2["onset"]["e"],107)
        self.assertEqual(c2["permanent"]["e"],107)
        self.assertEqual(c3["onset"]["e"],161)
        self.assertEqual(c3["permanent"]["e"],163)
        self.assertEqual(r.find_pi_decade_crossover(2,107)["first_decade"],32)
        self.assertEqual(r.find_pi_decade_crossover(3,161)["first_decade"],48)

    def test_policy_fixed_points_and_lossless_carrier(self):
        n=12321 # 111^2
        for pol in r.POLICIES:
            v,meta=r.choose_endpoint(n,2,pol,scale_context=10**6)
            if pol=="ALL_ENDPOINTS": self.assertEqual(v,{n})
            else: self.assertEqual(v,n)
            self.assertTrue(meta["exact"])
        n=12322
        v,meta=r.choose_endpoint(n,2,"ANCHOR_PLUS_RESIDUAL",scale_context=10**6)
        self.assertEqual(v,n)
        self.assertEqual(meta["carrier"]["anchor"]+meta["carrier"]["residual"],n)

    def test_stochastic_sampler_reproducible(self):
        args=dict(seed=7,trajectory_id="T",layer_id="L",scale_context=10**12)
        a=r.choose_endpoint(314159265358,2,"DISTANCE_WEIGHTED_STOCHASTIC",**args)
        b=r.choose_endpoint(314159265358,2,"DISTANCE_WEIGHTED_STOCHASTIC",**args)
        self.assertEqual(a,b)

    def test_direction_order_reverses_across_algorithm_future(self):
        D=36; ref=r.pi_floor(D)
        gd=r.gauss_legendre_fixed(D,2,"DOWN","iteration_boundary",max_iter=9)["pi_fp"]
        gu=r.gauss_legendre_fixed(D,2,"UP","iteration_boundary",max_iter=9)["pi_fp"]
        cd=r.chudnovsky_fixed(D,2,"DOWN","iteration_boundary")["pi_fp"]
        cu=r.chudnovsky_fixed(D,2,"UP","iteration_boundary")["pi_fp"]
        self.assertLess(gd,gu)
        self.assertLess(gd,ref); self.assertGreater(gu,ref)
        # Collapse acts on a denominator-like partial sum in this Chudnovsky channel.
        self.assertGreater(cd,cu)
        self.assertGreater(cd,ref); self.assertLess(cu,ref)

    def test_all_endpoints_recoalescence(self):
        g=r.gauss_legendre_all_endpoints(36,2,8)
        self.assertEqual(g["state_count"],172)
        self.assertEqual(g["pi_count"],129)
        self.assertEqual(g["observable_recoalescence"],43)
        self.assertLess(int(g["pi_min"]),int(g["pi_max"]))

    def test_residual_only_is_valid_zero_attractor(self):
        run=r.gauss_legendre_fixed(36,2,"RESIDUAL_ONLY","iteration_boundary",max_iter=100,long_horizon=True)
        self.assertEqual(run["status"],"OK")
        self.assertEqual(run["pi_fp"],0)
        self.assertEqual(run["cycle"]["length"],1)

    def test_naive_phase_scale_covariance_counterexample(self):
        # p=2, n=2 has basin [1,4], phi=1/3. Scaling by q^p=4 gives n'=8,
        # basin [4,9], phi'=4/5; phase is not invariant.
        b=r.bracket(2,2); c=r.bracket(8,2)
        self.assertEqual(b.phase,Fraction(1,3))
        self.assertEqual(c.phase,Fraction(4,5))
        self.assertNotEqual(b.phase,c.phase)

    def test_p2_down_equal_anchor_ladder_local_step(self):
        S=10**6
        k=920
        a=k*k
        x=r.p2_down_equal_anchor_next(a,S)
        self.assertFalse(x["divisible"])
        self.assertEqual(x["raw_sqrt"],a-1)
        self.assertEqual(x["down"],(k-1)**2)

    def test_formula_channel_residual_is_small_stable_coordinate(self):
        x=r.formula_record(36,2,"RESIDUAL_ONLY",0)
        # Residual-only does not reconstruct pi, but formula outputs remain finite
        # and concentrate near the zero effective-pi attractor.
        c=x["channels"]["circumference"][0]
        cf=Fraction(int(c["num"]),int(c["den"]))
        self.assertLess(abs(cf),Fraction(1,10**30))


if __name__ == "__main__":
    unittest.main(verbosity=2)
