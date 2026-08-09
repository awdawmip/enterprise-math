import unittest

from enterprise_math.causal_coupling_composition import (
    aggregate_continuations,
    anonymous_uniform_composition,
    continuation_profiles_uniform_on_fibers,
)


class CausalCouplingCompositionTests(unittest.TestCase):
    def test_uniform_profiles_make_anonymous_kernel_future_safe(self):
        joint_to_marginal = {
            "j0": "r0",
            "j1": "r0",
            "j2": "r1",
        }
        continuations = {
            "j0": {"c0": 1, "c1": 2},
            "j1": {"c0": 1, "c1": 2},
            "j2": {"c0": 3},
        }
        self.assertTrue(
            continuation_profiles_uniform_on_fibers(joint_to_marginal, continuations)
        )
        exact = aggregate_continuations(joint_to_marginal, continuations)
        anonymous = anonymous_uniform_composition(joint_to_marginal, continuations)
        self.assertEqual(exact, anonymous)
        self.assertEqual(exact[("r0", "c0")], 2)
        self.assertEqual(exact[("r0", "c1")], 4)

    def test_same_parent_kappa_can_hide_different_next_incidence(self):
        joint_to_marginal = {"j0": "r", "j1": "r"}
        left_split = {
            "j0": {"c0": 1},
            "j1": {"c1": 1},
        }
        right_split = {
            "j0": {"c0": 1},
            "j1": {"c0": 1},
        }
        # Both parent summaries have kappa(r)=2, but their continuation results differ.
        self.assertFalse(
            continuation_profiles_uniform_on_fibers(joint_to_marginal, left_split)
        )
        self.assertTrue(
            continuation_profiles_uniform_on_fibers(joint_to_marginal, right_split)
        )
        self.assertNotEqual(
            aggregate_continuations(joint_to_marginal, left_split),
            aggregate_continuations(joint_to_marginal, right_split),
        )
        with self.assertRaises(ValueError):
            anonymous_uniform_composition(joint_to_marginal, left_split)

    def test_zero_entries_do_not_create_false_nonuniformity(self):
        joint_to_marginal = {"j0": "r", "j1": "r"}
        continuations = {
            "j0": {"c0": 1, "c1": 0},
            "j1": {"c0": 1},
        }
        self.assertTrue(
            continuation_profiles_uniform_on_fibers(joint_to_marginal, continuations)
        )


if __name__ == "__main__":
    unittest.main()
