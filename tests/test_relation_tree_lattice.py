import itertools
import unittest

from enterprise_math.relation_lattice import (
    capacity_gcd,
    primitive_capacity_vector,
    relation_translation_period,
)
from enterprise_math.relation_tree_lattice import (
    primitive_tree_relation_lattice_index,
    reconstruct_primitive_unit_star,
    tree_degrees,
    tree_relation_coordinates,
    tree_relation_index_extrema,
    tree_relation_lattice_index,
)


def bareiss_determinant(matrix):
    values = [list(row) for row in matrix]
    size = len(values)
    if size == 0:
        return 1
    if any(len(row) != size for row in values):
        raise ValueError("determinant matrix must be square")
    if size == 1:
        return values[0][0]
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        pivot_row = next(
            (
                row
                for row in range(pivot_index, size)
                if values[row][pivot_index] != 0
            ),
            None,
        )
        if pivot_row is None:
            return 0
        if pivot_row != pivot_index:
            values[pivot_index], values[pivot_row] = (
                values[pivot_row],
                values[pivot_index],
            )
            sign *= -1
        pivot = values[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for col in range(pivot_index + 1, size):
                numerator = (
                    values[row][col] * pivot
                    - values[row][pivot_index] * values[pivot_index][col]
                )
                if numerator % previous:
                    raise AssertionError("Bareiss elimination lost exact divisibility")
                values[row][col] = numerator // previous
        previous = pivot
        for row in range(pivot_index + 1, size):
            values[row][pivot_index] = 0
    return sign * values[-1][-1]


def coordinate_matrix(capacities, edges, primitive=False):
    divisor = capacity_gcd(capacities) if primitive else 1
    matrix = [[1] * len(capacities)]
    for left, right in edges:
        row = [0] * len(capacities)
        row[left] = capacities[right] // divisor
        row[right] = -capacities[left] // divisor
        matrix.append(row)
    return tuple(tuple(row) for row in matrix)


def prufer_tree(sequence, vertex_count):
    if vertex_count == 1:
        return ()
    if vertex_count == 2:
        return ((0, 1),)
    degrees = [1] * vertex_count
    for vertex in sequence:
        degrees[vertex] += 1
    edges = []
    for vertex in sequence:
        leaf = min(index for index, degree in enumerate(degrees) if degree == 1)
        edges.append((leaf, vertex))
        degrees[leaf] -= 1
        degrees[vertex] -= 1
    leaves = [index for index, degree in enumerate(degrees) if degree == 1]
    edges.append((leaves[0], leaves[1]))
    return tuple(edges)


def all_labelled_trees(vertex_count):
    if vertex_count == 1:
        return ((),)
    if vertex_count == 2:
        return (((0, 1),),)
    return tuple(
        prufer_tree(sequence, vertex_count)
        for sequence in itertools.product(range(vertex_count), repeat=vertex_count - 2)
    )


class RelationTreeLatticeTests(unittest.TestCase):
    def test_exact_determinant_formula_on_all_labelled_trees_through_five_vertices(self):
        capacity_families = {
            1: ((7,),),
            2: ((1, 1), (2, 3), (4, 6)),
            3: ((1, 2, 3), (2, 4, 6), (3, 5, 7)),
            4: ((1, 2, 3, 4), (2, 6, 4, 10), (3, 5, 7, 11)),
            5: ((1, 2, 3, 4, 5), (2, 4, 6, 8, 10), (2, 3, 5, 7, 11)),
        }
        for vertex_count, families in capacity_families.items():
            for capacities in families:
                for edges in all_labelled_trees(vertex_count):
                    full_det = abs(bareiss_determinant(coordinate_matrix(capacities, edges)))
                    primitive_det = abs(
                        bareiss_determinant(
                            coordinate_matrix(capacities, edges, primitive=True)
                        )
                    )
                    self.assertEqual(
                        full_det,
                        tree_relation_lattice_index(capacities, edges),
                    )
                    self.assertEqual(
                        primitive_det,
                        primitive_tree_relation_lattice_index(capacities, edges),
                    )

    def test_primitive_index_is_full_index_with_all_relation_quanta_removed(self):
        for capacities in (
            (2, 4),
            (6, 10, 14),
            (12, 18, 30, 42),
        ):
            divisor = capacity_gcd(capacities)
            for edges in all_labelled_trees(len(capacities)):
                self.assertEqual(
                    tree_relation_lattice_index(capacities, edges),
                    primitive_tree_relation_lattice_index(capacities, edges)
                    * divisor ** (len(capacities) - 1),
                )

    def test_tree_index_extrema_are_exact_over_all_labelled_trees(self):
        for capacities in (
            (2, 3, 5),
            (2, 4, 7, 9),
            (3, 6, 10, 15, 21),
        ):
            report = tree_relation_index_extrema(capacities)
            full_indices = []
            primitive_indices = []
            for edges in all_labelled_trees(len(capacities)):
                full_indices.append(tree_relation_lattice_index(capacities, edges))
                primitive_indices.append(
                    primitive_tree_relation_lattice_index(capacities, edges)
                )
            self.assertEqual(report.minimum_index, min(full_indices))
            self.assertEqual(report.maximum_index, max(full_indices))
            self.assertEqual(report.primitive_minimum_index, min(primitive_indices))
            self.assertEqual(report.primitive_maximum_index, max(primitive_indices))

    def test_minimum_and_maximum_are_star_centers_at_extreme_capacities(self):
        capacities = (2, 3, 5, 7, 11)
        report = tree_relation_index_extrema(capacities)
        for center, expected in (
            (report.minimum_centers[0], report.minimum_index),
            (report.maximum_centers[0], report.maximum_index),
        ):
            edges = tuple(
                (center, leaf)
                for leaf in range(len(capacities))
                if leaf != center
            )
            self.assertEqual(tree_relation_lattice_index(capacities, edges), expected)

    def test_tree_coordinates_reconstruct_direct_weighted_relations(self):
        capacities = (6, 10, 14, 22)
        totals = (5, -3, 8, 1)
        edges = ((2, 0), (2, 1), (3, 2))
        coordinates = tree_relation_coordinates(capacities, totals, edges)
        primitive = tree_relation_coordinates(
            capacities, totals, edges, primitive=True
        )
        self.assertEqual(coordinates[0], sum(totals))
        divisor = capacity_gcd(capacities)
        for index, (left, right) in enumerate(edges, start=1):
            expected = capacities[right] * totals[left] - capacities[left] * totals[right]
            self.assertEqual(coordinates[index], expected)
            self.assertEqual(primitive[index], expected // divisor)

    def test_unit_primitive_star_has_one_exact_mod_tau_legality_condition(self):
        capacities = (6, 12, 30, 42)
        primitive = primitive_capacity_vector(capacities)
        self.assertEqual(primitive[0], 1)
        tau = relation_translation_period(capacities)
        self.assertEqual(tau, sum(primitive))
        center = 0

        for totals in (
            (5, -3, 8, 1),
            (0, 0, 0, 0),
            (-4, 7, 2, -1),
        ):
            edges = tuple((center, leaf) for leaf in range(1, len(capacities)))
            coordinates = tree_relation_coordinates(
                capacities,
                totals,
                edges,
                primitive=True,
            )
            reconstructed = reconstruct_primitive_unit_star(
                capacities,
                center,
                coordinates[0],
                tuple((leaf, relation) for leaf, relation in zip(range(1, len(capacities)), coordinates[1:])),
            )
            self.assertTrue(reconstructed.legal)
            self.assertEqual(reconstructed.reconstructed_totals, totals)
            self.assertEqual(reconstructed.congruence_numerator % tau, 0)

        illegal = reconstruct_primitive_unit_star(
            capacities,
            center,
            grand_total=0,
            leaf_relations=((1, 0), (2, 0), (3, 1)),
        )
        self.assertFalse(illegal.legal)
        self.assertIsNone(illegal.reconstructed_totals)
        self.assertNotEqual(illegal.congruence_numerator % tau, 0)

    def test_equal_capacities_make_every_tree_have_index_N_after_primitive_normalization(self):
        for vertex_count in range(2, 6):
            capacities = (6,) * vertex_count
            for edges in all_labelled_trees(vertex_count):
                self.assertEqual(
                    primitive_tree_relation_lattice_index(capacities, edges),
                    vertex_count,
                )

    def test_edge_orientation_changes_relation_sign_not_lattice_index(self):
        capacities = (2, 3, 5, 7)
        totals = (4, -1, 6, 2)
        edges = ((0, 1), (1, 2), (1, 3))
        reversed_edges = tuple((right, left) for left, right in edges)
        first = tree_relation_coordinates(capacities, totals, edges)
        second = tree_relation_coordinates(capacities, totals, reversed_edges)
        self.assertEqual(first[0], second[0])
        self.assertEqual(first[1:], tuple(-value for value in second[1:]))
        self.assertEqual(
            tree_relation_lattice_index(capacities, edges),
            tree_relation_lattice_index(capacities, reversed_edges),
        )

    def test_invalid_tree_and_star_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            tree_relation_lattice_index((1, 2, 3), ((0, 1),))
        with self.assertRaises(ValueError):
            tree_relation_lattice_index((1, 2, 3), ((0, 1), (1, 0)))
        with self.assertRaises(ValueError):
            tree_relation_lattice_index((1, 2, 3), ((0, 1), (1, 3)))
        with self.assertRaises(ValueError):
            reconstruct_primitive_unit_star(
                (2, 3, 5),
                center=0,
                grand_total=0,
                leaf_relations=((1, 0), (2, 0)),
            )
        with self.assertRaises(ValueError):
            reconstruct_primitive_unit_star(
                (1, 2, 3),
                center=0,
                grand_total=0,
                leaf_relations=((1, 0),),
            )

    def test_single_vertex_degenerates_to_identity_coordinate(self):
        capacities = (9,)
        self.assertEqual(tree_degrees(capacities, ()), (0,))
        self.assertEqual(tree_relation_lattice_index(capacities, ()), 1)
        self.assertEqual(primitive_tree_relation_lattice_index(capacities, ()), 1)
        self.assertEqual(tree_relation_coordinates(capacities, (-4,), ()), (-4,))


if __name__ == "__main__":
    unittest.main()
