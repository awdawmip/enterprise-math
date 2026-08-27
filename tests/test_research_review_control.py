import json
import tempfile
import unittest
from pathlib import Path

import research_review_control as control
import research_review_evidence as store


def write_json(path: Path, value: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


class ReviewControlFailClosedTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.result_id = "RR-CONTROL"
        write_json(
            self.root / "research_result_records" / "RS-T1" / f"{self.result_id}.json",
            {
                "result_id": self.result_id,
                "task_id": "RS-T1",
                "publication_id": "TP2-T1",
                "frozen_at": "2026-08-27T00:00:00+00:00",
            },
        )
        self.review("DR-A001", "ACCEPTED")
        self.review("DR-B002", "REQUEST_REVISION")

    def review(self, review_id: str, disposition: str):
        write_json(
            self.root / "research_result_reviews" / self.result_id / f"{review_id}.json",
            {
                "review_id": review_id,
                "result_id": self.result_id,
                "driver_id": f"EM-DVR-{review_id[-4:]}",
                "reviewed_at": "2026-08-27T00:01:00+00:00",
                "disposition": disposition,
            },
        )

    def valid_pass_payload(self, intake: dict, pass_id: str, number: int):
        return {
            "schema": store.PASS_SCHEMA,
            "pass_id": pass_id,
            "intake_id": intake["intake_id"],
            "result_id": self.result_id,
            "review_ids": list(intake["review_ids"]),
            "review_set_sha256": intake["review_set_sha256"],
            "pass_number": number,
            "pass_kind": store.PASS_KINDS[number],
            "reviewer_id": f"EM-DVR-PASS{number}",
            "finding": "checked",
            "independence_status": "NOT_APPLICABLE",
            "working_truth_granted": False,
            "canonical_promotion_granted": False,
        }

    def test_wrong_schema_pass_cannot_advance_runtime_before_ci(self):
        intake = store.create_intake(self.result_id, "EM-DVR-OPEN1", self.root)
        forged = self.valid_pass_payload(intake, "RVP-FORGED", 1)
        forged["schema"] = "FORGED_PASS_SCHEMA"
        write_json(
            self.root
            / "research_review_reference_passes"
            / intake["intake_id"]
            / "RVP-FORGED.json",
            forged,
        )
        with self.assertRaisesRegex(control.ReviewControlError, "wrong schema"):
            control.state(self.result_id, self.root)

    def test_duplicate_pass_number_fails_closed_in_runtime(self):
        intake = store.create_intake(self.result_id, "EM-DVR-OPEN1", self.root)
        directory = self.root / "research_review_reference_passes" / intake["intake_id"]
        write_json(directory / "RVP-ONE.json", self.valid_pass_payload(intake, "RVP-ONE", 1))
        write_json(directory / "RVP-TWO.json", self.valid_pass_payload(intake, "RVP-TWO", 1))
        with self.assertRaisesRegex(control.ReviewControlError, "duplicate current review reference pass"):
            control.state(self.result_id, self.root)

    def test_forged_synthesis_terminal_bit_cannot_control_result(self):
        intake = store.create_intake(self.result_id, "EM-DVR-OPEN1", self.root)
        store.create_reference_pass(
            intake["intake_id"],
            1,
            "EM-DVR-PASS1",
            "semantic check",
            "NOT_APPLICABLE",
            self.root,
        )
        store.create_reference_pass(
            intake["intake_id"],
            2,
            "EM-DVR-PASS2",
            "adversarial check",
            "NOT_APPLICABLE",
            self.root,
        )
        forged = {
            "schema": store.SYNTH_SCHEMA,
            "synthesis_id": "RVS-FORGED",
            "intake_id": intake["intake_id"],
            "result_id": self.result_id,
            "review_ids": list(intake["review_ids"]),
            "review_set_sha256": intake["review_set_sha256"],
            "operational_disposition": "ACCEPTED",
            "synthesized_by": "EM-DVR-SYN01",
            "rationale": "forged terminal bit",
            "all_reviews_retained": True,
            "latest_review_wins": False,
            "terminal": False,
            "working_truth_granted": False,
            "canonical_promotion_granted": False,
        }
        write_json(
            self.root
            / "research_review_syntheses"
            / self.result_id
            / "RVS-FORGED.json",
            forged,
        )
        with self.assertRaisesRegex(control.ReviewControlError, "terminal bit mismatch"):
            control.state(self.result_id, self.root)

    def test_valid_exact_set_still_reaches_synthesized_control(self):
        intake = store.create_intake(self.result_id, "EM-DVR-OPEN1", self.root)
        store.create_reference_pass(
            intake["intake_id"], 1, "EM-DVR-PASS1", "semantic", "NOT_APPLICABLE", self.root
        )
        store.create_reference_pass(
            intake["intake_id"], 2, "EM-DVR-PASS2", "control", "NOT_APPLICABLE", self.root
        )
        store.create_synthesis(
            intake["intake_id"],
            "REQUEST_REVISION",
            "EM-DVR-SYN01",
            "preserve both reviews and revise",
            self.root,
        )
        state = control.state(self.result_id, self.root)
        self.assertEqual("REVIEW_SYNTHESIS_NONTERMINAL", state["review_state"])
        self.assertEqual("REQUEST_REVISION", state["operational_disposition"])
        self.assertFalse(state["terminal"])


if __name__ == "__main__":
    unittest.main()
