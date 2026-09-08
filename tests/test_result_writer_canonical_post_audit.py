"""Real local review transactions must share the exact canonical audit chain."""
from __future__ import annotations

import argparse
import contextlib
import copy
import functools
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from control_plane import check_result_review_binding_fault_isolated as checker
from control_plane import research_control_bootstrap as bootstrap
from control_plane import research_result_record_audit_fault_isolation as result_isolation
from tools import research_result_records as records
from tests.test_research_task_record_compatibility import _write_semantic_fixture


REPO = Path(__file__).resolve().parents[1]
HISTORICAL_ID = "RR-68BA014D54542DA7221C"
TARGET_ID = "RR-3287C6124F8D8A1F0901"
TARGET_PATH = (
    "research_result_records/RS-PRIME-FACTOR-SEMIPRIME-SHELL-RESIDUAL-VALIDATION/"
    + TARGET_ID + ".json"
)
DRIVER_ID = "EM-DVR-01E1D9"
REVIEWED_AT = "2026-09-08T07:50:00+00:00"


def setUpModule():
    # Standalone runs must retain the same task selectors as the complete shard.
    bootstrap.install(REPO)


class ResultWriterCanonicalPostAuditTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory(prefix="em-result-writer-post-audit-")
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.source_bytes = {}
        # Freeze validates the current publication through the real persistent
        # semantic/followup selectors. Supply their required, independently
        # pinned semantic fixture; its unrelated task remains nonoperational.
        _write_semantic_fixture(self.root)

        def capture(relative):
            source = REPO.joinpath(relative)
            raw = source.read_bytes()
            target = self.root.joinpath(relative)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(raw)
            self.source_bytes[relative] = raw
            return json.loads(raw) if relative.endswith(".json") else None

        payload = json.loads(REPO.joinpath(result_isolation.QUARANTINE_FILE).read_bytes())
        self.row = next(row for row in payload["entries"] if row["result_id"] == HISTORICAL_ID)
        self.registry = {**payload, "entries": [copy.deepcopy(self.row)]}
        self._write_registry()
        compatibility = json.loads(REPO.joinpath(records._base.COMPATIBILITY_FILE).read_bytes())
        compatibility["result_normalizations"] = [
            row for row in compatibility["result_normalizations"]
            if row["result_id"] in {HISTORICAL_ID, TARGET_ID}
        ]
        compatibility["review_normalizations"] = []
        self.root.joinpath(records._base.COMPATIBILITY_FILE).write_text(
            json.dumps(compatibility) + "\n", encoding="utf-8"
        )
        for relative in (self.row["record_path"], TARGET_PATH):
            result = capture(relative)
            execution_relative = (
                f"research_execution_records/{result['task_id']}/{result['execution_record_id']}.json"
            )
            execution = capture(execution_relative)
            dependencies = {result["return_path"], result["taskbook_path"]}
            dependencies.update(item["path"] for item in result["output_manifest"])
            if execution.get("taskbook_path"):
                dependencies.add(execution["taskbook_path"])
            for dependency in dependencies:
                capture(dependency)
        for publication in (self.row["publication_id"], self.row["superseding_publication_id"]):
            capture(f"research_task_records/{self.row['task_id']}/{publication}.json")

        # Retain a real, source-backed active Driver authority in the fixture.
        driver = records._driver_authority
        active = driver.require_active_driver(DRIVER_ID, REVIEWED_AT, REPO)
        self.assertIsNotNone(active)
        for relative in (driver.CONTRACT, driver.CONTROL_POLICY, driver.LEGACY_REVIEWS):
            capture(relative)
        capture(active["_record_path"])
        self.driver_authority = active

        self.target = {**json.loads(self.root.joinpath(TARGET_PATH).read_bytes()), "_record_path": TARGET_PATH}
        old_artifact = self.root.joinpath("driver_reviews/FIXTURE_EXISTING_REVIEW.md")
        old_artifact.parent.mkdir(parents=True)
        old_artifact.write_text("Local transaction fixture: existing review.\n", encoding="utf-8")
        first = records.review_result(
            result=self.target, driver_id=DRIVER_ID, disposition="REQUEST_REVISION",
            review_path=old_artifact, destination_class="NONE", destination_ref_or_none="",
            reviewed_at=REVIEWED_AT, root=self.root,
        )
        first["driver_authority_record_id"] = active["authority_record_id"]
        first["driver_authority_source_comment_id"] = active["source_comment_id"]
        first_path = self.root.joinpath("research_result_reviews", TARGET_ID, first["review_id"] + ".json")
        first_path.parent.mkdir(parents=True)
        first_path.write_bytes(records._write_tx.json_bytes(first))
        self.first_path, self.first_bytes = first_path, first_path.read_bytes()
        self.review_path = self.root.joinpath("driver_reviews/FIXTURE_NEW_REVIEW.md")
        self.review_path.write_text("Local transaction fixture: independent revision request.\n", encoding="utf-8")
        self.args = argparse.Namespace(
            result_id=TARGET_ID, driver_id=DRIVER_ID, disposition="REQUEST_REVISION",
            review_path="driver_reviews/FIXTURE_NEW_REVIEW.md", destination_class="NONE",
            destination_ref_or_none="", reviewed_at=REVIEWED_AT,
            followup_spec=None, followup_created_at=None,
        )
        self.new_id = records.review_result(
            result=self.target, driver_id=DRIVER_ID, disposition="REQUEST_REVISION",
            review_path=self.review_path, destination_class="NONE", destination_ref_or_none="",
            reviewed_at=REVIEWED_AT, root=self.root,
        )["review_id"]
        self.new_path = self.root.joinpath("research_result_reviews", TARGET_ID, self.new_id + ".json")

        # Forward legacy no-argument writer reads to this fixture. The actual
        # builders, validators, active-Driver check, checker and transaction run.
        # Install the real Result/review adapters on this root while retaining
        # the bootstrapped task selectors and their source-backed fixture above.
        self._install_result_fixture_view()
        result_map, iter_reviews, review_result = records.result_map, records.iter_reviews, records.review_result

        @functools.wraps(iter_reviews)
        def fixture_reviews(root=self.root):
            return iter_reviews(root)

        for patch in (
            mock.patch.object(records, "ROOT", self.root),
            mock.patch.object(records, "REVIEW_ROOT", self.root.joinpath("research_result_reviews")),
            mock.patch.object(records, "result_map", lambda root=self.root: result_map(root)),
            mock.patch.object(records, "iter_reviews", fixture_reviews),
            mock.patch.object(records, "review_result", functools.partial(review_result, root=self.root)),
            mock.patch.object(records, "_install_canonical_write_view", self._install_result_fixture_view),
        ):
            patch.start()
            self.addCleanup(patch.stop)

    def _install_result_fixture_view(self):
        checker.binding_isolation.install(self.root)
        checker.review_audit_isolation.install(self.root)
        checker.result_authority_isolation.install(self.root)

    def _write_registry(self):
        self.root.joinpath(result_isolation.QUARANTINE_FILE).write_text(
            json.dumps(self.registry) + "\n", encoding="utf-8"
        )

    def _run_review(self):
        with contextlib.redirect_stdout(io.StringIO()):
            return records.command_review_with_authority(self.args)

    def _assert_rollback(self, pattern):
        with self.assertRaisesRegex(records.ResultRecordError, pattern):
            self._run_review()
        self.assertFalse(self.new_path.exists())
        self.assertEqual(self.first_path.read_bytes(), self.first_bytes)

    def test_exact_history_allows_review_and_raw_audit_stays_strict(self):
        expected = [f"{self.row['record_path']}: {suffix}" for suffix in self.row["allowed_result_audit_errors"]]
        self.assertEqual(records.audit(self.root), expected)
        self.assertEqual(checker.audit(self.root), [])
        self.assertEqual(self._run_review(), 0)
        self.assertTrue(self.new_path.exists())
        self.assertEqual(records.audit(self.root), expected)
        self.assertEqual(self.first_path.read_bytes(), self.first_bytes)
        for path, raw in self.source_bytes.items():
            self.assertEqual(self.root.joinpath(path).read_bytes(), raw)

    def test_old_raw_postcheck_reproduces_rollback(self):
        with mock.patch.object(records, "_canonical_transaction_audit", records.audit):
            self._assert_rollback("no committed candidate.*invalid")

    def test_unregistered_result_error_survives_and_rolls_back_only_candidate(self):
        bad = {k: v for k, v in self.target.items() if not k.startswith("_")}
        bad.update(result_id="RR-UNQUARANTINED-FIXTURE", terminal_verdict="UNREGISTERED_BAD_ENUM")
        path = self.root.joinpath("research_result_records", bad["task_id"], bad["result_id"] + ".json")
        path.write_bytes(records._write_tx.json_bytes(bad))
        self._assert_rollback("no committed candidate.*invalid terminal_verdict")
        self.assertTrue(path.exists())

    def test_registered_result_pin_drift_still_rolls_back(self):
        path = self.root.joinpath(self.row["record_path"])
        path.write_bytes(path.read_bytes() + b"\n")
        self._assert_rollback("no committed candidate.*record blob drift")

    def test_unused_exact_suppression_still_rolls_back(self):
        self.registry["entries"][0]["allowed_result_audit_errors"].append("not a present strict error")
        self._write_registry()
        self._assert_rollback("no committed candidate.*stale or unused suppression")

    def test_candidate_errors_are_rejected_before_write(self):
        real_builder = records.review_result
        cases = (
            ("result_record_sha256", "sha256:" + "0" * 64, "result record digest drift"),
            ("review_sha256", "sha256:" + "0" * 64, "review artifact digest drift"),
            ("publication_id", "TP2-OTHER-FIXTURE", "result-linked field mismatch"),
            ("disposition", "UNREGISTERED_DISPOSITION", "invalid disposition"),
            ("review_id", json.loads(self.first_bytes)["review_id"], "duplicate review_id"),
        )
        for field, value, error in cases:
            with self.subTest(field=field):
                def damaged(**kwargs):
                    candidate = real_builder(**kwargs)
                    candidate[field] = value
                    return candidate

                with mock.patch.object(records, "review_result", side_effect=damaged), \
                     mock.patch.object(records._write_tx, "commit", wraps=records._write_tx.commit) as commit:
                    self._assert_rollback("candidate preflight.*" + error)
                    commit.assert_not_called()

    def test_freeze_uses_the_same_postcheck_and_preserves_history(self):
        relative = f"research_task_records/{self.target['task_id']}/{self.target['publication_id']}.json"
        publication = self.root.joinpath(relative)
        publication.parent.mkdir(parents=True, exist_ok=True)
        publication.write_bytes(REPO.joinpath(relative).read_bytes())
        args = argparse.Namespace(**{
            field: self.target[field] for field in (
                "execution_record_id", "return_path", "terminal_verdict", "hard_target_disposition",
                "unresolved_residue", "method_harvest", "independence_status",
                "source_exposure_status", "next_control_plane_recommendation",
            )
        })
        args.owner_head = "6efc3fdbad07bddee88270d10fc0ca2554a1184c"
        args.frozen_at = REVIEWED_AT
        args.output_paths_json = json.dumps([row["path"] for row in self.target["output_manifest"]])
        result_root = self.root.joinpath("research_result_records")
        before = {path: path.read_bytes() for path in result_root.rglob("*.json")}
        builder = records.freeze_result
        with mock.patch.object(records, "RESULT_ROOT", result_root), \
             mock.patch.object(records, "freeze_result", functools.partial(builder, root=self.root)), \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(records.command_freeze_transactional(args), 0)
            added = set(result_root.rglob("*.json")) - set(before)
            self.assertEqual(len(added), 1)
            candidate = added.pop()
            candidate.unlink()  # Only this test's just-created TEMP candidate.
            with mock.patch.object(records, "_canonical_transaction_audit", records.audit):
                with self.assertRaisesRegex(records.ResultRecordError, "no committed candidate.*invalid"):
                    records.command_freeze_transactional(args)
            self.assertFalse(candidate.exists())
        self.assertEqual({path: path.read_bytes() for path in before}, before)

    def test_inactive_driver_and_unknown_result_are_rejected_before_write(self):
        with mock.patch.object(records._write_tx, "commit", wraps=records._write_tx.commit) as commit:
            self.args.driver_id = "EM-DVR-FFFF"
            self._assert_rollback("no source-backed ACTIVE authority")
            self.args.driver_id = DRIVER_ID
            self.args.result_id = "RR-NOT-OPERATIONAL"
            self._assert_rollback("unknown result_id")
            commit.assert_not_called()


if __name__ == "__main__":
    unittest.main()
