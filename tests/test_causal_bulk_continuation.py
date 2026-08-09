import unittest

from enterprise_math.causal_bulk_continuation import (
    BulkContinuationLaw,
    BulkContinuationState,
    base_carry_continuation_law,
    exact_sum_from_carry_state,
    run,
    singleton_accumulator_law,
)
from enterprise_math.causal_close_packing_stack import next_orientation


class CausalBulkContinuationTests(unittest.TestCase):
    def test_pure_sum_has_one_structural_type(self):
        law = singleton_accumulator_law((0, 1, 2, 3))
        final = run(BulkContinuationState(0, "unit"), (2, 1, 3, 0, 2), law)
        self.assertEqual(final.bulk, 8)
        self.assertEqual(final.continuation, "unit")

    def test_base_carry_is_bulk_plus_residue_structure(self):
        for base, digits in (
            (2, (1, 1, 1, 0, 1)),
            (3, (2, 1, 2, 2, 0)),
            (5, (4, 4, 1, 3)),
        ):
            law = base_carry_continuation_law(base)
            final = run(BulkContinuationState(0, 0), digits, law)
            self.assertEqual(exact_sum_from_carry_state(final, base), sum(digits))

    def test_pair_grade_uses_finite_structural_type_plus_integer_bulk(self):
        # Continuation type remembers only the previous bit; bulk accumulates an
        # exact pair grade.  No full word history is stored.
        types = (0, 1)
        symbols = (0, 1)
        law = BulkContinuationLaw(
            symbols=symbols,
            types=types,
            next_type={(tau, symbol): symbol for tau in types for symbol in symbols},
            increment={
                (tau, symbol): (5 if tau == symbol else -2)
                for tau in types
                for symbol in symbols
            },
            combine_bulk=lambda bulk, inc: bulk + inc,
        )
        word = (1, 1, 0, 1, 0, 0)
        # First symbol is used to seed the structural type; subsequent symbols
        # complete one pair window each.
        final = run(BulkContinuationState(0, word[0]), word[1:], law)
        expected = sum(5 if a == b else -2 for a, b in zip(word, word[1:]))
        self.assertEqual(final.bulk, expected)
        self.assertEqual(final.continuation, word[-1])

    def test_close_packing_relative_orientation_is_same_schema(self):
        types = (-1, 1)
        modes = ("c", "h")
        law = BulkContinuationLaw(
            symbols=modes,
            types=types,
            next_type={
                (orientation, mode): next_orientation(orientation, mode)
                for orientation in types
                for mode in modes
            },
            increment={(orientation, mode): 0 for orientation in types for mode in modes},
            combine_bulk=lambda bulk, inc: bulk + inc,
        )
        final = run(
            BulkContinuationState(0, 1),
            ("c", "c", "h", "c", "h"),
            law,
        )
        expected_orientation = 1
        for mode in ("c", "c", "h", "c", "h"):
            expected_orientation = next_orientation(expected_orientation, mode)
        self.assertEqual(final.continuation, expected_orientation)
        self.assertEqual(final.bulk, 0)

    def test_max_saturation_can_live_entirely_in_bulk_channel(self):
        tau = "no-structure"
        symbols = (0, 1, 2, 3, 4, 5)
        law = BulkContinuationLaw(
            symbols=symbols,
            types=(tau,),
            next_type={(tau, symbol): tau for symbol in symbols},
            increment={(tau, symbol): symbol for symbol in symbols},
            combine_bulk=max,
        )
        final = run(BulkContinuationState(0, tau), (1, 5, 2, 4, 3), law)
        self.assertEqual(final, BulkContinuationState(5, tau))


if __name__ == "__main__":
    unittest.main()
