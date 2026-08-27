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

        with patch.object(records._parallel, "state", return_value=self.terminal_parallel_state()), patch.object(
            records, "_parallel_synthesis", return_value=self.terminal_synthesis()
        ), patch.object(records._review_evidence, "state", side_effect=review_state):
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

        with patch.object(records._parallel, "state", return_value=self.terminal_parallel_state()), patch.object(
            records, "_parallel_synthesis", return_value=self.terminal_synthesis()
        ), patch.object(records._review_evidence, "state", side_effect=review_state):
            out = records.task_result_state("RS-T", publication_id="TP2-T")

        self.assertEqual("TERMINAL", out["state"])
        self.assertTrue(out["terminal"])
        self.assertEqual("ACCEPTED", out["review"]["disposition"])
        self.assertEqual({"RR-A", "RR-B"}, set(out["result_review_authority"]))

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
