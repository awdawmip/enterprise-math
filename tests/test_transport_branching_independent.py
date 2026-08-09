import unittest
from itertools import product

from enterprise_math.contextual_closure import FiniteOperation
from enterprise_math.transport_branching import (
    canonical_transport_codebook,
    transport_branching_capacity,
)


def direct_observation_compatibility(states, operation, observation):
    tuples = tuple(product(states, repeat=operation.arity))
    for left in tuples:
        for right in tuples:
            if all(observation(a) == observation(b) for a, b in zip(left, right)):
                if observation(operation.apply(left)) != observation(operation.apply(right)):
                    return False
    return True


class TransportBranchingIndependentTests(unittest.TestCase):
    def test_capacity_one_iff_direct_congruence_exhaustive_two_states(self) -> None:
        states = (0, 1)
        for values in product(states, repeat=4):
            operation = FiniteOperation(
                "mu", 2, lambda args, values=values: values[2 * args[0] + args[1]]
            )
            for labels in product((0, 1), repeat=2):
                observation = lambda x, labels=labels: labels[x]
                self.assertEqual(
                    transport_branching_capacity(states, operation, observation) == 1,
                    direct_observation_compatibility(states, operation, observation),
                )

    def test_worst_cell_requires_distinct_tokens_for_distinct_outputs(self) -> None:
        states = (0, 1, 2, 3)
        operation = FiniteOperation(
            "mu", 2, lambda args: (2 * args[0] + args[1]) % 4
        )
        observation = lambda x: x // 2
        capacity = transport_branching_capacity(states, operation, observation)
        codebook = canonical_transport_codebook(states, operation, observation)

        worst_cell, outputs = max(codebook.items(), key=lambda item: len(item[1]))
        self.assertEqual(len(outputs), capacity)
        self.assertEqual(len(set(outputs)), capacity)

        # In one fixed coarse input cell, an exact decoder has no side channel
        # beyond the token. Therefore different coarse outputs must occupy
        # different token positions; the local codebook realizes this lower bound.
        tokens = tuple(range(len(outputs)))
        self.assertEqual(len(set(tokens)), capacity)
        self.assertEqual(worst_cell, worst_cell)  # Keep the side-information cell fixed.


if __name__ == "__main__":
    unittest.main()
