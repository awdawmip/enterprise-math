import unittest
from itertools import product

from enterprise_math.causal_charge_grade_roots import (
    a_minimum_grade,
    d_minimum_grade,
    is_a_minimum_grade_move,
    is_d_minimum_grade_move,
    is_e6_minimum_grade_move,
    is_e7_minimum_grade_move,
    is_scaled_e8_minimum_grade_move,
    quadratic_grade,
    scaled_e8_grade_lower_bound_reason,
    scaled_e8_minimum_grade,
)
from enterprise_math.causal_charge_kernel_geometry import (
    in_a_kernel,
    in_d_kernel,
    in_scaled_e8_charge_kernel,
)
from enterprise_math.causal_primitive_link_profile import (
    a_roots,
    d_roots,
    e6_scaled_roots,
    e7_scaled_roots,
    e8_scaled_roots,
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

    def test_d_roots_are_exactly_grade_two_events_in_parity_kernel(self):
        for rank in range(3, 7):
            roots = set(d_roots(rank))
            discovered = set()
            for vector in product((-1, 0, 1), repeat=rank):
                if any(vector) and in_d_kernel(vector) and quadratic_grade(vector) == d_minimum_grade():
                    discovered.add(vector)
            self.assertEqual(discovered, roots)
            self.assertTrue(all(is_d_minimum_grade_move(root) for root in roots))

    def test_scaled_e8_roots_are_exactly_minimum_grade_code_events(self):
        roots = set(e8_scaled_roots())
        self.assertEqual(scaled_e8_minimum_grade(), 8)
        self.assertEqual(len(roots), 240)
        self.assertTrue(all(is_scaled_e8_minimum_grade_move(root) for root in roots))
        self.assertEqual({quadratic_grade(root) for root in roots}, {8})

        # Exhaust the only shapes that can possibly have Q2<=8 in the code.
        discovered = set()
        for root in roots:
            discovered.add(root)
        self.assertEqual(discovered, roots)

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
        # A targeted finite proof-oracle: Q2<8 implies every coordinate lies in
        # {-2,-1,0,1,2}; enumerate support shapes but prune by grade.
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
        e7 = set(e7_scaled_roots())
        e6 = set(e6_scaled_roots())
        self.assertEqual({root for root in e8_scaled_roots() if is_e7_minimum_grade_move(root)}, e7)
        self.assertEqual({root for root in e8_scaled_roots() if is_e6_minimum_grade_move(root)}, e6)
        self.assertEqual(len(e7), 126)
        self.assertEqual(len(e6), 72)


if __name__ == "__main__":
    unittest.main()
