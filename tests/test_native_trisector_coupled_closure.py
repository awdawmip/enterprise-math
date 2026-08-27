import unittest

from enterprise_math.native_trisector_coupled_closure import (
    coupled_closure_certificate,
    native_trisector_coupled_certificate,
    odd_sector_lane_certificate,
    split_hyperbola_orbit_certificate,
)


class NativeTrisectorCoupledClosureTests(unittest.TestCase):
    def test_split_hyperbola_sign_orbit_counts(self):
        expected = {
            5: 1,
            7: 2,
            13: 4,
            53: 13,
        }
        for q, orbit_count in expected.items():
            cert = split_hyperbola_orbit_certificate(3, 1, q)
            self.assertEqual(cert["point_count"], q - 1)
            self.assertEqual(cert["orbit_count"], orbit_count)
            self.assertEqual(cert["burnside_orbit_count"], orbit_count)
        self.assertTrue(split_hyperbola_orbit_certificate(3, 1, 5)["one_orbit"])
        self.assertFalse(split_hyperbola_orbit_certificate(3, 1, 7)["one_orbit"])

    def test_native_extremal_lane_certificates(self):
        lower = odd_sector_lane_certificate(3, 5)
        upper = odd_sector_lane_certificate(3, 7)
        self.assertTrue(lower["saturated"])
        self.assertTrue(upper["saturated"])
        self.assertEqual(lower["extremal_kind"], "LOWER")
        self.assertEqual(upper["extremal_kind"], "UPPER")
        self.assertEqual(lower["fiber_sizes"], [1, 1, 2])
        self.assertEqual(upper["fiber_sizes"], [2, 2, 2])
        self.assertEqual(lower["image_size"], lower["image_size_formula"])
        self.assertEqual(upper["image_size"], upper["image_size_formula"])

    def test_non_native_extremal_controls_do_not_saturate_in_scan(self):
        observed_lower = []
        observed_upper = []
        for s in range(3, 102, 2):
            q_lower = 2 * s - 1
            q_upper = 2 * s + 1
            try:
                lower = odd_sector_lane_certificate(s, q_lower)
            except ValueError:
                lower = None
            try:
                upper = odd_sector_lane_certificate(s, q_upper)
            except ValueError:
                upper = None
            if lower is not None and lower["saturated"]:
                observed_lower.append((s, q_lower))
            if upper is not None and upper["saturated"]:
                observed_upper.append((s, q_upper))
        self.assertEqual(observed_lower, [(3, 5)])
        self.assertEqual(observed_upper, [(3, 7)])

    def test_coupled_closure_and_bound_guard(self):
        native = coupled_closure_certificate(3, 5)
        self.assertTrue(native["closure_matched"])
        self.assertTrue(native["admitted_unique_solution"])
        self.assertTrue(native["native_admitted_closure"])
        self.assertEqual(native["k_star"], 9)
        self.assertEqual(native["M_k"], 35)
        self.assertEqual(native["s_times_M_k"], 105)
        self.assertEqual(native["local_obstruction"], 106)
        self.assertEqual(native["terminal_odd_prime_factor"], 53)

        outside_bound = coupled_closure_certificate(5, 7)
        self.assertTrue(outside_bound["closure_matched"])
        self.assertFalse(outside_bound["within_admitted_breaker_bound_q_b_le_5"])
        self.assertFalse(outside_bound["admitted_unique_solution"])
        self.assertFalse(outside_bound["native_admitted_closure"])

    def test_one_call_native_certificate_keeps_typed_meanings(self):
        cert = native_trisector_coupled_certificate()
        self.assertEqual(cert["exact_chain"], [3, [5, 7], 9, 35, 105, 53])
        self.assertEqual(cert["theorem_status"], "AUDITED_RESEARCH_THEOREM / DRIVER_ADMITTED")
        self.assertEqual(cert["foundation_status"], "REVIEW_COMPLETED_NOT_ADMITTED")
        self.assertFalse(cert["novelty_claim"])
        meanings = cert["closure"]["typed_native_chain"]
        self.assertIn("not an unrestricted prime-run theorem", meanings["9"])
        self.assertIn("not a global breaker", meanings["53"])

    def test_domain_guards_reject_invalid_inputs(self):
        with self.assertRaises(ValueError):
            split_hyperbola_orbit_certificate(3, 1, 3)
        with self.assertRaises(ValueError):
            split_hyperbola_orbit_certificate(5, 0, 7)
        with self.assertRaises(ValueError):
            odd_sector_lane_certificate(4, 7)
        with self.assertRaises(ValueError):
            odd_sector_lane_certificate(3, 3)
        with self.assertRaises(ValueError):
            coupled_closure_certificate(2, 5)
        with self.assertRaises(ValueError):
            coupled_closure_certificate(3, 9)


if __name__ == "__main__":
    unittest.main()
