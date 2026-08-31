import unittest
from fractions import Fraction

from experiments.r025_multilayer_collapse_atlas import (
    floor_root, bracket, choose_endpoint, run_trajectory, run_all_endpoints,
    exact_probability_distribution, check_brc_interval_funnel,
    p_power_free_kernel, apply_operation,
)


class R025CollapseAtlasTests(unittest.TestCase):
    def test_floor_root_exact_basin(self):
        for p in range(2, 9):
            for n in range(0, 1000):
                k = floor_root(n, p)
                self.assertLessEqual(k ** p, n)
                self.assertLess(n, (k + 1) ** p)

    def test_exact_state_has_single_endpoint(self):
        for p in range(2, 8):
            for k in range(0, 20):
                n = k ** p
                for policy in ("ALWAYS_DOWN", "ALWAYS_UP", "NEAREST", "FARTHEST"):
                    self.assertEqual(choose_endpoint(n, p, policy)[0], n)

    def test_integer_power_basins_have_no_midpoint_tie(self):
        for p in range(2, 10):
            for k in range(0, 100):
                G = (k + 1) ** p - k ** p
                self.assertEqual(G % 2, 1)

    def test_nearest_equals_half_phase_threshold_on_naturals(self):
        for p in range(2, 10):
            for n in range(0, 2000):
                near = choose_endpoint(n, p, "NEAREST")[0]
                half = choose_endpoint(n, p, "PHASE_THRESHOLD", alpha=Fraction(1,2))[0]
                self.assertEqual(near, half)


    def test_near_far_single_step_complement(self):
        for p in range(2, 8):
            for n in range(0, 500):
                k,L,U,G,d,u,exact = bracket(n,p)
                if exact:
                    continue
                near = choose_endpoint(n,p,"NEAREST")[0]
                far = choose_endpoint(n,p,"FARTHEST")[0]
                self.assertEqual(abs(near-n)+abs(far-n), G)
                self.assertEqual(near+far, L+U)

    def test_aligned_precision_freeze(self):
        for p in range(2, 6):
            r = 2 ** p
            for n0 in range(0, 100):
                for policy in ("ALWAYS_DOWN","ALWAYS_UP","NEAREST","FARTHEST"):
                    rows,_ = run_trajectory(n0,[p]*6,[r]*5,policy)
                    self.assertTrue(all(row.exact_power_before_collapse for row in rows[1:]))

    def test_h4_is_really_false(self):
        # p=2, a=2, n=2, ALWAYS_UP: 8 -> 9, but 4*(2 -> 4)=16.
        self.assertEqual(choose_endpoint(8,2,"ALWAYS_UP")[0], 9)
        self.assertEqual(4*choose_endpoint(2,2,"ALWAYS_UP")[0], 16)

    def test_h6_is_really_false(self):
        a,d = p_power_free_kernel(8,2)
        self.assertEqual((a,d),(2,2))
        lhs = Fraction(choose_endpoint(8,2,"ALWAYS_UP")[0], 8)
        rhs = Fraction(choose_endpoint(2,2,"ALWAYS_UP")[0], 2)
        self.assertNotEqual(lhs,rhs)

    def test_unbiased_exact_distribution_martingale_and_variance(self):
        for n0 in range(0, 20):
            for p in range(2, 6):
                for r in range(1, 5):
                    out = exact_probability_distribution(n0,[p]*5,[r]*4,"UNBIASED")
                    self.assertEqual(Fraction(out["mean"]["num"],out["mean"]["den"]), Fraction(n0,1))
                    self.assertEqual(out["variance"], out["expected_conditional_variance_sum"])

    def test_counter_based_prng_is_reproducible(self):
        x1 = [choose_endpoint(123,5,"PRNG_50_50",seed=17,trajectory_id="abc",layer=i) for i in range(20)]
        x2 = [choose_endpoint(123,5,"PRNG_50_50",seed=17,trajectory_id="abc",layer=i) for i in range(20)]
        self.assertEqual(x1,x2)

    def test_brc_funnel_small_attack(self):
        for p in range(2,7):
            for r in range(1,2**p):
                ok,witness = check_brc_interval_funnel(p,r,12,12)
                self.assertTrue(ok,witness)

    def test_brc_binary_explosion_example(self):
        # p=2, r=5 > 4 and r is not a square: after first support, every layer doubles.
        layers=run_all_endpoints(2,[2]*8,[5]*7)
        c0=len(layers[0].support_after)
        self.assertEqual([len(x.support_after) for x in layers],[c0*(2**t) for t in range(8)])
        self.assertTrue(all(x.duplicate_collision_count==0 for x in layers[1:]))

    def test_monotone_operations_preserve_policy_envelope_example(self):
        for op in ("PHYSICAL_ADD_1","INTEGER_SCALE_2"):
            for n0 in range(0,20):
                D=run_trajectory(n0,[3]*4,[2]*3,"ALWAYS_DOWN",operation_id=op)[0]
                U=run_trajectory(n0,[3]*4,[2]*3,"ALWAYS_UP",operation_id=op)[0]
                N=run_trajectory(n0,[3]*4,[2]*3,"NEAREST",operation_id=op)[0]
                F=run_trajectory(n0,[3]*4,[2]*3,"FARTHEST",operation_id=op)[0]
                for t in range(4):
                    self.assertLessEqual(D[t].post_collapse_state,N[t].post_collapse_state)
                    self.assertLessEqual(N[t].post_collapse_state,U[t].post_collapse_state)
                    self.assertLessEqual(D[t].post_collapse_state,F[t].post_collapse_state)
                    self.assertLessEqual(F[t].post_collapse_state,U[t].post_collapse_state)

    def test_scale_microphase_bound(self):
        for p in range(2, 8):
            for a in range(2, 7):
                ap = a ** p
                for n in range(0, 1000):
                    k = floor_root(n, p)
                    j = floor_root(ap * n, p) - a * k
                    self.assertGreaterEqual(j, 0)
                    self.assertLess(j, a)

    def test_phase_threshold_is_antitone_in_alpha(self):
        alphas = [Fraction(0), Fraction(1,4), Fraction(1,2), Fraction(3,4), Fraction(1)]
        for p in range(2, 7):
            for n in range(0, 1000):
                vals = [choose_endpoint(n, p, "PHASE_THRESHOLD", alpha=a)[0] for a in alphas]
                self.assertTrue(all(vals[i] >= vals[i+1] for i in range(len(vals)-1)))

    def test_upper_closure_commutes_for_divisible_exponents_without_lift(self):
        for n in range(0, 1000):
            for p,q in ((2,4),(2,6),(3,6),(2,8),(4,8)):
                pq = choose_endpoint(choose_endpoint(n,p,"ALWAYS_UP")[0],q,"ALWAYS_UP")[0]
                qp = choose_endpoint(choose_endpoint(n,q,"ALWAYS_UP")[0],p,"ALWAYS_UP")[0]
                self.assertEqual(pq, qp)

    def test_sparse_phase_unbiased_probability_variance_formula(self):
        for p in range(3, 10):
            for n in range(2, min(2**p, 100)):
                k,L,U,G,d,u,exact = bracket(n,p)
                self.assertFalse(exact)
                self.assertEqual(k, 1)
                self.assertEqual(G, 2**p - 1)
                self.assertEqual(d, n - 1)
                self.assertEqual(u, 2**p - n)
                mean = Fraction(u,G)*L + Fraction(d,G)*U
                var = Fraction(u,G)*(L-n)**2 + Fraction(d,G)*(U-n)**2
                self.assertEqual(mean, n)
                self.assertEqual(var, (n-1)*(2**p-n))


if __name__ == "__main__":
    unittest.main()
