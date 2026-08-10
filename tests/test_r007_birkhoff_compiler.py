from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest


MODULE_PATH = Path(__file__).parents[1] / "experiments" / "r007_birkhoff_compiler.py"
spec = importlib.util.spec_from_file_location("r007_birkhoff_compiler", MODULE_PATH)
assert spec is not None and spec.loader is not None
bc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(bc)


class TestR007BirkhoffCompiler(unittest.TestCase):
    def test_frontier_compile_depth_and_antichain_spectrum(self) -> None:
        for size in range(0, 5):
            forward = [(i, j) for i in range(size) for j in range(i + 1, size)]
            seen = set()
            for raw_mask in range(1 << len(forward)):
                relations = [
                    pair for index, pair in enumerate(forward)
                    if raw_mask & (1 << index)
                ]
                order = bc.transitive_closure(size, relations)
                if order in seen:
                    continue
                seen.add(order)
                lowers = bc.lower_sets(size, order)
                for mask in lowers:
                    program = bc.compile_mask(size, order, mask)
                    self.assertEqual(bc.execute_program(size, order, program), mask)
                    self.assertEqual(len(program), len(bc.mask_frontier(size, order, mask)))
                    for depth in range(len(program)):
                        for shorter in __import__("itertools").combinations(range(size), depth):
                            self.assertNotEqual(
                                bc.execute_program(size, order, shorter), mask
                            )
                self.assertEqual(
                    bc.depth_spectrum(size, order),
                    bc.antichain_spectrum(size, order),
                )
                self.assertEqual(
                    max(bc.depth_spectrum(size, order), default=0),
                    bc.width(size, order),
                )

    def test_sharp_ideal_count_bounds(self) -> None:
        for size in range(1, 10):
            for width in range(1, size + 1):
                lower, upper = bc.ideal_count_extremal_bounds(size, width)
                low_order = bc.lower_extremizer(size, width)
                high_order = bc.upper_extremizer(size, width)
                self.assertEqual(bc.width(size, low_order), width)
                self.assertEqual(bc.width(size, high_order), width)
                self.assertEqual(len(bc.lower_sets(size, low_order)), lower)
                self.assertEqual(len(bc.lower_sets(size, high_order)), upper)

    def test_disjoint_chain_factor_shape_bounds(self) -> None:
        for size in range(1, 10):
            for width in range(1, size + 1):
                lower, upper = bc.disjoint_chain_ideal_count_bounds(size, width)
                balanced = bc.upper_extremizer(size, width)
                self.assertEqual(len(bc.lower_sets(size, balanced)), upper)
                skew_lengths = [size - width + 1] + [1] * (width - 1)
                relations = set()
                start = 0
                for length in skew_lengths:
                    chain = list(range(start, start + length))
                    for i, a in enumerate(chain):
                        for b in chain[i + 1 :]:
                            relations.add((a, b))
                    start += length
                skew = bc.transitive_closure(size, relations)
                self.assertEqual(bc.width(size, skew), width)
                self.assertEqual(len(bc.lower_sets(size, skew)), lower)

    def test_language_envelope_recovers_all_one_step_and_words(self) -> None:
        size = 5
        order = bc.transitive_closure(size, {(0, 2), (1, 2), (2, 4), (3, 4)})
        lowers = bc.lower_sets(size, order)
        for state in lowers:
            for a in lowers:
                for b in lowers:
                    masks = (a, b)
                    envelope = bc.language_envelope(masks)
                    visible = bc.project(state, envelope)
                    signature = bc.one_step_signature(state, masks)
                    self.assertEqual(signature, tuple(bc.project(visible, m) for m in masks))
                    self.assertEqual(
                        visible,
                        frozenset().union(*signature),
                    )
                    self.assertEqual(
                        bc.composite_projection(state, masks),
                        bc.project(visible, frozenset(a & b)),
                    )


if __name__ == "__main__":
    unittest.main()
