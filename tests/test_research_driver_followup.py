from __future__ import annotations

import unittest
from unittest import mock

import research_driver_followup as followup
from tools import research_result_records as results


def gate_rows(**overrides):
    rows = []
    for gate in followup.GATES:
        decision = overrides.get(gate, "NOT_REQUIRED")
        evidence = [f"evidence:{gate}"] if decision == "SATISFIED_BY_REVIEWED_RESULT" else []
        rows.append(
            {
                "gate": gate,
                "decision": decision,
                "reason": f"reason for {gate}",
                "evidence_refs": evidence,
            }
        )
    return rows


class DriverFollowupContractTests(unittest.TestCase):
    def test_cutover_is_fail_closed_for_new_reviews(self):
        legacy = {"reviewed_at": "2026-08-27T09:18:59+00:00"}
        current = {"reviewed_at": "2026-08-27T09:19:00+00:00"}
        self.assertFalse(followup.review_requires_followup(legacy))
        self.assertTrue(followup.review_requires_followup(current))

    def test_exact_gate_set_is_required(self):
        rows = gate_rows()
        rows.pop()
        with self.assertRaisesRegex(followup.DriverFollowupError, "exactly"):
            followup._gate_map(rows)

    def test_satisfied_gate_requires_evidence(self):
        rows = gate_rows()
        rows[0]["decision"] = "SATISFIED_BY_REVIEWED_RESULT"
        rows[0]["evidence_refs"] = []
        with self.assertRaisesRegex(followup.DriverFollowupError, "requires evidence_refs"):
            followup._gate_map(rows)

    def test_accepted_review_cannot_skip_external_prior_art(self):
        gates = followup._gate_map(gate_rows())
        review = {"disposition": "ACCEPTED", "destination_class": "NONE"}
        result = {"method_harvest": "RESULT_ONLY"}
        with self.assertRaisesRegex(followup.DriverFollowupError, "EXTERNAL_PRIOR_ART"):
            followup._forced_gate_rules(review, result, gates)

    def test_l4_acceptance_cannot_skip_lean(self):
        gates = followup._gate_map(
            gate_rows(EXTERNAL_PRIOR_ART_DUPLICATION="SATISFIED_BY_REVIEWED_RESULT")
        )
        review = {"disposition": "ACCEPTED", "destination_class": "L4"}
        result = {"method_harvest": "RESULT_ONLY"}
        with self.assertRaisesRegex(followup.DriverFollowupError, "LEAN_FORMALIZATION"):
            followup._forced_gate_rules(review, result, gates)

    def test_request_replication_requires_replication_task_gate(self):
        gates = followup._gate_map(gate_rows())
        review = {"disposition": "REQUEST_REPLICATION", "destination_class": "REPLICATION"}
        result = {"method_harvest": "RESULT_ONLY"}
        with self.assertRaisesRegex(followup.DriverFollowupError, "INDEPENDENT_REPLICATION"):
            followup._forced_gate_rules(review, result, gates)


class ResultReductionFollowupBarrierTests(unittest.TestCase):
    def setUp(self):
        self.result = {
            "result_id": "RR-TEST",
            "task_id": "RS-TEST",
            "publication_id": "TP2-TEST",
            "frozen_at": "2026-08-27T09:20:00+00:00",
        }
        self.review = {
            "review_id": "DR-TEST",
            "result_id": "RR-TEST",
            "disposition": "ACCEPTED",
            "reviewed_at": "2026-08-27T09:20:00+00:00",
        }

    def test_post_cutover_review_without_followup_is_nonterminal(self):
        with (
            mock.patch.object(results, "iter_results", return_value=[self.result]),
            mock.patch.object(results, "latest_review", return_value=self.review),
            mock.patch.object(
                results._driver_followup,
                "state_for_review",
                return_value={
                    "required": True,
                    "ready": False,
                    "state": "AWAITING_FOLLOWUP_TASKSET_PUBLICATION",
                    "packet": None,
                },
            ),
        ):
            state = results._single_result_state("RS-TEST", results.ROOT, "TP2-TEST")
        self.assertFalse(state["terminal"])
        self.assertEqual("AWAITING_DRIVER_REVIEW", state["state"])
        self.assertEqual(
            "AWAITING_FOLLOWUP_TASKSET_PUBLICATION",
            state["driver_followup_state"],
        )

    def test_valid_followup_allows_terminal_review_to_terminalize(self):
        packet = {"packet_id": "DFU-TEST", "decision": "TASK_SET_PUBLISHED"}
        with (
            mock.patch.object(results, "iter_results", return_value=[self.result]),
            mock.patch.object(results, "latest_review", return_value=self.review),
            mock.patch.object(
                results._driver_followup,
                "state_for_review",
                return_value={
                    "required": True,
                    "ready": True,
                    "state": "FOLLOWUP_TASKSET_READY",
                    "packet": packet,
                },
            ),
        ):
            state = results._single_result_state("RS-TEST", results.ROOT, "TP2-TEST")
        self.assertTrue(state["terminal"])
        self.assertEqual("TERMINAL", state["state"])
        self.assertEqual(packet, state["driver_followup"])

    def test_legacy_review_keeps_compatibility_path(self):
        with (
            mock.patch.object(results, "iter_results", return_value=[self.result]),
            mock.patch.object(results, "latest_review", return_value=self.review),
            mock.patch.object(
                results._driver_followup,
                "state_for_review",
                return_value={
                    "required": False,
                    "ready": True,
                    "state": "LEGACY_PRE_CUTOVER",
                    "packet": None,
                },
            ),
        ):
            state = results._single_result_state("RS-TEST", results.ROOT, "TP2-TEST")
        self.assertTrue(state["terminal"])
        self.assertEqual("TERMINAL", state["state"])


if __name__ == "__main__":
    unittest.main()
