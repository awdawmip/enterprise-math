import itertools
import unittest

from enterprise_math.lego_additive_operation import (
    additive_operation_preserves_composition,
    apply_additive_operation,
    apply_integer_matrix,
    compile_additive_operation,
    nonnegative_unit_images,
    unit_images_from_matrix,
)


class LegoAdditiveOperationTests(unittest.TestCase):
    def test_matrix_is_exactly_the_table_of_unit_images(self):
        images = (
            (1, 2),
            (3, -1),
            (0, 4),
        )
        matrix = compile_additive_operation(images)
        self.assertEqual(
            matrix,
            (
                (1, 3, 0),
                (2, -1, 4),
            ),
        )
        self.assertEqual(unit_images_from_matrix(matrix), images)

    def test_operation_is_generated_by_unit_effects(self):
        images = (
            (1, 2),
            (3, -1),
            (0, 4),
        )
        state = (2, -3, 5)
        matrix = compile_additive_operation(images)
        self.assertEqual(
            apply_additive_operation(images, state),
            apply_integer_matrix(matrix, state),
        )
        # 2*T(e0) - 3*T(e1) + 5*T(e2)
        self.assertEqual(apply_additive_operation(images, state), (-7, 27))

    def test_compiled_operation_preserves_lego_composition_for_many_integer_states(self):
        images = (
            (2, 0, 1),
            (-1, 3, 0),
        )
        states = tuple(itertools.product(range(-2, 3), repeat=2))
        for left in states:
            for right in states:
                self.assertTrue(
                    additive_operation_preserves_composition(images, left, right)
                )

    def test_unsigned_lego_operations_are_exactly_nonnegative_unit_images(self):
        unsigned = ((1, 0), (2, 3))
        signed = ((1, -1), (2, 3))
        self.assertTrue(nonnegative_unit_images(unsigned))
        self.assertFalse(nonnegative_unit_images(signed))

    def test_one_unit_stays_one_only_when_the_declared_operation_maps_it_to_one_unit(self):
        # The framework does not impose conservation automatically. It exposes
        # the causal rule at the level of unit images, where conservation or
        # branching must be stated/proved rather than hidden inside a matrix.
        conservative = ((1, 0), (0, 1))
        branching = ((1, 1), (0, 1))
        self.assertEqual(apply_additive_operation(conservative, (1, 0)), (1, 0))
        self.assertEqual(apply_additive_operation(branching, (1, 0)), (1, 1))


if __name__ == "__main__":
    unittest.main()
