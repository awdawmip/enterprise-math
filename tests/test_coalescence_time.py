import unittest

from enterprise_math.coalescence_time import (
    canonical_coalescence_bound,
    finite_saturation_step,
    first_coalescence_time,
    first_fixed_time,
    iterate,
    kernel_pairs_at_step,
    same_eventual_fixed_state,
    stabilization_kernel_pairs,
    stabilized_state,
    ultrametric_inequality_holds,
)


class CoalescenceTimeTests(unittest.TestCase):
    def test_decrement_stabilization_and_bound(self) -> None:
        operation = lambda n: max(n - 1, 0)
        for state in range(0, 60):
            self.assertEqual(first_fixed_time(operation, state), state)
            self.assertEqual(stabilized_state(operation, state), (state, 0))
        for left in range(0, 30):
            for right in range(0, 30):
                tau = first_coalescence_time(operation, left, right)
                bound = canonical_coalescence_bound(operation, left, right)
                self.assertIsNotNone(tau)
                self.assertIsNotNone(bound)
                self.assertLessEqual(tau, bound)

    def test_same_fixed_state_iff_finite_coalescence_for_bucket_map(self) -> None:
        operation = lambda n: n if n % 2 == 0 else n - 1
        for left in range(0, 50):
            for right in range(0, 50):
                same_fixed = same_eventual_fixed_state(operation, left, right)
                tau = first_coalescence_time(operation, left, right, max_steps=5)
                self.assertEqual(same_fixed, tau is not None)
                bound = canonical_coalescence_bound(operation, left, right, max_steps=5)
                self.assertEqual(same_fixed, bound is not None)
                if tau is not None and bound is not None:
                    self.assertLessEqual(tau, bound)

    def test_kernel_chain_is_monotone(self) -> None:
        operation = lambda n: n // 2
        states = range(0, 64)
        previous: set[tuple[int, int]] = set()
        for step in range(0, 8):
            current = kernel_pairs_at_step(operation, states, step)
            self.assertTrue(previous <= current)
            previous = current

    def test_finite_observation_kernel_saturates_at_max_stabilization_step(self) -> None:
        operation = lambda n: n // 2
        states = tuple(range(0, 64))
        saturation = finite_saturation_step(operation, states)
        self.assertEqual(
            kernel_pairs_at_step(operation, states, saturation),
            stabilization_kernel_pairs(operation, states),
        )

    def test_no_uniform_global_bound_on_decrement_map(self) -> None:
        operation = lambda n: max(n - 1, 0)
        for cutoff in [5, 10, 25, 50]:
            states = tuple(range(cutoff + 1))
            self.assertEqual(finite_saturation_step(operation, states), cutoff)

    def test_coalescence_time_is_ultrametric_inside_a_basin(self) -> None:
        operation = lambda n: n // 2
        states = range(0, 40)
        for x in states:
            for y in states:
                for z in states:
                    self.assertTrue(ultrametric_inequality_holds(operation, x, y, z))

    def test_distinct_stabilization_basins_never_coalesce(self) -> None:
        operation = lambda n: n if n % 2 == 0 else n - 1
        self.assertIsNone(first_coalescence_time(operation, 1, 3, max_steps=10))
        self.assertFalse(same_eventual_fixed_state(operation, 1, 3))

    def test_iterate(self) -> None:
        operation = lambda n: max(n - 1, 0)
        self.assertEqual(iterate(operation, 7, 3), 4)
        self.assertEqual(iterate(operation, 7, 9), 0)


if __name__ == "__main__":
    unittest.main()
