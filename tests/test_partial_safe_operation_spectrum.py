import itertools
import unittest

from enterprise_math.partial_safe_operation_spectrum import (
    four_state_incomparable_refinement_witness,
    four_state_refinement_spectrum,
    partial_endomap_is_safe,
    partition_block_sizes,
    safe_partial_endomap_count,
    safe_total_endomap_count,
    saturated_domain_count,
    total_endomap_is_safe,
)


def partial_endomaps(states):
    states = tuple(states)
    options = (None,) + states
    for targets in itertools.product(options, repeat=len(states)):
        yield {
            state: target
            for state, target in zip(states, targets)
            if target is not None
        }


def total_endomaps(states):
    states = tuple(states)
    for targets in itertools.product(states, repeat=len(states)):
        yield dict(zip(states, targets))


def set_partitions(states):
    states = tuple(states)
    labels = [0] * len(states)
    result = []

    def rec(index, maximum):
        if index == len(states):
            result.append(
                {state: labels[i] for i, state in enumerate(states)}
            )
            return
        for label in range(maximum + 2):
            labels[index] = label
            rec(index + 1, max(maximum, label))

    labels[0] = 0
    if len(states) == 1:
        return ({states[0]: 0},)
    rec(1, 0)
    return tuple(result)


class PartialSafeOperationSpectrumTests(unittest.TestCase):
    def test_closed_counts_match_complete_enumeration_through_four_states(self):
        checked = 0
        for size in range(1, 5):
            states = tuple(range(size))
            partials = tuple(partial_endomaps(states))
            totals = tuple(total_endomaps(states))
            for partition in set_partitions(states):
                direct_partial = sum(
                    partial_endomap_is_safe(partition, operation)
                    for operation in partials
                )
                direct_total = sum(
                    total_endomap_is_safe(partition, operation)
                    for operation in totals
                )
                self.assertEqual(
                    direct_partial,
                    safe_partial_endomap_count(partition),
                )
                self.assertEqual(
                    direct_total,
                    safe_total_endomap_count(partition),
                )
                checked += 1
        self.assertGreater(checked, 20)

    def test_count_depends_only_on_partition_shape(self):
        partitions = (
            {0: "a", 1: "a", 2: "b", 3: "b"},
            {0: "x", 1: "y", 2: "x", 3: "y"},
            {0: 7, 1: 9, 2: 9, 3: 7},
        )
        shapes = {partition_block_sizes(partition) for partition in partitions}
        self.assertEqual(shapes, {(2, 2)})
        self.assertEqual(
            {safe_partial_endomap_count(partition) for partition in partitions},
            {81},
        )
        self.assertEqual(
            {safe_total_endomap_count(partition) for partition in partitions},
            {64},
        )

    def test_four_state_spectrum_is_u_shaped_while_guard_domains_refine_monotonically(self):
        spectrum = four_state_refinement_spectrum()
        self.assertEqual(
            spectrum.partition_shapes,
            ((4,), (2, 2), (1, 1, 1, 1)),
        )
        self.assertEqual(spectrum.partial_counts, (257, 81, 625))
        self.assertEqual(spectrum.total_counts, (256, 64, 256))
        self.assertEqual(spectrum.saturated_domain_counts, (2, 4, 16))
        self.assertGreater(spectrum.partial_counts[0], spectrum.partial_counts[1])
        self.assertLess(spectrum.partial_counts[1], spectrum.partial_counts[2])

    def test_same_refinement_simultaneously_gains_and_loses_safe_operations(self):
        witness = four_state_incomparable_refinement_witness()
        self.assertFalse(
            partial_endomap_is_safe(
                witness.coarse_partition,
                witness.gained_partial_operation,
            )
        )
        self.assertTrue(
            partial_endomap_is_safe(
                witness.fine_partition,
                witness.gained_partial_operation,
            )
        )
        self.assertTrue(
            total_endomap_is_safe(
                witness.coarse_partition,
                witness.lost_total_operation,
            )
        )
        self.assertFalse(
            total_endomap_is_safe(
                witness.fine_partition,
                witness.lost_total_operation,
            )
        )

    def test_saturated_guard_domains_are_exact_unions_of_blocks(self):
        states = (0, 1, 2, 3)
        partition = {0: 0, 1: 0, 2: 1, 3: 2}
        safe_identity_domains = 0
        for mask in range(1 << len(states)):
            domain = {
                state
                for bit, state in enumerate(states)
                if mask & (1 << bit)
            }
            operation = {state: state for state in domain}
            if partial_endomap_is_safe(partition, operation):
                safe_identity_domains += 1
                for block_label in set(partition.values()):
                    block = {
                        state
                        for state, label in partition.items()
                        if label == block_label
                    }
                    self.assertTrue(
                        block <= domain or block.isdisjoint(domain)
                    )
        self.assertEqual(
            safe_identity_domains,
            saturated_domain_count(partition),
        )
        self.assertEqual(safe_identity_domains, 8)

    def test_extreme_partition_formulas(self):
        for size in range(1, 8):
            coarse = {state: 0 for state in range(size)}
            discrete = {state: state for state in range(size)}
            self.assertEqual(
                safe_partial_endomap_count(coarse),
                1 + size**size,
            )
            self.assertEqual(
                safe_total_endomap_count(coarse),
                size**size,
            )
            self.assertEqual(
                safe_partial_endomap_count(discrete),
                (size + 1) ** size,
            )
            self.assertEqual(
                safe_total_endomap_count(discrete),
                size**size,
            )

    def test_three_state_intermediate_partition_already_has_count_valley(self):
        coarse = {0: 0, 1: 0, 2: 0}
        middle = {0: 0, 1: 0, 2: 1}
        discrete = {0: 0, 1: 1, 2: 2}
        self.assertEqual(
            (
                safe_partial_endomap_count(coarse),
                safe_partial_endomap_count(middle),
                safe_partial_endomap_count(discrete),
            ),
            (28, 24, 64),
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            safe_partial_endomap_count({})
        with self.assertRaises(ValueError):
            partial_endomap_is_safe({0: 0, 1: 0}, {2: 0})
        with self.assertRaises(ValueError):
            partial_endomap_is_safe({0: 0, 1: 0}, {0: 2})
        with self.assertRaises(ValueError):
            total_endomap_is_safe({0: 0, 1: 0}, {0: 0})


if __name__ == "__main__":
    unittest.main()
