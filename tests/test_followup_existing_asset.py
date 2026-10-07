"""Existing integration routing binds evidence without creating successor work."""
import copy
from contextlib import ExitStack
import unittest
import subprocess
import sys
from unittest import mock

import research_driver_followup as impl
from control_plane import research_driver_followup_transaction as transaction
from tests import test_followup_current_publisher as fixture
from tests.test_followup_current_publisher import CURRENT, ORIGINAL, SESSION, CREATED, write_json
from tools import research_task_records


class ExistingAssetTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixture.CurrentPublisherBindingTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.tearDown)
        self.root = self.fixture.root
        self.review = self.fixture.review
        self.review.update(review_authority_kind="REVIEW_SYNTHESIS",
                           destination_class="FOLLOWUP_TASK",
                           destination_ref_or_none="RS-INTEGRATION/TP2-EXISTING")
        self.review["source_review_ids"] = ["DR-OLD", "DR-SECOND"]
        second = {key: value for key, value in self.review.items() if not key.startswith("_")}
        second["review_id"] = "DR-SECOND"
        write_json(self.root / "research_result_reviews/RR-OLD/DR-SECOND.json", second)
        self.synthesis_path = self.root / "research_review_syntheses/RR-OLD/DR-OLD.json"
        synthesis = {"schema": "ENTERPRISE_MATH_REVIEW_SYNTHESIS_V1", "synthesis_id": "DR-OLD",
                     "result_id": "RR-OLD", "review_ids": ["DR-OLD", "DR-SECOND"],
                     "synthesized_by": ORIGINAL, "operational_disposition": "ACCEPTED",
                     "operational_destination_class": "FOLLOWUP_TASK",
                     "operational_destination_ref_or_none": "RS-INTEGRATION/TP2-EXISTING"}
        write_json(self.synthesis_path, synthesis)
        self.review["review_synthesis"] = synthesis
        path = self.root / "research_tasks/integration.md"
        path.parent.mkdir(parents=True)
        path.write_text("# Existing integration task\n", encoding="utf-8")
        self.asset = {
            "record_schema": "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2",
            "record_state": "ACTIVE", "task_id": "RS-INTEGRATION",
            "publication_id": "TP2-EXISTING", "publication_generation": 1,
            "supersedes_publication_id": None, "publisher_role": "RESEARCH_DRIVER",
            "publisher_id": "EM-DVR-PRIOR123", "published_at": "2026-08-30T00:00:00+00:00",
            "parent_objective_id": "PO-OLD", "task_lineage": "INTEGRATION",
            "taskbook_path": "research_tasks/integration.md",
            "taskbook_blob_sha1": research_task_records.taskbook_blob(path),
        }
        self.asset_path = self.root / "research_task_records/RS-INTEGRATION/TP2-EXISTING.json"
        write_json(self.asset_path, self.asset)
        self.current = {"RS-INTEGRATION": self.asset,
                        "RS-OLD": {"publication_id": "TP2-OLD"}}
        self.spec = {
            "decision": impl.EXISTING_ASSET_DECISION, "tasks": [],
            "existing_task_publications": [{"task_id": "RS-INTEGRATION",
                "publication_id": "TP2-EXISTING", "task_role": "INTEGRATION_OR_TOOL_HARVEST"}],
            "gate_decisions": [{"gate": gate, "decision": "SATISFIED_BY_REVIEWED_RESULT",
                "reason": "Bounded review evidence", "evidence_refs": ["RR-OLD"]} for gate in impl.GATES],
        }
        self.spec["gate_decisions"][4].update(decision="SATISFIED_BY_EXISTING_CONTROL_ASSET",
                                              evidence_refs=["RS-INTEGRATION/TP2-EXISTING"])
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        for patch in (
            mock.patch.object(impl, "review_requires_followup", return_value=True),
            mock.patch.object(impl, "_source_parent_objective", return_value="PO-OLD"),
            mock.patch.object(research_task_records, "current_records", side_effect=lambda root: self.current),
            mock.patch.object(transaction, "_candidate_post_audit", side_effect=self.post_audit),
        ):
            self.stack.enter_context(patch)

    def post_audit(self, packet, root, **kwargs):
        transaction._validate_packet_candidate(packet, root, persisted=True)
        return []

    def materialize(self, *, spec=None, authorized=True):
        args = {"publishing_driver_id": CURRENT, "publisher_session_id": SESSION} if authorized else {}
        return transaction.materialize(review_id="DR-OLD", spec=spec or self.spec,
                                       created_at=CREATED, root=self.root, **args)

    def assert_no_packet(self):
        self.assertEqual([], list((self.root / "research_driver_followups").glob("*/*.json")))

    def test_reuses_old_publication_without_republishing_or_closing(self):
        originals = {path: path.read_bytes() for path in self.root.rglob("*") if path.is_file()}
        packet = self.materialize()
        impl.validate_packet(packet, self.root)
        self.assertEqual([], packet["task_publications"])
        self.assertEqual(self.spec["existing_task_publications"], packet["existing_task_publications"])
        self.assertEqual(ORIGINAL, packet["driver_id"])
        self.assertEqual(CURRENT, packet["materialization_publisher"]["driver_id"])
        self.assertFalse(packet["parent_completion_granted"])
        self.assertFalse(packet["parent_final_granted"])
        self.assertNotIn("terminal_scope", packet)
        for path, before in originals.items():
            self.assertEqual(before, path.read_bytes())
        added = {path for path in self.root.rglob("*") if path.is_file()} - originals.keys()
        self.assertEqual({self.root / packet["record_path"]}, added)
        state = impl.state_for_review("DR-OLD", self.root)
        self.assertTrue(state["ready"])
        self.assertEqual("EXISTING_CONTROL_ASSET_READY", state["state"])

    def test_requires_current_authorized_publisher(self):
        with self.assertRaisesRegex(transaction.DriverFollowupTransactionError, "authenticated current publisher"):
            self.materialize(authorized=False)
        self.assert_no_packet()

    def test_rejects_stale_source_or_destination_before_write(self):
        for task in ("RS-OLD", "RS-INTEGRATION"):
            before = self.current[task]
            self.current[task] = {"publication_id": "TP2-NEWER"}
            with self.assertRaisesRegex(impl.DriverFollowupError, "current"):
                self.materialize()
            self.current[task] = before
            self.assert_no_packet()

    def test_rejects_wrong_destination_and_cross_parent(self):
        self.review["destination_ref_or_none"] = "RS-OTHER/TP2-OTHER"
        with self.assertRaisesRegex(impl.DriverFollowupError, "exact synthesis destination"):
            self.materialize()
        self.review["destination_ref_or_none"] = "RS-INTEGRATION/TP2-EXISTING"
        self.asset["parent_objective_id"] = "PO-OTHER"
        write_json(self.asset_path, self.asset)
        with self.assertRaisesRegex(impl.DriverFollowupError, "same parent"):
            self.materialize()
        self.assert_no_packet()

    def test_rejects_duplicate_work_closure_and_other_gate_bypass(self):
        for changes in (
            {"tasks": [{"task_id": "RS-NEW"}]},
            {"terminal_scope": "TASK"},
            {"portfolio_continuation": {}},
            {"existing_task_publications": []},
        ):
            with self.subTest(changes=changes), self.assertRaises((impl.DriverFollowupError, transaction.DriverFollowupTransactionError)):
                self.materialize(spec={**self.spec, **changes})
        spec = copy.deepcopy(self.spec)
        spec["gate_decisions"][1].update(decision="SATISFIED_BY_EXISTING_CONTROL_ASSET",
                                        evidence_refs=["RS-INTEGRATION/TP2-EXISTING"])
        with self.assertRaisesRegex(impl.DriverFollowupError, "another follow-up gate"):
            self.materialize(spec=spec)
        self.assert_no_packet()

    def test_raw_publication_and_taskbook_drift_fail_validation(self):
        packet = self.materialize()
        before = self.asset_path.read_bytes()
        self.asset_path.write_bytes(before + b"\n")
        with self.assertRaisesRegex(impl.DriverFollowupError, "pin drift"):
            impl.validate_packet(packet, self.root)
        self.asset_path.write_bytes(before)
        path = self.root / self.asset["taskbook_path"]
        path.write_bytes(path.read_bytes() + b"changed\n")
        with self.assertRaisesRegex(impl.DriverFollowupError, "taskbook blob drift"):
            impl.validate_packet(packet, self.root)

    def test_raw_synthesis_drift_invalidates_binding_without_rewriting_reviews(self):
        packet = self.materialize()
        self.synthesis_path.write_bytes(self.synthesis_path.read_bytes() + b"\n")
        with self.assertRaisesRegex(impl.DriverFollowupError, "synthesis pin drift"):
            impl.validate_packet(packet, self.root)

    def test_postwrite_asset_drift_rolls_back_only_new_packet(self):
        before = self.asset_path.read_bytes()
        def drift(packet, root, **kwargs):
            self.asset_path.write_bytes(before + b"\n")
            return self.post_audit(packet, root, **kwargs)
        with mock.patch.object(transaction, "_candidate_post_audit", side_effect=drift):
            with self.assertRaisesRegex(transaction.DriverFollowupTransactionError, "pin drift"):
                self.materialize()
        self.assert_no_packet()
        self.assertEqual(before + b"\n", self.asset_path.read_bytes())

    def test_historical_binding_survives_later_publication(self):
        packet = self.materialize()
        self.current["RS-INTEGRATION"] = {"publication_id": "TP2-LATER"}
        impl.validate_packet(packet, self.root)
        with self.assertRaisesRegex(impl.DriverFollowupError, "current operational publication"):
            impl.validate_packet(packet, self.root, current_publication_required=True)

    def add_continued_destination(self):
        newer = {**self.asset, "publication_id": "TP2-CURRENT", "publication_generation": 2,
                 "supersedes_publication_id": "TP2-EXISTING", "task_lineage": "MAINTENANCE",
                 "taskbook_path": "research_tasks/current.md"}
        taskbook = self.root / newer["taskbook_path"]
        taskbook.write_text("# Authorized same-task maintenance\n", encoding="utf-8")
        newer["taskbook_blob_sha1"] = research_task_records.taskbook_blob(taskbook)
        path = self.asset_path.with_name("TP2-CURRENT.json")
        write_json(path, newer)
        self.current["RS-INTEGRATION"] = newer
        self.spec["current_destination_continuation"] = {
            "publication_id": "TP2-CURRENT",
            "rationale": "Driver fixture explicitly retains integration routing through the current maintenance generation.",
            "evidence_refs": ["RS-INTEGRATION/TP2-EXISTING", "RS-INTEGRATION/TP2-CURRENT"],
        }
        return newer, path

    def test_explicit_driver_continuation_preserves_synthesis_and_full_chain(self):
        self.add_continued_destination()
        before = self.review["destination_ref_or_none"]
        packet = self.materialize()
        self.assertEqual(before, self.review["destination_ref_or_none"])
        self.assertEqual("TP2-EXISTING", packet["existing_task_publications"][0]["publication_id"])
        self.assertEqual(["TP2-EXISTING", "TP2-CURRENT"],
                         [pin["publication_id"] for pin in packet["existing_asset_pins"]])
        self.assertEqual("TP2-CURRENT", packet["current_destination_continuation"]["publication_id"])
        self.assertEqual([], packet["task_publications"])
        impl.validate_packet(packet, self.root, current_publication_required=True)

    def test_never_implicitly_advances_or_uses_quarantined_head(self):
        self.add_continued_destination()
        continuation = self.spec.pop("current_destination_continuation")
        with self.assertRaisesRegex(impl.DriverFollowupError, "explicitly continue"):
            self.materialize()
        self.spec["current_destination_continuation"] = continuation
        self.current.pop("RS-INTEGRATION")
        with self.assertRaisesRegex(impl.DriverFollowupError, "current operational publication"):
            self.materialize()
        self.assert_no_packet()

    def test_continuation_requires_explicit_evidence_and_complete_same_task_chain(self):
        newer, path = self.add_continued_destination()
        original = copy.deepcopy(self.spec["current_destination_continuation"])
        for change in ({"rationale": ""}, {"evidence_refs": ["RS-INTEGRATION/TP2-CURRENT"]},
                       {"publication_id": "TP2-EXISTING"}, {"extra": "not permitted"}):
            self.spec["current_destination_continuation"] = {**original, **change}
            with self.subTest(change=change), self.assertRaises(impl.DriverFollowupError):
                self.materialize()
        self.spec["current_destination_continuation"] = original
        for change in ({"supersedes_publication_id": None},
                       {"supersedes_publication_id": "TP2-CURRENT"},
                       {"task_id": "RS-OTHER"}, {"parent_objective_id": "PO-OTHER"}):
            write_json(path, {**newer, **change})
            with self.subTest(change=change), self.assertRaises(impl.DriverFollowupError):
                self.materialize()
        self.assert_no_packet()

    def test_continuation_head_change_during_write_rolls_back_packet(self):
        self.add_continued_destination()
        def drift(packet, root, **kwargs):
            self.current["RS-INTEGRATION"] = {"publication_id": "TP2-LATER"}
            return self.post_audit(packet, root, **kwargs)
        with mock.patch.object(transaction, "_candidate_post_audit", side_effect=drift):
            with self.assertRaisesRegex(transaction.DriverFollowupTransactionError, "current operational publication"):
                self.materialize()
        self.assert_no_packet()

    def test_source_gate_is_available_without_guard_import(self):
        script = "import research_driver_followup as f; assert 'SATISFIED_BY_EXISTING_CONTROL_ASSET' in f.GATE_DECISIONS"
        subprocess.run([sys.executable, "-c", script], check=True, capture_output=True)

    def test_shared_taskbook_path_cannot_substitute_for_historical_bytes(self):
        newer, path = self.add_continued_destination()
        newer["taskbook_path"] = self.asset["taskbook_path"]
        shared = self.root / self.asset["taskbook_path"]
        shared.write_text("# New bytes overwrite old taskbook\n", encoding="utf-8")
        newer["taskbook_blob_sha1"] = research_task_records.taskbook_blob(shared)
        write_json(path, newer)
        with self.assertRaisesRegex(impl.DriverFollowupError, "taskbook blob drift"):
            self.materialize()
        self.assert_no_packet()

    def test_future_or_non_synthesis_route_is_not_accepted(self):
        self.asset["published_at"] = "2027-01-01T00:00:00+00:00"
        write_json(self.asset_path, self.asset)
        with self.assertRaisesRegex(impl.DriverFollowupError, "postdates"):
            self.materialize()
        self.asset["published_at"] = "2026-08-30T00:00:00+00:00"
        write_json(self.asset_path, self.asset)
        self.review["review_authority_kind"] = "IMMUTABLE_REVIEW"
        with self.assertRaisesRegex(impl.DriverFollowupError, "review synthesis"):
            self.materialize()
        self.assert_no_packet()

    def test_first_review_preflight_rejects_synthesis_only_decision(self):
        script = '''
from tools import research_result_records as records
import research_driver_followup as followup
spec = {"decision": followup.EXISTING_ASSET_DECISION, "tasks": [], "gate_decisions": [
    {"gate": gate, "decision": "NOT_REQUIRED", "reason": "fixture"} for gate in followup.GATES]}
try:
    records._preflight_first_review_followup(result={"result_id":"RR-X", "task_id":"RS-X", "publication_id":"TP2-X"},
        driver_id="EM-DVR-TEST123", disposition="CLOSED", destination_class="NONE", spec=spec)
except records.ResultRecordError as exc:
    assert "existing exact-set review synthesis" in str(exc), str(exc)
else:
    raise AssertionError("first-review preflight admitted a synthesis-only decision")
'''
        subprocess.run([sys.executable, "-c", script], check=True, capture_output=True)

    def test_gate_enum_and_evidence_are_intrinsic(self):
        gates = copy.deepcopy(self.spec["gate_decisions"])
        gates[4]["evidence_refs"] = []
        with self.assertRaisesRegex(impl.DriverFollowupError, "evidence_refs"):
            impl._gate_map(gates)


if __name__ == "__main__":
    unittest.main()
