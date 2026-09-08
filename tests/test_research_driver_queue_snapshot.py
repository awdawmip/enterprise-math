"""Bounded queue fixtures preserve the canonical per-pass read boundary."""
from __future__ import annotations

from contextlib import ExitStack
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from control_plane import research_control_bootstrap as bootstrap
from control_plane import research_result_authority_fault_isolation as authority
from tools import research_driver_queue as driver_queue
from tools import research_result_records as results


class DriverQueueSnapshotTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix="em-driver-queue-snapshot-")
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.heads = {}
        self.records = []
        for index in range(3):
            self._add_result(index)
        # Publications are fixture inputs. The Result/review reducers and the
        # existing dispatch/authority contexts remain real unless a test below
        # explicitly supplies a state or a validated isolation row.
        for patch in (
            mock.patch.object(bootstrap, "install", return_value=None),
            mock.patch.object(driver_queue, "_head_publications", return_value=self.heads),
        ):
            patch.start()
            self.addCleanup(patch.stop)

    def _add_result(self, index, **overrides):
        row = {
            "result_id": f"RR-{index:020X}",
            "task_id": f"TST-QUEUE-{index}",
            "publication_id": f"TP2-{index:020X}",
            "execution_record_id": f"ER-{index:020X}",
            "frozen_at": f"2026-09-08T00:00:0{index}Z",
            "terminal_verdict": "PASS",
            **overrides,
        }
        path = self.root.joinpath("research_result_records", row["task_id"], row["result_id"] + ".json")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(row) + "\n", encoding="utf-8")
        key = (row["task_id"], row["publication_id"])
        self.heads.setdefault(key, {"task_id": key[0], "publication_id": key[1]})
        self.records.append(row)
        return row

    def _measured(self, function):
        with ExitStack() as stack:
            calls = [
                stack.enter_context(mock.patch.object(owner, name, wraps=getattr(owner, name)))
                for owner, name in (
                    (results, "iter_results"), (results, "iter_reviews"),
                    (authority, "_validated_rows"), (authority, "_snapshot_stamp"),
                    (results._base, "_RAW_ITER_RESULTS"),
                )
            ]
            rows = function(self.root)
        return rows, [call.call_count for call in calls]

    def test_one_pass_preserves_rows_and_reduces_real_store_reads(self):
        before, before_counts = self._measured(driver_queue._queue_from_snapshot)
        after, after_counts = self._measured(driver_queue.queue)
        self.assertEqual(after, before)
        self.assertEqual(len(after), 3)
        # One operational read each, one validation, and both entry/exit stamps.
        # Other installed adapters may legitimately add underlying raw reads.
        self.assertEqual(after_counts[:4], [1, 1, 1, 2])
        for before_count, after_count in zip(before_counts, after_counts):
            self.assertGreater(before_count, after_count)

    def test_operational_filter_keeps_clean_same_generation_sibling(self):
        held = self.records[0]
        sibling = self._add_result(
            3, task_id=held["task_id"], publication_id=held["publication_id"]
        )
        # This test supplies an already-validated isolation row; it does not
        # certify source pins. The public operational Result filter stays real.
        isolation = {held["result_id"]: {
            **{key: held[key] for key in
               ("task_id", "publication_id", "execution_record_id")},
            "dependency_pins": [],
        }}
        waiting = {"state": "AWAITING_DRIVER_REVIEW", "review": None, "terminal": False}
        with mock.patch.object(authority, "_validated_rows", return_value=isolation), \
             mock.patch.object(results, "task_result_state", return_value=waiting) as states:
            rows = driver_queue.queue(self.root)
        result_ids = {rid for row in rows for rid in row["result_ids"]}
        self.assertNotIn(held["result_id"], result_ids)
        self.assertIn(sibling["result_id"], result_ids)
        self.assertEqual(states.call_count, 3)
        self.assertIn(mock.call(held["task_id"], self.root, publication_id=held["publication_id"]), states.call_args_list)

    def test_exception_restores_readers_and_authority_context(self):
        previous = results.iter_results, results.iter_reviews
        with mock.patch.object(results, "task_result_state", side_effect=RuntimeError("fixture failure")):
            with self.assertRaisesRegex(RuntimeError, "fixture failure"):
                driver_queue.queue(self.root)
        self.assertEqual((results.iter_results, results.iter_reviews), previous)
        self.assertIsNone(authority._ACTIVE.get())

    def test_new_result_during_pass_is_rejected_on_exit(self):
        previous = results.iter_results, results.iter_reviews
        real_state = results.task_result_state
        changed = False

        def mutate_after_state(task_id, root, publication_id=None):
            nonlocal changed
            value = real_state(task_id, root, publication_id=publication_id)
            if not changed:
                self._add_result(4)
                changed = True
            return value

        with mock.patch.object(results, "task_result_state", side_effect=mutate_after_state):
            with self.assertRaisesRegex(authority.ResultAuthorityIsolationError, "snapshot inputs changed"):
                driver_queue.queue(self.root)
        self.assertEqual((results.iter_results, results.iter_reviews), previous)
        self.assertIsNone(authority._ACTIVE.get())

    def test_other_root_and_next_call_observe_fresh_records(self):
        other = self.root.joinpath("other-root")
        path = other.joinpath("research_result_records", "OTHER", "RR-OTHER.json")
        path.parent.mkdir(parents=True)
        path.write_text(json.dumps({"result_id": "RR-OTHER"}) + "\n", encoding="utf-8")
        real_state = results.task_result_state

        def check_other_root(task_id, root, publication_id=None):
            self.assertEqual([row["result_id"] for row in results.iter_results(other)], ["RR-OTHER"])
            return real_state(task_id, root, publication_id=publication_id)

        with mock.patch.object(results, "task_result_state", side_effect=check_other_root):
            first = driver_queue.queue(self.root)
        self._add_result(3)
        second = driver_queue.queue(self.root)
        self.assertEqual(len(first), 3)
        self.assertEqual(len(second), 4)


if __name__ == "__main__":
    unittest.main()
