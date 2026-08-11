import itertools
import math
import unittest

from enterprise_math.prime_toolkit import (
    PrimeToolResult,
    actual_sieve_transient_quotient,
    finite_horizon_sieve_quotient,
    list_methods,
    method_record,
)
from enterprise_math import r005a_sieve_quotients as sieve


def periodicity_oracle(primes, language):
    q = math.prod(primes)
    pmax = max(primes)
    last = -1
    for n in range(pmax * pmax + q + 1):
        left = sieve._observation(n, primes, language, "actual")
        right = sieve._observation(n + q, primes, language, "actual")
        if left != right:
            last = n
    return last + 1


class R005ASieveIngestTests(unittest.TestCase):
    def test_transient_formulas_exhaustively(self):
        base = (2, 3, 5, 7, 11)
        for size in range(1, len(base) + 1):
            for primes in itertools.combinations(base, size):
                self.assertEqual(
                    sieve.relation_preperiod(primes),
                    periodicity_oracle(primes, "relation_resolved"),
                )
                self.assertEqual(
                    sieve.union_preperiod(primes),
                    periodicity_oracle(primes, "union_support"),
                )

    def test_prime_prefix_union_formula_and_facade_status(self):
        prefixes = ((2,), (2, 3), (2, 3, 5), (2, 3, 5, 7), (2, 3, 5, 7, 11))
        for primes in prefixes:
            self.assertEqual(sieve.union_preperiod(primes), max(primes) + 1)
        result = actual_sieve_transient_quotient((2, 3, 5, 7))
        self.assertIsInstance(result, PrimeToolResult)
        self.assertEqual(result.method_id, "r005a.actual_sieve_transient_quotient")
        self.assertEqual(result.toolization_status, "CANONICAL_TOOL_READY")
        self.assertIn("ENTERPRISE_SPECIALIZATION", result.mathematical_status)
        self.assertIn("ENTERPRISE_SPECIALIZATION", result.warning)
        self.assertTrue(result.value["prime_prefix"])
        self.assertEqual(result.value["union_support"]["preperiod"], 8)
        self.assertEqual(result.value["relation_resolved"]["preperiod"], 43)

    def test_single_prime_finite_horizon_formula(self):
        for p in (2, 3, 5, 7, 11):
            primes = (p,)
            for horizon in range(p * p + 2):
                self.assertEqual(
                    sieve.finite_horizon_class_count(
                        primes, "relation_resolved", "actual", horizon
                    ),
                    min(horizon + 2, p * p + 1),
                )
            self.assertEqual(
                sieve.stabilization_horizon(primes, "relation_resolved", "actual"),
                p * p - 1,
            )

    def test_relation_steady_recovery(self):
        for primes in ((2,), (2, 3), (2, 3, 5), (2, 3, 5, 7), (2, 3, 5, 7, 11)):
            self.assertEqual(
                sieve.stabilization_horizon(primes, "relation_resolved", "steady"),
                max(primes) - 2,
            )
        result = finite_horizon_sieve_quotient(
            (2, 3, 5, 7), 5, language="relation_resolved", activation="steady"
        )
        self.assertIsInstance(result, PrimeToolResult)
        self.assertEqual(result.method_id, "r005a.finite_horizon_sieve_quotient")
        self.assertEqual(result.value["stabilization_horizon"], 5)
        self.assertEqual(result.value["relation_steady_recovery_formula"], 5)
        self.assertTrue(result.value["is_full_quotient"])
        self.assertIn("ENTERPRISE_SPECIALIZATION", result.warning)

    def test_partition_refinement_equals_direct_windows(self):
        primes = (2, 3, 5, 7)
        for activation in ("actual", "steady"):
            for language in ("relation_resolved", "union_support"):
                for horizon in range(0, 41):
                    self.assertEqual(
                        sieve.finite_horizon_class_count(
                            primes, language, activation, horizon
                        ),
                        sieve.direct_window_class_count(
                            primes, language, activation, horizon
                        ),
                    )

    def test_segment_horizon_equality(self):
        primes = (2, 3, 5, 7)
        for language in ("relation_resolved", "union_support"):
            for activation in ("actual", "steady"):
                for block in (1, 2, 4, 8, 16):
                    for transitions in range(5):
                        horizon = (transitions + 1) * block - 1
                        self.assertEqual(
                            sieve.segment_class_count(
                                primes, language, activation, block, transitions
                            ),
                            sieve.finite_horizon_class_count(
                                primes, language, activation, horizon
                            ),
                        )
        result = finite_horizon_sieve_quotient(
            primes,
            8,
            language="relation_resolved",
            activation="steady",
            segment_length=4,
            transitions=2,
        )
        h_star = result.value["stabilization_horizon"]
        self.assertEqual(
            result.value["segment"]["transition_depth_to_full"],
            math.ceil((h_star + 1) / 4) - 1,
        )
        self.assertEqual(result.value["segment"]["equivalent_horizon"], 11)
        self.assertEqual(
            result.value["segment"]["class_count"],
            sieve.finite_horizon_class_count(
                primes, "relation_resolved", "steady", 11
            ),
        )

    def test_registry_keeps_rho_wip_and_non_callable(self):
        ids = {record["method_id"] for record in list_methods()}
        self.assertIn("r005a.actual_sieve_transient_quotient", ids)
        self.assertIn("r005a.finite_horizon_sieve_quotient", ids)
        self.assertIn("r005a.prime_wheel_phase_separation_radius", ids)
        rho = method_record("r005a.prime_wheel_phase_separation_radius")
        self.assertEqual(rho["toolization_status"], "VALIDATED_WIP_ADAPTER_ONLY")
        self.assertIn("NOVELTY_UNVERIFIED", rho["mathematical_status"])
        self.assertNotIn("toolkit_callable", rho)

    def test_validation_and_state_limit_fail_closed(self):
        with self.assertRaises(ValueError):
            actual_sieve_transient_quotient((2, 2, 3))
        with self.assertRaises(ValueError):
            actual_sieve_transient_quotient((2, 9))
        with self.assertRaises(ValueError):
            finite_horizon_sieve_quotient((2, 3, 5, 7), 2, state_limit=10)


if __name__ == "__main__":
    unittest.main()
