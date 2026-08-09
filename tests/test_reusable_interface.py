import unittest
from itertools import product

from enterprise_math.contextual_closure import (
    FiniteOperation,
    contextual_closure_partition,
)
from enterprise_math.reusable_interface import (
    canonical_reusable_state_count,
    interface_partition,
    observation_factors_through_interface,
    reusable_exact_interface,
    reusable_interface_refines_contextual_closure,
    reusable_interface_state_count,
)
from enterprise_math.transport_branching import transport_branching_capacity


class ReusableInterfaceTests(unittest.TestCase):
    def test_exhaustive_two_state_reusable_interfaces_refine_canonical_closure(self) -> None:
        states = (0, 1)
        for values in product(states, repeat=4):
            operation = FiniteOperation(
                "mu", 2, lambda args, values=values: values[2 * args[0] + args[1]]
            )
            for observation_labels in product((0, 1), repeat=2):
                observation = lambda x, labels=observation_labels: labels[x]
                canonical_count = canonical_reusable_state_count(
                    states, (operation,), observation
                )
                for interface_labels in product((0, 1), repeat=2):
                    interface = lambda x, labels=interface_labels: labels[x]
                    if not reusable_exact_interface(
                        states, (operation,), observation, interface
                    ):
                        continue
                    self.assertTrue(
                        reusable_interface_refines_contextual_closure(
                            states, (operation,), observation, interface
                        )
                    )
                    self.assertGreaterEqual(
                        reusable_interface_state_count(states, interface),
                        canonical_count,
                    )

    def test_raw_observation_can_fail_as_reusable_interface(self) -> None:
        states = (0, 1, 2, 3)
        add = FiniteOperation("add", 2, lambda args: (args[0] + args[1]) % 4)
        observation = lambda x: x // 2
        self.assertTrue(
            observation_factors_through_interface(
                states, observation, observation
            )
        )
        self.assertFalse(
            reusable_exact_interface(states, (add,), observation, observation)
        )

    def test_full_state_is_always_a_reusable_interface(self) -> None:
        states = (0, 1, 2, 3)
        operation = FiniteOperation(
            "mu", 2, lambda args: (2 * args[0] + args[1]) % 4
        )
        observation = lambda x: x // 2
        identity = lambda x: x
        self.assertTrue(
            reusable_exact_interface(states, (operation,), observation, identity)
        )
        self.assertTrue(
            reusable_interface_refines_contextual_closure(
                states, (operation,), observation, identity
            )
        )

    def test_cyclic_radix_addition_has_binary_one_shot_but_full_reusable_state(self) -> None:
        for radix in range(2, 40):
            modulus = 2 * radix
            states = tuple(range(modulus))
            add = FiniteOperation(
                "add",
                2,
                lambda args, modulus=modulus: (args[0] + args[1]) % modulus,
            )
            observation = lambda x, radix=radix: x // radix

            self.assertEqual(
                transport_branching_capacity(states, add, observation),
                2,
            )
            closure = contextual_closure_partition(states, (add,), observation)
            self.assertEqual(len(closure), modulus)
            self.assertEqual(
                canonical_reusable_state_count(states, (add,), observation),
                modulus,
            )

    def test_cyclic_radix_family_gap_grows_without_bound(self) -> None:
        gaps = []
        for radix in range(2, 30):
            modulus = 2 * radix
            states = tuple(range(modulus))
            add = FiniteOperation(
                "add",
                2,
                lambda args, modulus=modulus: (args[0] + args[1]) % modulus,
            )
            observation = lambda x, radix=radix: x // radix
            one_shot = transport_branching_capacity(states, add, observation)
            reusable = canonical_reusable_state_count(states, (add,), observation)
            gaps.append(reusable // one_shot)
            self.assertEqual(one_shot, 2)
            self.assertEqual(reusable // one_shot, radix)
        self.assertGreater(gaps[-1], gaps[0])

    def test_interface_partition_counts_actual_interface_states(self) -> None:
        states = (0, 1, 2, 3, 4)
        interface = lambda x: x % 3
        partition = interface_partition(states, interface)
        self.assertEqual(len(partition), 3)


if __name__ == "__main__":
    unittest.main()
