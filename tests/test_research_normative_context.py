"""Current rule routing must not repin evidence or open a source firewall."""
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timezone
from pathlib import Path
from types import ModuleType
from unittest import mock

import control_plane
from control_plane import research_continuation as continuation
from control_plane import researcher_startup_packet as startup


ROOT = Path(__file__).resolve().parents[1]
SOURCE = "a" * 40
EVIDENCE_SOURCE = "b" * 40
NOW = datetime(2026, 11, 1, tzinfo=timezone.utc)


class ResearchNormativeContextTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        (self.root / "EM_SNAPSHOT_READY.json").write_text(json.dumps({"sha": SOURCE}))
        (self.root / "research_tasks").mkdir()
        (self.root / "research_task_records/T1").mkdir(parents=True)
        self.metadata = {
            "task_id": "T1",
            "source_refs": [f"research_returns/prior.md@{EVIDENCE_SOURCE}"],
        }
        sections = "\n".join(f"## {name}\n\nPreserve this exact obligation.\n" for name in startup.TASK_SECTIONS)
        self.body = "<!-- ENTERPRISE_MATH_TASK_V1\n" + json.dumps(self.metadata) + "\n-->\n" + sections
        (self.root / "research_tasks/T1.md").write_text(self.body)
        self.record = {
            "task_id": "T1", "publication_id": "P1",
            "taskbook_path": "research_tasks/T1.md",
            "taskbook_blob_sha1": startup._git_blob_sha1(self.body.encode()),
        }
        (self.root / "research_task_records/T1/P1.json").write_text(json.dumps(self.record))
        blobs = {}
        for path in ("research_tasks/T1.md", "research_task_records/T1/P1.json"):
            raw = (self.root / path).read_bytes()
            blobs[path] = hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()
        (self.root / "EM_SOURCE_BLOBS.json").write_text(json.dumps({
            "schema": "ENTERPRISE_MATH_SOURCE_BLOB_MANIFEST_V1",
            "source_commit": SOURCE, "blobs": blobs,
        }))
        (self.root / "research_context_budget.json").write_text(json.dumps({
            "researcher_cold_start_envelope": {
                "compact_packet_hard_max_bytes": 8192,
                "normal_remote_source_reads_before_math_max": 2,
            },
        }))
        self.state = {"task_id": "T1", "state": "READY", "dispatch_state": "NEEDS_DISPATCH"}
        self.receipt = {
            "request_id": "fixture", "source_sha": SOURCE,
            "route": {"action": "CLAIM_NEW_OWNER", "target": self.record},
        }

    def continuation_packet(self, *, restricted=False):
        # Repository reducers/registries are unchanged inputs to this projection.
        # Use their smallest interfaces; exercise real snapshot and artifact reads.
        tools_module = ModuleType("tools")
        tools_module.__path__ = []
        modules = {"tools": tools_module}
        values = {
            "research_dispatch": {"reduce_definition": lambda *a, **kw: self.state},
            "research_task_records": {"current_records": lambda root: {"T1": self.record}},
            "research_result_records": {"task_result_state": lambda *a: None},
            "research_taskbook": {"split_taskbook": lambda body: (self.metadata, body)},
        }
        for name, attributes in values.items():
            module = ModuleType("tools." + name)
            for key, value in attributes.items():
                setattr(module, key, value)
            setattr(tools_module, name, module)
            modules[module.__name__] = module
        firewall = ModuleType("control_plane.research_source_firewall")
        firewall.validate_config = lambda value: {"allowed_source_pins": []} if restricted else None
        modules[firewall.__name__] = firewall
        with mock.patch.dict(sys.modules, modules), mock.patch.object(
            control_plane, "research_source_firewall", firewall, create=True
        ), mock.patch.object(continuation, "_definition", return_value={"task_id": "T1"}), mock.patch.object(
            continuation, "checkpoint_frontier", return_value={"state": "NOT_FOUND", "source_artifacts": []}
        ):
            return continuation.continuation_packet(
                "T1", root=self.root, events=[], now=NOW, source_commit=SOURCE
            )

    def test_both_packet_paths_separate_current_rules_from_frozen_inputs(self):
        original = copy.deepcopy((self.receipt, self.record, self.state, self.metadata))
        modern = self.continuation_packet()
        compact = startup.build_packet(self.receipt, self.root)
        rules = modern["current_normative_context"]
        self.assertEqual(rules, compact["current_normative_context"])
        self.assertEqual("main", rules["project"]["ref"])
        self.assertEqual("main", rules["authorized_account_only"]["ref"])
        self.assertFalse(rules["authority_granted"])
        self.assertEqual(SOURCE, modern["source_commit"])
        self.assertEqual(SOURCE, compact["source_sha"])
        self.assertEqual(self.record, modern["task"])
        self.assertEqual(self.record["taskbook_blob_sha1"], compact["task"]["taskbook_blob_sha1"])
        self.assertEqual({SOURCE}, {pin["source_commit"] for pin in modern["source_artifacts"]})
        self.assertEqual(EVIDENCE_SOURCE, modern["immutable_external_artifact_candidates"][0]["source_commit"])
        self.assertEqual([], modern["artifact_errors"])
        self.assertFalse(modern["execution_authorized"])
        self.assertNotIn(rules["project"]["path"], {pin["path"] for pin in modern["source_artifacts"]})
        self.assertEqual(original, (self.receipt, self.record, self.state, self.metadata))
        self.assertLessEqual(compact["packet_bytes"], 8192)

    def test_current_rule_pointer_does_not_open_a_blind_source_firewall(self):
        packet = self.continuation_packet(restricted=True)
        self.assertTrue(packet["source_access_policy"]["restricted"])
        self.assertEqual(1, packet["source_access_policy"]["withheld_declared_input_count"])
        self.assertEqual([], packet["immutable_external_artifact_candidates"])
        self.assertEqual("WITHHELD_BY_SOURCE_FIREWALL", packet["persisted_checkpoint"]["state"])
        self.assertIn("PROJECT_METHOD_ROUTE_DEFERRED", packet["current_normative_context"]["free_phase_a"])
        self.assertFalse(packet["execution_authorized"])

    def test_direct_startup_script_keeps_its_supported_entrypoint(self):
        receipt_path = self.root / "receipt.json"
        output_path = self.root / "packet.json"
        receipt_path.write_text(json.dumps(self.receipt))
        result = subprocess.run(
            [sys.executable, str(ROOT / "control_plane/researcher_startup_packet.py"),
             "--root", str(self.root), "--receipt", str(receipt_path), "--output", str(output_path)],
            cwd=self.root, text=True, capture_output=True, check=False,
        )
        self.assertEqual(0, result.returncode, result.stderr)
        packet = json.loads(output_path.read_text())
        self.assertIn("current_normative_context", packet)
        self.assertEqual(SOURCE, packet["source_sha"])
        self.assertLessEqual(packet["packet_bytes"], 8192)


if __name__ == "__main__":
    unittest.main()
