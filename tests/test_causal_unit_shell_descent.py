import unittest

from enterprise_math.causal_primitive_group_presentation import dense_coordinate_rank_mod_prime
from enterprise_math.causal_primitive_link_profile import (
    e8_scaled_roots,
    primitive_direction_graph,
)
from enterprise_math.causal_unit_shell_descent import (
    a_family_maximal_slice_count,
    d_family_maximal_slice_count,
    zero_fiber,
)


class CausalUnitShellDescentTests(unittest.TestCase):
    def test_explicit_small_integer_zero_fibers_realize_e8_to_a2_chain(self):
        current = e8_scaled_roots()
        selectors = (
            (-1, -1, 0, 0, 0, 0, 0, 0),
            (-1, 0, -1, 0, 0, 0, 0, 0),
            (-1, 0, 0, 0, 0, 0, 0, 0),
            (0, 0, 0, -1, 0, 0, 0, 0),
            (0, 0, 0, 0, -1, 0, 0, 0),
            (0, 0, 0, 0, 0, -1, -1, -1),
        )
        expected_counts = (126, 72, 40, 24, 12, 6)
        expected_ranks = (7, 6, 5, 4, 3, 2)
        expected_degrees = (32, 20, 12, 8, 4, 2)

        for selector, count, rank, degree in zip(
            selectors, expected_counts, expected_ranks, expected_degrees
        ):
            current = zero_fiber(current, selector)
            self.assertEqual(len(current), count)
            self.assertEqual(dense_coordinate_rank_mod_prime(current), rank)
            adjacency = primitive_direction_graph(current)
            self.assertEqual({len(neighbors) for neighbors in adjacency.values()}, {degree})

    def test_a_family_maximal_slice_count_is_lower_a_root_count(self):
        self.assertEqual([a_family_maximal_slice_count(rank) for rank in range(2, 7)], [2, 6, 12, 20, 30])

    def test_d_family_maximal_slice_count_is_lower_d_root_count(self):
        self.assertEqual([d_family_maximal_slice_count(rank) for rank in range(4, 8)], [12, 24, 40, 60])


if __name__ == "__main__":
    unittest.main()
