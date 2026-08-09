import itertools
import unittest
from math import comb

from enterprise_math.precision_projection_spectrum import (
    chain_projection_profiles,
    local_repair_sizes,
    minimum_repair_alphabet_size,
    reconstruct_repair_distribution_from_spectrum,
    repair_size_distribution,
    repair_spectrum,
    refines,
)
from enterprise_math.task_precision_refinement import (
    minimal_repair_alphabet_size as generic_minimum_repair,
)


class PrecisionProjectionSpectrumTests(unittest.TestCase):
    def test_local_split_sizes_are_projection_fiber_sizes(self) -> None:
        states = tuple(range(8))
        fine = {
            0: "a0",
            1: "a1",
            2: "a2",
            3: "b0",
            4: "b0",
            5: "b1",
            6: "c0",
            7: "c0",
        }
        coarse = {
            0: "A",
            1: "A",
            2: "A",
            3: "B",
            4: "B",
            5: "B",
            6: "B",
            7: "B",
        }
        self.assertTrue(refines(states, fine, coarse))
        self.assertEqual(local_repair_sizes(states, fine, coarse), {"A": 3, "B": 3})
        self.assertEqual(minimum_repair_alphabet_size(states, fine, coarse), 3)
        self.assertEqual(generic_minimum_repair(states, fine, coarse), 3)

    def test_spectrum_is_p011_collision_spectrum_of_quotient_projection(self) -> None:
        states = tuple(range(6))
        fine = {state: state for state in states}
        coarse = {state: state // 3 for state in states}
        spectrum = repair_spectrum(states, fine, coarse)
        expected = tuple(
            2 * comb(3, order) for order in range(1, 7)
        )
        self.assertEqual(spectrum, expected)

    def test_binomial_inversion_recovers_all_local_repair_sizes(self) -> None:
        states = tuple(range(9))
        fine = {
            0: "a0",
            1: "a1",
            2: "a2",
            3: "b0",
            4: "b0",
            5: "b1",
            6: "c0",
            7: "d0",
            8: "d0",
        }
        coarse = {
            0: "A",
            1: "A",
            2: "A",
            3: "B",
            4: "B",
            5: "B",
            6: "C",
            7: "C",
            8: "C",
        }
        spectrum = repair_spectrum(states, fine, coarse)
        self.assertEqual(
            reconstruct_repair_distribution_from_spectrum(spectrum),
            repair_size_distribution(states, fine, coarse),
        )
        self.assertEqual(
            {size: count for size, count in repair_size_distribution(states, fine, coarse).items() if count},
            {1: 1, 2: 1, 3: 1},
        )

    def test_refinement_chain_projection_fibers_compose_exactly(self) -> None:
        states = tuple(range(12))
        finest = {state: state for state in states}
        middle = {state: (state // 6, (state % 6) // 2) for state in states}
        coarsest = {state: state // 6 for state in states}
        data = chain_projection_profiles(states, finest, middle, coarsest)
        self.assertEqual(data["first_max"], 2)
        self.assertEqual(data["second_max"], 3)
        self.assertEqual(data["direct_max"], 6)
        self.assertEqual(data["product_bound"], 6)

    def test_chain_product_bound_can_be_strict(self) -> None:
        states = tuple(range(8))
        finest = {state: state for state in states}
        middle = {
            0: "a",
            1: "a",
            2: "a",
            3: "b",
            4: "c",
            5: "d",
            6: "e",
            7: "f",
        }
        coarsest = {
            0: "U",
            1: "U",
            2: "U",
            3: "V",
            4: "V",
            5: "V",
            6: "W",
            7: "W",
        }
        data = chain_projection_profiles(states, finest, middle, coarsest)
        self.assertEqual(data["first_max"], 3)
        self.assertEqual(data["second_max"], 3)
        self.assertEqual(data["direct_max"], 3)
        self.assertEqual(data["product_bound"], 9)

    def test_more_precise_observation_reduces_absolute_ambiguity_spectrum(self) -> None:
        states = tuple(range(4))
        identity = {state: state for state in states}
        coarse = {state: 0 for state in states}
        fine = {state: state % 2 for state in states}
        self.assertTrue(refines(states, fine, coarse))
        coarse_spectrum = repair_spectrum(states, identity, coarse)
        fine_spectrum = repair_spectrum(states, identity, fine)
        for order in range(1, len(states)):
            self.assertLessEqual(fine_spectrum[order], coarse_spectrum[order])

    def test_exhaustive_small_partition_refinement_monotonicity(self) -> None:
        states = (0, 1, 2, 3)
        partitions = []
        for labels in itertools.product(range(4), repeat=4):
            partition = dict(zip(states, labels, strict=True))
            # Canonicalize by equality relation only.
            if any(
                all(partition[s] == existing[s] for s in states)
                for existing in partitions
            ):
                continue
            partitions.append(partition)

        identity = {state: state for state in states}
        for fine in partitions:
            for coarse in partitions:
                if not refines(states, fine, coarse):
                    continue
                fine_abs = repair_spectrum(states, identity, fine)
                coarse_abs = repair_spectrum(states, identity, coarse)
                self.assertTrue(
                    all(a <= b for a, b in zip(fine_abs, coarse_abs, strict=True))
                )


if __name__ == "__main__":
    unittest.main()
