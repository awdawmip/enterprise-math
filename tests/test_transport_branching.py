import unittest
from itertools import product

from enterprise_math.contextual_closure import FiniteOperation
from enterprise_math.transport_branching import (
    canonical_transport_codebook,
    compose_disjoint_operations,
    composition_branching_bound,
    contextual_detail_counts,
    decode_transport_token,
    encode_transport_token,
    local_detail_transport_bound,
    operation_is_observation_congruent,
    radix_addition_transport_capacity,
    radix_multiplication_transport_capacity,
    radix_multiplication_worst_cell_outputs,
    transport_bit_cost,
    transport_branching_capacity,
    transport_branching_profile,
)


class TransportBranchingTests(unittest.TestCase):
    def test_capacity_one_exactly_matches_operation_congruence_exhaustive_two_states(self) -> None:
        states = (0, 1)
        for values in product(states, repeat=4):
            operation = FiniteOperation(
                "mu", 2, lambda args, values=values: values[2 * args[0] + args[1]]
            )
            for labels in product((0, 1), repeat=2):
                observation = lambda x, labels=labels: labels[x]
                capacity = transport_branching_capacity(states, operation, observation)
                self.assertEqual(
                    capacity == 1,
                    operation_is_observation_congruent(states, operation, observation),
                )

    def test_canonical_codebook_uses_exact_capacity_and_roundtrips(self) -> None:
        states = (0, 1, 2, 3)
        operation = FiniteOperation(
            "mu", 2, lambda args: (2 * args[0] + args[1]) % 4
        )
        observation = lambda x: x // 2
        codebook = canonical_transport_codebook(states, operation, observation)
        capacity = transport_branching_capacity(states, operation, observation)
        self.assertEqual(max(map(len, codebook.values())), capacity)

        for a, b in product(states, repeat=2):
            coarse_inputs = (observation(a), observation(b))
            coarse_output = observation(operation.apply((a, b)))
            token = encode_transport_token(codebook, coarse_inputs, coarse_output)
            self.assertLess(token, capacity)
            self.assertEqual(
                decode_transport_token(codebook, coarse_inputs, token),
                coarse_output,
            )

    def test_transport_bit_cost_is_exact_fixed_length_integer_cost(self) -> None:
        expected = {
            1: 0,
            2: 1,
            3: 2,
            4: 2,
            5: 3,
            8: 3,
            9: 4,
        }
        for capacity, bits in expected.items():
            self.assertEqual(transport_bit_cost(capacity), bits)

    def test_exhaustive_two_state_disjoint_composition_bound(self) -> None:
        states = (0, 1)
        unary_tables = tuple(product(states, repeat=2))
        binary_tables = tuple(product(states, repeat=4))
        observations = tuple(product((0, 1), repeat=2))

        for outer_values in binary_tables:
            outer = FiniteOperation(
                "outer",
                2,
                lambda args, values=outer_values: values[2 * args[0] + args[1]],
            )
            for first_values in unary_tables:
                first = FiniteOperation(
                    "first", 1, lambda args, values=first_values: values[args[0]]
                )
                for second_values in unary_tables:
                    second = FiniteOperation(
                        "second", 1, lambda args, values=second_values: values[args[0]]
                    )
                    composite = compose_disjoint_operations(outer, (first, second))
                    self.assertEqual(composite.arity, 2)
                    for labels in observations:
                        observation = lambda x, labels=labels: labels[x]
                        actual, bound = composition_branching_bound(
                            states, outer, (first, second), observation
                        )
                        self.assertLessEqual(actual, bound)
                        self.assertEqual(
                            actual,
                            transport_branching_capacity(states, composite, observation),
                        )

    def test_local_transport_never_exceeds_persistent_detail_product(self) -> None:
        states = (0, 1, 2, 3)
        operation = FiniteOperation(
            "mu", 2, lambda args: (2 * args[0] + args[1]) % 4
        )
        observation = lambda x: x // 2
        bounds = local_detail_transport_bound(
            states, (operation,), operation, observation
        )
        counts = contextual_detail_counts(states, (operation,), observation)
        global_detail = max(counts.values())
        capacity = transport_branching_capacity(states, operation, observation)
        self.assertLessEqual(capacity, global_detail ** operation.arity)
        for actual, bound in bounds.values():
            self.assertLessEqual(actual, bound)

    def test_exhaustive_two_state_local_detail_bound(self) -> None:
        states = (0, 1)
        for values in product(states, repeat=4):
            operation = FiniteOperation(
                "mu", 2, lambda args, values=values: values[2 * args[0] + args[1]]
            )
            for labels in product((0, 1), repeat=2):
                observation = lambda x, labels=labels: labels[x]
                for actual, bound in local_detail_transport_bound(
                    states, (operation,), operation, observation
                ).values():
                    self.assertLessEqual(actual, bound)

    def test_radix_addition_has_minimum_binary_transport_token(self) -> None:
        for radix in range(2, 65):
            self.assertEqual(radix_addition_transport_capacity(radix), 2)
            self.assertEqual(transport_bit_cost(2), 1)

    def test_radix_multiplication_saturates_full_residue_pair_bound(self) -> None:
        for radix in range(2, 40):
            outputs = radix_multiplication_worst_cell_outputs(radix)
            self.assertEqual(len(outputs), radix * radix)
            self.assertEqual(
                radix_multiplication_transport_capacity(radix),
                radix * radix,
            )

    def test_multiplication_transport_can_be_far_larger_than_addition(self) -> None:
        for radix in range(3, 25):
            add_capacity = radix_addition_transport_capacity(radix)
            mul_capacity = radix_multiplication_transport_capacity(radix)
            self.assertEqual(add_capacity, 2)
            self.assertEqual(mul_capacity, radix * radix)
            self.assertGreater(mul_capacity, add_capacity)

    def test_profile_capacity_matches_largest_output_fiber(self) -> None:
        states = tuple(range(6))
        operation = FiniteOperation("add", 2, lambda args: (args[0] + args[1]) % 6)
        observation = lambda x: x % 2
        profile = transport_branching_profile(states, operation, observation)
        self.assertEqual(transport_branching_capacity(states, operation, observation), 1)
        self.assertTrue(all(len(outputs) == 1 for outputs in profile.values()))


if __name__ == "__main__":
    unittest.main()
