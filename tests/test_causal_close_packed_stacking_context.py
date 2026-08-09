import unittest
from itertools import product

from enterprise_math.causal_close_packed_stacking_context import (
    FCC_CONTEXT,
    HCP_IN_PLANE_CONTEXT,
    all_fcc_signs,
    alternating_hcp_signs,
    exact_local_bond_context_histogram,
    local_context_is_determined_by_two_signs,
    local_hcp_indicator,
    predicted_local_bond_context_histogram,
    registry_sequence_from_signs,
)


class CausalClosePackedStackingContextTests(unittest.TestCase):
    def test_constant_sign_trajectory_is_locally_fcc_everywhere(self):
        signs = all_fcc_signs(-5, 5, 1)
        registries = registry_sequence_from_signs(signs, -4, 5)
        self.assertEqual(tuple(registries[layer] for layer in range(0, 7)), (0, 1, 2, 0, 1, 2, 0))
        for layer in range(-2, 3):
            self.assertEqual(exact_local_bond_context_histogram(signs, layer), {FCC_CONTEXT: 12})

    def test_alternating_sign_trajectory_is_locally_hcp_everywhere(self):
        signs = alternating_hcp_signs(-5, 5, 1)
        for layer in range(-2, 3):
            self.assertEqual(
                exact_local_bond_context_histogram(signs, layer),
                {FCC_CONTEXT: 6, HCP_IN_PLANE_CONTEXT: 6},
            )

    def test_two_adjacent_signs_completely_determine_center_bond_context(self):
        # Vary all six local transitions independently.  Only signs -1->0 and
        # 0->1 are allowed to influence the center-layer signature.
        transition_layers = tuple(range(-3, 3))
        for choices in product((-1, 1), repeat=len(transition_layers)):
            signs = dict(zip(transition_layers, choices))
            self.assertTrue(local_context_is_determined_by_two_signs(signs, 0))
            expected = predicted_local_bond_context_histogram(signs[-1], signs[0])
            self.assertEqual(exact_local_bond_context_histogram(signs, 0), expected)

    def test_hcp_indicator_is_exact_context_split_bit(self):
        for previous, following in product((-1, 1), repeat=2):
            chi = local_hcp_indicator(previous, following)
            expected = {FCC_CONTEXT: 12} if chi == 0 else {
                FCC_CONTEXT: 6,
                HCP_IN_PLANE_CONTEXT: 6,
            }
            self.assertEqual(
                predicted_local_bond_context_histogram(previous, following),
                expected,
            )


if __name__ == "__main__":
    unittest.main()
