import unittest

from enterprise_math.causal_continuation_kernel import (
    anonymous_coupling_kernel,
    anonymous_kernel_is_future_sufficient,
    compose_anonymous_when_safe,
    compose_typed_kernel,
    continuation_type_counts_by_coarse,
    induced_single_profile_per_coarse,
    typed_continuation_kernel,
)


class CausalContinuationKernelTests(unittest.TestCase):
    def test_typed_kernel_forgets_identity_but_keeps_future_type(self):
        witness_to_coarse = {"w0": "r", "w1": "r", "w2": "r"}
        witness_to_type = {"w0": "tau_a", "w1": "tau_a", "w2": "tau_b"}
        typed = typed_continuation_kernel(witness_to_coarse, witness_to_type)
        self.assertEqual(typed, {("r", "tau_a"): 2, ("r", "tau_b"): 1})
        self.assertEqual(anonymous_coupling_kernel(typed), {"r": 3})
        self.assertEqual(continuation_type_counts_by_coarse(typed), {"r": 2})
        self.assertFalse(anonymous_kernel_is_future_sufficient(typed))

    def test_same_future_type_does_not_require_witness_identity(self):
        witness_to_coarse = {"w0": "r", "w1": "r", "w2": "r"}
        witness_to_type = {"w0": "tau", "w1": "tau", "w2": "tau"}
        typed = typed_continuation_kernel(witness_to_coarse, witness_to_type)
        profile = {("tau", "z0"): 1, ("tau", "z1"): 2}
        exact = compose_typed_kernel(typed, profile)
        anonymous = compose_anonymous_when_safe(typed, profile)
        self.assertTrue(anonymous_kernel_is_future_sufficient(typed))
        self.assertEqual(exact, {("r", "z0"): 3, ("r", "z1"): 6})
        self.assertEqual(anonymous, exact)
        self.assertEqual(
            induced_single_profile_per_coarse(typed, profile),
            {("r", "z0"): 1, ("r", "z1"): 2},
        )

    def test_equal_anonymous_kappa_can_have_different_future(self):
        # Both systems have kappa(r)=2, but type incidence differs.
        typed_left = {("r", "tau_a"): 2}
        typed_mixed = {("r", "tau_a"): 1, ("r", "tau_b"): 1}
        profile = {("tau_a", "z0"): 1, ("tau_b", "z1"): 1}
        self.assertEqual(anonymous_coupling_kernel(typed_left), {"r": 2})
        self.assertEqual(anonymous_coupling_kernel(typed_mixed), {"r": 2})
        self.assertNotEqual(
            compose_typed_kernel(typed_left, profile),
            compose_typed_kernel(typed_mixed, profile),
        )
        self.assertEqual(compose_typed_kernel(typed_left, profile), {("r", "z0"): 2})
        self.assertEqual(
            compose_typed_kernel(typed_mixed, profile),
            {("r", "z0"): 1, ("r", "z1"): 1},
        )

    def test_full_identity_can_be_strictly_larger_than_minimum_state(self):
        # Four witnesses collapse to two continuation types: identity is unnecessary,
        # but anonymous kappa(r)=4 is too coarse.
        witness_to_coarse = {
            "w0": "r",
            "w1": "r",
            "w2": "r",
            "w3": "r",
        }
        witness_to_type = {
            "w0": "tau_a",
            "w1": "tau_a",
            "w2": "tau_b",
            "w3": "tau_b",
        }
        typed = typed_continuation_kernel(witness_to_coarse, witness_to_type)
        self.assertEqual(len(witness_to_coarse), 4)
        self.assertEqual(len(typed), 2)
        self.assertEqual(anonymous_coupling_kernel(typed), {"r": 4})
        profile = {("tau_a", "z0"): 1, ("tau_b", "z1"): 1}
        self.assertEqual(
            compose_typed_kernel(typed, profile),
            {("r", "z0"): 2, ("r", "z1"): 2},
        )

    def test_multiple_coarse_classes_are_typed_independently(self):
        witness_to_coarse = {"a0": "r0", "a1": "r0", "b0": "r1"}
        witness_to_type = {"a0": "tau_x", "a1": "tau_x", "b0": "tau_y"}
        typed = typed_continuation_kernel(witness_to_coarse, witness_to_type)
        profile = {("tau_x", "z"): 2, ("tau_y", "z"): 5}
        self.assertTrue(anonymous_kernel_is_future_sufficient(typed))
        self.assertEqual(
            compose_anonymous_when_safe(typed, profile),
            {("r0", "z"): 4, ("r1", "z"): 5},
        )


if __name__ == "__main__":
    unittest.main()
