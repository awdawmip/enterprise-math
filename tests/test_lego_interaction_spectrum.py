import itertools
import unittest

from enterprise_math.lego_interaction_spectrum import (
    has_higher_interactions,
    interaction_for_subset,
    interaction_order,
    interaction_spectrum,
    reconstruct_response,
)


def all_subsets(labels):
    labels = tuple(labels)
    for size in range(len(labels) + 1):
        for combo in itertools.combinations(labels, size):
            yield frozenset(combo)


class LegoInteractionSpectrumTests(unittest.TestCase):
    def test_additive_response_has_no_pair_or_higher_interactions(self):
        unit_effects = {
            "a": (1, 0),
            "b": (0, 2),
            "c": (3, -1),
        }
        table = {}
        for subset in all_subsets(unit_effects):
            table[subset] = (
                sum(unit_effects[label][0] for label in subset),
                sum(unit_effects[label][1] for label in subset),
            )
        interactions = interaction_spectrum(table)
        self.assertFalse(has_higher_interactions(interactions, 2))
        self.assertEqual(interaction_order(interactions), 1)
        for subset in table:
            self.assertEqual(reconstruct_response(interactions, subset), table[subset])

    def test_pair_interaction_is_exact_extra_joint_effect(self):
        table = {
            frozenset(): (0,),
            frozenset({"a"}): (2,),
            frozenset({"b"}): (3,),
            frozenset({"a", "b"}): (11,),
        }
        self.assertEqual(
            interaction_for_subset(table, frozenset({"a", "b"})),
            (6,),
        )
        interactions = interaction_spectrum(table)
        self.assertEqual(interactions[frozenset({"a", "b"})], (6,))
        self.assertEqual(reconstruct_response(interactions, frozenset({"a", "b"})), (11,))
        self.assertEqual(interaction_order(interactions), 2)

    def test_pure_three_body_effect_survives_after_all_pair_terms_cancel(self):
        labels = ("a", "b", "c")
        table = {}
        for subset in all_subsets(labels):
            # one unit of baseline per block, plus a pure +7 effect only when all
            # three units coexist.
            table[subset] = (len(subset) + (7 if len(subset) == 3 else 0),)
        interactions = interaction_spectrum(table)
        self.assertEqual(interactions[frozenset({"a", "b", "c"})], (7,))
        for pair in itertools.combinations(labels, 2):
            self.assertEqual(interactions[frozenset(pair)], (0,))
        self.assertEqual(interaction_order(interactions), 3)
        for subset in table:
            self.assertEqual(reconstruct_response(interactions, subset), table[subset])

    def test_nonzero_empty_interaction_tracks_operation_baseline(self):
        table = {
            frozenset(): (5,),
            frozenset({"a"}): (7,),
            frozenset({"b"}): (8,),
            frozenset({"a", "b"}): (10,),
        }
        interactions = interaction_spectrum(table)
        self.assertEqual(interactions[frozenset()], (5,))
        self.assertEqual(interactions[frozenset({"a"})], (2,))
        self.assertEqual(interactions[frozenset({"b"})], (3,))
        self.assertEqual(interactions[frozenset({"a", "b"})], (0,))
        self.assertEqual(reconstruct_response(interactions, frozenset({"a", "b"})), (10,))


if __name__ == "__main__":
    unittest.main()
