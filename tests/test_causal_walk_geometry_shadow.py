import unittest

from enterprise_math.causal_laminated_lattice import (
    LAMBDA9_GRAM,
    LAMBDA11_GRAM,
    LAMBDA12_GRAM,
    lambda9_minimal_vectors,
    lambda11_minimal_vectors,
    lambda12_minimal_vectors,
)
from enterprise_math.causal_pair_geometry_shadow import gram_inner_product
from enterprise_math.causal_primitive_link_profile import a_roots, primitive_direction_graph
from enterprise_math.causal_walk_geometry_shadow import minimum_pair_observation_horizon


class CausalWalkGeometryShadowTests(unittest.TestCase):
    def test_a3_root_inner_product_is_first_horizon_shadow(self):
        roots = a_roots(3)
        adjacency = primitive_direction_graph(roots)
        dot = lambda left, right: sum(a * b for a, b in zip(left, right))
        self.assertEqual(minimum_pair_observation_horizon(adjacency, dot, 2), 1)

    def test_lambda9_and_lambda12_gram_pair_geometry_is_second_horizon_shadow(self):
        cases = (
            (LAMBDA9_GRAM, lambda9_minimal_vectors()),
            (LAMBDA12_GRAM, lambda12_minimal_vectors()),
        )
        for gram, vectors in cases:
            adjacency = primitive_direction_graph(vectors)
            observation = lambda left, right, gram=gram: gram_inner_product(gram, left, right)
            self.assertEqual(minimum_pair_observation_horizon(adjacency, observation, 3), 2)

    def test_lambda11_requires_third_causal_walk_horizon(self):
        vectors = lambda11_minimal_vectors()
        adjacency = primitive_direction_graph(vectors)
        observation = lambda left, right: gram_inner_product(LAMBDA11_GRAM, left, right)
        self.assertEqual(minimum_pair_observation_horizon(adjacency, observation, 3), 3)


if __name__ == "__main__":
    unittest.main()
