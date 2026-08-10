import unittest

from enterprise_math.causal_laminated_lattice import lambda9_minimal_vectors
from enterprise_math.causal_lattice_selection_hypothesis import (
    causal_coherence_assessment,
    coherence_preference_key,
    pareto_coordinates,
)
from enterprise_math.causal_primitive_link_profile import (
    a_roots,
    d_roots,
    e6_scaled_roots,
    e7_scaled_roots,
    e8_scaled_roots,
    hcp_direction_graph,
    link_profile,
    primitive_direction_graph,
    primitive_link_profile,
)


def z_roots(rank):
    roots = []
    for index in range(rank):
        positive = [0] * rank
        negative = [0] * rank
        positive[index] = 1
        negative[index] = -1
        roots.extend((tuple(positive), tuple(negative)))
    return tuple(roots)


class CausalLatticeSelectionHypothesisTests(unittest.TestCase):
    def test_hard_gate_rejects_simple_axis_and_hcp_but_accepts_fcc(self):
        z3 = primitive_link_profile(z_roots(3), maximum_flag_size=1)
        fcc = primitive_link_profile(a_roots(3), maximum_flag_size=3)
        hcp = link_profile(hcp_direction_graph(), maximum_flag_size=3)
        self.assertFalse(causal_coherence_assessment(z3).hard_gate)
        self.assertTrue(causal_coherence_assessment(fcc).hard_gate)
        self.assertFalse(causal_coherence_assessment(hcp).hard_gate)

    def test_low_dimensional_hypothesis_selects_classical_root_sequence(self):
        candidates = {
            2: {"A2": primitive_link_profile(a_roots(2), maximum_flag_size=2)},
            3: {
                "A3": primitive_link_profile(a_roots(3), maximum_flag_size=3),
                "HCP": link_profile(hcp_direction_graph(), maximum_flag_size=3),
            },
            4: {
                "A4": primitive_link_profile(a_roots(4), maximum_flag_size=4),
                "D4": primitive_link_profile(d_roots(4), maximum_flag_size=4),
            },
            5: {
                "A5": primitive_link_profile(a_roots(5), maximum_flag_size=3),
                "D5": primitive_link_profile(d_roots(5), maximum_flag_size=3),
            },
            6: {
                "A6": primitive_link_profile(a_roots(6), maximum_flag_size=3),
                "D6": primitive_link_profile(d_roots(6), maximum_flag_size=3),
                "E6": primitive_link_profile(e6_scaled_roots(), maximum_flag_size=3),
            },
            7: {
                "A7": primitive_link_profile(a_roots(7), maximum_flag_size=3),
                "D7": primitive_link_profile(d_roots(7), maximum_flag_size=3),
                "E7": primitive_link_profile(e7_scaled_roots(), maximum_flag_size=3),
            },
            8: {
                "A8": primitive_link_profile(a_roots(8), maximum_flag_size=3),
                "D8": primitive_link_profile(d_roots(8), maximum_flag_size=3),
                "E8": primitive_link_profile(e8_scaled_roots(), maximum_flag_size=3),
            },
        }
        expected = {2: "A2", 3: "A3", 4: "D4", 5: "D5", 6: "E6", 7: "E7", 8: "E8"}
        for dimension, profiles in candidates.items():
            winner = min(profiles, key=lambda name: coherence_preference_key(profiles[name]))
            self.assertEqual(winner, expected[dimension])

    def test_lambda9_falsifies_coherence_as_a_universal_density_selector(self):
        lambda9 = link_profile(
            primitive_direction_graph(lambda9_minimal_vectors()),
            maximum_flag_size=1,
        )
        d9 = primitive_link_profile(d_roots(9), maximum_flag_size=3)
        assessment = causal_coherence_assessment(lambda9)
        self.assertFalse(assessment.hard_gate)
        self.assertEqual(lambda9.link_degree_histogram, ((28, 32), (56, 128), (60, 112)))
        self.assertTrue(causal_coherence_assessment(d9).hard_gate)
        self.assertGreater(lambda9.primitive_count, d9.primitive_count)
        self.assertNotEqual(pareto_coordinates(lambda9), pareto_coordinates(d9))


if __name__ == "__main__":
    unittest.main()
