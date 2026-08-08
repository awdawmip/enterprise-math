import itertools
import unittest
from collections import Counter


class TestP010HistoryMerge(unittest.TestCase):
    @staticmethod
    def all_maps(size):
        for values in itertools.product(range(size), repeat=size):
            yield values

    @staticmethod
    def compose(first, second):
        return tuple(second[first[x]] for x in range(len(first)))

    @staticmethod
    def multiplicity(mapping, x):
        target = mapping[x]
        return sum(1 for value in mapping if value == target)

    @staticmethod
    def image(mapping):
        return set(mapping)

    @staticmethod
    def restricted_injective(mapping, reachable):
        values = [mapping[z] for z in reachable]
        return len(values) == len(set(values))

    def test_strict_growth_criterion_exhaustive_on_three_states(self):
        size = 3
        for current in self.all_maps(size):
            for next_map in self.all_maps(size):
                updated = self.compose(current, next_map)
                for x in range(size):
                    strict = self.multiplicity(updated, x) > self.multiplicity(current, x)
                    witness = any(
                        current[y] != current[x]
                        and next_map[current[y]] == next_map[current[x]]
                        for y in range(size)
                    )
                    self.assertEqual(strict, witness)

    def test_increment_formula_exhaustive_on_three_states(self):
        size = 3
        for current in self.all_maps(size):
            old_weights = Counter(current)
            for next_map in self.all_maps(size):
                updated = self.compose(current, next_map)
                reachable = self.image(current)
                for x in range(size):
                    collision_states = {
                        z for z in reachable if next_map[z] == next_map[current[x]]
                    }
                    expected = sum(old_weights[z] for z in collision_states)
                    self.assertEqual(self.multiplicity(updated, x), expected)
                    increment = expected - old_weights[current[x]]
                    expected_increment = sum(
                        old_weights[z] for z in collision_states if z != current[x]
                    )
                    self.assertEqual(increment, expected_increment)

    def test_no_new_merging_iff_injective_on_reachable_image(self):
        size = 3
        for current in self.all_maps(size):
            reachable = self.image(current)
            for next_map in self.all_maps(size):
                updated = self.compose(current, next_map)
                no_new_merging = all(
                    self.multiplicity(updated, x) == self.multiplicity(current, x)
                    for x in range(size)
                )
                self.assertEqual(
                    no_new_merging,
                    self.restricted_injective(next_map, reachable),
                )

    def test_global_noninjectivity_outside_reachable_image_is_irrelevant(self):
        current = (0, 0, 1, 1)
        next_map = (0, 1, 2, 2)
        updated = self.compose(current, next_map)

        self.assertFalse(self.restricted_injective(next_map, set(range(4))))
        self.assertTrue(self.restricted_injective(next_map, self.image(current)))
        self.assertEqual(
            [self.multiplicity(updated, x) for x in range(4)],
            [self.multiplicity(current, x) for x in range(4)],
        )


if __name__ == "__main__":
    unittest.main()
