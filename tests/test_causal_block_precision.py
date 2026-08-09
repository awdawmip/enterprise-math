import unittest

from enterprise_math.causal_block_precision import (
    add_block_precision_states,
    block_precision_state,
    complete_block_collapse,
    nested_block_projection_is_exact,
    regroup_block_state,
)


class CausalBlockPrecisionTests(unittest.TestCase):
    def test_p008_linear_complete_growth_is_floor_block_completion(self):
        for capacity in range(1, 8):
            for units in range(20):
                state = block_precision_state(units, capacity)
                self.assertEqual(state.complete_blocks, units // capacity)
                self.assertEqual(state.detail_units, units % capacity)
                self.assertEqual(state.exact_units, units)
                self.assertEqual(
                    complete_block_collapse(units, capacity),
                    capacity * (units // capacity),
                )

    def test_nested_real_block_grouping_generates_divisibility_projection_chain(self):
        for fine in (1, 2, 3, 4):
            for multiplier in (1, 2, 3, 5):
                coarse = fine * multiplier
                for units in range(30):
                    self.assertTrue(
                        nested_block_projection_is_exact(units, fine, coarse)
                    )

    def test_detail_addition_generates_exact_carry(self):
        left = block_precision_state(17, 5)   # 3 blocks + 2 detail
        right = block_precision_state(14, 5)  # 2 blocks + 4 detail
        result, carry = add_block_precision_states(left, right)
        self.assertEqual(carry, 1)
        self.assertEqual(result.complete_blocks, 6)
        self.assertEqual(result.detail_units, 1)
        self.assertEqual(result.exact_units, 31)

    def test_no_carry_when_details_do_not_complete_a_block(self):
        left = block_precision_state(11, 5)   # detail 1
        right = block_precision_state(12, 5)  # detail 2
        result, carry = add_block_precision_states(left, right)
        self.assertEqual(carry, 0)
        self.assertEqual(result.detail_units, 3)
        self.assertEqual(result.exact_units, 23)

    def test_regrouping_keeps_exact_value_but_changes_complete_block_view(self):
        state = block_precision_state(23, 2)
        coarse = regroup_block_state(state, 6)
        self.assertEqual(coarse.exact_units, 23)
        self.assertEqual(coarse.complete_blocks, 3)
        self.assertEqual(coarse.detail_units, 5)

    def test_non_nested_scale_is_not_a_causal_block_regrouping(self):
        state = block_precision_state(17, 4)
        with self.assertRaises(ValueError):
            regroup_block_state(state, 6)


if __name__ == "__main__":
    unittest.main()
