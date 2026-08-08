import unittest

from enterprise_math.adaptive_precision import conflict_multiplicity
from enterprise_math.factor_precision import (
    factor_witness_state,
    first_factor_shell,
    square_basin,
)
from enterprise_math.legendre import is_prime, primes_up_to
from enterprise_math.p017_precision_horizon import (
    cutoff_is_survivor_prime_complete,
    factor_state_primality_conflicts,
    factor_witness_bit,
    high_factor_shell_semiprimes,
    least_witness_compatibility,
    least_witness_refines_full_projection,
    least_witness_state,
    root_observation_is_primality_inert,
    survivor_prime_horizon,
    survivor_prime_horizon_data,
    witness_bit_chain_is_compatible,
)
from enterprise_math.precision_system import ambiguity_multiplicity


class P017PrecisionHorizonTests(unittest.TestCase):
    def test_least_witness_projection_is_compatible(self):
        for n in range(2, 250):
            for low in range(0, 14):
                for high in range(low, 14):
                    self.assertTrue(least_witness_compatibility(n, low, high))

    def test_full_factor_state_refines_least_witness(self):
        for k in range(2, 35):
            for cutoff in range(0, k + 1):
                self.assertTrue(least_witness_refines_full_projection(k, cutoff))

    def test_full_least_and_bit_have_identical_primality_conflict(self):
        for k in range(2, 35):
            for cutoff in range(0, k + 1):
                for n in square_basin(k):
                    data = factor_state_primality_conflicts(k, n, cutoff)
                    self.assertEqual(data["full"], data["least"])
                    self.assertEqual(data["least"], data["bit"])

    def test_extra_factor_identity_can_reduce_ambiguity_without_proof_gain(self):
        k = 5
        cutoff = 3
        n = 30
        states = list(square_basin(k))
        full = lambda state: factor_witness_state(state, cutoff)
        least = lambda state: least_witness_state(state, cutoff)
        bit = lambda state: factor_witness_bit(state, cutoff)

        full_ambiguity = ambiguity_multiplicity(states, full, n)
        least_ambiguity = ambiguity_multiplicity(states, least, n)
        bit_ambiguity = ambiguity_multiplicity(states, bit, n)
        self.assertLess(full_ambiguity, least_ambiguity)
        self.assertLessEqual(least_ambiguity, bit_ambiguity)

        predicate = is_prime
        self.assertEqual(conflict_multiplicity(states, full, predicate, n), 0)
        self.assertEqual(conflict_multiplicity(states, least, predicate, n), 0)
        self.assertEqual(conflict_multiplicity(states, bit, predicate, n), 0)

    def test_one_bit_factor_state_need_not_form_a_refinement_chain(self):
        # At cutoff 3, both 2 and 3 report "some factor visible".  At cutoff 2,
        # they differ, so the high-cutoff bit cannot project deterministically to
        # the low-cutoff bit.
        self.assertFalse(witness_bit_chain_is_compatible([2, 3], 2, 3))

    def test_survivor_prime_horizon_is_minimal_and_bounded_by_k(self):
        for k in range(1, 150):
            data = survivor_prime_horizon_data(k)
            horizon = data["horizon"]
            self.assertLessEqual(horizon, k)
            self.assertEqual(data["slack"], k - horizon)
            for cutoff in range(0, k + 1):
                self.assertEqual(
                    cutoff_is_survivor_prime_complete(k, cutoff),
                    cutoff >= horizon,
                )

    def test_horizon_is_last_nonempty_first_factor_shell(self):
        for k in range(2, 100):
            horizon = survivor_prime_horizon(k)
            nonempty = [p for p in primes_up_to(k) if first_factor_shell(k, p)]
            self.assertEqual(horizon, max(nonempty, default=0))

    def test_high_factor_shells_are_semiprime(self):
        saw_nonempty = False
        for k in range(3, 120):
            upper = (k + 1) * (k + 1) - 1
            threshold = 0
            while (threshold + 1) ** 3 <= upper:
                threshold += 1
            for p in primes_up_to(k):
                if p <= threshold:
                    continue
                data = high_factor_shell_semiprimes(k, p)
                if data:
                    saw_nonempty = True
                for n, q in data:
                    self.assertEqual(n, p * q)
                    self.assertTrue(is_prime(q))
                    self.assertGreater(q, p)
        self.assertTrue(saw_nonempty)

    def test_root_observation_is_constant_inside_square_basin(self):
        for k in range(1, 100):
            self.assertTrue(root_observation_is_primality_inert(k))


if __name__ == "__main__":
    unittest.main()
