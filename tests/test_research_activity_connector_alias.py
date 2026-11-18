"""Synthetic connector observations; no remote activity, authority or repair writes."""
import copy
import hashlib
from pathlib import Path
import tempfile
import unittest

from tools import research_activity as activity


ALIAS = "mcp__GitHub__fetch_file"


def source_observation(path, raw, tool=ALIAS):
    commit = "a" * 40
    pin = {"repository": activity.REPOSITORY, "commit": commit, "path": path,
           "sha256": hashlib.sha256(raw).hexdigest()}
    return {**pin, "readback": {
        "tool_name": tool, "observation_id": "synthetic-alias-regression",
        "arguments": {"repository_full_name": pin["repository"], "ref": commit, "path": path},
        "result": {"isError": False, "structuredContent": {
            "content": raw.decode(), "encoding": "utf-8", "sha": activity.blob_id(raw),
            "display_url": f"https://github.com/{pin['repository']}/blob/{commit}/{path}",
        }},
    }}


class ConnectorAliasTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.activity_id = "RA-ALIASREGRESSION"
        self.session = "synthetic-original-session"
        activity.register(root=self.root, activity_id=self.activity_id, mode="TASK_RESEARCH",
                          session_id=self.session, researcher_id="EM-TEST-1234")
        self.path = activity.record_path(self.activity_id, self.root)
        self.source = source_observation("research_notes/synthetic.md", b"synthetic source\n")

    def checkpoint(self):
        return activity.checkpoint(self.activity_id, event_id="original",
            expected_sha256=activity.digest(self.path.read_bytes()),
            em_sources=[self.source], root=self.root)

    def audit(self):
        return activity.audit_observations(activity_id=self.activity_id, session_id=self.session,
            root=self.root, new_semantic_progress=False,
            registration_source=source_observation(f"{activity.STORE}/{self.activity_id}.json",
                                                   self.path.read_bytes()))

    def test_full_alias_observation_and_sidecar_preserve_the_actual_name_and_bytes(self):
        original_observation = activity.encoded(self.source["readback"])
        record = self.checkpoint()
        accepted = record["checkpoints"][0]["em_sources"][0]
        self.assertEqual(accepted["verification"]["tool_name"], ALIAS)
        self.assertEqual(accepted["verification"]["kind"], "OBSERVED_CONNECTOR_STRUCTURE_AND_BYTES_VERIFIED")
        self.assertEqual((self.root / accepted["verification_receipt"]).read_bytes(), original_observation)
        before = self.path.read_bytes()
        result = self.audit()
        self.assertTrue(result["persistence_allowed"])
        self.assertTrue(all(value is False for value in result["authority"].values()))
        self.assertEqual(self.path.read_bytes(), before)

    def test_legacy_alias_summary_remains_debt_without_inventing_a_sidecar(self):
        record = self.checkpoint()
        source = record["checkpoints"][0]["em_sources"][0]
        receipt = self.root / source.pop("verification_receipt")
        source.pop("verification_receipt_sha256")
        receipt.unlink()
        self.path.write_bytes(activity.encoded(record))
        before = self.path.read_bytes()
        result = self.audit()
        self.assertEqual(result["legacy_observation_debt_events"], ["original"])
        self.assertEqual(result["sync_debt_events"], ["original"])
        self.assertFalse(result["persistence_allowed"])
        self.assertEqual(result["required_action"], "REOBSERVE_LEGACY_EM_SOURCES_AND_APPEND_CURRENT_REPAIR")
        self.assertEqual(self.path.read_bytes(), before)
        self.assertFalse(receipt.exists())

    def test_an_alias_name_does_not_make_a_missing_sidecar_exist(self):
        record = self.checkpoint()
        source = record["checkpoints"][0]["em_sources"][0]
        (self.root / source["verification_receipt"]).unlink()
        with self.assertRaises(FileNotFoundError):
            self.audit()

    def test_unrelated_and_near_match_names_are_rejected(self):
        for name in ("mcp__Other__fetch_file", "mcp__github__fetch_file", "mcp__GitHub__fetch",
                     "github_fetch", ALIAS + "_unchecked", None, []):
            with self.subTest(tool=name):
                observed = copy.deepcopy(self.source["readback"])
                observed["tool_name"] = name
                with self.assertRaises(activity.ActivityError):
                    activity.verify_observation(observed, self.source)

    def test_alias_keeps_all_full_observation_integrity_checks(self):
        mutations = (
            lambda x: x["arguments"].update(repository_full_name="other/repository"),
            lambda x: x["arguments"].update(ref="b" * 40),
            lambda x: x["arguments"].update(path="research_notes/other.md"),
            lambda x: x["arguments"].update(start_line=1),
            lambda x: x["result"].update(isError=True),
            lambda x: x["result"]["structuredContent"].update(content="changed bytes"),
            lambda x: x["result"]["structuredContent"].update(sha="0" * 40),
            lambda x: x["result"]["structuredContent"].update(display_url="https://github.com/other/repository/blob/main/file"),
            lambda x: x.pop("observation_id"),
        )
        for number, mutate in enumerate(mutations):
            with self.subTest(mutation=number):
                observed = copy.deepcopy(self.source["readback"])
                mutate(observed)
                with self.assertRaises(activity.ActivityError):
                    activity.verify_observation(observed, self.source)
        wrong_pin = {**self.source, "sha256": "0" * 64}
        with self.assertRaises(activity.ActivityError):
            activity.verify_observation(self.source["readback"], wrong_pin)

    def test_alias_cannot_be_paired_with_the_mcp_api_verification_kind(self):
        record = self.checkpoint()
        source = record["checkpoints"][0]["em_sources"][0]
        source.pop("verification_receipt")
        source.pop("verification_receipt_sha256")
        source["verification"]["kind"] = "OBSERVED_MCP_GITHUB_API_STRUCTURE_AND_BYTES_VERIFIED"
        with self.assertRaisesRegex(activity.ActivityError, "invalid legacy source summary"):
            activity._events(record, self.root)

    def test_alias_does_not_bypass_original_session_or_record_cas(self):
        self.checkpoint()
        before = self.path.read_bytes()
        with self.assertRaisesRegex(activity.ActivityError, "different or unknown original session"):
            activity.audit_observations(activity_id=self.activity_id, session_id="another-session", root=self.root)
        with self.assertRaisesRegex(activity.ActivityError, "expected_sha256 mismatch"):
            activity.checkpoint(self.activity_id, event_id="next", expected_sha256="0" * 64,
                                em_sources=[self.source], root=self.root)
        self.assertEqual(self.path.read_bytes(), before)


if __name__ == "__main__":
    unittest.main()
