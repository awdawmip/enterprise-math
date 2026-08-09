import itertools
import unittest
from collections import Counter
from math import comb

from enterprise_math.p011_repair_spectrum import (
    collision_repair_count,
    collision_repair_spectrum,
    composition_bound_equality_witness,
    composition_repair_bound,
    composition_repair_profile,
    compose_maps,
    maximum_provenance_repair_alphabet,
    provenance_repair_profile,
    reconstruct_repair_distribution_from_spectrum,
    repair_alphabet_distribution,
)


class P011RepairSpectrumTests(unittest.TestCase):
    @staticmethod
    def maps(size: int):
        for values in itertools.product(range(size), repeat=size):
            yield {state: values[state] for state in range(size)}

    def test_local_provenance_repair_is_exact_fiber_size(self) -> None:
        mapping = {0: "a", 1: "a", 2: "b", 3: "b", 4: "b"}
        self.assertEqual(provenance_repair_profile(mapping), {"a": 2, "b": 3})
        self.assertEqual(maximum_provenance_repair_alphabet(mapping), 3)

    def test_collision_spectrum_is_binomial_repair_spectrum(self) -> None:
        mapping = {0: 0, 1: 0, 2: 1, 3: 1, 4: 1}
        profile = provenance_repair_profile(mapping)
        for order in range(1, 6):
            expected = sum(comb(size, order) for size in profile.values())
            self.assertEqual(collision_repair_count(mapping, order), expected)

    def test_binomial_inversion_recovers_local_repair_distribution(self) -> None:
        for mapping in self.maps(5):
            spectrum = collision_repair_spectrum(mapping)
            self.assertEqual(
                reconstruct_repair_distribution_from_spectrum(spectrum),
                repair_alphabet_distribution(mapping),
            )

    def test_postcomposition_profile_is_exact_sum_of_predecessor_repairs(self) -> None:
        first = {0: "a", 1: "a", 2: "b", 3: "b", 4: "b", 5: "c"}
        second = {"a": 0, "b": 0, "c": 1}
        self.assertEqual(provenance_repair_profile(first), {"a": 2, "b": 3, "c": 1})
        self.assertEqual(composition_repair_profile(first, second), {0: 5, 1: 1})
        self.assertEqual(
            provenance_repair_profile(compose_maps(first, second)),
            {0: 5, 1: 1},
        )

    def test_product_bound_holds_exhaustively_on_three_states(self) -> None:
        for first in self.maps(3):
            for second in self.maps(3):
                data = composition_repair_bound(first, second)
                self.assertLessEqual(data["composed_max"], data["product_bound"])
                witness = composition_bound_equality_witness(first, second)
                self.assertEqual(witness is not None, data["equality"])

    def test_product_bound_can_be_strict(self) -> None:
        first = {
            0: "a",
            1: "a",
            2: "a",
            3: "b",
            4: "b",
            5: "c",
            6: "d",
            7: "e",
        }
        second = {"a": "u", "b": "v", "c": "v", "d": "v", "e": "w"}
        data = composition_repair_bound(first, second)
        self.assertEqual(data["first_max"], 3)
        self.assertEqual(data["second_reachable_max"], 3)
        self.assertEqual(data["composed_max"], 4)
        self.assertEqual(data["product_bound"], 9)
        self.assertFalse(data["equality"])

    def test_pair_increment_counts_new_cross_repair_pairs(self) -> None:
        first = {0: "a", 1: "a", 2: "b", 3: "b", 4: "b", 5: "c"}
        second = {"a": 0, "b": 0, "c": 1}
        composed = compose_maps(first, second)
        old_pairs = collision_repair_count(first, 2)
        new_pairs = collision_repair_count(composed, 2)
        # The target 0 merges repair groups of sizes 2 and 3.
        self.assertEqual(new_pairs - old_pairs, 2 * 3)

    def test_spectrum_matches_existing_p011_fiber_formula(self) -> None:
        mapping = {0: "a", 1: "a", 2: "b", 3: "b", 4: "b", 5: "c"}
        sizes = Counter(mapping.values())
        expected = tuple(
            sum(comb(size, order) for size in sizes.values())
            for order in range(1, len(mapping) + 1)
        )
        self.assertEqual(collision_repair_spectrum(mapping), expected)


if __name__ == "__main__":
    unittest.main()
