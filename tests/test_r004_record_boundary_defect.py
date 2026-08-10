import itertools
import unittest
from fractions import Fraction

from enterprise_math.r004_record_boundary_defect import (
    boundary_window_fraction,
    cyclic_window_counts,
    endpoint_flow_defect,
    flow_defect_from_block_counts,
    linear_record_flow_defect,
    linear_window_counts,
    periodically_closed_window_counts,
    periodic_wrap_blocks,
)


class R004RecordBoundaryDefectTests(unittest.TestCase):
    def test_endpoint_formula_matches_direct_flow_defect(self):
        record = (0, 1, 1, 0, 1, 0)
        for width in range(1, len(record) + 1):
            self.assertEqual(
                linear_record_flow_defect(record, width),
                endpoint_flow_defect(record, width),
            )

    def test_endpoint_defect_is_zero_when_boundary_words_match(self):
        record = (0, 1, 0, 1, 0)
        self.assertEqual(endpoint_flow_defect(record, 2), {})
        self.assertEqual(linear_record_flow_defect(record, 2), {})

    def test_nonzero_endpoint_defect_has_unit_source_and_sink(self):
        record = (0, 0, 1, 1, 0, 1)
        defect = endpoint_flow_defect(record, 3)
        self.assertEqual(defect, {(0, 0): 1, (0, 1): -1})
        self.assertEqual(sum(defect.values()), 0)
        self.assertEqual(sum(abs(value) for value in defect.values()), 2)

    def test_periodic_wrap_blocks_are_exactly_k_minus_one(self):
        record = (0, 1, 1, 0, 1)
        for width in range(1, len(record) + 1):
            wraps = periodic_wrap_blocks(record, width)
            self.assertEqual(len(wraps), width - 1)
            closed = periodically_closed_window_counts(record, width)
            self.assertEqual(closed, cyclic_window_counts(record, width))
            self.assertEqual(flow_defect_from_block_counts(closed), {})
            self.assertEqual(
                boundary_window_fraction(record, width),
                Fraction(width - 1, len(record)),
            )

    def test_linear_plus_wrap_counts_equal_cyclic_counts(self):
        record = (0, 0, 1, 0)
        width = 3
        linear = linear_window_counts(record, width)
        self.assertEqual(linear, {(0, 0, 1): 1, (0, 1, 0): 1})
        wraps = periodic_wrap_blocks(record, width)
        self.assertEqual(len(wraps), 2)
        self.assertEqual(
            periodically_closed_window_counts(record, width),
            cyclic_window_counts(record, width),
        )

    def test_endpoint_identity_exhaustive_for_small_binary_records(self):
        checked = 0
        for size in range(1, 8):
            for record in itertools.product((0, 1), repeat=size):
                for width in range(1, size + 1):
                    direct = linear_record_flow_defect(record, width)
                    closed_form = endpoint_flow_defect(record, width)
                    self.assertEqual(direct, closed_form)
                    self.assertEqual(
                        periodically_closed_window_counts(record, width),
                        cyclic_window_counts(record, width),
                    )
                    checked += 1
        self.assertEqual(checked, sum(size * (2**size) for size in range(1, 8)))

    def test_invalid_inputs_fail_closed(self):
        with self.assertRaises(ValueError):
            linear_window_counts((), 1)
        with self.assertRaises(ValueError):
            linear_window_counts((0, 1), 0)
        with self.assertRaises(ValueError):
            linear_window_counts((0, 1), 3)
        with self.assertRaises(ValueError):
            flow_defect_from_block_counts({})
        with self.assertRaises(ValueError):
            flow_defect_from_block_counts({(0,): 1, (0, 1): 1})
        with self.assertRaises(ValueError):
            flow_defect_from_block_counts({(0, 1): -1})


if __name__ == "__main__":
    unittest.main()
