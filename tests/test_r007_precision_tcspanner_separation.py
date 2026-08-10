from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "experiments" / "r007_precision_tcspanner_separation.py"
spec = importlib.util.spec_from_file_location("r007_precision_tcspanner_separation", MODULE_PATH)
assert spec is not None and spec.loader is not None
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class R007PrecisionTCSpannerSeparationTests(unittest.TestCase):
    def test_repair_is_coarsest_stable_refinement_on_small_systems(self) -> None:
        systems = (
            (
                (0, 0, 1, 2),
                ((1, 2, 3, 3),),
            ),
            (
                (0, 0, 1, 1),
                ((1, 0, 3, 2), (2, 3, 0, 1)),
            ),
            (
                (0, 1, 1, 2),
                ((0, 0, 1, 2), (1, 2, 3, 0)),
            ),
        )
        for observation, operations in systems:
            repair = mod.repair_partition(observation, operations)
            self.assertTrue(mod.partition_refines(repair, observation))
            self.assertTrue(mod.stable_partition(repair, operations))
            for partition in mod.all_partitions(len(observation)):
                if (
                    mod.partition_refines(partition, observation)
                    and mod.stable_partition(partition, operations)
                ):
                    self.assertTrue(mod.partition_refines(partition, repair))

    def test_projecting_a_tc_spanner_along_stable_quotient_preserves_depth(self) -> None:
        operations = ((1, 2, 3, 3),)
        fine = (0, 1, 2, 3)
        coarse = (0, 1, 1, 1)
        self.assertTrue(mod.stable_partition(fine, operations))
        self.assertTrue(mod.stable_partition(coarse, operations))
        for k in (1, 2, 3):
            fine_n, fine_graph = mod.quotient_transition_graph(fine, operations)
            spanner = mod.minimum_k_tc_spanner(fine_n, fine_graph, k)
            projected = mod.project_tc_spanner(operations, fine, coarse, spanner, k)
            coarse_n, coarse_graph = mod.quotient_transition_graph(coarse, operations)
            self.assertTrue(mod.is_k_tc_spanner(coarse_n, coarse_graph, projected, k))
            self.assertLessEqual(len(projected), len(spanner))

    def test_coarsest_stable_repair_minimizes_small_exact_tc_spanner_sizes(self) -> None:
        systems = (
            ((0, 0, 1, 2), ((1, 2, 3, 3),)),
            ((0, 0, 1, 1), ((1, 0, 3, 2), (2, 3, 0, 1))),
        )
        for observation, operations in systems:
            repair = mod.repair_partition(observation, operations)
            coarse_n, coarse_graph = mod.quotient_transition_graph(repair, operations)
            for k in (1, 2, 3):
                coarse_size = len(mod.minimum_k_tc_spanner(coarse_n, coarse_graph, k))
                for fine in mod.all_partitions(len(observation)):
                    if (
                        mod.partition_refines(fine, repair)
                        and mod.stable_partition(fine, operations)
                    ):
                        fine_n, fine_graph = mod.quotient_transition_graph(fine, operations)
                        fine_size = len(mod.minimum_k_tc_spanner(fine_n, fine_graph, k))
                        self.assertLessEqual(coarse_size, fine_size)

    def test_directed_line_endpoints_match_full_closure_and_hasse_basis(self) -> None:
        n = 6
        path = frozenset((i, i + 1) for i in range(n - 1))
        one_step = mod.minimum_k_tc_spanner(n, path, 1)
        hasse_depth = mod.minimum_k_tc_spanner(n, path, n - 1)
        self.assertEqual(len(one_step), n * (n - 1) // 2)
        self.assertEqual(len(hasse_depth), n - 1)
        self.assertEqual(len(mod.minimum_k_tc_spanner(n, path, 2)), 8)

    def test_divisor_box_interval_count_equals_cap_shift_semantic_count(self) -> None:
        for exponents in ((1,), (3,), (1, 1, 1), (2, 3), (1, 2, 4)):
            comparable = mod.comparable_pair_count_for_box(exponents)
            macros = mod.cap_shift_semantic_count(exponents)
            self.assertEqual(comparable, macros)
            self.assertGreaterEqual(comparable, mod.state_count_for_box(exponents))


if __name__ == "__main__":
    unittest.main()
