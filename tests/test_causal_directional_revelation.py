import unittest

from enterprise_math.causal_directional_revelation import (
    direction_revelation_spectrum,
    direction_type_sizes,
    first_direction_split_horizon,
    minimum_precision_direction_contract,
)
from enterprise_math.causal_laminated_lattice import lambda9_minimal_vectors
from enterprise_math.causal_primitive_link_profile import (
    a_roots,
    hcp_direction_graph,
    primitive_direction_graph,
)


def z_roots(rank):
    roots = []
    for index in range(rank):
        for sign in (-1, 1):
            vector = [0] * rank
            vector[index] = sign
            roots.append(tuple(vector))
    return tuple(roots)


class CausalDirectionalRevelationTests(unittest.TestCase):
    def test_fcc_remains_one_direction_type_through_checked_horizon(self):
        adjacency = primitive_direction_graph(a_roots(3))
        self.assertEqual(direction_type_sizes(adjacency, 0), (12,))
        self.assertEqual(direction_type_sizes(adjacency, 1), (12,))
        self.assertEqual(direction_type_sizes(adjacency, 2), (12,))
        self.assertIsNone(first_direction_split_horizon(adjacency, 3))
        self.assertTrue(minimum_precision_direction_contract(adjacency, 3))

    def test_hcp_direction_difference_is_revealed_at_second_relation_horizon(self):
        adjacency = hcp_direction_graph()
        self.assertEqual(direction_type_sizes(adjacency, 0), (12,))
        self.assertEqual(direction_type_sizes(adjacency, 1), (12,))
        self.assertEqual(direction_type_sizes(adjacency, 2), (6, 6))
        self.assertEqual(first_direction_split_horizon(adjacency, 4), 2)
        spectrum = direction_revelation_spectrum(adjacency, 2, 3)
        self.assertEqual(spectrum[0], (0, 0, 0))
        self.assertEqual(spectrum[1], (0, 36, 180))
        self.assertTrue(minimum_precision_direction_contract(adjacency, 1))
        self.assertFalse(minimum_precision_direction_contract(adjacency, 2))

    def test_lambda9_is_anisotropic_at_first_relation_horizon_in_this_language(self):
        adjacency = primitive_direction_graph(lambda9_minimal_vectors())
        self.assertEqual(direction_type_sizes(adjacency, 0), (272,))
        self.assertEqual(direction_type_sizes(adjacency, 1), (128, 112, 32))
        self.assertEqual(first_direction_split_horizon(adjacency, 1), 1)
        spectrum = direction_revelation_spectrum(adjacency, 1, 4)[0]
        self.assertEqual(spectrum, (0, 22016, 2742784, 206156160))
        self.assertFalse(minimum_precision_direction_contract(adjacency, 1))

    def test_simple_axis_vacuous_uniformity_is_rejected_by_connectivity_gate(self):
        adjacency = primitive_direction_graph(z_roots(3))
        self.assertEqual(direction_type_sizes(adjacency, 1), (6,))
        self.assertIsNone(first_direction_split_horizon(adjacency, 3))
        self.assertFalse(minimum_precision_direction_contract(adjacency, 0))


if __name__ == "__main__":
    unittest.main()
