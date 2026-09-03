import itertools
import unittest

from enterprise_math.tetrahedral_endpoint_sum import (
    F2_POINTS,
    TORSION_DOUBLE_LIFT,
    TORSION_WITNESS,
    ResidualCode,
    affine_support,
    canonical_decomposition,
    canonical_representative,
    delta_equivalent,
    endpoint_sum,
    hidden_translation_phase,
    lift_difference,
    matching_sums,
    normal_form,
    residual_code,
    verify_torsion_certificate,
)


class TetrahedralEndpointSumTests(unittest.TestCase):
    def test_endpoint_sum_and_matching_identity(self):
        v = (3, -2, 5, -6)
        self.assertEqual(sum(v), 0)
        edges = endpoint_sum(v)
        self.assertEqual(sum(edges), 0)
        self.assertEqual(matching_sums(edges), (0, 0, 0))

    def test_normal_form_has_requested_code(self):
        for p, q, parity in ((0, 0, 0), (2, -3, 1), (-7, 4, 0)):
            state = normal_form(p, q, parity)
            self.assertEqual(residual_code(state), ResidualCode(p, q, parity))

    def test_canonical_decomposition_reconstructs(self):
        for edge_values in (
            (2, -1, 3, -3, 1, -2),
            (5, 2, -4, 1, -3, -1),
            TORSION_WITNESS,
        ):
            self.assertEqual(sum(edge_values), 0)
            decomposition = canonical_decomposition(edge_values)
            self.assertEqual(
                tuple(
                    a + b
                    for a, b in zip(
                        decomposition.representative,
                        endpoint_sum(decomposition.lift),
                    )
                ),
                edge_values,
            )
            self.assertTrue(delta_equivalent(edge_values, decomposition.representative))

    def test_parity_is_exact_lift_obstruction(self):
        zero = (0, 0, 0, 0, 0, 0)
        self.assertIsNone(lift_difference(TORSION_WITNESS, zero))
        doubled = tuple(2 * value for value in TORSION_WITNESS)
        self.assertEqual(lift_difference(doubled, zero), TORSION_DOUBLE_LIFT)
        self.assertTrue(verify_torsion_certificate())

    def test_same_code_if_and_only_if_delta_equivalent_on_sample_box(self):
        states = []
        for first_five in itertools.product(range(-1, 2), repeat=5):
            sixth = -sum(first_five)
            states.append(first_five + (sixth,))
        for x in states[::17]:
            representative = canonical_representative(x)
            self.assertEqual(residual_code(x), residual_code(representative))
            lift = lift_difference(x, representative)
            self.assertIsNotNone(lift)

    def test_affine_nonconstant_states_are_six_two_point_edges(self):
        supports = set()
        for p, q in ((1, 0), (0, 1), (1, 1)):
            for parity in (0, 1):
                support = frozenset(affine_support(ResidualCode(p, q, parity)))
                self.assertEqual(len(support), 2)
                supports.add(support)
        self.assertEqual(len(supports), 6)
        self.assertEqual(
            supports,
            {frozenset(pair) for pair in itertools.combinations(F2_POINTS, 2)},
        )

    def test_torsion_toggle_complements_support(self):
        all_points = set(F2_POINTS)
        for p, q in ((0, 0), (1, 0), (0, 1), (1, 1)):
            code0 = ResidualCode(p, q, 0)
            code1 = ResidualCode(p, q, 1)
            self.assertEqual(
                set(affine_support(code1)),
                all_points - set(affine_support(code0)),
            )

    def test_hidden_translation_phase_is_f2_pairing(self):
        code = ResidualCode(3, 4, 1)
        self.assertEqual(hidden_translation_phase(code, (1, 0)), 1)
        self.assertEqual(hidden_translation_phase(code, (0, 1)), 0)
        self.assertEqual(hidden_translation_phase(code, (1, 1)), 1)


if __name__ == "__main__":
    unittest.main()
