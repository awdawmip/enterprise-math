import unittest
from fractions import Fraction

from enterprise_math.abc_projective_debruijn_bridge import (
    classical_debruijn_abc_limit_power,
    classical_selector_strictly_beats_pcc_route,
    nonunit_pcc_failure_pair_radical_state,
    oesterle_via_pcc_debruijn_limit_power,
    pcc_debruijn_failure_power,
    unit_pcc_failure_small_radical_component,
)


class ProjectiveDebruijnBridgeTests(unittest.TestCase):
    def test_nonunit_failure_compresses_to_pair_product_radical(self) -> None:
        state = nonunit_pcc_failure_pair_radical_state(3, 125, 128, 1, 10)
        self.assertIsNotNone(state)
        assert state is not None
        self.assertEqual(state.component_values, (128, 125))
        self.assertEqual(state.component_product, 16_000)
        self.assertEqual(state.residual_product, 1_600)
        self.assertEqual(state.radical_product, 10)
        self.assertEqual(state.radical_product * state.residual_product, state.component_product)

    def test_unit_failure_reduces_to_one_small_radical_component(self) -> None:
        # Exact hard unit failure already used by Stage 50.
        result = unit_pcc_failure_small_radical_component(
            1, 239**2, 2 * 13**4, 3, 5
        )
        self.assertIsNotNone(result)
        assert result is not None
        n, radical_n = result
        self.assertIn(n, (239**2, 2 * 13**4))
        self.assertGreater(radical_n, 0)

    def test_pcc_debruijn_power_is_one_minus_eta(self) -> None:
        self.assertEqual(pcc_debruijn_failure_power(3, 5), Fraction(2, 5))
        self.assertEqual(pcc_debruijn_failure_power(1, 10), Fraction(9, 10))

    def test_classical_global_radical_selector_is_strictly_stronger(self) -> None:
        for M_num, M_den in ((2, 1), (3, 2), (11, 10), (10, 3)):
            self.assertTrue(classical_selector_strictly_beats_pcc_route(M_num, M_den))
            self.assertEqual(
                oesterle_via_pcc_debruijn_limit_power(M_num, M_den),
                Fraction(M_den, M_num),
            )
            self.assertEqual(
                classical_debruijn_abc_limit_power(M_num, M_den),
                Fraction(2 * M_den, 3 * M_num),
            )


if __name__ == "__main__":
    unittest.main()
