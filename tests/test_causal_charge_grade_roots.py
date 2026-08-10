import unittest
from itertools import product

from enterprise_math.causal_charge_grade_roots import (
    a_minimum_grade,
    absolute_event_mass,
    conserved_transfer_mass,
    d_minimum_grade,
    is_a_minimum_grade_move,
    is_d_minimum_grade_move,
    is_e6_minimum_grade_move,
    is_e7_minimum_grade_move,
    is_scaled_bcc_minimum_grade_move,
    is_scaled_e8_minimum_grade_move,
    quadratic_grade,
    scaled_bcc_minimum_grade,
    scaled_bcc_minimum_grade_moves,
    scaled_e8_grade_lower_bound_reason,
    scaled_e8_minimum_grade,
    support_size_histogram,
    transfer_mass_histogram,
)
from enterprise_math.causal_charge_kernel_geometry import (
    in_a_kernel,
    in_d_kernel,
    in_scaled_bcc_charge_kernel,
    in_scaled_e8_charge_kernel,
)
from enterprise_math.causal_primitive_link_profile import (
    a_roots,
    d_roots,
    e6_scaled_roots,
    e7_scaled_roots,
    e8_scaled_roots,
    primitive_link_profile,
)


class CausalChargeGradeRootsTests(unittest.TestCase):
    def test_a_roots_are_exactly_grade_two_events_in_exact_total_kernel(self):
        for p in range(1, 6):
            roots = set(a_roots(p))
            discovered = set()
            for vector in product((-1, 0, 1), repeat=p + 1):
                if any(vector) and in_a_kernel(vector) and quadratic_grade(vector) == a_minimum_grade():
                    discovered.add(vector)
            self.assertEqual(discovered, roots)
            self.assertTrue(all(is_a_minimum_grade_move(root) for root in roots))
            self.assertEqual(transfer_mass_histogram(tuple(roots)), {1: len(roots)})
            self.assertEqual(support_size_histogram(tuple(roots)), {2: len(roots)})

    def test_d_roots_are_exactly_grade_two_events_in_parity_kernel(self):
        for rank in range(3, 7):
            roots = set(d_roots(rank))
            discovered = set()
            for vector in product((-1, 0, 1), repeat=rank):
                if any(vector) and in_d_kernel(vector) and quadratic_grade(vector) == d_minimum_grade():
                    discovered.add(vector)
            self.assertEqual(discovered, roots)
            self.assertTrue(all(is_d_minimum_grade_move(root) for root in roots))
            self.assertEqual(support_size_histogram(tuple(roots)), {2: len(roots)})
            self.assertEqual({absolute_event_mass(root) for root in roots}, {2})

    def test_scaled_bcc_is_minimum_quadratic_shell_of_same_parity_code(self):
        roots = set(scaled_bcc_minimum_grade_moves())
        self.assertEqual(len(roots), 8)
        self.assertEqual(scaled_bcc_minimum_grade(), 3)
        self.assertTrue(all(in_scaled_bcc_charge_kernel(root) for root in roots))
        self.assertTrue(all(is_scaled_bcc_minimum_grade_move(root) for root in roots))
        self.assertEqual({quadratic_grade(root) for root in roots}, {3})
        discovered = {
            vector
            for vector in product(range(-2, 3), repeat=3)
            if any(vector)
            and in_scaled_bcc_charge_kernel(vector)
            and quadratic_grade(vector) == 3
        }
        self.assertEqual(discovered, roots)

    def test_scaled_bcc_direction_link_is_edgeless_despite_eight_equal_grade_directions(self):
        profile = primitive_link_profile(scaled_bcc_minimum_grade_moves())
        self.assertEqual(profile.primitive_count, 8)
        self.assertEqual(profile.link_degree_histogram, ((0, 8),))
        self.assertEqual(profile.link_edge_count, 0)
        self.assertEqual(profile.link_component_sizes, (1, 1, 1, 1, 1, 1, 1, 1))

    def test_scaled_e8_roots_are_exactly_minimum_grade_code_events(self):
        roots = set(e8_scaled_roots())
        self.assertEqual(scaled_e8_minimum_grade(), 8)
        self.assertEqual(len(roots), 240)
        self.assertTrue(all(is_scaled_e8_minimum_grade_move(root) for root in roots))
        self.assertEqual({quadratic_grade(root) for root in roots}, {8})
        self.assertEqual(support_size_histogram(tuple(roots)), {2: 112, 8: 128})
        self.assertEqual({absolute_event_mass(root) for root in roots}, {4, 8})

        examples = (
            (2, -2, 0, 0, 0, 0, 0, 0),
            (1, 1, 1, 1, 1, 1, 1, 1),
            (-1, -1, 1, 1, 1, 1, 1, 1),
        )
        for vector in examples:
            reason, lower_bound = scaled_e8_grade_lower_bound_reason(vector)
            self.assertEqual(lower_bound, 8)
            self.assertNotEqual(reason, "zero")

    def test_no_nonzero_scaled_e8_code_vector_can_have_grade_below_eight(self):
        found = []

        def search(prefix, remaining_slots, remaining_grade):
            if remaining_slots == 0:
                vector = tuple(prefix)
                if any(vector) and in_scaled_e8_charge_kernel(vector):
                    found.append(vector)
                return
            for value in (-2, -1, 0, 1, 2):
                square = value * value
                if square >= remaining_grade:
                    continue
                search(prefix + [value], remaining_slots - 1, remaining_grade - square)

        search([], 8, 8)
        self.assertEqual(found, [])

    def test_e7_and_e6_roots_are_exact_charge_sections_of_same_grade_eight_code(self):
        e7 = tuple(e7_scaled_roots())
        e6 = tuple(e6_scaled_roots())
        self.assertEqual({root for root in e8_scaled_roots() if is_e7_minimum_grade_move(root)}, set(e7))
        self.assertEqual({root for root in e8_scaled_roots() if is_e6_minimum_grade_move(root)}, set(e6))
        self.assertEqual(len(e7), 126)
        self.assertEqual(len(e6), 72)
        self.assertEqual(transfer_mass_histogram(e7), {2: 56, 4: 70})
        self.assertEqual(transfer_mass_histogram(e6), {2: 32, 4: 40})
        self.assertEqual(support_size_histogram(e7), {2: 56, 8: 70})
        self.assertEqual(support_size_histogram(e6), {2: 32, 8: 40})

    def test_equal_quadratic_grade_does_not_imply_equal_unit_transfer_cost(self):
        e7 = e7_scaled_roots()
        self.assertEqual({quadratic_grade(root) for root in e7}, {8})
        self.assertEqual(set(transfer_mass_histogram(e7)), {2, 4})
        self.assertNotEqual(len(transfer_mass_histogram(e7)), 1)


if __name__ == "__main__":
    unittest.main()
