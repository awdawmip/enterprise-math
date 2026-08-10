import unittest
from fractions import Fraction
from itertools import combinations, product

from enterprise_math.causal_a_voronoi_bridge import (
    a3_voronoi_vertex_partition,
    a_quadratic_grade,
    a_transfer_mass,
    a_voronoi_response_vertices,
    a_voronoi_vertex_count,
    all_declared_vertices_are_primitive_unit_bounded,
    centered_subset_probe,
    cut_probe_distance_identity,
    cut_probe_value,
    maximum_cut_probe_response,
    primitive_response_implies_voronoi_inequality,
    primitive_transfer_cut_response,
    probe_has_zero_gauge,
    probe_is_primitive_unit_bounded,
    quadratic_dominates_twice_transfer_mass,
)


class CausalAVoronoiBridgeTests(unittest.TestCase):
    def test_integer_square_grade_dominates_twice_unit_transfer_mass(self):
        for slots in range(2, 7):
            for displacement in product(range(-2, 3), repeat=slots):
                if sum(displacement) != 0:
                    continue
                self.assertTrue(quadratic_dominates_twice_transfer_mass(displacement))
                self.assertGreaterEqual(a_quadratic_grade(displacement), 2 * a_transfer_mass(displacement))

    def test_every_centered_subset_probe_is_zero_sum_and_primitive_unit_bounded(self):
        for slots in range(2, 8):
            vertices = a_voronoi_response_vertices(slots)
            self.assertEqual(len(vertices), a_voronoi_vertex_count(slots))
            self.assertEqual(len(set(vertices)), len(vertices))
            self.assertTrue(all(probe_has_zero_gauge(vertex) for vertex in vertices))
            self.assertTrue(all(probe_is_primitive_unit_bounded(vertex) for vertex in vertices))
            self.assertTrue(all_declared_vertices_are_primitive_unit_bounded(slots))

    def test_primitive_response_constraints_imply_all_small_voronoi_inequalities(self):
        for slots in range(2, 6):
            probes = a_voronoi_response_vertices(slots)
            displacements = [
                vector
                for vector in product(range(-2, 3), repeat=slots)
                if sum(vector) == 0 and any(vector)
            ]
            for probe in probes:
                for displacement in displacements:
                    self.assertTrue(primitive_response_implies_voronoi_inequality(probe, displacement))

    def test_cut_probes_are_exact_unit_response_extremes_on_primitive_transfers(self):
        for slots in range(2, 7):
            for size in range(1, slots):
                for subset in combinations(range(slots), size):
                    responses = {
                        primitive_transfer_cut_response(slots, receiver, donor, subset)
                        for receiver in range(slots)
                        for donor in range(slots)
                        if receiver != donor
                    }
                    self.assertTrue(responses <= {-1, 0, 1})
                    self.assertIn(1, responses)
                    self.assertIn(-1, responses)

    def test_word_distance_is_maximum_absolute_cut_imbalance(self):
        for slots in range(2, 7):
            for displacement in product(range(-2, 3), repeat=slots):
                if sum(displacement) != 0:
                    continue
                self.assertTrue(cut_probe_distance_identity(displacement))
                self.assertEqual(maximum_cut_probe_response(displacement), a_transfer_mass(displacement))

    def test_centered_subset_probe_pairing_equals_integer_cut_probe_on_zero_sum_states(self):
        for slots in range(2, 6):
            for displacement in product((-1, 0, 1), repeat=slots):
                if sum(displacement) != 0:
                    continue
                for size in range(1, slots):
                    for subset in combinations(range(slots), size):
                        probe = centered_subset_probe(slots, subset)
                        pairing = sum(Fraction(value) * coordinate for value, coordinate in zip(displacement, probe))
                        self.assertEqual(pairing, cut_probe_value(displacement, subset))

    def test_rank_three_has_four_six_four_vertex_orbits_and_fourteen_total(self):
        self.assertEqual(a3_voronoi_vertex_partition(), {1: 4, 2: 6, 3: 4})
        self.assertEqual(a_voronoi_vertex_count(4), 14)

    def test_rank_three_vertices_have_expected_two_level_coordinates(self):
        single = centered_subset_probe(4, (0,))
        pair = centered_subset_probe(4, (0, 1))
        triple = centered_subset_probe(4, (0, 1, 2))
        self.assertEqual(single, (Fraction(3, 4), Fraction(-1, 4), Fraction(-1, 4), Fraction(-1, 4)))
        self.assertEqual(pair, (Fraction(1, 2), Fraction(1, 2), Fraction(-1, 2), Fraction(-1, 2)))
        self.assertEqual(triple, (Fraction(1, 4), Fraction(1, 4), Fraction(1, 4), Fraction(-3, 4)))

    def test_unit_transfer_roots_saturate_voronoi_bound_at_one_response_unit(self):
        probe = centered_subset_probe(5, (0, 2))
        saturated = (1, -1, 0, 0, 0)
        neutral = (1, 0, -1, 0, 0)
        self.assertTrue(primitive_response_implies_voronoi_inequality(probe, saturated))
        self.assertTrue(primitive_response_implies_voronoi_inequality(probe, neutral))


if __name__ == "__main__":
    unittest.main()
