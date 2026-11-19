"""Exact historical test successors preserve the coordinate regression gate."""
from __future__ import annotations

import tempfile
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

from tools import check_coordinate_regressions as gate


CLASS = "tests.test_x6_current_publication_integrity_isolation.X6CurrentPublicationIntegrityIsolationTests"
PAIRS = (
    ("test_six_exact_records_and_four_actual_errors_are_pinned",
     "test_six_original_records_and_heading_diagnostics_remain_historical"),
    ("test_only_the_six_current_definitions_change_and_are_blocked",
     "test_retired_style_rows_have_no_remaining_publication_or_dispatch_effect"),
    ("test_twenty_four_errors_require_the_new_validated_isolation",
     "test_retired_heading_errors_need_no_envelope_or_audit_exception"),
    ("test_missing_and_invented_error_suppressions_fail_strict_audit",
     "test_retired_missing_style_is_ignored_but_invented_error_still_fails"),
)
UNCHANGED = ("tests.test_lattice_geometry.LatticeGeometryTests", "test_low_dimensional_coordinator_shells")


class CoordinateRegressionComparisonTests(unittest.TestCase):
    def reports(self):
        before = {(CLASS, old): None for old, _ in PAIRS}
        after = {(CLASS, new): None for _, new in PAIRS}
        before[UNCHANGED] = after[UNCHANGED] = None
        return before, after

    def write_report(self, root, name, cases, outcome=None):
        report = ET.Element("testsuites")
        suite = ET.SubElement(report, "testsuite")
        for (classname, testname), failure in cases:
            case = ET.SubElement(suite, "testcase", classname=classname, name=testname)
            if failure is not None:
                problem = ET.SubElement(case, "failure", message="assertion")
                problem.text = failure
            if outcome:
                ET.SubElement(case, outcome)
        path = root / name
        ET.ElementTree(report).write(path, encoding="unicode")
        return path

    def test_two_xml_reports_keep_all_66_cases_and_accept_fixed_historical_failure(self):
        before, after = self.reports()
        for index in range(61):
            key = ("tests.test_coordinate_fixture", f"test_unchanged_{index}")
            before[key] = after[key] = None
        before[(CLASS, PAIRS[2][0])] = "historical fixed-heading failure"
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            old_path = self.write_report(root, "baseline.xml", before.items())
            new_path = self.write_report(root, "candidate.xml", after.items())
            result = gate.compare(gate.read_report(root, old_path), gate.read_report(root, new_path))
        self.assertEqual(result["tests_executed_each"], 66)
        self.assertEqual(result["baseline_failures"], 1)
        self.assertEqual(result["candidate_passed"], 66)
        self.assertEqual(result["historical_test_migration"]["matched_cases"], 4)
        self.assertTrue(result["complete_suite_green"])

    def test_changed_policy_successor_must_pass_even_if_old_failure_is_identical(self):
        for old, new in PAIRS:
            with self.subTest(successor=new):
                before, after = self.reports()
                before[(CLASS, old)] = after[(CLASS, new)] = "same failure"
                with self.assertRaisesRegex(AssertionError, "Changed-policy successor failed"):
                    gate.compare(before, after)

    def test_same_case_count_does_not_hide_deleted_or_renamed_test(self):
        before, after = self.reports()
        after.pop(UNCHANGED)
        after[("tests.test_lattice_geometry.LatticeGeometryTests", "test_unreviewed_replacement")] = None
        self.assertEqual(len(before), len(after))
        with self.assertRaisesRegex(AssertionError, "Changed regression population"):
            gate.compare(before, after)

    def test_mapping_is_only_for_exact_historical_class_and_baseline_side(self):
        before, after = self.reports()
        old, new = PAIRS[0]
        after[(CLASS, old)] = after.pop((CLASS, new))
        with self.assertRaisesRegex(AssertionError, "Changed regression population"):
            gate.compare(before, after)
        before, after = self.reports()
        before[("other." + CLASS, old)] = before.pop((CLASS, old))
        with self.assertRaisesRegex(AssertionError, "Changed regression population"):
            gate.compare(before, after)

    def test_duplicate_successor_is_not_silently_collapsed(self):
        before, after = self.reports()
        before[(CLASS, PAIRS[0][1])] = None
        with self.assertRaisesRegex(AssertionError, "Duplicate historical test successor"):
            gate.compare(before, after)

    def test_unchanged_tests_keep_new_failure_and_detail_regression_checks(self):
        before, after = self.reports()
        after[UNCHANGED] = "new failure"
        with self.assertRaisesRegex(AssertionError, "New failing test"):
            gate.compare(before, after)
        before[UNCHANGED] = "old failure"
        with self.assertRaisesRegex(AssertionError, "Changed failure"):
            gate.compare(before, after)
        after[UNCHANGED] = before[UNCHANGED]
        result = gate.compare(before, after)
        self.assertFalse(result["complete_suite_green"])
        self.assertEqual(result["candidate_failures"], 1)

    def test_xml_errors_skips_duplicates_and_empty_reports_remain_errors(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for outcome in ("error", "skipped"):
                with self.subTest(outcome=outcome):
                    path = self.write_report(root, "invalid.xml", [(UNCHANGED, None)], outcome)
                    with self.assertRaisesRegex(AssertionError, "errors/skips"):
                        gate.read_report(root, path)
            path = self.write_report(root, "duplicate.xml", [(UNCHANGED, None), (UNCHANGED, None)])
            with self.assertRaises(AssertionError):
                gate.read_report(root, path)
            path = self.write_report(root, "empty.xml", [])
            with self.assertRaisesRegex(AssertionError, "NO_TESTS_RAN"):
                gate.read_report(root, path)

    def test_failure_normalization_only_replaces_checkout_path(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = self.write_report(root, "failure.xml", [(UNCHANGED, str(root) + "/tests/test.py:7")])
            result = gate.read_report(root, path)
        self.assertEqual(result[UNCHANGED], "assertion\n$ROOT/tests/test.py:7")


if __name__ == "__main__":
    unittest.main()
