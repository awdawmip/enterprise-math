"""Exercise the startup packet's actual UTF-8 LF CLI wire format."""
import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "control_plane" / "researcher_startup_packet.py"
HARD_MAX = 8192
SECTIONS = {
    "Mother question": "Preserve the exact question.",
    "Frozen inputs and scope": "Use the frozen inputs.",
    "Hard target and required outputs": "Return the required certificate.",
    "Research value to preserve": "Keep the established frontier.",
    "Success, kill, and return criteria": "Return proof or the exact obstruction.",
}


def pretty_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode(
        "utf-8"
    )


class ResearcherStartupPacketByteTests(unittest.TestCase):
    def make_fixture(self):
        temporary = tempfile.TemporaryDirectory(prefix="em-packet-bytes-")
        self.addCleanup(temporary.cleanup)
        root = Path(temporary.name)
        (root / "research_task_records" / "T1").mkdir(parents=True)
        (root / "research_tasks").mkdir()
        (root / "research_returns").mkdir()
        (root / "research_returns" / "R1.md").write_bytes(b"Frozen dependency.\n")
        (root / "research_context_budget.json").write_bytes(pretty_bytes({
            "researcher_cold_start_envelope": {
                "compact_packet_hard_max_bytes": HARD_MAX,
                "normal_remote_source_reads_before_math_max": 2,
            }
        }))
        receipt = {
            "request_id": "byte-fixture",
            "generated_at": "2026-09-08T00:00:00Z",
            "source_sha": "a" * 40,
            "kind": "RESEARCH",
            "immutable_receipt_path": "control_plane/chatgpt_dispatch_receipts/byte-fixture.json",
            "route": {
                "action": "CLAIM_NEW_OWNER",
                "new_claim_required": True,
                "owner_claim_preserved": False,
                "reason": "Exact fixture route.",
                "startup_transport": {"control_epoch": "E1"},
                "target": {
                    "task_id": "T1", "publication_id": "P1",
                    "title": "Exact task", "identity_lane": "L1",
                    "owner": "research/t1", "state": "READY",
                    "dispatch_state": "NEEDS_DISPATCH", "claim_id": None,
                    "researcher_id": None, "lease_until": None,
                    "frontier": "Preserve this frontier.", "next_action": "Begin.",
                },
            },
        }
        self.write_publication(root, SECTIONS)
        return root, receipt

    def write_publication(self, root, sections):
        metadata = {"task_id": "T1", "last_progress_ref": "research_returns/R1.md"}
        body = "<!-- ENTERPRISE_MATH_TASK_V1\n" + json.dumps(metadata) + "\n-->\n\n# T1\n\n"
        for name, value in sections.items():
            body += f"## {name}\n\n{value}\n\n"
        raw = body.encode("utf-8")
        (root / "research_tasks" / "T1.md").write_bytes(raw)
        pin = "sha1:" + hashlib.sha1(f"blob {len(raw)}\0".encode("ascii") + raw).hexdigest()
        publication = {
            "record_schema": "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2",
            "task_id": "T1", "publication_id": "P1",
            "taskbook_path": "research_tasks/T1.md", "taskbook_blob_sha1": pin,
        }
        (root / "research_task_records" / "T1" / "P1.json").write_bytes(pretty_bytes(publication))
        return pin

    def run_cli(self, root, receipt):
        receipt_path = root / "receipt.json"
        receipt_path.write_bytes(pretty_bytes(receipt))
        output_path = root / "packet.json"
        environment = os.environ.copy()
        environment.pop("PYTHONPATH", None)
        completed = subprocess.run(
            [sys.executable, "-X", "utf8", "-B", str(SCRIPT), "--receipt", str(receipt_path),
             "--output", str(output_path), "--root", str(root)],
            cwd=ROOT, env=environment, capture_output=True, encoding="utf-8", timeout=15,
        )
        return completed, output_path

    def successful_output(self, root, receipt):
        completed, output = self.run_cli(root, receipt)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        raw = output.read_bytes()
        packet = json.loads(raw)
        self.assertEqual(packet["packet_bytes"], len(raw))
        self.assertEqual(json.loads(completed.stdout)["packet_bytes"], len(raw))
        self.assertEqual(raw, pretty_bytes(packet))
        self.assertNotIn(b"\r", raw)
        self.assertTrue(raw.endswith(b"\n"))
        self.assertLessEqual(len(raw), HARD_MAX)
        return packet, raw

    def padded_sections(self, root, receipt, extra_bytes):
        completed, output = self.run_cli(root, receipt)
        self.assertEqual(completed.returncode, 0, completed.stderr)
        candidate = json.loads(output.read_bytes())
        candidate["packet_bytes"] = HARD_MAX
        padding = HARD_MAX - len(pretty_bytes(candidate)) + extra_bytes
        self.assertGreater(padding, 0)
        sections = dict(SECTIONS)
        sections["Frozen inputs and scope"] += "x" * padding
        candidate["task"]["projection"] = sections
        self.assertEqual(len(pretty_bytes(candidate)), HARD_MAX + extra_bytes)
        without_annotation = copy.deepcopy(candidate)
        del without_annotation["packet_bytes"]
        self.assertLess(len(pretty_bytes(without_annotation)), HARD_MAX)
        return sections

    def test_cli_ascii_and_non_ascii_count_real_bytes_and_preserve_route(self):
        for text in ("ordinary", "进取坐标，保留全部边界 🧮"):
            with self.subTest(text=text):
                root, receipt = self.make_fixture()
                sections = {name: value + text for name, value in SECTIONS.items()}
                pin = self.write_publication(root, sections)
                receipt["route"]["target"]["title"] = text
                packet, raw = self.successful_output(root, receipt)
                self.assertIn(text.encode("utf-8"), raw)
                self.assertEqual(packet["schema"], "ENTERPRISE_MATH_RESEARCHER_STARTUP_PACKET_V1")
                for field in ("action", "new_claim_required", "owner_claim_preserved", "reason"):
                    self.assertEqual(packet[field], receipt["route"][field])
                self.assertEqual(packet["source_sha"], receipt["source_sha"])
                self.assertEqual(packet["control_epoch"], "E1")
                for field, value in receipt["route"]["target"].items():
                    self.assertEqual(packet["task"][field], value)
                self.assertEqual(packet["task"]["projection"], sections)
                self.assertEqual(packet["task"]["required_task_sections"], list(SECTIONS))
                self.assertEqual(packet["task"]["taskbook_blob_sha1"], pin)
                self.assertEqual(packet["task"]["taskbook_path"], "research_tasks/T1.md")
                self.assertEqual(packet["task"]["publication_record_path"], "research_task_records/T1/P1.json")
                self.assertEqual(packet["read_plan"]["first_dependency_ref"], "research_returns/R1.md")

    def test_cli_complete_projection_at_exact_limit_stays_inline(self):
        root, receipt = self.make_fixture()
        sections = self.padded_sections(root, receipt, 0)
        pin = self.write_publication(root, sections)
        packet, raw = self.successful_output(root, receipt)
        self.assertEqual(len(raw), HARD_MAX)
        self.assertEqual(packet["task"]["projection_mode"], "INLINE_EXACT_TASKBOOK_SECTIONS")
        self.assertEqual(packet["task"]["projection"], sections)
        self.assertEqual(packet["task"]["taskbook_blob_sha1"], pin)

    def test_cli_annotation_overflow_falls_back_whole_projection(self):
        root, receipt = self.make_fixture()
        sections = self.padded_sections(root, receipt, 1)
        pin = self.write_publication(root, sections)
        packet, _ = self.successful_output(root, receipt)
        self.assertEqual(packet["task"]["projection_mode"], "EXACT_TASKBOOK_REQUIRED_PACKET_BUDGET")
        self.assertIsNone(packet["task"]["projection"])
        self.assertEqual(packet["task"]["required_task_sections"], list(SECTIONS))
        self.assertEqual(packet["task"]["taskbook_blob_sha1"], pin)
        self.assertEqual(packet["task"]["taskbook_path"], "research_tasks/T1.md")
        for field, value in receipt["route"]["target"].items():
            self.assertEqual(packet["task"][field], value)

    def test_cli_oversize_without_projection_refuses_before_writing(self):
        for has_target in (False, True):
            with self.subTest(has_target=has_target):
                root, receipt = self.make_fixture()
                if has_target:
                    self.write_publication(root, {"Mother question": "Incomplete taskbook."})
                else:
                    receipt["route"]["target"] = None
                    receipt["route"]["action"] = "NO_DISPATCH"
                receipt["route"]["reason"] = "界" * 4000
                completed, output = self.run_cli(root, receipt)
                self.assertNotEqual(completed.returncode, 0)
                self.assertIn("startup packet exceeds 8192 bytes", completed.stderr)
                self.assertFalse(output.exists())

    def test_cli_preserves_existing_no_target_actions_and_claim_flags(self):
        for action, new_claim, preserved in (
            ("NO_DISPATCH", False, False),
            ("ADOPT_OWNER_CLAIM", False, True),
            ("VERIFY_SESSION_LIVENESS", False, True),
        ):
            with self.subTest(action=action):
                root, receipt = self.make_fixture()
                receipt["route"].update(action=action, target=None,
                                        new_claim_required=new_claim, owner_claim_preserved=preserved)
                packet, _ = self.successful_output(root, receipt)
                self.assertEqual(packet["action"], action)
                self.assertIs(packet["new_claim_required"], new_claim)
                self.assertIs(packet["owner_claim_preserved"], preserved)
                self.assertIsNone(packet["task"])
                self.assertIsNone(packet["read_plan"]["first_dependency_ref"])

    def test_cli_taskbook_byte_drift_still_refuses(self):
        root, receipt = self.make_fixture()
        taskbook = root / "research_tasks" / "T1.md"
        taskbook.write_bytes(taskbook.read_bytes() + b"Unregistered byte drift.\n")
        completed, output = self.run_cli(root, receipt)
        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("taskbook blob mismatch", completed.stderr)
        self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
