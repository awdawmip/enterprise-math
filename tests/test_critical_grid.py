import unittest

from enterprise_math.core import collapse
from enterprise_math.critical_grid import (
    bifurcated_pair_map,
    cancellation_example,
    common_prefix_reduction,
    common_suffix_reduction,
    compose_adjacent_pairs,
    operation_family_difference,
    rectangle_endpoint_pairs,
    rectangle_holonomy,
    rectangle_holonomy_decompositions,
    rectangle_variation_identity,
)


class CriticalGridTests(unittest.TestCase):
    def test_adjacent_pair_composition(self) -> None:
        self.assertEqual(compose_adjacent_pairs(("a", "b"), ("b", "c")), ("a", "c"))
        with self.assertRaises(ValueError):
            compose_adjacent_pairs(("a", "b"), ("x", "c"))

    def test_bifurcated_pair_map(self) -> None:
        self.assertEqual(
            bifurcated_pair_map(lambda x: x + 1, lambda x: x * 2, (3, 4)),
            (4, 8),
        )

    def test_endpoint_pair_interchange_on_generic_states(self) -> None:
        f0 = lambda x: f"{x}L"
        f1 = lambda x: f"{x}R"
        g0 = lambda y: f"top({y})"
        g1 = lambda y: f"bottom({y})"
        for state in ["s", "t", "u"]:
            outer, route_one, route_two = rectangle_endpoint_pairs(f0, f1, g0, g1, state)
            self.assertEqual(outer, route_one)
            self.assertEqual(outer, route_two)

    def test_numeric_rectangle_decompositions_exhaustive_small_domain(self) -> None:
        first_families = [
            (lambda x: x, lambda x: x + 1),
            (lambda x: x // 2, lambda x: (x + 3) // 2),
            (lambda x: collapse(x, 2), lambda x: collapse(x + 2, 2)),
        ]
        second_families = [
            (lambda y: y, lambda y: y + 2),
            (lambda y: y // 2, lambda y: y // 3),
            (lambda y: collapse(y, 2), lambda y: collapse(y, 3)),
        ]
        for f0, f1 in first_families:
            for g0, g1 in second_families:
                for state in range(0, 101):
                    outer, route_one, route_two = rectangle_holonomy_decompositions(
                        f0, f1, g0, g1, state
                    )
                    self.assertEqual(outer, route_one)
                    self.assertEqual(outer, route_two)

    def test_rectangle_variation_identity(self) -> None:
        f0 = lambda x: x // 2
        f1 = lambda x: (x + 5) // 3
        g0 = lambda y: collapse(y, 2)
        g1 = lambda y: collapse(y, 3)
        for state in range(0, 250):
            left, right = rectangle_variation_identity(f0, f1, g0, g1, state)
            self.assertEqual(left, right)

    def test_common_suffix_reduces_to_response(self) -> None:
        f0 = lambda x: x
        f1 = lambda x: x + 3
        suffix = lambda y: collapse(y, 2)
        for state in range(0, 100):
            self.assertEqual(*common_suffix_reduction(f0, f1, suffix, state))

    def test_common_prefix_reduces_to_pointwise_family_difference(self) -> None:
        prefix = lambda x: x // 2
        g0 = lambda y: collapse(y, 2)
        g1 = lambda y: collapse(y, 3)
        for state in range(0, 100):
            self.assertEqual(*common_prefix_reduction(prefix, g0, g1, state))

    def test_zero_outer_does_not_force_zero_local_defects(self) -> None:
        for state in range(1, 50):
            example = cancellation_example(state)
            self.assertEqual(example["outer"], 0)
            self.assertNotEqual(example["first_displacement"], 0)
            self.assertNotEqual(example["g_defect_at_f1"], 0)

    def test_collapse_commuting_case_is_zero_outer_holonomy(self) -> None:
        # P003 comparable exponents: both paths C2∘C4 and C4∘C2 agree.
        first_left = lambda x: collapse(x, 4)
        first_right = lambda x: collapse(x, 2)
        second_left = lambda y: collapse(y, 2)
        second_right = lambda y: collapse(y, 4)
        for state in range(0, 500):
            self.assertEqual(
                rectangle_holonomy(
                    first_left, first_right, second_left, second_right, state
                ),
                0,
            )

    def test_incomparable_collapse_exponents_expose_nonzero_outer_holonomy(self) -> None:
        first_left = lambda x: collapse(x, 3)
        first_right = lambda x: collapse(x, 2)
        second_left = lambda y: collapse(y, 2)
        second_right = lambda y: collapse(y, 3)
        self.assertNotEqual(
            rectangle_holonomy(first_left, first_right, second_left, second_right, 8),
            0,
        )

    def test_operation_family_difference_orientation(self) -> None:
        self.assertEqual(operation_family_difference(lambda y: y + 3, lambda y: y, 10), -3)


if __name__ == "__main__":
    unittest.main()
