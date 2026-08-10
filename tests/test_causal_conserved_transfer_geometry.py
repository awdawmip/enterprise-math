import unittest
from itertools import permutations, product

from enterprise_math.causal_conserved_transfer_geometry import (
    a3_primitive_images,
    a3_to_d3_fcc,
    a_flag_extension_count,
    a_full_rank_flag_law,
    apply_transfer_plan,
    d3_fcc_to_a3,
    is_d3_fcc_state,
    is_primitive_conserved_unit_transfer,
    minimum_transfer_plan,
    primitive_transfer,
    primitive_transfers,
    transfer_distance,
    zero_sum_basis,
    zero_sum_relation_rank,
)


class CausalConservedTransferGeometryTests(unittest.TestCase):
    def test_all_primitive_moves_are_exactly_one_donor_one_receiver(self):
        for slots in range(2, 7):
            roots = primitive_transfers(slots)
            self.assertEqual(len(roots), slots * (slots - 1))
            self.assertEqual(len(set(roots)), len(roots))
            self.assertTrue(all(is_primitive_conserved_unit_transfer(root) for root in roots))

    def test_one_transfer_orbit_under_full_slot_permutation_is_all_a_roots(self):
        for slots in range(2, 6):
            seed = primitive_transfer(slots, receiver=0, donor=1)
            orbit = set()
            for permutation in permutations(range(slots)):
                image = [0] * slots
                for old_index, value in enumerate(seed):
                    image[permutation[old_index]] = value
                orbit.add(tuple(image))
            self.assertEqual(orbit, set(primitive_transfers(slots)))

    def test_zero_sum_basis_has_rank_slots_minus_one_and_spans_all_small_states(self):
        for slots in range(2, 6):
            basis = zero_sum_basis(slots)
            self.assertEqual(len(basis), zero_sum_relation_rank(slots))
            self.assertEqual(len(basis), slots - 1)
            for vector in product(range(-2, 3), repeat=slots):
                if sum(vector) != 0:
                    continue
                rebuilt = [0] * slots
                for coefficient, basis_vector in zip(vector[:-1], basis):
                    for index, value in enumerate(basis_vector):
                        rebuilt[index] += coefficient * value
                self.assertEqual(tuple(rebuilt), vector)

    def test_transfer_distance_is_attained_by_constructive_unit_plan(self):
        cases = (
            ((3, 0, 0, 0), (0, 1, 1, 1)),
            ((0, 4, 1, 0), (2, 0, 1, 2)),
            ((5, 2, 3), (1, 6, 3)),
            ((1, 1, 1, 1), (1, 1, 1, 1)),
        )
        for left, right in cases:
            plan = minimum_transfer_plan(left, right)
            self.assertEqual(len(plan), transfer_distance(left, right))
            self.assertEqual(apply_transfer_plan(left, plan), right)
            self.assertEqual(
                transfer_distance(left, right),
                sum(abs(a - b) for a, b in zip(left, right)) // 2,
            )

    def test_no_shorter_plan_can_exist_by_surplus_lower_bound(self):
        left = (7, 0, 2, 1)
        right = (1, 3, 3, 3)
        distance = transfer_distance(left, right)
        total_deficit = sum(max(0, target - source) for source, target in zip(left, right))
        self.assertEqual(distance, total_deficit)
        self.assertEqual(distance, 6)

    def test_full_rank_a_flag_law_is_closed_and_uniform(self):
        expected = {
            1: (0,),
            2: (2, 0),
            3: (4, 1, 0),
            4: (6, 2, 1, 0),
            5: (8, 3, 2, 1, 0),
            6: (10, 4, 3, 2, 1, 0),
        }
        for p, law in expected.items():
            self.assertEqual(a_full_rank_flag_law(p), law)
            self.assertEqual(len(law), p)
            for size, continuation in enumerate(law, start=1):
                self.assertEqual(a_flag_extension_count(p, size), continuation)

    def test_dimension_is_relation_slots_minus_one_conservation_law(self):
        for p in range(1, 8):
            self.assertEqual(zero_sum_relation_rank(p + 1), p)

    def test_a3_to_d3_fcc_map_is_integer_bijection_on_small_states(self):
        for state in product(range(-2, 3), repeat=4):
            if sum(state) != 0:
                continue
            image = a3_to_d3_fcc(state)
            self.assertTrue(is_d3_fcc_state(image))
            self.assertEqual(d3_fcc_to_a3(image), state)

        for state in product(range(-3, 4), repeat=3):
            if not is_d3_fcc_state(state):
                continue
            image = d3_fcc_to_a3(state)
            self.assertEqual(a3_to_d3_fcc(image), state)

    def test_a3_primitive_transfers_map_exactly_to_twelve_d3_fcc_nearest_moves(self):
        images = set(a3_primitive_images())
        expected = set()
        for zero_index in range(3):
            other = [index for index in range(3) if index != zero_index]
            for left_sign in (-1, 1):
                for right_sign in (-1, 1):
                    vector = [0, 0, 0]
                    vector[other[0]] = left_sign
                    vector[other[1]] = right_sign
                    expected.add(tuple(vector))
        self.assertEqual(len(images), 12)
        self.assertEqual(images, expected)


if __name__ == "__main__":
    unittest.main()
