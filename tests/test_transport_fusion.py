import unittest
from itertools import product

from enterprise_math.transport_fusion import (
    binary_carry_field_budget,
    carry_detail_state,
    carry_token_alone_is_not_composable_witness,
    combine_carry_detail,
    fold_carry_detail,
    fused_carry_savings_lower_bound,
    nary_addition_transport_bit_cost,
    nary_addition_transport_capacity,
    total_carry,
)


class TransportFusionTests(unittest.TestCase):
    def test_nary_capacity_matches_exhaustive_residue_outputs(self) -> None:
        for radix in range(2, 7):
            for arity in range(1, 7):
                observed = {
                    sum(residues) // radix
                    for residues in product(range(radix), repeat=arity)
                }
                self.assertEqual(
                    len(observed),
                    nary_addition_transport_capacity(radix, arity),
                )
                self.assertEqual(observed, set(range(max(observed) + 1)))

    def test_total_carry_is_exact_one_shot_token(self) -> None:
        for radix in range(2, 12):
            for residues in product(range(radix), repeat=4):
                carry, detail = carry_detail_state(radix, residues)
                self.assertEqual(carry, total_carry(radix, residues))
                self.assertEqual(
                    radix * carry + detail,
                    sum(residues),
                )

    def test_carry_detail_composition_is_associative(self) -> None:
        for radix in range(2, 10):
            states = tuple((carry, detail) for carry in range(4) for detail in range(radix))
            for left, middle, right in product(states, repeat=3):
                self.assertEqual(
                    combine_carry_detail(
                        radix,
                        combine_carry_detail(radix, left, middle),
                        right,
                    ),
                    combine_carry_detail(
                        radix,
                        left,
                        combine_carry_detail(radix, middle, right),
                    ),
                )

    def test_folding_single_residues_recovers_direct_euclidean_state(self) -> None:
        for radix in range(2, 10):
            for residues in product(range(radix), repeat=5):
                singleton_states = tuple((0, residue) for residue in residues)
                self.assertEqual(
                    fold_carry_detail(radix, singleton_states),
                    carry_detail_state(radix, residues),
                )

    def test_tree_grouping_does_not_change_final_transport_state(self) -> None:
        for radix in range(2, 10):
            for residues in product(range(radix), repeat=4):
                a, b, c, d = ((0, residue) for residue in residues)
                left_grouped = combine_carry_detail(
                    radix,
                    combine_carry_detail(radix, a, b),
                    combine_carry_detail(radix, c, d),
                )
                right_grouped = combine_carry_detail(
                    radix,
                    a,
                    combine_carry_detail(
                        radix,
                        b,
                        combine_carry_detail(radix, c, d),
                    ),
                )
                self.assertEqual(left_grouped, right_grouped)

    def test_total_carry_fixed_width_is_never_worse_than_separate_binary_fields(self) -> None:
        for radix in range(2, 50):
            for arity in range(1, 100):
                self.assertLessEqual(
                    nary_addition_transport_bit_cost(radix, arity),
                    binary_carry_field_budget(arity),
                )
                self.assertGreaterEqual(
                    fused_carry_savings_lower_bound(radix, arity),
                    0,
                )

    def test_carry_token_alone_is_not_recursively_composable(self) -> None:
        for radix in range(2, 50):
            witness = carry_token_alone_is_not_composable_witness(radix)
            self.assertEqual(witness["left_first"][0], witness["left_second"][0])
            self.assertNotEqual(
                witness["combined_first_carry"],
                witness["combined_second_carry"],
            )

    def test_capacity_is_linear_not_binary_tree_exponential(self) -> None:
        for radix in range(2, 20):
            for arity in range(2, 20):
                capacity = nary_addition_transport_capacity(radix, arity)
                self.assertLessEqual(capacity, arity)
                self.assertLess(capacity, 2 ** (arity - 1))


if __name__ == "__main__":
    unittest.main()
