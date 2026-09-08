"""Small real file stores exercise the read scope, not Driver authorization.

No Result/review reader, authority validator or exact-set reducer is replaced.
The fixture has no source-backed Driver contract and is not a publication test.
Fault callbacks below only introduce a concurrent file change or read another
root; they delegate the actual per-Result decision to the existing reducer.
"""
from __future__ import annotations

from contextlib import ExitStack
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import research_driver_followup_guard as guard
import research_review_evidence as evidence
from control_plane import research_result_authority_fault_isolation as authority
from tools import research_dispatch as dispatch
from tools import research_result_records as results


class FollowupAuthoritySnapshotTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix="em-followup-authority-read-")
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.records = [self.add_result(index) for index in range(3)]
        # Two clean Results in the same publication remain distinct authorities.
        self.add_review(0, "DR-A001", "REQUEST_REVISION")
        self.add_review(1, "DR-B001", "ACCEPTED")

    @staticmethod
    def write(path, value):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes((json.dumps(value, sort_keys=True) + "\n").encode("utf-8"))

    def add_result(self, index, *, root=None):
        root = self.root if root is None else root
        group = 0 if index in (0, 1) else index
        row = {
            "result_id": f"RR-{index:020X}",
            "task_id": f"TST-FOLLOWUP-{group}",
            "publication_id": f"TP2-{group:020X}",
            "execution_record_id": f"ER-{index:020X}",
            "frozen_at": "2026-09-08T00:00:00Z",
        }
        self.write(root.joinpath("research_result_records", row["task_id"], row["result_id"] + ".json"), row)
        return row

    def review_path(self, index, review_id):
        return self.root.joinpath("research_result_reviews", f"RR-{index:020X}", review_id + ".json")

    def add_review(self, index, review_id, disposition="REQUEST_REVISION"):
        row = {
            "record_schema": evidence.REVIEW_SCHEMA,
            "review_id": review_id,
            "result_id": f"RR-{index:020X}",
            "driver_id": "EM-DVR-TEST1",
            "reviewed_at": "2026-09-08T00:01:00Z",
            "disposition": disposition,
            "terminal": disposition in evidence.TERMINAL_DISPOSITIONS,
            "destination_class": "NONE",
            "destination_ref_or_none": "",
        }
        self.write(self.review_path(index, review_id), row)
        return row

    def measured(self, callback):
        with ExitStack() as stack:
            calls = [
                stack.enter_context(mock.patch.object(owner, name, wraps=getattr(owner, name)))
                for owner, name in (
                    (results, "iter_results"), (results, "iter_reviews"),
                    (authority, "_validated_rows"), (authority, "_snapshot_stamp"),
                    (results._base, "_RAW_ITER_RESULTS"),
                    (results._base, "_RAW_ITER_REVIEWS"),
                )
            ]
            value = callback(self.root)
        return value, [call.call_count for call in calls]

    def test_real_store_counts_and_complete_authority_values_are_preserved(self):
        before, before_counts = self.measured(guard._authority_map_from_snapshot)
        after, after_counts = self.measured(guard.authority_map)
        self.assertEqual(after, before)
        self.assertEqual(list(after), ["DR-A001", "DR-B001"])
        self.assertEqual(after["DR-A001"]["disposition"], "REQUEST_REVISION")
        self.assertFalse(after["DR-A001"]["terminal"])
        self.assertEqual(after["DR-B001"]["disposition"], "ACCEPTED")
        self.assertTrue(after["DR-B001"]["terminal"])
        # These are scoped operation counts in this three-Result fixture.
        self.assertEqual(after_counts[:4], [1, 1, 1, 2])
        for index in (0, 1, 2, 4, 5):
            self.assertGreater(before_counts[index], after_counts[index])

    def test_new_review_after_return_reopens_exact_set_on_next_call(self):
        first = guard.authority_map(self.root)
        self.assertIn("DR-A001", first)
        self.assertIsNone(authority._ACTIVE.get())
        new = self.add_review(0, "DR-A002", "CLOSED")
        # A newer terminal disposition cannot win merely by timestamp.
        new["reviewed_at"] = "2026-09-08T00:05:00Z"
        self.write(self.review_path(0, "DR-A002"), new)
        second = guard.authority_map(self.root)
        self.assertNotIn("DR-A001", second)
        self.assertNotIn("DR-A002", second)
        self.assertIn("DR-B001", second)
        self.assertEqual(evidence.state(self.records[0]["result_id"], self.root)["review_state"], "AWAITING_REVIEW_INTAKE")
        self.assertTrue(self.review_path(0, "DR-A001").is_file())

    def test_added_review_during_read_is_rejected_and_readers_restored(self):
        previous = results.iter_results, results.iter_reviews
        active = authority._ACTIVE.get()
        original = guard.authority_for_result
        changed = False

        def append_after_read(result_id, root):
            nonlocal changed
            value = original(result_id, root)
            if not changed:
                self.add_review(2, "DR-C001")
                changed = True
            return value

        with mock.patch.object(guard, "authority_for_result", side_effect=append_after_read):
            with self.assertRaisesRegex(authority.ResultAuthorityIsolationError, "snapshot inputs changed"):
                guard.authority_map(self.root)
        self.assertEqual((results.iter_results, results.iter_reviews), previous)
        self.assertIs(authority._ACTIVE.get(), active)
        self.assertIn("DR-C001", guard.authority_map(self.root))

    def test_changed_review_bytes_during_read_are_rejected(self):
        original = guard.authority_for_result
        changed = False

        def change_after_read(result_id, root):
            nonlocal changed
            value = original(result_id, root)
            if not changed:
                path = self.review_path(1, "DR-B001")
                row = json.loads(path.read_text(encoding="utf-8"))
                row["reviewed_at"] = "2026-09-08T00:06:00Z"
                self.write(path, row)
                changed = True
            return value

        with mock.patch.object(guard, "authority_for_result", side_effect=change_after_read):
            with self.assertRaisesRegex(authority.ResultAuthorityIsolationError, "snapshot inputs changed"):
                guard.authority_map(self.root)
        self.assertIsNone(authority._ACTIVE.get())

    def test_added_result_during_read_is_rejected(self):
        original = guard.authority_for_result
        changed = False

        def append_after_read(result_id, root):
            nonlocal changed
            value = original(result_id, root)
            if not changed:
                self.add_result(3)
                changed = True
            return value

        with mock.patch.object(guard, "authority_for_result", side_effect=append_after_read):
            with self.assertRaisesRegex(authority.ResultAuthorityIsolationError, "snapshot inputs changed"):
                guard.authority_map(self.root)
        self.assertIsNone(authority._ACTIVE.get())

    def test_invalid_current_review_still_fails_and_restores_context(self):
        previous = results.iter_results, results.iter_reviews
        active = authority._ACTIVE.get()
        path = self.review_path(1, "DR-B001")
        row = json.loads(path.read_text(encoding="utf-8"))
        row["terminal"] = False
        self.write(path, row)
        with self.assertRaisesRegex(evidence.ReviewEvidenceError, "terminal flag mismatch"):
            guard.authority_map(self.root)
        self.assertEqual((results.iter_results, results.iter_reviews), previous)
        self.assertIs(authority._ACTIVE.get(), active)
        row["terminal"] = True
        self.write(path, row)
        self.assertIn("DR-B001", guard.authority_map(self.root))

    def test_other_root_reads_remain_fresh_inside_scope(self):
        other = self.root.joinpath("other-root")
        self.add_result(10, root=other)
        original = guard.authority_for_result
        observed = []

        def read_other_then_delegate(result_id, root):
            observed.append(len(results.iter_results(other)))
            if len(observed) == 1:
                self.add_result(11, root=other)
            return original(result_id, root)

        with mock.patch.object(guard, "authority_for_result", side_effect=read_other_then_delegate):
            value = guard.authority_map(self.root)
        self.assertEqual(observed, [1, 2, 2])
        self.assertEqual(list(value), ["DR-A001", "DR-B001"])

    def test_existing_outer_read_scope_shares_validation_without_extending_it(self):
        previous = results.iter_results, results.iter_reviews

        def nested(root):
            with dispatch._dispatch_result_read_snapshot(root):
                first = guard.authority_map(root)
                self.assertEqual(guard.authority_map(root), first)
                return first

        value, counts = self.measured(nested)
        self.assertEqual(list(value), ["DR-A001", "DR-B001"])
        self.assertEqual(counts[:4], [1, 1, 1, 2])
        self.assertEqual((results.iter_results, results.iter_reviews), previous)
        self.assertIsNone(authority._ACTIVE.get())


if __name__ == "__main__":
    unittest.main()
