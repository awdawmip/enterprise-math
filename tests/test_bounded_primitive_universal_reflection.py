import itertools
import unittest

from enterprise_math.bounded_local_law_reflection import (
    bounded_primitive_sumset,
    minimal_reflective_modulus,
    primitive_collision_fixture,
    reflective_modulus_reproduces_exact_weighted_sequence,
    weighted_refinement_sequence,
)
from enterprise_math.relation_support_stable_refinement import partition_from_observation


class BoundedPrimitiveUniversalReflectionTests(unittest.TestCase):
    def test_primitives_one_two_with_two_edges_need_mod_five_uniformly(self):
        primitives = (1, 2)
        max_terms = 2
        alphabet = bounded_primitive_sumset(primitives, max_terms)
        self.assertEqual(alphabet, frozenset({0, 1, 2, 3, 4}))
        self.assertEqual(minimal_reflective_modulus(alphabet), 5)

        states = (0, 1)
        observation = lambda _state: 0
        edges = tuple(itertools.product(states, repeat=2))
        checked = 0
        for choices in itertools.product((None, *primitives), repeat=len(edges)):
            relation = {
                edge: weight
                for edge, weight in zip(edges, choices, strict=True)
                if weight is not None
            }
            # Two target states imply at most two outgoing primitive terms per
            # source, exactly the declared universal class bound.
            family = {"a": relation}
            self.assertTrue(
                reflective_modulus_reproduces_exact_weighted_sequence(
                    states,
                    family,
                    observation,
                    5,
                )
            )
            checked += 1
        self.assertEqual(checked, 3 ** 4)

    def test_every_smaller_modulus_has_a_compiled_class_counterexample(self):
        primitives = (1, 2)
        max_terms = 2
        for modulus in (2, 3, 4):
            states, family, observation, values = primitive_collision_fixture(
                primitives,
                max_terms,
                modulus,
            )
            initial = partition_from_observation(states, observation)
            exact = weighted_refinement_sequence(initial, family)
            modular = weighted_refinement_sequence(initial, family, modulus=modulus)
            self.assertNotEqual(values[0], values[1])
            self.assertEqual(values[0] % modulus, values[1] % modulus)
            self.assertNotEqual(exact, modular)

    def test_scaled_single_primitive_can_need_far_less_than_width_bound(self):
        primitives = (2,)
        max_terms = 2
        alphabet = bounded_primitive_sumset(primitives, max_terms)
        self.assertEqual(alphabet, frozenset({0, 2, 4}))
        self.assertEqual(minimal_reflective_modulus(alphabet), 3)

        states = (0, 1)
        observation = lambda _state: 0
        edges = tuple(itertools.product(states, repeat=2))
        for choices in itertools.product((None, 2), repeat=len(edges)):
            family = {
                "a": {
                    edge: weight
                    for edge, weight in zip(edges, choices, strict=True)
                    if weight is not None
                }
            }
            self.assertTrue(
                reflective_modulus_reproduces_exact_weighted_sequence(
                    states,
                    family,
                    observation,
                    3,
                )
            )


if __name__ == "__main__":
    unittest.main()
