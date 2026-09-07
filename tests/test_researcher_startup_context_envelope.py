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
        self.assertLessEqual(
            packet["read_plan"]["remote_source_reads_before_substantive_math_max"],
            2,
        )

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

    def test_component_ceiling_sum_fits_hard_envelope(self):
        policy = json.loads((ROOT / "research_context_budget.json").read_text(encoding="utf-8"))
        cold = policy["researcher_cold_start_envelope"]
        components = cold["component_hard_max_bytes"]
        self.assertEqual(sum(components.values()), cold["component_hard_max_sum_bytes"])
        self.assertLessEqual(
            cold["component_hard_max_sum_bytes"], cold["cold_start_raw_hard_max_bytes"]
        )
        self.assertLessEqual(cold["cold_start_raw_soft_max_bytes"], 65536)
        self.assertLessEqual(cold["cold_start_raw_hard_max_bytes"], 81920)


if __name__ == "__main__":
    unittest.main()
