import unittest

from enterprise_math.causal_gram_lattice import gram_norm
from enterprise_math.causal_laminated_lattice import (
    LAMBDA9_GRAM,
    LAMBDA10_GRAM,
    embedded_degree_transition,
    lambda9_minimal_vectors,
    lambda9_profile,
    lambda10_minimal_vectors,
    lambda10_profile,
    primitive_degree_histogram,
)


class CausalLaminatedLatticeTests(unittest.TestCase):
    def test_exact_gram_enumeration_recovers_catalogue_minimal_shell_sizes(self):
        lambda9 = lambda9_minimal_vectors()
        lambda10 = lambda10_minimal_vectors()
        self.assertEqual(len(lambda9), 272)
        self.assertEqual(len(lambda10), 336)
        self.assertEqual({gram_norm(LAMBDA9_GRAM, v) for v in lambda9}, {4})
        self.assertEqual({gram_norm(LAMBDA10_GRAM, v) for v in lambda10}, {4})

    def test_lambda9_primitive_link_is_not_regular(self):
        vectors = lambda9_minimal_vectors()
        self.assertEqual(
            primitive_degree_histogram(vectors),
            {28: 32, 56: 128, 60: 112},
        )
        profile = lambda9_profile()
        self.assertEqual(profile["layer_histogram"], {-1: 16, 0: 240, 1: 16})
        self.assertEqual(
            profile["layer_degree_histogram"],
            {(-1, 28): 16, (0, 56): 128, (0, 60): 112, (1, 28): 16},
        )
        self.assertEqual(
            profile["layer_edge_histogram"],
            {(-1, -1): 112, (-1, 0): 224, (0, 0): 6720, (0, 1): 224, (1, 1): 112},
        )

    def test_lambda10_preserves_lambda9_shell_and_refines_old_direction_types(self):
        old = lambda9_minimal_vectors()
        new = lambda10_minimal_vectors()
        self.assertEqual(
            embedded_degree_transition(old, new),
            {(28, 36): 32, (56, 60): 128, (60, 60): 64, (60, 68): 48},
        )
        profile = lambda10_profile()
        self.assertEqual(profile["degree_histogram"], {36: 96, 60: 192, 68: 48})
        self.assertEqual(profile["layer_histogram"], {-1: 32, 0: 272, 1: 32})
        self.assertEqual(
            profile["layer_degree_histogram"],
            {
                (-1, 36): 32,
                (0, 36): 32,
                (0, 60): 192,
                (0, 68): 48,
                (1, 36): 32,
            },
        )
        self.assertEqual(
            profile["layer_edge_histogram"],
            {(-1, -1): 288, (-1, 0): 576, (0, 0): 7392, (0, 1): 576, (1, 1): 288},
        )

    def test_lamination_is_dimension_induced_relation_refinement_not_value_change(self):
        old = lambda9_minimal_vectors()
        new = set(lambda10_minimal_vectors())
        self.assertTrue(all(vector + (0,) in new for vector in old))
        # Every old primitive state survives unchanged as an integer coefficient state;
        # only its new-dimensional relation context may gain neighbors.
        transition = embedded_degree_transition(old, tuple(new))
        self.assertEqual(sum(transition.values()), len(old))
        self.assertTrue(all(new_degree >= old_degree for old_degree, new_degree in transition))


if __name__ == "__main__":
    unittest.main()
