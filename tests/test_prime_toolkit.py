import unittest

from enterprise_math.centered_prime_radius import slack_centered_radius_equivalence
from enterprise_math.factor_precision import first_factor_shell as owner_first_factor_shell
from enterprise_math.legendre import (
    binary_carry_square_interval_prime_count,
    direct_square_interval_prime_count,
)
from enterprise_math.p017_precision_horizon import (
    least_witness_state,
    survivor_prime_horizon_data,
)
from enterprise_math.p018_p023_power_free_action_basis import (
    minimal_root_quotient_action_basis,
)
from enterprise_math.prime_gap_slack import factor_proof_slack
from enterprise_math.prime_toolkit import (
    bounded_primality,
    bounded_prime_enumeration,
    centered_prime_slack_coordinates,
    first_factor_shell,
    least_factor_witness,
    least_visible_factor,
    list_methods,
    method_record,
    power_free_action_basis,
    proof_factor_horizon,
    square_basin_certificate,
)


REQUIRED_FIELDS = {
    "method_id",
    "source_owner",
    "source_ref",
    "mathematical_status",
    "prior_art_status",
    "inputs",
    "outputs",
    "exactness",
    "preconditions",
    "failure_modes",
    "integer_only",
    "complexity_characteristics",
    "lean_status",
    "current_regression_evidence",
    "reusable_for",
    "not_safe_for",
    "toolization_status",
}


class PrimeToolkitTests(unittest.TestCase):
    def test_inventory_schema_and_status_gate(self):
        methods = list_methods()
        self.assertGreaterEqual(len(methods), 15)
        ids = {record["method_id"] for record in methods}
        self.assertEqual(len(ids), len(methods))
        for record in methods:
            self.assertTrue(REQUIRED_FIELDS <= set(record))
        ready = list_methods("CANONICAL_TOOL_READY")
        self.assertTrue(ready)
        self.assertTrue(
            all(record["toolization_status"] == "CANONICAL_TOOL_READY" for record in ready)
        )
        with self.assertRaises(ValueError):
            list_methods("MADE_UP_STATUS")

    def test_wip_methods_are_discoverable_but_not_promoted(self):
        prime_compiler = method_record("p018_p023.prime_primitive_generator_basis")
        self.assertEqual(
            prime_compiler["toolization_status"], "VALIDATED_WIP_ADAPTER_ONLY"
        )
        self.assertIn("PROVED_WIP", prime_compiler["source_status"])
        r005 = method_record("r005.bounded_prime_oracle")
        self.assertEqual(r005["toolization_status"], "DUPLICATE")

    def test_classical_oracles_keep_classical_status(self):
        self.assertFalse(bounded_primality(1).value)
        prime = bounded_primality(97)
        self.assertTrue(prime.value)
        self.assertIn("CLASSICAL_BASELINE", prime.source_status)
        self.assertEqual(
            bounded_prime_enumeration(20).value,
            [2, 3, 5, 7, 11, 13, 17, 19],
        )
        composite_factor = least_factor_witness(91)
        self.assertEqual(composite_factor.value, 7)
        self.assertIsNone(composite_factor.warning)
        prime_factor = least_factor_witness(97)
        self.assertEqual(prime_factor.value, 97)
        self.assertIsNotNone(prime_factor.warning)

    def test_least_visible_factor_preserves_owner_semantics(self):
        self.assertEqual(least_visible_factor(77, 5).value, least_witness_state(77, 5))
        visible = least_visible_factor(77, 7)
        self.assertEqual(visible.value, 7)
        self.assertIsNone(visible.warning)
        unresolved = least_visible_factor(77, 5)
        self.assertEqual(unresolved.value, 0)
        self.assertIn("not a prime certificate", unresolved.warning)
        prime_self = least_visible_factor(97, 97)
        self.assertEqual(prime_self.value, 97)
        self.assertIn("not a proper-factor/compositeness witness", prime_self.warning)

    def test_first_factor_shell_is_thin_owner_adapter(self):
        for k, prime in ((10, 2), (10, 3), (20, 7)):
            self.assertEqual(
                first_factor_shell(k, prime).value,
                owner_first_factor_shell(k, prime),
            )

    def test_horizon_is_thin_owner_adapter_with_semantic_warning(self):
        for k in (4, 10, 25):
            result = proof_factor_horizon(k)
            self.assertEqual(result.value, survivor_prime_horizon_data(k))
            self.assertIn("not an independent ex-ante bound", result.warning)

    def test_square_basin_certificate_crosschecks_all_owner_counts(self):
        for k in (1, 4, 10):
            result = square_basin_certificate(k)
            self.assertTrue(result.value["verified_equal"])
            self.assertEqual(
                result.value["prime_count"],
                direct_square_interval_prime_count(k),
            )
            self.assertEqual(
                result.value["binary_carry"],
                binary_carry_square_interval_prime_count(k),
            )

    def test_centered_coordinate_adapter_keeps_size_hypothesis(self):
        valid_k = None
        for k in range(4, 200):
            slack = factor_proof_slack(k)
            radius = slack + 1
            left = k + 1 - radius
            if left >= 3 and left > radius * radius:
                valid_k = k
                break
        self.assertIsNotNone(valid_k)
        result = centered_prime_slack_coordinates(valid_k)
        self.assertEqual(result.value, slack_centered_radius_equivalence(valid_k))
        self.assertIn("conditional", result.warning)
        with self.assertRaises(ValueError):
            centered_prime_slack_coordinates(10)

    def test_power_free_basis_does_not_claim_prime_compiler(self):
        result = power_free_action_basis(30, 2)
        self.assertEqual(
            result.value,
            list(minimal_root_quotient_action_basis(30, 2)),
        )
        self.assertIn("one-step", result.warning)
        self.assertIn("Draft #333", result.warning)


if __name__ == "__main__":
    unittest.main()
