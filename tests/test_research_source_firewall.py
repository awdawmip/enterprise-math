import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools import research_runtime_guard as guard


class SourceFirewallConfigTests(unittest.TestCase):
    def good(self):
        return {
            "mode": "BLIND_INDEPENDENT",
            "pre_math_stamp_required": True,
            "remote_stamp_before_math_required": False,
            "allowed_source_pins": [
                {
                    "path": "research_inputs/packet.md",
                    "commit": "a" * 40,
                    "blob_sha1": "b" * 40,
                }
            ],
            "withheld_until_raw_freeze": ["originating proof", "source checker"],
            "raw_freeze_path": "research_returns/task_raw.md",
        }

    def test_none_is_no_extra_gate(self):
        self.assertIsNone(guard.validate_source_firewall_config(None))
        self.assertIsNone(guard.validate_source_firewall_config({"mode": "NONE"}))

    def test_blind_config_requires_exact_commit_and_blob(self):
        cfg = self.good()
        cfg["allowed_source_pins"][0]["commit"] = "main"
        with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "40-hex commit"):
            guard.validate_source_firewall_config(cfg)

        cfg = self.good()
        cfg["allowed_source_pins"][0]["blob_sha1"] = "unknown"
        with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "40-hex Git blob"):
            guard.validate_source_firewall_config(cfg)

    def test_path_traversal_and_duplicate_pin_are_rejected(self):
        cfg = self.good()
        cfg["allowed_source_pins"][0]["path"] = "../secret.md"
        with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "safe repository-relative"):
            guard.validate_source_firewall_config(cfg)

        cfg = self.good()
        cfg["allowed_source_pins"].append(dict(cfg["allowed_source_pins"][0]))
        with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "duplicate"):
            guard.validate_source_firewall_config(cfg)

    def test_raw_freeze_path_is_required_and_repository_relative(self):
        cfg = self.good()
        cfg["raw_freeze_path"] = "/tmp/raw.md"
        with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "raw_freeze_path"):
            guard.validate_source_firewall_config(cfg)


class GitObjectPinTests(unittest.TestCase):
    def make_repo(self):
        td = tempfile.TemporaryDirectory()
        root = Path(td.name)
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.name", "test"], cwd=root, check=True)
        (root / "research_inputs").mkdir()
        packet = root / "research_inputs" / "packet.md"
        packet.write_text("frozen packet\n", encoding="utf-8")
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        subprocess.run(["git", "commit", "-qm", "packet"], cwd=root, check=True)
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
        blob = subprocess.check_output(
            ["git", "rev-parse", "HEAD:research_inputs/packet.md"],
            cwd=root,
            text=True,
        ).strip()
        return td, root, commit, blob

    def firewall(self, commit, blob):
        return {
            "mode": "BLIND_INDEPENDENT",
            "pre_math_stamp_required": True,
            "remote_stamp_before_math_required": False,
            "allowed_source_pins": [
                {
                    "path": "research_inputs/packet.md",
                    "commit": commit,
                    "blob_sha1": blob,
                }
            ],
            "withheld_until_raw_freeze": ["originating proof"],
            "raw_freeze_path": "research_returns/raw.md",
        }

    def test_exact_path_commit_blob_passes_without_network(self):
        td, root, commit, blob = self.make_repo()
        self.addCleanup(td.cleanup)
        result = guard.validate_source_pins(self.firewall(commit, blob), root)
        self.assertEqual(1, len(result))
        self.assertEqual("PASS", result[0]["status"])
        self.assertEqual(blob, result[0]["actual_blob_sha1"])

    def test_wrong_blob_fails_closed_before_math(self):
        td, root, commit, _ = self.make_repo()
        self.addCleanup(td.cleanup)
        with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "blob mismatch"):
            guard.validate_source_pins(self.firewall(commit, "0" * 40), root)

    def test_missing_commit_fails_closed_before_math(self):
        td, root, _, blob = self.make_repo()
        self.addCleanup(td.cleanup)
        with self.assertRaises(guard.RuntimeAuthorizationError):
            guard.validate_source_pins(self.firewall("f" * 40, blob), root)


class PreMathStampTests(unittest.TestCase):
    def firewall(self, *, remote=False):
        return {
            "mode": "BLIND_INDEPENDENT",
            "pre_math_stamp_required": True,
            "remote_stamp_before_math_required": remote,
            "allowed_source_pins": [
                {"path": "research_inputs/p.md", "commit": "a" * 40, "blob_sha1": "b" * 40}
            ],
            "withheld_until_raw_freeze": ["source proof"],
            "raw_freeze_path": "research_returns/raw.md",
        }

    def record(self):
        return {
            "publication_id": "TP2-ONE",
            "taskbook_path": "research_tasks/t.md",
            "taskbook_blob_sha1": "sha1:" + "c" * 40,
        }

    def validation(self):
        return [
            {
                "path": "research_inputs/p.md",
                "commit": "a" * 40,
                "declared_blob_sha1": "b" * 40,
                "actual_blob_sha1": "b" * 40,
                "status": "PASS",
            }
        ]

    def test_stamp_freezes_before_math_false_and_exact_publication(self):
        with mock.patch.object(guard, "source_firewall_for_task", return_value=(self.firewall(), self.record())), mock.patch.object(
            guard, "validate_source_pins", return_value=self.validation()
        ):
            stamp = guard.build_pre_math_stamp(
                task_id="RS-T",
                researcher_id="EM-T-ABC123",
                created_at="2026-08-26T10:00:00+08:00",
            )
        self.assertEqual(guard.STAMP_SCHEMA, stamp["schema"])
        self.assertEqual("STARTED_BEFORE_MATH", stamp["phase"])
        self.assertFalse(stamp["math_source_read_before_stamp"])
        self.assertEqual("TP2-ONE", stamp["publication_id"])
        self.assertEqual("NOT_REQUIRED_BEFORE_MATH", stamp["remote_stamp_verification"])

    def test_stamp_writer_is_exclusive_and_never_rewrites_provenance(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            with mock.patch.object(guard, "build_pre_math_stamp", return_value={"schema": guard.STAMP_SCHEMA}):
                stamp, path = guard.write_pre_math_stamp(
                    task_id="RS-T",
                    researcher_id="EM-T-ABC123",
                    output=Path("evidence/RS-T/execution_stamp.json"),
                    root=root,
                )
                self.assertTrue(path.exists())
                self.assertEqual(guard.STAMP_SCHEMA, json.loads(path.read_text())["schema"])
                with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "refusing to overwrite"):
                    guard.write_pre_math_stamp(
                        task_id="RS-T",
                        researcher_id="EM-T-ABC123",
                        output=Path("evidence/RS-T/execution_stamp.json"),
                        root=root,
                    )

    def test_authorize_blind_execution_requires_local_stamp(self):
        safe = {
            "task": {"task_id": "RS-T"},
            "task_registration": {"state": "IMMUTABLE_REGISTERED"},
            "durable_frontier": {},
        }
        with mock.patch.object(guard, "canonicalize_registration", return_value=safe), mock.patch.object(
            guard, "source_firewall_for_task", return_value=(self.firewall(), self.record())
        ):
            with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "requires PRE_MATH execution_stamp"):
                guard.authorize_execution(safe)

    def test_authorize_blind_execution_accepts_verified_local_stamp_without_remote_tax(self):
        safe = {
            "task": {"task_id": "RS-T"},
            "task_registration": {"state": "IMMUTABLE_REGISTERED"},
            "durable_frontier": {"execution_stamp": "evidence/RS-T/execution_stamp.json"},
        }
        with mock.patch.object(guard, "canonicalize_registration", return_value=safe), mock.patch.object(
            guard, "source_firewall_for_task", return_value=(self.firewall(), self.record())
        ), mock.patch.object(guard, "verify_pre_math_stamp", return_value={"phase": "STARTED_BEFORE_MATH"}) as verify:
            result = guard.authorize_execution(safe)
        self.assertTrue(result["authorized"])
        self.assertEqual("BLIND_INDEPENDENT_PRE_MATH_VERIFIED", result["source_firewall"])
        verify.assert_called_once()

    def test_explicit_remote_override_requires_external_orchestrator_proof(self):
        safe = {
            "task": {"task_id": "RS-T"},
            "task_registration": {"state": "IMMUTABLE_REGISTERED"},
            "durable_frontier": {"execution_stamp": "evidence/RS-T/execution_stamp.json"},
        }
        with mock.patch.object(guard, "canonicalize_registration", return_value=safe), mock.patch.object(
            guard, "source_firewall_for_task", return_value=(self.firewall(remote=True), self.record())
        ), mock.patch.object(guard, "verify_pre_math_stamp", return_value={}):
            with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "external orchestrator"):
                guard.authorize_execution(safe)


if __name__ == "__main__":
    unittest.main()
