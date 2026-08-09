import unittest
from itertools import product

from enterprise_math.causal_operation_projection import (
    operation_projection_audit,
    operation_projection_collision_spectrum,
    operation_projection_fiber_histogram,
    quotient_endomorphism_count,
    quotient_map_lift_count,
    safe_raw_endomorphism_count,
    uniform_partition_operation_fiber,
)


def _preserves_partition(states, partition, mapping):
    return all(
        partition[a] != partition[b]
        or partition[mapping[a]] == partition[mapping[b]]
        for a in states
        for b in states
    )


def _induced_map(states, partition, mapping):
    classes = max(partition.values()) + 1
    result = [None] * classes
    for state in states:
        source = partition[state]
        target = partition[mapping[state]]
        if result[source] is None:
            result[source] = target
        elif result[source] != target:
            return None
    return tuple(result)


class CausalOperationProjectionTests(unittest.TestCase):
    def test_uniform_partition_has_equal_operation_fibers(self):
        states = (0, 1, 2, 3)
        partition = {0: 0, 1: 0, 2: 1, 3: 1}
        histogram = operation_projection_fiber_histogram(states, partition)
        # c=2,b=2,n=4: 2^2 quotient maps, each with 2^4=16 raw lifts.
        self.assertEqual(histogram, {16: 4})
        self.assertEqual(quotient_endomorphism_count(states, partition), 4)
        self.assertEqual(safe_raw_endomorphism_count(states, partition), 64)
        self.assertTrue(operation_projection_audit(states, partition))
        self.assertEqual(uniform_partition_operation_fiber(2, 2), (4, 16, 64))

    def test_nonuniform_partition_has_nonuniform_operation_fibers(self):
        states = (0, 1, 2, 3)
        partition = {0: 0, 1: 0, 2: 0, 3: 1}  # sizes 3,1
        histogram = operation_projection_fiber_histogram(states, partition)
        self.assertGreater(len(histogram), 1)
        self.assertEqual(sum(histogram.values()), 4)
        self.assertEqual(
            sum(multiplicity * count for multiplicity, count in histogram.items()),
            safe_raw_endomorphism_count(states, partition),
        )
        self.assertTrue(operation_projection_audit(states, partition))

    def test_lift_formula_matches_exhaustive_raw_endomaps(self):
        states = (0, 1, 2)
        partition = {0: 0, 1: 0, 2: 1}  # sizes 2,1
        observed = {}
        for outputs in product(states, repeat=len(states)):
            mapping = dict(zip(states, outputs))
            if not _preserves_partition(states, partition, mapping):
                continue
            induced = _induced_map(states, partition, mapping)
            observed[induced] = observed.get(induced, 0) + 1

        self.assertEqual(len(observed), quotient_endomorphism_count(states, partition))
        for quotient_map, count in observed.items():
            self.assertEqual(
                count,
                quotient_map_lift_count(states, partition, quotient_map),
            )
        self.assertEqual(sum(observed.values()), safe_raw_endomorphism_count(states, partition))

    def test_operation_projection_p011_spectrum_counts_collapsed_raw_dynamics(self):
        states = (0, 1, 2, 3)
        partition = {0: 0, 1: 0, 2: 1, 3: 1}
        # Four quotient maps, each fiber multiplicity 16.
        spectrum = operation_projection_collision_spectrum(states, partition, 3)
        self.assertEqual(spectrum[0], 64)
        self.assertEqual(spectrum[1], 4 * 120)
        self.assertEqual(spectrum[2], 4 * 560)

    def test_discrete_and_indiscrete_extremes_both_preserve_all_raw_maps(self):
        states = (0, 1, 2)
        discrete = {0: 0, 1: 1, 2: 2}
        indiscrete = {0: 0, 1: 0, 2: 0}
        all_maps = len(states) ** len(states)
        self.assertEqual(safe_raw_endomorphism_count(states, discrete), all_maps)
        self.assertEqual(safe_raw_endomorphism_count(states, indiscrete), all_maps)
        # Their quotient-operation projections are nevertheless very different.
        self.assertEqual(quotient_endomorphism_count(states, discrete), all_maps)
        self.assertEqual(quotient_endomorphism_count(states, indiscrete), 1)


if __name__ == "__main__":
    unittest.main()
