import unittest

from enterprise_math.causal_interaction_coupling_bridge import (
    binary_lego_interaction,
    induced_response_map,
    response_descends_through_marginals,
    response_split_excess,
)


class CausalInteractionCouplingBridgeTests(unittest.TestCase):
    def test_nonlinear_response_can_be_fully_determined_by_marginals(self):
        # Four fully visible marginal pairs.  The cross response a*b has a
        # nonzero LEGO pair interaction, but adds no new future distinction.
        state_to_marginal = {
            "00": (0, 0),
            "01": (0, 1),
            "10": (1, 0),
            "11": (1, 1),
        }
        response = {
            "00": 0,
            "01": 0,
            "10": 0,
            "11": 1,
        }
        self.assertEqual(binary_lego_interaction(0, 0, 0, 1), 1)
        self.assertTrue(response_descends_through_marginals(state_to_marginal, response))
        self.assertEqual(response_split_excess(state_to_marginal, response), 0)
        self.assertEqual(induced_response_map(state_to_marginal, response)[(1, 1)], 1)

    def test_response_creates_coupling_exactly_when_marginal_fiber_is_split(self):
        state_to_marginal = {
            "x0": ("a", "b"),
            "x1": ("a", "b"),
            "x2": ("c", "d"),
        }
        response = {
            "x0": 0,
            "x1": 1,
            "x2": 0,
        }
        self.assertFalse(response_descends_through_marginals(state_to_marginal, response))
        self.assertEqual(response_split_excess(state_to_marginal, response), 1)
        with self.assertRaises(ValueError):
            induced_response_map(state_to_marginal, response)

    def test_constant_cross_response_is_causally_redundant(self):
        state_to_marginal = {
            "x0": (0, 0),
            "x1": (0, 0),
            "x2": (1, 1),
        }
        response = {"x0": 7, "x1": 7, "x2": 9}
        self.assertTrue(response_descends_through_marginals(state_to_marginal, response))
        self.assertEqual(response_split_excess(state_to_marginal, response), 0)


if __name__ == "__main__":
    unittest.main()
