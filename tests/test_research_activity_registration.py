"""Activity bookkeeping boundaries; connector observations below are synthetic fixtures.

No test publishes research, creates a claim, or treats its fixture response as a
real remote readback. The fresh CLI checks use the actual repository entrypoint.
"""
from __future__ import annotations

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from threading import Barrier
from unittest import mock

from tools import research_activity as activity
from tools import research_runtime_guard as runtime_guard

ROOT = Path(__file__).resolve().parents[1]


class ResearchActivityRegistrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="em-activity-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def register(self, session="synthetic-session", mode="FREE_AXIOM_DISCOVERY"):
        return activity.register(root=self.root, session_id=session, mode=mode,
                                 researcher_id="EM-FREE-ABC123")

    def source(self, path="research_notes/synthetic_frontier.md", data="有限观察\n".encode("utf-8")):
        commit = "1" * 40
        pin = {"repository": activity.REPOSITORY, "commit": commit, "path": path,
               "sha256": activity.digest(data)}
        pin["readback"] = {
            "tool_name": "github_fetch_file", "observation_id": "SYNTHETIC_TEST_OBSERVATION",
            "arguments": {"repository_full_name": activity.REPOSITORY, "ref": commit, "path": path},
            "result": {"isError": False, "structuredContent": {
                "content": data.decode("utf-8"), "encoding": "utf-8", "sha": activity.blob_id(data),
                "display_url": f"https://github.com/{activity.REPOSITORY}/blob/{commit}/{path}"}},
        }
        return pin

    def registration_source(self, record):
        path = activity.record_path(record["activity_id"], self.root)
        return self.source(path.relative_to(self.root).as_posix(), path.read_bytes())

    def checkpoint(self, record, event_id, **kwargs):
        return activity.checkpoint(record["activity_id"], root=self.root, event_id=event_id,
            expected_sha256=activity.digest(activity.record_path(record["activity_id"], self.root).read_bytes()),
            **kwargs)

    def guard(self, record, **kwargs):
        session_id = kwargs.pop("session_id", record["session_id"])
        return activity.guard(activity_id=record["activity_id"], root=self.root,
                              session_id=session_id, registration_source=self.registration_source(record), **kwargs)

    def test_fresh_public_cli_gives_registration_action_for_ordinary_unregistered_chat(self):
        result = subprocess.run([sys.executable, "-B", "-X", "utf8",
            str(ROOT.joinpath("tools/research_runtime_guard.py")), "authorize", "--state-json",
            json.dumps({"research_mode": "TASK_RESEARCH", "session_id": "new-direct-chat"})],
            cwd=self.root, capture_output=True, text=True, encoding="utf-8", timeout=30)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        decision = json.loads(result.stdout)
        self.assertEqual(decision["required_action"], "REGISTER_RESEARCH_ACTIVITY")
        self.assertFalse(decision["authorized"])
        self.assertFalse(any(decision["authority"].values()))

    def test_free_phase_a_registers_without_topic_task_catalog_or_claim_and_is_idempotent(self):
        record = self.register()
        before = activity.record_path(record["activity_id"], self.root).read_bytes()
        self.assertEqual(self.register(), record)
        self.assertEqual(activity.record_path(record["activity_id"], self.root).read_bytes(), before)
        self.assertNotIn("topic", record)
        self.assertNotIn("task_id", record)
        self.assertEqual([p.name for p in self.root.iterdir()], [activity.STORE])
        self.assertTrue(self.guard(record)["activity_allowed"])
        self.assertFalse(any(self.guard(record)["authority"].values()))
        local = activity.guard(activity_id=record["activity_id"], session_id=record["session_id"], root=self.root)
        self.assertFalse(local["activity_allowed"])
        self.assertIn("PUBLISH_ACTIVITY_RECORD", local["required_action"])

    def test_cli_register_and_guard_work_in_an_empty_root(self):
        cmd = [sys.executable, "-B", "-X", "utf8", str(ROOT.joinpath("tools/research_activity.py")),
               "--root", str(self.root)]
        result = subprocess.run(cmd + ["register", "--mode", "FREE_AXIOM_DISCOVERY", "--session-id",
            "cli-session", "--researcher-id", "EM-FREE-ABC123"], capture_output=True, text=True,
            encoding="utf-8", timeout=15)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        receipt = json.loads(result.stdout)
        path = self.root.joinpath(receipt["record_path"])
        self.assertEqual(activity.digest(path.read_bytes()), receipt["record_sha256"])
        self.assertNotIn(b"\r", path.read_bytes())
        gate = subprocess.run(cmd + ["guard", "--activity-id", receipt["record"]["activity_id"]],
            capture_output=True, text=True, encoding="utf-8", timeout=15)
        self.assertEqual(gate.returncode, 2)
        self.assertFalse(json.loads(gate.stdout)["activity_allowed"])
        observation = self.root.joinpath("registration-observation.json")
        observation.write_bytes(activity.encoded(self.registration_source(receipt["record"])))
        verified = subprocess.run(cmd + ["guard", "--activity-id", receipt["record"]["activity_id"],
            "--session-id", "cli-session",
            "--registration-json", str(observation)], capture_output=True, text=True,
            encoding="utf-8", timeout=15)
        self.assertEqual(verified.returncode, 0, verified.stdout + verified.stderr)
        self.assertTrue(json.loads(verified.stdout)["activity_allowed"])

    def test_retrospective_registration_keeps_original_session_and_identity_unknown(self):
        kwargs = dict(root=self.root, mode="UNKNOWN_RESEARCH", source_tracking_key="journal/exact-source.md")
        record = activity.register(**kwargs)
        self.assertEqual(record["registration_origin"]["kind"], "RETROSPECTIVE_SOURCE")
        self.assertEqual(record["session_state"], "UNKNOWN")
        self.assertIsNone(record["session_id"])
        self.assertIsNone(record["researcher_id"])
        self.assertEqual(activity.register(**kwargs), record)
        tracked = self.guard(record)
        self.assertFalse(tracked["activity_allowed"])
        self.assertIn("RETROSPECTIVE_TRACKING_ONLY", tracked["required_action"])
        with self.assertRaisesRegex(activity.ActivityError, "cannot invent"):
            activity.register(**kwargs, session_id="invented-old-session")
        with self.assertRaisesRegex(activity.ActivityError, "different or unknown"):
            self.guard(record, session_id="new-live-session")

    def test_registration_collision_cannot_replace_another_session(self):
        record = self.register()
        path = activity.record_path(record["activity_id"], self.root)
        before = path.read_bytes()
        with self.assertRaisesRegex(activity.ActivityError, "collision"):
            activity.register(root=self.root, mode=record["mode"], session_id="other-session",
                researcher_id=record["researcher_id"], activity_id=record["activity_id"])
        self.assertEqual(path.read_bytes(), before)

    def test_checkpoint_rejects_cross_activity_path_identity_drift(self):
        first = self.register("one")
        second = self.register("two")
        path = activity.record_path(first["activity_id"], self.root)
        path.write_bytes(activity.encoded(second))
        before = path.read_bytes()
        with self.assertRaisesRegex(activity.ActivityError, "path/identity mismatch"):
            activity.checkpoint(first["activity_id"], root=self.root, event_id="wrong-session",
                                expected_sha256=activity.digest(before))
        self.assertEqual(path.read_bytes(), before)

    def test_kb_only_is_visible_sync_debt_and_blocks_substantive_final(self):
        record = self.checkpoint(self.register(), "kb-only", kb_sources=["journal/enterprise-math/example.md"])
        decision = self.guard(record, boundary="pre-final", event_id="kb-only")
        self.assertFalse(decision["persistence_allowed"])
        self.assertEqual(decision["required_action"], "PERSIST_EM_CHECKPOINT")
        self.assertEqual(activity.overview(self.root)["items"][0]["sync_debt_events"], ["kb-only"])

    def test_existing_em_branch_source_is_not_mislabelled_as_kb_only_or_main(self):
        record = self.checkpoint(self.register(), "published-source", em_sources=[self.source()],
                                 kb_sources=["journal/enterprise-math/mirror.md"])
        decision = self.guard(record, boundary="checkpoint", event_id="published-source")
        self.assertTrue(decision["persistence_allowed"])
        self.assertEqual(decision["sync_debt_events"], [])
        self.assertIn("VERIFY_CANONICAL_INTAKE", decision["canonical_owner_visibility"])
        verification = record["checkpoints"][0]["em_sources"][0]["verification"]
        self.assertIsNone(verification["call_id"])
        self.assertFalse(verification["network_request_by_this_tool"])
        self.assertFalse(verification["server_signature_authenticated"])

    def test_unknown_publication_and_caller_boolean_do_not_clear_debt(self):
        source = self.source()
        source.pop("readback")
        source["published"] = True
        record = self.checkpoint(self.register(), "unobserved", em_sources=[source])
        self.assertEqual(self.guard(record)["required_action"], "VERIFY_EM_PUBLICATION")
        source["readback"] = {"verified": True}
        with self.assertRaisesRegex(activity.ActivityError, "full github_fetch_file"):
            self.checkpoint(record, "fake-boolean", em_sources=[source])

    def test_no_new_semantic_progress_does_not_invent_a_checkpoint_or_clear_old_debt(self):
        record = self.register()
        decision = self.guard(record, boundary="pre-final", new_semantic_progress=False)
        self.assertTrue(decision["persistence_allowed"])
        self.assertEqual(activity.read(record["activity_id"], self.root)["checkpoints"], [])
        record = self.checkpoint(record, "existing-debt", kb_sources=["journal/x"])
        decision = self.guard(record, boundary="pre-final", new_semantic_progress=False)
        self.assertFalse(decision["persistence_allowed"])
        self.assertEqual(decision["required_action"], "PERSIST_EM_CHECKPOINT")
        with self.assertRaisesRegex(activity.ActivityError, "explicit boolean"):
            self.guard(record, new_semantic_progress="false")

    def test_repair_is_a_new_event_and_keeps_the_original_checkpoint(self):
        record = self.checkpoint(self.register(), "debt", kb_sources=["journal/enterprise-math/missing.md"])
        original_event = copy.deepcopy(record["checkpoints"][0])
        prior_publication = self.registration_source(record)
        record = self.checkpoint(record, "repair", em_sources=[self.source()], repairs_event_id="debt")
        self.assertEqual(record["checkpoints"][0], original_event)
        self.assertEqual(len(record["checkpoints"]), 2)
        self.assertTrue(self.guard(record, boundary="pre-final", event_id="repair")["persistence_allowed"])
        with self.assertRaisesRegex(activity.ActivityError, "current activity bytes"):
            activity.guard(activity_id=record["activity_id"], session_id=record["session_id"],
                           root=self.root, registration_source=prior_publication)
        summary = activity.overview(self.root)["items"][0]
        self.assertEqual(summary["sync_debt_events"], ["debt"])
        self.assertEqual(summary["recorded_repair_events"], [{"event_id": "repair", "repairs_event_id": "debt"}])
        self.assertEqual(summary["required_action"], "VERIFY_RECORDED_DEBT_REPAIR")

    def test_public_live_activity_requires_the_explicit_current_session(self):
        record = self.register("session-A")
        state = {"activity_id": record["activity_id"], "research_mode": record["mode"],
                 "activity_registration_source": self.registration_source(record)}
        omitted = runtime_guard.authorize_execution(state, events=[], root=self.root)
        self.assertFalse(omitted["activity_allowed"])
        self.assertFalse(omitted["persistence_allowed"])
        self.assertEqual(omitted["required_action"], "BIND_CURRENT_RESEARCH_ACTIVITY_SESSION")
        for value in (None, "", " ", 1):
            with self.subTest(session_id=value):
                invalid = runtime_guard.authorize_execution({**state, "session_id": value}, events=[], root=self.root)
                self.assertFalse(invalid["activity_allowed"])
        with self.assertRaisesRegex(runtime_guard.RuntimeAuthorizationError, "different or unknown"):
            runtime_guard.authorize_execution({**state, "session_id": "session-B"}, events=[], root=self.root)
        matched = runtime_guard.authorize_execution({**state, "session_id": "session-A"}, events=[], root=self.root)
        self.assertTrue(matched["activity_allowed"])
        self.assertTrue(matched["persistence_allowed"])
        self.assertFalse(matched["authorized"])

    def test_retrospective_persistence_cannot_grant_public_research_final(self):
        record = activity.register(root=self.root, mode="UNKNOWN_RESEARCH", source_tracking_key="synthetic-historical-activity")
        record = self.checkpoint(record, "past-checkpoint", em_sources=[self.source()])
        liveness = {name: False for name in (
            "parent_objective_complete", "user_requested_stop_pause_review_or_wait", "parent_hard_blocker",
            "platform_or_tool_hard_limit", "independent_safe_work_exhausted", "same_action_repeated_without_state_change",
            "supported_alternative_available", "parent_state_recomputed_without_change")}
        liveness.update(parent_objective_complete=True, executable_next_actions=0)
        result = runtime_guard.pre_final_gate({"activity_id": record["activity_id"],
            "activity_registration_source": self.registration_source(record),
            "research_checkpoint_event_id": "past-checkpoint", "parent_liveness": liveness}, root=self.root)
        self.assertTrue(result["persistence_allowed"])
        self.assertFalse(result["activity_allowed"])
        self.assertFalse(result["final_allowed"])
        self.assertEqual(result["required_action"], "RETROSPECTIVE_TRACKING_ONLY_REGISTER_CURRENT_LIVE_SESSION_TO_RESEARCH")

    def test_unverified_repair_cannot_hide_an_existing_debt(self):
        record = self.checkpoint(self.register(), "old-debt", kb_sources=["journal/old"])
        path = activity.record_path(record["activity_id"], self.root)
        before = path.read_bytes()
        with self.assertRaisesRegex(activity.ActivityError, "observed EM source"):
            self.checkpoint(record, "false-repair", repairs_event_id="old-debt")
        self.assertEqual(path.read_bytes(), before)
        record["checkpoints"].append({"event_id": "false-repair", "em_sources": [], "kb_sources": [],
                                     "state": "SYNC_DEBT", "repairs_event_id": "old-debt"})
        path.write_bytes(activity.encoded(record))
        with self.assertRaisesRegex(activity.ActivityError, "repair must reference"):
            self.guard(record)
        self.assertEqual(activity.overview(self.root)["items"][0]["required_action"], "REPAIR_ACTIVITY_RECORD")

    def test_cas_event_dedup_and_conflict_preserve_history(self):
        record = self.register()
        original_sha = activity.digest(activity.record_path(record["activity_id"], self.root).read_bytes())
        record = self.checkpoint(record, "event", kb_sources=["journal/x"])
        path = activity.record_path(record["activity_id"], self.root)
        before = path.read_bytes()
        retry = activity.checkpoint(record["activity_id"], root=self.root, event_id="event",
            expected_sha256=original_sha, kb_sources=["journal/x"])
        self.assertEqual(retry, record)
        for event_id, journals, error in (("other", ["journal/y"], "expected_sha256"),
                                          ("event", ["journal/y"], "event_id conflict")):
            with self.assertRaisesRegex(activity.ActivityError, error):
                activity.checkpoint(record["activity_id"], root=self.root, event_id=event_id,
                    expected_sha256=original_sha, kb_sources=journals)
        self.assertEqual(path.read_bytes(), before)

    def test_concurrent_distinct_checkpoint_writers_cannot_silently_overwrite(self):
        record = self.register()
        expected = activity.digest(activity.record_path(record["activity_id"], self.root).read_bytes())
        barrier = Barrier(2)
        def write(number):
            barrier.wait(timeout=5)
            try:
                activity.checkpoint(record["activity_id"], root=self.root, event_id=str(number),
                    expected_sha256=expected, kb_sources=[f"journal/{number}"])
                return "written"
            except activity.ActivityError:
                return "conflict"
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(write, (1, 2)))
        self.assertEqual(sorted(results), ["conflict", "written"])
        self.assertEqual(len(activity.read(record["activity_id"], self.root)["checkpoints"]), 1)

    def test_source_pin_content_ref_blob_and_partial_readback_drift_are_rejected(self):
        record = self.register()
        modifications = (
            lambda s: s.update(sha256="0" * 64),
            lambda s: s["readback"]["arguments"].update(ref="main"),
            lambda s: s["readback"]["arguments"].update(start_line=1),
            lambda s: s["readback"]["result"]["structuredContent"].update(sha="0" * 40),
            lambda s: s["readback"]["result"]["structuredContent"].update(content="changed\n"),
            lambda s: s["readback"]["result"].update(isError="false"),
        )
        for index, mutate in enumerate(modifications):
            with self.subTest(index=index):
                source = self.source()
                mutate(source)
                with self.assertRaises(activity.ActivityError):
                    self.checkpoint(record, f"bad-{index}", em_sources=[source])
        self.assertEqual(activity.read(record["activity_id"], self.root)["checkpoints"], [])

    def test_stored_source_observation_or_state_tamper_fails_closed(self):
        record = self.checkpoint(self.register(), "valid", em_sources=[self.source()])
        receipt = self.root.joinpath(record["checkpoints"][0]["em_sources"][0]["verification_receipt"])
        receipt.write_bytes(receipt.read_bytes() + b"\n")
        with self.assertRaisesRegex(activity.ActivityError, "receipt bytes drift"):
            self.guard(record)
        other = self.checkpoint(self.register("other"), "debt", kb_sources=["journal/x"])
        other["checkpoints"][0]["state"] = "EM_REPRESENTED"
        activity.record_path(other["activity_id"], self.root).write_bytes(activity.encoded(other))
        with self.assertRaisesRegex(activity.ActivityError, "derived from actual source"):
            self.guard(other)

    def test_activity_does_not_bypass_task_claim_authority(self):
        record = self.register()
        state = {"task": {"task_id": "RS-NOT-PUBLISHED"}, "activity_id": record["activity_id"],
                 "research_mode": "FREE_AXIOM_DISCOVERY", "activity_registration_source": self.registration_source(record)}
        with self.assertRaises((runtime_guard.RuntimeAuthorizationError, ValueError)):
            runtime_guard.authorize_execution(state, events=[], root=self.root)
        for key in ("task_id", "publication_id", "execution_binding", "execution_record_id"):
            with self.subTest(key=key):
                alias_state = {"activity_id": record["activity_id"], key: "unverified-formal-binding"}
                self.assertFalse(runtime_guard._is_activity_state(alias_state))

    def test_pre_final_requires_current_checkpoint_and_preserves_parent_liveness(self):
        record = self.checkpoint(self.register(), "current", em_sources=[self.source()])
        state = {"activity_id": record["activity_id"], "session_id": record["session_id"],
                 "activity_registration_source": self.registration_source(record)}
        self.assertEqual(runtime_guard.pre_final_gate(state, root=self.root)["required_action"], "RECORD_SEMANTIC_CHECKPOINT")
        state["research_checkpoint_event_id"] = "current"
        state["parent_liveness"] = {name: False for name in (
            "parent_objective_complete", "user_requested_stop_pause_review_or_wait", "parent_hard_blocker",
            "platform_or_tool_hard_limit", "independent_safe_work_exhausted", "same_action_repeated_without_state_change",
            "supported_alternative_available", "parent_state_recomputed_without_change")}
        state["parent_liveness"]["executable_next_actions"] = 1
        self.assertFalse(runtime_guard.pre_final_gate(state, root=self.root)["final_allowed"])
        state["parent_liveness"]["user_requested_stop_pause_review_or_wait"] = True
        self.assertTrue(runtime_guard.pre_final_gate(state, root=self.root)["final_allowed"])
        state["parent_liveness"]["parent_objective_complete"] = True
        self.assertFalse(runtime_guard.pre_final_gate(state, root=self.root)["final_allowed"])

    def test_explicit_nonresearch_roles_do_not_get_relabelled_as_research_activity(self):
        for mode in ("CONTROL_PLANE_MAINTENANCE", "RESEARCH_DRIVER", "FOUNDATION_STEWARD"):
            with self.subTest(mode=mode):
                self.assertFalse(runtime_guard._is_activity_state({"research_mode": mode}))
                with self.assertRaises((runtime_guard.RuntimeAuthorizationError, ValueError)):
                    runtime_guard.authorize_execution({"research_mode": mode}, events=[], root=self.root)

    def test_owner_overview_is_bounded_and_does_not_enter_claim_selection(self):
        first = self.register("one")
        self.checkpoint(first, "debt", kb_sources=["journal/x"])
        self.register("two", mode="TASK_RESEARCH")
        page = activity.overview(self.root, limit=1)
        self.assertTrue(page["has_more"])
        next_page = activity.overview(self.root, limit=1, after=page["next_cursor"])
        self.assertNotEqual(page["items"][0]["activity_id"], next_page["items"][0]["activity_id"])
        self.assertIn("NOT_CLAIM_QUEUE", page["scope"])
        import research_control_dispatch as dispatch
        # Existing selector inputs are held fixed; the actual activity store is
        # read by the real canonical route and must not supply a fresh candidate.
        with mock.patch.object(dispatch.research_dispatch, "effective_states", return_value={}), \
             mock.patch.object(dispatch, "_leased_targets", return_value=[]), \
             mock.patch.object(dispatch, "_fresh_lane", return_value=None), \
             mock.patch.object(dispatch.research_runtime_reducer, "load_policy", return_value={}), \
             mock.patch.object(dispatch.research_runtime_reducer, "select_state", return_value=None), \
             mock.patch.object(dispatch.research_publication_fault_isolation, "validated_quarantines", return_value={}), \
             mock.patch.object(dispatch.research_task_integrity_fault_isolation, "validated_quarantines", return_value={}):
            value = dispatch.route_control([], now=dispatch.datetime.now(dispatch.timezone.utc), root=self.root)
        self.assertEqual(value["action"], dispatch.research_runtime.NO_DISPATCH)
        self.assertEqual(len(value["research_activity_overview"]["items"]), 2)

    def test_owner_overview_reports_metadata_without_replaying_research_sources(self):
        record = self.checkpoint(self.register(), "source", em_sources=[self.source()])
        with mock.patch.object(activity, "verify_observation", side_effect=AssertionError("no source replay in dispatch")):
            summary = activity.overview(self.root)
        self.assertIn("METADATA_ONLY", summary["verification_scope"])
        self.assertEqual(len(summary["items"][0]["source_links"]), 1)
        self.assertEqual(summary["items"][0]["activity_id"], record["activity_id"])


if __name__ == "__main__":
    unittest.main()
