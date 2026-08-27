import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import research_review_evidence as review_evidence
from tools import research_result_records as result_records


def write_json(path: Path, value: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


class ReviewEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.result_id = "RR-TEST"
        write_json(
            self.root / "research_result_records" / "RS-T1" / f"{self.result_id}.json",
            {
                "result_id": self.result_id,
                "task_id": "RS-T1",
                "publication_id": "TP2-T1",
                "frozen_at": "2026-08-27T00:00:00+00:00",
            },
        )

    def review(self, review_id: str, disposition: str, reviewed_at: str):
        write_json(
            self.root / "research_result_reviews" / self.result_id / f"{review_id}.json",
            {
                "review_id": review_id,
                "result_id": self.result_id,
                "driver_id": f"EM-DVR-{review_id[-4:]}",
                "reviewed_at": reviewed_at,
                "disposition": disposition,
            },
        )

    def test_zero_and_single_review_keep_low_burden_flow(self):
        zero = review_evidence.state(self.result_id, self.root)
        self.assertEqual("NO_REVIEW", zero["review_state"])
        self.review("DR-A001", "ACCEPTED", "2026-08-27T00:01:00+00:00")
        one = review_evidence.state(self.result_id, self.root)
        self.assertEqual("SINGLE_REVIEW_FLOW", one["review_state"])
        self.assertTrue(one["terminal"])
        self.assertFalse((self.root / "research_review_intakes").exists())

    def test_two_reviews_never_latest_win_before_synthesis(self):
        self.review("DR-A001", "ACCEPTED", "2026-08-27T00:01:00+00:00")
        self.review("DR-B002", "REQUEST_REVISION", "2026-08-27T00:02:00+00:00")
        state = review_evidence.state(self.result_id, self.root)
        self.assertEqual("AWAITING_REVIEW_INTAKE", state["review_state"])
        self.assertFalse(state["terminal"])
        self.assertEqual(["DR-A001", "DR-B002"], state["review_ids"])

    def test_two_reference_passes_then_synthesis_controls_disposition(self):
        self.review("DR-A001", "ACCEPTED", "2026-08-27T00:01:00+00:00")
        self.review("DR-B002", "REQUEST_REVISION", "2026-08-27T00:02:00+00:00")
        intake = review_evidence.create_intake(self.result_id, "EM-DVR-OPEN1", self.root)
        state = review_evidence.state(self.result_id, self.root)
        self.assertEqual("AWAITING_REVIEW_REFERENCE_PASS_1", state["review_state"])
        review_evidence.create_reference_pass(
            intake["intake_id"], 1, "EM-DVR-PASS1", "semantic comparison complete",
            "SHARED_CONTROL_CONTEXT_DISCLOSED", self.root,
        )
        state = review_evidence.state(self.result_id, self.root)
        self.assertEqual("AWAITING_REVIEW_REFERENCE_PASS_2", state["review_state"])
        review_evidence.create_reference_pass(
            intake["intake_id"], 2, "EM-DVR-PASS2", "adversarial control comparison complete",
            "CLEAN_INDEPENDENT_CONTEXT", self.root,
        )
        state = review_evidence.state(self.result_id, self.root)
        self.assertEqual("AWAITING_REVIEW_SYNTHESIS", state["review_state"])
        synthesis = review_evidence.create_synthesis(
            intake["intake_id"], "REQUEST_REVISION", "EM-DVR-SYN01",
            "retain both reviews and return for revision", self.root,
        )
        state = review_evidence.state(self.result_id, self.root)
        self.assertEqual("REVIEW_SYNTHESIS_NONTERMINAL", state["review_state"])
        self.assertEqual("REQUEST_REVISION", state["operational_disposition"])
        self.assertFalse(state["terminal"])
        self.assertTrue(synthesis["all_reviews_retained"])
        self.assertFalse(synthesis["latest_review_wins"])

    def test_new_review_invalidates_old_exact_set_synthesis_without_deleting_history(self):
        self.review("DR-A001", "ACCEPTED", "2026-08-27T00:01:00+00:00")
        self.review("DR-B002", "ACCEPTED", "2026-08-27T00:02:00+00:00")
        intake = review_evidence.create_intake(self.result_id, "EM-DVR-OPEN1", self.root)
        review_evidence.create_reference_pass(
            intake["intake_id"], 1, "EM-DVR-PASS1", "semantic pass",
            "SHARED_CONTROL_CONTEXT_DISCLOSED", self.root,
        )
        review_evidence.create_reference_pass(
            intake["intake_id"], 2, "EM-DVR-PASS2", "control pass",
            "CLEAN_INDEPENDENT_CONTEXT", self.root,
        )
        review_evidence.create_synthesis(
            intake["intake_id"], "ACCEPTED", "EM-DVR-SYN01", "two-review synthesis", self.root,
        )
        self.assertTrue(review_evidence.state(self.result_id, self.root)["terminal"])
        self.review("DR-C003", "REQUEST_REPLICATION", "2026-08-27T00:03:00+00:00")
        state = review_evidence.state(self.result_id, self.root)
        self.assertEqual("AWAITING_REVIEW_INTAKE", state["review_state"])
        self.assertFalse(state["terminal"])
        self.assertTrue((self.root / "research_review_syntheses" / self.result_id).exists())

    def test_result_state_uses_review_synthesis_not_latest_review(self):
        self.review("DR-A001", "ACCEPTED", "2026-08-27T00:01:00+00:00")
        self.review("DR-B002", "REQUEST_REVISION", "2026-08-27T00:02:00+00:00")
        with patch.object(
            result_records._parallel,
            "state",
            return_value={"parallel_state": "SINGLE_RESULT_FLOW"},
        ):
            pending = result_records.task_result_state(
                "RS-T1", self.root, publication_id="TP2-T1"
            )
        self.assertEqual("AWAITING_DRIVER_REVIEW", pending["state"])
        self.assertEqual("AWAITING_REVIEW_INTAKE", pending["review_parallel_state"])

        intake = review_evidence.create_intake(self.result_id, "EM-DVR-OPEN1", self.root)
        review_evidence.create_reference_pass(
            intake["intake_id"], 1, "EM-DVR-PASS1", "semantic pass",
            "SHARED_CONTROL_CONTEXT_DISCLOSED", self.root,
        )
        review_evidence.create_reference_pass(
            intake["intake_id"], 2, "EM-DVR-PASS2", "control pass",
            "CLEAN_INDEPENDENT_CONTEXT", self.root,
        )
        review_evidence.create_synthesis(
            intake["intake_id"], "ACCEPTED", "EM-DVR-SYN01", "synthesized acceptance", self.root,
        )
        with patch.object(
            result_records._parallel,
            "state",
            return_value={"parallel_state": "SINGLE_RESULT_FLOW"},
        ):
            terminal = result_records.task_result_state(
                "RS-T1", self.root, publication_id="TP2-T1"
            )
        self.assertEqual("TERMINAL", terminal["state"])
        self.assertTrue(terminal["terminal"])
        self.assertEqual("ACCEPTED", terminal["review"]["disposition"])
        self.assertEqual(["DR-A001", "DR-B002"], terminal["parallel_review_ids"])

    def test_audit_accepts_exact_review_chain(self):
        self.review("DR-A001", "ACCEPTED", "2026-08-27T00:01:00+00:00")
        self.review("DR-B002", "ACCEPTED", "2026-08-27T00:02:00+00:00")
        intake = review_evidence.create_intake(self.result_id, "EM-DVR-OPEN1", self.root)
        review_evidence.create_reference_pass(
            intake["intake_id"], 1, "EM-DVR-PASS1", "semantic pass",
            "SHARED_CONTROL_CONTEXT_DISCLOSED", self.root,
        )
        review_evidence.create_reference_pass(
            intake["intake_id"], 2, "EM-DVR-PASS2", "control pass",
            "CLEAN_INDEPENDENT_CONTEXT", self.root,
        )
        review_evidence.create_synthesis(
            intake["intake_id"], "ACCEPTED", "EM-DVR-SYN01", "accepted after two passes", self.root,
        )
        self.assertEqual([], review_evidence.audit(self.root))


if __name__ == "__main__":
    unittest.main()
