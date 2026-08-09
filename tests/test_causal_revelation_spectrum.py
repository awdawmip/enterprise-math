import unittest

from enterprise_math.causal_revelation_spectrum import (
    collision_profile_by_budget,
    pair_distinguishing_histogram,
    pair_revelation_matches_cost_histogram,
    revelation_spectrum,
    revelation_spectrum_is_nonnegative,
    telescoping_revelation_total,
)


class CausalRevelationSpectrumTests(unittest.TestCase):
    def setUp(self):
        self.states = (0, 1, 2, 3)
        self.observation = {0: 0, 1: 0, 2: 0, 3: 1}
        self.generators = {
            "g": {0: 0, 1: 0, 2: 1, 3: 0},
            "h": {0: 0, 1: 3, 2: 0, 3: 0},
        }
        self.costs = {"g": 2, "h": 5}

    def test_pair_revelation_is_exact_histogram_of_distinguishing_costs(self):
        histogram = pair_distinguishing_histogram(
            self.states,
            self.observation,
            self.generators,
            self.costs,
        )
        self.assertEqual(histogram, {0: 3, 5: 1, 7: 2})
        self.assertTrue(
            pair_revelation_matches_cost_histogram(
                self.states,
                self.observation,
                self.generators,
                self.costs,
            )
        )

    def test_collision_profile_is_monotone_and_revelation_nonnegative(self):
        profile = collision_profile_by_budget(
            self.states,
            self.observation,
            self.generators,
            self.costs,
            maximum_budget=8,
            maximum_order=4,
        )
        for before, after in zip(profile, profile[1:]):
            self.assertEqual(before[0], after[0])  # J1=|X|
            self.assertTrue(all(a <= b for a, b in zip(after[1:], before[1:])))
        self.assertTrue(
            revelation_spectrum_is_nonnegative(
                self.states,
                self.observation,
                self.generators,
                self.costs,
                maximum_budget=8,
                maximum_order=4,
            )
        )

    def test_pair_spectrum_reveals_cost_five_then_cost_seven(self):
        spectrum = revelation_spectrum(
            self.states,
            self.observation,
            self.generators,
            self.costs,
            maximum_budget=8,
            maximum_order=2,
        )
        self.assertEqual(spectrum[4][1], 1)  # budget 5
        self.assertEqual(spectrum[6][1], 2)  # budget 7
        self.assertEqual(sum(row[1] for row in spectrum), 3)

    def test_every_order_telescopes_exactly(self):
        for order in range(1, 5):
            summed, telescoped = telescoping_revelation_total(
                self.states,
                self.observation,
                self.generators,
                self.costs,
                maximum_budget=8,
                order=order,
            )
            self.assertEqual(summed, telescoped)

    def test_permanently_equivalent_pairs_never_appear_in_finite_revelation(self):
        states = (0, 1, 2)
        observation = {0: 0, 1: 0, 2: 1}
        generators = {"id": {0: 0, 1: 1, 2: 2}}
        costs = {"id": 3}
        histogram = pair_distinguishing_histogram(
            states, observation, generators, costs
        )
        self.assertEqual(histogram, {0: 2})
        spectrum = revelation_spectrum(
            states,
            observation,
            generators,
            costs,
            maximum_budget=12,
            maximum_order=2,
        )
        self.assertTrue(all(row[1] == 0 for row in spectrum))


if __name__ == "__main__":
    unittest.main()
