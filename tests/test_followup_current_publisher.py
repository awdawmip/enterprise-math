import copy
from contextlib import ExitStack
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import research_driver_authority as authority
import research_driver_followup as impl
import research_driver_followup_guard as guard
from control_plane import research_driver_followup_transaction as transaction
from tools import research_task_records


CURRENT = "EM-DVR-NEW123"
ORIGINAL = "EM-DVR-OLD123"
SESSION = "MCP-current-publisher"
CREATED = "2026-09-01T01:00:00+00:00"


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, sort_keys=True), encoding="utf-8")


def authorization(driver=CURRENT, session=SESSION, event="AUTHORIZE", comment=901):
    at = "2026-08-31T00:00:00+00:00" if event == "AUTHORIZE" else "2026-09-02T00:00:00+00:00"
    body = json.dumps({"schema": authority.EVENT_SCHEMA, "event": event,
                       "driver_id": driver, "scope": "CONTROL_PLANE",
                       "authority": "RESEARCH_DRIVER", "session_id": session})
    return {
        "record_schema": authority.RECORD_SCHEMA,
        "authority_record_id": authority._record_id(driver, event, comment),
        "driver_id": driver, "event": event, "scope": "CONTROL_PLANE",
        "authority": "RESEARCH_DRIVER", "source_repository": "awdawmip/enterprise-math",
        "source_issue": 240, "source_comment_id": comment,
        "source_issue_url": "https://api.github.com/repos/awdawmip/enterprise-math/issues/240",
        "source_comment_url": f"https://api.github.com/repos/awdawmip/enterprise-math/issues/comments/{comment}",
        "source_body": body, "source_body_sha256": "sha256:" + hashlib.sha256(body.encode()).hexdigest(),
        "source_created_at": at, "source_updated_at": at,
        "source_server_author": {"login": "owner", "user_id": 7, "author_association": "OWNER"},
        "edited": False, "server_authenticated": True, "control_authorized": True,
        "github_app_is_authority": False, "global_knowledge_is_authority": False,
        "working_truth_granted": False, "foundation_authority_granted": False,
        "canonical_promotion_granted": False,
    }


class CurrentPublisherBindingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        write_json(self.root / authority.CONTRACT, {
            "schema": authority.CONTRACT_SCHEMA, "status": "ACTIVE_CANONICAL",
            "repository": "awdawmip/enterprise-math", "control_issue": 240,
            "source_event_schema": authority.EVENT_SCHEMA, "record_schema": authority.RECORD_SCHEMA,
            "global_knowledge_runtime_authority": False, "github_app_runtime_authority": False,
        })
        write_json(self.root / authority.CONTROL_POLICY, {
            "schema": "ENTERPRISE_MATH_CONTROL_EVENT_AUTHORIZATION_V1", "status": "ACTIVE_CANONICAL",
            "repository": "awdawmip/enterprise-math", "issue": 240,
            "mode": "EXACT_SERVER_AUTHOR_ALLOWLIST",
            "authorized_server_authors": [{"login": "owner", "user_id": 7, "author_association": ["OWNER"]}],
        })
        self.add_authorization(authorization())
        result_path = "research_result_records/RS-OLD/RR-OLD.json"
        write_json(self.root / result_path, {"result_id": "RR-OLD", "task_id": "RS-OLD"})
        self.result = {"result_id": "RR-OLD", "task_id": "RS-OLD", "publication_id": "TP2-OLD",
                       "_record_path": result_path, "next_control_plane_recommendation": "retained recommendation"}
        self.review = {
            "review_id": "DR-OLD", "review_authority_id": "DR-OLD",
            "review_authority_kind": "IMMUTABLE_REVIEW", "source_review_ids": ["DR-OLD"],
            "driver_id": ORIGINAL, "result_id": "RR-OLD", "disposition": "ACCEPTED",
            "destination_class": "NONE", "reviewed_at": "2026-09-01T00:00:00+00:00",
            "result_record_path": result_path,
            "result_record_sha256": "sha256:" + hashlib.sha256((self.root / result_path).read_bytes()).hexdigest(),
            "_record_path": "research_result_reviews/RR-OLD/DR-OLD.json",
        }
        write_json(self.root / self.review["_record_path"], self.review)
        self.patches = [
            mock.patch.object(guard, "authority_map", side_effect=lambda root: {"DR-OLD": copy.deepcopy(self.review)}),
            mock.patch.object(guard, "_immutable_review_map", side_effect=lambda root: {"DR-OLD": copy.deepcopy(self.review)}),
            mock.patch.object(impl, "review_map", side_effect=lambda root: {"DR-OLD": copy.deepcopy(self.review)}),
            mock.patch.object(impl, "result_map", return_value={"RR-OLD": self.result}),
        ]
        for patch in self.patches:
            patch.start()

    def tearDown(self):
        for patch in reversed(self.patches):
            patch.stop()
        self.temp.cleanup()

    def add_authorization(self, record):
        write_json(self.root / authority.RECORD_ROOT / record["driver_id"] /
                   (record["authority_record_id"] + ".json"), record)

    def binding(self, driver=CURRENT, session=SESSION, current=True):
        return impl._materialization_binding("DR-OLD", driver, session, CREATED, self.root,
                                            require_current=current)

    def packet(self):
        gates = [{"gate": gate, "decision": "NOT_REQUIRED", "reason": "fixture", "evidence_refs": []}
                 for gate in impl.GATES]
        with mock.patch.object(impl, "review_requires_followup", return_value=True), \
                mock.patch.object(impl, "_source_parent_objective", return_value="PO-OLD"), \
                mock.patch.object(impl, "_forced_gate_rules"):
            return impl.build_packet(review_id="DR-OLD", decision="PARENT_OBJECTIVE_CLOSURE",
                                     gate_decisions=gates, task_publications=[], driver_id=ORIGINAL,
                                     created_at=CREATED, root=self.root,
                                     publishing_driver_id=CURRENT, publisher_session_id=SESSION)

    def validate(self, packet):
        with mock.patch.object(impl, "review_requires_followup", return_value=True), \
                mock.patch.object(impl, "publication_map", return_value={}), \
                mock.patch.object(impl, "_source_parent_objective", return_value="PO-OLD"), \
                mock.patch.object(impl, "_forced_gate_rules"), \
                mock.patch.object(impl, "_objective_head", return_value={"objective_status": "CLOSED"}):
            impl.validate_packet(packet, self.root)

    def test_new_publisher_is_distinct_from_immutable_review_author(self):
        before = (self.root / self.review["_record_path"]).read_bytes()
        packet = self.packet()
        self.validate(packet)
        self.assertEqual(ORIGINAL, packet["driver_id"])
        self.assertEqual(CURRENT, packet["materialization_publisher"]["driver_id"])
        self.assertEqual(ORIGINAL, packet["materialization_publisher"]["source_review_driver_id"])
        self.assertEqual(before, (self.root / self.review["_record_path"]).read_bytes())

    def test_missing_or_partial_identity_is_rejected(self):
        self.assertIsNone(impl._materialization_binding("DR-OLD", None, None, CREATED, self.root))
        for driver, session in ((CURRENT, None), (None, SESSION), (CURRENT, "")):
            with self.subTest(driver=driver, session=session), self.assertRaises(impl.DriverFollowupError):
                self.binding(driver, session)

    def test_unprivileged_driver_and_forged_server_author_are_rejected(self):
        with self.assertRaises(authority.DriverAuthorityError):
            self.binding("EM-DVR-NOAUTH")
        forged = authorization()
        forged["source_server_author"]["login"] = "outsider"
        self.add_authorization(forged)
        with self.assertRaises(authority.DriverAuthorityError):
            self.binding()

    def test_foreign_session_and_old_actor_impersonation_are_rejected(self):
        with self.assertRaisesRegex(impl.DriverFollowupError, "session"):
            self.binding(session="MCP-other")
        self.add_authorization(authorization(ORIGINAL, "MCP-original-reviewer", comment=902))
        with self.assertRaisesRegex(impl.DriverFollowupError, "session"):
            self.binding(ORIGINAL, SESSION)

    def test_revoked_driver_cannot_backdate_a_new_write(self):
        self.add_authorization(authorization(event="REVOKE", comment=903))
        with self.assertRaises(authority.DriverAuthorityError):
            self.binding()
        self.assertEqual(CURRENT, self.binding(current=False)["driver_id"])

    def test_raw_review_or_exact_review_set_drift_invalidates_packet(self):
        packet = self.packet()
        path = self.root / self.review["_record_path"]
        before = path.read_bytes()
        path.write_bytes(before + b"\n")
        with self.assertRaisesRegex(impl.DriverFollowupError, "binding drift"):
            self.validate(packet)
        path.write_bytes(before)
        self.review["source_review_ids"] = ["DR-OLD", "DR-NEW"]
        with self.assertRaises(impl.DriverFollowupError):
            self.validate(packet)

    def test_result_pin_drift_is_not_rebound_to_new_bytes(self):
        packet = self.packet()
        path = self.root / self.result["_record_path"]
        path.write_bytes(path.read_bytes() + b"\n")
        with self.assertRaisesRegex(impl.DriverFollowupError, "Result bytes"):
            self.validate(packet)

    def test_packet_cannot_relabel_old_review_actor_or_publisher(self):
        packet = self.packet()
        packet["driver_id"] = CURRENT
        with self.assertRaisesRegex(impl.DriverFollowupError, "review Driver"):
            self.validate(packet)
        packet = self.packet()
        packet["materialization_publisher"]["driver_id"] = ORIGINAL
        with self.assertRaises((impl.DriverFollowupError, authority.DriverAuthorityError)):
            self.validate(packet)

    def test_raw_da_record_drift_invalidates_the_publisher_binding(self):
        packet = self.packet()
        path = self.root / packet["materialization_publisher"]["authority_record_path"]
        path.write_bytes(path.read_bytes() + b"\n")
        with self.assertRaisesRegex(impl.DriverFollowupError, "binding drift"):
            self.validate(packet)

    def materialize_fixture(self, *, explicit=True, change_review_during_build=False):
        """Exercise real files/transaction/bindings; isolate task-authoring policy."""
        def publication(meta, *, path, publisher_role, publisher_id, published_at, **kwargs):
            if change_review_during_build:
                review_path = self.root / self.review["_record_path"]
                review_path.write_bytes(review_path.read_bytes() + b"\n")
            return {"record_schema": "ENTERPRISE_MATH_TASK_PUBLICATION_RECORD_V2",
                    "task_id": "RS-NEXT", "publication_id": "TP2-NEXT",
                    "publisher_role": publisher_role, "publisher_id": publisher_id,
                    "published_at": published_at, "parent_objective_id": "PO-OLD",
                    "taskbook_path": path.relative_to(self.root).as_posix(),
                    "taskbook_blob_sha1": research_task_records.taskbook_blob(path)}

        def publications(root):
            return {row["publication_id"]: row for path in (root / "research_task_records").glob("*/*.json")
                    for row in [json.loads(path.read_text(encoding="utf-8"))]}

        def post_audit(packet, root, **kwargs):
            transaction._validate_packet_candidate(packet, root, persisted=True)
            return []

        gates = [{"gate": gate, "decision": "NOT_REQUIRED", "reason": "fixture", "evidence_refs": []}
                 for gate in impl.GATES]
        with ExitStack() as patches:
            for patch in (
                mock.patch.object(impl, "review_requires_followup", return_value=True),
                mock.patch.object(impl, "_source_parent_objective", return_value="PO-OLD"),
                mock.patch.object(impl, "_forced_gate_rules"),
                mock.patch.object(impl, "publication_map", side_effect=publications),
                mock.patch.object(transaction, "_prepared_taskbook_bytes",
                                  return_value=({"task_id": "RS-NEXT"}, b"prepared fixture\n")),
                mock.patch.object(research_task_records, "build_record", side_effect=publication),
                mock.patch.object(research_task_records, "audit", return_value=[]),
                mock.patch.object(transaction, "_candidate_post_audit", side_effect=post_audit),
            ):
                patches.enter_context(patch)
            args = {"publishing_driver_id": CURRENT, "publisher_session_id": SESSION} if explicit else {}
            return transaction.materialize(
                review_id="DR-OLD", created_at=CREATED, root=self.root,
                spec={"decision": "TASK_SET_PUBLISHED", "gate_decisions": gates,
                      "tasks": [{"task_id": "RS-NEXT", "task_role": "OTHER", "research_value": "fixture"}]},
                **args,
            )

    def test_transaction_publishes_as_current_driver_without_reauthoring_review(self):
        review_bytes = (self.root / self.review["_record_path"]).read_bytes()
        packet = self.materialize_fixture()
        pub_path = self.root / "research_task_records/RS-NEXT/TP2-NEXT.json"
        publication = json.loads(pub_path.read_text())
        self.assertEqual(CURRENT, publication["publisher_id"])
        self.assertEqual(ORIGINAL, packet["driver_id"])
        self.assertEqual(CURRENT, packet["materialization_publisher"]["driver_id"])
        self.assertEqual(review_bytes, (self.root / self.review["_record_path"]).read_bytes())

    def test_old_call_keeps_original_publisher_and_packet_shape(self):
        packet = self.materialize_fixture(explicit=False)
        publication = json.loads((self.root / "research_task_records/RS-NEXT/TP2-NEXT.json").read_text())
        self.assertEqual(ORIGINAL, publication["publisher_id"])
        self.assertNotIn("materialization_publisher", packet)

    def test_changed_review_at_write_boundary_rolls_back_only_new_outputs(self):
        path = self.root / self.review["_record_path"]
        review_bytes = path.read_bytes()
        with self.assertRaisesRegex(transaction.DriverFollowupTransactionError, "changed before write"):
            self.materialize_fixture(change_review_during_build=True)
        self.assertFalse((self.root / "research_tasks/RS-NEXT_old.md").exists())
        self.assertFalse((self.root / "research_task_records/RS-NEXT/TP2-NEXT.json").exists())
        self.assertEqual(review_bytes + b"\n", path.read_bytes())


if __name__ == "__main__":
    unittest.main()
