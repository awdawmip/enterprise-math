from __future__ import annotations

import unittest
from unittest import mock

import research_driver_followup as impl
import research_driver_followup_guard as followup
import research_review_evidence
from tools import research_result_records as results


def gate_rows(**overrides):
    rows = []
    for gate in impl.GATES:
        decision = overrides.get(gate, "NOT_REQUIRED")
        evidence = (
            [f"evidence:{gate}"]
            if decision in {
                "SATISFIED_BY_REVIEWED_RESULT",
                followup.EXISTING_ASSET_DECISION,
            }
            else []
        )
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
    def test_frozen_review_id_not_timestamp_controls_compatibility(self):
        legacy_id = "DR-674A8EC67ED785D968FA"
        legacy = {
            "review_id": legacy_id,
            "review_authority_id": legacy_id,
            "review_authority_kind": "IMMUTABLE_REVIEW",
            "reviewed_at": "2099-01-01T00:00:00+00:00",
        }
        backdated_new = {
            "review_id": "DR-NEW-BACKDATED",
            "review_authority_id": "DR-NEW-BACKDATED",
            "review_authority_kind": "IMMUTABLE_REVIEW",
            "reviewed_at": "2000-01-01T00:00:00+00:00",
        }
        synthesis = {
            "review_id": "RVS-SYNTH",
            "review_authority_id": "RVS-SYNTH",
            "review_authority_kind": "REVIEW_SYNTHESIS",
        }
        self.assertFalse(followup.review_requires_followup(legacy))
        self.assertTrue(followup.review_requires_followup(backdated_new))
        self.assertTrue(followup.review_requires_followup(synthesis))

    def test_baseline_is_pinned_and_current_ids_remain_present(self):
        self.assertEqual([], followup.baseline_audit())
        self.assertEqual(12, len(followup.legacy_review_ids()))

    def test_missing_authority_id_never_gains_legacy_exemption(self):
        self.assertTrue(followup.review_requires_followup({}))

    def test_exact_gate_set_is_required(self):
        rows = gate_rows()
        rows.pop()
        with self.assertRaisesRegex(impl.DriverFollowupError, "exactly"):
            impl._gate_map(rows)

    def test_reviewed_result_satisfaction_requires_evidence(self):
        rows = gate_rows()
        rows[0]["decision"] = "SATISFIED_BY_REVIEWED_RESULT"
        rows[0]["evidence_refs"] = []
        with self.assertRaisesRegex(impl.DriverFollowupError, "requires evidence_refs"):
            impl._gate_map(rows)

    def test_existing_control_asset_satisfaction_requires_evidence(self):
        rows = gate_rows()
        rows[0]["decision"] = followup.EXISTING_ASSET_DECISION
        rows[0]["evidence_refs"] = []
        with self.assertRaisesRegex(impl.DriverFollowupError, "requires evidence_refs"):
            impl._gate_map(rows)

    def test_accepted_review_cannot_skip_external_prior_art(self):
        gates = impl._gate_map(gate_rows())
        review = {
            "disposition": "ACCEPTED",
            "destination_class": "NONE",
        }
        result = {"method_harvest": "RESULT_ONLY"}
        with self.assertRaisesRegex(impl.DriverFollowupError, "EXTERNAL_PRIOR_ART"):
            impl._forced_gate_rules(review, result, gates)

    def test_accepted_review_may_pin_existing_external_prior_art_task(self):
        gates = impl._gate_map(
            gate_rows(EXTERNAL_PRIOR_ART_DUPLICATION=followup.EXISTING_ASSET_DECISION)
        )
        review = {
            "disposition": "ACCEPTED",
            "destination_class": "NONE",
        }
        result = {"method_harvest": "RESULT_ONLY"}
        impl._forced_gate_rules(review, result, gates)

    def test_l4_acceptance_cannot_skip_lean(self):
        gates = impl._gate_map(
            gate_rows(EXTERNAL_PRIOR_ART_DUPLICATION="SATISFIED_BY_REVIEWED_RESULT")
        )
        review = {"disposition": "ACCEPTED", "destination_class": "L4"}
        result = {"method_harvest": "RESULT_ONLY"}
        with self.assertRaisesRegex(impl.DriverFollowupError, "LEAN_FORMALIZATION"):
            impl._forced_gate_rules(review, result, gates)

    def test_request_replication_accepts_already_materialized_replication(self):
        gates = impl._gate_map(
            gate_rows(INDEPENDENT_REPLICATION=followup.EXISTING_ASSET_DECISION)
        )
        review = {
            "disposition": "REQUEST_REPLICATION",
            "destination_class": "REPLICATION",
        }
        result = {"method_harvest": "RESULT_ONLY"}
        impl._forced_gate_rules(review, result, gates)

    def test_request_replication_rejects_missing_replication_asset(self):
        gates = impl._gate_map(gate_rows())
        review = {
            "disposition": "REQUEST_REPLICATION",
            "destination_class": "REPLICATION",
        }
        result = {"method_harvest": "RESULT_ONLY"}
        with self.assertRaisesRegex(impl.DriverFollowupError, "INDEPENDENT_REPLICATION"):
            impl._forced_gate_rules(review, result, gates)


class ExactSetReviewAuthorityFollowupTests(unittest.TestCase):
    def setUp(self):
        self.result = {
            "result_id": "RR-TEST",
            "task_id": "RS-TEST",
            "publication_id": "TP2-TEST",
            "frozen_at": "2026-08-27T09:20:00+00:00",
        }
        self.review1 = {
            "record_schema": results.REVIEW_SCHEMA,
            "review_id": "DR-ONE",
            "result_id": "RR-TEST",
            "task_id": "RS-TEST",
            "publication_id": "TP2-TEST",
            "driver_id": "EM-DVR-ABC123",
            "reviewed_at": "2026-08-27T10:00:00+00:00",
            "disposition": "ACCEPTED",
            "destination_class": "NONE",
            "destination_ref_or_none": "",
            "terminal": True,
        }
        self.review2 = {
            **self.review1,
            "review_id": "DR-TWO",
            "driver_id": "EM-DVR-DEF456",
            "reviewed_at": "2026-08-27T10:01:00+00:00",
        }

    def test_single_review_is_operational_authority(self):
        with (
            mock.patch.object(results, "result_map", return_value={"RR-TEST": self.result}),
            mock.patch.object(results, "iter_reviews", return_value=[self.review1]),
            mock.patch.object(
                research_review_evidence,
                "state",
                return_value={
                    "result_id": "RR-TEST",
                    "review_state": "SINGLE_REVIEW_FLOW",
                    "review_ids": ["DR-ONE"],
                    "review": self.review1,
                    "operational_disposition": "ACCEPTED",
                    "terminal": True,
                },
            ),
        ):
            authority = followup.authority_for_result("RR-TEST")
        self.assertEqual("IMMUTABLE_REVIEW", authority["review_authority_kind"])
        self.assertEqual("DR-ONE", authority["review_authority_id"])
        self.assertEqual(["DR-ONE"], authority["source_review_ids"])

    def test_review_synthesis_not_latest_source_review_is_operational_authority(self):
        synthesis = {
            "synthesis_id": "RVS-ONE",
            "result_id": "RR-TEST",
            "review_ids": ["DR-ONE", "DR-TWO"],
            "operational_disposition": "ACCEPTED",
            "synthesized_by": "EM-DVR-SYN123",
            "terminal": True,
        }
        with (
            mock.patch.object(results, "result_map", return_value={"RR-TEST": self.result}),
            mock.patch.object(results, "iter_reviews", return_value=[self.review1, self.review2]),
            mock.patch.object(
                research_review_evidence,
                "state",
                return_value={
                    "result_id": "RR-TEST",
                    "review_state": "REVIEW_SYNTHESIS_TERMINAL",
                    "review_ids": ["DR-ONE", "DR-TWO"],
                    "synthesis": synthesis,
                    "operational_disposition": "ACCEPTED",
                    "terminal": True,
                },
            ),
        ):
            authority = followup.authority_for_result("RR-TEST")
        self.assertEqual("REVIEW_SYNTHESIS", authority["review_authority_kind"])
        self.assertEqual("RVS-ONE", authority["review_authority_id"])
        self.assertEqual("EM-DVR-SYN123", authority["driver_id"])
        self.assertEqual({"DR-ONE", "DR-TWO"}, set(authority["source_review_ids"]))
        self.assertEqual("NONE", authority["destination_class"])

    def test_mixed_source_destinations_fail_closed_without_synthesized_destination(self):
        review2 = {**self.review2, "destination_class": "L4"}
        synthesis = {
            "synthesis_id": "RVS-MIXED",
            "result_id": "RR-TEST",
            "review_ids": ["DR-ONE", "DR-TWO"],
            "operational_disposition": "ACCEPTED",
            "synthesized_by": "EM-DVR-SYN123",
            "terminal": True,
        }
        with (
            mock.patch.object(results, "result_map", return_value={"RR-TEST": self.result}),
            mock.patch.object(results, "iter_reviews", return_value=[self.review1, review2]),
            mock.patch.object(
                research_review_evidence,
                "state",
                return_value={
                    "result_id": "RR-TEST",
                    "review_state": "REVIEW_SYNTHESIS_TERMINAL",
                    "review_ids": ["DR-ONE", "DR-TWO"],
                    "synthesis": synthesis,
                    "operational_disposition": "ACCEPTED",
                    "terminal": True,
                },
            ),
        ):
            authority = followup.authority_for_result("RR-TEST")
        self.assertIsNone(authority["destination_class"])


class ResultReductionFollowupBarrierTests(unittest.TestCase):
    def setUp(self):
        self.result = {
            "result_id": "RR-TEST",
            "task_id": "RS-TEST",
            "publication_id": "TP2-TEST",
        }
        self.authority = {
            "review_id": "DR-TEST",
            "review_authority_id": "DR-TEST",
            "review_authority_kind": "IMMUTABLE_REVIEW",
            "result_id": "RR-TEST",
            "disposition": "ACCEPTED",
            "destination_class": "NONE",
            "terminal": True,
        }

    def reduced(self):
        return {
            "state": "TERMINAL",
            "result": self.result,
            "review": self.authority,
            "terminal": True,
        }

    def test_governed_authority_without_followup_is_nonterminal(self):
        with mock.patch.object(
            results._driver_followup,
            "state_for_review",
            return_value={
                "required": True,
                "ready": False,
                "state": "AWAITING_FOLLOWUP_TASKSET_PUBLICATION",
                "packet": None,
            },
        ):
            state = results._apply_followup_gate(self.reduced(), self.result, results.ROOT)
        self.assertFalse(state["terminal"])
        self.assertEqual("AWAITING_DRIVER_REVIEW", state["state"])
        self.assertEqual("AWAITING_FOLLOWUP_TASKSET_PUBLICATION", state["driver_followup_state"])

    def test_valid_followup_allows_terminal_authority_to_terminalize(self):
        packet = {"packet_id": "DFU-TEST", "decision": "TASK_SET_PUBLISHED"}
        with mock.patch.object(
            results._driver_followup,
            "state_for_review",
            return_value={
                "required": True,
                "ready": True,
                "state": "FOLLOWUP_TASKSET_READY",
                "packet": packet,
            },
        ):
            state = results._apply_followup_gate(self.reduced(), self.result, results.ROOT)
        self.assertTrue(state["terminal"])
        self.assertEqual("TERMINAL", state["state"])
        self.assertEqual(packet, state["driver_followup"])

    def test_legacy_authority_keeps_compatibility_path(self):
        with mock.patch.object(
            results._driver_followup,
            "state_for_review",
            return_value={
                "required": False,
                "ready": True,
                "state": "LEGACY_PRE_CUTOVER",
                "packet": None,
            },
        ):
            state = results._apply_followup_gate(self.reduced(), self.result, results.ROOT)
        self.assertTrue(state["terminal"])
        self.assertEqual("TERMINAL", state["state"])


if __name__ == "__main__":
    unittest.main()
