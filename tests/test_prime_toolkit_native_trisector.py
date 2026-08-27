import unittest

from enterprise_math.prime_toolkit import (
    coupled_closure_certificate,
    method_record,
    native_trisector_coupled_certificate,
    odd_sector_lane_certificate,
    split_hyperbola_orbit_certificate,
)


class PrimeToolkitNativeTrisectorTests(unittest.TestCase):
    def test_inventory_supplement_is_loaded(self):
        ids = (
            "native_filament.split_hyperbola_orbit_certificate",
            "native_filament.odd_sector_lane_certificate",
            "native_filament.coupled_closure_certificate",
            "native_filament.native_trisector_coupled_certificate",
        )
        for method_id in ids:
            record = method_record(method_id)
            self.assertEqual(record["toolization_status"], "VALIDATED_WIP_ADAPTER_ONLY")
            self.assertIn("CANONICAL_MAIN", record["source_status"])
            self.assertIn("EXECUTABLE_CHECKED", record["source_status"])

    def test_wrappers_preserve_status_and_owner_values(self):
        orbit = split_hyperbola_orbit_certificate(3, 1, 5)
        self.assertEqual(orbit.method_id, "native_filament.split_hyperbola_orbit_certificate")
        self.assertTrue(orbit.value["one_orbit"])
        self.assertIn("does not invent", orbit.warning)

        lane = odd_sector_lane_certificate(3, 7)
        self.assertTrue(lane.value["saturated"])
        self.assertEqual(lane.value["fiber_sizes"], [2, 2, 2])
        self.assertIn("Only s=3", lane.warning)

        closure = coupled_closure_certificate(3, 5)
        self.assertTrue(closure.value["native_admitted_closure"])
        self.assertEqual(closure.value["terminal_odd_prime_factor"], 53)
        self.assertIn("breaker-coprime capacity", closure.warning)

        native = native_trisector_coupled_certificate()
        self.assertEqual(native.value["exact_chain"], [3, [5, 7], 9, 35, 105, 53])
        self.assertFalse(native.value["novelty_claim"])
        self.assertIn("Foundation review completed", native.warning)


if __name__ == "__main__":
    unittest.main()
