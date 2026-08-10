import unittest
from fractions import Fraction
from itertools import product

from enterprise_math.precision_genesis import (
    ball,
    branching_increment,
    collapse_fibers,
    collision_spectrum,
    compatible_paths,
    construct_dual_monotone_system,
    dual_monotone_transition_compatible,
    environment_overlap,
    exhaustive_hidden_geometry_counts,
    exhaustive_history_resurrection_counts,
    first_geometry_scale,
    geodesic_count,
    history_balance,
    history_count,
    merge_excess,
    occupied_count,
    projection,
    projection_relation,
    propagate_history_multiplicities,
    rational_seed,
    shell,
    shortest_distance,
    square_forward_difference,
    square_riemann_error,
    square_riemann_sum,
    toy_universe,
)


class PrecisionGenesisTests(unittest.TestCase):
    def test_precision_one_and_hidden_geometry_counterexample(self):
        layers = toy_universe()
        self.assertEqual(layers[0].states, (0,))
        self.assertFalse(layers[0].adjacency)
        self.assertEqual(
            exhaustive_hidden_geometry_counts(3),
            {
                "observable_classes": 1,
                "simple_graphs": 8,
                "nonempty_simple_graphs": 7,
                "connected_simple_graphs": 4,
            },
        )

    def test_forgetting_relational_refinement_and_finite_latent_paths(self):
        self.assertEqual(
            (projection(7, 1, 8), projection(7, 2, 8), projection(7, 4, 8)),
            (0, 1, 3),
        )
        self.assertEqual(
            projection_relation(2, 4),
            frozenset({(0, 0), (0, 1), (1, 2), (1, 3)}),
        )
        paths = compatible_paths((1, 2, 4, 8))
        self.assertEqual(len(paths), 8)
        self.assertEqual(paths[-1], (0, 1, 3, 7))

    def test_many_to_one_collapse(self):
        self.assertEqual(
            collapse_fibers(range(6)), {0: (0, 1), 2: (2, 3), 4: (4, 5)}
        )

    def test_geometry_emergence_and_intrinsic_observables(self):
        layers = toy_universe(8, 4)
        self.assertEqual(first_geometry_scale(layers), 4)
        geometry = next(layer for layer in layers if layer.scale == 4)
        self.assertEqual(
            shortest_distance(geometry.states, geometry.adjacency, 0, 2), 2
        )
        self.assertEqual(
            shell(geometry.states, geometry.adjacency, 0, 1), frozenset({1, 3})
        )
        self.assertEqual(
            ball(geometry.states, geometry.adjacency, 0, 1), frozenset({0, 1, 3})
        )
        self.assertEqual(
            geodesic_count(geometry.states, geometry.adjacency, 0, 2), 2
        )

    def test_exhaustive_history_resurrection_boundary(self):
        self.assertEqual(
            exhaustive_history_resurrection_counts(3),
            {
                "state_extensional_relations": 7,
                "state_extensional_resurrections": 0,
                "history_indexed_relations": 49,
                "history_indexed_resurrections": 42,
            },
        )

    def test_branching_opens_paths_without_resurrecting_merge(self):
        before = {0: 2}
        relation = frozenset({(0, 0), (0, 1)})
        after = propagate_history_multiplicities(before, relation)
        self.assertEqual(after, {0: 2, 1: 2})
        self.assertEqual((history_count(before), history_count(after)), (2, 4))
        self.assertEqual((occupied_count(before), occupied_count(after)), (1, 2))
        self.assertEqual((merge_excess(before), merge_excess(after)), (1, 2))
        self.assertEqual(history_balance(before, relation), (2, 1, 1))

    def test_toy_open_merge_reopen_collision_spectrum(self):
        multiplicities = {0: 1}
        multiplicities = propagate_history_multiplicities(
            multiplicities, frozenset({(0, 0), (0, 1)})
        )
        self.assertEqual(dict(collision_spectrum(multiplicities, 2))[2], 0)
        multiplicities = propagate_history_multiplicities(
            multiplicities, frozenset({(0, 0), (1, 0)})
        )
        self.assertEqual(dict(collision_spectrum(multiplicities, 2))[2], 1)
        multiplicities = propagate_history_multiplicities(
            multiplicities, frozenset({(0, 0), (0, 1)})
        )
        self.assertEqual(multiplicities, {0: 2, 1: 2})
        self.assertEqual(dict(collision_spectrum(multiplicities, 2))[2], 2)

    def test_exhaustive_small_serial_relations_preserve_Wk(self):
        targets = (0, 1, 2)
        supports = [
            frozenset(
                target
                for index, target in enumerate(targets)
                if mask & (1 << index)
            )
            for mask in range(1, 8)
        ]
        checked = 0
        for left, right in product(supports, repeat=2):
            relation = frozenset(
                [(0, target) for target in left]
                + [(1, target) for target in right]
            )
            for n0, n1 in product(range(3), repeat=2):
                if n0 == n1 == 0:
                    continue
                before = {0: n0, 1: n1}
                after = propagate_history_multiplicities(before, relation)
                before_spectrum = dict(collision_spectrum(before, 3))
                after_spectrum = dict(collision_spectrum(after, 3))
                self.assertTrue(
                    all(
                        after_spectrum[order] >= before_spectrum[order]
                        for order in (1, 2, 3)
                    )
                )
                checked += 1
        self.assertEqual(checked, 392)

    def test_history_indexed_split_can_resurrect(self):
        self.assertEqual(dict(collision_spectrum({0: 2}, 2))[2], 1)
        self.assertEqual(dict(collision_spectrum({"h0": 1, "h1": 1}, 2))[2], 0)

    def test_exact_branching_balance(self):
        before = {0: 2, 1: 1}
        relation = frozenset({(0, "a"), (0, "b"), (1, "b")})
        after = propagate_history_multiplicities(before, relation)
        branch, occupied_delta, merge_delta = history_balance(before, relation)
        self.assertEqual(
            history_count(after) - history_count(before),
            branching_increment(before, relation),
        )
        self.assertEqual(merge_delta, branch - occupied_delta)
        self.assertGreaterEqual(merge_delta, 0)

    def test_arbitrary_dual_monotone_sequences_have_finite_model(self):
        system = construct_dual_monotone_system((4, 7, 9, 12), (4, 3, 2, 1))
        self.assertTrue(dual_monotone_transition_compatible(system))
        self.assertEqual(
            tuple(len(set(mapping)) for mapping in system.history_maps),
            (4, 3, 2, 1),
        )

    def test_environment_overlap_is_exact(self):
        self.assertEqual(
            environment_overlap(("a", "b"), ("a", "b")), Fraction(1, 1)
        )
        self.assertEqual(
            environment_overlap(("a", "b"), ("a", "c")), Fraction(1, 2)
        )
        self.assertEqual(
            environment_overlap(("a", "b"), ("c", "d")), Fraction(0, 1)
        )

    def test_finite_continuum_approximations(self):
        self.assertEqual(square_riemann_sum(4), Fraction(7, 32))
        self.assertEqual(square_riemann_error(4), Fraction(11, 96))
        self.assertLessEqual(square_riemann_error(4), Fraction(1, 8))
        self.assertEqual(square_forward_difference(10, 3), Fraction(7, 10))
        self.assertEqual(
            square_forward_difference(10, 3) - Fraction(6, 10), Fraction(1, 10)
        )

    def test_rational_branching_has_finite_integer_seed(self):
        self.assertEqual(
            rational_seed((Fraction(1, 2), Fraction(1, 3), Fraction(1, 6))),
            (6, (3, 2, 1)),
        )


if __name__ == "__main__":
    unittest.main()
