import importlib.util
import math
import random
import sys
import unittest
from fractions import Fraction
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "experiments" / "r026_collapse_external_benchmarks.py"
spec = importlib.util.spec_from_file_location("r026", MODULE_PATH)
r026 = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = r026
spec.loader.exec_module(r026)


class CollapsePrimitiveTests(unittest.TestCase):
    def test_unbiased_distance_rounding_preserves_expectation(self):
        x, step = 0.37, 0.125
        vals = []
        for i in range(20000):
            vals.append(r026.quantize_endpoint(x, step, "UNBIASED_DISTANCE_RANDOM", random.Random(i)))
        self.assertLess(abs(sum(vals) / len(vals) - x), 3e-3)

    def test_uniform_endpoint_is_biased_away_from_midpoint(self):
        x, step = 0.37, 0.125
        vals = [r026.quantize_endpoint(x, step, "UNIFORM_ENDPOINT_RANDOM", random.Random(i)) for i in range(20000)]
        self.assertGreater(abs(sum(vals) / len(vals) - x), 1e-2)

    def test_error_feedback_reconstructs_additive_total(self):
        xs = [0.01] * 1000
        ys, residual = r026.error_feedback_quantize(xs, 1 / 64)
        self.assertLess(abs(sum(ys) + residual - sum(xs)), 1e-10)
        self.assertLessEqual(abs(residual), 1 / 128 + 1e-12)


class BenchmarkContractTests(unittest.TestCase):
    def test_balanced_and_floor_gcd_preserve_gcd_and_bezout(self):
        a, b = 10946, 6765
        ref = math.gcd(a, b)
        for mode in ("floor", "ceil", "nearest"):
            g, x, y, depth, _ = r026._extended_gcd_variant(a, b, mode)
            self.assertEqual(g, ref)
            self.assertEqual(a * x + b * y, g)
            self.assertGreater(depth, 0)

    def test_anchor_necessity_counterexample_really_distinguishes_future(self):
        witness = r026.anchor_necessity_counterexample()
        self.assertTrue(witness["same_residual"])
        self.assertFalse(witness["future_equal"])

    def test_multigrid_residual_correction_beats_state_restriction(self):
        rows = r026.benchmark_multigrid()
        residual = next(r for r in rows if r.collapse_family == "RESIDUAL_COLLAPSE")
        state_only = next(r for r in rows if r.collapse_family == "DOWN_PROJECTION")
        self.assertLess(residual.final_error, state_only.final_error * 1e-3)

    def test_far_projection_loses_metric_projection_objective(self):
        rows = r026.benchmark_projection()
        far = next(r for r in rows if r.collapse_family == "FAR_PROJECTION")
        near = next(r for r in rows if r.collapse_family == "NEAREST_PROJECTION")
        self.assertGreater(far.final_error, 0.0)
        self.assertEqual(near.final_error, 0.0)

    def test_integer_error_accumulator_matches_nearest_raster(self):
        for p, q, n in ((2, 7, 200), (13, 29, 500), (1, 2, 40)):
            self.assertEqual(r026.raster_nearest_naive(p, q, n), r026.raster_error_accumulator(p, q, n))


    def test_ill_conditioned_refinement_needs_residual_precision(self):
        rows = r026.benchmark_linear_systems()
        exact = next(r for r in rows if r.case_id == "ill_conditioned_exact_residual" and r.collapse_family == "RESIDUAL_COLLAPSE")
        coarse = next(r for r in rows if r.case_id == "ill_conditioned_quantized_residual" and r.collapse_family == "RESIDUAL_COLLAPSE")
        self.assertLess(exact.final_error, 1e-12)
        self.assertGreater(coarse.final_error, 1e-3)
        self.assertEqual(coarse.classification, "FAILS_CONVERGENCE_OR_INVARIANT")

    def test_collision_anchor_plus_residual_preserves_invariants(self):
        rows = r026.benchmark_collision()
        exact_split = next(r for r in rows if r.collapse_family == "ANCHOR_PLUS_RESIDUAL")
        residual_only = next(r for r in rows if r.collapse_family == "RESIDUAL_COLLAPSE")
        self.assertEqual(exact_split.invariant_violation, 0.0)
        self.assertGreater(residual_only.invariant_violation, 0.0)


    def test_machine_rows_include_taskbook_required_state_contract_fields(self):
        row = r026.benchmark_gcd()[0]
        d = r026.asdict(row)
        d.update(r026.machine_context(row))
        for key in (
            "problem_size_condition_parameters", "initial_state", "terminal_state",
            "residual_history_summary", "correctness", "final_error", "bias", "variance",
            "invariant_violation", "arithmetic_work_proxy", "state_bytes_proxy",
            "reconstruction_cost_proxy"
        ):
            self.assertIn(key, d)

    def test_capability_matrix_covers_every_family_and_benchmark(self):
        matrix = r026.capability_matrix([])
        self.assertEqual(set(matrix["collapse_families"]), set(r026.FAMILIES))
        for bench, cells in matrix["matrix"].items():
            self.assertEqual(set(cells), set(r026.FAMILIES), bench)
            self.assertTrue(set(cells.values()).issubset(set(r026.CLASSIFICATIONS)))


if __name__ == "__main__":
    unittest.main()
