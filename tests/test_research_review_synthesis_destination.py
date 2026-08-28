import json
import tempfile
import unittest
from pathlib import Path

import research_driver_followup_guard as followup
import research_review_evidence as review_evidence


def write_json(path: Path, value: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


class ReviewSynthesisDestinationTests(unittest.TestCase):
    def setup_chain(self, root: Path, destination_a: str, destination_b: str):
        result_id = "RR-DEST"
        write_json(
            root / "research_result_records" / "RS-DEST" / f"{result_id}.json",
            {
                "result_id": result_id,
                "task_id": "RS-DEST",
                "publication_id": "TP2-DEST",
                "frozen_at": "2026-08-28T00:00:00+00:00",
            },
        )
        for index, destination in enumerate((destination_a, destination_b), start=1):
            review_id = f"DR-D{index:03d}"
            write_json(
                root / "research_result_reviews" / result_id / f"{review_id}.json",
                {
                    "record_schema": review_evidence.REVIEW_SCHEMA,
                    "review_id": review_id,
                    "result_id": result_id,
                    "task_id": "RS-DEST",
                    "publication_id": "TP2-DEST",
                    "driver_id": f"EM-DVR-D{index:03d}",
                    "reviewed_at": f"2026-08-28T00:0{index}:00+00:00",
                    "disposition": "ACCEPTED",
                    "destination_class": destination,
                    "destination_ref_or_none": "",
                    "terminal": True,
                },
            )
        intake = review_evidence.create_intake(result_id, "EM-DVR-OPEN1", root)
        review_evidence.create_reference_pass(
            intake["intake_id"],
            1,
            "EM-DVR-PASS1",
            "semantic comparison complete",
            "SHARED_CONTROL_CONTEXT_DISCLOSED",
            root,
        )
        review_evidence.create_reference_pass(
            intake["intake_id"],
            2,
            "EM-DVR-PASS2",
            "adversarial control comparison complete",
            "CLEAN_INDEPENDENT_CONTEXT",
            root,
        )
        return result_id, intake

    def test_explicit_synthesis_destination_resolves_mixed_source_destinations(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            result_id, intake = self.setup_chain(root, "NONE", "L4")
            synthesis = review_evidence.create_synthesis(
                intake["intake_id"],
                "ACCEPTED",
                "EM-DVR-SYN01",
                "synthesize one operational destination after exact-set review",
                root,
                operational_destination_class="TOOL",
                operational_destination_ref_or_none="TP2-TOOL-NEXT",
            )
            self.assertEqual("TOOL", synthesis["operational_destination_class"])
            self.assertEqual(
                "TP2-TOOL-NEXT", synthesis["operational_destination_ref_or_none"]
            )
            state = review_evidence.state(result_id, root)
            self.assertEqual("REVIEW_SYNTHESIS_TERMINAL", state["review_state"])
            self.assertEqual(
                "TOOL", state["synthesis"]["operational_destination_class"]
            )
            sources = review_evidence.reviews_for_result(result_id, root)
            destination, destination_ref = followup._synthesis_destination(
                state["synthesis"], sources
            )
            self.assertEqual("TOOL", destination)
            self.assertEqual("TP2-TOOL-NEXT", destination_ref)
            self.assertEqual([], review_evidence.audit(root))

    def test_invalid_explicit_synthesis_destination_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            _, intake = self.setup_chain(root, "NONE", "L4")
            with self.assertRaisesRegex(
                review_evidence.ReviewEvidenceError,
                "operational_destination_class",
            ):
                review_evidence.create_synthesis(
                    intake["intake_id"],
                    "ACCEPTED",
                    "EM-DVR-SYN01",
                    "invalid destination must fail closed",
                    root,
                    operational_destination_class="LATEST_REVIEW_WINS",
                )

    def test_omitted_synthesis_destination_preserves_common_source_inference(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            result_id, intake = self.setup_chain(root, "NONE", "NONE")
            synthesis = review_evidence.create_synthesis(
                intake["intake_id"],
                "ACCEPTED",
                "EM-DVR-SYN01",
                "common source destination remains backward compatible",
                root,
            )
            self.assertNotIn("operational_destination_class", synthesis)
            sources = review_evidence.reviews_for_result(result_id, root)
            destination, destination_ref = followup._synthesis_destination(
                synthesis, sources
            )
            self.assertEqual("NONE", destination)
            self.assertEqual("", destination_ref)
            self.assertEqual([], review_evidence.audit(root))


if __name__ == "__main__":
    unittest.main()
