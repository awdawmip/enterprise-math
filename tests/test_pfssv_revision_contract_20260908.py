"""New bounded substrate cases, not repeats of the archived discovery audit."""
from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT.joinpath("scripts/check_prime_factor_semiprime_shell_residual_validation_revision_20260908.py")
spec = importlib.util.spec_from_file_location("pfssv_revision_stage1", SCRIPT)
subject = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = subject
spec.loader.exec_module(subject)


class NativeSubstrateContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.prefix = subject.PrimePrefix(1000)
        cls.coordinates = subject.CoordinateBins()

    def cell(self, X=121, num=1, den=20):
        return subject.shell_cell(self.prefix, X, num, den, self.coordinates)

    def test_complete_prefix_and_actual_rank(self):
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                    53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        self.assertEqual(list(subject.PrimePrefix(100).primes), expected)
        self.assertEqual(self.prefix.rank(61), 18)
        self.assertEqual(self.prefix.rank(60), 17)
        self.assertEqual(self.prefix.rank_interval(61, 63), (18, 18))
        self.assertEqual(self.prefix.rank_interval(25, 25), (10, 9))

    def test_zero_observed_support_retained_and_geometric_empty_separate(self):
        c = self.cell()
        rows = {row["p"]: row for row in c["rows"]}
        self.assertEqual(rows[5]["count"], 0)
        self.assertEqual(rows[7]["count"], 0)
        self.assertEqual(rows[5]["bins"]["density_flat"] is not None, True)
        self.assertEqual(rows[7]["bins"]["coarse_band"] is not None, True)
        self.assertEqual(c["zero_prime_count_rows"], 2)
        self.assertEqual([row["p"] for row in c["geometrically_empty_rows"]], [11])
        self.assertEqual(c["totals"]["raw"], 2)
        self.assertEqual(list(subject.iter_pairs(self.prefix, c)), [(2, 61), (3, 41)])

    def test_pi_coordinates_do_not_depend_on_survival_or_width(self):
        narrow = {r["p"]: r for r in self.cell()["rows"]}
        wide = {r["p"]: r for r in self.cell(121, 1, 5)["rows"]}
        self.assertEqual((narrow[5]["count"], wide[5]["count"]), (0, 1))
        self.assertEqual(narrow[5]["pi_p"], 3)
        self.assertEqual(wide[5]["pi_p"], 3)
        self.assertEqual(wide[5]["q_prime_rank_first"], 10)
        self.assertEqual(wide[5]["q_prime_rank_last"], 10)

    def test_joint_grid_matches_independent_integer_interval_membership(self):
        c = self.cell(121, 1, 5)
        grid = [[0] * subject.BINS for _ in range(subject.BINS)]
        pe = subject.rank_edges(c["prime_rank_caps"]["p"])
        qe = c["prime_rank_q_edges_zero_based"]
        for p, q in subject.iter_pairs(self.prefix, c):
            rp, rq = self.prefix.rank(p), self.prefix.rank(q)
            pb = next(i for i in range(subject.BINS) if pe[i] < rp <= pe[i + 1])
            qb = next(i for i in range(subject.BINS) if qe[i] < rq <= qe[i + 1])
            grid[pb][qb] += 1
        self.assertEqual(grid, c["profiles"]["prime_rank_joint"])

    def test_square_overflow_not_clipped_and_right_endpoint_declared(self):
        c = self.cell(48, 1, 24)
        row = next(r for r in c["rows"] if r["p"] == 7)
        self.assertEqual((row["qlo"], row["qhi"], row["count"]), (7, 7, 1))
        self.assertTrue(row["bins"]["overflow_u_gt_half"])
        self.assertIsNone(row["bins"]["density_flat"])
        self.assertEqual(c["totals"]["overflow"], 1)
        self.assertEqual(c["totals"]["diagonal"], 1)
        endpoint = self.coordinates.bins(7, 49)
        self.assertEqual(endpoint["raw"], 23)
        self.assertEqual(endpoint["density_flat"], 23)
        self.assertEqual(len(subject.orbit_diagnostic(7, 7)), 3)
        self.assertEqual(len(subject.orbit_diagnostic(5, 7)), 6)

    def test_full_serialization_preserves_added_scientific_vectors(self):
        c = self.cell()
        c["corrected_profiles"] = {"density_flat": list(range(24))}
        c["signed_residual_profiles"] = {"density_flat": list(range(-12, 12))}
        c["null_profiles"] = [list(range(24)), list(reversed(range(24)))]
        self.assertEqual(json.loads(subject.serial_cell(c)), c)
        del c["signed_residual_profiles"]
        with self.assertRaisesRegex(ValueError, "required cell payload"):
            subject.serial_cell(c)

    def test_stage1_does_not_manufacture_zero_correction_or_joint_null(self):
        c = self.cell()
        self.assertIsNone(c["corrected_profiles"])
        self.assertIsNone(c["signed_residual_profiles"])
        self.assertEqual(c["scientific_status"], "NOT_COMPUTED_STAGE_1")
        self.assertFalse(c["joint_rank_null"]["required_for_stage_1"])
        c["profiles"]["raw"].pop()
        with self.assertRaisesRegex(ValueError, "full one-dimensional"):
            subject.serial_cell(c)

    def test_bounded_independent_primality_and_domain_rejection(self):
        for n, expected in [(0, False), (1, False), (2, True), (49, False), (97, True), (121, False)]:
            self.assertEqual(subject.bounded_trial_prime(n), expected)
        for invalid in [-1, True]:
            with self.assertRaises(ValueError):
                subject.bounded_trial_prime(invalid)
        with self.assertRaises(subject.ResourceBoundary):
            subject.bounded_trial_prime(subject.MAX_Q + 1)
        with self.assertRaises(ValueError):
            subject.shell_cell(subject.PrimePrefix(50), 121, 1, 20)
        with self.assertRaises(ValueError):
            self.cell(121, 1, 0)

    def test_actual_native_returns_are_captured_and_trace_budget_fails(self):
        previous = sys.getprofile()
        with tempfile.TemporaryDirectory(prefix="pfssv-stage1-") as tmp:
            path = Path(tmp).joinpath("trace.jsonl")
            with subject.NativeTraceCapture(path) as capture:
                trace = subject._divide(37, 5)
                self.assertEqual((trace.quotient, trace.remainder, trace.collapsed_numerator), (7, 2, 35))
                self.assertEqual(subject._root(50).root_index, 7)
                subject._divide(37, 5)
            rec = capture.receipt()
            self.assertEqual(rec["native_code_object_calls"]["brc_evaluate_division"], 2)
            self.assertEqual(rec["all_trace_events"], 3)
            self.assertEqual(rec["distinct_traces"], 2)
            records = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]
            self.assertIn("trace_ref", records[-1])
            with self.assertRaisesRegex(subject.ResourceBoundary, "trace byte cap"):
                with subject.NativeTraceCapture(Path(tmp).joinpath("small.jsonl"), byte_limit=1):
                    subject._divide(10, 3)
        self.assertIs(sys.getprofile(), previous)

    def test_unseparated_coordinate_is_not_silently_binned(self):
        with mock.patch.object(subject, "SCALES", ()):
            with self.assertRaises(subject.PrecisionUnresolved):
                subject.CoordinateBins().bins(5, 121)

    def test_exactly_reachable_capacity_violation_no_sampling_or_clipping(self):
        # A frozen synthetic row contract, not either archived discovery cell.
        source_channels = [0] * 30
        source_channels[1] = 2
        target_channels = [0] * 30
        row = {"bins": {"coarse_band": 2}, "p_mod_30": 1}
        fixture = {"rows": [
            {**row, "p": 31, "qlo": 31, "qhi": 61, "q_mod_30_counts": source_channels},
            {**row, "p": 61, "qlo": 91, "qhi": 91, "q_mod_30_counts": target_channels}]}
        witness = subject.null_a_capacity_witness(fixture)
        self.assertEqual(witness["status"], "REACHABLE_INTEGER_RESIDUE_CAPACITY_VIOLATION")
        self.assertEqual(witness["source_count"], 2)
        self.assertEqual(witness["target_integer_residue_capacity"], 1)
        self.assertEqual(witness["assignment_probability"], {"numerator": 1, "denominator": 2})
        self.assertEqual(witness["random_draws"], 0)
        self.assertFalse(witness["null_repaired"])


if __name__ == "__main__":
    unittest.main()
