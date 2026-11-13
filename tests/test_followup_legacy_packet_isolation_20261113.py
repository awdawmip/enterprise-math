"""Regression: historical V1_3 follow-ups do not poison current packet validation."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import research_driver_followup as followup


class LegacyFollowupPacketIsolationTests(unittest.TestCase):
    @staticmethod
    def write_packet(root: Path, review_id: str, packet_id: str, value: dict) -> None:
        path = root / "research_driver_followups" / review_id / (packet_id + ".json")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(value, sort_keys=True), encoding="utf-8")

    def test_legacy_followup_id_is_preserved_but_excluded_from_current_packet_index(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.write_packet(
                root, "DR-LEGACY", "DFU-LEGACY",
                {
                    "schema": "ENTERPRISE_MATH_RESEARCH_DRIVER_FOLLOWUP_V1_3",
                    "followup_id": "DFU-LEGACY",
                    "review_id": "DR-LEGACY",
                    "decision": "TASK_SET_PUBLISHED",
                },
            )
            self.write_packet(
                root, "DR-CURRENT", "DFU-CURRENT",
                {
                    "schema": followup.SCHEMA,
                    "policy": followup.POLICY,
                    "packet_id": "DFU-CURRENT",
                    "review_id": "DR-CURRENT",
                    "decision": "TASK_SET_PUBLISHED",
                },
            )
            indexed = followup.packet_map(root)
            self.assertEqual({"DR-CURRENT"}, set(indexed))
            self.assertEqual("DFU-CURRENT", indexed["DR-CURRENT"]["packet_id"])
            self.assertTrue(
                (root / "research_driver_followups" / "DR-LEGACY" / "DFU-LEGACY.json").is_file()
            )

    def test_checked_in_legacy_baseline_does_not_poison_current_packet_map(self):
        root = Path(__file__).resolve().parents[1]
        legacy = (
            root / "research_driver_followups"
            / "DR-2C7E91A4B5D8063F1248"
            / "DFU-6F1A4C8E2D9057B3A216.json"
        )
        self.assertTrue(legacy.is_file())
        record = json.loads(legacy.read_text(encoding="utf-8"))
        self.assertEqual("ENTERPRISE_MATH_RESEARCH_DRIVER_FOLLOWUP_V1_3", record["schema"])
        self.assertEqual("DFU-6F1A4C8E2D9057B3A216", record["followup_id"])
        self.assertNotIn("packet_id", record)
        indexed = followup.packet_map(root)
        self.assertNotIn("DR-2C7E91A4B5D8063F1248", indexed)
        self.assertEqual(
            "DFU-E7CBFD0E9958AF25E942",
            indexed["DR-CE3F008C48F9EBBFF9FA"]["packet_id"],
        )

    def test_pretyped_accepted_review_binds_its_exact_existing_task(self):
        # Original 2026-08-30 accepted GEO6 review has a canonical immutable
        # schema but predates the explicit review_authority_kind field.
        root = Path(__file__).resolve().parents[1]
        review_path = (
            root / "research_result_reviews" / "RR-547A186EBDE5EE6CD8A3"
            / "DR-CE3F008C48F9EBBFF9FA.json"
        )
        pub_path = (
            root / "research_task_records"
            / "RS-GEO6-SECONDWAVE-PACKING-KAKEYA-PRIOR-ART-SYNTHESIS"
            / "TP2-B531F3BB4A597B7D3EAF.json"
        )
        review = json.loads(review_path.read_text(encoding="utf-8"))
        publication = json.loads(pub_path.read_text(encoding="utf-8"))
        self.assertEqual(followup.result_impl.REVIEW_SCHEMA, review["record_schema"])
        self.assertNotIn("review_authority_kind", review)
        self.assertEqual("ACCEPTED", review["disposition"])
        row = {"task_id": publication["task_id"],
               "publication_id": publication["publication_id"],
               "task_role": "INTEGRATION_OR_TOOL_HARVEST"}
        pins = followup._existing_published_task_pins(
            review, [row], {}, publication["parent_objective_id"], root,
            bound_at="2026-11-13T10:20:00+00:00",
        )
        self.assertEqual(publication["publication_id"], pins[0]["publication_id"])
        self.assertEqual(publication["task_id"], pins[0]["task_id"])
        bad = dict(review, review_authority_kind="REVIEW_SYNTHESIS")
        with self.assertRaisesRegex(
            followup.DriverFollowupError,
            "existing published Task requires one operational",
        ):
            followup._existing_published_task_pins(
                bad, [row], {}, publication["parent_objective_id"], root,
                bound_at="2026-11-13T10:20:00+00:00",
            )

    def test_malformed_current_schema_still_fails_packet_id_validation(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.write_packet(
                root, "DR-BAD", "DFU-BAD",
                {"schema": followup.SCHEMA, "review_id": "DR-BAD"},
            )
            with self.assertRaisesRegex(followup.DriverFollowupError, "packet_id is invalid"):
                followup.packet_map(root)

    def test_unknown_schema_is_not_silently_ignored(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            self.write_packet(
                root, "DR-UNKNOWN", "DFU-UNKNOWN",
                {"schema": "UNKNOWN_FOLLOWUP_SCHEMA_V99", "review_id": "DR-UNKNOWN"},
            )
            with self.assertRaisesRegex(followup.DriverFollowupError, "unsupported follow-up schema"):
                followup.packet_map(root)


if __name__ == "__main__":
    unittest.main()
