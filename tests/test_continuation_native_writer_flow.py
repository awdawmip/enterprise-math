"""Opt-in full-copy integration fixture; never publishes or evaluates mathematics.

Run EM_FULL_CONTINUATION_FIXTURE=1 python -m unittest
tests.test_continuation_native_writer_flow -v. All comments/claims and the
disposition are synthetic control-test inputs confined to a temporary copy.
"""
import hashlib
import json
import os
import shutil
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SOURCE = "369fcbce4a644c6b7b199b1e8bb7ceaa9825d4ed"
TASK = "RS-EMW59A-JT2-UR-SUN-PARITY-DEFECT"


@unittest.skipUnless(os.environ.get("EM_FULL_CONTINUATION_FIXTURE") == "1", "full isolated Source-copy fixture is opt-in")
class NativeWriterFlowTests(unittest.TestCase):
    def test_governance_driver_claim_checkpoint_and_handoff_without_researcher_activity(self):
        from control_plane import research_control_bootstrap as bootstrap
        from control_plane import research_continuation_writer as writer
        from tools import research_dispatch, research_execution_records, research_runtime_guard, research_task_records
        import research_driver_authority as driver
        from tests.test_research_driver_authority import record as authority_fixture
        with tempfile.TemporaryDirectory(prefix="em-native-governance-fixture-") as temp:
            root = Path(temp) / "source"
            shutil.copytree(REPO, root, ignore=shutil.ignore_patterns(".git", "__pycache__", "TEMP"))
            (root / writer.MARKER).write_text(json.dumps({"schema": "ENTERPRISE_MATH_ISOLATED_WRITE_SANDBOX_V1", "source_commit": SOURCE, "isolated": True}))
            bootstrap.install(root)
            task = "GOV-T6-SHAPE-MOMENT-PERSISTENT-LINE-DRIVER"
            publication = research_task_records.current_records(root)[task]
            self.assertEqual("GOVERNANCE", publication["kind"])
            did, sid = "EM-DVR-FIXGOV", "fixture-governance-session"
            now = datetime.now(timezone.utc)
            body = json.dumps({"schema": driver.EVENT_SCHEMA, "event": "AUTHORIZE", "driver_id": did,
                               "scope": "CONTROL_PLANE", "authority": "RESEARCH_DRIVER", "session_id": sid})
            da = authority_fixture(comment_id=9900000001, created=(now - timedelta(minutes=2)).isoformat())
            da.update(driver_id=did, authority_record_id=driver._record_id(did, "AUTHORIZE", 9900000001),
                      source_body=body, source_body_sha256="sha256:" + hashlib.sha256(body.encode()).hexdigest(),
                      source_server_author={"login": "awdawmip", "user_id": 30957095, "author_association": "OWNER"})
            self.assertEqual([], driver.validate_record(da, root))
            da_path = root / f"research_driver_authority_records/{did}/{da['authority_record_id']}.json"
            da_path.parent.mkdir(parents=True)
            da_path.write_text(json.dumps(da))
            namespace = f"research_artifacts/mcp/{task}/{sid}"
            intent = research_execution_records.prepare_intent(task_id=task, claim_id="fixture-governance-claim",
                researcher_id=did, theorem_owner=publication["owner"], execution_branch="research/fixture-governance",
                execution_branch_base=SOURCE, allowed_outputs=[namespace + "/"], owner_lease_minutes=120,
                prepared_at=(now - timedelta(minutes=1)).isoformat(), root=root)
            intent["executor_role"] = "RESEARCH_DRIVER"
            er_path = root / f"research_execution_records/{task}/{intent['execution_record_id']}.json"
            er_path.parent.mkdir(parents=True)
            er_path.write_text(json.dumps(intent))
            before_activities = set((root / "research_activity_records").glob("*.json"))
            def raw(payload, cid, at):
                return {"id": cid, "body": json.dumps(payload), "created_at": at.isoformat(), "updated_at": at.isoformat(),
                        "issue_url": "https://api.github.com/repos/awdawmip/enterprise-math/issues/240",
                        "user": {"login": "awdawmip", "id": 30957095}, "author_association": "OWNER"}
            event = {"schema": research_dispatch.EVENT_SCHEMA, "event": "CLAIM", "task_id": task,
                     "publication_id": publication["publication_id"], "claim_id": intent["claim_id"],
                     "researcher_id": did, "session_id": sid, "executor_role": "RESEARCH_DRIVER", "lease_minutes": 120}
            comments = [raw(event, 9900000002, now)]
            state = {"task": {"task_id": task}, "task_registration": {}, "research_mode": "RESEARCH_DRIVER",
                     "executor_role": "RESEARCH_DRIVER", "driver_id": did,
                     "owner_claim": {"claim_id": intent["claim_id"], "researcher_id": did}, "session": {"session_id": sid}}
            authorized = research_runtime_guard.authorize_execution(state,
                events=research_dispatch.events_from_github_comments(comments, root=root), now=now, root=root)
            self.assertEqual("RESEARCH_DRIVER", authorized["execution_binding"]["executor_role"])
            with self.assertRaises(research_runtime_guard.RuntimeAuthorizationError):
                research_runtime_guard.authorize_execution({**state, "executor_role": "RESEARCHER", "research_mode": "TASK_RESEARCH"},
                    events=research_dispatch.events_from_github_comments(comments, root=root), now=now, root=root)
            checkpoint = root / namespace / "checkpoint.json"
            checkpoint.parent.mkdir(parents=True)
            checkpoint.write_text(json.dumps({"task_id": task, "executor_role": "RESEARCH_DRIVER", "session_id": sid,
                                              "claim_id": intent["claim_id"], "ownership_epoch": 9900000002}))
            comments.append(raw({**event, "event": "PROGRESS", "progress_ref": "fixture:governance-checkpoint",
                                 "next_action": "fixture handoff"}, 9900000003, now + timedelta(seconds=1)))
            comments.append(raw({**event, "event": "HANDOFF", "handoff_scope": "CONTINUATION",
                                 "progress_ref": "fixture:governance-checkpoint", "next_action": "resume scoped governance from checkpoint"},
                                9900000004, now + timedelta(seconds=2)))
            definition = research_dispatch.registered_definition(publication, root)
            runtime = research_dispatch.reduce_definition(definition, research_dispatch.events_from_github_comments(comments, root=root),
                                                          now=now + timedelta(seconds=3), root=root)
            self.assertEqual("NEEDS_DISPATCH", runtime["dispatch_state"])
            self.assertIsNone(runtime["claim_id"])
            self.assertEqual(before_activities, set((root / "research_activity_records").glob("*.json")))

    def test_new_session_takeover_native_freeze_and_first_driver_review_followup(self):
        from control_plane import research_continuation as continuation
        from control_plane import research_continuation_writer as writer
        from control_plane import research_control_bootstrap as bootstrap
        from tools import research_dispatch, research_execution_records, research_runtime_guard, research_task_records
        import research_driver_authority as driver
        import research_driver_followup as followup
        with tempfile.TemporaryDirectory(prefix="em-native-continuation-fixture-") as temp:
            root = Path(temp) / "source"
            shutil.copytree(REPO, root, ignore=shutil.ignore_patterns(".git", "__pycache__", "TEMP"))
            (root / writer.MARKER).write_text(json.dumps({"schema": "ENTERPRISE_MATH_ISOLATED_WRITE_SANDBOX_V1", "source_commit": SOURCE, "isolated": True}))
            bootstrap.install(root)
            publication = research_task_records.current_records(root)[TASK]
            (root / "EM_SOURCE_BLOBS.json").write_text(json.dumps({"schema": "ENTERPRISE_MATH_SOURCE_BLOB_MANIFEST_V1",
                "source_commit": SOURCE, "blobs": {publication["taskbook_path"]: publication["taskbook_blob_sha1"].removeprefix("sha1:")}}))
            stamp = datetime.now(timezone.utc)
            old_id, new_id, session = "EM-UR-FIXAAA", "EM-UR-FIXBBB", "fixture-new-session"
            base = f"research_artifacts/mcp/{TASK}/{session}"
            report_path = f"{base}/return.md"
            report = root / report_path
            report.parent.mkdir(parents=True)
            report.write_text("# CONTROL FIXTURE ONLY\nSynthetic bounded-return payload; no real mathematical assertion or publication.\n")

            def save(relative, value):
                path = root / relative
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes((json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode())

            def comment(event, cid, at):
                return {"id": cid, "body": json.dumps(event),
                    "issue_url": "https://api.github.com/repos/awdawmip/enterprise-math/issues/240",
                    "url": f"https://api.github.com/repos/awdawmip/enterprise-math/issues/comments/{cid}",
                    "user": {"login": "awdawmip", "id": 30957095}, "author_association": "OWNER",
                    "created_at": at.isoformat(), "updated_at": at.isoformat(), "performed_via_github_app": None}

            old_intent = research_execution_records.prepare_intent(task_id=TASK, claim_id="fixture-old",
                researcher_id=old_id, theorem_owner=publication["owner"], execution_branch="research/fixture-old",
                execution_branch_base=SOURCE, allowed_outputs=[base + "/"], owner_lease_minutes=120,
                prepared_at=(stamp - timedelta(minutes=31)).isoformat(), root=root)
            save(f"research_execution_records/{TASK}/{old_intent['execution_record_id']}.json", old_intent)
            old_claim = {"schema": research_dispatch.EVENT_SCHEMA, "event": "CLAIM", "task_id": TASK,
                "publication_id": publication["publication_id"], "claim_id": "fixture-old", "researcher_id": old_id,
                "session_id": "fixture-old-session", "lease_minutes": 120}
            comments = [comment(old_claim, 990000001, stamp - timedelta(minutes=30))]
            pin = continuation.artifact_pin(root, publication["taskbook_path"], SOURCE)
            frontier = {"source_commit": SOURCE, "artifacts": [pin], "current_unfinished_unit": "fixture controller transition",
                "next_action": "exercise native writer with synthetic control data", "completed_units": [],
                "do_not_repeat": [], "contributor_ids": [old_id]}
            evidence = {"basis": "STALE_SESSION", "previous_session_id": "fixture-old-session",
                "observed_at": (stamp - timedelta(seconds=1)).isoformat(),
                "last_activity_at": (stamp - timedelta(minutes=30)).isoformat(), "source_ref": pin,
                "active_session_confirmed": False}
            prepared = continuation.prepare_takeover(TASK, root=root,
                events=research_dispatch.events_from_github_comments(comments, root=root), now=stamp, source_commit=SOURCE,
                new_researcher_id=new_id, new_session_id=session, new_claim_id="fixture-new",
                execution_branch="research/fixture-new", execution_branch_base=SOURCE, allowed_outputs=[base + "/"],
                expected_previous_claim_id="fixture-old", expected_previous_comment_id=990000001,
                frontier=frontier, reason="Synthetic isolated control test", recovery_evidence=evidence)
            intent = prepared["intent"]
            save(f"research_execution_records/{TASK}/{intent['execution_record_id']}.json", intent)
            continuation.validate_prepared_claim(root=root, events=research_dispatch.events_from_github_comments(comments, root=root),
                now=stamp, source_commit=SOURCE, claim_event=prepared["claim_event"], intent=intent)
            comments.append(comment(prepared["claim_event"], 990000002, stamp))
            state = {"task": {"task_id": TASK}, "task_registration": {},
                     "owner_claim": {"claim_id": "fixture-new", "researcher_id": new_id}, "session": {"session_id": session}}
            events = research_dispatch.events_from_github_comments(comments, root=root)
            self.assertTrue(research_runtime_guard.authorize_execution(state, events=events, now=stamp, root=root)["authorized"])
            old_state = {**state, "owner_claim": {"claim_id": "fixture-old", "researcher_id": old_id}, "session": {"session_id": "fixture-old-session"}}
            with self.assertRaises(research_runtime_guard.RuntimeAuthorizationError):
                research_runtime_guard.authorize_execution(old_state, events=events, now=stamp, root=root)
            checkpoint_path = f"{base}/checkpoint.json"
            save(checkpoint_path, {"task_id": TASK, "claim_id": "fixture-new", "ownership_epoch": 990000002,
                                   "session_id": session, "status": "AUTHOR_REPORTED_CONTROL_FIXTURE"})
            progress = {"schema": research_dispatch.EVENT_SCHEMA, "event": "PROGRESS", "task_id": TASK,
                        "claim_id": "fixture-new", "researcher_id": new_id, "progress_ref": "fixture:checkpoint",
                        "next_action": "fixture freeze"}
            comments.append(comment(progress, 990000003, datetime.now(timezone.utc)))
            payload = {"execution_record_id": intent["execution_record_id"], "return_path": report_path,
                "output_paths": [report_path, checkpoint_path], "owner_head": SOURCE, "terminal_verdict": "PASS",
                "hard_target_disposition": "SATISFIED", "unresolved_residue": "Control fixture only; real parent untouched.",
                "method_harvest": "NO_TOOL_PAYLOAD", "independence_status": "SHARED_AMBIENT_CONTEXT_DISCLOSED",
                "source_exposure_status": "NONBLIND_DISCLOSED", "next_control_plane_recommendation": "fixture independent review"}
            frozen = writer.prepare_freeze(root=root, source_commit=SOURCE, runtime_state=state, raw_comments=comments, payload=payload)
            self.assertIn("write_authorization", frozen["record"])
            self.assertNotIn("progress_ref", frozen["handoff_event_template"])
            result = frozen["record"]

            did, dsid, cid = "EM-DVR-FIXDRV", "fixture-driver-session", 990000004
            authorized = datetime.now(timezone.utc)
            body = json.dumps({"schema": driver.EVENT_SCHEMA, "event": "AUTHORIZE", "driver_id": did,
                               "scope": "CONTROL_PLANE", "authority": "RESEARCH_DRIVER", "session_id": dsid})
            da = {"record_schema": driver.RECORD_SCHEMA, "authority_record_id": driver._record_id(did, "AUTHORIZE", cid),
                  "driver_id": did, "event": "AUTHORIZE", "scope": "CONTROL_PLANE", "authority": "RESEARCH_DRIVER",
                  "source_repository": "awdawmip/enterprise-math", "source_issue": 240, "source_comment_id": cid,
                  "source_issue_url": "https://api.github.com/repos/awdawmip/enterprise-math/issues/240",
                  "source_comment_url": f"https://api.github.com/repos/awdawmip/enterprise-math/issues/comments/{cid}",
                  "source_body": body, "source_body_sha256": "sha256:" + hashlib.sha256(body.encode()).hexdigest(),
                  "source_created_at": authorized.isoformat(), "source_updated_at": authorized.isoformat(),
                  "source_server_author": {"login": "awdawmip", "user_id": 30957095, "author_association": "OWNER"},
                  "server_authenticated": True, "control_authorized": True, "edited": False,
                  "github_app_is_authority": False, "global_knowledge_is_authority": False,
                  "working_truth_granted": False, "foundation_authority_granted": False, "canonical_promotion_granted": False}
            self.assertEqual([], driver.validate_record(da, root))
            save(f"research_driver_authority_records/{did}/{da['authority_record_id']}.json", da)
            review_path = f"research_artifacts/mcp/driver/{dsid}/review.md"
            (root / review_path).parent.mkdir(parents=True)
            (root / review_path).write_text("# CONTROL FIXTURE ONLY\nSynthetic Driver report to test canonical transactions.\n")
            spec = {"decision": followup.TASK_SCOPE_DECISION, "terminal_scope": "TASK", "tasks": [],
                "gate_decisions": [{"gate": gate, "decision": "SATISFIED_BY_REVIEWED_RESULT", "reason": "Control fixture only.",
                                    "evidence_refs": [report_path]} for gate in followup.GATES],
                "portfolio_continuation": {"source_result_id": result["result_id"], "parent_objective_id": publication["parent_objective_id"],
                    "action": "REEVALUATE_CANONICAL_PORTFOLIO", "dispatcher": "research_control_dispatch.py",
                    "next_action": "End this isolated test; no real mathematical conclusion.",
                    "remaining_parent_scope": ["Real project unaffected."], "evidence_refs": [report_path]}}
            reviewed = writer.prepare_review(root=root, source_commit=SOURCE, payload={"result_id": result["result_id"],
                "driver_id": did, "reviewer_session_id": dsid, "reviewer_contribution_ids": [],
                "disposition": "ACCEPTED", "review_path": review_path, "destination_class": "NONE",
                "expected_result_sha256": hashlib.sha256((root / frozen["result_record_path"]).read_bytes()).hexdigest(),
                "followup_spec": spec})
            self.assertIn("write_authorization", reviewed["review"])
            self.assertEqual(2, len(reviewed["files"]))
            self.assertFalse(reviewed["default_successor_generated"])


if __name__ == "__main__":
    unittest.main()
