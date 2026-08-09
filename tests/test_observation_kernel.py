import unittest

from enterprise_math.observation_kernel import (
    observation_compatible_on_domain,
    observed_collision_coefficients,
    observed_equal_at,
    observed_first_equal_time,
    observed_kernel_persistent_on_horizon,
    postcomposed_observation_kernel_inclusion,
    quotient_addition_descent_counterexample,
    semiconjugacy_holds_on_domain,
    true_merge_time_dominates_observed_first_equality,
)


def coefficient(coefficients: tuple[int, ...], degree: int) -> int:
    index = degree - 1
    return coefficients[index] if index < len(coefficients) else 0


class ObservationKernelTests(unittest.TestCase):
    def test_fixed_time_postprocessing_only_coarsens_kernel(self) -> None:
        operation = lambda n: 2 * n + 1
        identity = lambda n: n
        quotient2 = lambda n: n // 2
        states = tuple(range(16))
        for step in range(6):
            self.assertTrue(
                postcomposed_observation_kernel_inclusion(
                    operation, identity, quotient2, states, step
                )
            )

    def test_observed_equality_can_split_without_dynamic_closure(self) -> None:
        operation = lambda n: 2 * n
        quotient2 = lambda n: n // 2
        self.assertTrue(observed_equal_at(operation, quotient2, 0, 1, 0))
        self.assertFalse(observed_equal_at(operation, quotient2, 0, 1, 1))
        self.assertFalse(
            observation_compatible_on_domain(operation, quotient2, range(8))
        )
        self.assertFalse(
            observed_kernel_persistent_on_horizon(
                operation, quotient2, range(8), horizon=4
            )
        )

    def test_semiconjugate_coarse_dynamics_is_closed(self) -> None:
        fine = lambda n: n + 2
        quotient2 = lambda n: n // 2
        coarse = lambda q: q + 1
        states = tuple(range(32))
        self.assertTrue(
            semiconjugacy_holds_on_domain(fine, coarse, quotient2, states)
        )
        self.assertTrue(observation_compatible_on_domain(fine, quotient2, states))
        self.assertTrue(
            observed_kernel_persistent_on_horizon(
                fine, quotient2, states, horizon=8
            )
        )

    def test_coarse_observation_can_merge_strictly_earlier_than_true_state(self) -> None:
        fine = lambda n: n + 2
        quotient2 = lambda n: n // 2
        self.assertEqual(
            observed_first_equal_time(fine, quotient2, 0, 1, max_steps=20), 0
        )
        self.assertTrue(
            true_merge_time_dominates_observed_first_equality(
                fine, quotient2, 0, 1, max_steps=20
            )
        )

    def test_observed_collision_spectrum_can_decrease_without_closure(self) -> None:
        fine = lambda n: 2 * n
        quotient2 = lambda n: n // 2
        states = (0, 1)
        at_zero = observed_collision_coefficients(fine, quotient2, states, 0)
        at_one = observed_collision_coefficients(fine, quotient2, states, 1)
        self.assertEqual(coefficient(at_zero, 2), 1)
        self.assertEqual(coefficient(at_one, 2), 0)

    def test_compatible_observed_kernel_is_time_monotone(self) -> None:
        # Q2(max(n-2,0)) = max(Q2(n)-1,0), so the quotient observation
        # admits an autonomous coarse dynamics.
        fine = lambda n: max(n - 2, 0)
        quotient2 = lambda n: n // 2
        coarse = lambda q: max(q - 1, 0)
        states = tuple(range(24))
        self.assertTrue(
            semiconjugacy_holds_on_domain(fine, coarse, quotient2, states)
        )
        self.assertTrue(
            observed_kernel_persistent_on_horizon(
                fine, quotient2, states, horizon=12
            )
        )

    def test_quotient_coordinates_do_not_support_exact_addition_without_detail(self) -> None:
        for radix in range(2, 20):
            first, second = quotient_addition_descent_counterexample(radix)
            self.assertEqual(
                (first[0] // radix, first[1] // radix),
                (second[0] // radix, second[1] // radix),
            )
            self.assertNotEqual(
                (first[0] + first[1]) // radix,
                (second[0] + second[1]) // radix,
            )


if __name__ == "__main__":
    unittest.main()
