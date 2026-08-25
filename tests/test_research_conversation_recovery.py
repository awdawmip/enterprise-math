import json
import pathlib
import tempfile
import unittest

from tools import research_scheduler as rs

ROOT = pathlib.Path(__file__).resolve().parents[1]


def task(task_id="RS-STALE"):
    return {
        "task_id": task_id,
        "title": task_id,
        "kind": "RESEARCH",
        "owner": "research/stale-recovery-test",
        "base_state": "READY",
        "priority": "P1",
        "leverage": "HIGH",
        "frontier": "stale conversation recovery regression",
        "next_action": "resume from durable checkpoint",
        "dependencies": [],
        "source_refs": [],
        "last_progress_ref": "seed",
        "last_progress_at": "2026-08-25T11:00:00+08:00",
        "hard_block": None,
    }


def v2(kind, at, **extra):
    event = {
        "schema": rs.V2_SCHEMA,
        "event": kind,
        "task_id": "RS-STALE",
        "at": at,
    }
    event.update(extra)
    return event


class ConversationRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = pathlib.Path(self.tempdir.name)
        (self.root / "research_tasks").mkdir()
        self.config = json.loads((ROOT / "research_scheduler.json").read_text())
        (self.root / "research_scheduler.json").write_text(json.dumps(self.config))
        legacy = {"schema": "ENTERPRISE_MATH_RESEARCH_SCHEDULER_V1", "tasks": []}
        (self.root / "research_scheduler_v1_legacy.json").write_text(json.dumps(legacy))

    def tearDown(self):
        self.tempdir.cleanup()

    def test_policy_contract_freezes_ten_minute_recovery_bridge(self):
        liveness = json.loads((ROOT / "active_turn_liveness.json").read_text())
        control = json.loads((ROOT / "research_control_state_machine.json").read_text())
        scheduler = self.config

        self.assertEqual(10, liveness["cross_conversation_recovery"]["stale_after_minutes_without_verifiable_action"])
        self.assertEqual(10, scheduler["conversation_stale_minutes"])
        self.assertGreater(scheduler["claim_lease_minutes"], scheduler["conversation_stale_minutes"])
        bridge = scheduler["conversation_recovery_contract"]
        self.assertTrue(bridge["stale_preempts_unexpired_claim_lease"])
        self.assertEqual("ORPHAN", bridge["stale_release_event"])
        self.assertEqual("ADOPT", bridge["resume_event"])
        self.assertEqual(
            "STALE_CONVERSATION_NO_VERIFIABLE_ACTION_10M",
            bridge["stale_release_reason"],
        )
        self.assertEqual(
            {
                "VERIFIED_COMPLETE",
                "IN_PROGRESS_RECOVERABLE",
                "UNFINISHED",
                "NEVER_STARTED",
            },
            set(bridge["recovery_classes"]),
        )
        self.assertEqual(
            "ORPHAN",
            control["conversation_recovery_contract"]["scheduler_release_event"],
        )
        self.assertEqual(
            "ADOPT",
            control["conversation_recovery_contract"]["scheduler_resume_event"],
        )
        self.assertIn("conversation", control["state_vector"])

    def test_driver_can_orphan_stale_conversation_before_live_lease_expires_and_adopt(self):
        payload = task()
        events = [
            v2(
                "PUBLISH",
                "2026-08-25T11:00:00+08:00",
                publisher_role="RESEARCH_DRIVER",
                publisher_id="EM-DVR-111AAA",
                task=payload,
                publication_ref="research_tasks/stale.md@abcdef1",
            ),
            v2(
                "REVIEW_CLAIM",
                "2026-08-25T11:01:00+08:00",
                reviewer_id="EM-DVR-222BBB",
                review_claim_id="publish-review",
            ),
            v2(
                "APPROVE",
                "2026-08-25T11:02:00+08:00",
                reviewer_id="EM-DVR-222BBB",
                review_claim_id="publish-review",
                taskbook_ref="research_tasks/stale.md@abcdef1",
                review_ref="reviews/stale.md@abcdef2",
            ),
            v2(
                "CLAIM",
                "2026-08-25T11:03:00+08:00",
                claim_id="claim-old",
                execution_id="EM-RX-ABC123",
                actor_role="RESEARCHER",
                lease_minutes=60,
            ),
            v2(
                "PROGRESS",
                "2026-08-25T11:04:00+08:00",
                claim_id="claim-old",
                execution_id="EM-RX-ABC123",
                progress_ref="research/checkpoint.md@abcdef3",
                next_action="resume exact remaining step",
                lease_minutes=60,
            ),
            v2(
                "ORPHAN",
                "2026-08-25T11:15:00+08:00",
                driver_id="EM-DVR-444DDD",
                reason="STALE_CONVERSATION_NO_VERIFIABLE_ACTION_10M",
                evidence_ref="research/checkpoint.md@abcdef3",
            ),
        ]

        materialized = {
            item["task_id"]: item
            for item in rs.materialize_tasks(self.config, events, root=self.root)
        }
        state = rs.reduce_task(
            materialized["RS-STALE"],
            events,
            config=self.config,
            now=rs.parse_time("2026-08-25T11:16:00+08:00"),
        )

        self.assertEqual("ORPHANED", state["state"])
        self.assertEqual("ORPHAN_RECOVERY", state["dispatch_state"])
        self.assertEqual(
            "STALE_CONVERSATION_NO_VERIFIABLE_ACTION_10M",
            state["orphan_records"][-1]["reason"],
        )
        self.assertEqual(
            "research/checkpoint.md@abcdef3",
            state["orphan_records"][-1]["recovery_ref"],
        )
        self.assertEqual("research/checkpoint.md@abcdef3", state["last_progress_ref"])

        events.append(
            v2(
                "ADOPT",
                "2026-08-25T11:16:00+08:00",
                claim_id="claim-new",
                execution_id="EM-RX-DEF456",
                actor_role="RESEARCHER",
                recovery_ref="research/checkpoint.md@abcdef3",
                lease_minutes=60,
            )
        )
        recovered = rs.reduce_task(
            materialized["RS-STALE"],
            events,
            config=self.config,
            now=rs.parse_time("2026-08-25T11:17:00+08:00"),
        )

        self.assertEqual("CLAIMED", recovered["state"])
        self.assertEqual("LEASED", recovered["dispatch_state"])
        self.assertEqual("claim-new", recovered["claim_id"])
        self.assertEqual("EM-RX-DEF456", recovered["execution_id"])
        self.assertEqual("research/checkpoint.md@abcdef3", recovered["last_progress_ref"])


if __name__ == "__main__":
    unittest.main()
