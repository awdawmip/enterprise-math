import itertools
import unittest

from enterprise_math.refinement_forest import (
    all_prufer_degree_sequences,
    maximum_refinement_tree_index,
    minimum_refinement_tree_index,
    refinement_tree_index_formula,
    refinement_tree_index_identity,
    relation_tree_degrees,
    star_parents,
)


def path_parents(vertex_count: int) -> tuple[int, ...]:
    return tuple(-1 if vertex == 0 else vertex - 1 for vertex in range(vertex_count))


class RefinementForestTests(unittest.TestCase):
    def test_direct_determinant_matches_closed_index_formula(self):
        capacity_sets = (
            (1,),
            (1, 1),
            (1, 2, 3),
            (2, 1, 3, 2),
            (1, 2, 1, 3, 2),
        )
        for capacities in capacity_sets:
            count = len(capacities)
            trees = [path_parents(count)]
            trees.extend(star_parents(count, center) for center in range(count))
            for root, parents in enumerate(trees):
                # Every generated parents tuple carries its own unique -1 root.
                actual_root = parents.index(-1)
                self.assertEqual(
                    refinement_tree_index_identity(
                        capacities, parents, actual_root
                    )[0],
                    refinement_tree_index_identity(
                        capacities, parents, actual_root
                    )[1],
                )

    def test_unit_capacities_make_relation_tree_index_shape_independent(self):
        for count in range(2, 9):
            capacities = (1,) * count
            self.assertEqual(
                refinement_tree_index_formula(
                    capacities, path_parents(count), 0
                ),
                count,
            )
            for center in range(count):
                parents = star_parents(count, center)
                self.assertEqual(
                    refinement_tree_index_formula(capacities, parents, center),
                    count,
                )

    def test_star_index_formula(self):
        capacities = (2, 5, 3, 7, 4)
        total_capacity = sum(capacities)
        count = len(capacities)
        for center, capacity in enumerate(capacities):
            parents = star_parents(count, center)
            self.assertEqual(
                relation_tree_degrees(parents, center)[center],
                count - 1,
            )
            self.assertEqual(
                refinement_tree_index_formula(capacities, parents, center),
                total_capacity * capacity ** (count - 2),
            )

    def test_prufer_degree_extrema_match_minimum_and_maximum_capacity_stars(self):
        for capacities in (
            (1, 2),
            (1, 2, 3),
            (2, 1, 3, 2),
            (4, 1, 2, 3, 5),
        ):
            count = len(capacities)
            if count == 2:
                observed = [sum(capacities)]
            else:
                total_capacity = sum(capacities)
                observed = []
                for degrees in all_prufer_degree_sequences(count):
                    index = total_capacity
                    for capacity, degree in zip(capacities, degrees):
                        index *= capacity ** (degree - 1)
                    observed.append(index)
            self.assertEqual(min(observed), minimum_refinement_tree_index(capacities))
            self.assertEqual(max(observed), maximum_refinement_tree_index(capacities))

    def test_extrema_are_attained_at_min_and_max_capacity_stars(self):
        for capacities in itertools.product(range(1, 4), repeat=5):
            min_center = min(range(5), key=lambda index: capacities[index])
            max_center = max(range(5), key=lambda index: capacities[index])
            min_parents = star_parents(5, min_center)
            max_parents = star_parents(5, max_center)
            self.assertEqual(
                refinement_tree_index_formula(capacities, min_parents, min_center),
                minimum_refinement_tree_index(capacities),
            )
            self.assertEqual(
                refinement_tree_index_formula(capacities, max_parents, max_center),
                maximum_refinement_tree_index(capacities),
            )


if __name__ == "__main__":
    unittest.main()
