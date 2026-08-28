import unittest
from unittest.mock import patch

from tools import research_result_records as records


class ParallelResultReviewCompositionTests(unittest.TestCase):
    def terminal_parallel_state(self):
        return {
            "parallel_state": "PARALLEL_SYNTHESIS_TERMINAL",
            "result_ids": ["RR-A", "RR-B"],
            "intake_id": "PI-1",
            "evidence_set_sha256": "sha256:abc",
        }

    def terminal_synthesis(self):
        return {
            "synthesis_id": "PS-1",
            "_path": "research_parallel_syntheses/RS-T/PS-1.json",
            "terminal_control_disposition": "ACCEPTED",
        }

    def authority(self, result_id: str, *, synthesis: bool = False):
        authority_id = f"RVS-{result_id}" if synthesis else f"DR-{result_id}"
        return {
            "review_id": authority_id,
            "review_authority_id": authority_id,
            "review_authority_kind": "REVIEW_SYNTHESIS" if synthesis else "IMMUTABLE_REVIEW",
            "source_review_ids": [authority_id],
            "result_id": result_id,
            "task_id": "RS-T",
            "publication_id": "TP2-T",
            "driver_id": "EM-DVR-ABC123",
            "reviewed_at": "2026-08-28T00:00:00+00:00",
            "disposition": "ACCEPTED",
            "destination_class": "NONE",
            "destination_ref_or_none": "",
            "terminal": True,
        }

    def followup_ready(self):
        return {
            "required": False,
            "ready": True,
            "state": "LEGACY_PRE_CUTOVER",
            "packet": None,
        }

    def test_new_unresolved_second_review_reopens_old_parallel_terminal_synthesis(self):
        def review_state(result_id, root):
            if result_id == "RR-A":
                return {
                    "result_id": result_id,
                    "review_state": "AWAITING_REVIEW_INTAKE",
                    "review_ids": ["DR-A1", "DR-A2"],
                    "terminal": False,
                }
            return {
                "result_id": result_id,
                "review_state": "SINGLE_REVIEW_FLOW",
                "review_ids": ["DR-B1"],
                "operational_disposition": "ACCEPTED",
                "terminal": True,
            }

        def authority_for(result_id, root):
            return None if result_id == "RR-A" else self.authority("RR-B")

        with patch.object(records._parallel, "state", return_value=self.terminal_parallel_state()), patch.object(
            records, "_parallel_synthesis", return_value=self.terminal_synthesis()
        ), patch.object(records._review_evidence, "state", side_effect=review_state), patch.object(
            records._driver_followup, "authority_for_result", side_effect=authority_for
        ), patch.object(
            records._driver_followup, "state_for_review", return_value=self.followup_ready()
        ):
            out = records.task_result_state("RS-T", publication_id="TP2-T")

        self.assertEqual("AWAITING_DRIVER_REVIEW", out["state"])
        self.assertFalse(out["terminal"])
        self.assertEqual("AWAITING_RESULT_REVIEW_AUTHORITY", out["parallel_state"])
        self.assertEqual(["RR-A"], out["pending_result_review_ids"])

    def test_resolved_review_authority_allows_parallel_terminal_synthesis(self):
        def review_state(result_id, root):
            return {
                "result_id": result_id,
                "review_state": "REVIEW_SYNTHESIS_TERMINAL"
                if result_id == "RR-A"
                else "SINGLE_REVIEW_FLOW",
                "review_ids": ["DR-1", "DR-2"] if result_id == "RR-A" else ["DR-3"],
                "operational_disposition": "ACCEPTED",
                "terminal": True,
            }

        def authority_for(result_id, root):
            return self.authority(result_id, synthesis=result_id == "RR-A")

        with patch.object(records._parallel, "state", return_value=self.terminal_parallel_state()), patch.object(
            records, "_parallel_synthesis", return_value=self.terminal_synthesis()
        ), patch.object(records._review_evidence, "state", side_effect=review_state), patch.object(
            records._driver_followup, "authority_for_result", side_effect=authority_for
        ), patch.object(
            records._driver_followup, "state_for_review", return_value=self.followup_ready()
        ):
            out = records.task_result_state("RS-T", publication_id="TP2-T")

        self.assertEqual("TERMINAL", out["state"])
        self.assertTrue(out["terminal"])
        self.assertEqual("ACCEPTED", out["review"]["disposition"])
        self.assertEqual({"RR-A", "RR-B"}, set(out["result_review_authority"]))
        self.assertEqual(
            {"RR-A", "RR-B"}, set(out["result_operational_review_authority"])
        )

    def test_zero_review_result_blocks_parallel_nonterminal_control_too(self):
        parallel = dict(self.terminal_parallel_state())
        parallel["parallel_state"] = "PARALLEL_SYNTHESIS_NONTERMINAL"
        synthesis = {
            "synthesis_id": "PS-2",
            "_path": "research_parallel_syntheses/RS-T/PS-2.json",
            "disposition": "RETURN_FOR_MORE_RESEARCH",
        }
        with patch.object(records._parallel, "state", return_value=parallel), patch.object(
            records, "_parallel_synthesis", return_value=synthesis
        ), patch.object(
            records._review_evidence,
            "state",
            return_value={"review_state": "NO_REVIEW", "review_ids": [], "terminal": False},
        ):
            out = records.task_result_state("RS-T", publication_id="TP2-T")
        self.assertEqual("AWAITING_DRIVER_REVIEW", out["state"])
        self.assertEqual("AWAITING_RESULT_REVIEW_AUTHORITY", out["parallel_state"])
        self.assertEqual(["RR-A", "RR-B"], out["pending_result_review_ids"])


if __name__ == "__main__":
    unittest.main()
