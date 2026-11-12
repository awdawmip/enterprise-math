import json
import unittest
from pathlib import Path

from control_plane import researcher_startup_packet as startup


ROOT = Path(__file__).resolve().parents[1]


class ResearcherStartupContextEnvelopeTests(unittest.TestCase):
    def test_current_dispatch_receipt_builds_bounded_compact_packet(self):
        receipt_path = ROOT / "control_plane" / "chatgpt_dispatch_receipt.json"
        receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        packet = startup.build_packet(receipt, ROOT)
        policy = json.loads((ROOT / "research_context_budget.json").read_text(encoding="utf-8"))
        cold = policy["researcher_cold_start_envelope"]

        encoded = json.dumps(
            packet, ensure_ascii=False, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
        self.assertLessEqual(len(encoded), cold["compact_packet_hard_max_bytes"])
        self.assertEqual(packet["read_plan"]["reading_budget_mode"], "ADAPTIVE_SOFT_GUIDANCE")
        self.assertFalse(packet["read_plan"]["additional_reads_require_approval"])
        self.assertNotIn("remote_source_reads_before_substantive_math_max", packet["read_plan"])

        # Large diagnostic surfaces must never leak into the ordinary startup packet.
        packet_text = encoded.decode("utf-8")
        self.assertNotIn("quarantined_tasks", packet_text)
        self.assertNotIn("task_integrity_quarantines", packet_text)
        self.assertNotIn("ignored_events", packet_text)
        self.assertNotIn("startup_transport", packet_text)
        self.assertIn("FULL_DISPATCH_RECEIPT_ON_ORDINARY_START", packet_text)
        self.assertIn("HIGH_FANOUT_DIRECTORY_OR_RECURSIVE_TREE_DISCOVERY", packet_text)

        if packet["task"] is not None:
            self.assertTrue(packet["task"]["taskbook_path"])
            self.assertTrue(packet["task"]["taskbook_blob_sha1"].startswith("sha1:"))
            self.assertIn(
                packet["task"]["projection_mode"],
                {
                    "INLINE_EXACT_TASKBOOK_SECTIONS",
                    "EXACT_TASKBOOK_REQUIRED",
                    "EXACT_TASKBOOK_REQUIRED_PACKET_BUDGET",
                },
            )

    def test_reading_targets_are_advisory(self):
        policy = json.loads((ROOT / "research_context_budget.json").read_text(encoding="utf-8"))
        self.assertEqual(policy["reading_autonomy"]["mode"], "ADAPTIVE_SOFT_GUIDANCE")
        self.assertFalse(policy["reading_autonomy"]["approval_required_to_exceed_guidance"])
        self.assertEqual(policy["static_hot_start_guard"]["enforcement"], "REPORT_ONLY")


if __name__ == "__main__":
    unittest.main()

