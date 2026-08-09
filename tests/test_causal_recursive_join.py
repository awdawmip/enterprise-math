import unittest

from enterprise_math.causal_recursive_join import (
    compose_inventories,
    deterministic_join_kernel,
    fold_inventory,
    kernel_is_associative,
    singleton_inventory,
    three_way_left,
    three_way_right,
    typed_associativity_defect,
    unit_type_is_exact,
    xor_parity_kernel,
)


class CausalRecursiveJoinTests(unittest.TestCase):
    def test_parity_type_localizes_apparent_three_body_constraint(self):
        kernel = xor_parity_kernel()
        self.assertTrue(kernel_is_associative((0, 1), kernel))
        self.assertTrue(unit_type_is_exact(0, (0, 1), kernel))

        one_slot = {(0, 0): 1, (1, 0): 1}
        two = compose_inventories(one_slot, one_slot, kernel)
        three = compose_inventories(two, one_slot, kernel)

        # All four binary input combinations remain possible, but are compressed
        # to their continuation parity: two even, two odd.
        self.assertEqual(two, {(0, 0): 2, (1, 0): 2})
        # Eight triples split into four even and four odd.  Final acceptance of
        # parity zero therefore gives exactly the classic even-parity four-state
        # set without any ternary composition primitive.
        self.assertEqual(three, {(0, 0): 4, (1, 0): 4})

    def test_associative_kernel_gives_identical_three_way_bracketings(self):
        kernel = xor_parity_kernel()
        for first in (0, 1):
            for second in (0, 1):
                for third in (0, 1):
                    self.assertEqual(
                        three_way_left(first, second, third, kernel),
                        three_way_right(first, second, third, kernel),
                    )
        self.assertEqual(typed_associativity_defect((0, 1), kernel), {})

    def test_nonassociative_binary_law_produces_typed_three_body_defect(self):
        # Boolean NAND is not associative.
        types = (0, 1)
        operation = {
            (left, right): int(not (left and right))
            for left in types
            for right in types
        }
        kernel = deterministic_join_kernel(types, operation)
        self.assertFalse(kernel_is_associative(types, kernel))
        defect = typed_associativity_defect(types, kernel)
        self.assertTrue(defect)
        # At least one triple must have different exact continuation outcomes.
        triple, (left_only, right_only) = next(iter(defect.items()))
        self.assertEqual(len(triple), 3)
        self.assertTrue(left_only or right_only)

    def test_grade_shift_is_part_of_exact_associativity_not_a_posthoc_scalar(self):
        types = ("u",)
        associative = {("u", "u", "u", 1): 1}
        # Every binary join adds one grade, so both bracketings add two.
        self.assertTrue(kernel_is_associative(types, associative))
        self.assertEqual(
            three_way_left("u", "u", "u", associative),
            {("u", 2): 1},
        )

        # Same output type but bracket-sensitive grade law via an intermediate
        # type creates a real typed compatibility defect.
        types2 = ("a", "b")
        nonassoc = {
            ("a", "a", "b", 0): 1,
            ("b", "a", "a", 0): 1,
            ("a", "b", "a", 1): 1,
            ("b", "b", "b", 0): 1,
        }
        self.assertFalse(kernel_is_associative(types2, nonassoc))

    def test_four_slot_parity_fold_is_dimension_uniform(self):
        kernel = xor_parity_kernel()
        one_slot = {(0, 0): 1, (1, 0): 1}
        result = fold_inventory((one_slot, one_slot, one_slot, one_slot), kernel)
        self.assertEqual(result, {(0, 0): 8, (1, 0): 8})

    def test_exact_unit_is_structural_not_numeric_grade_value(self):
        # For XOR the even continuation type acts as the join unit.  Its grade is
        # zero because grade is an observation channel; this does not redefine
        # the project's primitive LEGO unit value 1.
        kernel = xor_parity_kernel()
        self.assertTrue(unit_type_is_exact(0, (0, 1), kernel))
        self.assertEqual(
            compose_inventories(singleton_inventory(0), singleton_inventory(1), kernel),
            singleton_inventory(1),
        )


if __name__ == "__main__":
    unittest.main()
