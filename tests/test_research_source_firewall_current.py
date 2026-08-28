import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from control_plane import research_source_firewall as fw
from tools import research_runtime_guard as guard


class SourceFirewallConfigTests(unittest.TestCase):
    def good(self):
        return {
            "mode": "BLIND_INDEPENDENT",
            "pre_math_stamp_required": True,
            "remote_stamp_before_math_required": False,
            "allowed_source_pins": [
                {"path": "inputs/packet.md", "commit": "a" * 40, "blob_sha1": "b" * 40}
            ],
            "withheld_source_pins": [
                {"path": "hidden/proof.md", "commit": "c" * 40, "blob_sha1": "d" * 40}
            ],
            "raw_freeze_path": "research_returns/raw.md",
        }

    def test_none_does_not_burden_ordinary_task(self):
        self.assertIsNone(fw.validate_config(None))
        self.assertIsNone(fw.validate_config({"mode": "NONE"}))

    def test_blind_config_requires_exact_commit_and_blob(self):
        cfg = self.good()
        cfg["allowed_source_pins"][0]["commit"] = "main"
        with self.assertRaisesRegex(fw.SourceFirewallError, "40-hex commit"):
            fw.validate_config(cfg)

        cfg = self.good()
        cfg["allowed_source_pins"][0]["blob_sha1"] = "moving"
        with self.assertRaisesRegex(fw.SourceFirewallError, "40-hex Git blob"):
            fw.validate_config(cfg)

    def test_pre_and_post_freeze_source_sets_must_be_disjoint(self):
        cfg = self.good()
        cfg["withheld_source_pins"] = [dict(cfg["allowed_source_pins"][0])]
        with self.assertRaisesRegex(fw.SourceFirewallError, "must be disjoint"):
            fw.validate_config(cfg)

    def test_path_traversal_is_rejected(self):
        cfg = self.good()
        cfg["withheld_source_pins"][0]["path"] = "../hidden.md"
        with self.assertRaisesRegex(fw.SourceFirewallError, "safe repository-relative"):
            fw.validate_config(cfg)


class BlindRepoFixture(unittest.TestCase):
    def make_repo(self):
        td = tempfile.TemporaryDirectory()
        root = Path(td.name)
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=root, check=True)
        subprocess.run(["git", "config", "user.name", "test"], cwd=root, check=True)
        (root / "inputs").mkdir()
        (root / "hidden").mkdir()
        (root / "research_returns").mkdir()
        (root / "inputs" / "packet.md").write_text("problem only\n", encoding="utf-8")
        (root / "hidden" / "proof.md").write_text("withheld proof\n", encoding="utf-8")
        subprocess.run(["git", "add", "."], cwd=root, check=True)
        subprocess.run(["git", "commit", "-qm", "frozen source set"], cwd=root, check=True)
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
        allowed_blob = subprocess.check_output(
            ["git", "rev-parse", "HEAD:inputs/packet.md"], cwd=root, text=True
        ).strip()
        withheld_blob = subprocess.check_output(
            ["git", "rev-parse", "HEAD:hidden/proof.md"], cwd=root, text=True
        ).strip()
        return td, root, commit, allowed_blob, withheld_blob

    def config(self, commit, allowed_blob, withheld_blob, *, remote=False):
        return {
            "mode": "BLIND_INDEPENDENT",
            "pre_math_stamp_required": True,
            "remote_stamp_before_math_required": remote,
            "allowed_source_pins": [
                {"path": "inputs/packet.md", "commit": commit, "blob_sha1": allowed_blob}
            ],
            "withheld_source_pins": [
                {"path": "hidden/proof.md", "commit": commit, "blob_sha1": withheld_blob}
            ],
            "raw_freeze_path": "research_returns/raw.md",
        }

    def record(self):
        return {
            "task_id": "RS-BLIND",
            "publication_id": "TP2-BLIND",
            "taskbook_path": "research_tasks/blind.md",
            "taskbook_blob_sha1": "sha1:" + "e" * 40,
        }

    def binding(self, *, claim="claim-one", lane=False):
        value = {
            "publication_id": "TP2-BLIND",
            "claim_id": claim,
            "researcher_id": "EM-BLIND-ABC123",
        }
        if lane:
            value.update(
                {
                    "execution_cohort_id": "EC-BLIND",
                    "execution_lane_id": "replication",
                }
            )
        return value


class GitObjectPinTests(BlindRepoFixture):
    def test_exact_path_commit_blob_passes_without_network(self):
        td, root, commit, allowed_blob, withheld_blob = self.make_repo()
        self.addCleanup(td.cleanup)
        cfg = self.config(commit, allowed_blob, withheld_blob)
        result = fw.validate_source_pins(cfg["allowed_source_pins"], root)
        self.assertEqual("PASS", result[0]["status"])
        self.assertEqual(allowed_blob, result[0]["actual_blob_sha1"])

    def test_wrong_blob_and_missing_commit_fail_closed(self):
        td, root, commit, allowed_blob, withheld_blob = self.make_repo()
        self.addCleanup(td.cleanup)
        cfg = self.config(commit, allowed_blob, withheld_blob)
        bad = [dict(cfg["allowed_source_pins"][0], blob_sha1="0" * 40)]
        with self.assertRaisesRegex(fw.SourceFirewallError, "blob mismatch"):
            fw.validate_source_pins(bad, root)
        missing = [dict(cfg["allowed_source_pins"][0], commit="f" * 40)]
        with self.assertRaises(fw.SourceFirewallError):
            fw.validate_source_pins(missing, root)


class ClaimScopedLifecycleTests(BlindRepoFixture):
    def test_pre_math_raw_freeze_then_source_exposure(self):
        td, root, commit, allowed_blob, withheld_blob = self.make_repo()
        self.addCleanup(td.cleanup)
        cfg = self.config(commit, allowed_blob, withheld_blob)
        binding = self.binding()
        with mock.patch.object(fw, "source_firewall_for_task", return_value=(cfg, self.record())):
            stamp, stamp_path = fw.write_pre_math_stamp(
                task_id="RS-BLIND",
                binding=binding,
                created_at="2026-08-28T06:00:00+00:00",
                root=root,
            )
            self.assertFalse(stamp["math_source_read_before_stamp"])
            self.assertEqual("claim-one", stamp["claim_id"])
            self.assertEqual(1, len(stamp["source_validation"]))
            self.assertNotIn("withheld_source_validation", stamp)

            with self.assertRaisesRegex(fw.SourceFirewallError, "RAW_FREEZE record does not exist"):
                fw.build_source_exposure_record(
                    task_id="RS-BLIND",
                    binding=binding,
                    raw_record_path=Path("evidence/missing.json"),
                    root=root,
                )

            raw_artifact = root / "research_returns" / "raw.md"
            raw_artifact.write_text("independent raw result\n", encoding="utf-8")
            raw, raw_path = fw.write_raw_freeze_record(
                task_id="RS-BLIND",
                binding=binding,
                pre_math_stamp_path=stamp_path,
                created_at="2026-08-28T06:10:00+00:00",
                root=root,
            )
            self.assertEqual("RAW_FREEZE", raw["phase"])
            self.assertTrue(raw["source_exposure_permitted"])

            exposure, _ = fw.write_source_exposure_record(
                task_id="RS-BLIND",
                binding=binding,
                raw_record_path=raw_path,
                created_at="2026-08-28T06:11:00+00:00",
                root=root,
            )
            self.assertEqual("SOURCE_EXPOSED", exposure["phase"])
            self.assertEqual("PASS", exposure["withheld_source_validation"][0]["status"])
            self.assertEqual(withheld_blob, exposure["withheld_source_validation"][0]["actual_blob_sha1"])

    def test_raw_artifact_drift_blocks_exposure(self):
        td, root, commit, allowed_blob, withheld_blob = self.make_repo()
        self.addCleanup(td.cleanup)
        cfg = self.config(commit, allowed_blob, withheld_blob)
        binding = self.binding()
        with mock.patch.object(fw, "source_firewall_for_task", return_value=(cfg, self.record())):
            _, stamp_path = fw.write_pre_math_stamp(task_id="RS-BLIND", binding=binding, root=root)
            raw_artifact = root / "research_returns" / "raw.md"
            raw_artifact.write_text("raw v1\n", encoding="utf-8")
            _, raw_path = fw.write_raw_freeze_record(
                task_id="RS-BLIND", binding=binding, pre_math_stamp_path=stamp_path, root=root
            )
            raw_artifact.write_text("rewritten after freeze\n", encoding="utf-8")
            with self.assertRaisesRegex(fw.SourceFirewallError, "RAW_FREEZE artifact"):
                fw.build_source_exposure_record(
                    task_id="RS-BLIND", binding=binding, raw_record_path=raw_path, root=root
                )

    def test_stamp_cannot_be_reused_by_different_claim(self):
        td, root, commit, allowed_blob, withheld_blob = self.make_repo()
        self.addCleanup(td.cleanup)
        cfg = self.config(commit, allowed_blob, withheld_blob)
        with mock.patch.object(fw, "source_firewall_for_task", return_value=(cfg, self.record())):
            _, stamp_path = fw.write_pre_math_stamp(
                task_id="RS-BLIND", binding=self.binding(claim="claim-one"), root=root
            )
            with self.assertRaisesRegex(fw.SourceFirewallError, "claim_id mismatch"):
                fw.verify_pre_math_stamp(
                    task_id="RS-BLIND",
                    binding=self.binding(claim="claim-two"),
                    stamp_path=stamp_path,
                    root=root,
                )

    def test_lane_scope_is_frozen_into_all_records(self):
        td, root, commit, allowed_blob, withheld_blob = self.make_repo()
        self.addCleanup(td.cleanup)
        cfg = self.config(commit, allowed_blob, withheld_blob)
        binding = self.binding(lane=True)
        with mock.patch.object(fw, "source_firewall_for_task", return_value=(cfg, self.record())):
            stamp = fw.build_pre_math_stamp(task_id="RS-BLIND", binding=binding, root=root)
        self.assertEqual("EC-BLIND", stamp["execution_cohort_id"])
        self.assertEqual("replication", stamp["execution_lane_id"])

    def test_records_are_append_only(self):
        td, root, commit, allowed_blob, withheld_blob = self.make_repo()
        self.addCleanup(td.cleanup)
        cfg = self.config(commit, allowed_blob, withheld_blob)
        binding = self.binding()
        with mock.patch.object(fw, "source_firewall_for_task", return_value=(cfg, self.record())):
            fw.write_pre_math_stamp(task_id="RS-BLIND", binding=binding, root=root)
            with self.assertRaisesRegex(fw.SourceFirewallError, "refusing to overwrite"):
                fw.write_pre_math_stamp(task_id="RS-BLIND", binding=binding, root=root)


class ExecutionGateTests(BlindRepoFixture):
    def test_default_local_pre_math_gate_adds_no_remote_requirement(self):
        cfg = self.config("a" * 40, "b" * 40, "c" * 40)
        binding = self.binding()
        with mock.patch.object(fw, "source_firewall_for_task", return_value=(cfg, self.record())), mock.patch.object(
            fw, "verify_pre_math_stamp", return_value={"phase": "PRE_MATH"}
        ):
            out = fw.execution_gate(
                task_id="RS-BLIND",
                binding=binding,
                state={"durable_frontier": {"source_firewall_pre_math_stamp": "evidence/stamp.json"}},
            )
        self.assertEqual("PRE_MATH_VERIFIED", out["phase"])
        self.assertFalse(out["remote_stamp_before_math_required"])

    def test_remote_override_cannot_be_satisfied_by_caller_boolean(self):
        cfg = self.config("a" * 40, "b" * 40, "c" * 40, remote=True)
        binding = self.binding()
        with mock.patch.object(fw, "source_firewall_for_task", return_value=(cfg, self.record())), mock.patch.object(
            fw, "verify_pre_math_stamp", return_value={"phase": "PRE_MATH"}
        ):
            with self.assertRaisesRegex(fw.SourceFirewallError, "external orchestrator"):
                fw.execution_gate(
                    task_id="RS-BLIND",
                    binding=binding,
                    state={"durable_frontier": {"source_firewall_remote_stamp_verified": True}},
                )


class RuntimeWrapperTests(unittest.TestCase):
    def core_result(self):
        return {
            "authorized": True,
            "task_id": "RS-T",
            "task_registration": {"state": "IMMUTABLE_REGISTERED"},
            "owner_claim": {"claim_id": "c"},
            "execution_binding": {
                "publication_id": "TP2-T",
                "claim_id": "c",
                "researcher_id": "EM-T-ABC123",
            },
            "authorization_authority": "CURRENT_AUTHORIZED_WINNING_ISSUE_240_CLAIM",
        }

    def test_ordinary_authorization_is_byte_semantically_unchanged(self):
        base = self.core_result()
        with mock.patch.object(guard._core, "authorize_execution", return_value=dict(base)), mock.patch.object(
            guard._firewall, "execution_gate", return_value=None
        ):
            out = guard.authorize_execution({"task": {"task_id": "RS-T"}}, events=[])
        self.assertEqual(base, out)

    def test_blind_gate_is_composed_after_winning_claim(self):
        with mock.patch.object(guard._core, "authorize_execution", return_value=self.core_result()), mock.patch.object(
            guard._firewall,
            "execution_gate",
            return_value={"mode": "BLIND_INDEPENDENT", "phase": "PRE_MATH_VERIFIED"},
        ):
            out = guard.authorize_execution({"task": {"task_id": "RS-T"}}, events=[])
        self.assertEqual("PRE_MATH_VERIFIED", out["source_firewall"]["phase"])
        self.assertTrue(out["authorization_authority"].endswith("+BLIND_PRE_MATH_VERIFIED"))

    def test_blind_gate_failure_is_runtime_authorization_failure(self):
        with mock.patch.object(guard._core, "authorize_execution", return_value=self.core_result()), mock.patch.object(
            guard._firewall,
            "execution_gate",
            side_effect=fw.SourceFirewallError("missing PRE_MATH"),
        ):
            with self.assertRaisesRegex(guard.RuntimeAuthorizationError, "missing PRE_MATH"):
                guard.authorize_execution({"task": {"task_id": "RS-T"}}, events=[])


if __name__ == "__main__":
    unittest.main()
