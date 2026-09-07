import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from control_plane import researcher_startup_packet as startup


SECTIONS = {
    "Mother question": "What is the exact question?",
    "Frozen inputs and scope": "Keep the frozen scope.",
    "Hard target and required outputs": "Produce one exact certificate.",
    "Research value to preserve": "Preserve the current frontier.",
    "Success, kill, and return criteria": "Return on proof or exact obstruction.",
}


class ResearcherStartupPacketTests(unittest.TestCase):
    def make_root(self, *, long_projection: bool = False) -> tuple[Path, dict]:
        temp = tempfile.TemporaryDirectory(prefix="em-startup-packet-")
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        (root / "research_task_records" / "T1").mkdir(parents=True)
        (root / "research_tasks").mkdir()
        (root / "research_returns").mkdir()
        (root / "research_returns" / "R1.md").write_text("durable frontier\n", encoding="utf-8")
        policy = {
            "researcher_cold_start_envelope": {
                "compact_packet_hard_max_bytes": 8192,
                "normal_remote_source_reads_before_math_max": 2,
            }
        }
        (root / "research_context_budget.json").write_text(
            json.dumps(policy), encoding="utf-8"
        )
        body_sections = dict(SECTIONS)
        if long_projection:
            body_sections["Frozen inputs and scope"] = "x" * 12000
        meta = {
            "task_id": "T1",
            "last_progress_ref": "branch@deadbeef / research_returns/R1.md",
            "dependencies": [
                {"target": "logical dependency", "satisfied": True}
            ],
        }
        body = "<!-- ENTERPRISE_MATH_TASK_V1\n" + json.dumps(meta) + "\n-->\n\n# T1\n\n"
        for name, value in body_sections.items():
            body += f"## {name}\n\n{value}\n\n"
        taskbook = root / "research_tasks" / "T1.md"
        taskbook.write_text(body, encoding="utf-8")
        sha1 = "sha1:" + hashlib.sha1(taskbook.read_bytes()).hexdigest()
        publication = {
            "record_schema": "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2",
            "task_id": "T1",
            "publication_id": "P1",
            "taskbook_path": "research_tasks/T1.md",
            "taskbook_blob_sha1": sha1,
        }
        (root / "research_task_records" / "T1" / "P1.json").write_text(
            json.dumps(publication), encoding="utf-8"
        )
        receipt = {
            "request_id": "req-1",
            "generated_at": "2026-09-07T00:00:00Z",
            "source_sha": "abc123",
            "kind": "RESEARCH",
            "immutable_receipt_path": "control_plane/chatgpt_dispatch_receipts/req-1.json",
            "route": {
                "action": "CLAIM_NEW_OWNER",
                "new_claim_required": True,
                "owner_claim_preserved": False,
                "reason": "fixture",
                "startup_transport": {"control_epoch": "E1"},
                "target": {
                    "task_id": "T1",
                    "publication_id": "P1",
                    "title": "fixture task",
                    "identity_lane": "L1",
                    "owner": "research/t1",
                    "state": "READY",
                    "dispatch_state": "NEEDS_DISPATCH",
                    "claim_id": None,
                    "researcher_id": None,
                    "lease_until": None,
                    "frontier": "advance exact fixture",
                    "next_action": "start",
                },
            },
        }
        return root, receipt

    def test_inline_projection_is_exact_and_dependency_is_bounded(self):
        root, receipt = self.make_root()
        packet = startup.build_packet(receipt, root)
        self.assertEqual(packet["schema"], startup.SCHEMA)
        self.assertEqual(packet["task"]["projection_mode"], "INLINE_EXACT_TASKBOOK_SECTIONS")
        self.assertEqual(packet["task"]["projection"]["Mother question"], SECTIONS["Mother question"])
        self.assertNotIn("ENTERPRISE_MATH_TASK_V1", json.dumps(packet))
        self.assertEqual(
            packet["read_plan"]["first_dependency_ref"],
            "research_returns/R1.md",
        )
        self.assertLessEqual(packet["packet_bytes"], 8192)
        self.assertEqual(packet["diagnostics"]["load_policy"], "TRIGGERED_ONLY")

    def test_oversize_projection_falls_back_without_semantic_truncation(self):
        root, receipt = self.make_root(long_projection=True)
        packet = startup.build_packet(receipt, root)
        self.assertEqual(
            packet["task"]["projection_mode"],
            "EXACT_TASKBOOK_REQUIRED_PACKET_BUDGET",
        )
        self.assertIsNone(packet["task"]["projection"])
        self.assertLessEqual(packet["packet_bytes"], 8192)

    def test_no_dispatch_target_stays_minimal(self):
        root, receipt = self.make_root()
        receipt["route"]["action"] = "NO_DISPATCH"
        receipt["route"]["target"] = None
        packet = startup.build_packet(receipt, root)
        self.assertIsNone(packet["task"])
        self.assertIsNone(packet["read_plan"]["first_dependency_ref"])
        self.assertLessEqual(packet["packet_bytes"], 8192)

    def test_taskbook_digest_mismatch_fails_closed(self):
        root, receipt = self.make_root()
        publication_path = root / "research_task_records" / "T1" / "P1.json"
        publication = json.loads(publication_path.read_text(encoding="utf-8"))
        publication["taskbook_blob_sha1"] = "sha1:" + "0" * 40
        publication_path.write_text(json.dumps(publication), encoding="utf-8")
        with self.assertRaises(startup.StartupPacketError):
            startup.build_packet(receipt, root)


if __name__ == "__main__":
    unittest.main()
